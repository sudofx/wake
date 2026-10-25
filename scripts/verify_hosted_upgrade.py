#!/usr/bin/env python3
"""Verify an upgrade on disposable recovery copies; never save hosted checkpoints."""
import argparse
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
        transport.open()
        checkpoint = transport.read_manifest()
        if checkpoint['installation_id'] != policy['installation_id']:
            raise ValueError('Checkpoint installation differs from policy')
        records = root / 'installation'
        transport.restore(records, workers=4)
        program = r'''
import json,sys
from pathlib import Path
from wake.authority import open_authoritative_store
from wake.hosted import record_identity
root=Path(sys.argv[1]);result={}
for directory in sorted((root/'nodes').glob('*/record')):
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
        results = []
        for source in (baseline, candidate):
            env = dict(os.environ, PYTHONPATH=str(source))
            # Provider credentials are neither needed nor passed to the audits.
            for key in tuple(env):
                if any(marker in key for marker in ('API_KEY', 'STATE_KEY', 'INGEST_TOKEN')):
                    env.pop(key)
            output = subprocess.check_output([sys.executable, '-c', program, str(records)],
                                             cwd=source, env=env, text=True)
            results.append(json.loads(output))
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
