#!/usr/bin/env python3
"""Apply an explicit operator configuration to a drained hosted installation."""
import argparse
import base64
from copy import deepcopy
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import tomllib

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.complete_hosted_upgrade import read_policy, writer_outstanding
from wake.hosted import GitHub, HostedState
from wake.installation_cli import NODE_IDS

FEATURES = {
    'memory_mode': 'active',
    'decision_memory_mode': 'active',
    'autonomous_context_improvement': True,
    'experimental_research_enabled': True,
    'inquiry_drive_enabled': True,
    'same_wake_research': True,
    'research_quality_policy': True,
}


def feature_configuration(original):
    """Change root feature switches while preserving every table and other key."""
    before = tomllib.loads(original)
    root = True
    retained = []
    for line in original.splitlines(keepends=True):
        if line.lstrip().startswith('['):
            root = False
        match = re.match(r'^\s*([A-Za-z0-9_]+)\s*=', line)
        if root and match and match[1] in FEATURES:
            continue
        retained.append(line)
    updated = ''.join(f'{key} = {json.dumps(value)}\n' for key, value in FEATURES.items()) + ''.join(retained)
    after = tomllib.loads(updated)
    expected = {**before, **FEATURES}
    if after != expected:
        raise ValueError('Feature configuration changed unrelated settings')
    return updated, {key: before.get(key) for key in FEATURES}


def current_stop(client, control_run):
    latest = client.request('actions/workflows/hosted-control.yml/runs?per_page=1')['workflow_runs']
    if not latest or latest[0]['id'] != control_run:
        raise ValueError('A newer operator control superseded feature configuration')
    run = client.request('actions/runs/' + str(control_run))
    if (run.get('path') != '.github/workflows/hosted-control.yml'
            or run.get('head_branch') != 'master'
            or run.get('status') != 'completed' or run.get('conclusion') != 'success'):
        raise ValueError('The requested stop control has not succeeded')
    if client.request('actions/workflows/research-worker.yml')['state'] != 'disabled_manually':
        raise ValueError('Hosted research must remain stopped during configuration')


def configure(client, transport, control_run, drained_run, *, timeout=2700):
    deadline = time.monotonic() + timeout
    while True:
        current_stop(client, control_run)
        run = client.request('actions/runs/' + str(drained_run))
        if run.get('path') != '.github/workflows/research-worker.yml' or run.get('head_branch') != 'master':
            raise ValueError('Drain identity must name the hosted master research worker')
        if run['status'] == 'completed':
            if run['conclusion'] != 'success':
                raise ValueError('Research did not complete a successful drained checkpoint')
            break
        if time.monotonic() >= deadline:
            raise TimeoutError('The research worker is still draining; no configuration changed')
        time.sleep(30)
    policy, _ = read_policy(client)
    binding = policy['installations'][client.repository]
    if binding.get('experimental_research_enabled') is not True or binding.get('pending_upgrade'):
        raise ValueError('An explicit scientific grant and no competing upgrade are required')
    blob = client.request('contents/hosted-runtime.json?ref=' + run['head_sha'])
    drained_binding = json.loads(base64.b64decode(blob['content']))['installations'][client.repository]
    if (drained_binding['installation_id'] != binding['installation_id']
            or not re.fullmatch('[a-f0-9]{40}', str(drained_binding.get('source_revision', '')))):
        raise ValueError('Drained worker has a different installation binding')
    intent = {'baseline': drained_binding['source_revision'], 'candidate': binding['source_revision'],
              'drained_run': drained_run, 'superseded_queued_runs': [40554824224],
              'superseded_queued_baselines': {40554824224: '49c9c2bd058c851768320143edc4cf6d6d1e85d4'}}
    # JSON policy maps use string keys; use the existing queue reconciliation.
    intent['superseded_queued_baselines'] = {str(k): v for k, v in intent['superseded_queued_baselines'].items()}
    for status in ('queued', 'in_progress'):
        listing = client.request(f'actions/workflows/research-worker.yml/runs?status={status}&per_page=100')
        rows = listing['workflow_runs']
        if listing.get('total_count', len(rows)) > len(rows):
            raise ValueError('Outstanding worker listing is incomplete')
        if any(writer_outstanding(client, row, intent, binding['installation_id']) for row in rows):
            raise ValueError('Another research worker is outstanding')
    transport.open()
    with tempfile.TemporaryDirectory(prefix='wake-feature-configuration-') as directory:
        root = Path(directory) / 'installation'
        manifest = transport.restore(root, workers=3)
        if manifest['installation_id'] != binding['installation_id'] or set(manifest['nodes']) != set(NODE_IDS):
            raise ValueError('Restored installation differs from the requested binding')
        records = deepcopy(manifest['nodes'])
        path = root / 'config/wake.toml'
        updated, previous = feature_configuration(path.read_text())
        path.write_text(updated)
        current_stop(client, control_run)
        current, _ = read_policy(client)
        if current['installations'][client.repository] != binding:
            raise ValueError('Hosted policy changed during feature configuration')
        with transport.lease():
            latest = transport.read_manifest()
            if latest != manifest:
                raise ValueError('Hosted checkpoint changed during configuration')
            manifest['auxiliary'] = transport.put_auxiliary(root, transport.assets())
            if manifest['nodes'] != records:
                raise ValueError('Feature configuration must not change native records')
            transport.save(manifest)
    return {'installation_id': binding['installation_id'], 'generation': manifest['generation'],
            'previous': previous, 'configured': FEATURES, 'native_records_changed': False}


def restart(client, control_run):
    """Resume through the normal control only while the same stop owns intent."""
    current_stop(client, control_run)
    client.request('actions/workflows/hosted-control.yml/dispatches', method='POST',
                   body={'ref': 'master', 'inputs': {'action': 'start'}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--control-run', type=int, required=True)
    parser.add_argument('--drained-run', type=int, required=True)
    parser.add_argument('--restart', action='store_true')
    args = parser.parse_args()
    client = GitHub(os.environ['GITHUB_REPOSITORY'], os.environ['GH_TOKEN'])
    if args.restart:
        restart(client, args.control_run)
        return
    result = configure(client, HostedState.from_environment(), args.control_run, args.drained_run)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
