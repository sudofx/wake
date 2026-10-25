#!/usr/bin/env python3
"""Complete an explicit, exact-run upgrade request after its background gate."""
import argparse
import base64
import json
import os
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wake.hosted import GitHub
from wake.installation_cli import NODE_IDS


def read_policy(client):
    blob = client.request('contents/hosted-runtime.json?ref=master')
    return json.loads(base64.b64decode(blob['content'])), blob['sha']


def write_policy(client, policy, sha, message):
    return client.request('contents/hosted-runtime.json', method='PUT', body={
        'branch': 'master', 'sha': sha, 'message': message,
        'content': base64.b64encode((json.dumps(policy, indent=2) + '\n').encode()).decode()})


def complete_upgrade(client, report, run_id):
    policy, sha = read_policy(client)
    binding = policy['installations'][client.repository]
    intent = binding.get('pending_upgrade')
    if not intent or intent['verification_run'] != run_id:
        return 'no-matching-request'
    candidate, baseline = intent['candidate'], intent['baseline']
    if (not all(re.fullmatch('[a-f0-9]{40}', value) for value in (candidate, baseline, intent['checkpoint_ref']))
            or report.get('status') != 'verified'
            or report.get('candidate') != candidate or report.get('baseline') != baseline
            or report.get('installation_id') != binding['installation_id']
            or report.get('generation') != intent['generation']
            or not re.fullmatch('[a-f0-9]{64}', report.get('checkpoint_sha256', ''))
            or report.get('provider_calls') != 0 or report.get('remote_record_writes') != 0
            or set(report.get('nodes', {})) != set(NODE_IDS)):
        raise ValueError('Audit differs from the explicit upgrade request')
    for node in report['nodes'].values():
        if (set(node) != {'head', 'native_head', 'version', 'revision'}
                or any(not re.fullmatch('[a-f0-9]{64}', str(node[key])) for key in ('head', 'native_head'))
                or any(type(node[key]) is not int or node[key] < 0 for key in ('version', 'revision'))):
            raise ValueError('Incomplete native audit')
    run = client.request(f'actions/runs/{run_id}')
    if (run['status'] != 'completed' or run['conclusion'] != 'success'
            or run['head_branch'] != 'master' or run['event'] != 'workflow_dispatch'
            or run['path'] != '.github/workflows/verify-hosted-upgrade.yml'):
        raise ValueError('Verification workflow did not succeed')
    checks = client.request(f'actions/workflows/test.yml/runs?head_sha={candidate}&status=success&per_page=20')['workflow_runs']
    if not any(item['head_sha'] == candidate and item['head_branch'] == 'master'
               and item['event'] in ('push', 'workflow_dispatch') for item in checks):
        raise ValueError('Candidate has no successful master code checks')
    if binding['source_revision'] == baseline:
        controls = client.request('actions/workflows/hosted-control.yml/runs?per_page=1')['workflow_runs']
        if not controls or controls[0]['id'] != intent['control_run']:
            raise ValueError('A newer operator control superseded this upgrade request')
        if client.request('actions/workflows/hosted-research.yml')['state'] != 'disabled_manually':
            raise ValueError('Research must be drained before the final frozen-checkpoint promotion')
        for status in ('in_progress', 'queued'):
            if client.request(f'actions/workflows/hosted-research.yml/runs?status={status}&per_page=1')['workflow_runs']:
                raise ValueError('Research has an outstanding writer')
        if client.request('git/ref/heads/wake-hosted-state')['object']['sha'] != intent['checkpoint_ref']:
            raise ValueError('Final checkpoint changed after verification')
        binding['source_revision'] = candidate
        write_policy(client, policy, sha, 'Promote verified hosted runtime ' + candidate[:12])
    elif binding['source_revision'] != candidate:
        raise ValueError('Runtime binding changed since the request')
    # On an interrupted rerun, a dispatched start/active successor is enough.
    active = client.request('actions/workflows/hosted-research.yml')['state'] == 'active'
    if not active:
        for status in ('queued', 'in_progress'):
            if client.request(f'actions/workflows/hosted-control.yml/runs?status={status}&per_page=1')['workflow_runs']:
                raise ValueError('A control operation is already outstanding; do not duplicate it')
        client.request('actions/workflows/hosted-control.yml/dispatches', method='POST',
                       body={'ref': 'master', 'inputs': {'action': 'start'}})
    current, current_sha = read_policy(client)
    selected = current['installations'][client.repository]
    if selected.get('pending_upgrade') != intent or selected['source_revision'] != candidate:
        raise ValueError('Upgrade request changed before completion')
    del selected['pending_upgrade']
    write_policy(client, current, current_sha, 'Complete hosted upgrade restart request')
    return 'promoted-and-start-requested'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-id', type=int, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    client = GitHub(os.environ['GITHUB_REPOSITORY'], os.environ['GH_TOKEN'])
    result = complete_upgrade(client, json.loads(args.report.read_text()), args.run_id)
    print(json.dumps({'status': result, 'verification_run': args.run_id}))


if __name__ == '__main__':
    main()
