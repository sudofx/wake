"""Opt-in offline Chrome acceptance through the real export/HTTP/invocation path.

Run with PLAYWRIGHT_MODULE pointing at an installed Playwright module and optional
CHROME_EXECUTABLE. All records, exports, generation and credentials are fixtures.
No Docker process, live provider or hosted artifact is consulted.
"""
from contextlib import contextmanager
from copy import deepcopy
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import threading
import unittest
from unittest.mock import patch

from wake.authority import open_authoritative_store
from wake.engine import DEFAULTS, Engine
from wake.kernel.generation import GenerationResponse
from wake.reader_preview import ReaderPreview
from wake.reader_questions import ReaderQuestions
from wake.report import export


class FixtureGate:
    url = 'fixture://offline-reader-integration'
    wait_seconds = 1
    outcome = None

    @contextmanager
    def request(self, model):
        yield True


@unittest.skipUnless(shutil.which('node') and os.environ.get('PLAYWRIGHT_MODULE'),
                     'Opt-in browser acceptance requires Node and PLAYWRIGHT_MODULE')
class ReaderBrowserIntegrationTests(unittest.TestCase):
    def test_generated_reader_reaches_native_journal_without_research_or_transcript_mutation(self):
        with tempfile.TemporaryDirectory(prefix='wake-offline-reader-browser-') as temporary:
            root = Path(temporary)
            record = root / 'record'
            engine = Engine(record, dict(DEFAULTS),
                            store=open_authoritative_store(record, allow_initialize=True))
            self.addCleanup(engine.store.close)
            with engine.store.lock():
                engine.initialize()
            original_state = deepcopy(engine.store.load())
            state = deepcopy(original_state)
            state.update(projects={}, notebooks={}, research={})
            post = {'id': 'offline-integration-post', 'title': 'Synthetic reader integration',
                    'lede': 'A synthetic fixture for browser acceptance, not a research finding.',
                    'body': 'The synthetic test recorded twelve completed tasks. Its cause remains unknown.\n\nSummary\n\nThis fixture supports a count, not a causal conclusion.',
                    'evidence': ['offline-integration-source'], 'notebooks': [],
                    'created_version': 1, 'created_by': 'offline-publication', 'status': 'published',
                    'published_at': '2026-10-17T20:00:00Z'}
            state['posts'] = {post['id']: post}
            state['evidence'] = {'offline-integration-source': {
                'id': 'offline-integration-source', 'source': 'https://example.org/offline-fixture',
                'content': 'Synthetic fixture: twelve completed tasks; cause unknown.'}}
            state['invocations'] = {'offline-publication': {'id': 'offline-publication',
                'time': '2026-10-17T20:00:00Z', 'status': 'accepted', 'provider': 'fixture'}}
            installation = root / 'installation'
            site = installation / 'site' / 'current'
            export(destination=site, projection={'state': state, 'head': 'a' * 64,
                                               'events': [], 'metrics': {'storage': {'event_count': 0}}},
                   browser_only=True, standalone=True)
            (installation / 'installation-id.json').write_text(json.dumps({'id': 'offline-reader-integration'}))
            before_export = {str(path.relative_to(site)): path.read_bytes()
                             for path in site.rglob('*') if path.is_file()}
            questions = ReaderQuestions(engine, DEFAULTS, installation / 'site', lambda: False)
            packets = []

            def bridge(packet):
                packets.append(packet)
                return questions.answer(packet)

            with patch.dict(os.environ, {'GEMINI_API_KEY': 'OFFLINE-FIXTURE-SECRET'}), \
                    patch('wake.reader_questions.group_provider_gate', return_value=FixtureGate()), \
                    patch('wake.reader_questions.GeminiGenerationProvider.generate', return_value=GenerationResponse(
                        'google-gemini', 'fixture', json.dumps({
                            'answer': 'OFFLINE-INTEGRATION-ANSWER: The synthetic count is twelve; it does not establish a cause. [S1]',
                            'citations': ['S1']}), {'usage': {'totalTokenCount': 77}})) as generate:
                server = ReaderPreview(installation, port=0, bridge=bridge)
                worker = threading.Thread(target=server.serve_forever, daemon=True)
                worker.start()
                try:
                    result = subprocess.run(['node', str(Path(__file__).parent / 'browser/ask-bob-export.cjs'),
                                             server.origin], capture_output=True, text=True, timeout=60)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    browser = json.loads(result.stdout.strip().splitlines()[-1])
                    self.assertEqual(browser['result'], 'PASS')
                    print(result.stdout.strip())
                finally:
                    server.shutdown()
                    server.server_close()
                    worker.join(timeout=5)
                generate.assert_called_once()
                self.assertIn('OFFLINE-INTEGRATION-QUESTION', generate.call_args.args[0].prompt)
                self.assertIn('offline-integration-source', generate.call_args.args[0].prompt)
            self.assertEqual(len(packets), 1)
            self.assertEqual(packets[0]['expected_article_hash'], browser['article_hash'])
            self.assertIsNone(packets[0]['previous_article']['self_report'])
            self.assertEqual(packets[0]['condition'], 'C')
            self.assertEqual(engine.store.load(), original_state)
            events = engine.store.invocation_history()
            self.assertEqual([event['stage'] for event in events],
                             ['requested', 'context_delivered', 'attempt_started',
                              'proposal_received', 'governed', 'completed'])
            self.assertIsNone(events[-1]['receipt_id'])
            encoded = json.dumps(events)
            for private in ('OFFLINE-INTEGRATION-QUESTION', 'OFFLINE-INTEGRATION-ANSWER', 'OFFLINE-FIXTURE-SECRET'):
                self.assertNotIn(private, encoded)
            after_export = {str(path.relative_to(site)): path.read_bytes()
                            for path in site.rglob('*') if path.is_file()}
            self.assertEqual(after_export, before_export)
