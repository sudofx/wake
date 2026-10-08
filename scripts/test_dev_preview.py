"""Run inside the configured development container; only its isolated record is used.

Exercises the actual lifecycle process rather than mocking readiness, locks or
Linux PID identity. Leaves the paused preview ready; the caller owns container
cleanup. Never run against an operator volume or hosted authority.
"""
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
# Direct script execution adds scripts/, not the checkout, to Python's path.
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location('dev_preview', ROOT / 'scripts/dev_preview.py')
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


def run(*args, expected=0):
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/dev_preview.py'), *args],
                            capture_output=True, text=True, timeout=100)
    assert result.returncode == expected, (result.stdout, result.stderr)
    return result.stdout


def snapshot():
    from wake.record_store import RecordStore
    from wake.authority import verify_existing_record
    verify_existing_record(preview.RECORD / 'wake.sqlite')
    store = RecordStore(preview.RECORD)
    try:
        return store.head(), store.events()
    finally:
        store.close()


def main():
    import wake
    assert Path(wake.__file__).resolve().is_relative_to(ROOT), wake.__file__
    run('start')
    before = snapshot()
    identity = json.loads(preview.PID.read_text())
    assert preview.alive(identity)
    assert not preview.alive({**identity, 'start_time': str(int(identity['start_time']) + 1)})
    run('start')
    assert json.loads(preview.PID.read_text()) == identity
    assert snapshot() == before
    with urllib.request.urlopen('http://127.0.0.1:8080/runtime.json') as response:
        assert json.load(response)['state'] == 'paused'
    with urllib.request.urlopen('http://127.0.0.1:8080/deployment.json') as response:
        assert json.load(response) == {'schema': 1, 'mode': 'standalone'}
    run('start', '--port', '8081', expected=1)
    assert json.loads(preview.PID.read_text()) == identity
    run('stop')
    with socket.socket() as occupied:
        occupied.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        occupied.bind(('0.0.0.0', 8081))
        occupied.listen(1)
        run('start', '--port', '8081', expected=1)
    assert snapshot() == before
    run('start', '--port', '8081')
    with urllib.request.urlopen('http://127.0.0.1:8081/runtime.json') as response:
        assert json.load(response)['state'] == 'paused'
    run('stop')
    run('start')
    assert snapshot() == before
    audit = json.loads(subprocess.check_output([sys.executable, '-m', 'wake', '--data', str(preview.RECORD), 'audit'], cwd=ROOT, text=True))
    assert audit['invocations'] == 0, audit
    print(json.dumps({'source': str(Path(wake.__file__).resolve()), 'record': str(preview.RECORD),
                      'head': before[0], 'paused': True, 'exact_record_preserved': True,
                      'idempotent_launch': True, 'pid_reuse_guard': True, 'port_collision_guard': True}))


if __name__ == '__main__':
    main()
