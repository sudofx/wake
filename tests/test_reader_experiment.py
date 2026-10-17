import copy
import json
from pathlib import Path
import tempfile
import unittest

from wake.reader_context import CONTEXT_MAX_BYTES, article_descriptor
from wake.reader_experiment import compare, fixture
from wake.reader_transport import export_reader_transport, record_path


class ReaderExperimentTests(unittest.TestCase):
    def test_controlled_comparison_measures_inputs_without_quality_claim(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            request = fixture(site)
            before = copy.deepcopy(request)
            result = compare(site, request)
        self.assertEqual(request, before)
        rows = {row['condition']: row for row in result['conditions']}
        self.assertEqual(rows['A']['metrics']['history_selected_turns'], 0)
        self.assertEqual(rows['B']['metrics']['history_selected_turns'], len(request['history']))
        for row in rows.values():
            self.assertEqual(row['metrics']['source_records'], 3)
            self.assertLessEqual(row['exact_input_bytes'], CONTEXT_MAX_BYTES)
        self.assertLess(rows['C']['exact_input_bytes'], rows['B']['exact_input_bytes'])
        self.assertEqual(result['provider_calls'], 0)
        self.assertIsNone(result['provider_tokens'])
        self.assertIsNone(result['energy_savings'])
        self.assertIn('Not measured', result['quality_assessment'])
        self.assertNotIn(request['question'], json.dumps(result))

    def test_exported_descriptor_does_not_mutate_publication_or_depend_on_head(self):
        article = {'id': 'post', 'title': 'A public note', 'body': 'Recorded observation.',
                   'evidence': [], 'created_version': 1}
        data = {'head': 'head-one', 'state': {'version': 1, 'posts': {'post': article}}, 'events': []}
        original = copy.deepcopy(data)
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            bootstrap = export_reader_transport(data, site)
            shard = json.loads((site / record_path('posts', 'post')).read_text())
            self.assertEqual(bootstrap['state']['posts']['post']['_reader_article'],
                             shard['article'])
            self.assertEqual(shard['item'], article)
        self.assertEqual(data, original)
        self.assertEqual(article_descriptor(article, 'head-one')['hash'],
                         article_descriptor(article, 'head-two')['hash'])
        revised = {**article, 'body': 'Corrected observation.'}
        self.assertNotEqual(article_descriptor(article, 'head-one')['hash'],
                            article_descriptor(revised, 'head-one')['hash'])


if __name__ == '__main__':
    unittest.main()
