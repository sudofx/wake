"""Local operator commands and verified installation transport artifacts.

The controller owns draining and mutations. This client never opens a second
writer or deletes live data. Manual archives are separate from public exports.
"""
from __future__ import annotations

import argparse
import fcntl
from datetime import datetime, timezone
import hashlib
import json
import os
import re
from pathlib import Path
import shutil
import socket
import stat
import subprocess
import tempfile
import zipfile

from .kernel.record import Record
from .kernel.storage import GENESIS_HASH

NODE_IDS = tuple(f'{parent + child}.wake' for parent in (100, 200, 300) for child in range(4))
MAX_MESSAGE = 1024 * 1024
ARCHIVE_FORMAT = 'wake-installation-backup-v1'


def data_root() -> Path:
    return Path(os.environ.get('WAKE_INSTALLATION_DATA', '/data'))


def control_socket(root: Path) -> Path:
    """Docker Desktop bind mounts cannot carry Unix sockets; keep IPC local."""
    identity = hashlib.sha256(str(Path(root).resolve()).encode()).hexdigest()[:16]
    return Path('/tmp') / ('wake-research-' + identity + '.sock')


def _digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def _record_metadata(path: Path) -> dict:
    record = Record.open_read_only(path)
    revision, state = record.full_replay()
    from .application import WAKE_APPLICATION
    from .kernel.applications import application_state
    envelope = application_state(WAKE_APPLICATION, state.get('app:wake'))
    if not isinstance(envelope, dict) or not (envelope.get('state') or {}).get('objective'):
        raise ValueError('Archive requires initialized WAKE application authority')
    record.invocation_history()
    record.application_access_history()
    # Replay verifies semantics; the historical head identifies this exact chain.
    with record.connect() as connection:
        row = connection.execute('SELECT event_hash FROM events ORDER BY sequence DESC LIMIT 1').fetchone()
    return {'revision': revision, 'head': row[0] if row else GENESIS_HASH,
            'sha256': _digest(path)}


def export_records(root: Path, destination: Path) -> dict:
    """Snapshot every drained node; publish a complete archive atomically."""
    root, destination = Path(root), Path(destination)
    if destination.exists():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.wake-export-', dir=destination.parent) as temporary:
        staging = Path(temporary)
        manifest = {'format': ARCHIVE_FORMAT, 'created_at': datetime.now(timezone.utc).isoformat(), 'nodes': {}}
        for node in NODE_IDS:
            target = staging / 'nodes' / node / 'record' / 'wake.sqlite'
            Record.open_read_only(root / 'nodes' / node / 'record' / 'wake.sqlite').backup_to(target)
            manifest['nodes'][node] = _record_metadata(target)
        (staging / 'manifest.json').write_text(json.dumps(manifest, sort_keys=True))
        archive_path = staging / 'archive.zip'
        with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            archive.write(staging / 'manifest.json', 'manifest.json')
            for node in NODE_IDS:
                name = f'nodes/{node}/record/wake.sqlite'
                archive.write(staging / name, name)
        # An explicit export must not silently overwrite an existing manual copy.
        os.link(archive_path, destination)
    return manifest


def _verified_archive(archive_path: Path, staging: Path) -> dict:
    expected = {'manifest.json'} | {f'nodes/{node}/record/wake.sqlite' for node in NODE_IDS}
    with zipfile.ZipFile(archive_path) as archive:
        entries = archive.infolist()
        names = [entry.filename for entry in entries]
        if len(names) != len(set(names)) or set(names) != expected:
            raise ValueError('Archive must contain exactly the manifest and twelve node records')
        if sum(entry.file_size for entry in entries) > 8 * 1024**3:
            raise ValueError('Archive exceeds the installation size limit')
        for entry in entries:
            mode = entry.external_attr >> 16
            if stat.S_ISLNK(mode) or (stat.S_IFMT(mode) and not stat.S_ISREG(mode)):
                raise ValueError('Archive links and special files are forbidden')
            if entry.file_size > 8 * 1024**3 or (entry.filename == 'manifest.json' and entry.file_size > MAX_MESSAGE):
                raise ValueError('Archive member exceeds allowed size')
        manifest = json.loads(archive.read('manifest.json'))
        if manifest.get('format') != ARCHIVE_FORMAT or set(manifest.get('nodes', {})) != set(NODE_IDS):
            raise ValueError('Unsupported installation backup identity')
        # Fixed known paths are written individually; arbitrary extraction is forbidden.
        for node in NODE_IDS:
            name = f'nodes/{node}/record/wake.sqlite'
            target = staging / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(name) as source, target.open('wb') as output:
                shutil.copyfileobj(source, output)
            if _record_metadata(target) != manifest['nodes'][node]:
                raise ValueError(f'Node {node} record does not match its verified manifest')
    return manifest


