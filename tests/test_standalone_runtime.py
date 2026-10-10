"""Independent-volume bootstrap and continuity guarantees."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, MagicMock
from types import SimpleNamespace
import os
import json
import shutil
import subprocess

from wake.engine import DEFAULTS
from wake.errors import IntegrityError
from wake.providers import Fixture
from wake.standalone import bootstrap, load_secret, publish, run
from wake.governance import Rejected


class StandaloneRuntimeTests(unittest.TestCase):
    def test_runner_control_file_does_not_block_fresh_volume_bootstrap(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / 'data'
            data.mkdir()
            (data / '.wake-runner-control.json').write_text('{"research":"running"}')

            engine = bootstrap(data, dict(DEFAULTS), enable_continuity_matrix=True)
            try:
                self.assertTrue((data / 'wake.sqlite').exists())
                self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 0)
            finally:
                engine.store.close()

    def test_context_limit_keeps_website_available_without_retrying(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = bootstrap(directory, dict(DEFAULTS))
            args = SimpleNamespace(interval=1, config='unused', provider='fixture',
                                   data=directory, paused=False, enable_continuity_matrix=False,
                                   host='127.0.0.1', port=0, model='test')
            server = MagicMock()
            stop = MagicMock()
            stop.is_set.side_effect = [False]
            reason = 'Context ceiling reached; human review required, no model call made'
            with patch('wake.standalone.config', return_value=dict(DEFAULTS)), \
                 patch('wake.standalone.bootstrap', return_value=engine), \
                 patch('wake.standalone.verify_existing_record'), \
                 patch('wake.standalone.publish', return_value=True), \
                 patch('wake.standalone.ThreadingHTTPServer', return_value=server), \
                 patch('wake.standalone.threading.Thread'), \
                 patch('wake.standalone.threading.Event', return_value=stop), \
                 patch.object(engine, 'run', side_effect=Rejected(reason)) as cycle:
                run(args)
            cycle.assert_called_once()
            stop.wait.assert_called_once()
            self.assertEqual(server.runtime_status['state'], 'blocked')
            self.assertEqual(server.runtime_status['reason'], reason)

    def test_permanent_provider_failure_stays_visible_without_repeating_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = bootstrap(directory, dict(DEFAULTS))
            args = SimpleNamespace(interval=1, config='unused', provider='fixture',
                data=directory, paused=False, enable_continuity_matrix=False,
                host='127.0.0.1', port=0, model='test')
            server, stop = MagicMock(), MagicMock()
            stop.is_set.side_effect = [False]
            with patch('wake.standalone.config', return_value=dict(DEFAULTS)), \
                 patch('wake.standalone.bootstrap', return_value=engine), \
                 patch('wake.standalone.verify_existing_record'), \
                 patch('wake.standalone.publish', return_value=True), \
                 patch('wake.standalone.ThreadingHTTPServer', return_value=server), \
                 patch('wake.standalone.threading.Thread'), \
                 patch('wake.standalone.threading.Event', return_value=stop), \
                 patch.object(engine, 'run', return_value=dict(status='failed', reason='Invalid provider credential')) as cycle:
                run(args)
            cycle.assert_called_once()
            stop.wait.assert_called_once()
            self.assertEqual(server.runtime_status['state'], 'blocked')
            self.assertEqual(server.runtime_status['reason'], 'Invalid provider credential')

    def test_matrix_opt_in_preserves_history_advances_and_survives_restart(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / 'data'
            root = Path(directory) / 'website'
            root.mkdir()
            engine = bootstrap(data, dict(DEFAULTS))
            for _ in range(7):
                engine.run(Fixture('before-opt-in'))
            before = engine.store.events()
            self.assertIsNone(engine.store.continuity_matrix_progress())
            engine.store.close()

            engine = bootstrap(data, dict(DEFAULTS), enable_continuity_matrix=True)
            self.assertEqual(engine.store.events(), before)
            self.assertEqual(engine.store.load()['version'], 7)
            self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 0)
            opted_in_record = engine.store.record.full_replay()
            engine.store.close()
            engine = bootstrap(data, dict(DEFAULTS), enable_continuity_matrix=True)
            self.assertEqual(engine.store.record.full_replay(), opted_in_record)
            engine.run(Fixture('after-opt-in'))
            self.assertEqual(engine.store.events()[:len(before)], before)
            self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 1)
            publish(engine, root)
            matrix = json.loads((root / 'current' / 'research-data.json').read_text())['matrix']
            self.assertTrue(matrix['enabled'])
            self.assertEqual(matrix['completed'], 1)
            engine.store.close()
            engine = bootstrap(data, dict(DEFAULTS))
            self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 1)
            engine.store.record.full_replay()
            engine.store.close()

    def test_reopen_keeps_exact_history_and_appends(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / 'data'
            engine = bootstrap(data, dict(DEFAULTS))
            engine.run(Fixture('first'))
            before = engine.store.events()
            head = engine.store.head()
            engine.store.close()
            reopened = bootstrap(data, dict(DEFAULTS))
            self.assertEqual(reopened.store.head(), head)
            self.assertEqual(reopened.store.events(), before)
            reopened.run(Fixture('second'))
            self.assertEqual(reopened.store.events()[:len(before)], before)
            self.assertEqual(reopened.store.load()['version'], 2)
            reopened.store.record.full_replay()
            reopened.store.close()

    def test_missing_used_authority_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory)
            engine = bootstrap(data, dict(DEFAULTS))
            engine.store.close()
            (data / 'wake.sqlite').unlink()
            with self.assertRaises(IntegrityError):
                bootstrap(data, dict(DEFAULTS))
            self.assertFalse((data / 'wake.sqlite').exists())

    def test_corruption_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'wake.sqlite'
            path.write_bytes(b'not a record')
            with self.assertRaises(Exception):
                bootstrap(directory, dict(DEFAULTS))
            self.assertEqual(path.read_bytes(), b'not a record')

    def test_restart_closes_abandoned_provider_invocation(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = bootstrap(directory, dict(DEFAULTS))
            with engine.store.lock():
                invocation, _ = engine.start('fixture', 'interrupted')
            engine.store.close()
            recovered = bootstrap(directory, dict(DEFAULTS))
            state = recovered.store.load()
            self.assertIsNone(state['pending'])
            self.assertEqual(state['invocations'][invocation]['status'], 'recovered')
            recovered.store.record.full_replay()
            recovered.store.close()

    def test_website_snapshot_marks_local_mode_without_changing_record(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / 'data'
            root = Path(directory) / 'website'
            root.mkdir()
            engine = bootstrap(data, dict(DEFAULTS))
            head = engine.store.head()
            publish(engine, root)
            for page in (root / 'current').rglob('*.html'):
                self.assertIn('window.WAKE_STANDALONE=true', page.read_text())
            self.assertEqual(json.loads((root / 'current' / 'deployment.json').read_text()),
                             {'schema': 1, 'mode': 'standalone'})
            self.assertEqual((root / 'current' / 'head.txt').read_text().strip(), head)
            self.assertFalse((root / 'current' / 'wake.sqlite').exists())
            self.assertEqual(engine.store.head(), head)
            engine.store.close()

    def test_secret_file_is_runtime_only_and_ambiguity_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'key'
            path.write_text('test-secret\n')
            with patch.dict(os.environ, {'GEMINI_API_KEY_FILE': str(path)}, clear=True):
                load_secret()
                self.assertEqual(os.environ['GEMINI_API_KEY'], 'test-secret')
                with self.assertRaises(ValueError):
                    load_secret()

    @unittest.skipUnless(shutil.which('node'), 'Node is optional browser-boundary verification')
    def test_home_bootstrap_fetches_only_its_installation(self):
        # Execute the actual home-page bootstrap, rather than checking source strings.
        page = (Path(__file__).resolve().parents[1] / 'wake/assets/index.html').read_text()
        javascript = r"""
