"""Research views preserve provenance, scope, and source-depth uncertainty."""
import json
from copy import deepcopy
from pathlib import Path
import tempfile
import unittest

from wake.domain_events import empty
from wake.provenance import build_map
from wake.research_projection import build_research_projection, MAX_GRAPH_NODES
from wake.live import build_live_projection
from wake.engine import Engine
from wake.providers import Fixture
from wake.store import Store
from wake.report import export


class ResearchProjectionTests(unittest.TestCase):
    def state(self):
        state = empty()
        state['version'] = 2
        state['research_topics'] = [{'id': 'topic', 'label': 'A human-facing question'}]
        state['projects'] = {'p': {'id': 'p', 'title': 'A real project', 'question': 'What changed?',
                                   'status': 'active', 'domain': 'topic'}}
        state['notebooks'] = {'n': {'id': 'n', 'title': 'Source comparison', 'project': 'p',
                                    'evidence': ['a', 'b', 'metadata'], 'revision': 2}}
        state['evidence'] = {
            'a': {'id': 'a', 'source': 'https://example.org/a', 'content': json.dumps({'evidence_role': 'source', 'source_identity': 'doi:one', 'excerpt': 'Readable content'})},
            'b': {'id': 'b', 'source': 'https://example.org/mirror', 'content': json.dumps({'evidence_role': 'source', 'source_identity': 'doi:one', 'excerpt': 'Same work'})},
            'metadata': {'id': 'metadata', 'source': 'https://api.crossref.org/works/one', 'content': json.dumps({'evidence_role': 'metadata', 'excerpt': 'Metadata is not a source work'})},
            'receipt': {'id': 'receipt', 'source': 'runtime:continuity', 'content': '{}'},
            'unknown': {'id': 'unknown', 'source': 'https://example.org/unknown', 'content': '{clipped…'},
        }
        state['invocations'] = {
            'a': {'id': 'a', 'time': '2026-10-04T10:00:00+00:00', 'finished': '2026-10-04T10:01:00+00:00', 'status': 'accepted'},
            'b': {'id': 'b', 'time': '2026-10-04T12:00:00+00:00', 'finished': '2026-10-04T12:01:00+00:00', 'status': 'rejected'},
        }
        return state

    def test_classification_keeps_unknowns_receipts_and_work_identity_distinct(self):
        data = build_research_projection(self.state(), [], 'head')
        self.assertEqual(data['evidence']['source_works'], 1)
        self.assertEqual(data['evidence']['by_class'], {'source': 2, 'metadata': 1, 'receipt': 1, 'unclassified': 1})
        self.assertFalse(data['evidence']['classification_complete'])
        self.assertNotIn('receipt', [x['id'] for x in data['evidence']['recent']])

    def test_projection_does_not_mutate_or_invent_graph_relationships(self):
        state = self.state()
        before = deepcopy(state)
        graph = build_map(state, [], 'head', replay_history=False)
        data = build_research_projection(state, [], 'head', graph=graph)
        self.assertEqual(state, before)
        self.assertEqual(data['head'], graph['meta']['head'])
        self.assertFalse(data['authoritative'])
        original = {(e['source'], e['target'], e['relation'], e['record']) for e in graph['edges']}
        ids = {n['id'] for n in data['graph']['nodes']}
        for edge in data['graph']['edges']:
            self.assertIn((edge['source'], edge['target'], edge['relation'], edge['record']), original)
            self.assertIn(edge['source'], ids)
            self.assertIn(edge['target'], ids)

    def test_history_population_and_empty_hour_bins_are_explicit(self):
        data = build_research_projection(
            self.state(), [], 'head',
            metrics={'accepted_actions': {'by_type': {'notebook': 7, 'blog': 3}},
                     'storage': {'sqlite_bytes': 12_345}},
        )
        self.assertEqual(data['metrics']['completed'], 2)
        self.assertEqual(data['metrics']['outcomes'], {'accepted': 1, 'rejected': 1})
        self.assertEqual(len(data['metrics']['hourly']), 3)
        self.assertEqual(data['metrics']['hourly'][1], {'time': '2026-10-04T11:00:00+00:00'})
        self.assertEqual(data['metrics']['research_actions'], {'notebook': 7})
        self.assertEqual(data['metrics']['editorial_actions'], 3)
        self.assertFalse(data['metrics']['provider_requests_complete'])
        self.assertEqual(data['metrics']['storage'], {'sqlite_bytes': 12_345})

    def test_overview_is_bounded_without_dangling_edges(self):
        state = self.state()
        state['projects'] = {str(i): {'id': str(i), 'title': 'Project', 'status': 'parked'} for i in range(MAX_GRAPH_NODES + 10)}
        data = build_research_projection(state, [], 'head')
        self.assertLessEqual(len(data['graph']['nodes']), MAX_GRAPH_NODES)
        self.assertTrue(data['graph']['truncated'])
        self.assertEqual(data['record_totals']['projects'], MAX_GRAPH_NODES + 10)

    def test_export_refuses_a_research_snapshot_from_a_different_head(self):
        state = self.state()
        research = build_research_projection(state, [], 'other-head')
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaisesRegex(ValueError, 'does not match'):
                export(None, folder, browser_only=True, projection={
                    'state': state, 'head': 'head', 'events': [], 'research': research,
                })


    def test_cube_uses_native_coordinates_and_distinguishes_unknown_from_disabled(self):
        from wake.matrix import MATRIX, MATRIX_KEY
        unknown = build_research_projection(self.state(), [], 'head')['matrix']
        self.assertEqual(len(unknown['cells']), 343)
        self.assertEqual({x['id'] for x in unknown['cells']}, {x.coordinate_id for x in MATRIX.coordinates()})
        self.assertIsNone(unknown['enabled'])
        self.assertIsNone(unknown['completed'])
        disabled = build_research_projection(self.state(), [], 'head', matrix_reported=True)['matrix']
        self.assertFalse(disabled['enabled'])
        self.assertEqual(disabled['completed'], 0)
        coordinate = next(iter(MATRIX.coordinates())).coordinate_id
        progress = {'matrix': MATRIX_KEY, 'definition_digest': MATRIX.definition_digest,
                    'completed_count': 1, 'results': {coordinate: {'status': 'failed', 'score': 0.25,
                                                                  'invocation_id': 'b', 'research_status': 'rejected'}}}
        recorded = build_research_projection(self.state(), [], 'head', matrix_reported=True, matrix_progress=progress)['matrix']
        self.assertTrue(recorded['enabled'])
        self.assertEqual(recorded['cells'][0]['status'], 'failed')
        self.assertEqual(recorded['cells'][0]['score'], 0.25)
        self.assertEqual(recorded['cells'][0]['invocation_id'], 'b')
        self.assertEqual(recorded['cells'][0]['research_status'], 'rejected')
        with self.assertRaisesRegex(ValueError, 'definition'):
            build_research_projection(self.state(), [], 'head', matrix_progress={'matrix': 'wrong'})


    def test_wake_context_preserves_full_recorded_request_without_truncation(self):
        state = self.state()
        request = {'system': 'Full instructions ' * 500,
                   'context': {'objective': 'A full objective', 'material': 'Source material ' * 1000}}
        events = [{'kind': 'invocation_started', 'seq': 9, 'time': state['invocations']['b']['time'],
                   'hash': 'start-hash', 'payload': {'id': 'b', 'base_version': 2, 'request': request,
                   'context_delivery': {'delivered_request_chars': 18000, 'rich_context_chars': 36000, 'request_compression_ratio': 0.5}}}]
        before = deepcopy(events)
        trace = build_research_projection(state, events, 'head')['wakes'][0]
        self.assertEqual(trace['context']['system'], request['system'])
        self.assertEqual(trace['context']['request'], request)
        self.assertEqual(trace['base_version'], 2)
        self.assertEqual(trace['context_delivery']['request_compression_ratio'], 0.5)
        self.assertEqual(events, before)

    def test_wake_trace_preserves_rejection_receipt_and_explicit_context_gap(self):
        state = self.state()
        events = [{'kind': 'rejected', 'seq': 10, 'time': state['invocations']['b']['finished'],
                   'hash': 'terminal-hash', 'payload': {'id': 'b', 'reason': 'Rejected proposal',
                   'raw_response': json.dumps({'title': 'An unaccepted idea', 'actions': [{'type': 'project', 'id': 'p'}]})}}]
        trace = build_research_projection(state, events, 'head')['wakes'][0]
        self.assertEqual(trace['status'], 'rejected')
        self.assertFalse(trace['context']['available'])
        self.assertIsNone(trace['context']['characters'])
        self.assertTrue(trace['receipt']['available'])
        self.assertEqual(trace['receipt']['hash'], 'terminal-hash')
        self.assertIsNone(trace['receipt']['result_hash'])
        self.assertEqual(trace['proposal']['title'], 'An unaccepted idea')
        self.assertEqual(trace['proposal']['actions'][0]['type'], 'project')
        self.assertEqual(state['version'], 2)
        self.assertIsNotNone(trace['response'])

    def test_live_source_classification_precedes_clipping_and_survives_export(self):
        with tempfile.TemporaryDirectory() as folder:
            engine = Engine(Path(folder) / 'data', store_factory=Store)
            try:
                engine.run(Fixture())
                with engine.store.lock():
                    engine.store.append('observation', {'id': 'long-source', 'actor': 'collector', 'source': 'https://example.org/full',
                        'content': json.dumps({'evidence_role': 'source', 'source_identity': 'doi:full', 'excerpt': 'Research material ' * 400})})
                payload = build_live_projection(engine.store)
                self.assertEqual(payload['research']['evidence']['source_works'], 1)
                self.assertGreater(len(engine.store.load()['evidence']['long-source']['content']), 2400)
                self.assertLess(len(payload['state']['evidence']['long-source']['content']), 2500)
                export(None, Path(folder)/'site', browser_only=True, projection=payload)
                exported = json.loads((Path(folder)/'site/research-data.json').read_text())
                self.assertEqual(exported, payload['research'])
                self.assertEqual(exported['head'], payload['head'])
                for name in ('console.html', 'research.css', 'research.js'):
                    self.assertTrue((Path(folder)/'site'/name).exists())
            finally:
                engine.store.close()


if __name__ == '__main__':
    unittest.main()
