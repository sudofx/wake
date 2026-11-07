"""Inspect stopped startup on disposable checkpoint copies; emit locations only."""
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wake.hosted import HostedState
from scripts.github_research import (apply_decision_memory_policy,
    apply_provider_pacing_policy, apply_experimental_research_policy)


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
    from wake.record_store import RecordStore
    from wake.installation import NODE_IDS
    for node in NODE_IDS:
        store = RecordStore(root / 'nodes' / node / 'record')
        state = store.load()
        print(json.dumps({'startup_record': node, 'bytes': Path(store.path).stat().st_size,
            'counts': {key: len(state.get(key, {})) for key in ('invocations', 'evidence', 'journal', 'notebooks', 'research')}}), flush=True)
        store.close()
        del state, store
    with tempfile.TemporaryDirectory() as temporary:
        # Inject stack sampling without changing the installed runtime. Never
        # pass provider credentials or checkpoint capabilities to the processes.
        Path(temporary, 'sitecustomize.py').write_text('import faulthandler\nfaulthandler.dump_traceback_later(30, repeat=True)\n')
        env = {key: os.environ[key] for key in ('PATH', 'LANG', 'LC_ALL', 'LD_LIBRARY_PATH') if key in os.environ}
        env.update(PYTHONPATH=temporary + os.pathsep + str(Path.cwd()), WAKE_DEV_RELOAD='false')
        with (root / 'controller.log').open('wb') as log:
            process = subprocess.Popen([sys.executable, '-m', 'wake.installation', '--data', str(root),
                '--config', str(root / 'config/wake.toml'), '--host', '127.0.0.1', '--port', '0', '--provider', 'fixture'],
                env=env, stdout=log, stderr=log, start_new_session=True)
            try:
                process.wait(timeout=60)
            except subprocess.TimeoutExpired:
                pass
            finally:
                for node in NODE_IDS:
                    base = root / 'nodes' / node
                    print(json.dumps({'startup_node': node, 'runtime': (base / 'runtime.json').exists(),
                        'export': (base / 'site/current').exists(),
                        'largest_files': sorted([p.stat().st_size for p in (base / 'site').rglob('*') if p.is_file()], reverse=True)[:5]}), flush=True)
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    pass
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
    for path in [root / 'controller.log', *sorted(root.glob('nodes/*/worker.log'))]:
        with path.open('rb') as stream:
            stream.seek(max(0, path.stat().st_size - 32768))
            lines = stream.read(32768).decode('utf-8', errors='replace').splitlines()
        frames, errors = [], []
        for line in lines:
            frame = re.fullmatch(r'  File ".*?/(wake|scripts)/([A-Za-z0-9_/.]+\.py)", line ([0-9]+)(?:,? in ([A-Za-z0-9_<>]+))', line)
            if frame:
                frames.append({'source': frame[1] + '/' + frame[2], 'line': int(frame[3]), 'function': frame[4]})
            error = re.match(r'^([A-Za-z_][A-Za-z0-9_]*(?:Error|Exception)):', line)
            if error:
                errors.append(error[1])
        print(json.dumps({'log': str(path.relative_to(root)), 'bytes': path.stat().st_size,
                          'frames': frames[-30:], 'errors': errors[-4:]}), flush=True)


if __name__ == '__main__':
    main()
