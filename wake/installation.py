"""One installation lifecycle, one HTTP listener, independently governed nodes.

The controller owns process/control wiring only. Records remain owned by the
existing application and kernel; HTTP serves already exported snapshots.
"""
import argparse
from datetime import datetime, timezone
import fcntl
from functools import partial
from http.server import ThreadingHTTPServer
import json
import os
import queue
from pathlib import Path
import secrets
import shutil
import signal
import socketserver
import subprocess
import sys
import tempfile
import threading
import time
from urllib.parse import unquote, urlsplit

from .installation_gate import InstallationCallCoordinator
from .report import PublicSnapshotHandler, atomic_write

NODE_IDS = tuple(f'{parent + offset}.wake' for parent in (100, 200, 300) for offset in range(4))
ASSETS = Path(__file__).parent / 'assets'


def provider_admitted(mode, member, packet, editorial_nonce=None):
    """Separate explicit reader questions from automatic research admission.

    Packets arrive only through the authenticated internal worker boundary.
    The reader role belongs to the owning worker; it grants no quota exemption.
    STOP still closes reader admission, while PAUSE leaves manual questions usable.
    """
    return (mode == 'running'
            or (mode == 'paused' and member == NODE_IDS[0] and packet.get('purpose') == 'reader')
            or bool(member == NODE_IDS[0] and editorial_nonce
                    and packet.get('editorial_nonce') == editorial_nonce))


def read_json(path, maximum=16_000_000):
    path = Path(path)
    with path.open('rb') as stream:
        raw = stream.read(maximum + 1)
    if len(raw) > maximum:
        raise ValueError('Snapshot exceeds its bounded transport')
    return json.loads(raw)


def worker_runtime(root, name):
    """Read one bounded observation, never an authority or research graph."""
    try:
        runtime = read_json(Path(root) / 'nodes' / name / 'runtime.json', 32768)
        observed = datetime.fromisoformat(runtime['observed_at'])
        if not 0 <= (datetime.now(timezone.utc) - observed).total_seconds() <= 5:
            return {'state': 'unavailable', 'observed_at': runtime['observed_at']}
        return runtime
    except (OSError, ValueError, KeyError, TypeError):
        return {'state': 'unavailable'}


def exported_head(site):
    try:
        with (Path(site) / 'current/head.txt').open() as stream:
            head = stream.read(129).strip()
        # Unified exports use a presentation fingerprint, never a node receipt
        # head. Both bounded forms may notify readers that a view changed.
        identity = head.removeprefix('snapshot:')
        return head if len(identity) == 64 and all(c in '0123456789abcdef' for c in identity) else None
    except OSError:
        return None


def installation_snapshot(root, *, live=True, include_research=True):
    from .installation_cli import _public_projection
    root = Path(root)
    nodes = []
    for name in NODE_IDS:
        base = root / 'nodes' / name
        node = {'id': name, 'role': 'parent' if name[:3].endswith('00') else 'child',
                'parent': None if name[:3].endswith('00') else name[0] + '00.wake',
                'available': False, 'runtime': {'state': 'unavailable'}}
        if include_research:
            try:
                overview = base / 'site/current/installation-overview.json'
                if overview.exists():
                    research = _public_projection(read_json(overview))
                else:
                    from .live import installation_overview
                    research = installation_overview(_public_projection(read_json(base / 'site/current/research-data.json')))
                node.update(available=True, snapshot={k: research.get(k) for k in ('head', 'version', 'generated')},
                            research=research)
            except (OSError, ValueError, TypeError):
                pass
        if live:
            node['runtime'] = worker_runtime(root, name)
        else:
            node['runtime'] = {'state': 'snapshot', 'activity': {'active': False}}
        nodes.append(node)
    identity = read_json(root / 'installation-id.json', 1024)
    return {'schema': 1, 'installation_id': identity['id'], 'generated': datetime.now(timezone.utc).isoformat(),
            'live': live, 'nodes': nodes}


