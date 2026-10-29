#!/usr/bin/env python3
"""Automatic presentation checks; exact mechanical fixes and isolated model proposals.

No native record or runtime control is opened. Only a trusted, reproducible cache
key transformation can advance master. Model output remains on a review branch.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import self_correction as source

SCHEMA = 'wake-automatic-correction@1'
INDEX = 'wake/assets/self-correction/index.html'
ASSETS = ('self-correction.js', 'self-correction.css')
OUTCOMES = {'healthy', 'repaired', 'republished', 'review_required', 'provider_wait',
            'outside_scope', 'budget_wait', 'failed'}


def api(root, path):
    return json.loads(source.gh(root, 'api', path))


def outputs(**values):
    target = os.environ.get('GITHUB_OUTPUT')
    if target:
        with open(target, 'a') as stream:
            for key, value in values.items():
                source.require('\n' not in str(value), 'Invalid workflow output')
                stream.write(f'{key}={value}\n')


def tracked(root, path):
    """Use committed bytes only, including symlink-parent and clean-base checks."""
    p = root / path
    source.require(p.is_file() and not p.is_symlink(), 'Expected regular source file')
    parts = Path(path).parts
    source.require(all(not root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts))),
                   'Symlinked source directory')
    value = subprocess.check_output(['git', '-C', str(root), 'cat-file', 'blob', f'HEAD:{path}'])
    source.require(p.read_bytes() == value, 'Source differs from committed base')
    source.require(len(value) <= source.MAX_FILE_BYTES, 'Source file exceeds limit')
    return value


def mechanical_plan(root):
    """The entire auto-applied language: replace two local asset query keys."""
    original = tracked(root, INDEX).decode('utf-8')
    updated = original
    for asset in ASSETS:
        digest = source.sha(tracked(root, 'wake/assets/self-correction/' + asset))[:12]
        pattern = rf'(?P<prefix>(?:src|href)="{re.escape(asset)}\?v=)[A-Za-z0-9_.-]+(?P<suffix>")'
        source.require(len(re.findall(pattern, updated)) == 1, 'Expected one exact local asset reference')
        updated = re.sub(pattern, lambda m: m['prefix'] + digest + m['suffix'], updated)
    if updated == original:
        return None
    return {'schema': SCHEMA, 'base_revision': source.git(root, 'rev-parse', 'HEAD'),
            'kind': 'asset_cache_keys', 'path': INDEX, 'before_sha256': source.sha(original.encode()),
            'content': updated}


def validate_mechanical(root, plan):
    source.require(plan == mechanical_plan(root) and plan is not None,
                   'Candidate is not the exact trusted mechanical repair')
    return plan


def eligible_syntax_faults(root):
    faults = []
    paths = source.git(root, 'ls-files', 'wake/assets/*.js').splitlines()
    for path in paths:
        try:
            source.allowed_path(path)
        except ValueError:
            continue
        if (root / path).stat().st_size > source.MAX_FILE_BYTES:
            continue
        data = source.source_file(root, path)
        result = subprocess.run(['node', '--input-type=module', '--check'], input=data,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
        if result.returncode:
            # Source and parser diagnostics are untrusted model input, not instructions.
            faults.append(path)
    return faults


def recent_attempts(root, repository, now):
    data = api(root, f'repos/{repository}/actions/workflows/self-correction.yml/runs?per_page=100')
    runs = data['workflow_runs']
    today = now.date().isoformat()
    current = os.environ.get('GITHUB_RUN_ID')
    if len(runs) == 100 and runs[-1]['created_at'][:10] >= today:
        return None
    attempts = []
    for run in runs:
        if str(run['id']) == current or run['created_at'][:10] != today:
            continue
        jobs = api(root, f'repos/{repository}/actions/runs/{run["id"]}/jobs?per_page=100')['jobs']
        # A failed/interrupted attempt still consumes capacity; skipped jobs do not.
        for job in jobs:
            kind = 'republish' if job['name'].startswith('republish / ') else job['name']
            if kind in ('propose', 'republish', 'test') and job.get('conclusion') != 'skipped' and job.get('started_at'):
                attempts.append((kind, run['head_sha']))
    return attempts


def model_budget(root, repository, base, now):
    attempts = recent_attempts(root, repository, now)
    if attempts is None:
        return False, 'Daily attempt history is incomplete; no model request was made.'
    proposed = [revision for kind, revision in attempts if kind == 'propose']
    if base in proposed:
        return False, 'This source revision already had a repair attempt; awaiting review or new source.'
    return len(proposed) < 4, 'At most four automatic source-model requests per UTC day.'


def inspect(root, output, event, request='', paths='', model=source.MODEL, repository=None):
    source.require(not source.git(root, 'status', '--porcelain', '--untracked-files=no'), 'Tracked source has local edits')
    base = source.git(root, 'rev-parse', 'HEAD')
    report = {'schema': SCHEMA, 'base_revision': base, 'checked_at': datetime.now(timezone.utc).isoformat(),
              'mode': 'none', 'outcome': 'healthy', 'reason': 'No fault found by the supported presentation checks.',
              'research_records_opened': 0, 'provider_calls': 0}
    # Explicit requests remain an advanced optional override. An empty dispatch
    # executes the same automatic detector as workflow completion events.
    if request.strip():
        chosen = [p.strip() for p in paths.split(',') if p.strip()]
        source.capture(root, chosen)
        source.require(10 <= len(request.strip()) <= 4000, 'Invalid optional request')
        report.update(mode='model', request=request, paths=','.join(chosen), model=model)
    else:
        repair = mechanical_plan(root)
        faults = eligible_syntax_faults(root)
        if repair:
            report.update(mode='mechanical', reason='Local self-correction asset cache keys do not match their content.')
        elif faults and len(faults) <= source.MAX_FILES:
            report.update(mode='model', request='Repair the JavaScript syntax errors detected by node --check in these files. Preserve public interfaces and behavior. Make only syntax corrections. Files: ' + ', '.join(faults),
                          paths=','.join(faults), model=source.MODEL,
                          reason='The automatic JavaScript parser found a source defect.')
        elif faults:
            report.update(outcome='outside_scope', reason='More source faults than the bounded four-file repair allowance.')
        elif event.get('workflow_run', {}).get('name') == 'WAKE — Publish website' and event['workflow_run'].get('conclusion') in ('failure', 'timed_out'):
            checked = api(root, f'repos/{repository}/actions/workflows/test.yml/runs?branch=master&status=success&per_page=20')['workflow_runs']
            checked = [run for run in checked if run['head_branch'] == 'master' and run['event'] in ('push', 'workflow_dispatch')]
            attempts = recent_attempts(root, repository, datetime.now(timezone.utc))
            if checked and checked[0]['head_sha'] == base and attempts is not None and ('republish', base) not in attempts:
                report.update(mode='republish', reason='Retry the failed website publication once from independently checked source.')
            else:
                report.update(outcome='budget_wait', reason='Publication needs checked current source or has already had its one automatic retry today.')
        elif event.get('workflow_run', {}).get('conclusion') in ('failure', 'timed_out', 'cancelled'):
            report.update(outcome='outside_scope', reason='The preceding workflow did not complete successfully. No supported source fault was diagnosed; its run remains visible for investigation.')
        if repair:
            attempts = recent_attempts(root, repository, datetime.now(timezone.utc))
            if attempts is None or ('test', base) in attempts:
                report.update(mode='none', outcome='budget_wait', reason='This source already had a candidate test today or attempt history is incomplete. No repeated repair loop.')
            output.mkdir(parents=True)
            (output / 'mechanical.json').write_text(json.dumps(repair, indent=2) + '\n')
    if report['mode'] == 'model' and not request.strip():
        allowed, reason = model_budget(root, repository, base, datetime.now(timezone.utc))
        if not allowed:
            report.update(mode='none', outcome='budget_wait', reason=reason)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'check.json').write_text(json.dumps(report, indent=2) + '\n')
    outputs(base=base, mode=report['mode'], outcome=report['outcome'])
    print(json.dumps({k: report[k] for k in ('base_revision', 'mode', 'outcome', 'reason')}))
    return report


def prepare(root, directory):
    report = json.loads((directory / 'check.json').read_text())
    source.require(report['base_revision'] == source.git(root, 'rev-parse', 'HEAD'), 'Stale diagnosis')
    try:
        os.environ['CORRECTION_MODEL'] = report['model']
        source.generate(root, report['paths'].split(','), report['request'], directory / 'proposal')
    except ValueError as error:
        if re.search(r'HTTP (429|503)', str(error)):
            outputs(outcome='provider_wait')
        raise


def apply_mechanical(root, path):
    source.require(not source.git(root, 'status', '--porcelain', '--untracked-files=no'), 'Tracked source has local edits')
    plan = validate_mechanical(root, json.loads(path.read_text()))
    (root / INDEX).write_text(plan['content'])


def publish_mechanical(root, path, repository):
    """Recompute from trusted base after tests; never execute model output here."""
    plan = validate_mechanical(root, json.loads(path.read_text()))
    apply_mechanical(root, path)
    source.git(root, 'add', '--', INDEX)
    source.git(root, '-c', 'user.name=WAKE self-correction', '-c',
               'user.email=wake-self-correction@users.noreply.github.com',
               'commit', '-m', 'Repair self-correction asset cache keys automatically')
    head = source.git(root, 'rev-parse', 'HEAD')
    source.require(source.git(root, 'rev-list', '--parents', '-n', '1', head).split() == [head, plan['base_revision']], 'Unexpected repair history')
    # Git's non-forced ref update rejects a concurrent master change, including
    # after our last read. No merge API or force update can widen the tested tree.
    source.git(root, 'push', 'origin', f'{head}:refs/heads/master')
    source.gh(root, 'workflow', 'run', 'test.yml', '--ref', 'master')
    print(json.dumps({'outcome': 'repaired', 'head_revision': head,
                      'publication': 'CI requested; Pages delivery remains separately observed'}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['inspect', 'prepare', 'apply-mechanical', 'publish-mechanical'])
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--directory', type=Path, default=Path('/tmp/wake-auto-correction'))
    args = parser.parse_args()
    root = args.root.resolve()
    repository = os.environ.get('GITHUB_REPOSITORY', 'sudofx/wake')
    if args.operation == 'inspect':
        event_path = os.environ.get('GITHUB_EVENT_PATH')
        event = json.loads(Path(event_path).read_text()) if event_path else {}
        inspect(root, args.directory, event, os.environ.get('CORRECTION_REQUEST', ''),
                os.environ.get('CORRECTION_PATHS', ''), os.environ.get('CORRECTION_MODEL') or source.MODEL, repository)
    elif args.operation == 'prepare':
        prepare(root, args.directory)
    elif args.operation == 'apply-mechanical':
        apply_mechanical(root, args.directory / 'mechanical.json')
    else:
        publish_mechanical(root, args.directory / 'mechanical.json', repository)


if __name__ == '__main__':
    main()
