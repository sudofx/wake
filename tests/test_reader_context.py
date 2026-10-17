"""Deterministic bounded reader context; never providers or operator records."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.reader_context import (prepare_context, article_descriptor, SOURCE_MAX_BYTES,
                                 CONTEXT_MAX_BYTES, CONTEXT_MAX_CHARS, MAX_LINKED_RECORDS)
from wake.reader_transport import record_path


class ReaderContextTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.head = 'a' * 64
        self.post = {'id': 'article', 'title': 'A bounded result', 'lede': 'What changed?',
                     'body': 'A recorded result remains provisional.', 'lens': '',
                     'evidence': ['e1'], 'notebooks': [], 'created_version': 3}
        self.write('posts', self.post)
        self.write('evidence', {'id': 'e1', 'source': 'https://example.org', 'content': 'A measured value.'})
        self.request = {'article_id': 'article', 'question': 'What does provisional mean?'}

    def write(self, collection, item, head=None):
        path = self.root / record_path(collection, item['id'])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'head': head or self.head, 'collection': collection, 'item': item}))
        return path

    def test_exact_public_records_and_repeatable_prompt_without_archive(self):
        original = Path.open
        reads = []
        def opened(path, *args, **kwargs):
            reads.append(str(path))
            return original(path, *args, **kwargs)
        with patch.object(Path, 'open', opened):
            first = prepare_context(self.root, self.request)
            second = prepare_context(self.root, self.request)
        self.assertEqual(first, second)
        self.assertEqual([row['record_id'] for row in first['sources']], ['article', 'e1'])
        self.assertTrue(all('reader-records/' in value for value in reads))
        self.assertLessEqual(first['metrics']['context_bytes'], CONTEXT_MAX_BYTES)
        self.assertLessEqual(first['metrics']['context_chars'], CONTEXT_MAX_CHARS)

    def test_conditions_keep_full_turns_or_recoverable_relevant_excerpts(self):
        history = [{'id': 'one', 'article_id': 'article', 'question': 'Explain the result',
                    'answer': 'x ' * 1000 + 'provisional means uncertainty remains.'},
                   {'id': 'other', 'article_id': 'different', 'question': 'Unrelated?', 'answer': 'Other.'}]
        results = {condition: prepare_context(self.root, {**self.request, 'condition': condition, 'history': history})
                   for condition in ('A', 'B', 'C')}
        self.assertEqual(results['A']['context']['history'], [])
        self.assertEqual(results['B']['context']['history'][0]['answer'], history[0]['answer'])
        compressed = results['C']['context']['history'][0]
        self.assertIn('provisional', compressed['answer'])
        self.assertTrue(compressed['excerpted'])
        self.assertEqual(compressed['id'], 'one')
        self.assertEqual(compressed['original_index'], 0)
        self.assertEqual(len(compressed['original_hash']), 64)
        self.assertEqual(compressed['answer'], history[0]['answer'][compressed['answer_excerpt_start']:compressed['answer_excerpt_end']])
        self.assertLess(results['C']['metrics']['context_bytes'], results['B']['metrics']['context_bytes'])

    def test_exposure_is_never_understanding_and_self_report_is_hash_scoped(self):
        descriptor = article_descriptor(self.post, self.head)
        previous = {'id': 'article', 'hash': descriptor['hash'], 'exposure': {'opened': True}}
        result = prepare_context(self.root, {**self.request, 'previous_article': previous})
        self.assertEqual(result['context']['reader_state']['understanding'], 'unknown')
        previous['self_report'] = 'understood'
        result = prepare_context(self.root, {**self.request, 'previous_article': previous})
        self.assertIn('not validated', result['context']['reader_state']['understanding'])
        previous['hash'] = 'b' * 64
        result = prepare_context(self.root, {**self.request, 'previous_article': previous})
        self.assertEqual(result['context']['reader_state']['understanding'], 'unknown')
        self.assertIn('prior bytes unavailable', result['context']['revision']['comparison'])

    def test_article_content_hash_survives_new_snapshot_and_rejects_stale_question(self):
        descriptor = article_descriptor(self.post, self.head)
        self.assertEqual(descriptor['hash'], article_descriptor({**self.post, 'status': 'superseded'}, 'c' * 64)['hash'])
        self.write('posts', {**self.post, 'body': 'Changed public text.'})
        with self.assertRaisesRegex(ValueError, 'reload'):
            prepare_context(self.root, {**self.request, 'expected_article_hash': descriptor['hash']})

    def test_verified_linked_revision_supports_actual_text_comparison(self):
        self.write('posts', {**self.post, 'supersedes': 'old'})
        self.write('posts', {**self.post, 'id': 'old', 'body': 'Previously described as certain.'})
        result = prepare_context(self.root, {**self.request, 'prior_article_hash': 'b' * 64})
        self.assertIn('Linked published revision', result['context']['revision']['comparison'])
        self.assertEqual(result['context']['records'][0]['item']['body'], 'Previously described as certain.')
        self.assertIn('not established as the reader', result['context']['revision']['comparison'])
        prior = article_descriptor({**self.post, 'id': 'old', 'body': 'Previously described as certain.'}, self.head)
        result = prepare_context(self.root, {**self.request, 'prior_article_hash': prior['hash']})
        self.assertIn('matches the previous content hash', result['context']['revision']['comparison'])

    def test_different_article_exposure_is_not_current_version_or_understanding(self):
        result = prepare_context(self.root, {**self.request, 'previous_article': {
            'id': 'different', 'hash': 'b' * 64, 'exposure': {'opened': True}, 'self_report': 'understood'}})
        self.assertFalse(result['metrics']['article_changed'])
        self.assertEqual(result['context']['reader_state']['exposure'], {'opened': False})
        self.assertEqual(result['context']['reader_state']['understanding'], 'unknown')

    def test_missing_and_mismatched_sources_are_explicit(self):
        self.write('posts', {**self.post, 'evidence': ['missing', 'e1']})
        self.write('evidence', {'id': 'e1', 'content': 'Different generation'}, 'b' * 64)
        result = prepare_context(self.root, self.request)
        self.assertEqual(len(result['missing']), 2)
        self.assertEqual(len(result['sources']), 1)
        self.assertEqual(result['context']['missing'], result['missing'])

    def test_group_editorial_refs_resolve_exact_qualified_notebook_by_question(self):
        references = []
        members = ['100.wake', '101.wake', '102.wake', '103.wake', '200.wake', '201.wake']
        for index, member in enumerate(members):
            identifier = 'n' + str(index)
            references.append({'member': member, 'notebook_id': identifier,
                'record_url': f'/nodes/{member}/index.html#projects/notebook:{identifier}',
                'head': 'c' * 64, 'revision': index,
                'title': 'Provisional qualifications' if index == 5 else 'Other results'})
            self.write('notebooks', {'id': member + '::' + identifier, 'title': 'Notebook ' + str(index), 'summary': 'Exact public notebook.'})
        article = {**self.post, 'id': '100.wake::article', 'origin': {'node': '100.wake'},
                   'evidence': [], 'editorial_references': [references]}
        self.write('posts', article)
        result = prepare_context(self.root, {**self.request, 'article_id': article['id']})
        self.assertEqual(result['sources'][1]['record_id'], '201.wake::n5')
        self.assertEqual(result['sources'][1]['collection'], 'notebooks')
        self.assertEqual(result['context']['records'][0]['reference_provenance']['captured_head'], 'c' * 64)
        self.assertEqual(len(result['sources']), MAX_LINKED_RECORDS + 1)
        self.assertTrue(any('limit' in warning for warning in result['warnings']))

    def test_group_reference_rejects_unknown_member_or_mismatched_route(self):
        article = {**self.post, 'id': '100.wake::article', 'origin': {'node': '100.wake'}, 'evidence': [],
                   'editorial_references': [[
                       {'member': 'outside', 'notebook_id': 'n', 'record_url': '/nodes/outside/index.html#projects/notebook:n'},
                       {'member': '100.wake', 'notebook_id': 'n', 'record_url': '/nodes/101.wake/index.html#projects/notebook:n'}]]}
        self.write('posts', article)
        result = prepare_context(self.root, {**self.request, 'article_id': article['id']})
        self.assertEqual(len(result['sources']), 1)
        self.assertEqual(result['missing'], [])

    def test_source_read_size_and_symlink_escape_fail_closed(self):
        path = self.root / record_path('posts', 'article')
        path.write_bytes(b' ' * (SOURCE_MAX_BYTES + 1))
        with self.assertRaisesRegex(ValueError, 'unavailable'):
            prepare_context(self.root, self.request)
        path.unlink()
        path.symlink_to(Path('/etc/hosts'))
        with self.assertRaisesRegex(ValueError, 'unavailable'):
            prepare_context(self.root, self.request)

    def test_unicode_context_and_link_count_remain_bounded(self):
        ids = ['e' + str(i) for i in range(8)]
        self.write('posts', {**self.post, 'body': '界' * 12000, 'evidence': ids})
        for identifier in ids:
            self.write('evidence', {'id': identifier, 'content': 'One direct record.'})
        result = prepare_context(self.root, self.request)
        self.assertLessEqual(result['metrics']['context_bytes'], CONTEXT_MAX_BYTES)
        self.assertLessEqual(result['metrics']['source_records'], MAX_LINKED_RECORDS + 1)
        self.assertTrue(result['warnings'])
        self.assertNotEqual(result['context']['current_article']['body'], '界' * 12000)

    def test_oversized_or_malformed_browser_inputs_are_rejected(self):
        for extra in ({'question': 'x' * 2001}, {'condition': 'D'}, {'history': [{}]},
                      {'previous_article': {'id': 'article', 'self_report': 'measured comprehension'}},
                      {'history': [{'article_id': 'article', 'question': '', 'answer': 'x' * 6001}]}):
            with self.subTest(extra=str(extra)[:100]), self.assertRaises(ValueError):
                prepare_context(self.root, {**self.request, **extra})


if __name__ == '__main__':
    unittest.main()
