"""Start the same stopped installation inside a Dev Container or Codespace."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'data' / 'installation'


def alive(identity):
    try:
        proc = Path('/proc') / str(identity['pid'])
        return ((proc / 'stat').read_text().rsplit(')', 1)[1].split()[19] == identity['start_time']
                and (proc / 'cwd').resolve() == ROOT
                and (proc / 'cmdline').read_bytes().split(b'\0')[:-1] == [s.encode() for s in identity['argv']]
                and identity['argv'] == [sys.executable, '-m', 'wake.installation', '--data', str(HOME), '--config', str(ROOT / 'wake.toml')])
    except (OSError, KeyError, IndexError):
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('start', 'stop'))
    args = parser.parse_args()
    HOME.mkdir(parents=True, exist_ok=True)
    topics = ROOT / 'research-topics.toml'
    if args.action == 'start' and not topics.exists():
        import shutil
        shutil.copyfile(ROOT / 'example.research-topics.toml', topics)
    identity_file = HOME / 'preview-process.json'
    identity = json.loads(identity_file.read_text()) if identity_file.exists() else None
    if args.action == 'stop':
        if identity and alive(identity):
            os.kill(identity['pid'], signal.SIGTERM)
            deadline = time.monotonic() + 300
            while alive(identity):
                if time.monotonic() >= deadline:
                    raise RuntimeError('Installation is still draining; do not start a second controller')
                time.sleep(0.5)
            identity_file.unlink(missing_ok=True)
        return
    if identity and alive(identity):
        print('WAKE installation already running; use wake-research for controls')
        return
    argv = [sys.executable, '-m', 'wake.installation', '--data', str(HOME), '--config', str(ROOT / 'wake.toml')]
    env = dict(os.environ, WAKE_INSTALLATION_DATA=str(HOME), WAKE_TERMINAL_ROLE='installation')
    with (HOME / 'controller.log').open('ab') as log:
        process = subprocess.Popen(argv, env=env, cwd=ROOT, stdin=subprocess.DEVNULL,
                                   stdout=log, stderr=log, start_new_session=True)
    identity = {'pid': process.pid, 'argv': argv,
                'start_time': (Path('/proc') / str(process.pid) / 'stat').read_text().rsplit(')', 1)[1].split()[19]}
    identity_file.write_text(json.dumps(identity))
    print('WAKE installation launching stopped on forwarded port 8080')


if __name__ == '__main__':
    main()
