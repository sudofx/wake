#!/usr/bin/env python3
"""Verify an upgrade on disposable recovery copies; never save hosted checkpoints."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--baseline', type=Path, required=True)
    parser.add_argument('--policy', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    candidate, baseline = args.candidate.resolve(), args.baseline.resolve()
    policy = json.loads(args.policy.read_text())['installations'][os.environ['GITHUB_REPOSITORY']]
    def revision(root):
        value = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
        if not re.fullmatch('[a-f0-9]{40}', value):
            raise ValueError('Expected an immutable source revision')
        return value
    candidate_sha, baseline_sha = revision(candidate), revision(baseline)
    if baseline_sha != policy['source_revision']:
        raise ValueError('Baseline differs from the bound runtime')
    sys.path.insert(0, str(candidate))
    from wake.hosted import HostedState
    from wake.installation_cli import NODE_IDS
    with tempfile.TemporaryDirectory(prefix='wake-upgrade-verification-') as temporary:
        root = Path(temporary)
        transport = HostedState(root / 'transport', os.environ['GITHUB_REPOSITORY'],
                                os.environ['GH_TOKEN'], os.environ['WAKE_HOSTED_STATE_KEY'])
        # Read-only workflow permissions prevent any remote write. No controller,
        # provider, save, seed, prune, or research-start capability is invoked.
        print('Opening authenticated disposable recovery copies', flush=True)
        transport.open()
        checkpoint = transport.read_manifest()
        if checkpoint['installation_id'] != policy['installation_id']:
            raise ValueError('Checkpoint installation differs from policy')
        records = root / 'installation'
        transport.restore(records, workers=4)
        print('Restored and verified all twelve checkpoint identities', flush=True)
        program = r'''
import json,sys
from pathlib import Path
from wake.authority import open_authoritative_store
from wake.hosted import record_identity
root=Path(sys.argv[1]);result={}
for directory in [root/'nodes'/sys.argv[2]/'record']:
    path=directory/'wake.sqlite'
    before=record_identity(path)
    store=open_authoritative_store(directory)
    try:
        state,head=store.audit()
        result[directory.parent.name]={'head':head,'version':state['version'],'revision':before['revision'],'native_head':before['head']}
    finally:store.close()
    after=record_identity(path)
    if any(before[key]!=after[key] for key in ('head','revision')):raise ValueError('Audit changed native history')
print(json.dumps(result,sort_keys=True))
'''
        def compare_node(node):
            pair = []
            for name, source in (('baseline', baseline), ('candidate', candidate)):
                env = dict(os.environ, PYTHONPATH=str(source))
                # Audits receive no provider, checkpoint or publication credential.
                for key in tuple(env):
                    if any(marker in key for marker in ('API_KEY', 'STATE_KEY', 'INGEST_TOKEN', 'GH_TOKEN', 'GITHUB_TOKEN')):
                        env.pop(key)
                print('Full ' + name + ' audit: ' + node, flush=True)
                output = subprocess.check_output([sys.executable, '-c', program, str(records), node],
                                                 cwd=source, env=env, text=True)
                pair.append(json.loads(output))
            if pair[0] != pair[1] or set(pair[0]) != {node}:
                raise ValueError('Candidate and baseline disagree on ' + node)
            print('Matching full audits: ' + node, flush=True)
            return pair
        # Each pair owns a different disposable node; never audit the same copy
        # concurrently or open an operational controller. Bound replay memory.
        results = [{}, {}]
        with ThreadPoolExecutor(max_workers=2) as executor:
            for pair in executor.map(compare_node, NODE_IDS):
                for index in (0, 1):
                    results[index].update(pair[index])
        if set(results[0]) != set(NODE_IDS) or results[0] != results[1]:
            raise ValueError('Candidate and baseline disagree on the twelve records')
        report = {'status': 'verified', 'candidate': candidate_sha, 'baseline': baseline_sha,
                  'installation_id': checkpoint['installation_id'],
                  'generation': checkpoint['generation'], 'nodes': results[1],
                  'provider_calls': 0, 'remote_record_writes': 0}
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
        print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
