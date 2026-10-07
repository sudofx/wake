"""Routine memory must preserve provenance, corrections, budget and policy authority."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from wake.engine import Engine, DEFAULTS, config
from wake.event_format import digest
from wake.governance import Rejected
from wake.memory import build_active_memory
from wake.providers import Fixture
from wake.record_store import RecordStore
from wake.retrieval import build_retrieval_shadow
from wake.trust import build_trust_compacts_shadow
from support import charter_settings
from test_research import project, notebook


class CountingFixture(Fixture):
    def __init__(self):
        super().__init__('active-memory-test')
        self.calls = 0
        self.request = None
    def propose(self, request):
        self.calls += 1
        self.request = copy.deepcopy(request)
        return super().propose(request)


class ActiveMemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = RecordStore(self.root / 'data', initialize_empty=True)
        self.engine = Engine(self.store.directory, dict(DEFAULTS), store=self.store)
        self.engine.initialize()

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def submit(self, actions):
        invocation, request = self.engine.start('manual', 'isolated-test')
        result = self.engine.finish(invocation, json.dumps(dict(base_version=request['context']['version'],
            title='Memory contract test', summary='Isolated test actions', actions=actions)))
        self.assertEqual(result['status'], 'accepted')

    def test_active_mode_delivers_routine_memory_below_ceiling_and_makes_one_call(self):
        self.engine.config['memory_mode'] = 'active'
        provider = CountingFixture()
        self.engine.run(provider)
        context = provider.request['context']
        self.assertEqual(provider.calls, 1)
        self.assertEqual(context['memory']['mode'], 'active')
        self.assertEqual(context['bounded_context']['activation_reason'], 'operator-active-memory')
        item = max(self.store.load()['invocations'].values(), key=lambda item: item['time'])
        self.assertLess(item['context_delivery']['rich_context_chars'], DEFAULTS['max_context_chars'])
        self.assertEqual(item['context_delivery']['memory_mode'], 'active')
        self.assertEqual(item['context_delivery']['memory_digest'], digest(context['memory']))
        self.assertEqual(item['request_hash'], digest(provider.request))
        self.assertIn('working_set_shadow', item)
        self.assertIn('retrieval_shadow', item)
        self.assertIn('trust_compacts_shadow', item)

    def test_switch_back_to_shadow_restores_rich_delivery(self):
        self.engine.config['memory_mode'] = 'active'
        self.engine.run(CountingFixture())
        self.engine.config['memory_mode'] = 'shadow'
        provider = CountingFixture()
        self.engine.run(provider)
        self.assertNotIn('memory', provider.request['context'])
        item = max(self.store.load()['invocations'].values(), key=lambda item: item['time'])
        self.assertEqual(item['context_delivery']['mode'], 'rich')
        self.assertEqual(item['context_delivery']['memory_mode'], 'shadow')

    def test_retracted_belief_and_new_human_falsifier_are_recovered_with_original_roots(self):
        self.engine.observe('An initial sensor comparison.', 'operator:initial', evidence_id='original')
        belief = dict(type='belief', id='b', statement='Sensor counts are equal.', confidence=0.95,
                      status='active', evidence=['original'], reason='Test reading', falsifier='A measured unequal count.')
        self.submit([belief])
        self.engine.observe('The measured counts are 2 and 3; the claim is false.', 'operator:measurement', evidence_id='falsifier')
        self.submit([{**belief, 'status': 'retracted', 'confidence': 0, 'evidence': ['falsifier'], 'reason': 'Measured unequal counts.'}])
        self.engine.config['memory_mode'] = 'active'
        invocation, request = self.engine.start('manual', 'next-model')
        memory = request['context']['memory']
        compact = memory['trust_compacts'][0]
        self.assertEqual(compact['status'], 'CHALLENGED')
        self.assertTrue(compact['advisory'])
        recovered = {(item['kind'], item['id']): item for item in memory['retrieved_records']}
        self.assertEqual(recovered['belief', 'b']['value']['status'], 'retracted')
        self.assertEqual(recovered['evidence', 'falsifier']['content_location'], {'field': 'context.evidence', 'id': 'falsifier'})
        self.assertEqual(recovered['evidence', 'falsifier']['value']['actor'], 'human')
        self.assertEqual(set(compact['provenance']['evidence_roots']), {'original', 'falsifier'})
        evidence = {item['id']: item for item in request['context']['evidence']}
        self.assertIn('false', evidence['falsifier']['content'])
        self.assertNotIn('content_omitted', evidence['falsifier'])

    def test_open_obligations_and_belief_identities_survive_routine_delivery(self):
        self.engine.observe('Test observation', 'operator:test', evidence_id='e')
        self.submit([dict(type='belief', id='b'+str(index), statement='Claim '+str(index), confidence=0.2,
                         status='active', evidence=['e'], reason='Isolated test') for index in range(8)])
        self.submit([dict(type='commit', id='c'+str(index), task='Review source '+str(index),
                         due_cycle=10, reason='An open obligation') for index in range(8)])
        self.engine.config['memory_mode'] = 'active'
        _, request = self.engine.start('manual', 'new-provider')
        self.assertEqual({item['id'] for item in request['context']['beliefs']}, {'b'+str(i) for i in range(8)})
        self.assertEqual({item['id'] for item in request['context']['commitments']}, {'c'+str(i) for i in range(8)})

    def test_impossible_budget_stops_before_provider_instead_of_dropping_obligations(self):
        self.engine.observe('Test observation', 'operator:test', evidence_id='e')
        for offset in (0, 10, 20, 30):
            self.submit([dict(type='belief', id='b'+str(index), statement='Long claim '+('content '*100), confidence=0.2,
                             status='active', evidence=['e'], reason='Isolated test') for index in range(offset, offset+10)])
        self.engine.config.update(memory_mode='active', max_context_chars=4000)
        provider = CountingFixture()
        with self.assertRaisesRegex(Rejected, 'Context ceiling'):
            self.engine.run(provider)
        self.assertEqual(provider.calls, 0)
        self.assertEqual(len(self.store.load()['beliefs']), 40)

    def test_missing_roots_are_visible_and_record_excerpts_are_labeled(self):
        state = dict(version=1, beliefs={'b': dict(id='b', statement='Long claim '+('content '*200), confidence=0,
                     status='retracted', evidence=['missing'], reason='Retracted')}, evidence={}, notebooks={}, commitments={})
        compacts = build_trust_compacts_shadow(state)
        retrieval = build_retrieval_shadow(state, {'beliefs': []}, compacts)
        before = copy.deepcopy(state)
        memory = build_active_memory(state, compacts, retrieval)
        self.assertEqual(memory['trust_compacts'][0]['missing_evidence_roots'], ['missing'])
        self.assertIn({'kind': 'evidence', 'id': 'missing'}, memory['omissions']['missing_records'])
        self.assertTrue(memory['retrieved_records'][0]['context_excerpt'])
        self.assertEqual(state, before)

    def test_active_memory_keeps_collector_and_human_source_roles_separate(self):
        self.engine.config.update(charter_settings(memory_mode='shadow'))
        self.engine.initialize()
        for identifier in ('s1', 's2'):
            self.store.append('observation', dict(id=identifier, source='https://example.org/'+identifier,
                actor='collector', scope='collected', content=json.dumps(dict(excerpt='entropy comparison measurement',
                verification_required=True, topic_domain='entropy', evidence_role='source',
                host_tier='verification-fulltext', source_identity='doi:'+identifier))))
        self.submit([project(), notebook(['s1', 's2'], 'Entropy comparison measurement [s1] [s2].')])
        self.engine.observe('Human commentary is not collected scientific evidence.', 'operator:comment', evidence_id='human')
        self.engine.config['memory_mode'] = 'active'
        _, request = self.engine.start('manual', 'memory-research-test')
        context = request['context']
        self.assertIn('s1', context['project_evidence']['p'])
        self.assertIn('s2', context['project_evidence']['p'])
        self.assertNotIn('human', context['project_evidence']['p'])
        self.assertEqual(set(context['blog_notebooks']['p'][0]['evidence']), {'s1', 's2'})
        item = self.store.load()['invocations'][self.store.load()['pending']]
        self.assertNotIn('evidence', item['working_set_shadow']['recent_notebooks'][0])

    def test_memory_cannot_bypass_collector_prose_budget(self):
        state = dict(version=1, beliefs={}, notebooks={}, commitments={}, evidence={
            identifier: dict(id=identifier, actor='collector', source='https://example.org/'+identifier,
                             scope='collected', version=index, content='Source prose '+identifier)
            for index, identifier in enumerate(('visible', 'outside-budget', 'discovery'))})
        retrieval = dict(candidates=[dict(trigger='unincorporated_evidence',
            record=dict(kind='evidence', id=identifier), evidence=[]) for identifier in state['evidence']])
        memory = build_active_memory(state, {'compacts': []}, retrieval, visible_collector_ids={'visible'})
        records = {item['id']: item for item in memory['retrieved_records']}
        self.assertIn('content', records['visible']['value'])
        for identifier in ('outside-budget', 'discovery'):
            self.assertNotIn('content', records[identifier]['value'])
            self.assertTrue(records[identifier]['content_omitted'])
            self.assertEqual(records[identifier]['record_hash'], digest(state['evidence'][identifier]))
        self.assertIn('content', state['evidence']['outside-budget'])

    def test_budget_compaction_preserves_obligations_and_recovery_pointers(self):
        from wake.event_format import canonical
        commitments = [{'id': 'c'+str(i), 'task': 'Review inherited work'} for i in range(8)]
        beliefs = [{'id': 'b', 'status': 'retracted', 'evidence': ['e']}]
        context = dict(commitments=copy.deepcopy(commitments), beliefs=copy.deepcopy(beliefs),
            evidence=[dict(id='e', content='Measured counterevidence')],
            memory=dict(retrieved_records=[dict(kind='evidence', id='e', value=dict(content='Measured counterevidence'))]),
            bounded_context=dict(omitted_categories=[]), representation_recovery=[dict(project='p',
                parked=dict(id='p', question='Long archived question '*1000),
                frames=[dict(id='frame', observations=['e'], old_frame='Long archived frame '*1000)])])
        request=dict(context=context)
        self.engine.config['max_context_chars'] = 4000
        self.engine.fit_active_request(request)
        self.assertLess(len(canonical(request)), 4000)
        self.assertEqual(context['beliefs'], beliefs)
        self.assertEqual(context['commitments'], commitments)
        self.assertEqual(context['representation_recovery'][0]['frames'], [dict(id='frame', observations=['e'])])
        self.assertEqual(context['evidence'][0]['content'], 'Measured counterevidence')
        original_hash = context['representation_recovery'][0]['record_hash']
        self.engine.config['max_context_chars'] = 100
        self.engine.fit_active_request(request)
        self.assertEqual(context['representation_recovery'][0]['record_hash'], original_hash)

    def test_invalid_mode_rejected(self):
        filename = self.root / 'invalid.toml'
        filename.write_text('memory_mode="authoritative"\n')
        with self.assertRaisesRegex(Rejected, 'memory_mode'):
            config(filename)
