"""Independent local scheduler and read-only website over WAKE's existing authority."""

import argparse
from datetime import datetime, timezone
import fcntl
from functools import partial
from http.server import ThreadingHTTPServer
import json
import hashlib
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import tempfile
import threading
import time
from types import SimpleNamespace

from .authority import open_authoritative_store, verify_existing_record
from .engine import Engine, config
from .group_peers import collect_group_peer_research, group_bob_snapshot, group_research_snapshot
from .governance import Rejected
from .providers import Fixture, Gemini
from .report import export, PublicSnapshotHandler
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
    pause_at = value.get('pause_at') if isinstance(value, dict) else None
    if pause_at:
        # The deadline is local operational control, never record authority.
        # Invalid or timezone-free deadlines fail closed before another effect.
        deadline = datetime.fromisoformat(pause_at)
        if deadline.tzinfo is None:
            raise ValueError('Research pause_at must include a timezone')
        if datetime.now(timezone.utc) >= deadline and (mode or default) == 'running':
            mode = 'paused'
    return (mode if mode in _RESEARCH_MODES else default,
            reset_id if isinstance(reset_id, str) else None)


def _write_control_ack(directory, reset_id, error=None):
    target = Path(directory) / _CONTROL_ACK_FILE
    temporary = target.with_suffix('.tmp')
    temporary.write_text(json.dumps({'reset_id': reset_id, 'error': error}))
    os.replace(temporary, target)


def _reader_admission_paused(directory, default, stop, handled_reset_id):
    mode, reset_id = _research_control(directory, default)
    return stop.is_set() or mode != 'running' or bool(reset_id and reset_id != handled_reset_id)


def _reader_drain_pending(service, server, mode, reset_id, handled_reset_id):
    """Withhold drainage/reset acknowledgements while the reader owns an effect."""
    pending_reset = bool(reset_id and reset_id != handled_reset_id)
    if service and service.active and (mode != 'running' or pending_reset):
        server.runtime_status = {'mode': 'standalone', 'state': 'draining',
                                 'reason': 'Waiting for the active reader request to finish'}
        return True
    return False


def _pause_after_introduction(directory, state):
    """Consume an operator's group-post pause before the next research effect."""
    target = Path(directory) / _CONTROL_FILE
    try:
        value = json.loads(target.read_text())
    except FileNotFoundError:
        return False
    checkpoint = value.get('pause_after_group_checkpoint')
    if checkpoint is None:
        if value.get('pause_after_group_introduction') is not True:
            return False
        checkpoint = 1
    if isinstance(checkpoint, bool) or not isinstance(checkpoint, int) or checkpoint < 1:
        raise ValueError('Group publication pause requires a positive checkpoint integer')
    # Inactive one-use controls do not need an expensive authority projection.
    state = state() if callable(state) else state
    if state.get('group_bob', {}).get('checkpoint', 0) < checkpoint:
        return False
    value['research'] = 'paused'
    value.pop('pause_after_group_introduction', None)
    value.pop('pause_after_group_checkpoint', None)
    temporary = target.with_suffix('.intro.tmp')
    temporary.write_text(json.dumps(value))
    os.replace(temporary, target)
    return True


def _shared_provider_schedule(filename):
    """A missing/racing observation cannot terminate an owned node.

    This is a wait optimization only. The installation request gate still owns
    permission to send every provider effect, including on a fresh installation.
    """
    path = Path(filename)
    try:
        if not path.exists():
            return {}
        with path.open('rb') as stream:
            raw = stream.read(32769)
        if len(raw) > 32768:
            return None
        packet = json.loads(raw)
        models = packet.get('models') if isinstance(packet, dict) else None
        if not isinstance(models, dict) or any(not isinstance(value, dict) for value in models.values()):
            return None
        return models
    except (OSError, ValueError):
        return None


def _completed_runtime_status(result, schedule=None):
    """Expose terminal outcomes before slow projection reads or website rendering."""
    schedule = schedule or {}
    quota = result.get('quota_exhausted')
    if quota or schedule.get('quota_standby'):
        if quota == 'free_tier_daily' or schedule.get('provider_quota_limited'):
            return {'mode': 'standalone', 'state': 'standby',
                    'reason': 'Provider API quota reported; retrying on the regular schedule'}
        return {'mode': 'standalone', 'state': 'standby',
                'resume_at': schedule.get('quota_standby_until'),
                'reason': 'Configured API request limit reached; research resumes at midnight Pacific time'}
    if result.get('status') == 'failed':
        return {'mode': 'standalone', 'state': 'blocked',
                'reason': result.get('reason', 'Provider failed'),
                'action': 'Review provider configuration and restart'}
    return {'mode': 'standalone', 'state': 'idle'}


