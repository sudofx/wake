"""Bounded standalone worker recovery; never owns or repairs the durable record.

The worker verifies authority and recovers pending invocations before any effect.
The parent only restores execution after a signal or an explicitly temporary exit.
Normal shutdown and configuration/integrity failures remain stopped.
"""
import json
import os
import signal
import subprocess
import threading
import time

TEMPORARY_EXIT = 75


def supervise(command, *, stop=None, retry_delay=2, window_seconds=900, restart_limit=5):
    stop = stop or threading.Event()
    previous = {}
    for sig in (signal.SIGTERM, signal.SIGINT):
        previous[sig] = signal.signal(sig, lambda *_: stop.set())
    restarts = []
    failures = 0
    try:
        while not stop.is_set():
            env = dict(os.environ, WAKE_RUNTIME_CHILD='1')
            process = subprocess.Popen(command, env=env)
            try:
                while process.poll() is None and not stop.wait(.2):
                    pass
            finally:
                if stop.is_set() and process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=300)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
            code = process.wait()
            if stop.is_set() or code == 0:
                return 0
            # An ordinary nonzero exit is an operator/configuration/integrity
            # failure. Retrying it cannot heal source code or grant authority.
            if code != TEMPORARY_EXIT and code >= 0:
                return code
            now = time.monotonic()
            restarts = [at for at in restarts if now - at < window_seconds]
            delay = min(60, retry_delay * 2 ** min(failures, 5))
            if len(restarts) >= restart_limit:
                delay = max(delay, window_seconds - (now - restarts[0]))
            print(json.dumps({'runtime_recovery': 'worker-restart', 'exit_code': code,
                              'retry_after_seconds': round(delay, 3),
                              'boundary': 'record verification and invocation recovery required before effects'}), flush=True)
            if stop.wait(delay):
                return 0
            restarts.append(time.monotonic())
            failures += 1
        return 0
    finally:
        for sig, handler in previous.items():
            signal.signal(sig, handler)
