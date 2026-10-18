"""Static external inspection of architecture, fixture evidence and dated exports.

This exporter opens public presentation files only. It never opens authority,
contacts a provider, infers executing code from the checkout, or enables a service.
"""
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import unquote, urlsplit

from .reader_transport import record_path

CANONICAL_ROOT = 'https://sudofx.github.io/wake/inspect/'
MAX_RESOURCE_BYTES = 256 * 1024
RESOURCES = (
    ('readme', 'README.md', 'text/markdown', 'Start here: scope and how to inspect this packet.'),
    ('architecture', 'architecture.md', 'text/markdown', 'Authority, context and proposal boundaries.'),
    ('evidence', 'evidence.md', 'text/markdown', 'Reproducible demonstration and dated public-export pointers.'),
    ('limitations', 'limitations.md', 'text/markdown', 'What the demonstration and exported records cannot establish.'),
    ('evaluate', 'evaluate.md', 'text/markdown', 'Questions an external reviewer can evaluate independently.'),
    ('demo', 'demo.json', 'application/json', 'Actual offline task-list kernel events and replay result.'),
    ('packet', 'packet.md', 'text/markdown', 'Self-contained inspection document, including the exact offline demonstration.'),
    ('index', 'index.html', 'text/html', 'Static inspection entry page; no JavaScript or service required.'),
)
PUBLIC_FILES = frozenset(filename for _, filename, _, _ in RESOURCES) | {'manifest.json'}


def _json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + '\n'


def _read_json(path, maximum=MAX_RESOURCE_BYTES):
    with Path(path).open('rb') as stream:
        raw = stream.read(maximum + 1)
    if len(raw) > maximum:
        raise ValueError('Inspection input exceeds its public transport bound')
    return json.loads(raw)


def _snapshot(reader, projection):
    source = projection.get('source', {}) if isinstance(projection, dict) else {}
    heads = source.get('node_heads', {})
    captured = {}
    if not isinstance(heads, dict) or len(heads) > 12:
        raise ValueError('Invalid inspection node-head metadata')
    for node, item in sorted(heads.items()):
        if not re.fullmatch(r'[123]0[0-3](?:\.wake)?', node) or not isinstance(item, dict):
            raise ValueError('Invalid inspection node identity')
        captured[node] = {key: item[key] for key in ('node', 'head', 'version', 'snapshot_digest', 'generated')
                          if key in item and (isinstance(item[key], str) and len(item[key]) <= 128
                                              or type(item[key]) is int and item[key] >= 0)}
    return {'head': reader.get('head'), 'version': reader.get('state', {}).get('version'),
            'generated_at': reader.get('generated'), 'authoritative': False,
            'version_meaning': 'Sum of accepted node cycles; not one authoritative record version.',
            'node_heads': captured}


def _record_pointers(target, reader):
    pointers = []
    for collection, limit in (('posts', 2), ('evidence', 2), ('notebooks', 1)):
        rows = reader.get('state', {}).get(collection, {})
        if not isinstance(rows, dict):
            continue
        for identifier in sorted(rows)[-limit:]:
            if not isinstance(identifier, str) or len(identifier) > 240:
                continue
            relative = record_path(collection, identifier)
            path = target / relative
            if not path.is_file() or path.is_symlink():
                continue
            # Read only one bounded exact public record at a time. Its head must
            # match the captured bootstrap, but its body is never copied here.
            try:
                packet = _read_json(path, maximum=512 * 1024)
            except (OSError, ValueError):
                continue
            if (packet.get('head') != reader.get('head') or packet.get('collection') != collection
                    or packet.get('item', {}).get('id') != identifier):
                continue
            pointers.append({'id': identifier, 'collection': collection,
                             'url': '../' + relative, 'head': reader['head']})
    return pointers


