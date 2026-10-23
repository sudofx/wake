"""Forward research configuration preserves history and existing governance."""
import json
from pathlib import Path
import tempfile
import tomllib
import unittest

from wake.engine import Engine, _topics
from wake.governance import Rejected, transition
from wake.store import Store
from wake.research_expansion import (ASSIGNMENTS, EXPERIMENT_ID, apply_hosted_configuration,
                                     observations, compare_observations, observation_event,
                                     read_observation_history, CATALOG_EXPERIMENT_ID, EXPERIMENT_IDS)
from support import charter_settings

ROOT = Path(__file__).resolve().parents[1]


class ExpansionTests(unittest.TestCase):
    def test_restored_nodes_adopt_catalog_before_any_research_wake(self):
        from unittest.mock import patch
        from wake.standalone import bootstrap
        catalog = {t['id']: t for t in _topics({'research_topics_file': 'research-topics.toml'}, ROOT / 'wake.toml')}
        with tempfile.TemporaryDirectory() as directory:
            for parent, assigned in ASSIGNMENTS.items():
                for suffix in range(4):
                    node = parent[0] + str(suffix).zfill(2) + '.wake'
                    path = Path(directory) / node
                    settings = charter_settings('Research')
                    settings['research_topics'] = [catalog[t] for t in assigned[:2]]
                    with patch.dict('os.environ', {'WAKE_GROUP_INSTANCE': node}):
                        old = bootstrap(path, settings)
                        before = old.store.load()
                        prefix = json.dumps(old.store.events(), sort_keys=True)
                        old.store.close()
                        settings['research_topics'] = [catalog[t] for t in assigned]
                        restored = bootstrap(path, settings)
                        try:
                            state = restored.store.load()
                            self.assertEqual(state['version'], before['version'])
                            self.assertEqual(json.dumps(restored.store.events()[:-1], sort_keys=True), prefix)
                            self.assertEqual({t['id'] for t in state['research_topics']}, set(assigned))
                            self.assertEqual(state['research_configuration']['active_experiments'], sorted(EXPERIMENT_IDS))
                            self.assertEqual(state['research_configuration']['node'], node)
                            self.assertEqual(restored.store.replay()[0], state)
                        finally:
                            restored.store.close()

    def test_native_catalog_upgrade_appends_a_boundary_without_rewriting_history(self):
        from wake.record_store import RecordStore
        topics = _topics({'research_topics_file': 'research-topics.toml'}, ROOT / 'wake.toml')
        with tempfile.TemporaryDirectory() as directory:
            store = RecordStore(Path(directory), initialize_empty=True)
            try:
                settings = charter_settings('Research')
                settings['research_topics'] = topics[:3]
                engine = Engine(store.directory, settings, store=store)
                before = engine.initialize()
                events = json.dumps(store.events(), sort_keys=True)
                engine.config['research_topics'] = topics
                after = engine.initialize()
                self.assertEqual(json.dumps(store.events()[:-1], sort_keys=True), events)
                self.assertEqual(after['version'], before['version'])
                self.assertEqual(after['research_topics'][:3], before['research_topics'])
                self.assertEqual(after['research_configuration']['active_experiments'], sorted(EXPERIMENT_IDS))
                self.assertEqual(store.replay()[0], after)
            finally:
                store.close()

    def test_complete_history_review_rejects_mixed_truncated_or_broken_streams(self):
        import gzip
        heads = {'100': {'head': 'last', 'version': 1}}
        events = [
            {'seq': 1, 'prev_hash': '0' * 64, 'hash': 'first', 'kind': 'initialized',
             'origin': {'node': '100', **heads['100']}, 'payload': {}},
            {'seq': 2, 'prev_hash': 'first', 'hash': 'last', 'kind': 'accepted',
             'origin': {'node': '100', **heads['100']},
             'payload': {'proposal': {'base_version': 0, 'actions': [
                 {'type': 'notebook', 'id': 'n', 'project': 'p', 'findings': 'Public finding'}]}}}]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'events.jsonl.gz'
            def write(rows):
                with gzip.open(path, 'wt') as stream:
                    stream.write(''.join(json.dumps(row) + '\n' for row in rows))
            write(events)
            self.assertEqual(len(read_observation_history(path, heads)), 1)
            with self.assertRaises(ValueError):
                read_observation_history(path, {'100': {'head': 'other', 'version': 1}})
            for rows in (events[:1], events[1:], [events[0], {**events[1], 'prev_hash': 'wrong'}]):
                write(rows)
                with self.assertRaises(ValueError):
                    read_observation_history(path, heads)

    def test_activity_traces_later_notebook_changes_without_counting_rejections(self):
        from copy import deepcopy
        state = {'version': 4, 'projects': {'p': {'id': 'p', 'domain': 'topic', 'created_version': 1}},
                 'research_configuration': {'node': '100.wake'}}
        events = []
        for cycle, findings, outcome in [(1, 'First result', 'accepted'),
                                          (2, 'First result', 'accepted'),
                                          (3, 'Corrected result', 'rejected'),
                                          (4, 'Corrected result', 'accepted')]:
            events.append({'seq': cycle, 'hash': 'receipt-' + str(cycle), 'kind': outcome,
                'payload': {'id': 'wake-' + str(cycle), 'raw_response': 'PRIVATE RESPONSE',
                    'proposal': {'base_version': cycle - 1, 'actions': [
                        {'type': 'notebook', 'id': 'n', 'project': 'p', 'findings': findings}]}}})
        before = deepcopy(events)
        direct = observations(state, events)['questions'][0]['accepted_activity']
        compact = [observation_event(e) for e in events]
        self.assertEqual(observations(state, compact)['questions'][0]['accepted_activity'], direct)
        self.assertEqual(events, before)
        self.assertEqual([row['accepted_cycle'] for row in direct], [1, 2, 4])
        self.assertEqual(direct[0]['content_digest'], direct[1]['content_digest'])
        self.assertNotEqual(direct[1]['content_digest'], direct[2]['content_digest'])
        self.assertEqual(direct[-1]['hash'], 'receipt-4')
        encoded = json.dumps(compact)
        self.assertNotIn('PRIVATE', encoded)
        self.assertNotIn('Corrected result', encoded)
        self.assertEqual(observations(state, compact)['proposal_outcomes'], [])
        events[0]['payload']['proposal']['actions'][0]['private'] = 'PRIVATE NOTE'
        self.assertEqual(observations(state, events)['questions'][0]['accepted_activity'][0], direct[0])

    def test_notebook_only_activity_changes_are_visible_in_comparisons(self):
        from copy import deepcopy
        baseline = {'accepted_cycles': 2, 'questions': [{'id': 'p', 'accepted_activity': []}],
                    'source': {'installation_id': 'one', 'node_heads': {'100': {'version': 2}}}}
        current = deepcopy(baseline)
        current['accepted_cycles'] = 3
        current['source']['node_heads']['100']['version'] = 3
        current['questions'][0]['accepted_activity'] = [{'type': 'notebook', 'hash': 'new'}]
        report = compare_observations(baseline, current)
        self.assertTrue(report['activity_comparison_available'])
        self.assertEqual(report['changed_questions'], ['p'])
        del baseline['questions'][0]['accepted_activity']
        report = compare_observations(baseline, current)
        self.assertFalse(report['activity_comparison_available'])
        self.assertEqual(report['changed_questions'], [])

    def test_malformed_rejected_proposals_cannot_break_observation_exports(self):
        events = [{'kind': 'rejected', 'payload': {'proposal': proposal}}
                  for proposal in (None, [], {'actions': None}, {'actions': 'project'},
                                   {'actions': [None, 'project', 3]})]
        report = observations({'version': 0}, events)
        self.assertEqual(report['proposal_outcomes'], [])
        self.assertTrue(all(observation_event(event) is None for event in events))

    def test_report_never_mistakes_a_windowed_update_for_original_provenance(self):
        project = {'id': 'p', 'domain': 'assumption_challenge', 'created_version': 1,
                   'question': 'A new question', 'status': 'active'}
        state = {'version': 30, 'projects': {'p': project},
                 'research_configuration': {'node': '100.wake'},
                 'invocations': {'i': {'provider': 'fixture'}}}
        event = {'seq': 99, 'kind': 'accepted', 'payload': {'id': 'i',
                 'proposal': {'base_version': 29, 'actions': [{'type': 'project', **project}]}}}
        row = observations(state, [event])['questions'][0]
        self.assertIsNone(row['original_proposal'])
        self.assertIsNone(row['origin_event'])
        self.assertIsNone(row['simulated'])
        self.assertEqual(row['originating_node'], '100.wake')
        event['payload']['proposal']['base_version'] = 0
        row = observations(state, [event])['questions'][0]
        self.assertTrue(row['simulated'])
        self.assertIn('not a live discovery', row['origin'])

    def test_comparison_requires_same_installation_nodes_and_forward_cycles(self):
        from copy import deepcopy
        baseline = {'accepted_cycles': 2, 'questions': [{'id': 'p', 'status': 'active'}],
                    'source': {'installation_id': 'one', 'node_heads': {'100': {'version': 2}}}}
        current = deepcopy(baseline)
        current['accepted_cycles'] = 4
        current['source']['node_heads']['100']['version'] = 4
        current['questions'][0]['status'] = 'parked'
        current['questions'].append({'id': 'new', 'status': 'active'})
        report = compare_observations(baseline, current)
        self.assertEqual(report['accepted_cycle_delta'], 2)
        self.assertEqual(report['added_questions'], ['new'])
        self.assertEqual(report['changed_questions'], ['p'])
        for source in ({'installation_id': 'other', 'node_heads': {'100': {'version': 4}}},
                       {'installation_id': 'one', 'node_heads': {}},
                       {'installation_id': 'one', 'node_heads': {'100': {'version': 1}}}):
            current['source'] = source
            with self.assertRaises(ValueError):
                compare_observations(baseline, current)

    def test_broader_catalog_keeps_primary_ids_and_assigns_every_candidate(self):
        topics = _topics({'research_topics_file': 'research-topics.toml'}, ROOT / 'wake.toml')
        by_id = {t['id']: t for t in topics}
        self.assertEqual(len(by_id), 16)
        self.assertTrue(all(t['enabled'] for t in topics))
        self.assertEqual({t['id'] for t in topics if t.get('experiment_id') == EXPERIMENT_ID},
                         {'assumption_challenge', 'emergent_preferences', 'unassigned_problem'})
        self.assertEqual(sum(t.get('experiment_id') == CATALOG_EXPERIMENT_ID for t in topics), 13)
        self.assertEqual(set(by_id), {topic for group in ASSIGNMENTS.values() for topic in group})
        invalid = {**topics[-1], 'experiment_id': ''}
        with self.assertRaises(Rejected):
            _topics({'research_topics_file': 'unused', 'research_topics': [invalid]})

    def test_retirement_reactivation_and_boundaries_preserve_event_prefix(self):
        with tempfile.TemporaryDirectory() as directory:
            engine = Engine(Path(directory), charter_settings('Research'), store_factory=Store)
            try:
                state = engine.initialize()
                prefix = json.dumps(engine.store.events(), sort_keys=True)
                original = engine.config['research_topics']
                removed = original[-1]
                engine.config['research_topics'] = original[:-1]
                changed = engine.initialize()
                self.assertFalse(next(t for t in changed['research_topics'] if t['id'] == removed['id'])['enabled'])
                self.assertEqual(json.dumps(engine.store.events()[:-1], sort_keys=True), prefix)
                self.assertEqual(changed['version'], state['version'])
                self.assertEqual(changed['research_configuration']['effective_from_version'], state['version'])
                engine.config['research_topics'] = original
                restored = engine.initialize()
                self.assertEqual(restored['research_topics'], original)
                self.assertEqual(engine.store.replay()[0], restored)
                report = observations(restored, engine.store.events())
                self.assertTrue(report['boundaries'])
                self.assertTrue(all(x is None for x in report['assessment'].values()))
                # Configuration metadata cannot become a model action.
                for action in [{'type': 'research_topics_changed', 'topics': []},
                               {'type': 'delete_history'}, {'type': 'shell', 'command': 'true'},
                               {'type': 'experimental_regime_adopted', 'actor': 'operator'}]:
                    with self.assertRaises(Rejected):
                        transition(restored, {'base_version': restored['version'], 'title': 'Invalid',
                                   'summary': 'Invalid', 'actions': [action]}, 'test')
            finally:
                engine.store.close()

    def test_hosted_distribution_is_reversible_idempotent_and_keeps_originals(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base = root / 'config/.wake-runner-topics'
            base.mkdir(parents=True)
            original = '[[topics]]\nid="old"\nlabel="Original"\nquery="history"\nenabled=true\n'
            for parent in ASSIGNMENTS:
                (base / (parent + '.toml')).write_text(original)
            apply_hosted_configuration(root, True, True)
            first = {p.name: p.read_bytes() for p in base.iterdir()}
            apply_hosted_configuration(root, True, True)
            self.assertEqual(first, {p.name: p.read_bytes() for p in base.iterdir()})
            for parent, assigned in ASSIGNMENTS.items():
                topics = tomllib.loads((base / (parent + '.toml')).read_text())['topics']
                self.assertEqual([t['id'] for t in topics], ['old', *assigned])
                self.assertTrue(topics[0]['enabled'])
                # Saturation/capability rotation always has another coordinate.
                from wake.attention import plan
                state = {'charter': 'Research', 'research_topics': topics[1:],
                         'projects': {}, 'invocations': {},
                         'attention': {'attention': {'topic': assigned[0]},
                                       'deferred': {assigned[0]: {'cause': 'attention_saturation'}}}}
                self.assertIn(plan(state)['selected_topic'], assigned[1:])
            apply_hosted_configuration(root, True, False)
            for p in base.iterdir():
                topics = tomllib.loads(p.read_text())['topics']
                self.assertEqual(len(topics), 1 + len(ASSIGNMENTS[p.stem]))
                self.assertTrue(all(t['enabled'] == (t.get('experiment_id') != CATALOG_EXPERIMENT_ID)
                                    for t in topics))
            apply_hosted_configuration(root, False, True)
            for p in base.iterdir():
                topics = tomllib.loads(p.read_text())['topics']
                self.assertEqual(len(topics), 1 + len(ASSIGNMENTS[p.stem]))
                self.assertTrue(topics[0]['enabled'])
                self.assertTrue(all(not t['enabled'] for t in topics[1:]))
