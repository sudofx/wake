"""Task-shaped context must preserve recovery, provenance and offered-action contracts."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.engine import Engine
from wake.event_format import canonical, digest
from wake.memory import build_active_memory, compact_retrieved_records, preserve_retrieved_views
from wake.prompts import (BOUNDED_RESEARCH_SYSTEM, BOB_CHECKPOINT_SYSTEM, QUALITY_RESEARCH_SYSTEM,
                          compact_request_instructions)
from wake.providers import Fixture, provider_input_chars
from wake.record_store import RecordStore
from support import charter_settings


class RequestCompactionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = RecordStore(self.root / 'data', initialize_empty=True)
        self.engine = Engine(self.store.directory, charter_settings(memory_mode='active'), store=self.store)
        self.engine.initialize()

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def test_seed_is_consumed_by_any_durable_project_in_every_delivery_view(self):
        self.store.append('project_adopted', dict(id='old', title='Existing question', question='Question already owns its topic',
            domain='information_survival', status='parked', next_step='Await relevant evidence', reason='Fixture', actor='operator'))
        state = self.store.load()
        for mode in ('active', 'shadow'):
            self.engine.config['memory_mode'] = mode
            invocation, request = self.engine.start('manual', 'seed-boundary', phase='planning')
            topics = {t['id']: t for t in request['context']['research_topics']}
            self.assertNotIn('seed_question', topics['information_survival'])
            self.assertIn('seed_question', topics['curiosity'])
            self.store.append('recovered', dict(id=invocation, reason='Isolated test cleanup'))
        self.assertIn('seed_question', next(t for t in state['research_topics'] if t['id'] == 'information_survival'))

    def test_planning_is_fitted_as_planning_and_keeps_protected_context(self):
        seen = []
        fit = self.engine.fit_active_request
        def inspect(request):
            seen.append(deepcopy(request))
            fit(request)
        with patch.object(self.engine, 'fit_active_request', side_effect=inspect):
            _, request = self.engine.start('manual', 'planning-view', phase='planning', question='Find evidence for the current question')
        self.assertTrue(seen)
        for item in seen:
            self.assertEqual(set(item['response_schema']['properties']), {'requests'})
            self.assertEqual(item['context']['research_phase'], 'planning')
        context = request['context']
        for field in ('blog_notebooks', 'recent_blog', 'bob_reflection_due', 'reflection_history', 'proposal_constraints', 'evidence_quality'):
            self.assertNotIn(field, context)
        for field in ('attention', 'projects', 'beliefs', 'commitments', 'evidence'):
            self.assertIn(field, context)
        self.assertEqual(context['operator_question'], 'Find evidence for the current question')
        self.assertLessEqual(provider_input_chars(request), self.engine.config['max_context_chars'])

    def test_sharing_is_reversible_without_erasing_conflicts_or_missing_records(self):
        supplied = dict(id='n', summary='Exact supplied summary', evidence=['e1', 'e2'], source='record:one')
        matching = dict(kind='notebook', id='n', record_hash=digest(supplied), value=deepcopy(supplied), triggers=['notebook_revised'])
        conflict = dict(kind='notebook', id='n', record_hash='different', value={**supplied, 'evidence': ['other']})
        missing = dict(kind='notebook', id='absent', record_hash='absent-hash', value=dict(id='absent', summary='Only copy'))
        context = dict(notebooks=[deepcopy(supplied)], memory=dict(retrieved_records=[matching, conflict, missing]))
        original = deepcopy(context)
        compact_retrieved_records(context)
        self.assertEqual(context['notebooks'], original['notebooks'])
        self.assertEqual(matching['content_location'], dict(field='context.notebooks', id='n'))
        restored = {**context['notebooks'][0], **matching['value']}
        self.assertEqual(restored, original['memory']['retrieved_records'][0]['value'])
        self.assertEqual(matching['record_hash'], digest(supplied))
        self.assertEqual(conflict, original['memory']['retrieved_records'][1])
        self.assertEqual(missing, original['memory']['retrieved_records'][2])
        once = canonical(context)
        compact_retrieved_records(context)
        self.assertEqual(canonical(context), once)

    def test_collector_memory_reuses_source_delivery_instead_of_clipping_raw_json_again(self):
        source = dict(id='source', actor='collector', scope='collected', source='https://example.edu/paper',
                      content=canonical(dict(excerpt='Collected source prose ' * 200, evidence_role='source')))
        state = dict(version=3, evidence=dict(source=source))
        retrieval = dict(candidates=[dict(record=dict(kind='evidence', id='source'),
                          trigger='project_source_handoff', evidence=['source'])])
        memory = build_active_memory(state, dict(compacts=[]), retrieval, visible_collector_ids={'source'})
        item = memory['retrieved_records'][0]
        self.assertNotIn('content', item['value'])
        self.assertEqual(item['record_hash'], digest(source))
        context = dict(evidence=[deepcopy(source)], memory=memory)
        compact_retrieved_records(context)
        self.assertEqual(item['content_location'], dict(field='context.evidence', id='source'))
        self.assertEqual(context['evidence'][0]['content'], source['content'])
        hidden = build_active_memory(state, dict(compacts=[]), retrieval, visible_collector_ids=set())
        self.assertTrue(hidden['retrieved_records'][0]['content_omitted'])
        self.assertNotIn('content', hidden['retrieved_records'][0]['value'])
        # Context-only legacy/shadow builders do not change their delivery contract.
        self.assertIn('content', build_active_memory(state, dict(compacts=[]), retrieval)['retrieved_records'][0]['value'])

    def test_later_focus_cannot_leave_a_shared_record_pointer_without_its_content(self):
        supplied = dict(id='n', summary='The only surviving interpretation', evidence=['exact-root'])
        item = dict(kind='notebook', id='n', record_hash=digest(supplied),
                    content_location=dict(field='context.notebooks', id='n'), value={})
        context = dict(notebooks=[deepcopy(supplied)], memory=dict(retrieved_records=[item]))
        with preserve_retrieved_views(context):
            context['notebooks'] = []
        self.assertNotIn('content_location', item)
        self.assertEqual(item['value'], supplied)
        self.assertEqual(item['record_hash'], digest(supplied))
        self.assertTrue(item['context_excerpt'])

    def test_active_instruction_branches_follow_final_schema_and_can_reopen(self):
        ordinary = dict(properties=dict(actions=dict(items=dict(anyOf=[]))))
        context = dict(bob_reflection_due=False, research_quality_policy=3)
        system = BOUNDED_RESEARCH_SYSTEM + QUALITY_RESEARCH_SYSTEM
        compact = compact_request_instructions(system, context, ordinary)
        self.assertNotIn(BOB_CHECKPOINT_SYSTEM, compact)
        self.assertNotIn(QUALITY_RESEARCH_SYSTEM, compact)
        self.assertIn('Models propose; WAKE governance decides', compact)
        self.assertIn('Ordinary blog publication is optional', compact)
        due = deepcopy(ordinary); due['properties']['bob_checkpoint'] = dict(type='object')
        self.assertIn(BOB_CHECKPOINT_SYSTEM, compact_request_instructions(system, context, due))
        notebook = deepcopy(ordinary)
        notebook['properties']['actions']['items']['anyOf'] = [dict(properties=dict(type=dict(enum=['notebook'])))]
        self.assertIn(QUALITY_RESEARCH_SYSTEM, compact_request_instructions(compact, context, notebook))
        self.assertEqual(ordinary, dict(properties=dict(actions=dict(items=dict(anyOf=[])))))

    def test_optional_recall_does_not_reintroduce_planning_only_omissions(self):
        self.engine.config['decision_memory_mode'] = 'active'
        self.engine.observe('A measured calibration offset needs a targeted follow-up.', 'operator:calibration', evidence_id='measurement')
        before = self.store.load()['version']
        _, request = self.engine.start('manual', 'planning-recall', phase='planning', question='calibration offset')
        context = request['context']
        for field in ('proposal_constraints', 'proposal_recovery', 'evidence_quality', 'recent_blog'):
            self.assertNotIn(field, context)
        self.assertEqual(set(request['response_schema']['properties']), {'requests'})
        self.assertEqual(self.store.load()['version'], before)
        self.assertLessEqual(provider_input_chars(request), self.engine.config['max_context_chars'])

    def test_planning_reference_receipt_never_claims_accepted_research(self):
        from wake.decision_memory import DECISION_MEMORY_SYSTEM
        self.engine.config['decision_memory_mode'] = 'active'
        # A deterministic optional selection makes the reference boundary observable
        # without depending on unrelated fixture ranking or making a provider call.
        def recall(state, request, retrieval, question=None, phase='proposal'):
            request = deepcopy(request)
            request['system'] += DECISION_MEMORY_SYSTEM
            receipt = dict(mode='active', delivered=True, capsule=dict(selected_memories=[dict(kind='project', id='calibration')]))
            return request, receipt
        class Plan(Fixture):
            def propose(self, request):
                return canonical(dict(requests=[dict(query='calibration', domain='information_survival', project='', url='')])), {}
        before = self.store.load()['version']
        with patch.object(self.engine, 'decision_memory_delivery', side_effect=recall):
            result = self.engine._run_invocation(Plan('isolated-plan'), phase='planning')
        self.assertEqual(result['status'], 'planned')
        item = self.store.load()['invocations'][result['id']]
        self.assertEqual(item['decision_memory_use']['referenced'], [dict(kind='project', id='calibration')])
        self.assertEqual(item['decision_memory_use']['governance_outcome'], 'research_planned')
        self.assertIsNone(item['decision_memory_use']['decision_changed'])
        self.assertIsNone(item['decision_memory_use']['outcome_improved'])
        self.assertEqual(self.store.load()['version'], before)
        self.assertEqual(self.store.audit()[1], self.store.head())


if __name__ == '__main__':
    unittest.main()