def verify_import(archive: Path) -> dict:
    with tempfile.TemporaryDirectory(prefix='wake-import-check-') as temporary:
        return _verified_archive(Path(archive), Path(temporary))


def import_records(root: Path, archive: Path) -> dict:
    """Replace drained active nodes only after all imported records verify.

    Controller must stop every writer and leave research stopped after this call.
    Backups are outside nodes and remain untouched. No backup is manufactured.
    """
    root = Path(root)
    with tempfile.TemporaryDirectory(prefix='.wake-import-', dir=root) as temporary:
        staging = Path(temporary)
        manifest = _verified_archive(Path(archive), staging)
        active = root / 'nodes'
        retired = staging / 'retired'
        if active.exists():
            active.rename(retired)
        try:
            (staging / 'nodes').rename(active)
        except BaseException:
            if retired.exists():
                retired.rename(active)
            raise
    return manifest


_PUBLIC_OMIT = {'request', 'response', 'raw_response', 'system', 'credentials', 'api_key',
                'authorization', 'private', 'token', 'draft_excerpt',
                'decision_memory', 'decision_memory_use', 'decision_state_capsule'}


def _public_projection(value):
    """Published receipt views retain identity/outcome, never provider bodies."""
    if isinstance(value, dict):
        return {key: _public_projection(item) for key, item in value.items()
                if key.lower() not in _PUBLIC_OMIT and not key.startswith('.')}
    if isinstance(value, list):
        return [_public_projection(item) for item in value]
    return value


def _copy_public_site(source: Path, destination: Path, *, include_reader_inference=True):
    inspection = source / 'inspect'
    if inspection.exists():
        from .inspection import validate_inspection
        validate_inspection(source, allow_unlisted=True)
    assets = Path(__file__).parent / 'assets'
    root_data = {'research-data.json', 'research.json', 'wake-data.json', 'state.json',
                 'events.jsonl', 'head.txt', 'map-data.json', 'map3d-data.json',
                 'deployment.json', 'manifest.webmanifest', 'experiment.json', 'export-format.json', 'blog.xml', 'research-expansion.json'}
    for path in source.rglob('*'):
        relative = path.relative_to(source)
        if path.is_symlink():
            raise ValueError('Public sites may not contain symlink assets')
        # Only the unified blog mounts Ask Bob. Avoid duplicating the large
        # browser engines in twelve node views that cannot use them.
        if not include_reader_inference and path.name.startswith(('ask-bob-engine', 'ask-bob-gpu-')):
            continue
        if not path.is_file() or any(part.startswith('.') for part in relative.parts):
            continue
        allowed = (len(relative.parts) == 1 and (path.name in root_data or
                   (assets / path.name).is_file() or path.name in {
                       'state.html', 'events.html', 'rejected.html', '404.html',
                       'console-records.html', 'console-map.html', 'console-map3d.html',
                       'console-events.html', 'console-state.html', 'console-rejected.html',
                       'research.html', 'topics.html', 'blog.html', 'projects.html',
                       'journal.html', 'lab.html', 'metrics.html', 'evidence.html',
                       'history.html', 'about.html'}))
        allowed = allowed or (relative.parts[0] in {'icons', 'backgrounds', 'self-correction'} and (assets / relative).is_file())
        allowed = allowed or (relative.parts[0] in {'blog', 'notebooks', 'journal'} and path.suffix == '.html')
        allowed = allowed or (relative.parts[0] == 'map3d' and path.suffix == '.json')
        allowed = allowed or relative.as_posix() in {'group/bob-publication.json', 'group/bob.json', 'reader-data.json', 'research-overview.json'}
        allowed = allowed or (relative.parts[0] in {'reader-records', 'research-details'} and path.suffix == '.json')
        if len(relative.parts) == 2 and relative.parts[0] == 'inspect':
            from .inspection import PUBLIC_FILES
            allowed = allowed or relative.name in PUBLIC_FILES
        if not allowed:
            continue
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if relative.parts[0] == 'inspect':
            # Preserve the reviewed static bundle's exact hashed bytes.
            shutil.copyfile(path, target)
        elif path.suffix == '.json':
            value = _public_projection(json.loads(path.read_text()))
            if path.name == 'wake-data.json' and isinstance(value.get('events'), list):
                # The overview duplicates history already published in events.jsonl.
                # Keep a bounded display tail while the complete export stays intact.
                from .live import MAX_EVENTS
                total = value.get('event_history', {}).get('total', len(value['events']))
                value['events'] = value['events'][-MAX_EVENTS:]
                value['event_history'] = {'displayed': len(value['events']), 'total': total,
                                          'complete_url': 'events.jsonl'}
            if path.name == 'deployment.json':
                value['snapshot_only'] = True
            target.write_text(json.dumps(value, ensure_ascii=False))
        elif path.suffix == '.jsonl':
            target.write_text(''.join(json.dumps(_public_projection(json.loads(line)), ensure_ascii=False) + '\n'
                                      for line in path.read_text().split('\n') if line.strip()))
        elif path.suffix == '.html':
            page = path.read_text()
            def mark_snapshot(match):
                deployment = json.loads(match.group(1))
                deployment['snapshot_only'] = True
                return 'window.WAKE_DEPLOYMENT=' + json.dumps(deployment) + ";window.WAKE_STANDALONE=true;document.documentElement.dataset.wakeSnapshotOnly='true';"
            page = re.sub(r'window\.WAKE_DEPLOYMENT=(\{[^<]*?\});window\.WAKE_STANDALONE=(?:true|false);', mark_snapshot, page)
            prefix = '../' * (len(relative.parts) - 1)
            page = page.replace('href="/runtime.json"', f'href="{prefix}installation.json"').replace('Inspect local WAKE runtime', 'Inspect published WAKE snapshot')
            # A public snapshot has no execution control, even before scripts load.
            page = re.sub(r'<a\b[^>]*class="[^"]*actions-light[^"]*"[^>]*>.*?</a>', '', page, flags=re.S)
            target.write_text(page)
        else:
            shutil.copyfile(path, target)


