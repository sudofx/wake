"""Restore a lost GitHub handoff only while the operator continuation latch is open.

This transport watchdog never reads public projections as authority. It retries
only a timed-out run or a failed successor-dispatch job; application failures
remain visible for diagnosis. A new wake verifies/restores its authoritative
checkpoint and accounts interrupted invocations before any provider effect.
"""
import json
import os
import subprocess
import sys
import tempfile
import tomllib
from datetime import datetime, timezone
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))


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


def quota_retry_token(now):
    """Return a stable dispatch token for this scheduled 15-minute retry slot."""
    now = now.astimezone(timezone.utc)
    slot_minute = now.minute - now.minute % 15
    slot = now.replace(minute=slot_minute, second=0, microsecond=0)
    return 'quota-retry-' + slot.strftime('%Y%m%dT%H%MZ')


def authoritative_quota_status():
    """Read the quota boundary from wake-state; live projections are never authority."""
    from scripts.github_wake import ROOT, StateBranch
    from wake.authority import open_authoritative_store
    from wake.engine import DEFAULTS
    from wake.scheduling import wake_status

    with tempfile.TemporaryDirectory(prefix='wake-quota-check-') as folder:
        checkout = Path(folder) / 'state'
        branch = StateBranch(ROOT, checkout)
        try:
            branch.open()
            store = open_authoritative_store(checkout / 'data', allow_initialize=False)
            try:
                settings_file = ROOT / 'wake.toml'
                settings = {**DEFAULTS,
                            **(tomllib.loads(settings_file.read_text()) if settings_file.exists() else {})}
                daily_limit = None if settings.get('model_daily_call_limits') else settings['daily_call_limit']
                return wake_status(store.load(), daily_call_limit=daily_limit)
            finally:
                store.close()
        finally:
            if checkout.exists():
                branch.git('worktree', 'remove', '--force', str(checkout), check=False)


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
    now = datetime.now(timezone.utc)
    token = None
    if not reason:
        if any(run['status'] != 'completed' for run in runs if run['head_sha'] == runtime):
            print('A WAKE cycle is active; no duplicate quota retry.')
            return
        quota = authoritative_quota_status()
        token = quota_retry_token(now) if quota.get('provider_quota_limited') else None
        eligible = quota.get('next_eligible')
        if eligible:
            try:
                due = datetime.fromisoformat(str(eligible).replace('Z', '+00:00'))
                if due.tzinfo is None:
                    due = due.replace(tzinfo=timezone.utc)
                if due > now:
                    token = None
            except (TypeError, ValueError):
                token = None
        if not token:
            print('No provider quota retry is due.')
            return
        if any(token in str(run.get('display_title', '')) for run in runs):
            print('Provider quota retry was already dispatched in this 15-minute slot.')
            return
        reason = 'provider-quota-retry'
    # Recheck intent and executable identity immediately before dispatch. A
    # concurrent Stop still closes/drains this lane and the cycle checks its pin.
    if (api(repository, 'actions/workflows/wake-runner.yml')['state'] != 'active'
            or api(repository, 'git/ref/heads/wake-runtime')['object']['sha'] != runtime):
        return
    dispatch_token = token or f'recovery-{os.environ["GITHUB_RUN_ID"]}'
    subprocess.run(['gh', 'workflow', 'run', 'wake.yml', '--repo', repository, '--ref', 'wake-runtime',
                    '-f', f'runtime_ref={runtime}', '-f', f'dispatch_token={dispatch_token}'],
                   check=True, timeout=30)
    print(json.dumps({'continuation_recovery': reason, 'runtime': runtime}))


if __name__ == '__main__':
    main()
