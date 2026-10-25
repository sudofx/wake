#!/usr/bin/env python3
"""Verify an upgrade on disposable recovery copies; never save hosted checkpoints."""
import argparse
import hashlib
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import shutil
import zipfile


def capture_snapshot(transport, destination):
    """Retain encrypted inputs before replay; rotating recovery may then advance."""
    from wake.hosted import unseal
    destination = Path(destination)
    if destination.exists():
        raise ValueError('Snapshot destination must not exist')
    with tempfile.TemporaryDirectory(dir=destination.parent) as temporary:
        staged = Path(temporary)
        manifest = transport.read_manifest()
        shutil.copyfile(transport.checkout / 'current.enc', staged / 'current.enc')
        blocks = {item['name']: item for value in manifest['nodes'].values() for item in value['blocks']}
        blocks.update({item['name']: item for item in manifest['auxiliary']})
        (staged / 'blocks').mkdir()
        for name, item in blocks.items():
            if not re.fullmatch(r'block-[0-9a-f]{64}\.bin', name):
                raise ValueError('Invalid encrypted snapshot block name')
            data = transport.api.request(f'releases/assets/{int(item["id"])}', binary=True)
            unseal(transport.key, data, name)  # Never retain unauthenticated inputs.
            (staged / 'blocks' / name).write_bytes(data)
        # Publish only a complete capture; no decrypted records enter artifacts.
        staged.rename(destination)
    return manifest


class SnapshotFiles:
    """Offline, GET-only encrypted inputs; no GitHub or provider capability."""
    def __init__(self, root, manifest):
        self.root = Path(root)
        self.names = {int(item['id']): item['name'] for value in manifest['nodes'].values() for item in value['blocks']}
        self.names.update({int(item['id']): item['name'] for item in manifest['auxiliary']})

    def request(self, path, *, binary=False):
        if not binary or not re.fullmatch(r'releases/assets/[0-9]+', path):
            raise ValueError('Snapshot permits encrypted block reads only')
        name = self.names[int(path.rsplit('/', 1)[1])]
        if not re.fullmatch(r'block-[0-9a-f]{64}\.bin', name):
            raise ValueError('Invalid encrypted snapshot block name')
        return (self.root / 'blocks' / name).read_bytes()


def restore_audit_nodes(transport, manifest, records, nodes):
    """Each shard verifies only its assigned records, never twelve copies each."""
    from wake.hosted import verify_recovery
    records = Path(records)
    transport.get_file(manifest['auxiliary'], records / 'aux.zip')
    with zipfile.ZipFile(records / 'aux.zip') as archive:
        if json.loads(archive.read('installation-id.json'))['id'] != manifest['installation_id']:
            raise ValueError('Installation identity mismatch')
    for node in nodes:
        value = manifest['nodes'][node]
        target = records / 'nodes' / node / 'record/wake.sqlite'
        transport.get_file(value['blocks'], target)
        if verify_recovery(target) != {key: value[key] for key in ('revision', 'head', 'sha256')}:
            raise ValueError('Restored node history differs from checkpoint: ' + node)