def _build_public_artifact(root: Path, destination: Path, *, progress=None) -> dict:
    """Copy only generated public sites; records/private runtime files stay local."""
    root, destination = Path(root), Path(destination)
    if destination.exists():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.wake-public-', dir=destination.parent) as temporary:
        staging = Path(temporary) / 'site'
        staging.mkdir()
        nodes, snapshots, research = [], {}, {}
        from .report import export, _deployment_site
        from .export_cache import renderer_signature
        compatible_renderer = renderer_signature()
        for node in NODE_IDS:
            if not (root / 'nodes' / node / 'site/current').exists():
                continue
            if progress:
                progress(f'Building website pages for {node} ({NODE_IDS.index(node) + 1}/12).')
            source = (root / 'nodes' / node / 'site' / 'current').resolve(strict=True)
            # Public generation may use a current symlink, but contained assets must be real files.
            for path in source.rglob('*'):
                if path.is_symlink():
                    raise ValueError('Public sites may not contain symlink assets')
            snapshot = json.loads((source / 'wake-data.json').read_text())
            view = json.loads((source / 'research-data.json').read_text())
            if snapshot['head'] != view['head'] or snapshot['state']['version'] != view['version']:
                raise ValueError('Node export does not identify one matching snapshot')
            snapshots[node], research[node] = snapshot, view
            marker = source / 'export-format.json'
            try:
                compatible = json.loads(marker.read_text()) == {
                    'schema': 1, 'renderer': compatible_renderer}
            except (OSError, ValueError):
                # A missing or damaged hint invalidates reuse, not the captured
                # record packet. Rebuild it through the normal exporter.
                compatible = False
            if compatible:
                # Completed immutable pages already contain deployment identity
                # and the exact captured record. No second render is needed.
                if progress:
                    progress(f'Reusing completed website pages for {node}.')
                _copy_public_site(source, staging / 'nodes' / node, include_reader_inference=False)
            else:
                # Render the recorded packet with current owned assets, so an upload
                # cannot retain obsolete live-polling code from an earlier export.
                generated = Path(temporary) / 'generated' / node
                from .feeds import HOME
                export(None, generated, projection={**snapshot, 'research':view}, standalone=True,
                       feed_base=HOME + f'nodes/{node}/')
                for name in ('events.jsonl', 'events.html', 'state.html', 'map-data.json', 'map3d-data.json'):
                    if (source / name).is_file():
                        shutil.copyfile(source / name, generated / name)
                if (source / 'map3d').exists():
                    shutil.copytree(source / 'map3d', generated / 'map3d', dirs_exist_ok=True)
                deployment = json.loads((source / 'deployment.json').read_text())
                _deployment_site(generated, standalone=True, installation=deployment)
                for name in ('bob.json', 'bob-publication.json'):
                    packet = source / 'group' / name
                    if packet.is_file():
                        (generated / 'group').mkdir(exist_ok=True)
                        shutil.copyfile(packet,generated / 'group' / name)
                _copy_public_site(generated, staging / 'nodes' / node, include_reader_inference=False)
            nodes.append({'id': node, 'url': f'/nodes/{node}/',
                          'record': {'head': snapshot['head'], 'version': snapshot['state']['version']}})
        from .installation import installation_snapshot
        manifest = _public_projection(installation_snapshot(root, live=False))
        for node in manifest['nodes']:
            status = root / 'nodes' / node['id'] / 'recorded-runtime.json'
            if status.exists():
                node['recorded_runtime'] = json.loads(status.read_text())
        manifest['public_projection'] = 'provider-bodies-omitted'
        manifest['record_heads'] = {entry['id']: entry['record'] for entry in nodes}
        from .mirror import heads_digest, exported_identity
        manifest['export_digest'] = heads_digest(manifest['record_heads'])
        manifest['publication_digest'] = exported_identity(root)['publication_digest']
        for entry in manifest['nodes']:
            entry['export_status'] = 'captured' if entry['id'] in snapshots else 'missing'
        # The public mirror retains the complete unified site, not a metrics-only
        # landing page. Snapshot identity disables local runtime polling.
        from .installation_projection import build_unified_projection
        from .installation_site import export_unified_site
        projection = build_unified_projection(snapshots, research, manifest['installation_id'])
        if progress:
            progress('Building the combined website and complete exported history.')
        generated = Path(temporary) / 'generated' / 'unified'
        export_unified_site(projection, generated)
        _copy_public_site(generated, staging)
        from .installation_site import export_unified_history
        export_unified_history({node: root / 'nodes' / node / 'site/current' for node in snapshots}, snapshots, staging)
        encoded = json.dumps(manifest, sort_keys=True)
        (staging / 'installation.json').write_text(encoded)
        for node in snapshots:
            (staging / 'nodes' / node / 'installation.json').write_text(encoded)
        package_public_history(staging)
        from .inspection import validate_inspection
        validate_inspection(staging)
        (staging / '.nojekyll').touch()
        staging.rename(destination)
    return manifest


