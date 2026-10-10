"""Independent local scheduler and read-only website over WAKE's existing authority."""

import argparse
from datetime import datetime, timezone
import fcntl
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import tempfile
import threading
import time

from .authority import open_authoritative_store, verify_existing_record
from .engine import Engine, config
from .group_peers import collect_group_peer_research, group_bob_snapshot, group_research_snapshot
from .governance import Rejected
from .providers import Fixture, Gemini
from .report import export
from .scheduling import wake_status
from .activity import RuntimeActivity


_CONTROL_FILE = '.wake-runner-control.json'
_CONTROL_ACK_FILE = '.wake-runner-reset-ack.json'
_RESEARCH_MODES = {'running', 'stopped', 'paused'}


def _research_control(directory, default='running'):
    try:
        value = json.loads((Path(directory) / _CONTROL_FILE).read_text())
    except FileNotFoundError:
        return default, None
    mode = value.get('research') if isinstance(value, dict) else None
    reset_id = value.get('reset_id') if isinstance(value, dict) else None
    return (mode if mode in _RESEARCH_MODES else default,
            reset_id if isinstance(reset_id, str) else None)


def _write_control_ack(directory, reset_id, error=None):
    target = Path(directory) / _CONTROL_ACK_FILE
    temporary = target.with_suffix('.tmp')
    temporary.write_text(json.dumps({'reset_id': reset_id, 'error': error}))
    os.replace(temporary, target)


def _wait_for_control(stop, directory, seconds, mode, reset_id):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        next_mode, next_reset_id = _research_control(directory, mode)
        if next_mode != mode or next_reset_id != reset_id:
            return False
        if stop.wait(min(.5, max(0, deadline - time.monotonic()))):
            return True
    return False