def aggregate_reports(directory, *, candidate, policy, node_ids):
    """Fail closed unless every node passed against one identical checkpoint."""
    reports = [json.loads(path.read_text()) for path in sorted(directory.glob('*.json'))]
    if len(reports) != len(node_ids):
        raise ValueError('Expected exactly one report for each of the twelve nodes')
    shared = ('candidate', 'baseline', 'installation_id', 'generation', 'checkpoint_sha256')
    first = reports[0]
    if (first['candidate'] != candidate or first['baseline'] != policy['source_revision']
            or first['installation_id'] != policy['installation_id']
            or type(first['generation']) is not int or first['generation'] < 1
            or not re.fullmatch('[a-f0-9]{64}', first['checkpoint_sha256'])):
        raise ValueError('Report differs from the requested candidate, policy or checkpoint')
    nodes = {}
    for report in reports:
        if (report['status'] != 'verified-node'
                or any(report[key] != first[key] for key in shared)
                or report['provider_calls'] != 0 or report['remote_record_writes'] != 0
                or len(report['nodes']) != 1):
            raise ValueError('Incomplete or inconsistent node verification')
        node, result = next(iter(report['nodes'].items()))
        if node not in node_ids or node in nodes:
            raise ValueError('Unexpected or duplicate node verification')
        if (set(result) != {'head', 'version', 'native_head', 'revision'}
                or any(not isinstance(result[key], str) or not re.fullmatch('[a-f0-9]{64}', result[key])
                       for key in ('head', 'native_head'))
                or any(type(result[key]) is not int or result[key] < 0
                       for key in ('version', 'revision'))):
            raise ValueError('Incomplete full audit result')
        nodes[node] = result
    if set(nodes) != set(node_ids):
        raise ValueError('Missing node verification')
    return {**{key: first[key] for key in shared}, 'status': 'verified',
            'nodes': nodes, 'provider_calls': 0, 'remote_record_writes': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path)
    parser.add_argument('--capture', type=Path, help='Capture encrypted audit inputs without replay or research controls')
    parser.add_argument('--snapshot', type=Path, help='Audit retained encrypted inputs entirely offline')
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--node', help='Audit one node in a bounded workflow shard')
    parser.add_argument('--aggregate', type=Path, help='Directory of all twelve node reports')
    parser.add_argument('--policy', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    policy = json.loads(args.policy.read_text())['installations'][os.environ['GITHUB_REPOSITORY']]
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from wake.hosted import HostedState
    if args.capture:
        if args.candidate or args.baseline or args.node or args.aggregate or args.snapshot:
            parser.error('Capture does not run audits')
        with tempfile.TemporaryDirectory(prefix='wake-upgrade-capture-') as temporary:
            transport = HostedState(temporary, os.environ['GITHUB_REPOSITORY'],
                                    os.environ['GH_TOKEN'], os.environ['WAKE_HOSTED_STATE_KEY'])
            transport.open()
            if transport.read_manifest()['installation_id'] != policy['installation_id']:
                raise ValueError('Checkpoint installation differs from policy')
            manifest = capture_snapshot(transport, args.capture.resolve())
            args.output.write_text(json.dumps({'generation': manifest['generation'],
                                               'installation_id': manifest['installation_id']}))
        return 0
    if not args.candidate:
        parser.error('Audits require a candidate')
    candidate = args.candidate.resolve()
    def revision(root):
        value = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
        if not re.fullmatch('[a-f0-9]{40}', value):
            raise ValueError('Expected an immutable source revision')
        return value
    candidate_sha = revision(candidate)
    # Node membership comes from the trusted workflow checkout, not its input.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from wake.installation_cli import NODE_IDS
    if args.aggregate:
        if args.node or args.baseline:
            parser.error('Aggregation does not run audits')
        report = aggregate_reports(args.aggregate, candidate=candidate_sha, policy=policy, node_ids=NODE_IDS)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
        return 0
    if not args.baseline or (args.node and args.node not in NODE_IDS):
        parser.error('Audits require a baseline and a valid node')
    baseline = args.baseline.resolve()
    baseline_sha = revision(baseline)
    if baseline_sha != policy['source_revision']:
        raise ValueError('Baseline differs from the bound runtime')
    with tempfile.TemporaryDirectory(prefix='wake-upgrade-verification-') as temporary:
        root = Path(temporary)
        transport = HostedState(root / 'transport', os.environ['GITHUB_REPOSITORY'],
                                'offline' if args.snapshot else os.environ['GH_TOKEN'], os.environ['WAKE_HOSTED_STATE_KEY'])
        # Read-only workflow permissions prevent any remote write. No controller,
        # provider, save, seed, prune, or research-start capability is invoked.
        print('Opening authenticated disposable recovery copies', flush=True)
        if args.snapshot:
            transport.checkout = args.snapshot.resolve()
        else:
            transport.open()
        checkpoint = transport.read_manifest()
        if checkpoint['installation_id'] != policy['installation_id']:
            raise ValueError('Checkpoint installation differs from policy')
        records = root / 'installation'
        if args.snapshot:
            transport.api = SnapshotFiles(args.snapshot, checkpoint)
        selected = (args.node,) if args.node else NODE_IDS
        restore_audit_nodes(transport, checkpoint, records, selected)
        print('Restored and verified assigned checkpoint identities', flush=True)
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
            identity = checkpoint['nodes'][node]
            if any(pair[1][node][key] != identity[field] for key, field in
                   (('native_head', 'head'), ('revision', 'revision'))):
                raise ValueError('Audit differs from the authenticated checkpoint: ' + node)
            return pair
        # Each pair owns a different disposable node; never audit the same copy
        # concurrently or open an operational controller. Bound replay memory.
        results = [{}, {}]
        with ThreadPoolExecutor(max_workers=2) as executor:
            for pair in executor.map(compare_node, selected):
                for index in (0, 1):
                    results[index].update(pair[index])
        if set(results[0]) != set(selected) or results[0] != results[1]:
            raise ValueError('Candidate and baseline disagree on the twelve records')
        report = {'status': 'verified-node' if args.node else 'verified', 'candidate': candidate_sha, 'baseline': baseline_sha,
                  'installation_id': checkpoint['installation_id'],
                  'generation': checkpoint['generation'],
                  'checkpoint_sha256': hashlib.sha256(json.dumps(checkpoint, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                  'nodes': results[1],
                  'provider_calls': 0, 'remote_record_writes': 0}
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
        print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
