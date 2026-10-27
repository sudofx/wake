"""Hosted recovery preserves native meaning, privacy and pre-effect durability."""
from pathlib import Path
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from wake.engine import Engine, DEFAULTS
from wake.hosted import HostedState, verify_recovery
from wake.installation_cli import NODE_IDS
from wake.providers import Fixture
from wake.record_store import RecordStore


class Assets:
    def __init__(self):
        self.repository, self.token = 'example/repo', 'test-token'
        self.objects = {}
        self.next_id = 1

    def request(self, path, *, method='GET', body=None, binary=False, upload=False):
        if path.startswith('releases/tags/'):
            return {'id': 1}
        if upload:
            from urllib.parse import parse_qs, urlsplit
            name = parse_qs(urlsplit(path).query)['name'][0]
            identity = self.next_id
            self.next_id += 1
            self.objects[identity] = {'name': name, 'data': body, 'id': identity}
            return {'id': identity, 'state': 'uploaded', 'size': len(body)}
        if path.startswith('releases/1/assets?'):
            from urllib.parse import parse_qs, urlsplit
            page = int(parse_qs(urlsplit(path).query)['page'][0])
            return [{'id': item['id'], 'name': item['name'], 'state': item.get('state', 'uploaded')}
                    for item in list(self.objects.values())[(page-1)*100:page*100]]
        if path.startswith('releases/assets/'):
            identity = int(path.rsplit('/', 1)[1])
            if method == 'DELETE':
                del self.objects[identity]
                return
            return self.objects[identity]['data']
        raise AssertionError((path, method))


class LocalState(HostedState):
    remote = None

    def git(self, *args):
        if args[:3] == ('remote', 'add', 'origin'):
            args = (*args[:3], str(self.remote))
        return super().git(*args)


