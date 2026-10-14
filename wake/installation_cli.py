"""Local operator commands and verified installation transport artifacts.

The controller owns draining and mutations. This client never opens a second
writer or deletes live data. Manual archives are separate from public exports.
"""
from __future__ import annotations

import argparse
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
                'authorization', 'passenger', 'private', 'token'}


def _public_projection(value):
    """Published receipt views retain identity/outcome, never provider bodies."""
    if isinstance(value, dict):
        return {key: _public_projection(item) for key, item in value.items()
                if key.lower() not in _PUBLIC_OMIT and not key.lower().startswith('.passenger')}
    if isinstance(value, list):
        return [_public_projection(item) for item in value]
    return value


def _copy_public_site(source: Path, destination: Path):
    assets = Path(__file__).parent / 'assets'
    root_data = {'research-data.json', 'research.json', 'wake-data.json', 'state.json',
                 'events.jsonl', 'head.txt', 'map-data.json', 'map3d-data.json',
                 'deployment.json', 'manifest.webmanifest', 'experiment.json'}
    for path in source.rglob('*'):
        relative = path.relative_to(source)
        if path.is_symlink():
            raise ValueError('Public sites may not contain symlink assets')
        if not path.is_file() or any(part.startswith('.') for part in relative.parts):
            continue
        allowed = (len(relative.parts) == 1 and (path.name in root_data or
                   (assets / path.name).is_file() or path.name in {
                       'state.html', 'events.html', 'rejected.html', '404.html',
                       'console-records.html', 'console-map.html', 'console-map3d.html',
                       'console-events.html', 'console-state.html', 'console-rejected.html'}))
        allowed = allowed or (relative.parts[0] in {'icons', 'backgrounds'} and (assets / relative).is_file())
        allowed = allowed or (relative.parts[0] in {'blog', 'notebooks', 'journal'} and path.suffix == '.html')
        allowed = allowed or (relative.parts[0] == 'map3d' and path.suffix == '.json')
        allowed = allowed or relative.as_posix() in {'group/bob-publication.json', 'group/bob.json'}
        if not allowed:
            continue
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == '.json':
            value = _public_projection(json.loads(path.read_text()))
            if path.name == 'deployment.json':
                value['snapshot_only'] = True
            target.write_text(json.dumps(value, ensure_ascii=False))
        elif path.suffix == '.jsonl':
            target.write_text(''.join(json.dumps(_public_projection(json.loads(line)), ensure_ascii=False) + '\n'
                                      for line in path.read_text().splitlines() if line.strip()))
        elif path.suffix == '.html':
            page = path.read_text()
            def mark_snapshot(match):
                deployment = json.loads(match.group(1))
                deployment['snapshot_only'] = True
                return 'window.WAKE_DEPLOYMENT=' + json.dumps(deployment) + ";window.WAKE_STANDALONE=true;document.documentElement.dataset.wakeSnapshotOnly='true';"
            page = re.sub(r'window\.WAKE_DEPLOYMENT=(\{[^<]*?\});window\.WAKE_STANDALONE=(?:true|false);', mark_snapshot, page)
            prefix = '../' * (len(relative.parts) - 1)
            page = page.replace('href="/runtime.json"', f'href="{prefix}installation.json"').replace('Inspect local WAKE runtime', 'Inspect published WAKE snapshot')
            target.write_text(page)
        else:
            shutil.copyfile(path, target)


def build_public_artifact(root: Path, destination: Path) -> dict:
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
        for node in NODE_IDS:
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
            # Render the recorded packet with current owned assets, so an upload
            # cannot retain obsolete live-polling code from an earlier export.
            generated = Path(temporary) / 'generated' / node
            export(None, generated, projection={**snapshot, 'research':view}, standalone=True)
            deployment = json.loads((source / 'deployment.json').read_text())
            _deployment_site(generated, standalone=True, installation=deployment)
            for name in ('bob.json', 'bob-publication.json'):
                packet = source / 'group' / name
                if packet.is_file():
                    (generated / 'group').mkdir(exist_ok=True)
                    shutil.copyfile(packet,generated / 'group' / name)
            _copy_public_site(generated, staging / 'nodes' / node)
            nodes.append({'id': node, 'url': f'/nodes/{node}/',
                          'record': _record_metadata(root / 'nodes' / node / 'record' / 'wake.sqlite')})
        from .installation import installation_snapshot
        manifest = _public_projection(installation_snapshot(root, live=False))
        manifest['public_projection'] = 'provider-bodies-omitted'
        manifest['record_heads'] = {entry['id']: entry['record'] for entry in nodes}
        # The public mirror retains the complete unified site, not a metrics-only
        # landing page. Snapshot identity disables local runtime polling.
        from .installation_projection import build_unified_projection
        from .installation_site import export_unified_site
        projection = build_unified_projection(snapshots, research, manifest['installation_id'])
        generated = Path(temporary) / 'generated' / 'unified'
        export_unified_site(projection, generated)
        _copy_public_site(generated, staging)
        encoded = json.dumps(manifest, sort_keys=True)
        (staging / 'installation.json').write_text(encoded)
        for node in NODE_IDS:
            (staging / 'nodes' / node / 'installation.json').write_text(encoded)
        (staging / '.nojekyll').touch()
        staging.rename(destination)
    return manifest


def upload_public_artifact(target: Path, repository: str, branch: str):
    """Upload a prepared public site using native Git credentials and normal pushes."""
    target = Path(target).resolve(strict=True)
    if not repository or not branch or branch in {'master', 'main', 'wake-runtime', 'wake-state'}:
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
            git('fetch', 'origin', f'refs/heads/{branch}')
            git('checkout', '-b', branch, 'FETCH_HEAD')
        else:
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
    if not repository or not branch or branch in {'master', 'main', 'wake-runtime', 'wake-state'}:
        raise ValueError('Configure WAKE_PUBLISH_REPOSITORY and a dedicated WAKE_PUBLISH_BRANCH')
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
    for action in ('start', 'stop', 'pause', 'restart', 'RESET', 'status'):
        actions.add_parser(action)
    actions.add_parser('import', help='Verify and replace active data, leaving research stopped').add_argument('archive', help='Archive basename inside data/backups')
    actions.add_parser('export', help='Drain and export reloadable records into data/backups').add_argument('--name', default=None, help='New .zip archive basename')
    actions.add_parser('publish', help='Publish generated public data using configured dedicated GitHub branch').add_argument('--output', type=Path, help='Build a local public artifact instead of uploading')
    args = parser.parse_args(argv)
    payload = {'action': args.action}
    try:
        if args.action in ('import', 'export'):
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
