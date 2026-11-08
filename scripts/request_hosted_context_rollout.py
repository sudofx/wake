"""Request one checked repair through the existing hosted upgrade gates."""
import json
import os
from pathlib import Path
import time
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from wake.hosted import GitHub, HostedState
from scripts.complete_hosted_upgrade import read_policy, write_policy


def main():
    client = GitHub(os.environ['GITHUB_REPOSITORY'], os.environ['GH_TOKEN'])
    candidate = os.environ['GITHUB_SHA']
    policy, _ = read_policy(client)
    binding = policy['installations'][client.repository]
    baseline = binding['source_revision']
    if binding.get('pending_upgrade'):
        raise ValueError('Another exact upgrade request is outstanding')

    def wait_for(probe, seconds=1200):
        deadline = time.monotonic() + seconds
        while time.monotonic() < deadline:
            value = probe()
            if value:
                return value
            time.sleep(15)
        raise TimeoutError('Repair dependency did not become ready')

    def checked():
        rows = client.request('actions/workflows/test.yml/runs?head_sha=' + candidate + '&per_page=20')['workflow_runs']
        rows = [r for r in rows if r['head_sha'] == candidate and r['head_branch'] == 'master' and r['event'] == 'push']
        if any(r['status'] == 'completed' and r['conclusion'] != 'success' for r in rows):
            raise ValueError('Candidate code checks did not pass')
        return any(r['status'] == 'completed' and r['conclusion'] == 'success' for r in rows)

    def dispatch(workflow, inputs=None):
        previous = {r['id'] for r in client.request(f'actions/workflows/{workflow}/runs?per_page=20')['workflow_runs']}
        head = client.request('git/ref/heads/master')['object']['sha']
        if head != candidate:
            raise ValueError('Source changed since this exact repair was requested')
        client.request(f'actions/workflows/{workflow}/dispatches', method='POST', body={'ref': 'master', 'inputs': inputs or {}})
        def discover():
            rows = client.request(f'actions/workflows/{workflow}/runs?per_page=20')['workflow_runs']
            matches = [r for r in rows if r['id'] not in previous and r['head_sha'] == candidate and r['event'] == 'workflow_dispatch']
            if len(matches) > 1:
                raise ValueError('Ambiguous workflow dispatch; refusing to choose')
            return matches[0] if matches else None
        return wait_for(discover, 180)

    stop = client.request('actions/runs/' + os.environ['WAKE_REPAIR_STOP_RUN'])
    controls = client.request('actions/workflows/hosted-control.yml/runs?per_page=1')['workflow_runs']
    if (stop['status'] != 'completed' or stop['conclusion'] != 'success'
            or stop['path'] != '.github/workflows/hosted-control.yml'
            or not controls or controls[0]['id'] != stop['id']):
        raise ValueError('A newer or incomplete operator control superseded this repair')
    if client.request('actions/workflows/research-worker.yml')['state'] != 'disabled_manually':
        raise ValueError('Research stop latch is not closed')
    print(json.dumps({'repair_control_run': stop['id'], 'stage': 'waiting-for-drain'}), flush=True)
    wait_for(lambda: not client.request('actions/workflows/research-worker.yml/runs?status=in_progress&per_page=1')['workflow_runs'])

    # Preserve historical jobless queue entries. The existing completion gate
    # independently proves their ancestry, ordering and empty job lists.
    queued = client.request('actions/workflows/research-worker.yml/runs?status=queued&per_page=100')
    if queued['total_count'] != len(queued['workflow_runs']):
        raise ValueError('Incomplete outstanding writer listing')
    successful = client.request('actions/workflows/research-worker.yml/runs?status=success&per_page=100')['workflow_runs']
    drained = next(r for r in successful if r['conclusion'] == 'success')
    superseded, original_bindings = [], {}
    for run in queued['workflow_runs']:
        if run['run_number'] >= drained['run_number']:
            raise ValueError('A queued writer is not superseded by completed drainage')
        jobs = client.request('actions/runs/' + str(run['id']) + '/jobs?per_page=1')
        if jobs['total_count'] or jobs['jobs']:
            raise ValueError('A queued writer has executable jobs')
        import base64
        blob = client.request('contents/hosted-runtime.json?ref=' + run['head_sha'])
        original = json.loads(base64.b64decode(blob['content']))['installations'][client.repository]
        superseded.append(run['id'])
        original_bindings[str(run['id'])] = original['source_revision']

    transport = HostedState.from_environment()
    transport.open()
    manifest = transport.read_manifest()
    checkpoint_ref = client.request('git/ref/heads/wake-hosted-state')['object']['sha']
    if manifest['installation_id'] != binding['installation_id']:
        raise ValueError('Repair checkpoint installation mismatch')
    verification = dispatch('verify-hosted-upgrade.yml')
    # The read-only full-history audit can run while CI and startup proof finish.
    # An upgrade intent is written only once those independent checks pass.
    wait_for(checked)
    if client.request('actions/workflows/hosted-control.yml/runs?per_page=1')['workflow_runs'][0]['id'] != stop['id']:
        raise ValueError('Operator control changed during drain')
    if client.request('git/ref/heads/wake-hosted-state')['object']['sha'] != checkpoint_ref:
        raise ValueError('Checkpoint changed during audit dispatch')
    latest, sha = read_policy(client)
    selected = latest['installations'][client.repository]
    if selected != binding:
        raise ValueError('Installation binding changed during repair preparation')
    selected['pending_upgrade'] = {
        'candidate': candidate, 'baseline': baseline, 'verification_run': verification['id'],
        'checkpoint_ref': checkpoint_ref, 'generation': manifest['generation'], 'control_run': stop['id'],
        'drained_run': drained['id'], 'superseded_queued_runs': superseded,
        'superseded_queued_baselines': original_bindings,
    }
    write_policy(client, latest, sha, 'Request verified hosted context budget rollout ' + candidate[:12])
    audit = client.request('actions/runs/' + str(verification['id']))
    if audit['status'] == 'completed' and audit['conclusion'] == 'success':
        client.request('actions/workflows/complete-hosted-upgrade.yml/dispatches',
                       method='POST', body={'ref': 'master', 'inputs': {}})
    print(json.dumps({'stage': 'requested-existing-upgrade-gate', 'candidate': candidate,
                      'verification_run': verification['id'], 'generation': manifest['generation']}), flush=True)


if __name__ == '__main__':
    main()