def installation_runtime(snapshot, mode, coordinator):
    """Separate operator intent from fresh worker observations."""
    counts = {}
    for node in snapshot['nodes']:
        state = node.get('runtime', {}).get('state', 'unavailable')
        counts[state] = counts.get(state, 0) + 1
    state, reason = mode, None
    if mode == 'running' and not coordinator.get('active'):
        if len(counts) == 1:
            observed = next(iter(counts))
            if observed in ('waiting', 'standby', 'blocked', 'unavailable'):
                state = observed
                reason = next((n['runtime'].get('reason') for n in snapshot['nodes']
                               if n['runtime'].get('reason')), 'Worker observations unavailable')
    return {'mode': 'installation', 'state': state, 'research': mode,
            'reason': reason, 'worker_states': counts, 'nodes': len(snapshot['nodes']),
            'capabilities': {'live_activity': False}}


class InstallationHTTP(PublicSnapshotHandler):
    def stream_runtime(self):
        controller = self.server.controller
        if not controller.observer_slots.acquire(blocking=False):
            self.send_error(503, 'Observer connection limit reached')
            return
        try:
            self.connection.settimeout(5)
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Accel-Buffering', 'no')
            self.end_headers()
            while not controller.shutdown.is_set():
                body = json.dumps(controller.runtime_snapshot(), separators=(',', ':'))
                self.wfile.write(('data: ' + body + '\n\n').encode())
                self.wfile.flush()
                if controller.shutdown.wait(1):
                    break
        except (OSError, ValueError):
            # A disconnected observer has no effect on workers or provider gates.
            pass
        finally:
            controller.observer_slots.release()
            self.close_connection = True

    def json_response(self, status, packet):
        body = json.dumps(packet, separators=(',', ':')).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(body)

    def do_GET(self):
        route = unquote(urlsplit(self.path).path)
        controller = self.server.controller
        if route == '/installation.json' or route in {f'/nodes/{n}/installation.json' for n in NODE_IDS}:
            packet = controller.installation_manifest()
            packet['coordinator'] = controller.coordinator.status()
            self.json_response(200, packet)
            return
        if route == '/runtime.json':
            self.json_response(200, controller.runtime_snapshot())
            return
        if route == '/runtime.events':
            if self.command == 'HEAD':
                self.json_response(200, {'capability': 'read-only-status-stream'})
            else:
                self.stream_runtime()
            return
        if route.startswith('/nodes/') and route.endswith('/runtime.json'):
            name = route.split('/')[2]
            if name in NODE_IDS:
                packet = worker_runtime(controller.root, name)
                self.json_response(200, packet)
                return
        if route == '/group/bob-inputs.json':
            try:
                inputs = [read_json(controller.root / 'nodes' / n / 'site/current/group/bob-input.json', 16000) for n in NODE_IDS]
                packet = {'schema': 1, 'group_id': 'wake', 'members': list(NODE_IDS), 'leader': NODE_IDS[0], 'inputs': inputs}
                from .group_editorial import validate_inputs
                validate_inputs(packet)
                self.json_response(200, packet)
            except (OSError, ValueError):
                self.json_response(503, {'error': 'Every node snapshot is required'})
            return
        if route == '/group/bob-publication.json':
            try:
                self.json_response(200, read_json(controller.root / 'nodes' / NODE_IDS[0] / 'site/current/group/bob-publication.json', 240000))
            except (OSError, ValueError):
                self.json_response(503, {'error': 'Publication unavailable'})
            return
        if route in ('/', '/index.html', '/console.html') and not (controller.root / 'site/current').exists():
            self.send_error(503, 'The unified website is preparing its first node snapshots')
            return
        super().do_GET()

    def do_HEAD(self):
        self.do_GET()

    def translate_path(self, path):
        route = unquote(urlsplit(path).path)
        parts = route.strip('/').split('/')
        if any(p in ('.', '..') or p.startswith('.') for p in parts):
            return str(ASSETS / '__unavailable__')
        if parts[:1] == ['nodes'] and len(parts) >= 3 and parts[1] in NODE_IDS:
            base = self.server.controller.root / 'nodes' / parts[1] / 'site/current'
            target = base.joinpath(*parts[2:])
            if not target.resolve().is_relative_to(base.resolve()):
                return str(ASSETS / '__unavailable__')
            return str(target)
        base = self.server.controller.root / 'site/current'
        target = base / ('index.html' if route == '/' else route.lstrip('/'))
        if target.resolve().is_relative_to(base.resolve()) and target.is_file():
            return str(target)
        if (len(parts) == 1 and not parts[0].endswith('.html')) or parts[:1] in (['icons'], ['backgrounds']):
            target = ASSETS.joinpath(*parts)
            if target.resolve().is_relative_to(ASSETS.resolve()):
                return str(target)
        return str(ASSETS / '__unavailable__')

    def do_POST(self):
        controller = self.server.controller
        if self.path != '/group/coordinator':
            self.json_response(405, {'error': 'Research management is available only through wake-research'})
            return
        authorization = self.headers.get('Authorization', '')
        if not secrets.compare_digest(authorization, 'Bearer ' + controller.token):
            self.json_response(403, {'error': 'Internal worker access required'})
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 4096:
                raise ValueError('Invalid packet')
            packet = json.loads(self.rfile.read(length))
            member, request_id = packet['member'], packet['request_id']
            if member not in NODE_IDS or not isinstance(request_id, str) or len(request_id) != 32:
                raise ValueError('Invalid identity')
            key = ('wake', member, request_id)
            if packet['action'] == 'acquire':
                if not provider_admitted(controller.mode, member, packet, controller.editorial_nonce):
                    self.json_response(409, {'error': 'Research stopped'})
                    return
                with controller.slot_condition:
                    deadline = time.monotonic() + 5
                    while True:
                        result = controller.coordinator.acquire(key, packet['model'], packet.get('lease_seconds', 120),
                            confirmation_required=packet.get('confirmation_required', False))
                        if (result.get('status') == 'granted' or result.get('reason') not in ('busy', 'fifo')
                                or time.monotonic() >= deadline
                                or not provider_admitted(controller.mode, member, packet, controller.editorial_nonce)):
                            break
                        controller.slot_condition.wait(timeout=max(.01, deadline - time.monotonic()))
                    if result.get('status') == 'granted' and not result.get('confirmation_required'):
                        controller.persist_schedule()
            elif packet['action'] == 'confirm':
                if not provider_admitted(controller.mode, member, packet, controller.editorial_nonce):
                    self.json_response(409, {'error': 'Research stopped'})
                    return
                with controller.slot_condition:
                    confirmed = controller.coordinator.confirm(key, packet['token'])
                    if confirmed:
                        controller.persist_schedule()
                    controller.slot_condition.notify_all()
                result = {'status': 'confirmed' if confirmed else 'expired'}
            elif packet['action'] == 'release':
                with controller.slot_condition:
                    released = controller.coordinator.release(key, packet['token'], packet.get('outcome'),
                        persist=controller.persist_schedule)
                    controller.slot_condition.notify_all()
                result = {'status': 'released' if released else 'expired'}
            elif packet['action'] == 'cancel':
                with controller.slot_condition:
                    controller.coordinator.cancel_request(key)
                    controller.slot_condition.notify_all()
                result = {'status': 'cancelled'}
            else:
                raise ValueError('Unknown action')
            self.json_response(200, result)
        except (KeyError, ValueError, TypeError):
            self.json_response(400, {'error': 'Invalid worker packet'})

    def log_message(self, fmt, *args):
        # Paths may contain operator-controlled query text; do not echo them.
        pass