class HostedTransportTests(unittest.TestCase):
    def test_retired_private_archives_round_trip_opaquely(self):
        import zipfile
        private = self.active / 'private'
        saved = {'.passenger.md': b'RETIRED PRIVATE ARCHIVE\x00',
                 '.passenger-state.json': b'{opaque historical bytes}'}
        for name, data in saved.items():
            (private / name).write_bytes(data)
        assets = self.transport.assets()
        refs = self.transport.put_auxiliary(self.active, assets)
        archive_path = self.root / 'retained.zip'
        self.transport.get_file(refs, archive_path)
        with zipfile.ZipFile(archive_path) as archive:
            for name, data in saved.items():
                self.assertEqual(archive.read('private/' + name), data)
            self.assertNotIn('private/.private.md', archive.namelist())

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.active = self.root / 'source'
        for node in NODE_IDS:
            directory = self.active / 'nodes' / node / 'record'
            store = RecordStore(directory, initialize_empty=True)
            engine = Engine(directory, dict(DEFAULTS), store=store)
            engine.initialize()
            engine.run(Fixture('before-transfer'))
            store.close()
            (directory / '.standalone-initialized').write_text('Authority: wake.sqlite\n')
        (self.active / 'installation-id.json').write_text('{"id":"test-installation"}')
        (self.active / 'config').mkdir()
        (self.active / 'config/wake.toml').write_text('provider="fixture"\n')
        (self.active / 'private').mkdir()
        (self.active / 'private/.private.md').write_text('PRIVATE SIDECAR CONTENT')
        (self.active / 'private/.private-state.json').write_text('{"generation":0}')
        self.remote = self.root / 'remote.git'
        subprocess.run(['git', 'init', '--bare', '-q', str(self.remote)], check=True)
        LocalState.remote = self.remote
        self.assets = Assets()
        self.key = b'k' * 32
        self.transport = self.new_transport('seed')
        self.transport.seed(self.active)

    def new_transport(self, name):
        value = LocalState(self.root / name, 'example/repo', 'test-token', self.key)
        value.api = self.assets
        return value

    def tearDown(self):
        self.temp.cleanup()

    def test_explicit_reset_replaces_only_cycle_zero_state_without_retaining_old_checkpoint(self):
        import shutil
        fresh = self.root/'fresh'
        for node in NODE_IDS:
            folder = fresh/'nodes'/node/'record'
            store = RecordStore(folder, initialize_empty=True)
            Engine(folder, dict(DEFAULTS), store=store).initialize()
            store.close()
        (fresh/'installation-id.json').write_text('{"id":"test-installation"}')
        shutil.copytree(self.active/'config', fresh/'config')
        reset = self.transport.reset(fresh, 'Disposable experiment reset test')
        self.assertFalse((self.transport.checkout/'previous.enc').exists())
        self.assertEqual(self.transport.read_manifest()['experimental_reset'], reset)
        successor = self.new_transport('after-reset')
        successor.open()
        restored = self.root/'reset-restored'
        successor.restore(restored)
        self.assertEqual(json.loads((restored/'experimental-reset.json').read_text()), reset)
        for node in NODE_IDS:
            store = RecordStore(restored/'nodes'/node/'record')
            self.assertEqual(store.load()['version'], 0)
            store.close()
        with self.assertRaisesRegex(ValueError, 'cycle zero'):
            self.transport.reset(self.active, 'Must reject a non-reset experiment')

    def test_transfer_and_successor_preserve_history_identity_and_exclude_private_files(self):
        successor = self.new_transport('successor')
        successor.open()
        restored = self.root / 'restored'
        manifest = successor.restore(restored)
        self.assertEqual(manifest['installation_id'], 'test-installation')
        self.assertFalse((restored / 'private').exists())
        for node in NODE_IDS:
            source = RecordStore(self.active / 'nodes' / node / 'record')
            target = RecordStore(restored / 'nodes' / node / 'record')
            self.assertEqual(source.events(), target.events())
            self.assertEqual(source.head(), target.head())
            self.assertEqual(target.load()['version'], 1)
            source.close()
            target.close()
            control = json.loads((restored / 'nodes' / node / 'record/.wake-runner-control.json').read_text())
            self.assertEqual(control['research'], 'stopped')
        directory = restored / 'nodes/100.wake/record'
        store = RecordStore(directory)
        result = Engine(directory, dict(DEFAULTS), store=store,
                        effect_checkpoint=lambda: successor.checkpoint_node(directory)).run(Fixture('after-transfer'))
        self.assertEqual(result['status'], 'accepted')
        store.close()
        again = self.new_transport('again')
        again.open()
        again.restore(self.root / 'again-restored')
        store = RecordStore(self.root / 'again-restored/nodes/100.wake/record')
        self.assertEqual(store.load()['version'], 2)
        store.close()
        with successor.lease():
            successor.prune()
        # A previous complete checkpoint is retained in the same atomic tree.
        self.assertTrue((successor.checkout / 'previous.enc').exists())
        for item in self.assets.objects.values():
            self.assertNotIn(b'SQLite format', item['data'])
            self.assertNotIn(b'PRIVATE SIDECAR', item['data'])
        self.assertNotIn(b'test-installation', (successor.checkout / 'current.enc').read_bytes())
        parents = successor.git('rev-list', '--parents', '-n', '1', 'HEAD').split()
        self.assertEqual(len(parents), 1)  # Bounded transport history, full record history.

    def test_stale_runner_cannot_replace_a_newer_checkpoint(self):
        first, stale = self.new_transport('first'), self.new_transport('stale')
        first.open()
        stale.open()
        first.restore(self.root / 'first-root')
        stale.restore(self.root / 'stale-root')
        first.checkpoint_node(self.root / 'first-root/nodes/100.wake/record')
        with self.assertRaisesRegex(RuntimeError, 'Git operation failed'):
            stale.checkpoint_node(self.root / 'stale-root/nodes/100.wake/record')

    def test_growing_records_automatically_use_larger_blocks_without_losing_bytes(self):
        source = self.root / 'growing.bin'
        source.write_bytes(bytes(range(256)) * 1024)
        with patch('wake.hosted.BLOCK_SIZE', 1024):
            blocks = self.transport.put_file(source, self.transport.assets())
        self.assertLessEqual(len(blocks), 32)
        self.transport.get_file(blocks, self.root / 'growing-restored.bin')
        self.assertEqual(source.read_bytes(), (self.root / 'growing-restored.bin').read_bytes())

    def test_pruning_refuses_stale_ref_and_missing_recovery_blocks(self):
        first, stale = self.new_transport('prune-first'), self.new_transport('prune-stale')
        first.open()
        stale.open()
        first.restore(self.root / 'prune-root')
        first.checkpoint_node(self.root / 'prune-root/nodes/100.wake/record')
        before = set(self.assets.objects)
        with stale.lease(), self.assertRaisesRegex(RuntimeError, 'stale hosted ref'):
            stale.prune()
        self.assertEqual(before, set(self.assets.objects))
        current = first.read_manifest()
        missing = current['nodes']['103.wake']['blocks'][0]['id']
        del self.assets.objects[missing]
        before = set(self.assets.objects)
        with first.lease(), self.assertRaisesRegex(ValueError, 'Incomplete hosted recovery'):
            first.prune()
        self.assertEqual(before, set(self.assets.objects))

    def test_wrong_key_and_tampering_fail_closed(self):
        wrong = self.new_transport('wrong')
        wrong.key = b'z' * 32
        from cryptography.exceptions import InvalidTag
        with self.assertRaises(InvalidTag):
            wrong.open()
        successor = self.new_transport('tampered')
        successor.open()
        item = next(iter(self.assets.objects.values()))
        item['data'] = item['data'][:-1] + bytes([item['data'][-1] ^ 1])
        with self.assertRaises(InvalidTag):
            successor.restore(self.root / 'corrupt-root')

    def test_empty_or_existing_destinations_never_initialize_silently(self):
        missing = self.new_transport('missing')
        empty = self.root / 'empty.git'
        subprocess.run(['git', 'init', '--bare', '-q', str(empty)], check=True)
        with patch.object(LocalState, 'remote', empty):
            with self.assertRaisesRegex(ValueError, 'authority missing'):
                missing.open()
        successor = self.new_transport('occupied')
        successor.open()
        with self.assertRaisesRegex(ValueError, 'must be empty'):
            successor.restore(self.active)


    def test_quota_failed_upload_reconciles_absence_before_one_retry(self):
        from urllib.error import HTTPError
        base = self.assets.request
        uploads = []
        def quota_once(path, **kwargs):
            if kwargs.get('upload'):
                uploads.append(path)
                if len(uploads) == 1:
                    raise HTTPError('https://uploads.github.com',403,'Forbidden',{'X-RateLimit-Remaining':'0'},None)
            return base(path, **kwargs)
        with patch.object(self.assets, 'request', side_effect=quota_once):
            result = self.transport.put_block(b'quota-retry-proof', self.transport.assets())
        self.assertEqual(len(uploads),2)
        self.assertEqual(uploads[0],uploads[1])
        self.assertIn(result['id'],self.assets.objects)

    def test_ambiguous_upload_reuses_acknowledged_identity_without_reposting(self):
        from urllib.error import URLError
        base = self.assets.request
        uploads=[]
        def lost_response(path, **kwargs):
            result=base(path,**kwargs)
            if kwargs.get('upload'):
                uploads.append(path)
                raise URLError('lost response')
            return result
        with patch.object(self.assets,'request',side_effect=lost_response):
            result=self.transport.put_block(b'lost-response-proof',self.transport.assets())
        self.assertEqual(len(uploads),1)
        target=self.root/'reconciled.bin';self.transport.get_file([result],target)
        self.assertEqual(target.read_bytes(),b'lost-response-proof')

    def test_upload_permission_error_is_not_retried(self):
        from urllib.error import HTTPError
        base=self.assets.request;uploads=[]
        def forbidden(path,**kwargs):
            if kwargs.get('upload'):
                uploads.append(path)
                raise HTTPError('https://uploads.github.com',403,'Forbidden',{},None)
            return base(path,**kwargs)
        with patch.object(self.assets,'request',side_effect=forbidden):
            with self.assertRaises(HTTPError):
                self.transport.put_block(b'permission-proof',self.transport.assets())
        self.assertEqual(len(uploads),1)