def _wait_for_control(stop, directory, seconds, mode, reset_id):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        next_mode, next_reset_id = _research_control(directory, mode)
        if next_mode != mode or next_reset_id != reset_id:
            return False
        if stop.wait(min(.5, max(0, deadline - time.monotonic()))):
            return True
    return False


def bootstrap(directory, settings, *, enable_continuity_matrix=True):
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
            if store.continuity_matrix_progress() is None:
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


class Website(PublicSnapshotHandler):
    """Serve only disposable snapshots, with an inspection-only runtime endpoint."""
    def do_GET(self):
        route = self.path.split('?', 1)[0]
        from urllib.parse import unquote
        if any(part.startswith('.passenger') for part in unquote(route).split('/')):
            self.send_error(404)
            return
        if route in ('/group/bob-input.json', '/group/bob-publication.json',
                     '/group/bob.json', '/group/research.json'):
            if not os.environ.get('WAKE_GROUP_ID') or not os.environ.get('WAKE_GROUP_INSTANCE'):
                self.send_error(404)
                return
            if not Path(self.translate_path(route)).is_file():
                self.send_error(503, 'Group projection is not published yet')
                return
            # Use the same atomic generation as the website. A slow record read
            # must not make every gateway poll queue another reconstruction.
            super().do_GET()
            return
        if route == '/runtime.json':
            status = dict(self.server.runtime_status)
            if getattr(self.server, 'development_status', None):
                status['development'] = dict(self.server.development_status)
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


def _publish(engine, root):
    """Publish the complete local artifact through one atomic generation switch.

    Assets, deployment identity and record views must come from the same export.
    Never replace an individual generated HTML page with its raw asset template;
    that discards installation transforms and may mislabel the displayed record.
    This path performs no provider call and never reads hosted projections.
    """
    target = Path(tempfile.mkdtemp(prefix='snapshot-', dir=root))
    installed = False
    try:
        export(engine.store, target, standalone=True)
        # Readers pin the preceding complete generation while this candidate
        # renders. Only switching and retiring generations require their lease.
        import fcntl
        with (root / '.export.lock').open('a') as lease:
            fcntl.flock(lease, fcntl.LOCK_EX)
            current = root / 'current'
            previous = current.resolve() if current.exists() else None
            link = root / 'next'
            link.symlink_to(target, target_is_directory=True)
            link.replace(current)
            installed = True
            for old in root.glob('snapshot-*'):
                if old not in (target, previous):
                    shutil.rmtree(old)
        from .passenger import record_initial_publication
        record_initial_publication(engine.store.load())
    except Rejected as exc:
        if not installed:
            shutil.rmtree(target)
        if str(exc) == 'Another wake owns this state directory; no call was made':
            return False
        raise
    except BaseException:
        if not installed:
            shutil.rmtree(target)
        raise
    return True


def publish(engine, root):
    # Serialize builders separately; capture never needs to wait for rendering.
    import fcntl
    root = Path(root).resolve()
    with (root / '.export-build.lock').open('a') as lease:
        fcntl.flock(lease, fcntl.LOCK_EX)
        return _publish(engine, root)


