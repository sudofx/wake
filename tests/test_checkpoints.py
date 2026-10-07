"""External witnesses detect replacement; signed seeds verify appended suffixes."""
import json
from pathlib import Path
import subprocess
import sqlite3
import tempfile
import unittest
from wake.checkpoints import create_checkpoint, replay_checkpoint, read_checkpoint, _compact_state
from wake.errors import IntegrityError
from wake.engine import DEFAULTS, Engine
from wake.record_store import RecordStore


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.private = self.root / 'private.pem'
        self.public = self.root / 'public.pem'
        subprocess.run(['openssl', 'genpkey', '-algorithm', 'ED25519', '-out', str(self.private)], check=True, capture_output=True)
        subprocess.run(['openssl', 'pkey', '-in', str(self.private), '-pubout', '-out', str(self.public)], check=True, capture_output=True)
        self.store = RecordStore(self.root / 'data', initialize_empty=True)
        self.engine = Engine(self.store.directory, dict(DEFAULTS), store=self.store)
        self.engine.initialize()
        self.checkpoint = self.root / 'witness'
        create_checkpoint(self.store.record, self.checkpoint, self.private)

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def test_suffix_matches_genesis_replay_and_reads_only_new_events(self):
        self.engine.observe('A new observation', 'operator:test')
        revision, state, proof = replay_checkpoint(self.store.record, self.checkpoint, self.public)
        full_revision, full_state = self.store.record.full_replay()
        self.assertEqual((revision, state), (full_revision, _compact_state(full_state)))
        self.assertEqual(proof['suffix_events_verified'], 1)
        self.assertEqual(replay_checkpoint(self.store.record, self.checkpoint, self.public, full=True)[:2], (revision, state))
        self.assertEqual(self.store.load()['evidence'][next(reversed(self.store.load()['evidence']))]['content'], 'A new observation')

    def test_modified_snapshot_and_wrong_key_fail(self):
        other = self.root / 'other.pem'
        subprocess.run(['openssl', 'genpkey', '-algorithm', 'ED25519', '-out', str(other)], check=True, capture_output=True)
        other_public = self.root / 'other-public.pem'
        subprocess.run(['openssl', 'pkey', '-in', str(other), '-pubout', '-out', str(other_public)], check=True, capture_output=True)
        with self.assertRaises(IntegrityError):
            read_checkpoint(self.checkpoint, other_public)
        snapshot = self.checkpoint / 'checkpoint.json'
        value = json.loads(snapshot.read_text()); value['revision'] += 1
        snapshot.write_text(json.dumps(value))
        with self.assertRaises(IntegrityError):
            read_checkpoint(self.checkpoint, self.public)

    def test_truncation_and_replacement_fail_against_external_witness(self):
        with self.store.record.connect() as connection:
            connection.execute('DELETE FROM events')
            connection.commit()
        with self.assertRaisesRegex(IntegrityError, 'rewrite or truncation'):
            replay_checkpoint(self.store.record, self.checkpoint, self.public)

    def test_suffix_tamper_fails_even_if_projection_still_looks_valid(self):
        self.engine.observe('A new observation', 'operator:test')
        with self.store.record.connect() as connection:
            connection.execute("UPDATE events SET payload='{}' WHERE sequence=(SELECT MAX(sequence) FROM events)")
            connection.commit()
        with self.assertRaises(IntegrityError):
            replay_checkpoint(self.store.record, self.checkpoint, self.public)

    def test_full_mode_detects_prefix_tamper_fast_mode_declares_its_trust_boundary(self):
        with self.store.record.connect() as connection:
            connection.execute("UPDATE events SET payload='{}' WHERE sequence=1")
            connection.commit()
        _, _, proof = replay_checkpoint(self.store.record, self.checkpoint, self.public)
        self.assertEqual(proof['verification'], 'signed-prefix-and-semantic-suffix')
        with self.assertRaises(IntegrityError):
            replay_checkpoint(self.store.record, self.checkpoint, self.public, full=True)

    def test_checkpoint_never_overwrites_retained_witness(self):
        before = (self.checkpoint / 'checkpoint.json').read_bytes()
        with self.assertRaises(FileExistsError):
            create_checkpoint(self.store.record, self.checkpoint, self.private)
        self.assertEqual(before, (self.checkpoint / 'checkpoint.json').read_bytes())

    def test_provider_journal_tamper_prevents_new_signed_checkpoint(self):
        from wake.providers import Fixture
        self.engine.run(Fixture('checkpoint-test'))
        self.assertGreater(len(self.store.record.invocation_history()), 0)
        with self.store.record.connect() as connection:
            connection.execute("UPDATE invocation_events SET event_hash='forged-hash' WHERE sequence=1")
            connection.commit()
        with self.assertRaises(IntegrityError):
            create_checkpoint(self.store.record, self.root / 'tampered-witness', self.private)
        self.assertFalse((self.root / 'tampered-witness').exists())

    def test_seed_omits_old_application_log_but_keeps_replayable_projection(self):
        seed = read_checkpoint(self.checkpoint, self.public)
        envelope = seed['state']['app:wake']
        self.assertNotIn('events', envelope)
        self.assertEqual(envelope['projection_state']['state'], self.store.load())
        self.assertGreater(len(self.store.record.history()), 0)

    def test_read_only_inspector_never_initializes_or_migrates_unknown_files(self):
        from wake.kernel.record import Record, StorageVersionError
        missing = self.root / 'missing.sqlite'
        with self.assertRaises(sqlite3.OperationalError):
            Record.open_read_only(missing)
        self.assertFalse(missing.exists())
        unknown = self.root / 'unrelated.sqlite'
        with sqlite3.connect(unknown) as connection:
            connection.execute('CREATE TABLE unrelated(value TEXT)')
        original = unknown.read_bytes()
        with self.assertRaises(StorageVersionError):
            Record.open_read_only(unknown)
        self.assertEqual(unknown.read_bytes(), original)
        readonly = Record.open_read_only(self.store.path)
        with readonly.connect() as connection:
            with self.assertRaises(sqlite3.OperationalError):
                connection.execute('DELETE FROM events')