class EffectCheckpointTests(unittest.TestCase):
    def test_recovery_rejects_a_self_consistent_projection_that_disagrees_with_receipt(self):
        from wake.kernel.record import _decode_projection_state, _encode_projection_state
        from wake.kernel.storage import canonical_json
        import hashlib
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            store = RecordStore(root, initialize_empty=True)
            Engine(root, dict(DEFAULTS), store=store).initialize()
            store.close()
            verify_recovery(root / 'wake.sqlite')
            with sqlite3.connect(root / 'wake.sqlite') as connection:
                raw = connection.execute('SELECT state FROM record_projection').fetchone()[0]
                state = json.loads(_decode_projection_state(raw))
                state['app:wake']['projection_state']['state']['objective'] = 'forged projection'
                encoded = canonical_json(state)
                connection.execute('UPDATE record_projection SET state=?,state_digest=?',
                    (_encode_projection_state(encoded), hashlib.sha256(encoded.encode()).hexdigest()))
            with self.assertRaisesRegex(ValueError, 'hash-linked application result'):
                verify_recovery(root / 'wake.sqlite')

    def test_physical_snapshot_includes_committed_wal(self):
        from wake.kernel.record import Record
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            record = Record(root / 'source.sqlite')
            with sqlite3.connect(root / 'source.sqlite') as connection:
                connection.execute('PRAGMA journal_mode=WAL')
                connection.execute('CREATE TABLE transport_probe(value TEXT)')
                connection.execute("INSERT INTO transport_probe VALUES ('committed WAL')")
                connection.commit()
                self.assertGreater((root / 'source.sqlite-wal').stat().st_size, 0)
                record.snapshot_to(root / 'snapshot.sqlite')
                with sqlite3.connect(root / 'snapshot.sqlite') as snapshot:
                    self.assertEqual(snapshot.execute('SELECT value FROM transport_probe').fetchone()[0], 'committed WAL')

    def test_verified_backup_still_rejects_semantically_corrupt_history(self):
        from wake.kernel.record import Record, IntegrityError
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            store = RecordStore(root / 'record', initialize_empty=True)
            Engine(root / 'record', dict(DEFAULTS), store=store).initialize()
            store.close()
            with sqlite3.connect(root / 'record/wake.sqlite') as connection:
                connection.execute('UPDATE events SET event_hash=? WHERE sequence=(SELECT MAX(sequence) FROM events)', ('f' * 64,))
            record = Record.open_read_only(root / 'record/wake.sqlite')
            record.snapshot_to(root / 'physical.sqlite')
            with self.assertRaises(IntegrityError):
                record.backup_to(root / 'verified.sqlite')

    def test_failed_injected_barrier_never_enters_provider(self):
        class Provider(Fixture):
            calls = 0
            def propose(self, *args, **kwargs):
                self.calls += 1
                return super().propose(*args, **kwargs)
        with tempfile.TemporaryDirectory() as folder:
            store = RecordStore(folder, initialize_empty=True)
            def fail():
                raise RuntimeError('remote unavailable')
            engine = Engine(folder, dict(DEFAULTS), store=store, effect_checkpoint=fail)
            engine.initialize()
            provider = Provider('fixture')
            with self.assertRaisesRegex(RuntimeError, 'remote unavailable'):
                engine.run(provider)
            self.assertEqual(provider.calls, 0)
            store.close()