class OperatorSocket(socketserver.StreamRequestHandler):
    def handle(self):
        try:
            raw = self.rfile.readline(8193)
            if len(raw) > 8192:
                raise ValueError('Command too large')
            packet = json.loads(raw)
            result = self.server.controller.submit(packet)
        except Exception as exc:
            result = {'ok': False, 'error': str(exc)[:300]}
        self.wfile.write((json.dumps(result) + '\n').encode())


class Controller:
    def __init__(self, root, config, provider, port):
        self.root, self.config = Path(root), Path(config).resolve()
        self.provider, self.port = provider, port
        self.workers, self.logs = {}, {}
        self.mode = 'stopped'
        self.editorial_nonce = None
        self.mirror_lock = threading.Lock()
        self.token = secrets.token_urlsafe(32)
        self.coordinator = InstallationCallCoordinator()
        self.command_lock = threading.Lock()
        self.schedule_lock = threading.Lock()
        self.slot_condition = threading.Condition()
        self.shutdown = threading.Event()
        self.commands = queue.Queue(maxsize=32)
        self.site_signature = None
        self.site_lock = threading.RLock()
        self.observer_lock = threading.Lock()
        self.observer_slots = threading.BoundedSemaphore(16)
        self.observer_sample = None
        self.observer_sample_at = 0
        self.manifest_sample = None
        self.root.mkdir(parents=True, exist_ok=True)
        schedule = self.root / 'provider-schedule.json'
        if schedule.exists():
            saved = read_json(schedule, 32768)
            for state in saved.get('models', {}).values():
                if state.get('daily') and state.get('probe_at', 0) <= time.time():
                    state['probe_at'] = time.time() + 300
            self.coordinator.restore_state(saved)
        identity = self.root / 'installation-id.json'
        if not identity.exists():
            atomic_write(identity, json.dumps({'id': secrets.token_hex(16)}))

    def runtime_snapshot(self):
        """Share one bounded sample across local observers for at most a second."""
        with self.observer_lock:
            sampled = time.monotonic()
            if (self.observer_sample is not None and sampled - self.observer_sample_at < 1
                    and self.observer_sample['research'] == self.mode):
                return self.observer_sample
            snapshot = installation_snapshot(self.root, include_research=False)
            result = installation_runtime(snapshot, self.mode, self.coordinator.status())
            fields = ('mode', 'state', 'runtime_id', 'observed_at', 'snapshot_generation', 'activity_schema')
            activity_fields = ('stage', 'active', 'invocation_id', 'coordinate_id', 'started_at')
            members = []
            for node in snapshot['nodes']:
                runtime = node['runtime']
                bounded = {key: runtime[key] for key in fields if key in runtime}
                bounded['capabilities'] = {'live_activity': runtime.get('capabilities', {}).get('live_activity') is True}
                if runtime.get('reason'):
                    bounded['reason'] = str(runtime['reason'])[:300]
                bounded['activity'] = {key: runtime.get('activity', {})[key]
                                      for key in activity_fields if key in runtime.get('activity', {})}
                members.append({'id': node['id'], 'runtime': bounded,
                                'head': exported_head(self.root / 'nodes' / node['id'] / 'site')})
            result.update(members=members, head=exported_head(self.root / 'site'), observed_at=snapshot['generated'])
            result['coordinator'] = self.coordinator.status()
            result['capabilities']['status_stream'] = True
            self.observer_sample, self.observer_sample_at = result, sampled
            return result

    def installation_manifest(self):
        """Serve completed comparison summaries without fanning out to workers."""
        from copy import deepcopy
        packet = deepcopy(self.manifest_sample)
        if packet is None:
            # Cold startup still serves a bounded unavailable observation. The
            # presentation thread fills summaries independently of this request.
            packet = installation_snapshot(self.root, include_research=False)
        observations = {member['id']: member['runtime'] for member in self.runtime_snapshot()['members']}
        packet.update(live=True, generated=datetime.now(timezone.utc).isoformat())
        for node in packet['nodes']:
            node['runtime'] = observations.get(node['id'], {'state': 'unavailable'})
        return packet

    def set_controls(self, mode):
        command_id = secrets.token_hex(16)
        self.mode = mode
        self.editorial_nonce = None
        (self.root / 'nodes' / NODE_IDS[0] / 'record' / '.wake-editorial-request.json').unlink(missing_ok=True)
        with self.slot_condition:
            self.slot_condition.notify_all()
        for name in NODE_IDS:
            record = self.root / 'nodes' / name / 'record'
            record.mkdir(parents=True, exist_ok=True)
            path = record / '.wake-runner-control.json'
            control = read_json(path) if path.exists() else {}
            control.update(research=mode, command_id=command_id)
            atomic_write(path, json.dumps(control))
        return command_id

    def submit(self, packet):
        event, result = threading.Event(), {}
        self.commands.put_nowait((packet, event, result))
        if not event.wait(290):
            return {'ok': False, 'error': 'Command still unresolved; inspect status before retrying'}
        return result

    def persist_schedule(self, state=None):
        if state is None:
            # Match acquire/release's lock order. A release callback already
            # holds the coordinator lock and supplies its detached state.
            with self.slot_condition:
                self.persist_schedule(self.coordinator.dump_state())
            return
        with self.schedule_lock:
            atomic_write(self.root / 'provider-schedule.json', json.dumps(state))

    def refresh_site(self):
        with self.site_lock:
            return self._refresh_site()

    def _refresh_site(self):
        """Publish one full website from attributed node exports, never records."""
        from .installation_projection import build_unified_projection
        from .installation_site import export_unified_site
        generations = {name: (self.root / 'nodes' / name / 'site/current').resolve() for name in NODE_IDS}
        signature = tuple((name, str(path)) for name, path in generations.items())
        if signature == self.site_signature:
            return False
        snapshots, research = {}, {}
        for name in NODE_IDS:
            generation = generations[name]
            try:
                snapshot = read_json(generation / 'wake-data.json')
                view = read_json(generation / 'research-data.json')
                if snapshot['head'] != view['head'] or snapshot['state']['version'] != view['version']:
                    continue
                snapshots[name], research[name] = snapshot, view
            except (OSError, ValueError, KeyError, TypeError):
                continue
        if not snapshots:
            return False
        identity = read_json(self.root / 'installation-id.json')['id']
        projection = build_unified_projection(snapshots, research, identity)
        projection['source']['expected_nodes'] = list(NODE_IDS)
        projection['source']['unavailable_nodes'] = sorted(set(NODE_IDS) - set(snapshots))
        projection['research']['source'] = projection['source']
        site = self.root / 'site'
        site.mkdir(exist_ok=True)
        candidate = Path(tempfile.mkdtemp(prefix='snapshot-', dir=site))
        try:
            export_unified_site(projection, candidate)
            from .installation_site import export_unified_history
            export_unified_history({name: generations[name] for name in snapshots}, snapshots, candidate)
            current = site / 'current'
            previous = current.resolve() if current.exists() else None
            replacement = site / 'next'
            replacement.symlink_to(candidate)
            replacement.replace(current)
            self.site_signature = signature
            from .live import installation_overview
            self.manifest_sample = {'schema': 1, 'installation_id': identity,
                'live': True, 'generated': projection['generated'], 'nodes': [
                    {'id': name, 'role': 'parent' if name[:3].endswith('00') else 'child',
                     'parent': None if name[:3].endswith('00') else name[0] + '00.wake',
                     'available': name in snapshots,
                     **({'snapshot': {key: research[name].get(key) for key in ('head','version','generated')},
                         'research': installation_overview(research[name])} if name in snapshots else {})}
                    for name in NODE_IDS]}
            for old in site.glob('snapshot-*'):
                if old not in (candidate, previous):
                    shutil.rmtree(old)
        except BaseException:
            shutil.rmtree(candidate)
            raise
        return True

    def shared_publication_digest(self):
        from .mirror import exported_identity
        return exported_identity(self.root)['publication_digest']

    def update_public_mirror(self):
        """Queue changed exported heads on cadence, or a new accepted article."""
        path = self.root / 'public-mirror.json'
        if not path.exists():
            return
        with self.mirror_lock:
            from .mirror import exported_identity, delivery_due, acknowledge, interval_seconds, mirror_status
            status = mirror_status(self.root)
            status.setdefault('interval_seconds', interval_seconds())
            current = exported_identity(self.root)
            if not delivery_due(status, current):
                return
            status.update(status='queued', queued_digest=current['publication_digest'],
                          queued_export_digest=current['export_digest'])
            if status.get('delivery') == 'host':
                atomic_write(path, json.dumps(status))
                return
            from .installation_cli import publish_artifact
            status['status'] = 'uploading'
            atomic_write(path, json.dumps(status))
            try:
                manifest = publish_artifact(self.root)
            except Exception as exc:
                status.update(status='failed', error=type(exc).__name__, retry_at=time.time() + 300)
            else:
                acknowledge(status, manifest)
            atomic_write(path, json.dumps(status))

    def spawn(self):
        # Linux parent-death signals bind to the creating thread. Process
        # creation must stay on the controller's main thread, including RESET
        # and import, rather than a short-lived socket handler thread.
        # Every installation launch is inspectable before any provider effect.
        self.set_controls('stopped')
        for name in NODE_IDS:
            base = self.root / 'nodes' / name
            base.mkdir(parents=True, exist_ok=True)
            parent = name[0] + '00.wake'
            peers = [p for p in NODE_IDS if p != name and
                     (p.startswith(name[0]) or (name == parent and p[:3].endswith('00')))]
            url = f'http://127.0.0.1:{self.port}'
            env = dict(os.environ, WAKE_RUNTIME_CHILD='1', WAKE_DEV_RELOAD='false',
                WAKE_INSTALLATION_WORKER='1', WAKE_INSTALLATION_URL=url,
                WAKE_INSTALLATION_SCHEDULE_FILE=str(self.root / 'provider-schedule.json'),
                WAKE_CONTROLLER_PID=str(os.getpid()),
                WAKE_INSTALLATION_TOKEN=self.token, WAKE_GROUP_ID='wake',
                WAKE_GROUP_INSTANCE=name, WAKE_PUBLIC_HOSTNAME=name,
                WAKE_GROUP_PEERS=','.join(peers), WAKE_GROUP_COORDINATOR_URL=url + '/group/coordinator',
                WAKE_PARENT_HOSTNAME='' if name == parent else parent)
            topics = self.config.parent / '.wake-runner-topics' / (parent + '.toml')
            if topics.is_file():
                env['WAKE_GROUP_TOPIC_FILE'] = str(topics)
            log = (base / 'worker.log').open('ab')
            argv = [sys.executable, '-m', 'wake.standalone', '--headless', '--paused',
                '--data', str(base / 'record'), '--config', str(self.config),
                '--site-root', str(base / 'site'), '--runtime-file', str(base / 'runtime.json'),
                '--provider', self.provider, '--interval', '.1']
            process = subprocess.Popen(argv, env=env, stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                                       start_new_session=False)
            self.workers[name], self.logs[name] = process, log

    def terminate(self):
        self.mode = 'stopped'
        for process in self.workers.values():
            if process.poll() is None:
                process.terminate()
        deadline = time.monotonic() + 180
        for name, process in self.workers.items():
            try:
                process.wait(timeout=max(.1, deadline - time.monotonic()))
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            self.coordinator.cancel_member(name)
            self.logs[name].close()
        self.workers.clear()
        self.logs.clear()

    def control(self, mode, timeout=180):
        command_id = self.set_controls(mode)
        pending = set(NODE_IDS)
        acknowledgments = {}
        deadline = time.monotonic() + timeout
        while pending and time.monotonic() < deadline and not self.shutdown.is_set():
            for name in list(pending):
                process = self.workers.get(name)
                if process is None or process.poll() is not None:
                    acknowledgments[name] = {'state': 'failed', 'reason': 'Worker exited'}
                    pending.remove(name)
                    continue
                try:
                    runtime = read_json(self.root / 'nodes' / name / 'runtime.json', 32768)
                    if mode == 'running':
                        done = runtime.get('control_ack') == command_id and runtime.get('state') not in ('paused', 'stopped')
                    else:
                        done = runtime.get('control_ack') == command_id and runtime.get('state') == mode
                    if done:
                        acknowledgments[name] = {'state': 'acknowledged' if mode == 'running' else 'drained'}
                        pending.remove(name)
                except (OSError, ValueError):
                    pass
            if pending:
                time.sleep(.1)
        for name in pending:
            acknowledgments[name] = {'state': 'unknown', 'reason': 'Acknowledgment timed out'}
        return {'ok': not pending and all(v['state'] != 'failed' for v in acknowledgments.values()),
                'research': mode, 'nodes': acknowledgments}

    def command(self, packet):
        from .installation_cli import export_records, import_records, publish_artifact
        with self.command_lock:
            action = packet['action']
            if action == 'status':
                result = installation_snapshot(self.root)
                for node in result['nodes']:
                    node.pop('research', None)
                from .mirror import mirror_status
                result.update(ok=True, research=self.mode, coordinator=self.coordinator.status(),
                    public_mirror=mirror_status(self.root))
                return result
            if action in ('mirror-enable', 'mirror-disable', 'mirror-ack'):
                with self.mirror_lock:
                    path = self.root / 'public-mirror.json'
                    status = read_json(path) if path.exists() else {}
                    if action == 'mirror-enable':
                        from .mirror import interval_seconds
                        status.update(enabled=True, delivery='host', interval_seconds=interval_seconds())
                    elif action == 'mirror-disable':
                        status.update(enabled=False, status='disabled')
                    else:
                        from .governance import require
                        import re
                        require(isinstance(packet.get('digest'), str) and re.fullmatch('[a-f0-9]{64}', packet['digest']), 'Invalid delivered publication digest')
                        if packet.get('export_digest'):
                            from .mirror import acknowledge
                            publication = packet.get('publication_digest')
                            require(publication is None or re.fullmatch('[a-f0-9]{64}', publication), 'Invalid delivered Bob digest')
                            acknowledge(status, {'export_digest': packet['digest'], 'publication_digest': publication})
                        else:
                            # Old publishers acknowledge only Bob; never pretend
                            # that this confirms a later or uncaptured record head.
                            status.update(published_digest=packet['digest'], status='published', retry_at=0,
                                          published_at=datetime.now(timezone.utc).isoformat())
                    atomic_write(path, json.dumps(status))
                return {'ok': True, 'research': self.mode, 'public_mirror': status}
            if action == 'bob':
                self.editorial_nonce = secrets.token_hex(16)
                atomic_write(self.root / 'nodes' / NODE_IDS[0] / 'record' / '.wake-editorial-request.json',
                             json.dumps({'nonce': self.editorial_nonce, **({'revision_reason': packet['revision_reason']} if packet.get('revision_reason') else {})}))
                return {'ok': True, 'research': self.mode, 'editorial': 'queued; bounded by cadence, capacity and provider quota'}
            if action == 'publish':
                with self.mirror_lock:
                    result = publish_artifact(self.root, output=packet.get('output'))
                    if not packet.get('output'):
                        from .mirror import acknowledge, interval_seconds
                        path = self.root / 'public-mirror.json'
                        status = read_json(path) if path.exists() else {}
                        status.update(enabled=True, delivery='controller', interval_seconds=interval_seconds())
                        atomic_write(path, json.dumps(acknowledge(status, result)))
                return {'ok': True, 'research': self.mode, 'publication': {
                    'installation_id': result.get('installation_id'), 'generated': result.get('generated'),
                    'nodes': len(result.get('nodes', [])), 'output': packet.get('output')}}
            if action == 'start':
                if any(p.poll() is not None for p in self.workers.values()):
                    raise ValueError('A worker exited; restart the installation before research')
                if self.provider == 'gemini':
                    key = os.environ.get('GEMINI_API_KEY')
                    filename = os.environ.get('GEMINI_API_KEY_FILE')
                    if key and filename:
                        raise ValueError('Configure either GEMINI_API_KEY or GEMINI_API_KEY_FILE')
                    if filename:
                        key = Path(filename).read_text().strip()
                    if not key:
                        raise ValueError('Configure GEMINI_API_KEY before starting research')
                if self.mode != 'running':
                    drained = self.control('stopped')
                    if not drained['ok']:
                        return drained
                    # Inspection-time edits must reach new worker imports before
                    # the operator's first research effect, without a reset.
                    self.terminate()
                    self.spawn()
                return self.control('running')
            if action in ('stop', 'pause'):
                return self.control('stopped' if action == 'stop' else 'paused')
            if action == 'restart':
                drained = self.control('stopped')
                # Dead owned workers cannot acknowledge drainage. They are safe
                # to reap, but a surviving unacknowledged worker must still stop
                # replacement. terminate() reaps before releasing their grants.
                if not all(
                    drained.get('nodes', {}).get(name, {}).get('state') == 'drained'
                    or (drained.get('nodes', {}).get(name, {}).get('state') == 'failed'
                        and name in self.workers and self.workers[name].poll() is not None)
                    for name in NODE_IDS
                ):
                    return drained
                # Recreate processes to pick up corrected configuration. No reset.
                self.terminate()
                for model, state in self.coordinator.dump_state()['models'].items():
                    if state.get('blocked'):
                        # Explicit restart acknowledges repaired access. Daily
                        # and minute cooldowns survive this administrative step.
                        state.pop('blocked', None)
                        packet = self.coordinator.dump_state()
                        packet['models'][model] = state
                        self.coordinator.restore_state(packet)
                self.persist_schedule()
                self.spawn()
                return self.control('running')
            if action not in ('RESET', 'import', 'export', 'publish'):
                raise ValueError('Unknown research command; RESET must be uppercase')
            drained = self.control('stopped')
            if not drained['ok']:
                return drained
            backups = self.root / 'backups'
            backups.mkdir(exist_ok=True)
            if action == 'export':
                name = packet.get('name') or datetime.now(timezone.utc).strftime('wake-%Y%m%dT%H%M%SZ.zip')
                if Path(name).name != name:
                    raise ValueError('Export must be a filename in data/backups')
                result = export_records(self.root, backups / name)
                return {'ok': True, 'research': 'stopped', 'export': str(backups / name), 'result': result}
            if action == 'import':
                name = packet.get('archive')
                if not isinstance(name, str) or Path(name).name != name:
                    raise ValueError('Choose an archive filename in data/backups')
                from .installation_cli import verify_import
                verify_import(backups / name)
            self.terminate()
            with self.site_lock:
                # Replacement records invalidate comparison observations too.
                # HTTP readers must not retain pre-reset counts while waiting
                # for the independent unified website renderer.
                self.manifest_sample = None
                if action == 'RESET':
                    for directory in ('nodes', 'site'):
                        target = self.root / directory
                        if target.exists():
                            shutil.rmtree(target)
                else:
                    import_records(self.root, backups / name)
                    if (self.root / 'site').exists():
                        shutil.rmtree(self.root / 'site')
                self.site_signature = None
                self.spawn()
                result = self.control('stopped')
                # Control acknowledgement follows each worker's completed
                # export. Prime the small comparison here, never on HTTP reads,
                # without waiting for a full unified-history render.
                self.manifest_sample = installation_snapshot(self.root, live=False)
                return result


