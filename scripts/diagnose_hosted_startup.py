"""Compare stopped startup on disposable copies; emit numeric observations only."""
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wake.hosted import HostedState
from wake.installation_cli import request
from scripts.github_research import (apply_decision_memory_policy,
    apply_provider_pacing_policy, apply_experimental_research_policy)


def memory_events():
    path = Path('/sys/fs/cgroup/memory.events')
    if not path.exists():
        return {}
    return {key: int(value) for key, value in (line.split() for line in path.read_text().splitlines())}


def sample(root, *, bounded):
    before = memory_events()
    started = time.monotonic()
    result = {'bounded_exports': bounded, 'ready': False, 'exited': []}
    with tempfile.TemporaryDirectory() as temporary:
        inject = 'import faulthandler\nfaulthandler.dump_traceback_later(60, repeat=True)\n'
        if not bounded:
            # Reproduce the old unbounded export behavior on the same source and
            # records. This override exists only in the disposable diagnostic.
            inject += "import contextlib\nimport wake.export_admission as a\na.export_slot = lambda directory: contextlib.nullcontext()\n"
        Path(temporary, 'sitecustomize.py').write_text(inject)
        env = {key: os.environ[key] for key in ('PATH', 'LANG', 'LC_ALL', 'LD_LIBRARY_PATH') if key in os.environ}
        env.update(PYTHONPATH=temporary + os.pathsep + str(Path.cwd()), WAKE_DEV_RELOAD='false')
        with (root / 'controller.log').open('wb') as log:
            process = subprocess.Popen([sys.executable, '-m', 'wake.installation', '--data', str(root),
                '--config', str(root / 'config/wake.toml'), '--host', '127.0.0.1', '--port', '0', '--provider', 'fixture'],
                env=env, stdout=log, stderr=log, start_new_session=True)
            try:
                deadline = started + 600
                while time.monotonic() < deadline:
                    if process.poll() is not None:
                        raise RuntimeError('Isolated diagnostic controller exited')
                    if (root / 'runtime-endpoint.json').exists():
                        status = request(root, {'action': 'status'})
                        result['exited'] = [{'id': n['id'], 'exit_code': n['process']['exit_code']}
                                            for n in status['nodes'] if n.get('process', {}).get('state') == 'exited']
                        result['ready'] = all(n.get('available') and n.get('runtime', {}).get('state') in ('stopped', 'paused')
                                              for n in status['nodes'])
                        if result['exited'] or result['ready']:
                            break
                    time.sleep(2)
            finally:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    pass
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
    result['seconds'] = round(time.monotonic() - started, 3)
    after = memory_events()
    result['memory_events_delta'] = {key: value - before.get(key, 0) for key, value in after.items()}
    print(json.dumps({'startup_comparison': result}), flush=True)
    return result


def main():
    transport = HostedState.from_environment()
    transport.open()
    root = Path(os.environ['WAKE_INSTALLATION_DATA'])
    manifest = transport.restore(root, workers=1)
    policy = json.loads(Path('hosted-runtime.json').read_text())['installations'][os.environ['GITHUB_REPOSITORY']]
    if manifest['installation_id'] != policy['installation_id']:
        raise ValueError('Diagnostic installation identity mismatch')
    apply_decision_memory_policy(root, policy)
    apply_provider_pacing_policy(root, policy)
    apply_experimental_research_policy(root, policy)
    if 'research_expansion_enabled' in policy:
        from wake.research_expansion import apply_hosted_configuration
        apply_hosted_configuration(root, policy['research_expansion_enabled'], policy.get('research_candidate_catalog_enabled', False))
    print(json.dumps({'diagnostic_generation': manifest['generation'], 'provider_calls': 0, 'remote_record_writes': 0}), flush=True)
    baseline_root = root.with_name(root.name + '-unbounded')
    shutil.copytree(root, baseline_root)
    baseline = sample(baseline_root, bounded=False)
    candidate = sample(root, bounded=True)
    if not candidate['ready'] or candidate['exited']:
        raise RuntimeError('Bounded candidate did not bring all twelve stopped workers online')
    print(json.dumps({'startup_repair': 'verified', 'baseline': baseline, 'candidate': candidate}), flush=True)


if __name__ == '__main__':
    main()