class ContinuationTests(unittest.TestCase):
    def test_late_recovery_does_not_seed_a_second_chain_after_manual_start(self):
        from scripts.github_research import continue_chain
        class Client:
            def request(self, path, **kwargs):
                if kwargs.get('method') == 'POST':
                    raise AssertionError('Duplicate chain dispatch')
                if path == 'actions/runs/10':
                    return {'path': '.github/workflows/hosted-research.yml', 'head_branch': 'master', 'run_number': 10}
                return {'workflow_runs': [
                    {'id': 10, 'run_number': 10, 'status': 'completed', 'display_title': 'old run'},
                    {'id': 11, 'run_number': 11, 'status': 'completed', 'display_title': 'WAKE — Hosted research'}]}
        with patch('scripts.github_research.api', return_value=Client()), \
             patch('scripts.github_research.enabled', return_value=True):
            continue_chain('10')

    def test_current_run_can_dispatch_one_successor_from_checked_source(self):
        from scripts.github_research import continue_chain
        calls = []
        class Client:
            def request(self, path, **kwargs):
                if kwargs.get('method') == 'POST':
                    calls.append(kwargs['body'])
                    return
                if path == 'actions/runs/10':
                    return {'path': '.github/workflows/hosted-research.yml', 'head_branch': 'master', 'run_number': 10}
                return {'workflow_runs': [
                    {'id': 10, 'run_number': 10, 'status': 'in_progress', 'display_title': 'current'},
                    {'id': 9, 'run_number': 9, 'status': 'queued', 'display_title': 'stale older start'}]}
        with patch('scripts.github_research.api', return_value=Client()), \
             patch('scripts.github_research.enabled', return_value=True), \
             patch('scripts.github_research.checked_revision', return_value='a' * 40):
            continue_chain('10')
        self.assertEqual(calls, [{'ref': 'master', 'inputs': {'handoff': 'after-10', 'runtime_ref': 'a' * 40}}])


if __name__ == '__main__':
    unittest.main()
