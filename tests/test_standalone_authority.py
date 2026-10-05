"""Standalone record adoption preserves meaning and fails closed on ambiguity."""
from pathlib import Path
import tempfile
import unittest
import sqlite3

from wake.authority import open_authoritative_store
from wake.errors import IntegrityError
from wake.engine import Engine, DEFAULTS
from wake.providers import Fixture
from wake.kernel.record import Record
from scripts.github_wake import StateBranch
import test_cloud_workflow as cloud_tests


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


class CheckpointAdoptionTests(unittest.TestCase):
    setUp = cloud_tests.CloudWorkflowTests.setUp
    tearDown = cloud_tests.CloudWorkflowTests.tearDown
    git = cloud_tests.CloudWorkflowTests.git
    live = cloud_tests.CloudWorkflowTests.live
    run_cloud = cloud_tests.CloudWorkflowTests.run_cloud
    # Reuse the realistic Git transport harness without duplicating its suite.
    def test_previous_archive_is_verified_and_replaced_by_canonical_package(self):
        self.assertEqual(self.run_cloud(Fixture('before-adoption')), 0)
        checkout = self.root / 'renamed-checkpoint'
        self.git('clone', '--branch', 'wake-state', self.remote, checkout)
        self.git('-C', checkout, 'mv', 'data/wake.sqlite.gz', 'data/previous.sqlite.gz')
        self.git('-C', checkout, '-c', 'user.name=test', '-c', 'user.email=test@example.com',
                 'commit', '-m', 'Previous checkpoint filename')
        self.git('-C', checkout, 'push', 'origin', 'wake-state')
        with tempfile.TemporaryDirectory() as temporary:
            branch = StateBranch(self.project, Path(temporary) / 'state')
            branch.open()
            before = Record(branch.checkout / 'data/wake.sqlite').full_replay()
            branch.checkpoint()
            self.assertEqual(Record(branch.checkout / 'data/wake.sqlite').full_replay(), before)
        tree = self.git('--git-dir', self.remote, 'ls-tree', '-r', '--name-only', 'wake-state').stdout
        self.assertEqual(tree.strip(), 'data/wake.sqlite.gz')
        self.assertEqual(self.run_cloud(Fixture('after-adoption')), 0)
        self.assertEqual(self.live()['state']['version'], 2)
