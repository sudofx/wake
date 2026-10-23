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
                                     observations, compare_observations, observation_event)
from support import charter_settings

ROOT = Path(__file__).resolve().parents[1]


class ExpansionTests(unittest.TestCase):
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

    def test_fresh_catalog_has_exactly_three_experiments(self):
        topics = _topics({'research_topics_file': 'research-topics.toml'}, ROOT / 'wake.toml')
        by_id = {t['id']: t for t in topics}
        self.assertEqual(len(by_id), 3)
        self.assertTrue(all(t['enabled'] for t in topics))
        self.assertEqual({t['id'] for t in topics if t.get('experiment_id') == EXPERIMENT_ID},
                         {topic for group in ASSIGNMENTS.values() for topic in group})
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
            apply_hosted_configuration(root, True)
            first = {p.name: p.read_bytes() for p in base.iterdir()}
            apply_hosted_configuration(root, True)
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
                self.assertEqual(plan(state)['selected_topic'], assigned[1])
            apply_hosted_configuration(root, False)
            for p in base.iterdir():
                topics = tomllib.loads(p.read_text())['topics']
                self.assertEqual(len(topics), 3)
                self.assertTrue(topics[0]['enabled'])
                self.assertFalse(topics[1]['enabled'])
                self.assertFalse(topics[2]['enabled'])