def run(args):
    if os.environ.get('WAKE_INSTALLATION_WORKER') == '1':
        # Linux container workers cannot outlive their controller, including
        # SIGKILL. A graceful stop still drains through the normal signal path.
        import ctypes
        expected_parent = int(os.environ['WAKE_CONTROLLER_PID'])
        if ctypes.CDLL(None, use_errno=True).prctl(1, signal.SIGKILL) != 0:
            raise OSError('Cannot bind worker lifecycle to controller')
        if os.getppid() != expected_parent:
            return 1
    if not math.isfinite(args.interval) or args.interval <= 0:
        raise ValueError('Interval must be positive')
    from .runtime_supervisor import (development_root, source_signature,
                                    watch_development_sources, DEVELOPMENT_RELOAD_EXIT)
    source_root = development_root()
    frozen_signature = os.environ.get('WAKE_DEV_SOURCE_SIGNATURE')
    initial_source = (tuple(tuple(item) for item in json.loads(frozen_signature))
                      if source_root and frozen_signature else
                      source_signature(source_root) if source_root else None)
    settings = config(args.config)
    if os.environ.get('WAKE_INSTALLATION_WORKER') == '1':
        settings['provider_managed_limits'] = True
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
    reload_requested = threading.Event() if source_root else None
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda *_: stop.set())
    with (data / 'standalone.lock').open('a') as lease:
        try:
            fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('Another standalone runtime owns this data volume') from None
        engine = bootstrap(data, settings)
        server = None
        reader_service = None
        try:
            from contextlib import nullcontext
            website_context = (nullcontext(args.site_root) if getattr(args, 'site_root', None)
                               else tempfile.TemporaryDirectory(prefix='wake-website-'))
            with website_context as directory:
                root = Path(directory)
                root.mkdir(parents=True, exist_ok=True)
                if not publish(engine, root):
                    raise ValueError('Writer busy during initial website publication; retry startup')
                headless = getattr(args, 'headless', False)
                server = (SimpleNamespace() if headless else
                          ThreadingHTTPServer((args.host, args.port), partial(Website, directory=str(root / 'current'))))
                server.engine = engine
                server.runtime_status = {'mode': 'standalone', 'state': research_mode}
                server.activity = RuntimeActivity()
                if (provider_name == 'gemini' and os.environ.get('WAKE_INSTALLATION_WORKER') == '1'
                        and os.environ.get('WAKE_PUBLIC_HOSTNAME') == '100.wake'):
                    from .reader_questions import ReaderQuestions, ReaderService
                    installation_root = Path(os.environ.get('WAKE_INSTALLATION_DATA', str(data.parents[2])))
                    reader_service = ReaderService(data, ReaderQuestions(
                        engine, settings, installation_root / 'site',
                        should_pause=lambda: _reader_admission_paused(data, default_mode, stop, handled_reset_id)))
                server.snapshot_generation = 1
                server.development_status = ({
                    'enabled': True, 'state': 'watching',
                    'source_root': str(source_root),
                    'imported_root': str(Path(__file__).resolve().parent.parent),
                    'source_signature': hashlib.sha256(json.dumps(initial_source).encode()).hexdigest(),
                } if source_root else None)
                if not headless:
                    thread = threading.Thread(target=server.serve_forever, daemon=True)
                    thread.start()
                print(f'WAKE authority at {data / "wake.sqlite"}; headless={headless}', flush=True)
                if headless:
                    def emit_status():
                        while not stop.is_set():
                            packet = {**server.runtime_status, **server.activity.snapshot(),
                                      'snapshot_generation': server.snapshot_generation}
                            if hasattr(server, 'control_ack'):
                                packet['control_ack'] = server.control_ack
                            target = Path(args.runtime_file)
                            temporary = target.with_suffix('.tmp')
                            temporary.write_text(json.dumps(packet))
                            os.replace(temporary, target)
                            stop.wait(.2)
                    threading.Thread(target=emit_status, daemon=True).start()
                if source_root:
                    threading.Thread(target=watch_development_sources,
                                     args=(source_root, initial_source, stop, reload_requested,
                                           os.environ.get('WAKE_DEV_CONFIG_SOURCE', args.config),
                                           lambda state: server.development_status.update(state=state)),
                                     daemon=True).start()
                last_group_editorial = 0
                paused_group_publication = None
                while not stop.is_set():
                    research_mode, reset_id = _research_control(data, default_mode)
                    if _reader_drain_pending(reader_service, server, research_mode, reset_id, handled_reset_id):
                        stop.wait(.05)
                        continue
                    if os.environ.get('WAKE_GROUP_ID') and time.monotonic() - last_group_editorial >= 15:
                        last_group_editorial = time.monotonic()
                        from .group_editorial import synchronize, fetch, gateway_url
                        try:
                            editorial_provider = None
                            editorial_request_path = data / '.wake-editorial-request.json'
                            editorial_command = json.loads(editorial_request_path.read_text()) if editorial_request_path.exists() else {}
                            editorial_nonce = editorial_command.get('nonce')
                            # Paused observers need a full authority read only when the
                            # shared post changes. This hint never authorizes a write.
                            shared_signature = None
                            if research_mode != 'running' and not editorial_nonce:
                                from .event_format import digest
                                shared_signature = digest(fetch(gateway_url('/group/bob-publication.json')))
                            # A slow unchanged fetch can keep the editorial timer due.
                            # Skip only publication work so control acknowledgments still run.
                            if research_mode == 'running' or editorial_nonce or shared_signature != paused_group_publication:
                                group = engine.store.load().get('group_bob', {})
                                if editorial_command.get('revision_reason') and group.get('last_revision_command') != editorial_nonce:
                                    from .event_format import digest
                                    with engine.store.lock():
                                        group = engine.store.load().get('group_bob', {})
                                        engine.store.append('group_bob_revision_requested', {
                                            'actor': 'operator', 'command_id': editorial_nonce, 'publication_digest': digest(group.get('publication')),
                                            'reason': editorial_command['revision_reason']})
                                if (research_mode == 'running' or editorial_nonce) and group.get('leader') == os.environ.get('WAKE_PUBLIC_HOSTNAME'):
                                    editorial_provider = Fixture(args.model or 'standalone-fixture') if provider_name == 'fixture' else Gemini(settings, args.model)
                                    if provider_name == 'gemini':
                                        from .group_coordinator import group_provider_gate
                                        editorial_provider.request_gate = group_provider_gate(settings, should_pause=lambda: stop.is_set() or (not editorial_request_path.exists() if editorial_nonce else _research_control(data, default_mode)[0] != 'running'))
                                        editorial_provider.request_gate.editorial_nonce = editorial_nonce
                                if synchronize(engine, editorial_provider) and publish(engine, root):
                                    server.snapshot_generation += 1
                                paused_group_publication = shared_signature
                                if editorial_nonce:
                                    editorial_request_path.unlink(missing_ok=True)
                        except Exception as exc:
                            # No partial group, synthetic fallback or concealed
                            # scientific progress when a peer/provider is unavailable.
                            print(f'Group Bob waiting ({type(exc).__name__}): {str(exc)[:180]}', flush=True)
                    if reset_id and reset_id != handled_reset_id:
                        try:
                            with engine.store.lock():
                                engine.store.reset()
                                engine.initialize()
                            paused_group_publication = None
                            if publish(engine, root):
                                server.snapshot_generation += 1
                            handled_reset_id = reset_id
                            _write_control_ack(data, reset_id)
                        except Exception as exc:
                            handled_reset_id = reset_id
                            _write_control_ack(data, reset_id, str(exc))
                    if _pause_after_introduction(data, engine.store.load):
                        research_mode = 'paused'
                    if research_mode != 'running':
                        # The automatic post-introduction pause may have arrived
                        # after the loop's first control read.
                        if _reader_drain_pending(reader_service, server, research_mode, reset_id, handled_reset_id):
                            stop.wait(.05)
                            continue
                        control = json.loads((data / _CONTROL_FILE).read_text()) if (data / _CONTROL_FILE).exists() else {}
                        server.activity.update(stage='idle')
                        server.runtime_status = {'mode': 'standalone', 'state': research_mode,
                                                 'control_ack': control.get('command_id')}
                        server.control_ack = control.get('command_id')
                        stop.wait(.5)
                        continue
                    if headless:
                        server.control_ack = json.loads((data / _CONTROL_FILE).read_text()).get('command_id')
                        if provider_name == 'gemini' and not os.environ.get('GEMINI_API_KEY'):
                            load_secret()
                        schedule_file = os.environ.get('WAKE_INSTALLATION_SCHEDULE_FILE')
                        if provider_name == 'gemini' and schedule_file:
                            models = Gemini(settings, args.model).models
                            shared = _shared_provider_schedule(schedule_file)
                            if shared is None:
                                server.runtime_status = {'mode': 'standalone', 'state': 'waiting',
                                    'reason': 'Shared provider scheduling observation temporarily unavailable'}
                                stop.wait(1)
                                continue
                            now = time.time()
                            eligible = [m for m in models if not shared.get(m, {}).get('blocked') and
                                        max(shared.get(m, {}).get('retry_at', 0), shared.get(m, {}).get('probe_at', 0)) <= now]
                            if not eligible:
                                deadlines = [max(shared.get(m, {}).get('retry_at', 0), shared.get(m, {}).get('probe_at', 0))
                                             for m in models if not shared.get(m, {}).get('blocked')]
                                delay = max(.5, min(deadlines) - now) if deadlines else 300
                                server.runtime_status = {'mode': 'standalone', 'state': 'standby' if deadlines else 'blocked',
                                    'reason': 'Shared provider allowance unavailable' if deadlines else 'Provider access requires operator repair',
                                    'action': None if deadlines else 'Correct provider configuration and restart research'}
                                if _wait_for_control(stop, data, min(delay, 300), research_mode, reset_id):
                                    break
                                continue
                    if (os.environ.get('WAKE_INSTALLATION_WORKER') != '1' and
                        os.environ.get('WAKE_GROUP_ID') and engine.store.load().get('group_bob', {}).get('checkpoint', 0) == 0):
                        # The legacy group inspection workflow awaits its introduction.
                        # Installation research must proceed independently of Bob
                        # availability or publication eligibility.
                        # Children contribute initialized records without making
                        # research requests while this startup objective is pending.
                        server.runtime_status = {'mode':'standalone', 'state':'waiting',
                                                 'reason':'Waiting for the shared WAKE01 introduction'}
                        stop.wait(.5)
                        continue
                    verify_existing_record(data / 'wake.sqlite')
                    state = engine.store.load()
                    daily_limit = (None if os.environ.get('WAKE_INSTALLATION_WORKER') == '1' else
                        None if engine.config.get('model_daily_call_limits')
                        else engine.config['daily_call_limit']
                    )
                    schedule = wake_status(state, daily_call_limit=daily_limit)
                    if os.environ.get('WAKE_INSTALLATION_WORKER') == '1':
                        # The installation queue owns shared provider eligibility;
                        # node-local dated projections cannot impose a second cap.
                        schedule['next_eligible'] = None
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
                    # Keep a provider-quota standby visible while its regular
                    # retry is in flight. Only a provider response can clear
                    # this state; wake_status below observes that response.
                    if schedule.get('provider_quota_limited'):
                        server.runtime_status = {
                            'mode': 'standalone', 'state': 'standby',
                            'reason': 'Provider API quota reported; retrying on the regular schedule',
                        }
                    else:
                        server.runtime_status = {'mode': 'standalone', 'state': 'running'}
                    provider = Fixture(args.model or 'standalone-fixture') if provider_name == 'fixture' else Gemini(settings, args.model)
                    if provider_name == 'gemini':
                        from .group_coordinator import group_provider_gate
                        provider.request_gate = group_provider_gate(
                            settings, should_pause=lambda: stop.is_set() or
                            _research_control(data, default_mode)[0] != 'running')
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
                    # A recorded failure must reach runtime observers before a
                    # potentially slow authority read or derived website build.
                    server.runtime_status = _completed_runtime_status(result)
                    quota_schedule = wake_status(
                        engine.store.load(), daily_call_limit=daily_limit
                    )
                    server.runtime_status = _completed_runtime_status(result, quota_schedule)
                    if publish(engine, root):
                        server.snapshot_generation += 1
                    if quota_schedule.get('quota_standby'):
                        if _wait_for_control(stop, data, args.interval, research_mode, reset_id):
                            break
                        continue
                    if result.get('status') == 'failed':
                        # Known temporary failures return deferred. A failed
                        # provider outcome is not permission for another effect
                        # on every loop (for example an invalid key/model).
                        print(json.dumps(server.runtime_status), flush=True)
                        if _wait_for_control(stop, data, 86400, research_mode, reset_id):
                            break
                        continue
                    if _wait_for_control(stop, data, args.interval, research_mode, reset_id):
                        break
        finally:
            stop.set()
            if reader_service:
                reader_service.close()
            if server and not getattr(args, 'headless', False):
                server.shutdown()
                server.server_close()
            engine.store.close()
    return DEVELOPMENT_RELOAD_EXIT if reload_requested and reload_requested.is_set() else 0


def main():
    # The same parent is used in Docker, Codespaces and a plain process. Child
    # identity is operational only; it never changes record ownership or policy.
    if os.environ.get('WAKE_RUNTIME_CHILD') != '1':
        from .runtime_supervisor import supervise
        return supervise([sys.executable, '-m', 'wake.standalone', *sys.argv[1:]])
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', default='/data')
    parser.add_argument('--headless', action='store_true', help='Internal installation worker; no web listener')
    parser.add_argument('--site-root', help='Disposable node export directory')
    parser.add_argument('--runtime-file', help='Internal redacted activity file')
    parser.add_argument('--config', default='/app/wake.toml')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--interval', type=float, default=float(os.environ.get('WAKE_INTERVAL_SECONDS', '60')))
    parser.add_argument('--provider', choices=('fixture', 'gemini'), default=os.environ.get('WAKE_PROVIDER') or None)
    parser.add_argument('--model', default=os.environ.get('WAKE_MODEL') or None)
    parser.add_argument('--paused', action='store_true', default=os.environ.get('WAKE_PAUSED', '').lower() == 'true')
    parser.add_argument('--enable-continuity-matrix', action='store_true',
                        default=True,
                        help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        return run(args)
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
