#!/usr/bin/env python3
"""Upload an already generated installation mirror; never execute research."""
import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from wake.installation_cli import upload_public_artifact


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', type=Path, required=True)
    args = parser.parse_args(argv)
    manifest = json.loads((args.artifact / 'installation.json').read_text())
    if manifest.get('live') is not False or len(manifest.get('nodes', [])) != 12:
        raise ValueError('Publish requires a twelve-node, snapshot-only public artifact')
    upload_public_artifact(args.artifact, os.environ.get('WAKE_PUBLISH_REPOSITORY', ''),
                           os.environ.get('WAKE_PUBLISH_BRANCH', ''))
    print(json.dumps({'status':'uploaded-snapshot','installation_id':manifest['installation_id'],
                      'generated':manifest['generated'],'nodes':len(manifest['nodes'])}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
