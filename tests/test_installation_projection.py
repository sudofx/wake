"""Unified views preserve node provenance without creating operational authority."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from wake.domain_events import empty
from wake.installation_projection import build_unified_projection
from wake.research_projection import build_research_projection, _matrix_projection
from wake.matrix import MATRIX, MATRIX_KEY
from wake.report import export


class InstallationProjectionTests(unittest.TestCase):
    def snapshot(self, node):
        state = empty()
        state.update(version=2, research_topics=[{'id': 'topic', 'label': 'Human topic'}],
                     projects={'p': {'id': 'p', 'title': 'Project', 'domain': 'topic', 'status': 'active'}},
                     notebooks={'n': {'id': 'n', 'title': 'Notebook', 'project': 'p', 'evidence': ['e'], 'summary': 'Summary', 'findings': 'Finding', 'limitations': 'Limited', 'next_questions': 'Next', 'revision': 1}},
                     evidence={'e': {'id': 'e', 'source': 'https://example.org/paper', 'content': json.dumps({'evidence_role': 'source', 'source_identity': 'doi:shared', 'excerpt': 'Shared passage'})}},
                     invocations={'i': {'id': 'i', 'time': '2026-10-13T10:00:00+00:00', 'status': 'accepted', 'provider': 'fixture', 'model': 'fixture'}},
                     journal=[{'invocation': 'i', 'cycle': 2, 'title': 'Work', 'summary': 'Work summary'}],
                     posts={'welcome': {'id': 'welcome', 'title': 'Welcome'},
                            'shared': {'id': 'shared', 'title': 'Group voice', 'body': 'Shared body', 'lede': 'Shared introduction', 'published_at': '2026-10-13T10:00:00+00:00', 'summary': 'Shared summary', 'created_by': 'i', 'status': 'current', 'evidence': [], 'notebooks': [], 'group_publication': {'group_id': 'group', 'checkpoint': 1, 'digest': 'digest', 'members': ['100', '101'], 'provider': {'name': 'gemini', 'model': 'actual-model'}}}})
        event = {'seq': 1, 'time': '2026-10-13T10:00:00+00:00', 'kind': 'accepted', 'hash': 'original-hash', 'payload': {'id': 'i', 'raw_response': 'exact bytes'}}
        return {'state': state, 'head': f'head-{node}', 'events': [event], 'generated': '2026-10-13T10:00:00+00:00', 'metrics': {'accepted_events': 2, 'accepted_actions': {'by_type': {'notebook': 1}}, 'storage': {'sqlite_bytes': 10}}}

    def build(self):
        packets = {node: self.snapshot(node) for node in ('100', '101')}
        research = {node: build_research_projection(packet['state'], [], packet['head']) for node, packet in packets.items()}
        return packets, research, build_unified_projection(packets, research, 'installation')

    def test_complete_history_is_separate_from_a_bounded_overview(self):
        from wake.installation_site import export_unified_site, export_unified_history
        packets, _, projection = self.build()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generations = {}
            for node, packet in packets.items():
                generation = root / node
                generation.mkdir()
                events = [{**packet['events'][0], 'seq': seq} for seq in range(1, 402)]
                (generation / 'events.jsonl').write_text(''.join(json.dumps(event) + '\n' for event in events))
                packet['events'] = events[-1:]
                generations[node] = generation
            target = root / 'unified'
            export_unified_site(projection, target)
            self.assertEqual(export_unified_history(generations, packets, target), 802)
            overview = json.loads((target / 'wake-data.json').read_text())
            self.assertEqual(overview['event_history']['total'], 802)
            self.assertLess(overview['event_history']['displayed'], 802)
            history = [json.loads(line) for line in (target / 'events.jsonl').read_text().splitlines()]
            self.assertEqual(history[0]['payload']['id'], '100::i')
            self.assertEqual(history[0]['original_event']['payload']['id'], 'i')
            self.assertNotIn('raw_response', history[0]['original_event']['payload'])
            self.assertTrue(all(row['projection_only'] for row in history))

    def test_namespaces_and_preserves_original_records_and_receipts(self):
        packets, research, unified = self.build()
        before = deepcopy((packets, research))
        repeated = build_unified_projection(packets, research, 'installation')
        self.assertEqual((packets, research), before)
        self.assertEqual(repeated['head'], unified['head'])
        self.assertEqual(unified['state']['version'], 4)
        self.assertFalse(unified['authoritative'])
        self.assertEqual(unified['state']['notebooks']['100::n']['project'], '100::p')
        self.assertEqual(unified['state']['notebooks']['101::n']['evidence'], ['101::e'])
        self.assertEqual(unified['state']['evidence']['100::e']['content'], packets['100']['state']['evidence']['e']['content'])
        self.assertEqual(unified['state']['notebooks']['101::n']['origin'], {'node': '101', 'head': 'head-101', 'version': 2, 'id': 'n'})
        for event in unified['events']:
            self.assertEqual(event['hash'], 'original-hash')
            self.assertEqual(event['original_event'], packets[event['origin']['node']]['events'][0])
            self.assertEqual(event['payload']['id'], event['origin']['node'] + '::i')
            self.assertEqual(event['payload']['raw_response'], 'exact bytes')
        self.assertEqual(unified['metrics']['accepted_events'], 4)
        self.assertEqual(unified['metrics']['storage']['sqlite_bytes'], 20)
        self.assertEqual(unified['research']['evidence']['source_works'], 1)
        self.assertFalse(unified['research']['matrix']['reported'])
        self.assertEqual(unified['research']['matrix']['score_count'], 0)

    def test_group_voice_deduplicates_only_exact_shared_publications(self):
        packets, research, unified = self.build()
        self.assertEqual(list(unified['state']['posts']), ['100::shared'])
        post = unified['state']['posts']['100::shared']
        self.assertEqual(len(post['origins']), 2)
        self.assertEqual(post['created_by'], '100::i')
        self.assertEqual(post['group_publication'], packets['100']['state']['posts']['shared']['group_publication'])
        packets['101']['state']['posts']['shared']['body'] = 'Different content'
        result = build_unified_projection(packets, research, 'installation')
        self.assertEqual(len(result['state']['posts']), 2)

    def test_project_frame_histories_keep_order_links_and_source_provenance(self):
        packets = {node: self.snapshot(node) for node in ('100', '101')}
        for packet in packets.values():
            packet['state']['representations'] = {'p': [
                {'type': 'reframe', 'project': 'p', 'old_frame': 'p',
                 'new_frame': label, 'observations': ['e'], 'created_by': 'i',
                 'created_version': version, 'status': 'hypothesis'}
                for version, label in enumerate(('First frame', 'Second frame'), 1)],
                'unused': []}
        original = deepcopy(packets)
        views = {node: build_research_projection(p['state'], [], p['head'])
                 for node, p in packets.items()}
        unified = build_unified_projection(packets, views, 'installation')
        histories = unified['state']['representations']
        self.assertEqual(set(histories), {'100::p', '101::p', '100::unused', '101::unused'})
        for node in packets:
            self.assertEqual(histories[f'{node}::unused'], [])
            frames = histories[f'{node}::p']
            self.assertEqual([f['new_frame'] for f in frames], ['First frame', 'Second frame'])
            for version, frame in enumerate(frames, 1):
                self.assertEqual(frame['project'], f'{node}::p')
                self.assertEqual(frame['observations'], [f'{node}::e'])
                self.assertEqual(frame['created_by'], f'{node}::i')
                self.assertEqual(frame['created_version'], version)
                self.assertEqual(frame['old_frame'], 'p')
                self.assertNotIn('id', frame)
                self.assertEqual(frame['origin'], {
                    'node': node, 'head': f'head-{node}', 'version': 2, 'project': 'p'})
        self.assertEqual(packets, original)
        with tempfile.TemporaryDirectory() as directory:
            export(None, destination=directory, projection=unified, standalone=True)
            exported = json.loads((Path(directory) / 'state.json').read_text())
            self.assertEqual(exported['representations'], histories)

    def test_graph_links_and_activity_are_node_qualified(self):
        _, _, unified = self.build()
        research = unified['research']
        self.assertEqual({item['id'] for item in research['activity']}, {'100::i', '101::i'})
        graph = research['graph']
        ids = {node['id'] for node in graph['nodes']}
        self.assertTrue(all(node.startswith(('100::', '101::')) for node in ids))
        for edge in graph['edges']:
            self.assertIn(edge['source'], ids)
            self.assertIn(edge['target'], ids)

    def test_exports_full_normal_website_without_store(self):
        _, _, unified = self.build()
        with tempfile.TemporaryDirectory() as directory:
            export(None, destination=directory, projection=unified, standalone=True)
            target = Path(directory)
            for name in ('index.html', 'console.html', 'state.json', 'wake-data.json', 'research-data.json', 'map-data.json', 'blog/100::shared.html', 'journal/100::i.html', 'notebooks/101::n.html'):
                self.assertTrue((target / name).exists(), name)
            data = json.loads((target / 'research-data.json').read_text())
            self.assertEqual(data['source']['installation'], 'unified')
            self.assertEqual(data['head'], unified['head'])

    def test_identical_topics_share_filter_but_conflicting_meanings_stay_separate(self):
        packets = {node: self.snapshot(node) for node in ('100', '101', '200')}
        for node, packet in packets.items():
            packet['state']['research_topics'][0].update(seed_question='Shared question', kind='scientific', enabled=True)
            packet['state']['invocations']['i']['attention'] = {'selected_topic': 'topic'}
            packet['events'][0]['payload'].update(domain='topic', request={'context': {'topic': 'topic'}})
            packet['metrics']['accepted_actions']['by_topic'] = {'topic': {'total': 1, 'by_type': {'notebook': 1}}}
        packets['200']['state']['research_topics'][0]['seed_question'] = 'Different question'
        original = deepcopy(packets)
        views = {node: build_research_projection(packet['state'], [], packet['head']) for node, packet in packets.items()}
        unified = build_unified_projection(packets, views, 'installation')
        topics = unified['state']['research_topics']
        self.assertEqual([topic['id'] for topic in topics], ['100::topic', '200::topic'])
        self.assertEqual([origin['node'] for origin in topics[0]['origins']], ['100', '101'])
        self.assertEqual(topics[0]['origins'][1]['head'], 'head-101')
        self.assertEqual(unified['state']['projects']['101::p']['domain'], '100::topic')
        self.assertEqual(unified['state']['projects']['200::p']['domain'], '200::topic')
        self.assertEqual(unified['state']['projects']['101::p']['origin']['node'], '101')
        self.assertEqual(unified['metrics']['accepted_actions']['by_topic']['100::topic']['total'], 2)
        self.assertEqual(unified['research']['metrics']['by_topic']['100::topic']['by_type']['notebook'], 2)
        self.assertEqual(unified['research']['topics'][0]['origins'], topics[0]['origins'])
        self.assertEqual(next(w for w in unified['research']['wakes'] if w['id'] == '101::i')['topic'], '100::topic')
        graph_project = next(n for n in unified['research']['graph']['nodes'] if n['id'].startswith('101::project:'))
        self.assertEqual(graph_project['detail']['domain'], '100::topic')
        projected_event = next(e for e in unified['events'] if e['origin']['node'] == '101')
        self.assertEqual(projected_event['payload']['domain'], '100::topic')
        self.assertEqual(projected_event['payload']['request']['context']['topic'], 'topic')
        self.assertEqual(projected_event['original_event'], original['101']['events'][0])
        self.assertEqual(packets, original)

    def test_unified_console_keeps_normal_site_below_installation_overview(self):
        from wake.installation_site import export_unified_site
        from wake.installation_cli import _copy_public_site
        _, _, unified = self.build()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / 'local'
            export_unified_site(unified, target)
            self.assertTrue((target / 'blog.xml').is_file())
            console = (target / 'console.html').read_text()
            self.assertLess(console.index('installation-overview'), console.index('id="status-band"'))
            self.assertEqual(console.count('id="main"'), 1)
            for panel in range(1, 19):
                self.assertIn(f'panel id: #{panel:03}', console)
            self.assertLess(console.index('panel id: #013'), console.index('panel id: #014'))
            self.assertLess(console.index('panel id: #014'), console.index('panel id: #015'))
            self.assertIn('masthead.css', console)
            self.assertIn('Group activity and things to watch', console)
            self.assertIn('id="installation-provenance"', console)
            deployment = json.loads((target / 'deployment.json').read_text())
            self.assertTrue(deployment['unified'])
            mirror = Path(directory) / 'public'
            _copy_public_site(target, mirror)
            self.assertTrue((mirror / 'blog.xml').is_file())
            self.assertIn('installation-overview', (mirror / 'console.html').read_text())
            self.assertIn('panel id: #018', (mirror / 'console.html').read_text())
            self.assertNotEqual((mirror / 'index.html').read_text(), console)
            self.assertIn('id="entries"', (mirror / 'journal.html').read_text())
            from wake.report import _READER_PAGES
            for section, filename in _READER_PAGES.items():
                document = (mirror / filename).read_text()
                self.assertIn(f'data-wake-page="{section}"', document)
                self.assertIn(f'<section id="{section}" class="view">', document)
                self.assertEqual(document.count('class="view"'), 1)
                self.assertIn('reader-theme.css', document)
                self.assertIn('page-routing.js', document)
            for filename in ('console.html', 'console-records.html', 'console-events.html'):
                document = (mirror / filename).read_text()
                self.assertNotIn('reader-theme.css', document)
                self.assertNotIn('page-routing.js', document)
            self.assertTrue(json.loads((mirror / 'deployment.json').read_text())['snapshot_only'])
            self.assertEqual(len(json.loads((mirror / 'state.json').read_text())['posts']), 1)

    def matrix_view(self, packet, results):
        view = build_research_projection(packet['state'], [], packet['head'])
        view['matrix'] = _matrix_projection({
            'matrix': MATRIX_KEY, 'definition_digest': MATRIX.definition_digest,
            'results': results, 'completed_count': sum(r['status'] == 'completed' for r in results.values()),
        }, True)
        return view

    def test_matrix_uses_latest_recorded_result_and_retains_all_node_contributions(self):
        packets = {node: self.snapshot(node) for node in ('100', '101')}
        coordinates = list(MATRIX.coordinates())
        first, second = coordinates[0].coordinate_id, coordinates[1].coordinate_id
        packets['101']['state']['invocations']['i']['finished'] = '2026-10-13T11:00:00+00:00'
        views = {
            '100': self.matrix_view(packets['100'], {first: {
                'status': 'completed', 'score': 1.0, 'invocation_id': 'i', 'passed': True, 'checks': {'answer': True}}}),
            '101': self.matrix_view(packets['101'], {
                first: {'status': 'completed', 'score': 0.2, 'invocation_id': 'i', 'passed': False, 'checks': {'answer': False}},
                second: {'status': 'completed', 'score': 0.7, 'invocation_id': 'i', 'passed': False, 'response_error': 'invalid answer'},
            }),
        }
        original = deepcopy((packets, views))
        matrix = build_unified_projection(packets, views, 'installation')['research']['matrix']
        self.assertEqual((packets, views), original)
        self.assertTrue(matrix['reported'])
        self.assertTrue(matrix['enabled'])
        cell = next(c for c in matrix['cells'] if c['id'] == first)
        self.assertEqual(cell['score'], 0.2)
        self.assertEqual(cell['invocation_id'], '101::i')
        self.assertEqual(cell['origin']['head'], 'head-101')
        self.assertEqual([r['score'] for r in cell['contributions']], [0.2, 1.0])
        self.assertEqual([r['origin']['node'] for r in cell['contributions']], ['101', '100'])
        self.assertEqual(matrix['completed'], 2)
        self.assertEqual(matrix['graded_count'], 1)
        self.assertEqual(matrix['passed'], 0)
        self.assertEqual(matrix['invalid_response_count'], 1)
        self.assertEqual(matrix['score_count'], 1)
        self.assertEqual(matrix['mean_score'], 0.2)
        self.assertEqual(matrix['failure_counts'], {'answer': 1})
        self.assertEqual(matrix['contribution_counts'], {'recorded': 3, 'completed': 3, 'failed': 0, 'deferred': 0, 'nodes': 2, 'coordinates': 2})
        self.assertIsNone(matrix['next_coordinate'])
        self.assertEqual(len(matrix['cells']), MATRIX.cell_count)
        self.assertEqual(sum(c['score'] is not None for c in matrix['cells']), 2)

    def test_matrix_missing_pass_status_is_not_inferred_from_a_score(self):
        packets = {'100': self.snapshot('100')}
        coordinate = next(iter(MATRIX.coordinates())).coordinate_id
        views = {'100': self.matrix_view(packets['100'], {coordinate: {
            'status': 'completed', 'score': 1.0, 'invocation_id': 'i'}})}
        matrix = build_unified_projection(packets, views, 'installation')['research']['matrix']
        self.assertIsNone(matrix['passed'])
        self.assertEqual(matrix['passed_known_cells'], 0)

    def test_matrix_rejects_mismatched_grammar_and_uses_stable_tie_break(self):
        packets = {node: self.snapshot(node) for node in ('100', '101')}
        coordinate = next(iter(MATRIX.coordinates())).coordinate_id
        views = {node: self.matrix_view(packet, {coordinate: {
            'status': 'completed', 'score': score, 'invocation_id': 'i', 'passed': False}})
            for (node, packet), score in zip(packets.items(), (0.1, 0.9))}
        matrix = build_unified_projection(packets, views, 'installation')['research']['matrix']
        cell = next(c for c in matrix['cells'] if c['id'] == coordinate)
        self.assertEqual(cell['origin']['node'], '101')
        views['101']['matrix']['definition_digest'] = 'different'
        with self.assertRaisesRegex(ValueError, 'grammar.*101'):
            build_unified_projection(packets, views, 'installation')

    def test_snapshot_fingerprint_tracks_instrument_changes_at_same_domain_head(self):
        packets, research, before = self.build()
        research['100']['matrix']['enabled'] = True
        after = build_unified_projection(packets, research, 'installation')
        self.assertNotEqual(before['head'],after['head'])
        self.assertEqual(before['source']['node_heads']['100']['head'],after['source']['node_heads']['100']['head'])

    def test_mismatched_research_fails_closed(self):
        packets, research, _ = self.build()
        research['101']['head'] = 'stale'
        with self.assertRaisesRegex(ValueError, 'node 101'):
            build_unified_projection(packets, research, 'installation')


if __name__ == '__main__':
    unittest.main()