def package_public_history(site, *, threshold=50 * 1024 * 1024):
    """Losslessly package large public streams; operational exports stay intact."""
    import gzip
    for history in Path(site).rglob('events.jsonl'):
        if history.stat().st_size <= threshold:
            continue
        archive = history.with_suffix('.jsonl.gz')
        with history.open('rb') as source, archive.open('wb') as destination:
            with gzip.GzipFile(filename='', fileobj=destination, mode='wb', mtime=0) as compressed:
                shutil.copyfileobj(source, compressed)
        # Rewrite only the generated pages belonging to this stream. Node views
        # name their own stream and must not inherit the root's packaging choice.
        for page in history.parent.glob('*.html'):
            page.write_text(page.read_text().replace('events.jsonl', 'events.jsonl.gz'))
        overview_path = history.parent / 'wake-data.json'
        overview = json.loads(overview_path.read_text())
        overview.setdefault('event_history', {})['complete_url'] = 'events.jsonl.gz'
        overview_path.write_text(json.dumps(overview, ensure_ascii=False, separators=(',', ':')))
        history.unlink()


def _pin_export_file(source, destination):
    """Immutable generation files survive retirement through their own link.

    Pins live beside the installation so compatible filesystems need no byte
    copy under the retention lease. Filesystems without hardlinks still copy.
    """
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)
    return destination