def bootstrap(directory, settings, *, enable_continuity_matrix=False):
    """Only a genuinely unused volume may bootstrap; missing prior state is loss."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    # The runner may write its operational control file as soon as Docker starts
    # the container, before this process acquires the lock and initializes a new
    # volume. It is not record authority and must not make that volume look used.
    existing = [p for p in directory.iterdir()
                if p.name not in {'standalone.lock', _CONTROL_FILE}]
    fresh = not existing
    store = open_authoritative_store(directory, allow_initialize=fresh)
    engine = Engine(directory, settings, store=store)
    try:
        with store.lock():
            if fresh:
                engine.initialize()
            else:
                verify_existing_record(directory / 'wake.sqlite')
                state, _, _ = store.replay_record()
                if not state['objective']:
                    raise ValueError('Existing authority is not initialized; refusing automatic bootstrap')
                engine.recover()
            if enable_continuity_matrix and store.continuity_matrix_progress() is None:
                store.enable_continuity_matrix()
            # A local continuity sentinel is not a second record or a state projection.
            marker = directory / '.standalone-initialized'
            if not marker.exists():
                with marker.open('x') as stream:
                    stream.write('Authority: wake.sqlite\n')
                    stream.flush()
                    os.fsync(stream.fileno())
        return engine
    except BaseException:
        store.close()
        raise


def load_secret():
    filename = os.environ.get('GEMINI_API_KEY_FILE')
    if filename:
        if os.environ.get('GEMINI_API_KEY'):
            raise ValueError('Use either GEMINI_API_KEY or GEMINI_API_KEY_FILE')
        secret = Path(filename).read_text().strip()
        if not secret:
            raise ValueError('Gemini secret file is empty')
        os.environ['GEMINI_API_KEY'] = secret


class Website(SimpleHTTPRequestHandler):
    """Serve only disposable snapshots, with an inspection-only runtime endpoint."""
    def do_GET(self):
        route = self.path.split('?', 1)[0]
        if route == '/group/bob.json':
            group_id = os.environ.get('WAKE_GROUP_ID', '')
            instance_id = os.environ.get('WAKE_GROUP_INSTANCE', '')
            if not group_id or not instance_id:
                self.send_error(404)
                return
            try:
                body = json.dumps(group_bob_snapshot(
                    self.server.engine, group_id, instance_id), separators=(',', ':')).encode()
            except (KeyError, ValueError):
                self.send_error(503, 'Group Bob projection unavailable')
                return
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if route == '/group/research.json':
            group_id = os.environ.get('WAKE_GROUP_ID', '')
            instance_id = os.environ.get('WAKE_GROUP_INSTANCE', '')
            if not group_id or not instance_id:
                self.send_error(404)
                return
            try:
                body = json.dumps(group_research_snapshot(
                    self.server.engine, group_id, instance_id), separators=(',', ':')).encode()
            except ValueError:
                self.send_error(503, 'Group research projection unavailable')
                return
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if route == '/runtime.json':
            status = dict(self.server.runtime_status)
            if hasattr(self.server, 'activity'):
                status.update(self.server.activity.snapshot())
                status['snapshot_generation'] = self.server.snapshot_generation
            body = json.dumps(status).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404)
        return None


def publish(engine, root):
    """Publish the complete local artifact through one atomic generation switch.

    Assets, deployment identity and record views must come from the same export.
    Never replace an individual generated HTML page with its raw asset template;
    that discards installation transforms and may mislabel the displayed record.
    This path performs no provider call and never reads hosted projections.
    """
    target = Path(tempfile.mkdtemp(prefix='snapshot-', dir=root))
    try:
        export(engine.store, target, standalone=True)
        current = root / 'current'
        previous = current.resolve() if current.exists() else None
        link = root / 'next'
        link.symlink_to(target, target_is_directory=True)
        link.replace(current)
        # Retain the preceding snapshot for requests already reading it.
        for old in root.glob('snapshot-*'):
            if old not in (target, previous):
                shutil.rmtree(old)
    except Rejected as exc:
        shutil.rmtree(target)
        if str(exc) == 'Another wake owns this state directory; no call was made':
            return False
        raise
    except BaseException:
        shutil.rmtree(target)
        raise
    return True


def run(args):
    if not math.isfinite(args.interval) or args.interval <= 0:
        raise ValueError('Interval must be positive')
    settings = config(args.config)
    provider_name = args.provider or settings['provider']
    if provider_name not in ('fixture', 'gemini'):
        raise ValueError('Standalone unattended providers: fixture or gemini')
    data = Path(args.data).resolve()
    data.mkdir(parents=True, exist_ok=True)
    default_mode = 'paused' if args.paused else 'running'
    research_mode, handled_reset_id = _research_control(data, default_mode)
    try:
        prior_ack = json.loads((data / _CONTROL_ACK_FILE).read_text())
        if prior_ack.get('reset_id') == handled_reset_id:
            handled_reset_id = prior_ack['reset_id']
    except (FileNotFoundError, AttributeError, json.JSONDecodeError):
        pass
    if research_mode == 'running' and provider_name == 'gemini':
        load_secret()
        if not os.environ.get('GEMINI_API_KEY'):
            raise ValueError('Set GEMINI_API_KEY or GEMINI_API_KEY_FILE at runtime')
    stop = threading.Event()
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda *_: stop.set())
    with (data / 'standalone.lock').open('a') as lease:
        try:
            fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('Another standalone runtime owns this data volume') from None
        engine = bootstrap(data, settings, enable_continuity_matrix=args.enable_continuity_matrix)
        server = None
        try:
            with tempfile.TemporaryDirectory(prefix='wake-website-') as directory:
                root = Path(directory)
                if not publish(engine, root):
                    raise ValueError('Writer busy during initial website publication; retry startup')
                server = ThreadingHTTPServer((args.host, args.port), partial(Website, directory=str(root / 'current')))
                server.engine = engine
                server.runtime_status = {'mode': 'standalone', 'state': research_mode}
                server.activity = RuntimeActivity()
                server.snapshot_generation = 1
                thread = threading.Thread(target=server.serve_forever, daemon=True)
                thread.start()
                print(f'Standalone WAKE: /data authority at {data / "wake.sqlite"}; website port {server.server_port}', flush=True)
                while not stop.is_set():
                    research_mode, reset_id = _research_control(data, default_mode)
                    if reset_id and reset_id != handled_reset_id:
                        try:
                            with engine.store.lock():
                                engine.store.reset()
                                engine.initialize()
                            if publish(engine, root):
                                server.snapshot_generation += 1
                            handled_reset_id = reset_id
                            _write_control_ack(data, reset_id)
                        except Exception as exc:
                            handled_reset_id = reset_id
                            _write_control_ack(data, reset_id, str(exc))
                    if research_mode != 'running':
                        server.runtime_status = {'mode': 'standalone', 'state': research_mode}
                        stop.wait(.5)
                        continue
                    verify_existing_record(data / 'wake.sqlite')
                    state = engine.store.load()
                    daily_limit = (
                        None if engine.config.get('model_daily_call_limits')
                        else engine.config['daily_call_limit']
                    )
                    schedule = wake_status(state, daily_call_limit=daily_limit)
                    eligibility = schedule['next_eligible']
                    if eligibility:
                        delay = (datetime.fromisoformat(eligibility) - datetime.now(timezone.utc)).total_seconds()
                        if delay > 0:
                            if schedule.get('quota_standby'):
                                server.runtime_status = {
                                    'mode': 'standalone', 'state': 'standby',
                                    'resume_at': schedule['quota_standby_until'],
                                    'reason': 'API allowance exhausted; research resumes at midnight Pacific time',
                                }
                            else:
                                server.runtime_status = {
                                    'mode': 'standalone', 'state': 'waiting',
                                    'next_eligible': eligibility,
                                }
                            if _wait_for_control(stop, data, min(delay, args.interval), research_mode, reset_id):
                                break
                            continue
                    server.runtime_status = {'mode': 'standalone', 'state': 'running'}
                    provider = Fixture(args.model or 'standalone-fixture') if provider_name == 'fixture' else Gemini(settings, args.model)
                    from .research import collect
                    try:
                        result = engine.run(provider, collector=collect if provider_name == 'gemini' and settings.get('mission') else None,
                                            activity=server.activity.update,
                                            peer_research=collect_group_peer_research())
                    except Rejected as exc:
                        if str(exc) == 'Context ceiling reached; human review required, no model call made':
                            server.runtime_status = {'mode': 'standalone', 'state': 'blocked',
                                                     'reason': str(exc), 'action': 'Review context budget and restart'}
                            print(json.dumps(server.runtime_status), flush=True)
                            # Keep the read-only website available without retrying
                            # an impossible request or spending provider quota.
                            if _wait_for_control(stop, data, 86400, research_mode, reset_id):
                                break
                            continue
                        if str(exc) != 'Another wake owns this state directory; no call was made':
                            raise
                        if _wait_for_control(stop, data, args.interval, research_mode, reset_id):
                            break
                        continue
                    print(json.dumps(result), flush=True)
                    if publish(engine, root):
                        server.snapshot_generation += 1
                    quota_schedule = wake_status(
                        engine.store.load(), daily_call_limit=daily_limit
                    )
                    if quota_schedule.get('quota_standby'):
                        server.runtime_status = {
                            'mode': 'standalone', 'state': 'standby',
                            'resume_at': quota_schedule['quota_standby_until'],
                            'reason': 'API allowance exhausted; research resumes at midnight Pacific time',
                        }
                        continue
                    if result.get('status') == 'failed':
                        # Known temporary failures return deferred. A failed
                        # provider outcome is not permission for another effect
                        # on every loop (for example an invalid key/model).
                        server.runtime_status = {'mode': 'standalone', 'state': 'blocked',
                                                 'reason': result.get('reason', 'Provider failed'),
                                                 'action': 'Review provider configuration and restart'}
                        print(json.dumps(server.runtime_status), flush=True)
                        if _wait_for_control(stop, data, 86400, research_mode, reset_id):
                            break
                        continue
                    server.runtime_status = {'mode': 'standalone', 'state': 'idle'}
                    if _wait_for_control(stop, data, args.interval, research_mode, reset_id):
                        break
        finally:
            if server:
                server.shutdown()
                server.server_close()
            engine.store.close()


def main():
    # The same parent is used in Docker, Codespaces and a plain process. Child
    # identity is operational only; it never changes record ownership or policy.
    if os.environ.get('WAKE_RUNTIME_CHILD') != '1':
        from .runtime_supervisor import supervise
        return supervise([sys.executable, '-m', 'wake.standalone', *sys.argv[1:]])
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', default='/data')
    parser.add_argument('--config', default='/app/wake.toml')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--interval', type=float, default=float(os.environ.get('WAKE_INTERVAL_SECONDS', '60')))
    parser.add_argument('--provider', choices=('fixture', 'gemini'), default=os.environ.get('WAKE_PROVIDER') or None)
    parser.add_argument('--model', default=os.environ.get('WAKE_MODEL') or None)
    parser.add_argument('--paused', action='store_true', default=os.environ.get('WAKE_PAUSED', '').lower() == 'true')
    parser.add_argument('--enable-continuity-matrix', action='store_true',
                        default=os.environ.get('WAKE_ENABLE_CONTINUITY_MATRIX', '').lower() == 'true',
                        help='Durably opt this installation into continuity@1; probes share ordinary provider calls')
    args = parser.parse_args()
    try:
        run(args)
    except Exception as exc:
        # Never print runtime credentials even if an external exception includes them.
        message = str(exc)
        secret = os.environ.get('GEMINI_API_KEY')
        if secret:
            message = message.replace(secret, '[redacted]')
        print(json.dumps({'error': message}), file=sys.stderr)
        # Only temporary OS transport/resource errors are restartable. Invalid
        # records, permissions, configuration and governance stay fail-closed.
        import errno
        from .runtime_supervisor import TEMPORARY_EXIT
        if isinstance(exc, OSError) and exc.errno in {
                errno.EAGAIN, errno.ENOMEM, errno.ETIMEDOUT, errno.ECONNRESET,
                errno.ECONNABORTED, errno.ENETDOWN, errno.ENETUNREACH,
                errno.EHOSTUNREACH}:
            return TEMPORARY_EXIT
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
