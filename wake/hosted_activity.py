"""Best-effort public activity samples; no records, effects, or controls."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import threading
from urllib.request import Request, urlopen

ACTIVITY_ORIGIN = 'https://wake-live-activity.coolgrove68.chatgpt.site'
NODES = tuple(f'{p+i}.wake' for p in (100, 200, 300) for i in range(4))
STATES = {'running','idle','paused','stopped','waiting','standby','blocked','unavailable'}
STAGES = {'idle','record','context','collecting','provider_wait','provider','provider_uncoordinated','provider_response','governance','continuity','receipt'}


def public_sample(packet, installation_id, run_id, revision):
    """Explicit allowlist before any bytes leave the runner. Never copy reasons."""
    members = []
    source = {item.get('id'): item.get('runtime', {}) for item in packet.get('members', [])}
    for node in NODES:
        runtime = source.get(node, {})
        activity = runtime.get('activity', {})
        try:
            age = (datetime.now(timezone.utc) - datetime.fromisoformat(runtime['observed_at'])).total_seconds()
            valid = (0 <= age <= 5 and runtime.get('state') in STATES
                     and activity.get('stage') in STAGES and runtime.get('activity_schema') == 1
                     and runtime.get('capabilities', {}).get('live_activity') is True
                     and runtime.get('mode') == 'standalone'
                     and isinstance(runtime.get('runtime_id'), str)
                     and re.fullmatch(r'[A-Za-z0-9_.:-]{1,100}', runtime['runtime_id']))
        except (KeyError, ValueError, TypeError):
            valid = False
        if not valid:
            bounded = {'state': 'unavailable'}
        else:
            active = runtime['state'] in ('running','standby') and activity.get('active') is True
            bounded = {key: runtime[key] for key in ('mode','state','runtime_id','observed_at','activity_schema')}
            bounded['capabilities'] = {'live_activity': True}
            bounded['activity'] = {'stage': activity['stage'], 'active': active}
            for key, pattern in (('invocation_id', r'w-[0-9a-f]{16}'), ('coordinate_id', r'[A-Za-z0-9_.:-]{1,120}')):
                value = activity.get(key)
                if active and isinstance(value, str) and re.fullmatch(pattern, value):
                    bounded['activity'][key] = value
        members.append({'id': node, 'runtime': bounded})
    coordinator = packet.get('coordinator', {})
    call = coordinator.get('active') or {}
    active = None
    if call.get('confirmed') is True and call.get('member') in NODES:
        active = {'member': call['member'], 'confirmed': True}
        if isinstance(call.get('model'), str) and re.fullmatch(r'[A-Za-z0-9_.:-]{1,100}', call['model']):
            active['model'] = call['model']
    queued = coordinator.get('queued', 0)
    return {'schema': 1, 'installation_id': installation_id, 'run_id': str(run_id),
            'source_revision': revision, 'observed_at': datetime.now(timezone.utc).isoformat(),
            'members': members, 'coordinator': {'active': active,
            'queued': min(12, queued) if type(queued) is int and queued >= 0 else 0}}


class HostedActivityPublisher:
    """One bounded background sampler. Failure never delays research or checkpointing."""
    def __init__(self, root, installation_id, run_id, revision):
        self.root = Path(root)
        self.identity = installation_id, run_id, revision
        self.token = os.environ.get('WAKE_ACTIVITY_INGEST_TOKEN')
        self.closed = threading.Event()
        self.thread = None

    def start(self):
        if self.token:
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def _run(self):
        previous = None
        while not self.closed.is_set():
            try:
                endpoint = json.loads((self.root / 'runtime-endpoint.json').read_text())['url']
                if not re.fullmatch(r'http://127\.0\.0\.1:[0-9]{1,5}/runtime\.json', endpoint):
                    raise ValueError('Invalid local observer')
                with urlopen(endpoint, timeout=2) as response:
                    packet = json.loads(response.read(32769))
                sample = public_sample(packet, *self.identity)
                body = json.dumps(sample, separators=(',', ':')).encode()
                if len(body) > 32768:
                    raise ValueError('Observation too large')
                if self.closed.is_set():
                    return
                request = Request(ACTIVITY_ORIGIN + '/ingest', data=body,
                    headers={'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'})
                with urlopen(request, timeout=3) as response:
                    response.read(1024)
                state = 'connected'
            except Exception:
                state = 'unavailable'
            if state != previous:
                print(json.dumps({'hosted_activity': state}), flush=True)
                previous = state
            self.closed.wait(3)

    def close(self):
        self.closed.set()
