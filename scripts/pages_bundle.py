"""Bound the disposable Pages fallback; complete public exports stay on GitHub."""
import json
import hashlib
from pathlib import Path
import posixpath
import re
from urllib.parse import urlsplit, urlunsplit

from wake.installation_cli import NODE_IDS
from wake.reader_transport import COLLECTIONS, record_path

DATA_BUDGET = 8 * 1024 * 1024
DETAIL_LIMIT = 512 * 1024
OVERVIEW_LIMIT = 4 * 1024 * 1024
ASSET_SUFFIXES = {'.js', '.css', '.svg', '.png', '.jpg', '.jpeg', '.webp', '.ico', '.woff', '.woff2', '.wasm'}
# Share scripts with static HTML entry points. Leave scripts that derive a
# node root from their URL or load dynamically from the document directory local.
SHARED_SCRIPTS = {'ant-colony.js', 'ant-drawing.js', 'ant-experiment.js', 'ant-farm.js',
                  'bob-ant-farm.js', 'console-component.js', 'console-layout.js', 'console-tools.js',
                  'flat-view.js', 'hosted-status.js', 'map.js', 'map3d.js', 'nav.js',
                  'process-field.js', 'reader-data.js', 'research-instruments.js',
                  'research-scene.js', 'research.js', 'site-theme.js'}
CSS_URL = re.compile(r'''url\(\s*(["']?)([^\s)"']+)\1\s*\)''')
HTML_ASSET = re.compile(r'''(\b(?:href|src)=)(["'])([^"']+)\2''')


def share_assets(site, root, keep, root_assets):
    """Use one URL for exact shared assets while leaving node-bound files local."""
    if root == site:
        return 0, 0
    matches = {}
    for path in keep:
        name = path.relative_to(root)
        shared = site / name
        if shared not in root_assets:
            continue
        if not (name.parts[0] in ('backgrounds', 'icons') or name.name == 'nebula-bg.webp'
                or name.suffix == '.css' or name.name in SHARED_SCRIPTS):
            continue
        if path.stat().st_size == shared.stat().st_size and path.read_bytes() == shared.read_bytes():
            matches[path] = shared

    def local_target(value, source):
        try:
            url = urlsplit(value)
        except ValueError:
            return None, None
        if url.scheme or url.netloc or not url.path or url.path.startswith('/'):
            return None, url
        return Path(posixpath.normpath((source.parent / url.path).as_posix())), url

    for path in tuple(matches):
        if path.suffix == '.css':
            css = path.read_text()
            if '@import' in css:
                del matches[path]
                continue
            for match in CSS_URL.finditer(css):
                dependency, _ = local_target(match[2], path)
                if dependency is not None and dependency.suffix in ASSET_SUFFIXES and dependency not in matches:
                    del matches[path]
                    break
        elif path.name == 'ant-drawing.js' and root / 'backgrounds/ant-body-v1.png' not in matches:
            del matches[path]

    def share_url(value, source):
        dependency, url = local_target(value, source)
        if dependency not in matches:
            return value
        relative = posixpath.relpath(matches[dependency].as_posix(), source.parent.as_posix())
        return urlunsplit(('', '', relative, url.query, url.fragment))

    for path in keep - matches.keys():
        if path.suffix == '.html':
            text = path.read_text()
            text = HTML_ASSET.sub(lambda m: m[1] + m[2] + share_url(m[3], path) + m[2], text)
            path.write_text(text)
        elif path.suffix == '.css':
            text = path.read_text()
            def css_url(match):
                target = share_url(match[2], path)
                return 'url(' + match[1] + target + match[1] + ')' if target != match[2] else match[0]
            text = CSS_URL.sub(css_url, text)
            path.write_text(text)
        elif path.name == 'manifest.webmanifest':
            manifest = json.loads(path.read_text())
            for icon in manifest.get('icons', []):
                icon['src'] = share_url(icon['src'], path)
            path.write_text(json.dumps(manifest))
    size = sum(path.stat().st_size for path in matches)
    for path in matches:
        path.unlink()
    return len(matches), size


def compact(site):
    site = Path(site).resolve()
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
        for row in data['state'].get('journal', []):
            retain(record_path('journal', 'cycle:' + str(row['cycle'])), DETAIL_LIMIT)
            if row.get('invocation'):
                retain(record_path('journal', row['invocation']), DETAIL_LIMIT)
        for path in root.rglob('*'):
            if not path.is_file():
                continue
            relative = path.relative_to(root)
            if 'nodes' in relative.parts:
                continue
            if path.suffix in ASSET_SUFFIXES or path.name.endswith('.LICENSE.txt'):
                keep.add(path)
            elif path.suffix == '.html' and path.parent == root:
                keep.add(path)
        plans.append((root, keep, used))
    # Resolve every mandatory file/budget before deleting anything.
    hashes={path:hashlib.sha256(path.read_bytes()).digest() for root,keep,_ in plans for path in keep
            if path.name not in ('installation.json','deployment.json') and
            path.suffix in ('.json','.txt','.md')}
    removed = shared_files = shared_bytes = 0
    for root, keep, used in plans:
        for path in root.rglob('*'):
            if path.is_file() and 'nodes' not in path.relative_to(root).parts and path not in keep:
                path.unlink(); removed += 1
        deployment = json.loads((root / 'deployment.json').read_text())
        deployment['public_data']['fallback'] = 'recent-overview'
        (root / 'deployment.json').write_text(json.dumps(deployment))
        for path in keep:
            if path.suffix != '.html':
                continue
            def binding(match):
                bound = json.loads(match.group(1))
                if 'public_data' in bound:
                    bound['public_data']['fallback'] = 'recent-overview'
                return 'window.WAKE_DEPLOYMENT=' + json.dumps(bound) + ';'
            page = path.read_text()
            path.write_text(re.sub(r'window\.WAKE_DEPLOYMENT=(\{[^<]*?\});', binding, page))
        count, size = share_assets(site, root, keep, plans[0][1])
        shared_files += count
        shared_bytes += size
    manifest['presentation']['fallback'] = {'kind':'recent-overview', 'data_budget_per_root_bytes':DATA_BUDGET,
        'retained_data_bytes':sum(used for _, _, used in plans), 'omitted_files':removed,
        'complete_data':'wake-public', 'shared_asset_files':shared_files,
        'shared_asset_bytes':shared_bytes}
    encoded = json.dumps(manifest, sort_keys=True)
    for root, _, _ in plans:
        (root / 'installation.json').write_text(encoded)
    if any(hashlib.sha256(path.read_bytes()).digest()!=digest for path,digest in hashes.items()):
        raise ValueError('A retained fallback packet changed')
    for path in sorted(site.rglob('*'), key=lambda p:len(p.parts), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    return manifest
