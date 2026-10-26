"""Bound the disposable Pages fallback; complete public exports stay on GitHub."""
import json
import hashlib
from pathlib import Path
import re

from wake.installation_cli import NODE_IDS
from wake.reader_transport import COLLECTIONS, record_path

DATA_BUDGET = 8 * 1024 * 1024
DETAIL_LIMIT = 512 * 1024
OVERVIEW_LIMIT = 4 * 1024 * 1024
ASSET_SUFFIXES = {'.js', '.css', '.svg', '.png', '.jpg', '.jpeg', '.webp', '.ico', '.woff', '.woff2', '.wasm'}


def compact(site):
    site = Path(site)
    manifest = json.loads((site / 'installation.json').read_text())
    if (manifest.get('live') is not False or
            manifest.get('presentation', {}).get('data_transport') != 'github-pinned@1'):
        raise ValueError('Bounded Pages payload requires a bound public snapshot')
    # This operation owns an export, never an installation or authority record.
    if any(p.is_symlink() or p.suffix in ('.sqlite', '.sqlite3') for p in site.rglob('*')):
        raise ValueError('Native records may not enter a Pages payload')
    roots = [site, *(site / 'nodes' / node for node in NODE_IDS)]
    if any(not (root / 'reader-data.json').is_file() for root in roots):
        raise ValueError('Every fallback node requires its bounded reader overview')
    plans = []
    for root in roots:
        keep, used = set(), 0
        def retain(relative, limit, *, required=False):
            nonlocal used
            path = root / relative
            if not path.is_file():
                if required:
                    raise ValueError('Missing required Pages overview: ' + relative)
                return
            if path in keep:
                return
            size = path.stat().st_size
            if size > limit or used + size > DATA_BUDGET:
                if required:
                    raise ValueError('Pages overview exceeds its fixed fallback budget')
                return
            keep.add(path); used += size
        for name in ('installation.json', 'deployment.json', 'reader-data.json'):
            retain(name, OVERVIEW_LIMIT, required=True)
        retain('research-overview.json', OVERVIEW_LIMIT)
        for name in ('head.txt', 'map3d-data.json', 'map-data.json', 'export-format.json',
                     'blog.xml', 'journal.xml', 'manifest.webmanifest', 'robots.txt', 'CNAME', '.nojekyll'):
            retain(name, DETAIL_LIMIT)
        for name in ('journal', 'events', 'evidence'):
            retain('reader-records/pages/' + name + '/0.json', DETAIL_LIMIT)
        data = json.loads((root / 'reader-data.json').read_text())
        for collection in COLLECTIONS:
            for identifier in data['state'].get(collection, {}):
                retain(record_path(collection, identifier), DETAIL_LIMIT)
                if collection == 'posts':
                    retain(record_path('guides', identifier), DETAIL_LIMIT)
        for row in data['state'].get('journal', []):
            retain(record_path('journal', 'cycle:' + str(row['cycle'])), DETAIL_LIMIT)
            if row.get('invocation'):
                retain(record_path('journal', row['invocation']), DETAIL_LIMIT)
        # The self-contained inspection demonstration is small, dated evidence.
        for path in sorted((root / 'inspect').glob('*')):
            if path.is_file():
                retain(str(path.relative_to(root)), DETAIL_LIMIT)
        gpu_manifest=root/'ask-bob-gpu-engine.json'
        gpu_files=set(json.loads(gpu_manifest.read_text())['files']) if gpu_manifest.exists() else set()
        for path in root.rglob('*'):
            if not path.is_file():
                continue
            relative = path.relative_to(root)
            if 'nodes' in relative.parts:
                continue
            if path.name.startswith('ask-bob-engine'):
                continue  # Retired CPU inference is not the public chat path.
            if path.name.startswith('ask-bob-gpu-') and path.suffix=='.wasm' and path.name not in gpu_files:
                continue
            if path.suffix in ASSET_SUFFIXES or path.name.endswith('.LICENSE.txt'):
                keep.add(path)
            elif path.suffix == '.html' and (path.parent == root or 'self-correction' in relative.parts):
                keep.add(path)
            elif path.name == 'ask-bob-gpu-engine.json':
                keep.add(path)
        plans.append((root, keep, used))
    # Resolve every mandatory file/budget before deleting anything.
    hashes={path:hashlib.sha256(path.read_bytes()).digest() for root,keep,_ in plans for path in keep
            if path.name not in ('installation.json','deployment.json') and
            (path.suffix in ('.json','.txt','.md') or 'inspect' in path.relative_to(root).parts)}
    removed = 0
    for root, keep, used in plans:
        for path in root.rglob('*'):
            if path.is_file() and 'nodes' not in path.relative_to(root).parts and path not in keep:
                path.unlink(); removed += 1
        deployment = json.loads((root / 'deployment.json').read_text())
        deployment['public_data']['fallback'] = 'recent-overview'
        (root / 'deployment.json').write_text(json.dumps(deployment))
        for path in keep:
            if path.suffix != '.html' or 'inspect' in path.relative_to(root).parts:
                continue
            def binding(match):
                bound = json.loads(match.group(1))
                if 'public_data' in bound:
                    bound['public_data']['fallback'] = 'recent-overview'
                return 'window.WAKE_DEPLOYMENT=' + json.dumps(bound) + ';'
            page = path.read_text()
            path.write_text(re.sub(r'window\.WAKE_DEPLOYMENT=(\{[^<]*?\});', binding, page))
    manifest['presentation']['fallback'] = {'kind':'recent-overview', 'data_budget_per_root_bytes':DATA_BUDGET,
        'retained_data_bytes':sum(used for _, _, used in plans), 'omitted_files':removed,
        'complete_data':'wake-public'}
    encoded = json.dumps(manifest, sort_keys=True)
    for root, _, _ in plans:
        (root / 'installation.json').write_text(encoded)
    if any(hashlib.sha256(path.read_bytes()).digest()!=digest for path,digest in hashes.items()):
        raise ValueError('A retained fallback packet changed')
    for path in sorted(site.rglob('*'), key=lambda p:len(p.parts), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    return manifest
