"""Encrypted transport of native records between disposable GitHub runners.

SQLite remains the sole authority. Release assets are authenticated encrypted
blocks of SQLite backups; a compare-and-swap Git ref selects a complete recovery
snapshot. No provider, browser, or projection can write that ref. Only current
and previous recovery snapshots are retained; each contains the full history.
"""
from __future__ import annotations

from contextlib import contextmanager, closing, nullcontext
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import base64
import fcntl
import gzip
import hashlib
import hmac
import io
import json
import multiprocessing
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
import zipfile

from .installation_cli import NODE_IDS, _record_metadata
from .kernel.record import Record
from .kernel.storage import canonical_json
from .report import atomic_write

STATE_BRANCH = 'wake-hosted-state'
RELEASE_TAG = 'wake-hosted-checkpoints'
FORMAT = 'wake-hosted-state@1'
BLOCK_SIZE = 4 * 1024 * 1024
MAX_BLOCK_SIZE = 256 * 1024 * 1024
MAX_DATABASE = 8 * 1024**3
# The two retired private files are opaque archival payloads only. Transport
# preserves their bytes; no runtime feature reads or updates their contents.
AUXILIARY = ('installation-id.json', 'provider-schedule.json', 'experimental-reset.json',
             'private/.passenger.md', 'private/.passenger-state.json')


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def atomic_bytes(path, body):
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(body)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def seal(key, data, purpose):
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    nonce = os.urandom(12)
    return nonce + AESGCM(key).encrypt(nonce, data, purpose.encode())


def unseal(key, data, purpose):
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if len(data) < 28:
        raise ValueError('Truncated encrypted checkpoint')
    return AESGCM(key).decrypt(data[:12], data[12:], purpose.encode())


