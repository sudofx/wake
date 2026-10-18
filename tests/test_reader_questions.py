"""Reader explanations account for effects without accepting research or transcripts."""
from contextlib import contextmanager
import json
import os
from pathlib import Path
import socket
import stat
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

from wake.authority import open_authoritative_store
from wake.engine import DEFAULTS, Engine
from wake.kernel.generation import GenerationResponse
from wake.kernel.runtime import context_digest, InvocationLifecycle
from wake.kernel.models import Context, SubmissionProvenance
from wake.reader_questions import ReaderQuestions, ReaderService, socket_path, validate_answer
from wake.providers import ProviderCallPaused
from wake.standalone import _reader_admission_paused, _reader_drain_pending
from types import SimpleNamespace


class Gate:
    url = 'fixture://coordinator'
    wait_seconds = 60
    outcome = None

    @contextmanager
    def request(self, model):
        yield True


class ReaderQuestionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = self.root / 'record'
        self.engine = Engine(self.data, dict(DEFAULTS),
                             store=open_authoritative_store(self.data, allow_initialize=True))
        self.addCleanup(self.engine.store.close)
        with self.engine.store.lock():
            self.engine.initialize()
        self.site = self.root / 'site'
        (self.site / 'current').mkdir(parents=True)
        self.prepared = {'system': 'Bounded public evidence', 'prompt': 'private fixture question',
                         'sources': [{'id': 'S1', 'path': 'reader/posts/item.json', 'label': 'Published article',
                                      'collection': 'posts', 'record_id': '100.wake:article'}],
                         'article': {'id': 'article', 'hash': 'a' * 64, 'head': 'public-head'},
                         'metrics': {'context_bytes': 50}, 'warnings': [], 'missing': []}
        self.questions = ReaderQuestions(self.engine, DEFAULTS, self.site, lambda: False)
        self.addCleanup(patch.stopall)
        patch.dict(os.environ, {'GEMINI_API_KEY': 'fixture-secret'}).start()
        patch('wake.reader_questions.prepare_context', return_value=self.prepared).start()
        self.gate = Gate()
        patch('wake.reader_questions.group_provider_gate', return_value=self.gate).start()
        self.generate = patch('wake.reader_questions.GeminiGenerationProvider.generate', return_value=GenerationResponse(
            'google-gemini', 'fixture', json.dumps({'answer': 'private fixture answer [S1]', 'citations': ['S1']}),
            {'usage': {'totalTokenCount': 42, 'private': 'fixture-secret'}})).start()

    def test_answer_uses_one_accounted_effect_without_research_or_transcript_persistence(self):
        before = json.dumps(self.engine.store.load(), sort_keys=True)
        result = self.questions.answer({'article_id': 'article', 'question': 'private fixture question'})
        self.assertTrue(result['ok'])
        self.generate.assert_called_once()
        self.assertEqual(self.questions.attempts, 1)
        self.assertEqual(self.gate.wait_seconds, 10)
        self.assertEqual(result['metrics']['provider_tokens'], {'totalTokenCount': 42})
        self.assertEqual(result['sources'][0]['url'], 'index.html#blog/100.wake%3Aarticle')
        self.assertEqual(json.dumps(self.engine.store.load(), sort_keys=True), before)
        events = self.engine.store.invocation_history()
        self.assertEqual([item['stage'] for item in events],
                         ['requested', 'context_delivered', 'attempt_started', 'proposal_received', 'governed', 'completed'])
        self.assertIsNone(events[-1]['receipt_id'])
        self.assertEqual(events[1]['context_receipt']['scope'],
                         {'kind': 'application', 'application_id': 'wake', 'purpose': 'reader'})
        journal = json.dumps(events)
        for secret in ('private fixture question', 'private fixture answer', 'fixture-secret'):
            self.assertNotIn(secret, journal)
        # Fingerprint the actual generation envelope, including schema/model/tools.
        from dataclasses import asdict
        generation = self.generate.call_args.args[0]
        exact = Context(events[0]['source_revision'], {'generation_request': asdict(generation)}, ())
        self.assertEqual(events[0]['context_digest'], context_digest(exact))
        self.assertEqual(generation.tools, ())

    def test_busy_paused_and_session_limit_never_call_provider(self):
        with self.questions.busy:
            self.assertEqual(self.questions.answer({})['error'], 'busy')
        self.questions.should_pause = lambda: True
        self.assertEqual(self.questions.answer({})['error'], 'paused')
        self.questions.should_pause = lambda: False
        self.questions.attempts = 24
        self.assertEqual(self.questions.answer({})['error'], 'session_limit')
        self.generate.assert_not_called()
        self.assertEqual(self.engine.store.invocation_history(), ())

    def test_reader_can_answer_during_research_without_recovery_interrupting_it(self):
        entered, release = threading.Event(), threading.Event()
        original = self.generate.return_value
        def generate(request):
            entered.set()
            if not release.wait(5):
                raise TimeoutError('fixture did not release provider')
            return original
        self.generate.side_effect = generate
        results = []
        before = self.engine.store.load()
        with self.engine.store.lock():
            worker = threading.Thread(target=lambda: results.append(self.questions.answer({'article_id': 'article'})))
            worker.start()
            try:
                self.assertTrue(entered.wait(5), 'Reader must not require the research turn lock')
                self.engine.recover()
                pending = self.engine.store.record.incomplete_invocations()
                self.assertEqual(len(pending), 1)
                self.assertEqual(self.engine.store.invocation_history()[-1]['stage'], 'attempt_started')
            finally:
                release.set()
                worker.join(5)
        self.assertFalse(worker.is_alive())
        self.assertTrue(results[0]['ok'])
        self.assertEqual(self.engine.store.load(), before)
        self.assertEqual(self.engine.store.invocation_history()[-1]['stage'], 'completed')

    def test_unfinished_managed_invocation_is_recoverable_after_owner_leaves(self):
        record = self.engine.store.record
        with self.assertRaisesRegex(RuntimeError, 'fixture interruption'):
            with InvocationLifecycle.managed(record, self.engine.store.kernel.context(),
                    provenance=SubmissionProvenance('model', 'fixture', 'fixture')) as live:
                self.assertEqual(self.engine.store.recover_invocation_lifecycles(), ())
                raise RuntimeError('fixture interruption')
        self.assertEqual(self.engine.store.recover_invocation_lifecycles(), (live.invocation_id,))
        self.assertEqual(record.invocation_history()[-1]['detail'], 'interrupted')

    def test_bad_citations_are_visible_failures_without_accepting_research(self):
        before = self.engine.store.load()['version']
        self.generate.return_value = GenerationResponse('fixture', 'fixture', json.dumps(
            {'answer': 'unsupported [S999]', 'citations': ['S1']}))
        result = self.questions.answer({'article_id': 'article'})
        self.assertEqual(result['error'], 'invalid_provider_answer')
        self.assertEqual(self.engine.store.load()['version'], before)
        self.assertEqual(self.engine.store.invocation_history()[-1]['detail'], 'invalid_reader_answer')

    def test_pause_at_gate_prevents_effect_without_mislabeling_provider_failure(self):
        @contextmanager
        def paused(model):
            raise ProviderCallPaused('private pause detail')
            yield
        self.gate.request = paused
        self.assertFalse(self.questions.answer({'article_id': 'article'})['ok'])
        self.generate.assert_not_called()
        event = self.engine.store.invocation_history()[-1]
        self.assertEqual(event['detail'], 'ProviderCallPaused')
        self.assertIsNone(event['outcome'])

    def test_application_access_blocks_disabled_and_revoked_effects(self):
        record = self.engine.store.record
        record.set_application_access(False, actor='fixture')
        self.assertEqual(self.questions.answer({})['error'], 'access_blocked')
        self.assertEqual(record.invocation_history(), ())
        record.set_application_access(True, actor='fixture')
        def revoke(*args):
            record.set_application_access(False, actor='fixture')
            return self.prepared
        with patch('wake.reader_questions.prepare_context', side_effect=revoke):
            self.assertFalse(self.questions.answer({})['ok'])
        self.generate.assert_not_called()
        self.assertEqual(record.invocation_history()[-1]['outcome'], 'effect_barrier_failure')

    def test_access_revoked_while_waiting_for_gate_prevents_provider_effect(self):
        @contextmanager
        def revoke(model):
            self.engine.store.record.set_application_access(False, actor='fixture')
            yield True
        self.gate.request = revoke
        self.assertFalse(self.questions.answer({})['ok'])
        self.generate.assert_not_called()
        self.assertEqual(self.engine.store.invocation_history()[-1]['outcome'], 'effect_barrier_failure')

    def test_service_drains_active_handler_before_close_returns(self):
        entered, release, closed = threading.Event(), threading.Event(), threading.Event()
        class SlowQuestions:
            def answer(self, request):
                entered.set()
                release.wait(5)
                return {'ok': True}
        service = ReaderService(self.data, SlowQuestions())
        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            client.connect(str(socket_path(self.data)))
            client.sendall(b'{}\n')
            self.assertTrue(entered.wait(2))
            self.assertTrue(service.active)
            runtime = SimpleNamespace(runtime_status={}, control_ack='old-command')
            for mode, reset_id in (('paused', None), ('stopped', None), ('running', 'new-reset')):
                self.assertTrue(_reader_drain_pending(service, runtime, mode, reset_id, None))
                self.assertEqual(runtime.runtime_status['state'], 'draining')
                self.assertNotIn('control_ack', runtime.runtime_status)
                self.assertEqual(runtime.control_ack, 'old-command')
            closer = threading.Thread(target=lambda: (service.close(), closed.set()))
            closer.start()
            self.assertFalse(closed.wait(.1))
            release.set()
            self.assertTrue(closed.wait(2))
            closer.join()
            self.assertFalse(service.active)
            self.assertFalse(_reader_drain_pending(service, runtime, 'stopped', None, None))
        finally:
            release.set()
            client.close()

    def test_pending_reset_blocks_reader_admission_before_acknowledgement(self):
        control = self.data / '.wake-runner-control.json'
        control.write_text(json.dumps({'research': 'running', 'reset_id': 'new'}))
        stop = threading.Event()
        self.assertTrue(_reader_admission_paused(self.data, 'running', stop, 'old'))
        self.assertFalse(_reader_admission_paused(self.data, 'running', stop, 'new'))

    def test_bridge_uses_private_socket_and_existing_worker(self):
        service = ReaderService(self.data, self.questions)
        try:
            self.assertEqual(stat.S_IMODE(socket_path(self.data).stat().st_mode), 0o600)
            self.assertEqual(socket_path(self.data).parent, Path('/tmp'))
            result = subprocess.run([sys.executable, '-m', 'wake.reader_questions', 'bridge', '--data', str(self.data)],
                                    input=json.dumps({'article_id': 'article'}), capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0)
            self.assertTrue(json.loads(result.stdout)['ok'])
            self.assertNotIn('private fixture question', result.stderr)
        finally:
            service.close()
        self.assertFalse(socket_path(self.data).exists())


if __name__ == '__main__':
    unittest.main()
