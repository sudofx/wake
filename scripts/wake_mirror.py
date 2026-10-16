#!/usr/bin/env python3
"""Deliver queued Bob exports with host Git credentials; research is untouched."""
import fcntl
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]

def run():
    # One host delivery worker per checkout, including after shell reconnection.
    with (ROOT / 'data/installation/.mirror-host.lock').open('a') as lease:
        fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            try:
                result = subprocess.run(['docker', 'exec', 'wake', 'wake-research', 'status'],
                                        check=True, capture_output=True, text=True, timeout=60)
                status = json.loads(result.stdout).get('public_mirror', {})
                if not status.get('enabled'):
                    return
                if status.get('status') == 'queued':
                    # Complete-history builds can exceed ten minutes. A timeout
                    # here kills only the shell, leaving its capture/upload child
                    # alive while a later retry starts a competing publisher.
                    subprocess.run([str(ROOT / 'scripts/wake_publish')], cwd=ROOT,
                                   check=True)
            except (subprocess.SubprocessError, ValueError) as exc:
                print(json.dumps({'mirror_delivery_failed': type(exc).__name__}), flush=True)
            time.sleep(60)

if __name__ == '__main__':
    run()