def export_inspection(target, projection=None):
    target = Path(target)
    assets = Path(__file__).parent / 'assets/inspection'
    destination = target / 'inspect'
    destination.mkdir(exist_ok=True)
    reader = _read_json(target / 'reader-data.json')
    deployment = _read_json(target / 'deployment.json', maximum=16_384)
    marker = _read_json(target / 'export-format.json', maximum=4096)
    if projection and projection.get('head') != reader.get('head'):
        raise ValueError('Inspection bootstrap differs from the unified snapshot')
    snapshot = _snapshot(reader, projection)
    pointers = _record_pointers(target, reader)
    for _, filename, _, _ in RESOURCES:
        if filename in {'README.md', 'architecture.md', 'evidence.md', 'limitations.md', 'evaluate.md', 'demo.json'}:
            raw = (assets / filename).read_bytes()
            if len(raw) > MAX_RESOURCE_BYTES:
                raise ValueError('Inspection source asset exceeds size limit')
            (destination / filename).write_bytes(raw)
    demo = _read_json(destination / 'demo.json')
    if demo.get('format') != 'wake-kernel-inspection@1':
        raise ValueError('Inspection requires the reproduced kernel demonstration')
    evidence = destination / 'evidence.md'
    with evidence.open('a') as stream:
        stream.write('\n\n## Captured public presentation\n\n'
                     'This is dated exported presentation, not a live status query or a second authority. '
                     'Generation time does not establish upload or serving time. The executing source revision is unknown.\n\n'
                     '```json\n' + _json(snapshot) + '```\n\n'
                     'Selected exact public records (bounded examples, not an exhaustive evidence review):\n\n')
        for entry in pointers:
            stream.write('- [' + entry['collection'] + ' record](' + entry['url'] + ')\n')
        if not pointers:
            stream.write('No matching bounded example records were available.\n')
        stream.write('\nFor complete history, read the current `event_history.complete_url` in '
                     '[the public export index](../wake-data.json); resolve that URL relative to the index, '
                     'not this inspection directory. The stream may be packaged as gzip.\n')
    packet = '# WAKE external inspection packet\n\nCanonical resource root: ' + CANONICAL_ROOT + '\n\n'
    for filename in ('README.md', 'architecture.md', 'evidence.md', 'limitations.md', 'evaluate.md'):
        packet += '\n\n---\n\n<!-- Source: ' + filename + ' -->\n\n' + (destination / filename).read_text()
    packet += '\n\n## Exact offline demonstration artifact\n\n```json\n' + _json(demo) + '```\n'
    if len(packet.encode()) > 64 * 1024:
        raise ValueError('Self-contained inspection packet exceeds 64 KiB')
    (destination / 'packet.md').write_text(packet)
    links = '<li><a href="manifest.json">Versioned manifest and resource hashes</a></li>' + ''.join('<li><a href="' + html.escape(filename, quote=True) + '">' + html.escape(description) + '</a></li>'
                    for _, filename, _, description in RESOURCES if filename != 'index.html')
    (destination / 'index.html').write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width">'
        '<title>External LLM inspection · WAKE</title><main><h1>External LLM inspection</h1>'
        '<p><a href="packet.md">Read or upload the self-contained inspection packet</a></p>'
        '<p>Inspect architecture, an offline kernel demonstration, and the limits of this dated public export. '
        'These files grant no research or execution authority.</p><ul>' + links + '</ul>'
        '<p><a href="../index.html">Return to WAKE</a></p></main></html>')
    resources = []
    for identifier, filename, kind, description in RESOURCES:
        raw = (destination / filename).read_bytes()
        resources.append({'id': identifier, 'type': kind, 'description': description, 'url': filename,
                          'canonical_url': CANONICAL_ROOT + filename,
                          'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
    manifest = {'format': 'wake-inspection@1', 'version': 1, 'project': 'WAKE✳︎', 'canonical_root': CANONICAL_ROOT,
                'generated_at': datetime.now(timezone.utc).isoformat(), 'uploaded_at': None,
                'source': {'executing_revision': None, 'revision_status': 'unknown',
                           'renderer': marker.get('renderer')},
                'deployment': {key: deployment[key] for key in ('schema', 'mode', 'snapshot_only', 'unified')
                               if key in deployment and isinstance(deployment[key], (str, int, bool))},
                'snapshot': snapshot, 'resources': resources, 'published_records': pointers,
                'claims': [
                    {'id': 'authority_boundary', 'kind': 'architecture', 'text': 'The architecture describes a single governed authority per node.',
                     'evidence_ids': ['architecture', 'limitations']},
                    {'id': 'offline_demonstration', 'kind': 'demonstrated_fixture', 'text': 'The supplied fixture records and replays three task-list decisions.',
                     'evidence_ids': ['demo', 'evidence', 'limitations']},
                ]}
    (destination / 'manifest.json').write_text(_json(manifest))
    validate_inspection(target)
    return manifest


def validate_inspection(target, *, allow_unlisted=False):
    target = Path(target)
    destination = target / 'inspect'
    manifest = _read_json(destination / 'manifest.json')
    if (manifest.get('format') != 'wake-inspection@1' or manifest.get('version') != 1
            or manifest.get('project') != 'WAKE✳︎'
            or manifest.get('canonical_root') != CANONICAL_ROOT
            or manifest.get('source', {}).get('executing_revision') is not None
            or manifest.get('uploaded_at') is not None):
        raise ValueError('Invalid inspection identity or deployment claim')
    actual = {path.name for path in destination.iterdir()}
    if not PUBLIC_FILES <= actual or (not allow_unlisted and actual != PUBLIC_FILES):
        raise ValueError('Unexpected inspection resources')
    resources = manifest.get('resources', [])
    if len(resources) != len(RESOURCES) or {item.get('url') for item in resources} != PUBLIC_FILES - {'manifest.json'}:
        raise ValueError('Invalid inspection resource index')
    expected = {identifier: (filename, kind) for identifier, filename, kind, _ in RESOURCES}
    if {item.get('id') for item in resources} != set(expected):
        raise ValueError('Invalid inspection resource identities')
    for resource in resources:
        filename, kind = expected[resource['id']]
        if (resource.get('url') != filename or resource.get('type') != kind
                or resource.get('canonical_url') != CANONICAL_ROOT + filename):
            raise ValueError('Invalid inspection resource reference')
        path = destination / filename
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_RESOURCE_BYTES:
            raise ValueError('Invalid inspection resource path or size')
        if filename != 'manifest.json':
            raw = path.read_bytes()
            if resource.get('sha256') != hashlib.sha256(raw).hexdigest() or resource.get('bytes') != len(raw):
                raise ValueError('Inspection resource hash mismatch')
    # Check the navigation that readers actually follow, including the Pages
    # project prefix. No network retrieval or executable browser is necessary.
    for filename in PUBLIC_FILES:
        if not filename.endswith(('.md', '.html')):
            continue
        content = (destination / filename).read_text(encoding='utf-8')
        links = re.findall(r'\]\(([^)]+)\)|href="([^"]+)"', content)
        for markdown, href in links:
            url = urlsplit(markdown or href)
            if url.scheme or url.netloc or not url.path:
                continue
            path = destination / unquote(url.path)
            if url.path.startswith('/') or not path.resolve().is_relative_to(target.resolve()) or not path.is_file():
                raise ValueError('Invalid inspection navigation link')
    for claim in manifest.get('claims', []):
        if (claim.get('kind') not in {'demonstrated_fixture', 'architecture', 'hypothesis', 'limitation'}
                or not claim.get('evidence_ids') or any(identifier not in expected for identifier in claim['evidence_ids'])):
            raise ValueError('Unattributed inspection claim')
    pointers = manifest.get('published_records', [])
    if len(pointers) > 5:
        raise ValueError('Too many inspection public-record references')
    for pointer in pointers:
        relative = pointer.get('url', '')
        if (pointer.get('collection') not in {'posts', 'evidence', 'notebooks'}
                or relative != '../' + record_path(pointer['collection'], pointer.get('id', ''))
                or pointer.get('head') != manifest['snapshot']['head']
                or not (destination / PurePosixPath(relative)).is_file()):
            raise ValueError('Invalid inspection public-record reference')
        packet = _read_json(destination / relative, maximum=512 * 1024)
        if (packet.get('head') != pointer['head'] or packet.get('collection') != pointer['collection']
                or packet.get('item', {}).get('id') != pointer['id']):
            raise ValueError('Inspection record identity mismatch')
    return manifest