def build_public_artifact(root: Path, destination: Path, *, progress=None) -> dict:
    """Pin each immutable export while its owner retains/deletes generations.

    No authority database is read or copied, and research keeps its control mode.
    The resulting manifest describes exported heads, never a later live record.
    """
    root = Path(root)
    with tempfile.TemporaryDirectory(prefix='.wake-pinned-', dir=root) as temporary:
        pinned = Path(temporary)
        shutil.copyfile(root / 'installation-id.json', pinned / 'installation-id.json')
        for node in NODE_IDS:
            if progress:
                progress(f'Capturing {node} ({NODE_IDS.index(node) + 1}/12); using its last completed export.')
            site = root / 'nodes' / node / 'site'
            if not (site / 'current').exists():
                if progress:
                    progress(f'{node} has no completed export; marking it missing.')
                continue
            with (site / '.export.lock').open('a') as lease:
                fcntl.flock(lease, fcntl.LOCK_EX)
                source = (site / 'current').resolve(strict=True)
                if any(path.is_symlink() for path in source.rglob('*')):
                    raise ValueError('Public sites may not contain symlink assets')
                shutil.copytree(source, pinned / 'nodes' / node / 'site' / 'current', symlinks=True, copy_function=_pin_export_file)
            # Only bounded, dated observation fields enter the mirror. They do
            # not provide a live runtime capability or research authority.
            try:
                from .installation import read_json
                runtime = read_json(root / 'nodes' / node / 'runtime.json', 32768)
                state = runtime.get('state')
                if state in {'running', 'waiting', 'idle', 'paused', 'stopped', 'standby', 'blocked', 'unavailable'}:
                    observed = runtime.get('observed_at')
                    if isinstance(observed, str):
                        from datetime import datetime
                        if datetime.fromisoformat(observed).utcoffset() is None:
                            raise ValueError('Runtime observation needs a timezone')
                        (pinned / 'nodes' / node / 'recorded-runtime.json').write_text(
                            json.dumps({'state': state, 'observed_at': observed}))
            except (OSError, ValueError, TypeError):
                pass
        if not any((pinned / 'nodes' / node / 'site/current').exists() for node in NODE_IDS):
            raise ValueError('No completed node exports are available')
        return _build_public_artifact(pinned, destination, progress=progress)


def upload_public_artifact(target: Path, repository: str, branch: str, *, expected_head=None):
    """Upload a prepared public site using native Git credentials and normal pushes."""
    target = Path(target).resolve(strict=True)
    for path in target.rglob('*'):
        if path.is_file() and path.stat().st_size > 100 * 1024 * 1024:
            raise ValueError(f'Public file exceeds GitHub limit: {path.relative_to(target)}; no upload attempted')
    if not repository or not branch or branch in {'master', 'main', 'wake-runtime', 'wake-state', 'wake-live'}:
        raise ValueError('Configure WAKE_PUBLISH_REPOSITORY and a dedicated WAKE_PUBLISH_BRANCH')
    if not re.fullmatch(r'(?:https://github\.com/|git@github\.com:)[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?', repository):
        raise ValueError('Publication requires a GitHub repository URL without embedded credentials')
    subprocess.run(['git', 'check-ref-format', '--branch', branch], check=True, capture_output=True)
    with tempfile.TemporaryDirectory(prefix='wake-publish-') as temporary:
        checkout = Path(temporary) / 'checkout'
        checkout.mkdir()
        def git(*args):
            return subprocess.run(['git', *args], cwd=checkout, check=True, capture_output=True)
        git('init')
        git('remote', 'add', 'origin', repository)
        refs = git('ls-remote', '--heads', 'origin', f'refs/heads/{branch}').stdout
        if refs.strip():
            # Only the current parent is needed to append a normal commit.
            # Keep remote history intact without downloading years of exports
            # into each disposable publisher.
            git('fetch', '--depth=1', 'origin', f'refs/heads/{branch}')
            if expected_head is not None and git('rev-parse', 'FETCH_HEAD').stdout.decode().strip() != expected_head:
                raise ValueError('Public snapshot advanced; refresh from its new head before publishing')
            git('checkout', '-b', branch, 'FETCH_HEAD')
        else:
            if expected_head is not None:
                raise ValueError('Expected public snapshot is missing')
            git('checkout', '--orphan', branch)
        # The branch is a dedicated public projection; history is retained and
        # normal pushes reject concurrent publication instead of overwriting it.
        for path in checkout.iterdir():
            if path.name == '.git':
                continue
            if path.is_dir() and not path.is_symlink():
                shutil.rmtree(path)
            else:
                path.unlink()
        shutil.copytree(target, checkout, dirs_exist_ok=True)
        (checkout / '.nojekyll').touch()
        git('add', '--all')
        git('-c', 'user.name=WAKE operator', '-c', 'user.email=wake@localhost',
            'commit', '--allow-empty', '-m', 'Publish WAKE public snapshot')
        git('push', 'origin', f'HEAD:refs/heads/{branch}')


