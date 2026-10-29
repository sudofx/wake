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

    def test_saved_configuration_dependencies_are_available_to_request_builder(self):
        config = self.root / 'config/wake.toml'
        config.parent.mkdir()
        config.write_bytes((ROOT / 'wake.toml').read_bytes())
        (config.parent / 'research-topics.toml').write_bytes((ROOT / 'example.research-topics.toml').read_bytes())
        topics = config.parent / '.wake-runner-topics/100.wake.toml'
        topics.parent.mkdir()
        topics.write_bytes((ROOT / 'example.research-topics.toml').read_bytes())
        result = diag.probe_node(ROOT, self.record, config, node='101.wake')
        self.assertTrue(all(value['status'] == 'fits' for value in result), result)

    def test_credential_environment_is_not_inherited_by_copy_execution(self):
        observed = []
        def runner(command, **kwargs):
            observed.append(kwargs['env'])
            self.assertNotEqual(Path(command[-3]), self.record.parent)
            self.assertIn('socket.socket=forbidden', command[2])
            return json.dumps({'phase': command[-1], 'provider_calls': 0, 'status': 'fits'})
        with patch.dict(os.environ, {'LD_LIBRARY_PATH':'/fixture/python/lib', 'GEMINI_API_KEY':'fixture', 'GH_TOKEN':'fixture', 'WAKE_HOSTED_STATE_KEY':'fixture', 'UNRELATED_SECRET':'fixture'}):
            diag.probe_node(ROOT, self.record, ROOT / 'wake.toml', node='101.wake', runner=runner)
        self.assertTrue(observed)
        self.assertTrue(all(env.get('LD_LIBRARY_PATH') == '/fixture/python/lib' for env in observed))
        self.assertTrue(all(not any('KEY' in key or 'TOKEN' in key or 'SECRET' in key for key in env) for env in observed))
