"""Bounded, read-only status transport; no authority, workers or providers."""
import json
from datetime import datetime, timezone, timedelta
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from unittest.mock import patch

from wake.installation import Controller, InstallationHTTP, read_json, worker_runtime


class InstallationObserverTests(unittest.TestCase):
    def test_research_http_admission_preserves_authentication_and_quota(self):
        self.controller.mode = 'running'
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(InstallationHTTP, directory=str(self.root)))
        server.controller = self.controller
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        packet = {'action': 'acquire', 'member': '100.wake', 'request_id': 'a' * 32,
                  'model': 'fixture'}
        def post(body, token=None):
            headers = {'Content-Type': 'application/json',
                       'Authorization': 'Bearer ' + (token or self.controller.token)}
            request = Request(f'http://127.0.0.1:{server.server_port}/group/coordinator',
                              data=json.dumps(body).encode(), headers=headers, method='POST')
            with urlopen(request, timeout=2) as response:
                return json.load(response)
        try:
            for body, token, status in ((packet, 'invalid', 403),
                    ({**packet, 'member': 'unknown'}, None, 400)):
                with self.assertRaises(HTTPError) as error:
                    post(body, token)
                self.assertEqual(error.exception.code, status)
                error.exception.close()
            granted = post(packet)
            self.assertEqual(granted['status'], 'granted')
            post({**packet, 'action': 'release', 'token': granted['token'],
                  'outcome': {'result': 'daily_quota'}})
            blocked = post({**packet, 'request_id': 'b' * 32})
            self.assertEqual(blocked['reason'], 'daily_quota')
            self.assertIsNone(self.controller.coordinator.status()['active'])
            self.controller.mode = 'stopped'
            with self.assertRaises(HTTPError) as error:
                post({**packet, 'request_id': 'c' * 32})
            self.assertEqual(error.exception.code, 409)
            error.exception.close()
        finally:
            server.shutdown()
            server.server_close()
            thread.join(2)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.controller = Controller(self.root, self.root / 'fixture.toml', 'fixture', 0)
        self.controller.mode = 'running'
        node = self.root / 'nodes/100.wake'
        node.mkdir(parents=True)
        (node / 'runtime.json').write_text(json.dumps({
            'mode': 'standalone', 'state': 'running', 'activity_schema': 1,
            'runtime_id': 'test-runtime', 'observed_at': datetime.now(timezone.utc).isoformat(),
            'capabilities': {'live_activity': True, 'secret': 'private-marker'},
            'activity': {'stage': 'context', 'active': True, 'private': 'private-marker'},
            'private': 'private-marker', 'development': {'large': 'x' * 24000}}))
        (node / 'site/current').mkdir(parents=True)
        (node / 'site/current/head.txt').write_text('a' * 64)

    def tearDown(self):
        self.controller.shutdown.set()
        self.temp.cleanup()

    def test_small_shared_sample_ignores_private_fields_and_research(self):
        with patch('wake.installation.read_json', wraps=read_json) as reads:
            first = self.controller.runtime_snapshot()
            second = self.controller.runtime_snapshot()
            self.assertIs(first, second)
            self.assertLessEqual(len(reads.call_args_list), 13)
            self.assertTrue(all(Path(call.args[0]).name in {'runtime.json', 'installation-id.json'}
                                for call in reads.call_args_list))
        encoded = json.dumps(first)
        self.assertNotIn('private-marker', encoded)
        self.assertNotIn('large', encoded)
        self.assertLess(len(encoded), 12000)
        self.assertEqual(first['members'][0]['head'], 'a' * 64)
        self.assertEqual(first['members'][0]['runtime']['activity']['stage'], 'context')
        self.assertTrue(first['capabilities']['status_stream'])
        self.assertFalse(list(self.root.rglob('*.sqlite')))
        self.controller.mode = 'paused'
        self.assertEqual(self.controller.runtime_snapshot()['research'], 'paused')

    def test_stale_or_future_worker_observations_are_not_live(self):
        path = self.root / 'nodes/100.wake/runtime.json'
        for offset in (-20, 20):
            path.write_text(json.dumps({'state': 'running', 'observed_at':
                (datetime.now(timezone.utc) + timedelta(seconds=offset)).isoformat()}))
            self.assertEqual(worker_runtime(self.root, '100.wake')['state'], 'unavailable')

    def test_comparison_reads_cached_exports_when_every_worker_is_unavailable(self):
        self.controller.manifest_sample = {'schema': 1, 'installation_id': 'fixture',
            'nodes': [{'id': '100.wake', 'available': True,
                       'snapshot': {'head': 'a' * 64, 'version': 3},
                       'research': {'version': 3}}]}
        (self.root / 'nodes/100.wake/runtime.json').unlink()
        with patch('wake.installation.read_json', wraps=read_json) as reads:
            packet = self.controller.installation_manifest()
        self.assertTrue(packet['nodes'][0]['available'])
        self.assertEqual(packet['nodes'][0]['runtime']['state'], 'unavailable')
        self.assertEqual(packet['nodes'][0]['snapshot']['version'], 3)
        self.assertTrue(all(Path(call.args[0]).name in {'runtime.json', 'installation-id.json'}
                            for call in reads.call_args_list))
        self.assertNotIn('runtime', self.controller.manifest_sample['nodes'][0])

    def test_atomic_export_writers_do_not_share_a_temporary_filename(self):
        from concurrent.futures import ThreadPoolExecutor
        from wake.report import atomic_write
        target = self.root / 'status.json'
        with ThreadPoolExecutor(max_workers=8) as executor:
            list(executor.map(lambda value: atomic_write(target, json.dumps({'value': value})), range(64)))
        self.assertIn(json.loads(target.read_text())['value'], range(64))
        self.assertEqual(list(self.root.glob('status.json.*.tmp')), [])

    def test_transient_schedule_read_does_not_kill_worker_or_change_authority(self):
        from wake.standalone import _shared_provider_schedule
        path=self.root/'provider-schedule.json'
        self.assertEqual(_shared_provider_schedule(path), {})
        path.write_text(json.dumps({'models': {'fixture': {'retry_at': 10}}}))
        self.assertEqual(_shared_provider_schedule(path), {'fixture': {'retry_at': 10}})
        with patch.object(Path, 'open', side_effect=FileNotFoundError('changed during read')):
            self.assertIsNone(_shared_provider_schedule(path))
        path.write_text('{broken')
        self.assertIsNone(_shared_provider_schedule(path))
        path.write_text('x'*32769)
        self.assertIsNone(_shared_provider_schedule(path))
        self.assertFalse(list(self.root.rglob('*.sqlite')))

    def test_unified_fingerprint_notifies_readers_without_becoming_a_record_head(self):
        site=self.root/'site/current';site.mkdir(parents=True)
        head='snapshot:'+'b'*64
        (site/'head.txt').write_text(head+'\n')
        packet=self.controller.runtime_snapshot()
        self.assertEqual(packet['head'],head)
        self.assertEqual(packet['members'][0]['head'],'a'*64)

    def test_stream_and_head_have_no_execution_effect_and_observer_limit_is_bounded(self):
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(InstallationHTTP, directory=str(self.root)))
        server.controller = self.controller
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        url = f'http://127.0.0.1:{server.server_port}/runtime.events'
        try:
            with urlopen(Request(url, method='HEAD'), timeout=2) as response:
                self.assertEqual(response.status, 200)
            with urlopen(url, timeout=2) as response:
                self.assertIn('text/event-stream', response.headers['Content-Type'])
                line = response.readline().decode()
                self.assertTrue(line.startswith('data: '))
                self.assertEqual(json.loads(line[6:])['research'], 'running')
            # A disconnected stream releases its bounded slot on its next tick.
            self.controller.shutdown.set()
            with patch.object(self.controller.observer_slots, 'acquire', return_value=False):
                with self.assertRaises(HTTPError) as limited:
                    urlopen(url, timeout=2)
                self.assertEqual(limited.exception.code, 503)
                limited.exception.close()
            self.assertEqual(self.controller.workers, {})
            self.assertEqual(self.controller.coordinator.status()['queued'], 0)
        finally:
            self.controller.shutdown.set()
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
