"""Independent preview and explicitly enabled research for Dev Containers/Codespaces.

Lifecycle hooks may run more than once. Keep a verified process identity, never
kill a process based only on a reused PID or an occupied port. Development data
lives in the checkout's ignored data directory, outside hosted/local volumes.
"""
import argparse
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PREVIEW_HOME = ROOT / 'data' / 'devcontainer'
RECORD = PREVIEW_HOME / 'record'
PID = PREVIEW_HOME / 'preview.json'


def command(port, research=False):
    return [sys.executable, '-m', 'wake.standalone', '--config', str(ROOT / 'wake.toml'),
            '--data', str(RECORD), '--host', '0.0.0.0', '--port', str(port),
            *(['--provider', 'gemini'] if research else ['--paused', '--provider', 'fixture'])]


def alive(identity):
    """Linux dev containers expose executable arguments and start-time in proc."""
    try:
        # Matching a stored PID/start-time/argv is insufficient if that argv
        # belongs to a foreign process. Only this launcher's canonical command
        # can confer stop or resume authority.
        args = identity['command']
        if not isinstance(args, list):
            return False
        port = int(args[args.index('--port') + 1])
        if not 1 <= port <= 65535 or args != command(port, bool(identity.get('research'))):
            return False
        proc = Path('/proc') / str(identity['pid'])
        # Start-time guards PID reuse even if another identical preview starts.
        fields = (proc / 'stat').read_text().rsplit(')', 1)[1].split()
        return (fields[0] != 'Z' and fields[19] == identity['start_time']
                and (proc / 'cmdline').read_bytes().split(b'\0')[:-1]
                == [arg.encode() for arg in identity['command']]
                and (proc / 'cwd').resolve() == ROOT)
    except (OSError, KeyError, ValueError, IndexError, TypeError):
        return False


def start(port, research=None):
    prior = json.loads(PID.read_text()) if PID.exists() else None
    # Persist explicit research intent across a Codespace/container restart.
    # Stop removes this identity, so the next lifecycle start is paused again.
    research = bool(prior and prior.get('research')) if research is None else research
    if research:
        # Validate before draining a healthy paused preview. Credentials stay in
        # this installation's environment and are never included in its record.
        # Do not load the file into the parent environment: the child owns
        # loading it, and receiving both forms would correctly fail closed.
        filename = os.environ.get('GEMINI_API_KEY_FILE')
        key = os.environ.get('GEMINI_API_KEY')
        if filename and key:
            raise ValueError('Use either GEMINI_API_KEY or GEMINI_API_KEY_FILE')
        if filename:
            key = Path(filename).read_text().strip()
        if not key:
            raise RuntimeError('Configure the Gemini secret before enabling research; existing preview retained')
    if prior and alive(prior) and bool(prior.get('research')) != research:
        stop()
        prior = None
    if prior and alive(prior):
        if prior['command'] != command(port, research):
            raise RuntimeError('Preview is already running with another port; stop it before changing ports')
        print(f'Development runtime already started on port {port}; research={research}')
        return
    # Refuse an occupied port before bootstrapping a new authority. An unrelated
    # process must not masquerade as this installation's successful launch.
    import socket
    with socket.socket() as sock:
        # Match the HTTP server's address reuse: recently closed connections
        # must not block a clean restart, while an active listener still does.
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', port))
    env = dict(os.environ)
    if not research:
        for key in ('GEMINI_API_KEY', 'GEMINI_API_KEY_FILE', 'WAKE_MODEL'):
            env.pop(key, None)
    env.update(WAKE_PAUSED='false' if research else 'true',
               WAKE_PROVIDER='gemini' if research else 'fixture', WAKE_ENABLE_CONTINUITY_MATRIX='false')
    args = command(port, research)
    with (PREVIEW_HOME / 'preview.log').open('ab') as log:
        process = subprocess.Popen(args, cwd=ROOT, env=env, stdin=subprocess.DEVNULL,
                                   stdout=log, stderr=log, start_new_session=True)
    identity = {'pid': process.pid, 'command': args, 'research': research,
                'start_time': (Path('/proc') / str(process.pid) / 'stat').read_text().rsplit(')', 1)[1].split()[19]}
    PID.write_text(json.dumps(identity))
    try:
        deadline = time.monotonic() + 300
        while time.monotonic() < deadline:
            if process.poll() is not None:
                raise RuntimeError('Preview exited; inspect data/devcontainer/preview.log')
            try:
                with urllib.request.urlopen(f'http://127.0.0.1:{port}/runtime.json', timeout=2) as response:
                    status = json.load(response)
                expected = {'running', 'idle', 'waiting'} if research else {'paused'}
                if status['state'] in expected:
                    print(f'Development runtime ready on port {port}; research={research}; record: {RECORD}')
                    return
            except (OSError, ValueError, KeyError):
                time.sleep(.2)
        raise RuntimeError('Preview readiness timed out; inspect data/devcontainer/preview.log')
    except BaseException:
        if alive(identity):
            process.terminate()
            process.wait(timeout=300)
        PID.unlink(missing_ok=True)
        raise


def stop():
    identity = json.loads(PID.read_text()) if PID.exists() else None
    if identity and alive(identity):
        os.kill(identity['pid'], signal.SIGTERM)
        deadline = time.monotonic() + 300
        while alive(identity) and time.monotonic() < deadline:
            time.sleep(.2)
        if alive(identity):
            raise RuntimeError('Preview has not drained; process identity retained for diagnosis')
    PID.unlink(missing_ok=True)
    print('Development preview stopped; record retained')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('start', 'stop', 'research', 'pause'))
    parser.add_argument('--port', type=int, default=8080)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('port must be between 1 and 65535')
    PREVIEW_HOME.mkdir(parents=True, exist_ok=True)
    with (PREVIEW_HOME / 'launcher.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if args.action == 'stop':
            stop()
        else:
            start(args.port, {'research': True, 'pause': False}.get(args.action))


if __name__ == '__main__':
    main()
