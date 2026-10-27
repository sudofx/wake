#!/usr/bin/env python3
"""Publish one disposable evaluation report as GitHub data, without website jobs."""
import argparse
import json
import re
from pathlib import Path
import subprocess

BRANCH = 'wake-evaluations'
MAX_BYTES = 2 * 1024 * 1024


def api(repository, resource, method='GET', body=None):
    result = subprocess.run(['gh', 'api', 'repos/'+repository+'/'+resource,
                             '--method', method, *(['--input', '-'] if body is not None else [])],
                            input=json.dumps(body).encode() if body is not None else None,
                            capture_output=True, check=True)
    return json.loads(result.stdout) if result.stdout.strip() else None


def publish(repository, report, *, initialize=False):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Expected owner/repository')
    content = json.dumps(report, ensure_ascii=False)+'\n'
    if len(content.encode()) > MAX_BYTES or report.get('schema') != 'wake-evaluation@1':
        raise ValueError('Expected a bounded wake-evaluation@1 report')
    try:
        parent = api(repository, 'git/ref/heads/'+BRANCH)['object']['sha']
    except subprocess.CalledProcessError as error:
        # A missing branch is the only condition that permits explicit creation.
        if not initialize or b'HTTP 404' not in error.stderr:
            raise
        parent = None
    blob = api(repository, 'git/blobs', 'POST', {'content': content, 'encoding': 'utf-8'})
    tree = api(repository, 'git/trees', 'POST', {'tree': [
        {'path': 'latest.json', 'mode': '100644', 'type': 'blob', 'sha': blob['sha']}]})
    commit = api(repository, 'git/commits', 'POST', {
        'message': 'Publish evaluation '+str(report['result_id']), 'tree': tree['sha'],
        'parents': [parent] if parent else []})
    if parent:
        api(repository, 'git/refs/heads/'+BRANCH, 'PATCH', {'sha': commit['sha'], 'force': False})
    else:
        api(repository, 'git/refs', 'POST', {'ref': 'refs/heads/'+BRANCH, 'sha': commit['sha']})
    return {'branch': BRANCH, 'revision': commit['sha'], 'result_id': report['result_id']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--repository', required=True)
    parser.add_argument('--initialize', action='store_true')
    args = parser.parse_args()
    if args.report.stat().st_size > MAX_BYTES:
        raise ValueError('Report exceeds 2 MiB')
    print(json.dumps(publish(args.repository, json.loads(args.report.read_text()),
                             initialize=args.initialize)))


if __name__ == '__main__':
    main()
