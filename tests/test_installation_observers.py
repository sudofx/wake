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
