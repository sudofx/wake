"""Bounded standalone worker recovery; never owns or repairs the durable record.

The worker verifies authority and recovers pending invocations before any effect.
The parent only restores execution after a signal or an explicitly temporary exit.
Normal shutdown and configuration/integrity failures remain stopped.
"""
import json
from contextlib import contextmanager, ExitStack
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import threading
import time
import tempfile
import tomllib

TEMPORARY_EXIT = 75
DEVELOPMENT_RELOAD_EXIT = 76


def development_root():
    """Only the editable checkout opts into reload; installed runtimes stay fixed."""
    root = Path(os.environ.get('WAKE_DEV_SOURCE_ROOT') or Path(__file__).resolve().parent.parent).resolve()
    enabled = os.environ.get('WAKE_DEV_RELOAD', '').lower()
    if enabled == 'true' or (not enabled and root == Path('/workspace') and (root / '.git').exists()):
        return root
    return None


class InvalidDevelopmentSource(ValueError):
    """A partial save is not permission to replace a functioning worker."""


@contextmanager
def development_worker(root, command, env):
    """Freeze only executable source/configuration, never credentials or records."""
    before = source_signature(root)
    with tempfile.TemporaryDirectory(prefix='wake-dev-source-') as directory:
        candidate = Path(directory)
        shutil.copytree(root / 'wake', candidate / 'wake',
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.passenger*'))
        for name in ('wake.toml', 'research-topics.toml', '.wake-runner-topics'):
            source = root / name
            if source.is_dir():
                shutil.copytree(source, candidate / name)
            elif source.is_file():
                shutil.copyfile(source, candidate / name)
        if before != source_signature(root):
            raise InvalidDevelopmentSource('Source changed while preparing replacement')
        try:
            for path in (candidate / 'wake').rglob('*.py'):
                compile(path.read_bytes(), str(path), 'exec')
            for path in candidate.rglob('*.toml'):
                tomllib.loads(path.read_text())
        except (SyntaxError, ValueError) as exc:
            raise InvalidDevelopmentSource('Incomplete Python or configuration save') from exc
        worker_env = dict(env, WAKE_DEV_RELOAD='true', WAKE_DEV_SOURCE_ROOT=str(root),
                          WAKE_DEV_SOURCE_SIGNATURE=json.dumps(before),
                          PYTHONPATH=str(candidate))
        for key in ('WAKE_GROUP_TOPIC_FILE',):
            value = worker_env.get(key)
            if value and Path(value).is_relative_to(root):
                worker_env[key] = str(candidate / Path(value).relative_to(root))
        worker_command = list(command)
        config_path = candidate / 'wake.toml'
        if '--config' in worker_command:
            index = worker_command.index('--config') + 1
            source_config = Path(worker_command[index]).resolve()
            if source_config.is_relative_to(root):
                config_path = candidate / source_config.relative_to(root)
                worker_command[index] = str(config_path)
            else:
                config_path = source_config
            worker_env['WAKE_DEV_CONFIG_SOURCE'] = str(source_config)
        probe = subprocess.run(
            [command[0], '-c', 'import sys; import wake.standalone; from wake.engine import config; config(sys.argv[1])',
             str(config_path)], cwd=candidate, env=worker_env,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=15)
        if probe.returncode:
            raise InvalidDevelopmentSource('Replacement imports or configuration are invalid')
        yield worker_command, worker_env, candidate


def wait_for_development_save(root, initial, stop):
    signature, changed_at = initial, None
    while not stop.wait(.5):
        current = source_signature(root)
        if current != signature:
            signature, changed_at = current, time.monotonic()
        elif changed_at is not None and time.monotonic() - changed_at >= 1:
            return


def source_signature(root):
    paths = list((root / 'wake').rglob('*'))
    paths += list((root / '.wake-runner-topics').glob('*.toml'))
    paths += [root / 'wake.toml', root / 'research-topics.toml']
    result = []
    for path in sorted(paths):
        if '__pycache__' in path.parts or any(part.startswith('.passenger') for part in path.parts) or not path.is_file():
            continue
        if path.suffix != '.py' and 'assets' not in path.parts and path.suffix != '.toml':
            continue
        try:
            stat = path.stat()
            result.append((str(path), stat.st_mtime_ns, stat.st_size))
        except FileNotFoundError:
            continue
    return tuple(result)


def watch_development_sources(root, initial, stop, reload_requested, config_path, status=None):
    """Request shutdown after a settled save; the worker drains its own attempt."""
    signature, changed_at = initial, None
    while not stop.wait(.5):
        current = source_signature(root)
        if current != signature:
            signature, changed_at = current, time.monotonic()
        elif changed_at is not None and time.monotonic() - changed_at >= 1:
            try:
                with development_worker(root, [sys.executable, '-m', 'wake.standalone',
                                               '--config', str(config_path)], os.environ):
                    pass
                if signature != source_signature(root):
                    continue
            except (InvalidDevelopmentSource, OSError, subprocess.TimeoutExpired):
                if status:
                    status('save-not-ready')
                print(json.dumps({'development_reload': 'save-not-ready',
                                  'boundary': 'current worker retained; waiting for another save'}), flush=True)
                changed_at = None
                continue
            reload_requested.set()
            if status:
                status('draining')
            stop.set()
            print(json.dumps({'development_reload': 'requested',
                              'boundary': 'finish current attempt before reloading source'}), flush=True)
            return


def supervise(command, *, stop=None, retry_delay=2, window_seconds=900, restart_limit=5):
    stop = stop or threading.Event()
    previous = {}
    for sig in (signal.SIGTERM, signal.SIGINT):
        previous[sig] = signal.signal(sig, lambda *_: stop.set())
    restarts = []
    failures = 0
    source_root = development_root()
    try:
        while not stop.is_set():
            source_before_start = source_signature(source_root) if source_root else None
            env = dict(os.environ, WAKE_RUNTIME_CHILD='1')
            try:
                with ExitStack() as worker_source:
                    if source_root:
                        worker_command, worker_env, cwd = worker_source.enter_context(
                            development_worker(source_root, command, env))
                        process = subprocess.Popen(worker_command, env=worker_env, cwd=cwd)
                    else:
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
            except (InvalidDevelopmentSource, OSError, subprocess.TimeoutExpired):
                if not source_root:
                    raise
                print(json.dumps({'development_reload': 'save-not-ready',
                                  'boundary': 'no worker started; waiting for another save'}), flush=True)
                wait_for_development_save(source_root, source_before_start, stop)
                continue
            if not stop.is_set() and code == DEVELOPMENT_RELOAD_EXIT:
                continue
            if stop.is_set() or code == 0:
                return 0
            # An ordinary nonzero exit is an operator/configuration/integrity
            # failure. Retrying it cannot heal source code or grant authority.
            if code != TEMPORARY_EXIT and code >= 0:
                if source_root:
                    # A broken edit stays closed until a new settled save. Never
                    # retry unchanged configuration or integrity failures.
                    print(json.dumps({'development_reload': 'waiting-for-corrected-source',
                                      'exit_code': code}), flush=True)
                    wait_for_development_save(source_root, source_before_start, stop)
                    continue
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