def publish_artifact(root: Path, output: Path | None = None) -> dict:
    if output is not None:
        return build_public_artifact(root, output)
    repository = os.environ.get('WAKE_PUBLISH_REPOSITORY', '')
    branch = os.environ.get('WAKE_PUBLISH_BRANCH', '')
    # Fail closed before reading active exports when publication is unconfigured.
    if not repository or not branch or branch in {'master', 'main', 'wake-runtime', 'wake-state', 'wake-live'}:
        raise ValueError('Configure WAKE_PUBLISH_REPOSITORY and a dedicated WAKE_PUBLISH_BRANCH')
    with (Path(root) / '.public-publish.lock').open('a') as lease:
        fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with tempfile.TemporaryDirectory(prefix='wake-public-') as temporary:
            target = Path(temporary) / 'site'
            manifest = build_public_artifact(root, target)
            upload_public_artifact(target, repository, branch)
    return manifest


def request(root: Path, payload: dict) -> dict:
    encoded = json.dumps(payload).encode() + b'\n'
    if len(encoded) > MAX_MESSAGE:
        raise ValueError('Control request too large')
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as connection:
        connection.settimeout(300)
        connection.connect(str(control_socket(root)))
        connection.sendall(encoded)
        response = bytearray()
        while b'\n' not in response:
            chunk = connection.recv(min(65536, MAX_MESSAGE + 1 - len(response)))
            if not chunk:
                raise ValueError('Controller disconnected without a complete acknowledgment')
            response.extend(chunk)
            if len(response) > MAX_MESSAGE:
                raise ValueError('Control response too large')
        result = json.loads(response.split(b'\n', 1)[0])
        if not isinstance(result, dict):
            raise ValueError('Invalid controller response')
        return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog='wake-research', description='Control this WAKE installation. New installations and imports start stopped. RESET destroys active data without making a backup; manual data/backups exports survive.')
    parser.add_argument('--data', type=Path, default=data_root(), help='Installation data root (WAKE_INSTALLATION_DATA, default /data)')
    actions = parser.add_subparsers(dest='action', required=True)
    for action in ('start', 'stop', 'pause', 'restart', 'RESET', 'status', 'mirror-enable', 'mirror-disable'):
        actions.add_parser(action)
    actions.add_parser('bob', help='Request eligible editorial work without starting research').add_argument('--revise', help='Request a model-written correction of the current shared article, with a recorded operator reason')
    ack = actions.add_parser('mirror-ack', help='Acknowledge the exact captured export digest; legacy Bob digests remain supported')
    ack.add_argument('digest')
    ack.add_argument('--export', action='store_true', dest='export_ack')
    ack.add_argument('--publication-digest')
    actions.add_parser('import', help='Verify and replace active data, leaving research stopped').add_argument('archive', help='Archive basename inside data/backups')
    actions.add_parser('export', help='Drain and export reloadable records into data/backups').add_argument('--name', default=None, help='New .zip archive basename')
    actions.add_parser('publish', help='Publish immutable exports without changing research controls; enable subsequent Bob mirror updates').add_argument('--output', type=Path, help='Build a local public artifact instead of uploading')
    args = parser.parse_args(argv)
    payload = {'action': args.action}
    try:
        if args.action == 'bob' and args.revise:
            payload['revision_reason'] = args.revise
        elif args.action == 'mirror-ack':
            payload['digest'] = args.digest
            if args.export_ack:
                payload.update(export_digest=args.digest, publication_digest=args.publication_digest)
        elif args.action in ('import', 'export'):
            name = args.archive if args.action == 'import' else args.name or datetime.now(timezone.utc).strftime('wake-%Y%m%dT%H%M%S%fZ.zip')
            if name != Path(name).name or not name.endswith('.zip') or '\\' in name:
                raise ValueError('Use a .zip basename inside data/backups')
            payload['archive' if args.action == 'import' else 'name'] = name
        elif args.action == 'publish' and args.output:
            payload['output'] = str(args.output.resolve())
        result = request(args.data, payload)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result.get('ok', False) else 1
    except (OSError, ValueError) as error:
        print(f'wake-research: {error}', file=__import__('sys').stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
