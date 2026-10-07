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

from .authority import open_authoritative_store, verify_existing_record
from .engine import Engine, config
from .governance import Rejected
from .providers import Fixture, Gemini
from .report import export
from .scheduling import wake_status


def bootstrap(directory, settings, *, enable_continuity_matrix=False):
    """Only a genuinely unused volume may bootstrap; missing prior state is loss."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    existing = [p for p in directory.iterdir() if p.name != 'standalone.lock']
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
        if self.path.split('?', 1)[0] == '/runtime.json':
            body = json.dumps(self.server.runtime_status).encode()
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
    """Build a complete projection before atomically making it visible."""
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
    if not args.paused and provider_name == 'gemini':
        load_secret()
        if not os.environ.get('GEMINI_API_KEY'):
            raise ValueError('Set GEMINI_API_KEY or GEMINI_API_KEY_FILE at runtime')
    data = Path(args.data).resolve()
    data.mkdir(parents=True, exist_ok=True)
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
                server.runtime_status = {'mode': 'standalone', 'state': 'paused' if args.paused else 'running'}
                thread = threading.Thread(target=server.serve_forever, daemon=True)
                thread.start()
                print(f'Standalone WAKE: /data authority at {data / "wake.sqlite"}; website port {server.server_port}', flush=True)
                while not stop.is_set():
                    if args.paused:
                        stop.wait(args.interval)
                        if not stop.is_set():
                            verify_existing_record(data / 'wake.sqlite')
                            publish(engine, root)
                        continue
                    verify_existing_record(data / 'wake.sqlite')
                    state = engine.store.load()
                    eligibility = wake_status(state, daily_call_limit=None)['next_eligible']
                    if eligibility:
                        delay = (datetime.fromisoformat(eligibility) - datetime.now(timezone.utc)).total_seconds()
                        if delay > 0:
                            server.runtime_status = {'mode': 'standalone', 'state': 'waiting', 'next_eligible': eligibility}
                            stop.wait(min(delay, args.interval))
                            continue
                    server.runtime_status = {'mode': 'standalone', 'state': 'running'}
                    provider = Fixture(args.model or 'standalone-fixture') if provider_name == 'fixture' else Gemini(settings, args.model)
                    from .research import collect
                    try:
                        result = engine.run(provider, collector=collect if provider_name == 'gemini' and settings.get('mission') else None)
                    except Rejected as exc:
                        if str(exc) != 'Another wake owns this state directory; no call was made':
                            raise
                        stop.wait(args.interval)
                        continue
                    print(json.dumps(result), flush=True)
                    publish(engine, root)
                    stop.wait(args.interval)
        finally:
            if server:
                server.shutdown()
                server.server_close()
            engine.store.close()


def main():
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
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
