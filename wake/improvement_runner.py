"""Run untrusted comparison code only in disposable restricted Docker containers.

The host scores JSON outside the container. No record, credentials, source tree,
Docker socket, expected answers or writable host directory is mounted. Docker is
an isolation boundary, not proof against container-runtime/kernel vulnerabilities.
There is intentionally no subprocess-on-host fallback.
"""
import json
import hashlib
import os
from pathlib import Path
import re
import selectors
import subprocess
import tempfile
import time
import uuid

DEFAULT_IMAGE = 'python@sha256:a1165e272e578941b84abc79e4ab38a0305cd12803a5c4247979ac7655f4d641'
OUTPUT_LIMIT = 65536


class CleanupError(ValueError):
    """Execution cannot be considered terminal while cleanup is unconfirmed."""

RUNNER = '''import importlib.util, json
spec = importlib.util.spec_from_file_location("candidate", "/experiment/program.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
inputs = json.load(open("/experiment/inputs.json"))
print(json.dumps([module.decision_context(c["state"], c["question"]) for c in inputs], allow_nan=False))
'''


def image_identity(image):
    if not re.fullmatch(r'[a-z0-9./:_-]+@sha256:[0-9a-f]{64}', image):
        raise ValueError('Evaluation requires an explicit repository image digest')
    result = subprocess.run(['docker', 'image', 'inspect', image, '--format', '{{.Id}}'],
                            capture_output=True, text=True, timeout=15, check=False)
    if result.returncode or not re.fullmatch(r'sha256:[0-9a-f]{64}', result.stdout.strip()):
        raise ValueError('Pinned evaluation image is unavailable locally; pull the reviewed image explicitly first')
    return result.stdout.strip()


def command(image_id, directory, name):
    return ['docker', 'run', '--rm', '--pull=never', '--name', name,
            '--network=none', '--read-only', '--user=65534:65534', '--cap-drop=ALL',
            '--security-opt=no-new-privileges', '--pids-limit=32', '--memory=128m',
            '--memory-swap=128m', '--cpus=0.5', '--ulimit=nofile=64:64',
            '--log-driver=none', '--ipc=none', '--tmpfs=/tmp:rw,noexec,nosuid,size=16m',
            '--mount', f'type=bind,source={directory},target=/experiment,readonly',
            '--workdir=/experiment', '--entrypoint=python', image_id,
            '-I', '-S', '-B', '/experiment/runner.py']


def container_names(evaluation_id):
    if not re.fullmatch('[a-z0-9-]{1,40}', evaluation_id):
        raise ValueError('Invalid evaluation identity')
    return [f'wake-improve-{evaluation_id}-{suite}-{arm}'
            for suite in ('development', 'holdout') for arm in ('baseline', 'candidate')]


def cleanup_containers(names):
    """Remove only disposable identities reserved by this experiment."""
    for name in names:
        if not re.fullmatch(r'wake-improve-[a-z0-9-]{1,80}', name):
            raise ValueError('Invalid disposable container identity')
        try:
            result = subprocess.run(['docker', 'rm', '-f', name], stdin=subprocess.DEVNULL,
                                    capture_output=True, timeout=15, check=False)
        except (OSError, subprocess.TimeoutExpired) as error:
            raise CleanupError('Disposable container cleanup unconfirmed: ' + name) from error
        if result.returncode and b'No such container' not in result.stderr:
            # --rm and explicit recovery can race during container teardown.
            # An ambiguous removal is confirmed only by observing this exact
            # reserved identity absent; other Docker failures remain failures.
            absent = False
            for _ in range(3):
                try:
                    check = subprocess.run(['docker', 'container', 'inspect', name, '--format', '{{.State.Status}}'],
                                           stdin=subprocess.DEVNULL, capture_output=True, timeout=5, check=False)
                except (OSError,subprocess.TimeoutExpired) as error:
                    raise CleanupError('Disposable container cleanup unconfirmed: '+name) from error
                if check.returncode and (b'No such container' in check.stderr or b'No such object' in check.stderr):
                    absent = True
                    break
                time.sleep(.1)
            if not absent:
                raise CleanupError('Disposable container cleanup unconfirmed: ' + name)


def run_program(source, inputs, image_id, *, timeout=20, name=None, runner=RUNNER):
    """Bound process lifetime AND stdout/stderr before parsing any untrusted JSON."""
    if not 0 < timeout <= 60:
        raise ValueError('Evaluation timeout must be between zero and 60 seconds')
    started = time.monotonic()
    name = name or 'wake-improve-' + uuid.uuid4().hex
    if not re.fullmatch(r'wake-improve-[a-z0-9-]{1,80}', name):
        raise ValueError('Invalid disposable container identity')
    with tempfile.TemporaryDirectory(prefix='wake-improve-') as temp:
        root = Path(temp)
        root.chmod(0o755)
        for filename, value in [('program.py', source), ('runner.py', runner),
                                ('inputs.json', json.dumps(inputs, allow_nan=False))]:
            path = root / filename
            path.write_text(value)
            path.chmod(0o444)
        process = None
        output = { 'stdout': bytearray(), 'stderr': bytearray() }
        failure = None
        try:
            process = subprocess.Popen(command(image_id, root, name), stdin=subprocess.DEVNULL,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            with selectors.DefaultSelector() as selector:
                selector.register(process.stdout, selectors.EVENT_READ, 'stdout')
                selector.register(process.stderr, selectors.EVENT_READ, 'stderr')
                deadline = started + timeout
                while selector.get_map():
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise TimeoutError('Container exceeded evaluation deadline')
                    for key, _ in selector.select(min(remaining, 0.1)):
                        block = os.read(key.fileobj.fileno(), 4096)
                        if not block:
                            selector.unregister(key.fileobj)
                            continue
                        output[key.data].extend(block)
                        if sum(map(len, output.values())) > OUTPUT_LIMIT:
                            raise ValueError('Container exceeded evaluation output limit')
                code = process.wait(timeout=max(0.01, deadline - time.monotonic()))
                if code:
                    raise ValueError('Container exited unsuccessfully: ' + output['stderr'].decode(errors='replace')[:1200])
            results = json.loads(output['stdout'], parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))
            return {'status': 'completed', 'outputs': results,
                    'cleanup_confirmed': True,
                    'wall_seconds': round(time.monotonic() - started, 4),
                    'output_bytes': len(output['stdout'])}
        except (OSError, ValueError, TimeoutError, subprocess.TimeoutExpired) as error:
            failure = str(error)
        finally:
            if process is not None:
                if process.poll() is None:
                    process.kill()
                process.wait(timeout=5)
                process.stdout.close()
                process.stderr.close()
                # Killing the client alone does not guarantee container death.
                cleanup_containers([name])
        return {'status': 'failed', 'reason': failure,
                'cleanup_confirmed': True,
                'diagnostics': {'stdout_prefix':bytes(output['stdout'][:4096]).decode(errors='replace'),
                    'stderr_prefix':bytes(output['stderr'][:4096]).decode(errors='replace'),
                    'captured_stdout_digest':hashlib.sha256(output['stdout']).hexdigest(),
                    'captured_stderr_digest':hashlib.sha256(output['stderr']).hexdigest(),
                    'captured_bytes':sum(map(len,output.values())),
                    'truncated':any(len(value)>4096 for value in output.values())},
                'wall_seconds': round(time.monotonic() - started, 4)}
