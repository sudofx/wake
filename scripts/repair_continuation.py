"""Restore a lost GitHub handoff only while the operator continuation latch is open.

This transport watchdog never reads public projections as authority. It retries
only a timed-out run or a failed successor-dispatch job; application failures
remain visible for diagnosis. A new wake verifies/restores its authoritative
checkpoint and accounts interrupted invocations before any provider effect.
"""
import json
import os
import subprocess
from datetime import datetime, timezone


def api(repository, path):
    result = subprocess.run(['gh', 'api', f'repos/{repository}/{path}'],
                            check=True, capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout)


def recovery_reason(runs, jobs, runtime, now):
    current = [run for run in runs if run['head_sha'] == runtime and run['head_branch'] == 'wake-runtime']
    for run in current:
        if run['status'] == 'completed':
            continue
        age = (now - datetime.fromisoformat(run['created_at'].replace('Z', '+00:00'))).total_seconds()
        # GitHub sometimes retains queued entries with no allocated job forever.
        # A newly queued dispatch must have time to acquire its runner.
        if run['status'] == 'queued' and not jobs.get(run['id']) and age >= 120:
            continue
        return None
    completed = sorted((run for run in current if run['status'] == 'completed'),
                       key=lambda run: run['created_at'], reverse=True)
    if not completed:
        return None
    latest = completed[0]
    if latest['conclusion'] == 'timed_out':
        return 'execution-timeout'
    handoff = next((job for job in jobs.get(latest['id'], []) if job['name'] == 'continue-again'), None)
    if handoff and handoff['conclusion'] in ('failure', 'timed_out'):
        return 'successor-dispatch-failed'
    return None


def main():
    repository = os.environ['GITHUB_REPOSITORY']
    if api(repository, 'actions/workflows/wake-runner.yml')['state'] != 'active':
        print('Operator continuation is closed; no recovery dispatch.')
        return
    for workflow in ('operator-stop.yml', 'operator-restart.yml', 'operator-reset.yml', 'promote-runtime.yml'):
        runs = api(repository, f'actions/workflows/{workflow}/runs?per_page=20')['workflow_runs']
        if any(run['status'] != 'completed' for run in runs):
            print('Operator maintenance is active; no recovery dispatch.')
            return
    runtime = api(repository, 'git/ref/heads/wake-runtime')['object']['sha']
    runs = api(repository, 'actions/workflows/wake.yml/runs?branch=wake-runtime&per_page=20')['workflow_runs']
    jobs = {run['id']: api(repository, f"actions/runs/{run['id']}/jobs?per_page=100")['jobs']
            for run in runs if run['head_sha'] == runtime}
    reason = recovery_reason(runs, jobs, runtime, datetime.now(timezone.utc))
    if not reason:
        print('No recoverable handoff loss; research is active or requires diagnosis.')
        return
    # Recheck intent and executable identity immediately before dispatch. A
    # concurrent Stop still closes/drains this lane and the cycle checks its pin.
    if (api(repository, 'actions/workflows/wake-runner.yml')['state'] != 'active'
            or api(repository, 'git/ref/heads/wake-runtime')['object']['sha'] != runtime):
        return
    subprocess.run(['gh', 'workflow', 'run', 'wake.yml', '--repo', repository, '--ref', 'wake-runtime',
                    '-f', f'runtime_ref={runtime}', '-f', f'dispatch_token=recovery-{os.environ["GITHUB_RUN_ID"]}'],
                   check=True, timeout=30)
    print(json.dumps({'continuation_recovery': reason, 'runtime': runtime}))


if __name__ == '__main__':
    main()