class GitHub:
    def __init__(self, repository, token, *, reserve=0, rate_wait_limit=3660, rate_file=None):
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
            raise ValueError('Expected owner/repository')
        if not token:
            raise ValueError('GitHub credential missing')
        self.repository, self.token = repository, token
        self.reserve, self.rate_wait_limit = reserve, rate_wait_limit
        self.rate = {}
        self.rate_file = Path(rate_file) if rate_file else None
        if self.rate_file:
            self.rate_file.parent.mkdir(parents=True, exist_ok=True)

    def _update_rate(self, incoming=None, *, debit=False):
        """Share conservative numeric budget estimates, never credentials."""
        def merge(left, right):
            if not right:
                return dict(left)
            if right.get('Reset', 0) > left.get('Reset', 0):
                return dict(right)
            if right.get('Reset', left.get('Reset')) != left.get('Reset'):
                return dict(left)
            value = {**left, **right}
            if 'Remaining' in left and 'Remaining' in right:
                value['Remaining'] = min(left['Remaining'], right['Remaining'])
            return value
        def update():
            state = dict(self.rate)
            if self.rate_file and self.rate_file.exists():
                saved = json.loads(self.rate_file.read_text())
                if (not isinstance(saved, dict) or set(saved) - {'Limit', 'Remaining', 'Reset'}
                        or any(type(v) is not int or v < 0 for v in saved.values())):
                    raise ValueError('Invalid shared GitHub rate budget')
                state = merge(state, saved)
            if state.get('Reset', float('inf')) <= time.time():
                state = {}
            state = merge(state, incoming or {})
            if debit and 'Remaining' in state:
                state['Remaining'] = max(0, state['Remaining'] - 1)
            self.rate = state
            if self.rate_file:
                atomic_write(self.rate_file, json.dumps(state))
        if self.rate_file:
            with self.rate_file.with_suffix('.lock').open('a') as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                update()
        else:
            update()

    def observe_rate(self, headers):
        # Uploads may omit these headers. Missing headers must not erase the
        # budget shared by checkpoint workers, publication and control reads.
        headers = headers or {}
        self._update_rate({name: int(headers.get('X-RateLimit-' + name))
                           for name in ('Limit', 'Remaining', 'Reset')
                           if str(headers.get('X-RateLimit-' + name, '')).isdigit()})

    def wait_rate(self, delay, waited):
        delay = max(1, delay)
        if delay + waited > self.rate_wait_limit:
            return False
        print(json.dumps({'hosted_api': 'rate-wait', 'seconds': round(delay),
                          'reserve': self.reserve, **self.rate}), flush=True)
        time.sleep(delay)
        return True

    def request(self, path, *, method='GET', body=None, binary=False, upload=False):
        host = 'https://uploads.github.com' if upload else 'https://api.github.com'
        url = host + '/repos/' + self.repository + '/' + path
        headers = {'Authorization': 'Bearer ' + self.token,
                   'Accept': 'application/octet-stream' if binary else 'application/vnd.github+json',
                   'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'WAKE-hosted-transport'}
        if body is not None:
            headers['Content-Type'] = 'application/octet-stream' if upload else 'application/json'
            if not upload:
                body = encode(body)
        # Only safe reads retry automatically. Mutations reconcile their actual
        # result at the caller before retrying the same identity.
        waited = 0
        self._update_rate()
        budget = dict(self.rate)
        if budget.get('Remaining', self.reserve + 1) <= self.reserve and 'Reset' in budget:
            delay = max(1, budget['Reset'] - time.time() + 1)
            if self.wait_rate(delay, waited):
                waited += delay
            elif self.reserve:
                raise RuntimeError('GitHub data budget wait exceeded its bound')
        for attempt in range(3):
            try:
                self._update_rate(debit=True)
                with urlopen(Request(url, data=body, headers=headers, method=method), timeout=120) as response:
                    self.observe_rate(response.headers)
                    data = response.read()
                return data if binary else json.loads(data) if data else None
            except (HTTPError, URLError, TimeoutError) as error:
                if isinstance(error, HTTPError):
                    self.observe_rate(error.headers)
                    # A forbidden request is not automatically a quota error.
                    # GitHub can omit Retry-After for secondary limits. Classify
                    # its bounded JSON message without ever logging that body.
                    secondary = False
                    if error.code == 403 and self.rate.get('Remaining') != 0:
                        raw = error.read(8192)
                        error.fp = io.BytesIO(raw)
                        try:
                            message = str(json.loads(raw).get('message', '')).lower()
                            secondary = 'secondary rate limit' in message or 'abuse detection' in message
                        except (ValueError, AttributeError):
                            pass
                    print(json.dumps({'hosted_api': 'request-failed', 'status': error.code,
                                      'method': method, 'secondary_limit': secondary, **self.rate}), flush=True)
                    retry_after = str((error.headers or {}).get('Retry-After', ''))
                    delay = (max(1, self.rate['Reset'] - time.time() + 1)
                             if self.rate.get('Remaining') == 0 and 'Reset' in self.rate
                             else int(retry_after) if retry_after.isdigit() else 60 if error.code == 429 or secondary else None)
                    if method == 'GET' and error.code in (403, 429) and delay is not None:
                        if attempt < 2 and self.wait_rate(delay, waited):
                            waited += max(1, delay)
                            error.close()
                            continue
                        raise
                transient = not isinstance(error, HTTPError) or error.code in (429, 500, 502, 503, 504)
                if method != 'GET' or not transient or attempt == 2:
                    raise
                time.sleep(2 ** attempt)


def record_identity(path):
    """Identify a coherent backup; full replay remains mandatory on restore."""
    with closing(sqlite3.connect(Path(path).resolve().as_uri() + '?mode=ro', uri=True)) as db:
        row = db.execute('SELECT revision_after,event_hash FROM events ORDER BY sequence DESC LIMIT 1').fetchone()
    if row is None:
        raise ValueError('Missing initialized record history')
    return {'revision': row[0], 'head': row[1], 'sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest()}


def _verified_snapshot(source, target):
    Record.open_read_only(source).snapshot_to(target)
    return _record_metadata(target)


def verify_recovery(path):
    """Verify all journals and bind the fast app projection to its last receipt.

    Migration audits replay every application action. Subsequent authenticated
    snapshots can use the native materialized state only when its canonical
    digest equals the result digest in the independently replayed event chain.
    This is not trust in the projection's self-reported checksum or a website.
    """
    from .application import WAKE_APPLICATION
    from .kernel.applications import application_state
    record = Record.open_read_only(path)
    revision, history = record.full_replay()
    projected_revision, projected = record.replay()
    envelope = history.get('app:wake') or {}
    events = envelope.get('events', [])
    if revision != projected_revision or not events:
        raise ValueError('Missing native WAKE application recovery history')
    state = application_state(WAKE_APPLICATION, projected.get('app:wake'))
    digest = hashlib.sha256(canonical_json(state).encode()).hexdigest()
    if digest != events[-1].get('result_digest') or not (state or {}).get('state', {}).get('objective'):
        raise ValueError('Recovery projection differs from the hash-linked application result')
    record.invocation_history()
    record.application_access_history()
    return record_identity(path)


class HostedState:
    def __init__(self, directory, repository, token, key):
        self.directory = Path(directory).resolve()
        # Data transfers share the workflow token with controls and handoff.
        # Pause before exhausting that shared allowance; never skip a barrier.
        self.api = GitHub(repository, token, reserve=100, rate_file=self.directory / 'github-rate.json')
        self.key = bytes.fromhex(key) if isinstance(key, str) else key
        if len(self.key) != 32:
            raise ValueError('Hosted checkpoint key must contain 32 random bytes')
        self.checkout = self.directory / 'ref'
        self.directory.mkdir(parents=True, exist_ok=True)

    @classmethod
    def from_environment(cls):
        return cls(os.environ['WAKE_HOSTED_STATE_DIR'], os.environ['GITHUB_REPOSITORY'],
                   os.environ['GH_TOKEN'], os.environ['WAKE_HOSTED_STATE_KEY'])

    @contextmanager
    def lease(self):
        # All node callbacks and final capture share this transport lease. Node
        # SQLite writers retain their existing record leases and governance.
        with (self.directory / 'transport.lock').open('a') as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            yield

    def git(self, *args):
        authorization = base64.b64encode(('x-access-token:' + self.api.token).encode()).decode()
        env = dict(os.environ, GIT_CONFIG_COUNT='1',
                   GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
                   GIT_CONFIG_VALUE_0='AUTHORIZATION: basic ' + authorization)
        result = subprocess.run(['git', *args], cwd=self.checkout, env=env,
                                capture_output=True, timeout=240)
        if result.returncode:
            # Do not echo Git's credential-bearing environment or provider data.
            raise RuntimeError('Hosted checkpoint Git operation failed: ' + args[0])
        return result.stdout.decode().strip()

    def open(self, *, initialize=False):
        self.checkout.mkdir(parents=True, exist_ok=True)
        self.git('init', '-q')
        self.git('config', 'user.name', 'WAKE hosted runner')
        self.git('config', 'user.email', 'wake@localhost')
        self.git('remote', 'add', 'origin', 'https://github.com/' + self.api.repository + '.git')
        refs = self.git('ls-remote', 'origin', 'refs/heads/' + STATE_BRANCH)
        if initialize:
            if refs:
                raise ValueError('Hosted state already exists; refusing to overwrite it')
            return
        if not refs:
            raise ValueError('Hosted authority missing; refusing fresh initialization')
        self.git('fetch', '--depth=1', 'origin', 'refs/heads/' + STATE_BRANCH)
        self.git('checkout', '--detach', 'FETCH_HEAD')
        self.read_manifest()  # Authentication is checked before any restoration.

    def read_manifest(self, name='current.enc'):
        value = json.loads(unseal(self.key, (self.checkout / name).read_bytes(), FORMAT))
        if value.get('format') != FORMAT or set(value.get('nodes', {})) != set(NODE_IDS):
            raise ValueError('Incomplete hosted installation checkpoint')
        if not isinstance(value.get('generation'), int) or value['generation'] < 1:
            raise ValueError('Invalid checkpoint generation')
        return value

    def release(self):
        cache = self.directory / 'release.json'
        if cache.exists():
            return json.loads(cache.read_text())
        try:
            release = self.api.request('releases/tags/' + RELEASE_TAG)
        except HTTPError as error:
            if error.code != 404:
                raise
            release = self.api.request('releases', method='POST', body={
                'tag_name': RELEASE_TAG, 'name': 'WAKE encrypted working checkpoints',
                'target_commitish': os.environ.get('WAKE_SOURCE_REVISION', 'master'),
                'prerelease': True,
                'body': 'Encrypted recovery blocks for the autonomous WAKE installation. '
                        'Only the current and previous complete checkpoints are retained. '
                        'Each verified native record retains its complete event history. '
                        'The decryption key is a repository secret; these are not public exports.'})
        atomic_write(cache, json.dumps({'id': release['id']}))
        return release

    def assets(self, *, refresh=False):
        cache = self.directory / 'assets.json'
        if cache.exists() and not refresh:
            return json.loads(cache.read_text())
        release = self.release()
        all_items = []
        page = 1
        while True:
            batch = self.api.request(f'releases/{release["id"]}/assets?per_page=100&page={page}')
            all_items.extend(batch)
            if len(batch) < 100:
                break
            page += 1
        items = {item['name']: item['id'] for item in all_items if item.get('state') == 'uploaded'}
        # A failed GitHub upload can leave an empty starter asset under the
        # requested name. It cannot satisfy a durability barrier or block the
        # next identical retry forever. Only this dedicated block namespace is
        # eligible for removal, under the transport lease.
        for item in all_items:
            if item.get('state') == 'starter' and re.fullmatch(r'block-[0-9a-f]{64}\.bin', item['name']):
                self.api.request(f'releases/assets/{item["id"]}', method='DELETE')
        atomic_write(cache, json.dumps(items))
        return items

    def put_block(self, raw, assets):
        name = 'block-' + hmac.new(self.key, b'block\0' + raw, hashlib.sha256).hexdigest() + '.bin'
        if name not in assets:
            body = seal(self.key, gzip.compress(raw, compresslevel=6, mtime=0), name)
            release = self.release()
            for attempt in range(2):
                try:
                    item = self.api.request(f'releases/{release["id"]}/assets?name={quote(name)}',
                                            method='POST', body=body, upload=True)
                    break
                except (HTTPError, URLError, TimeoutError) as error:
                    quota = (isinstance(error, HTTPError) and error.code == 403
                             and (str((error.headers or {}).get('X-RateLimit-Remaining')) == '0'
                                  or getattr(self.api, 'rate', {}).get('Remaining') == 0))
                    transient = not isinstance(error, HTTPError) or error.code in (429, 500, 502, 503, 504)
                    # Reconcile the same content identity before any retry. A
                    # safe listing waits for quota reset; permission errors do not.
                    found = self.assets(refresh=True)
                    if name in found:
                        item = {'id': found[name]}
                        break
                    if attempt or not (quota or transient):
                        raise
            if item.get('state', 'uploaded') != 'uploaded' or item.get('size', len(body)) != len(body):
                raise ValueError('GitHub did not acknowledge a complete encrypted block')
            assets[name] = item['id']
            atomic_write(self.directory / 'assets.json', json.dumps(assets))
        return {'name': name, 'id': assets[name], 'size': len(raw)}

    def put_file(self, path, assets):
        size = Path(path).stat().st_size
        if size > MAX_DATABASE:
            raise ValueError('Hosted checkpoint file exceeds the recovery limit')
        # Grow blocks automatically with records. Keeping at most 32 blocks
        # per node leaves room for both recovery snapshots and in-flight changes
        # below GitHub's 1000-assets-per-release limit, even after years of growth.
        block_size = BLOCK_SIZE
        while block_size * 32 < size:
            block_size *= 2
        if block_size > MAX_BLOCK_SIZE:
            raise ValueError('Hosted checkpoint block exceeds recovery limit')
        blocks = []
        with Path(path).open('rb') as stream:
            while raw := stream.read(block_size):
                blocks.append(self.put_block(raw, assets))
        return blocks

    def get_file(self, blocks, destination):
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        size = 0
        with destination.open('xb') as stream:
            for item in blocks:
                if not re.fullmatch(r'block-[0-9a-f]{64}\.bin', item['name']):
                    raise ValueError('Invalid encrypted block identity')
                data = self.api.request(f'releases/assets/{int(item["id"])}', binary=True)
                compressed = unseal(self.key, data, item['name'])
                with gzip.GzipFile(fileobj=io.BytesIO(compressed)) as source:
                    raw = source.read(MAX_BLOCK_SIZE + 1)
                expected = 'block-' + hmac.new(self.key, b'block\0' + raw, hashlib.sha256).hexdigest() + '.bin'
                if len(raw) != item['size'] or len(raw) > MAX_BLOCK_SIZE or expected != item['name']:
                    raise ValueError('Encrypted block content mismatch')
                size += len(raw)
                if size > MAX_DATABASE:
                    raise ValueError('Hosted checkpoint exceeds installation limit')
                stream.write(raw)

    def put_auxiliary(self, root, assets):
        root = Path(root)
        with tempfile.TemporaryDirectory(dir=self.directory) as temporary:
            target = Path(temporary) / 'aux.zip'
            with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
                paths = [root / relative for relative in AUXILIARY]
                paths += list((root / 'config').rglob('*.toml'))
                for node in NODE_IDS:
                    paths.append(root / 'nodes' / node / 'record/.standalone-initialized')
                for path in sorted(paths):
                    if path.is_file() and not path.is_symlink():
                        archive.write(path, str(path.relative_to(root)))
            return self.put_file(target, assets)

    def save(self, manifest, *, retain_previous=True):
        previous = self.checkout / 'current.enc'
        base = self.git('rev-parse', 'HEAD') if previous.exists() else ''
        if previous.exists() and retain_previous:
            shutil.copyfile(previous, self.checkout / 'previous.enc')
        elif not retain_previous:
            (self.checkout / 'previous.enc').unlink(missing_ok=True)
        manifest['generation'] += 1
        manifest['captured_at'] = datetime.now(timezone.utc).isoformat()
        atomic_bytes(previous, seal(self.key, encode(manifest), FORMAT))
        self.git('add', '--all')
        tree = self.git('write-tree')
        commit = self.git('commit-tree', tree, '-m', 'Checkpoint native WAKE installation')
        ref = 'refs/heads/' + STATE_BRANCH
        # A rotating ref avoids unbounded Git history of encrypted snapshots.
        # The previous complete checkpoint is a separate file in the same tree;
        # historical branches are never touched. Lease failure stops effects.
        try:
            self.git('push', 'origin', '--force-with-lease=' + ref + ':' + base, commit + ':' + ref)
        except RuntimeError:
            remote = self.git('ls-remote', 'origin', ref).split()
            if not remote or remote[0] != commit:
                raise
        self.git('reset', '--hard', commit)
        return commit

    def reset(self, root, reason):
        """Replace stopped cycle-zero experiment state, with no retained old copy."""
        from .record_store import RecordStore
        root = Path(root)
        with self.lease(), tempfile.TemporaryDirectory(dir=self.directory) as temporary:
            manifest = self.read_manifest()
            assets = self.assets()
            nodes = {}
            for node in NODE_IDS:
                source = root/'nodes'/node/'record'
                store = RecordStore(source)
                try:
                    if store.load()['version'] != 0:
                        raise ValueError('Reset requires every node stopped at cycle zero')
                finally:
                    store.close()
                target = Path(temporary)/(node+'.sqlite')
                identity = _verified_snapshot(source/'wake.sqlite', target)
                nodes[node] = {**identity, 'blocks': self.put_file(target, assets)}
            reset = {'id': os.urandom(16).hex(), 'at': datetime.now(timezone.utc).isoformat(),
                     'reason': reason, 'previous_generation': manifest['generation']}
            atomic_write(root/'experimental-reset.json', json.dumps(reset))
            manifest.update(nodes=nodes, experimental_reset=reset,
                            origin='Explicit experimental reset; earlier results discarded')
            manifest['auxiliary'] = self.put_auxiliary(root, assets)
            self.save(manifest, retain_previous=False)
            self.prune()
            return reset

    def checkpoint_node(self, record_directory):
        record_directory = Path(record_directory).resolve()
        node = record_directory.parent.name
        root = record_directory.parents[2]
        if node not in NODE_IDS or record_directory != root / 'nodes' / node / 'record':
            raise ValueError('Checkpoint requires an owned installation node')
        with self.lease(), tempfile.TemporaryDirectory(dir=self.directory) as temporary:
            manifest = self.read_manifest()
            assets = self.assets()
            backup = Path(temporary) / 'wake.sqlite'
            # This process already runs verified authority and native appends.
            # Transport needs a coherent physical image, not another full replay
            # of the growing prefix before every provider attempt. Restoring
            # always performs the complete semantic/journal audit below.
            Record.open_read_only(record_directory / 'wake.sqlite').snapshot_to(backup)
            manifest['nodes'][node] = {**verify_recovery(backup), 'blocks': self.put_file(backup, assets)}
            manifest['auxiliary'] = self.put_auxiliary(root, assets)
            self.save(manifest)
            # Bound release storage during long runs, not just on clean exit.
            if manifest['generation'] % 10 == 0:
                self.prune()

    def prune(self):
        # A local process lease cannot protect against an obsolete runner.
        # Never delete recovery blocks using a stale rotating-ref checkout.
        remote = self.git('ls-remote', 'origin', 'refs/heads/' + STATE_BRANCH).split()
        if not remote or remote[0] != self.git('rev-parse', 'HEAD'):
            raise RuntimeError('Refusing checkpoint pruning from a stale hosted ref')
        referenced = set()
        identities = {}
        for filename in ('current.enc', 'previous.enc'):
            if not (self.checkout / filename).exists():
                continue
            value = self.read_manifest(filename)
            referenced.update(item['name'] for item in value['auxiliary'])
            identities.update((item['name'], item['id']) for item in value['auxiliary'])
            for node in value['nodes'].values():
                referenced.update(item['name'] for item in node['blocks'])
                identities.update((item['name'], item['id']) for item in node['blocks'])
        assets = self.assets(refresh=True)
        if any(assets.get(name) != identity for name, identity in identities.items()):
            raise ValueError('Incomplete hosted recovery assets; refusing checkpoint pruning')
        for name, identity in list(assets.items()):
            if re.fullmatch(r'block-[0-9a-f]{64}\.bin', name) and name not in referenced:
                try:
                    self.api.request(f'releases/assets/{identity}', method='DELETE')
                except HTTPError as error:
                    if error.code != 404:
                        raise
                assets.pop(name)
        atomic_write(self.directory / 'assets.json', json.dumps(assets))

    def seed(self, root, *, workers=1, origin='operator-authorized transfer of stopped laptop installation'):
        root = Path(root)
        if not 1 <= workers <= 4:
            raise ValueError('Migration verification uses one to four processes')
        with self.lease(), tempfile.TemporaryDirectory(dir=self.directory) as temporary:
            self.open(initialize=True)
            manifest = {'format': FORMAT, 'generation': 0, 'nodes': {},
                        'installation_id': json.loads((root / 'installation-id.json').read_text())['id'],
                        'origin': origin,
                        'migrated_at': datetime.now(timezone.utc).isoformat()}
            assets = self.assets()
            context = (ProcessPoolExecutor(max_workers=workers, mp_context=multiprocessing.get_context('spawn'))
                       if workers > 1 else nullcontext(None))
            with context as executor:
                pending = {node: executor.submit(_verified_snapshot,
                    root / 'nodes' / node / 'record/wake.sqlite', Path(temporary) / (node + '.sqlite'))
                    for node in NODE_IDS} if executor else {}
                for node in NODE_IDS:
                    print('Verifying and encrypting ' + node, flush=True)
                    target = Path(temporary) / (node + '.sqlite')
                    identity = (pending[node].result() if executor else
                                _verified_snapshot(root / 'nodes' / node / 'record/wake.sqlite', target))
                    manifest['nodes'][node] = {**identity, 'blocks': self.put_file(target, assets)}
                    target.unlink()
            manifest['auxiliary'] = self.put_auxiliary(root, assets)
            return self.save(manifest)

    def restore(self, root, *, workers=1, fresh_experiment=False):
        """Restore records, or only trusted setup for an explicit disposable reset."""
        root = Path(root)
        if not 1 <= workers <= 4:
            raise ValueError('Recovery verification uses one to four processes')
        if root.exists() and any(root.iterdir()):
            raise ValueError('Restore destination must be empty')
        root.mkdir(parents=True, exist_ok=True)
        with self.lease(), tempfile.TemporaryDirectory(dir=self.directory) as temporary:
            manifest = self.read_manifest()
            context = (ProcessPoolExecutor(max_workers=workers, mp_context=multiprocessing.get_context('spawn'))
                       if workers > 1 else nullcontext(None))
            with context as executor:
                pending = {}
                for node in (() if fresh_experiment else NODE_IDS):
                    target = root / 'nodes' / node / 'record/wake.sqlite'
                    value = manifest['nodes'][node]
                    self.get_file(value['blocks'], target)
                    if executor:
                        pending[node] = executor.submit(verify_recovery, target)
                    else:
                        pending[node] = verify_recovery(target)
                for node, value in (() if fresh_experiment else manifest['nodes'].items()):
                    actual = pending[node].result() if executor else pending[node]
                    expected = {k: value[k] for k in ('revision', 'head', 'sha256')}
                    if actual != expected:
                        raise ValueError('Restored node history differs from checkpoint: ' + node)
            archive_path = Path(temporary) / 'aux.zip'
            self.get_file(manifest['auxiliary'], archive_path)
            with zipfile.ZipFile(archive_path) as archive:
                names = archive.namelist()
                if len(names) != len(set(names)):
                    raise ValueError('Duplicate auxiliary checkpoint paths')
                for entry in archive.infolist():
                    name = entry.filename
                    marker = any(name == f'nodes/{node}/record/.standalone-initialized' for node in NODE_IDS)
                    config = name.startswith('config/') and name.endswith('.toml')
                    if (name not in AUXILIARY and not marker and not config) or '..' in Path(name).parts or Path(name).is_absolute():
                        raise ValueError('Unexpected auxiliary checkpoint path')
                    if entry.file_size > 16 * 1024 * 1024:
                        raise ValueError('Auxiliary checkpoint file exceeds limit')
                    if fresh_experiment and marker:
                        continue  # A fresh record must bootstrap as unused.
                    target = root / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with target.open('xb') as output:
                        output.write(archive.read(entry))
            identity = json.loads((root / 'installation-id.json').read_text())['id']
            if identity != manifest['installation_id']:
                raise ValueError('Installation identity mismatch')
            for node in NODE_IDS:
                atomic_write(root / 'nodes' / node / 'record/.wake-runner-control.json',
                             json.dumps({'research': 'stopped'}))
            return manifest