const vm=require('node:vm');
let html='';process.stdin.on('data',chunk=>html+=chunk);
process.stdin.on('end',async()=>{
  const script=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]).find(s=>s.includes('window.WakeLiveUrl='));
  const results=[];
  for(const local of [true,false,null]){
    const calls=[];
    const window=local===null?{}:{WAKE_DEPLOYMENT:{schema:1,mode:local?'standalone':'hosted'}};
    vm.runInNewContext(script,{window,Date,fetch:async url=>{calls.push(url);return {ok:true,json:async()=>({state:{version:0},head:'test'})}}});
    await window.WakeData;results.push(calls);
  }
  process.stdout.write(JSON.stringify(results));
});
"""
        result = subprocess.run(['node', '-e', javascript], input=page, text=True,
                                capture_output=True, check=True)
        local, hosted, unknown = json.loads(result.stdout)
        self.assertTrue(local and all(url.startswith('wake-data.json?') for url in local))
        self.assertTrue(hosted[0].startswith('https://raw.githubusercontent.com/sudofx/wake/wake-live/'))
        self.assertTrue(unknown and all(url.startswith('wake-data.json?') for url in unknown))

    def test_busy_operator_does_not_discard_website_or_stop_refresh(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / 'data'
            root = Path(directory) / 'website'
            root.mkdir()
            engine = bootstrap(data, dict(DEFAULTS))
            self.assertTrue(publish(engine, root))
            before = (root / 'current').resolve()
            with engine.store.lock():
                self.assertFalse(publish(engine, root))
            self.assertEqual((root / 'current').resolve(), before)
            self.assertTrue(publish(engine, root))
            engine.store.close()
