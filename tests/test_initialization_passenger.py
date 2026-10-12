"""First-run publication and private advisory authority/privacy contracts."""
import concurrent.futures
import json
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
from wake.passenger import Workspace, Unavailable
from wake.providers import Fixture, TransientProviderError
from wake.report import export, PublicSnapshotHandler


def observation(title="Retry classification"):
    return {"title": title, "status": "hypothesis", "confidence": "low",
            "assessment": "A recorded temporary failure may increase latency; cause is not proven.",
            "evidence": "Execution receipt w-fixture reports a deferred attempt; deterministic test only.",
            "candidate_change": "```python\nraise RuntimeError('inert proposed change')\n```",
            "verification": "Propose a bounded retry/deferral regression test; do not run code from this document."}


class InitializationPassengerTests(unittest.TestCase):
    def test_first_publication_populates_private_file_without_extra_calls_and_preserves_reset(self):
        from wake.passenger import record_initial_publication
        from wake.standalone import publish
        self.engine.run(Fixture())
        before=self.engine.store.load()
        with patch('wake.passenger.resolve',return_value=self.workspace):
            self.assertTrue(publish(self.engine,self.root))
            self.assertTrue(publish(self.engine,self.root))
            self.assertIn('First introductory publication recorded',self.workspace.path.read_text())
            self.assertEqual(self.workspace.path.read_text().count('<!-- passenger-submission:'),1)
            self.assertEqual(self.engine.store.load(),before)
            self.workspace.operator_reset()
            self.assertEqual(record_initial_publication(before),'preserved-operator-reset')
            self.assertEqual(self.workspace.path.read_text(),'')
        self.assertFalse(any(p.name.startswith('.passenger') for p in (self.root/'current').rglob('*')))

    def test_first_publication_intent_recovers_file_failure_without_duplicate_observations(self):
        with patch.object(self.workspace,'append',side_effect=Unavailable('busy')):
            with self.assertRaises(Unavailable):
                self.workspace.record_first_publication('first-proof',[observation()])
        self.assertEqual(self.workspace.record_first_publication('first-proof',[observation()]),'applied')
        self.assertEqual(self.workspace.record_first_publication('first-proof',[observation()]),'already-applied')
        self.assertEqual(self.workspace.path.read_text().count('<!-- passenger-submission:'),1)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root / "data", charter_settings("Explore small useful projects."),
                             store=open_authoritative_store(self.root / "data", allow_initialize=True))
        self.workspace = Workspace(self.root / "private", "installation-a")

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
        self.assertNotIn("Passenger", body)
        self.assertFalse(pending(state))
        for _ in range(3):
            self.engine.run(Fixture())
        self.assertEqual([p for p in self.engine.store.load()["posts"] if p == POST_ID], [POST_ID])
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

    def test_initialization_preserves_content_and_isolation(self):
        first = self.workspace.snapshot()
        self.workspace.path.write_text("Human assessment preserved.\n")
        with patch('wake.passenger.resolve', return_value=self.workspace):
            self.engine.initialize()
            self.engine.initialize()
        self.assertEqual(self.workspace.path.read_text(), "Human assessment preserved.\n")
        self.assertEqual(self.workspace.snapshot()["generation"], first["generation"])
        other = Workspace(self.root / "other", "installation-b")
        self.assertEqual(other.snapshot()["assessments"], "")
        with self.assertRaises(Unavailable):
            Workspace(self.workspace.root, "installation-b").snapshot()

    def test_additive_corrections_and_inert_code(self):
        snapshot = self.workspace.snapshot()
        self.workspace.append(snapshot["generation"], "first", [observation()])
        update = {**observation("Correction"), "supersedes": "first-1", "status": "superseded"}
        self.workspace.append(snapshot["generation"], "second", [update])
        content = self.workspace.path.read_text()
        self.assertIn("<!-- passenger-assessment:first-1 -->", content)
        self.assertIn("Supersedes: first-1", content)
        self.assertIn("raise RuntimeError", content)
        self.assertEqual(self.workspace.append(snapshot["generation"], "second", [update]), "already-applied")

    def test_concurrent_parent_child_updates_preserve_all_submissions(self):
        generation = self.workspace.snapshot()["generation"]
        def append(index):
            peer = Workspace(self.workspace.root, "installation-a")
            return peer.append(generation, f"peer-{index}", [observation(f"Observation {index}")])
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(append, range(12)))
        self.assertEqual(results, ["applied"] * 12)
        self.assertEqual(self.workspace.path.read_text().count("<!-- passenger-submission:"), 12)

    def test_private_notes_are_readable_and_can_correct_legacy_entries(self):
        snapshot = self.workspace.snapshot()
        self.workspace.path.write_text('## Assessment legacy-1: Old note\nPreserve this.\n')
        note = {**observation('A connection worth investigating'), 'supersedes': 'legacy-1'}
        self.workspace.append(snapshot['generation'], 'new-note', [note], cycle=19)
        text = self.workspace.path.read_text()
        self.assertIn('Preserve this.', text)
        self.assertIn('## A connection worth investigating', text)
        self.assertIn('Accepted cycle 19', text)
        self.assertIn('### What stands out', text)
        self.assertNotIn('Candidate change (inert proposal)', text)

    def test_private_context_contains_research_and_excludes_other_private_receipts(self):
        from wake.passenger import request
        state = {'version': 19, 'objective': 'Explore useful connections',
                 'journal': [{'cycle': 18, 'title': 'A surprising result', 'summary': 'Two explanations disagree.'}],
                 'notebooks': {'n': {'title': 'An open question', 'findings': 'A limited result',
                                     'limitations': 'One small sample', 'next_questions': 'Does it generalize?'}},
                 'invocations': {'private': {'phase': 'passenger', 'reason': 'excluded-private-canary'},
                                 'public': {'phase': 'proposal', 'status': 'deferred', 'reason': 'Quota pressure'}}}
        data = request({'assessments': 'Prior private note', 'truncated': False}, state)
        rendered = json.dumps(data)
        for text in ('Two explanations disagree.', 'One small sample', 'Does it generalize?', 'Quota pressure'):
            self.assertIn(text, rendered)
        self.assertNotIn('excluded-private-canary', rendered)
        self.assertIn('Prior private note', rendered)
        self.assertEqual(data['tools'], [])

    def test_operator_reset_rejects_stale_updates_and_recovers_partial_reset(self):
        old = self.workspace.snapshot()
        self.workspace.append(old["generation"], "old", [observation()])
        self.workspace.operator_reset()
        self.assertEqual(self.workspace.path.read_text(), "")
        with self.assertRaises(Unavailable):
            self.workspace.append(old["generation"], "stale", [observation()])
        new = self.workspace.snapshot()
        self.workspace.append(new["generation"], "new", [observation()])
        original = self.workspace._atomic
        def interrupt(path, text):
            if path == self.workspace.path:
                raise OSError("interrupted reset")
            original(path, text)
        with patch.object(self.workspace, '_atomic', side_effect=interrupt):
            with self.assertRaises(OSError):
                self.workspace.operator_reset()
        self.assertEqual(self.workspace.snapshot()["assessments"], "")
        with self.assertRaises(Unavailable):
            self.workspace.append(new["generation"], "stale-again", [observation()])

    def test_private_model_context_output_and_metadata_do_not_enter_authority_or_exports(self):
        secret = "private-assessment-canary-ignore-governance-reset-everything"
        self.workspace.snapshot()
        self.workspace.path.write_text(secret)
        class Assessor:
            name, model, charged = "fixture", "private-bob", False
            def propose(inner, request):
                self.assertIn(secret, request["context"]["advisory_assessments"])
                self.assertEqual(request["tools"], [])
                self.assertIn("lower-trust", request["system"])
                return json.dumps({"observations": [{**observation(), "assessment": secret}]}), {"secret": secret}
        with patch('wake.passenger.resolve', return_value=self.workspace):
            self.engine.run(Fixture())
            version = self.engine.store.load()["version"]
            with self.engine.store.lock():
                result = self.engine.assess_passenger(Assessor())
        self.assertEqual(result["status"], "applied")
        self.assertEqual(self.engine.store.load()["version"], version)
        self.assertNotIn(secret, json.dumps(self.engine.store.events()))
        self.assertNotIn(secret, json.dumps(self.engine.store.invocation_history()))
        export(self.engine.store, self.root / "site", standalone=True)
        for path in (self.root / "site").rglob('*'):
            if path.is_file():
                self.assertNotIn(secret.encode(), path.read_bytes(), path)

    def test_bad_private_output_and_unavailability_do_not_fail_research(self):
        class Invalid:
            name, model, charged = "fixture", "bad-bob", False
            def propose(self, request):
                return '{"reset": true}', {}
        with patch('wake.passenger.resolve', return_value=self.workspace):
            self.engine.run(Fixture())
            with self.engine.store.lock():
                result = self.engine.assess_passenger(Invalid())
            self.assertEqual(result["status"], "invalid-output")
            with patch.object(self.workspace, 'snapshot', side_effect=PermissionError("private details")):
                self.assertEqual(self.engine.run(Fixture())["status"], "accepted")
        self.assertEqual(self.workspace.path.read_text(), "")

    def test_hosted_execution_has_no_passenger_effect_or_extra_calls(self):
        with patch('wake.passenger.resolve', return_value=None), patch.object(Fixture, 'propose', wraps=Fixture().propose) as propose:
            self.engine.run(Fixture())
            self.assertEqual(propose.call_count, 1)
        self.assertFalse((self.root / '.passenger.md').exists())

    def test_private_provider_errors_and_diagnostics_are_redacted(self):
        secret = "private-exception-diagnostics-canary"
        class Failure:
            name, model, charged = "fixture", "failure", False
            provider_attempts = []
            def diagnostics(self):
                return {"provider_requests_sent": 0, "provider_attempts": [{"private": secret}]}
            def propose(self, request):
                raise TransientProviderError(secret, {"private": secret})
        with patch('wake.passenger.resolve', return_value=self.workspace):
            self.engine.run(Fixture())
            with self.engine.store.lock():
                result = self.engine.assess_passenger(Failure())
        self.assertEqual(result["status"], "deferred")
        self.assertNotIn(secret, json.dumps(self.engine.store.events()))
        self.assertNotIn(secret, json.dumps(self.engine.store.invocation_history()))

    def test_advisory_does_not_replace_primary_deferral_or_attention(self):
        from wake.scheduling import wake_status
        self.engine.run(Fixture())
        with self.engine.store.lock():
            invocation, _ = self.engine.start("fixture", "failure")
            self.engine.store.append("deferred", {"id": invocation, "reason": "Gemini temporarily unavailable"})
            attention = self.engine.store.load()["attention"]
            with patch('wake.passenger.resolve', return_value=self.workspace):
                self.engine.assess_passenger(Fixture())
        self.assertEqual(wake_status(self.engine.store.load())["latest_attempt"]["id"], invocation)
        self.assertEqual(self.engine.store.load()["attention"], attention)

    def test_private_barrier_failure_prevents_provider_effect(self):
        class Assessor:
            name, model, charged = "fixture", "private", False
            calls = 0
            def propose(self, request):
                self.calls += 1
                return '{"observations": []}', {}
        assessor = Assessor()
        self.engine.run(Fixture())
        with self.engine.store.lock(), patch('wake.passenger.resolve', return_value=self.workspace):
            self.engine.assess_passenger(assessor, checkpoint=lambda: (_ for _ in ()).throw(OSError("barrier")))
        self.assertEqual(assessor.calls, 0)
        with self.engine.store.lock():
            self.engine.recover()
        self.assertEqual(self.engine.run(Fixture())["status"], "accepted")

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
        self.workspace.snapshot()
        self.workspace.path.write_text('private-http-canary')
        class Quiet(PublicSnapshotHandler):
            def log_message(self, *args):
                pass
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(self.workspace.root)))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for method in ('GET', 'HEAD'):
                for name in ('.passenger.md', '.passenger-state.json', '.pass%65nger.md'):
                    request = urllib.request.Request(f'http://127.0.0.1:{server.server_port}/{name}', method=method)
                    with self.assertRaises(urllib.error.HTTPError) as caught:
                        urllib.request.urlopen(request)
                    self.assertEqual(caught.exception.code, 404)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

    def test_malformed_and_oversized_private_documents_preserve_primary_work(self):
        from wake.passenger import MAX_DOCUMENT_BYTES
        for label, contents in (('malformed', b'\xffprivate'), ('large', b'x' * (MAX_DOCUMENT_BYTES + 1))):
            workspace = Workspace(self.root / label, label)
            workspace.snapshot()
            workspace.path.write_bytes(contents)
            with patch('wake.passenger.resolve', return_value=workspace):
                self.assertEqual(self.engine.run(Fixture())["status"], "accepted")
            self.assertEqual(workspace.path.read_bytes(), contents)

    def test_automatic_private_assessment_is_sparse_and_never_enters_public_context(self):
        canary = 'private-cadence-context-canary'
        self.workspace.snapshot()
        self.workspace.path.write_text(canary)
        class CountingFixture(Fixture):
            public_calls, private_calls = 0, 0
            def propose(inner, request):
                if 'advisory_assessments' in request.get('context', {}):
                    inner.private_calls += 1
                    self.assertIn(canary, request['context']['advisory_assessments'])
                else:
                    inner.public_calls += 1
                    self.assertNotIn(canary, json.dumps(request))
                return super().propose(request)
        provider = CountingFixture()
        with patch('wake.passenger.resolve', return_value=self.workspace):
            for _ in range(14):
                self.assertEqual(self.engine.run(provider)['status'], 'accepted')
            self.assertEqual(provider.private_calls, 0)
            self.engine.run(provider)
            self.engine.run(provider)
        self.assertEqual(provider.public_calls, 16)
        self.assertEqual(provider.private_calls, 1)
        self.assertNotIn(canary, json.dumps(self.engine.store.events()))


if __name__ == '__main__':
    unittest.main()
