#!/usr/bin/env python3
"""Apply checked presentation to a captured public export, without record access."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from wake.hosted_presentation import bind_hosted_status
from wake.reader_presentation import retired_reader_asset


def protected_files(root):
    """Research and inspection packets must survive a presentation release exactly."""
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and
            (p.suffix in ('.json', '.jsonl', '.txt') or 'inspect' in p.relative_to(root).parts)
            and p.name not in ('deployment.json', 'installation.json')
            and 'self-correction' not in p.relative_to(root).parts
            and not retired_reader_asset(p)}


def prepare(root, repository, revision):
    root = Path(root)
    before = protected_files(root)
    original = json.loads((root / 'installation.json').read_text())
    result = bind_hosted_status(root, repository, revision)
    if result['record_heads'] != original['record_heads'] or protected_files(root) != before:
        raise ValueError('Presentation changed a research or inspection packet')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', type=Path, required=True)
    parser.add_argument('--repository', required=True)
    parser.add_argument('--revision', required=True)
    parser.add_argument('--bounded-fallback', action='store_true', help='Ship bounded recent views instead of full public history')
    args = parser.parse_args()
    result = prepare(args.artifact, args.repository, args.revision)
    if args.bounded_fallback:
        from scripts.pages_bundle import compact
        result = compact(args.artifact)
    print(json.dumps({'installation_id': result['installation_id'],
                      'presentation_revision': args.revision, 'record_heads_preserved': True}))
