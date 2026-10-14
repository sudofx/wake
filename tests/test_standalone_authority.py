"""Standalone record adoption preserves meaning and fails closed on ambiguity."""
from pathlib import Path
import tempfile
import unittest
import sqlite3

from wake.authority import open_authoritative_store
from wake.errors import IntegrityError
from wake.engine import Engine, DEFAULTS
from wake.providers import Fixture


class RecordAdoptionTests(unittest.TestCase):
    def test_previous_filename_preserves_exact_record_and_domain_history(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            store = open_authoritative_store(root, allow_initialize=True)
            engine = Engine(root, dict(DEFAULTS), store=store)
            engine.initialize()
            self.assertEqual(engine.run(Fixture('standalone'))['status'], 'accepted')
            before = (store.load(), store.events(), store.head(), store.record.full_replay(),
                      store.invocation_history())
            store.close()
            (root / 'wake.sqlite').rename(root / 'previous.sqlite')
            adopted = open_authoritative_store(root)
            try:
                after = (adopted.load(), adopted.events(), adopted.head(), adopted.record.full_replay(),
                         adopted.invocation_history())
                self.assertEqual(before, after)
                self.assertFalse((root / 'previous.sqlite').exists())
                self.assertEqual(Engine(root, dict(DEFAULTS), store=adopted).run(Fixture('after-adoption'))['status'], 'accepted')
            finally:
                adopted.close()
            reopened = open_authoritative_store(root)
            self.assertEqual(reopened.load()['version'], 2)
            reopened.close()

    def test_multiple_candidates_or_canonical_plus_previous_fail_closed(self):
        for canonical in (False, True):
            with self.subTest(canonical=canonical), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / ('wake.sqlite' if canonical else 'first.sqlite')).write_bytes(b'unchanged')
                (root / 'second.sqlite').write_bytes(b'unchanged')
                with self.assertRaisesRegex(IntegrityError, 'Ambiguous'):
                    open_authoritative_store(root, allow_initialize=True)
                self.assertEqual((root / 'second.sqlite').read_bytes(), b'unchanged')

    def test_corrupt_previous_record_is_never_replaced_or_initialized(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'previous.sqlite'
            source.write_bytes(b'not a database')
            with self.assertRaises(sqlite3.DatabaseError):
                open_authoritative_store(root, allow_initialize=True)
            self.assertEqual(source.read_bytes(), b'not a database')
            self.assertFalse((root / 'wake.sqlite').exists())

    def test_unrelated_sqlite_is_rejected_without_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'previous.sqlite'
            with sqlite3.connect(source) as database:
                database.execute('CREATE TABLE unrelated (value TEXT)')
            before = source.read_bytes()
            with self.assertRaisesRegex(IntegrityError, 'Unrecognized'):
                open_authoritative_store(root, allow_initialize=True)
            self.assertEqual(source.read_bytes(), before)
            self.assertFalse((root / 'wake.sqlite').exists())
