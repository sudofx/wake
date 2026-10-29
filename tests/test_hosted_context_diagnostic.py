"""Capacity diagnosis isolates copied authority and never supplies network credentials."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.autonomous_demo import settings, seed
from wake.engine import Engine
from wake.record_store import RecordStore
from wake.hosted import record_identity

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('context_diagnostic', ROOT / 'scripts/diagnose_hosted_context.py')
diag = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diag)


class ContextDiagnosticTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        directory = self.root / 'record'
        store = RecordStore(directory, initialize_empty=True)
        engine = Engine(directory, settings(), store=store)
        engine.initialize();seed(engine);store.close()
        self.record = directory / 'wake.sqlite'

    def test_real_requests_build_only_on_copies_and_source_head_is_unchanged(self):
        before = record_identity(self.record)
        result = diag.probe_node(ROOT, self.record, ROOT / 'wake.toml', node='101.wake')
        self.assertEqual([value['phase'] for value in result], ['planning', 'proposal'])
        self.assertTrue(all(value['provider_calls'] == 0 for value in result))
        self.assertTrue(all(value['status'] == 'fits' for value in result), result)
        self.assertEqual(record_identity(self.record), before)

    def test_credential_environment_is_not_inherited_by_copy_execution(self):
        observed = []
        def runner(command, **kwargs):
            observed.append(kwargs['env'])
            self.assertNotEqual(Path(command[-3]), self.record.parent)
            self.assertIn('socket.socket=forbidden', command[2])
            return json.dumps({'phase': command[-1], 'provider_calls': 0, 'status': 'fits'})
        with patch.dict(os.environ, {'GEMINI_API_KEY':'fixture', 'GH_TOKEN':'fixture', 'WAKE_HOSTED_STATE_KEY':'fixture', 'UNRELATED_SECRET':'fixture'}):
            diag.probe_node(ROOT, self.record, ROOT / 'wake.toml', node='101.wake', runner=runner)
        self.assertTrue(observed)
        self.assertTrue(all(not any('KEY' in key or 'TOKEN' in key or 'SECRET' in key for key in env) for env in observed))
