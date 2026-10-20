#!/usr/bin/env python3
"""Upload an already generated installation mirror; never execute research."""
import argparse
import json
import os
from pathlib import Path
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from wake.installation_cli import upload_public_artifact


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', type=Path, required=True)
    parser.add_argument('--refresh-hosted-status', action='store_true', help='Refresh only generated hosted presentation, preserving captured research')
    parser.add_argument('--expected-head', help='Exact public branch parent captured for a presentation refresh')
    args = parser.parse_args(argv)
    manifest = json.loads((args.artifact / 'installation.json').read_text())
    if manifest.get('live') is not False or len(manifest.get('nodes', [])) != 12:
        raise ValueError('Publish requires a twelve-node, snapshot-only public artifact')
    repository = os.environ.get('WAKE_PUBLISH_REPOSITORY', '')
    if args.refresh_hosted_status:
        if not args.expected_head:
            raise ValueError('Presentation refresh requires the captured public head')
        from wake.hosted_presentation import bind_hosted_status
        name = repository.removeprefix('https://github.com/').removeprefix('git@github.com:').removesuffix('.git')
        revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
        manifest = bind_hosted_status(args.artifact, name, revision)
    upload_public_artifact(args.artifact, repository,
                           os.environ.get('WAKE_PUBLISH_BRANCH', ''), expected_head=args.expected_head)
    print(json.dumps({'status':'uploaded-snapshot','installation_id':manifest['installation_id'],
                      'generated':manifest['generated'],'nodes':len(manifest['nodes'])}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
