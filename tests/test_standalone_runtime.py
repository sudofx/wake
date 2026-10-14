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
    def test_next_group_post_pause_survives_until_a_new_publication(self):
        from wake.standalone import _pause_after_introduction, _research_control
        with tempfile.TemporaryDirectory() as directory:
            control = Path(directory) / '.wake-runner-control.json'
            control.write_text(json.dumps({'research':'running','pause_after_group_checkpoint':2}))
            self.assertFalse(_pause_after_introduction(directory, {'group_bob':{'checkpoint':1}}))
            self.assertEqual(_research_control(directory, 'paused')[0], 'running')
            self.assertTrue(_pause_after_introduction(directory, {'group_bob':{'checkpoint':18}}))
            self.assertEqual(_research_control(directory, 'running')[0], 'paused')
            self.assertNotIn('pause_after_group_checkpoint', json.loads(control.read_text()))

    def test_operator_first_post_pause_is_consumed_without_research_progress(self):
        from wake.standalone import _pause_after_introduction, _research_control
        with tempfile.TemporaryDirectory() as directory:
            control=Path(directory)/'.wake-runner-control.json'
            control.write_text(json.dumps({'research':'running','pause_after_group_introduction':True}))
            self.assertFalse(_pause_after_introduction(directory,{'group_bob':{'checkpoint':0}}))
            self.assertEqual(_research_control(directory)[0],'running')
            self.assertTrue(_pause_after_introduction(directory,{'version':0,'group_bob':{'checkpoint':1}}))
            self.assertEqual(_research_control(directory)[0],'paused')
            self.assertNotIn('pause_after_group_introduction',json.loads(control.read_text()))

    def test_group_startup_waits_for_shared_intro_without_child_research_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = bootstrap(directory, dict(DEFAULTS))
            args = SimpleNamespace(interval=1, config='unused', provider='fixture',
                data=directory, paused=False, enable_continuity_matrix=False,
                host='127.0.0.1', port=0, model='test')
            server, stop = MagicMock(), MagicMock()
            stop.is_set.side_effect = [False, True]
            with patch.dict(os.environ, {'WAKE_GROUP_ID':'wake','WAKE_PUBLIC_HOSTNAME':'101.wake'}), \
                 patch('wake.standalone.config', return_value=dict(DEFAULTS)), \
                 patch('wake.standalone.bootstrap', return_value=engine), \
                 patch('wake.standalone.publish', return_value=True), \
                 patch('wake.standalone.ThreadingHTTPServer', return_value=server), \
                 patch('wake.standalone.threading.Thread'), \
                 patch('wake.standalone.threading.Event', return_value=stop), \
                 patch('wake.group_editorial.synchronize',return_value=False), \
                 patch.object(engine,'run') as cycle:
                run(args)
            cycle.assert_not_called()
            self.assertEqual(server.runtime_status['state'],'waiting')
            self.assertIn('WAKE01',server.runtime_status['reason'])

    def test_installation_research_proceeds_before_group_blog_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = bootstrap(directory, dict(DEFAULTS))
            engine.store.append('group_bob_enrolled', {'actor':'operator', 'group_id':'wake',
                'members':['100.wake','101.wake'], 'leader':'100.wake', 'member':'101.wake'})
            args = SimpleNamespace(interval=1, config='unused', provider='fixture',
                data=directory, paused=False, enable_continuity_matrix=False,
                host='127.0.0.1', port=0, model='test')
            server, stop = MagicMock(), MagicMock()
            stop.is_set.return_value = False
            with patch.dict(os.environ, {'WAKE_GROUP_ID':'wake','WAKE_PUBLIC_HOSTNAME':'101.wake',
                                        'WAKE_INSTALLATION_WORKER':'1','WAKE_CONTROLLER_PID':str(os.getppid())}), \
                 patch('ctypes.CDLL',return_value=SimpleNamespace(prctl=lambda *args:0)), \
                 patch('wake.standalone.config', return_value=dict(DEFAULTS)), \
                 patch('wake.standalone.bootstrap', return_value=engine), \
                 patch('wake.standalone.publish', return_value=True), \
                 patch('wake.standalone.ThreadingHTTPServer', return_value=server), \
                 patch('wake.standalone.threading.Thread'), \
                 patch('wake.standalone.threading.Event', return_value=stop), \
                 patch('wake.standalone._wait_for_control', return_value=True), \
                 patch('wake.standalone.collect_group_peer_research', return_value={}), \
                 patch('wake.group_editorial.synchronize',return_value=False), \
                 patch.object(engine,'run',return_value={'status':'accepted'}) as cycle:
                run(args)
            cycle.assert_called_once()
            self.assertEqual(engine.store.load()['group_bob']['checkpoint'],0)
            engine.store.close()

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

    def test_provider_quota_stays_purple_and_retries_on_the_regular_interval(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = bootstrap(directory, dict(DEFAULTS))
            args = SimpleNamespace(interval=1, config='unused', provider='fixture',
                data=directory, paused=False, enable_continuity_matrix=False,
                host='127.0.0.1', port=0, model='test')
            server, stop = MagicMock(), MagicMock()
            stop.is_set.side_effect = [False, True]
            due = {'next_eligible': None, 'quota_standby': True,
                   'provider_quota_limited': True, 'quota_standby_until': None}
            with patch('wake.standalone.config', return_value=dict(DEFAULTS)), \
                 patch('wake.standalone.bootstrap', return_value=engine), \
                 patch('wake.standalone.verify_existing_record'), \
                 patch('wake.standalone.publish', return_value=True), \
                 patch('wake.standalone.ThreadingHTTPServer', return_value=server), \
                 patch('wake.standalone.threading.Thread'), \
                 patch('wake.standalone.threading.Event', return_value=stop), \
                 patch('wake.standalone.wake_status', side_effect=[{'next_eligible': None}, due]), \
                 patch('wake.standalone._wait_for_control', return_value=True) as wait_for_control, \
                 patch.object(engine, 'run', return_value={'status': 'deferred', 'reason': 'quota'}):
                run(args)
            self.assertEqual(server.runtime_status['state'], 'standby')
            self.assertIn('retrying on the regular schedule', server.runtime_status['reason'])
            self.assertEqual(wait_for_control.call_args.args[2], args.interval)

    def test_mandatory_matrix_preserves_history_advances_and_survives_restart(self):
        with tempfile.TemporaryDirectory() as directory:
            data = Path(directory) / 'data'
            root = Path(directory) / 'website'
            root.mkdir()
            engine = bootstrap(data, dict(DEFAULTS))
            for _ in range(7):
                engine.run(Fixture('before-opt-in'))
            before = engine.store.events()
            self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 7)
            engine.store.close()

            engine = bootstrap(data, dict(DEFAULTS), enable_continuity_matrix=True)
            self.assertEqual(engine.store.events(), before)
            self.assertEqual(engine.store.load()['version'], 7)
            self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 7)
            opted_in_record = engine.store.record.full_replay()
            engine.store.close()
            engine = bootstrap(data, dict(DEFAULTS), enable_continuity_matrix=True)
            self.assertEqual(engine.store.record.full_replay(), opted_in_record)
            engine.run(Fixture('after-opt-in'))
            self.assertEqual(engine.store.events()[:len(before)], before)
            self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 8)
            publish(engine, root)
            matrix = json.loads((root / 'current' / 'research-data.json').read_text())['matrix']
            self.assertTrue(matrix['enabled'])
            self.assertEqual(matrix['completed'], 8)
            engine.store.close()
            engine = bootstrap(data, dict(DEFAULTS))
            self.assertEqual(engine.store.continuity_matrix_progress()['completed_count'], 8)
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

    def test_group_http_serves_atomic_export_without_record_reads(self):
        from functools import partial
        from http.server import ThreadingHTTPServer
        import threading
        from urllib.request import urlopen
        from urllib.error import HTTPError
        from wake.standalone import Website

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'website'
            root.mkdir()
            engine = bootstrap(Path(directory) / 'data', dict(DEFAULTS))
            identity = {'WAKE_GROUP_ID': 'wake', 'WAKE_PUBLIC_HOSTNAME': '100.wake',
                        'WAKE_GROUP_INSTANCE': 'wake-100'}
            with patch.dict(os.environ, identity):
                self.assertTrue(publish(engine, root))
                head = engine.store.head()
                server = ThreadingHTTPServer(('127.0.0.1', 0),
                    partial(Website, directory=str(root / 'current')))
                server.engine = MagicMock()
                server.engine.store.load.side_effect = AssertionError('HTTP read authority')
                server.engine.store.replay.side_effect = AssertionError('HTTP replayed authority')
                thread = threading.Thread(target=server.serve_forever, daemon=True)
                thread.start()
                try:
                    base = f'http://127.0.0.1:{server.server_port}/group/'
                    packets = {}
                    for name in ('bob-input.json', 'bob-publication.json', 'bob.json', 'research.json'):
                        with urlopen(base + name, timeout=2) as response:
                            packets[name] = json.load(response)
                    self.assertEqual(packets['bob-input.json']['head'], head)
                    self.assertEqual(packets['bob.json']['application_head'], head)
                    self.assertEqual(packets['research.json']['application_head'], head)
                    self.assertIsNone(packets['bob-publication.json'])
                    self.assertEqual(engine.store.head(), head)
                    # An absent export is unavailable, never a live-record fallback.
                    (root / 'current' / 'group' / 'bob.json').unlink()
                    with self.assertRaises(HTTPError) as missing:
                        urlopen(base + 'bob.json', timeout=2)
                    self.assertEqual(missing.exception.code, 503)
                    missing.exception.close()
                    self.assertTrue(publish(engine, root))
                    with urlopen(base + 'bob.json', timeout=2) as response:
                        self.assertEqual(json.load(response)['application_head'], head)
                    server.engine.store.load.assert_not_called()
                    server.engine.store.replay.assert_not_called()
                finally:
                    server.shutdown()
                    server.server_close()
                    thread.join(timeout=2)
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