def run(args):
    root = Path(args.data).resolve()
    root.mkdir(parents=True, exist_ok=True)
    with (root / 'installation.lock').open('a') as lease:
        fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
        controller = Controller(root, args.config, args.provider, args.port)
        server = ThreadingHTTPServer((args.host, args.port), partial(InstallationHTTP, directory=str(ASSETS)))
        controller.port = server.server_port
        atomic_write(root / 'runtime-endpoint.json', json.dumps({'url': f'http://127.0.0.1:{server.server_port}/runtime.json'}))
        server.controller = controller
        from .installation_cli import control_socket
        socket_path = control_socket(root)
        socket_path.unlink(missing_ok=True)
        control_server = socketserver.ThreadingUnixStreamServer(str(socket_path), OperatorSocket)
        control_server.daemon_threads = True
        control_server.controller = controller
        socket_path.chmod(0o600)
        for sig in (signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, lambda *_: controller.shutdown.set())
        threading.Thread(target=server.serve_forever, daemon=True).start()
        threading.Thread(target=control_server.serve_forever, daemon=True).start()
        try:
            controller.spawn()
            def publish_loop():
                while not controller.shutdown.is_set():
                    try:
                        controller.refresh_site()
                    except Exception as exc:
                        print(json.dumps({'presentation_unavailable': type(exc).__name__}), flush=True)
                    controller.shutdown.wait(1)
            threading.Thread(target=publish_loop, daemon=True).start()
            def mirror_loop():
                while not controller.shutdown.wait(15):
                    try:
                        controller.update_public_mirror()
                    except Exception as exc:
                        print(json.dumps({'public_mirror_unavailable': type(exc).__name__}), flush=True)
            threading.Thread(target=mirror_loop, daemon=True).start()
            print(f'WAKE installation: one server on {controller.port}; twelve internal nodes; research stopped', flush=True)
            while not controller.shutdown.wait(.2):
                try:
                    packet, event, result = controller.commands.get_nowait()
                except queue.Empty:
                    pass
                else:
                    try:
                        result.update(controller.command(packet))
                    except Exception as exc:
                        result.update(ok=False, error=str(exc)[:300])
                    finally:
                        event.set()
                for name, process in controller.workers.items():
                    if process.poll() is not None:
                        controller.coordinator.cancel_member(name)
                # A controller restart is explicit; failed workers remain visible.
        finally:
            controller.shutdown.set()
            controller.terminate()
            server.shutdown()
            server.server_close()
            control_server.shutdown()
            control_server.server_close()
            socket_path.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', default=os.environ.get('WAKE_INSTALLATION_DATA', '/data'))
    parser.add_argument('--config', default=os.environ.get('WAKE_CONFIG', '/app/wake.toml'))
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--provider', choices=('fixture', 'gemini'), default=os.environ.get('WAKE_PROVIDER', 'gemini'))
    args = parser.parse_args()
    run(args)


if __name__ == '__main__':
    main()
