"""First-run publication, replay and hidden-file privacy contracts."""
import os
import subprocess
import sys
import threading
import urllib.request
import urllib.error
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from support import charter_settings
from wake.authority import open_authoritative_store
from wake.engine import Engine
from wake.introduction import POST_ID, pending
from wake.providers import Fixture, TransientProviderError
from wake.report import PublicSnapshotHandler


class InitializationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root / "data", charter_settings("Explore small useful projects."),
                             store=open_authoritative_store(self.root / "data", allow_initialize=True))

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def test_first_wake_publishes_canonical_introduction_and_replay_is_idempotent(self):
        first = self.engine.run(Fixture())
        self.assertEqual(first["status"], "accepted")
        state = self.engine.store.load()
        self.assertIn(POST_ID, state["posts"])
        self.assertEqual(state["posts"][POST_ID]["created_version"], 1)
        body = state["posts"][POST_ID]["body"]
        for phrase in ("infrastructure", "Bob", "Console", "Uncertainty", "Corrections", "hidden", "Summary"):
            self.assertIn(phrase, body)
        self.assertFalse(pending(state))
        for _ in range(3):
            self.engine.run(Fixture())
        self.assertEqual([p for p in self.engine.store.load()["posts"] if p == POST_ID], [POST_ID])
        self.assertEqual(self.engine.store.audit()[0], self.engine.store.load())

    def test_solo_research_makes_only_its_requested_provider_calls(self):
        class CountingFixture(Fixture):
            calls = 0
            def propose(self, request):
                self.calls += 1
                return super().propose(request)
        provider = CountingFixture()
        for _ in range(16):
            self.engine.run(provider)
        self.assertEqual(provider.calls, 16)
        self.assertEqual(self.engine.store.audit()[0], self.engine.store.load())

    def test_provider_failure_is_retained_and_local_publication_is_not_a_finding(self):
        class Failure:
            name, model, charged = "fixture", "unavailable", False
            def propose(self, request):
                raise TransientProviderError("Temporary outage")
        result = self.engine.run(Failure())
        self.assertEqual(result["status"], "deferred")
        self.assertEqual(result["initial_publication"]["status"], "accepted")
        state = self.engine.store.load()
        self.assertEqual(state["projects"], {})
        self.assertEqual(state["notebooks"], {})
        self.assertEqual(state["invocations"][result["id"]]["status"], "deferred")

    def test_failed_publication_stays_pending_then_recovers_without_duplicates(self):
        self.engine.initialize()
        from wake.introduction import Editorial
        with patch('wake.introduction.action', side_effect=lambda state: {"type": "forbidden"}):
            with self.engine.store.lock():
                result = self.engine._run_invocation(Editorial(self.engine.store.load()))
        self.assertEqual(result["status"], "rejected")
        self.assertTrue(pending(self.engine.store.load()))
        self.engine.run(Fixture())
        self.assertFalse(pending(self.engine.store.load()))

    def test_interrupted_first_commit_recovers_with_one_introduction(self):
        script = """from support import charter_settings
from wake.authority import open_authoritative_store
from wake.engine import Engine
from wake.providers import Fixture
import sys
e=Engine(sys.argv[1],charter_settings('Explore projects'),store=open_authoritative_store(sys.argv[1],allow_initialize=True))
e.run(Fixture(),crash_at='during-commit')
"""
        directory = self.root / 'interrupted'
        result = subprocess.run([sys.executable, '-c', script, str(directory)],
                                env={**os.environ, 'PYTHONPATH': str(Path(__file__).parent.resolve())}, capture_output=True)
        self.assertEqual(result.returncode, 86)
        engine = Engine(directory, charter_settings('Explore projects'),
                        store=open_authoritative_store(directory))
        try:
            engine.run(Fixture())
            self.assertEqual(set(engine.store.load()['posts']), {POST_ID})
            self.assertEqual(engine.store.audit()[0], engine.store.load())
        finally:
            engine.store.close()

    def test_public_server_blocks_get_and_head_even_if_private_file_is_in_root(self):
        (self.root / '.private.md').write_text('private-http-canary')
        class Quiet(PublicSnapshotHandler):
            def log_message(self, *args):
                pass
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(self.root)))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for method in ('GET', 'HEAD'):
                for name in ('.private.md', '.private-state.json', '.priv%61te.md'):
                    request = urllib.request.Request(f'http://127.0.0.1:{server.server_port}/{name}', method=method)
                    with self.assertRaises(urllib.error.HTTPError) as caught:
                        urllib.request.urlopen(request)
                    self.assertEqual(caught.exception.code, 404)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()
