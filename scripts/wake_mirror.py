#!/usr/bin/env python3
"""Deliver completed export snapshots with host Git credentials."""
import argparse
from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def container_python(code, *args):
    result = subprocess.run(['docker', 'exec', 'wake', 'python', '-c', code, *args],
                            check=True, capture_output=True, text=True, timeout=60)
    return json.loads(result.stdout)


def delivery_state():
    # Mounted-source execution makes cadence independent of the resident
    # controller version. The host ack file cannot enable a disabled mirror.
    return container_python('''
from pathlib import Path
import json, os, sys
from wake.mirror import exported_identity, delivery_due, interval_seconds, mirror_status
root = Path('/data')
if sys.argv[1]:
    os.environ['WAKE_MIRROR_INTERVAL_SECONDS'] = sys.argv[1]
def read(name):
    path = root / name
    return json.loads(path.read_text()) if path.exists() else {}
config = read('public-mirror.json')
status = mirror_status(root)
status['interval_seconds'] = interval_seconds()
print(json.dumps({'enabled': status['enabled'] and config.get('delivery') == 'host', 'due': delivery_due(status, exported_identity(root)), 'status': status}))
''', os.environ.get('WAKE_MIRROR_INTERVAL_SECONDS', ''))


@contextmanager
def publication_lease():
    # The same installation file lease covers manual, host and in-container
    # publishers through capture AND upload. EOF releases it if the host dies.
    code = '''
from pathlib import Path
import fcntl, sys
with Path('/data/.public-publish.lock').open('a') as lease:
    fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
    print('locked', flush=True)
    sys.stdin.read()
'''
    process = subprocess.Popen(['docker', 'exec', '-i', 'wake', 'python', '-c', code],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    try:
        if process.stdout.readline().strip() != 'locked':
            raise RuntimeError('Another publisher holds the installation lease')
        yield
    finally:
        process.stdin.close()
        process.wait(timeout=15)


def record_delivery(manifest):
    # Record only the artifact actually uploaded. Newer exports remain pending.
    container_python('''
from pathlib import Path
import json, os, sys
from wake.mirror import acknowledge, interval_seconds
from wake.report import atomic_write
root = Path('/data')
if sys.argv[2]:
    os.environ['WAKE_MIRROR_INTERVAL_SECONDS'] = sys.argv[2]
status = {'interval_seconds': interval_seconds()}
acknowledge(status, json.loads(sys.argv[1]))
atomic_write(root / 'public-mirror-host.json', json.dumps(status))
print('{}')
''', json.dumps(manifest), os.environ.get('WAKE_MIRROR_INTERVAL_SECONDS', ''))


def record_failure(exc):
    container_python('''
from pathlib import Path
import json, sys, time
from wake.report import atomic_write
path = Path('/data/public-mirror-host.json')
status = json.loads(path.read_text()) if path.exists() else {}
status.update(status='failed', error=sys.argv[1], retry_at=time.time() + 60)
atomic_write(path, json.dumps(status))
print('{}')
''', type(exc).__name__)


def publish():
    with publication_lease():
        subprocess.run([str(ROOT / 'scripts/wake_publish')], cwd=ROOT, check=True,
                       env={**os.environ, 'WAKE_MIRROR_LEASED': '1'})


def run():
    # One scheduler per checkout. The installation lease also excludes manual
    # uploads and a scheduler launched from another checkout of this source.
    lock = ROOT / 'data/installation/.mirror-host.lock'
    lock.parent.mkdir(parents=True, exist_ok=True)
    with lock.open('a') as lease:
        fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            try:
                state = delivery_state()
                if not state['enabled']:
                    return
                if state['due']:
                    publish()
            except (subprocess.SubprocessError, OSError, ValueError, RuntimeError) as exc:
                print(json.dumps({'mirror_delivery_failed': type(exc).__name__}), flush=True)
                try:
                    record_failure(exc)
                except (subprocess.SubprocessError, OSError, ValueError):
                    pass
            time.sleep(60)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--publish', action='store_true')
    parser.add_argument('--watch', action='store_true')
    parser.add_argument('--record-delivery', type=Path)
    args = parser.parse_args()
    if args.record_delivery:
        record_delivery(json.loads(args.record_delivery.read_text()))
        return
    if args.publish:
        publish()
    if args.watch or not args.publish:
        run()


if __name__ == '__main__':
    main()
