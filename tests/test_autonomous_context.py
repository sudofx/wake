"""Autonomous changes must earn bounded authority on the sole native record."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.autonomous_context import (BASELINE, CANDIDATE, SCHEMA, TRIAL_INTERVAL,
    advance, basis, initial, measure, policy_for, qualifies, reduce, rollback_reason, validate_settings)
from wake.autonomous_demo import demonstrate, seed, settings
from wake.decision_memory import decision_context
from wake.engine import Engine
from wake.event_format import digest
from wake.governance import Rejected
from wake.improvement_tasks import cases, expected
from wake.record_store import RecordStore


class AutonomousPolicyTests(unittest.TestCase):
    def state(self, index=0):
        state = deepcopy(cases(7, 12)[index]['state'])
        state.update(pending=None, invocations={})
        state['autonomous_context'] = {**initial(), 'enabled': True}
        return state

    def trial(self, state):
        return {'seq': 10, 'prev_hash': 'a' * 64, 'kind': 'autonomous_context_trial',
                'payload': {'schema': SCHEMA, 'actor': 'runtime', 'base_version': state['version'],
                            'based_on_head': 'a' * 64, 'prior_revision': state['autonomous_context']['revision'],
                            'proposal': {'policy': dict(CANDIDATE), 'basis': basis(state)}, 'seed': 37,
                            'measurement': measure(state, BASELINE, CANDIDATE, 37)}}

    def test_adoption_requires_both_fixed_and_current_native_improvement(self):
        state = self.state()
        event = self.trial(state)
        changed = reduce(state, event)
        self.assertEqual(changed['policy'], CANDIDATE)
        self.assertEqual(changed['adoptions'], 1)
        self.assertTrue(qualifies(changed['last_trial']['measurement']))
        self.assertEqual(state['autonomous_context']['policy'], BASELINE)
        # A fulfilled obligation does not justify changing the running policy.
        no_gain = self.state(1)
        # Include a still-open but non-preferred-topic obligation as a trigger.
        no_gain['commitments']['another'] = {'status': 'open', 'project': next(k for k in no_gain['projects'] if k.startswith('b-')),
                                            'due_cycle': 1}
        rejected = reduce(no_gain, self.trial(no_gain))
        self.assertEqual(rejected['policy'], BASELINE)
        self.assertEqual(rejected['last_trial']['status'], 'rejected_no_measured_gain')

    def test_candidate_cannot_edit_code_permissions_evaluator_or_quota(self):
        state = self.state()
        for field in ('candidate_source', 'daily_call_limit', 'governance', 'metric', 'deadline_horizon'):
            event = self.trial(state)
            event['payload']['proposal']['policy'][field] = 'change me'
            with self.subTest(field=field), self.assertRaises(Rejected):
                reduce(state, event)

    def test_forged_scores_provenance_stale_head_and_extra_fields_are_rejected(self):
        state = self.state()
        mutations = [lambda p: p['measurement']['holdout']['after'].update(passed=0),
                     lambda p: p['proposal']['basis'][0].update(digest='0' * 64),
                     lambda p: p.update(based_on_head='b' * 64),
                     lambda p: p.update(base_version=state['version'] - 1),
                     lambda p: p.update(prior_revision=9),
                     lambda p: p.update(seed=True), lambda p: p.update(approve=True)]
        for mutate in mutations:
            event = self.trial(state)
            mutate(event['payload'])
            with self.assertRaises(Rejected):
                reduce(state, event)

    def test_no_policy_change_during_pending_invocation_or_without_grant(self):
        state = self.state()
        event = self.trial(state)
        state['pending'] = 'in-flight'
        with self.assertRaisesRegex(Rejected, 'during an invocation'):
            reduce(state, event)
        state['pending'] = None
        state['autonomous_context']['enabled'] = False
        with self.assertRaisesRegex(Rejected, 'not enabled'):
            reduce(state, event)

    def test_change_allowance_and_cadence_cannot_be_removed_by_proposal(self):
        state = self.state()
        state['autonomous_context']['last_trial_version'] = state['version'] - TRIAL_INTERVAL + 1
        with self.assertRaisesRegex(Rejected, 'cadence'):
            reduce(state, self.trial(state))
        state['autonomous_context']['last_trial_version'] = None
        state['autonomous_context'] = reduce(state, self.trial(state))
        with self.assertRaisesRegex(Rejected, 'change allowance'):
            reduce(state, self.trial(state))

    def test_topic_override_and_missing_deadlines_remain_outside_candidate_authority(self):
        for case in cases(511, 120):
            self.assertEqual(decision_context(case['state'], case['question'], selection_policy=CANDIDATE), expected(case))
        with self.assertRaises(ValueError):
            decision_context(self.state(), selection_policy={'selector': 'run-python'})

    def test_enablement_is_boolean_and_requires_active_recall(self):
        for value in ('true', 1, None):
            with self.assertRaises(Rejected):
                validate_settings({'autonomous_context_improvement': value, 'decision_memory_mode': 'active'})
        with self.assertRaises(Rejected):
            validate_settings({'autonomous_context_improvement': True, 'decision_memory_mode': 'shadow'})
        self.assertFalse(validate_settings({}))

    def test_rollback_monitor_excludes_quota_waits_undelivered_context_and_other_models(self):
        state = self.state()
        state['autonomous_context'] = reduce(state, self.trial(state))
        old = [{'id': f'before-{i}', 'accepted': True} for i in range(8)]
        state['autonomous_context']['baseline_windows'] = [{'group': ['gemini', 'same-model', 'proposal'], 'observations': old}]
        def populate(model, statuses, delivered=True):
            state['invocations'] = {f'after-{i}': {'id': f'after-{i}', 'provider': 'gemini', 'model': model,
                'phase': 'proposal', 'status': outcome, 'autonomous_context_revision': 1,
                'context_delivery': {'decision_memory': {'delivered': delivered}}} for i, outcome in enumerate(statuses)}
        populate('same-model', ['deferred'] * 8)
        self.assertIsNone(rollback_reason(state))
        populate('different-model', ['rejected'] * 8)
        self.assertIsNone(rollback_reason(state))
        populate('same-model', ['rejected'] * 8, False)
        self.assertIsNone(rollback_reason(state))
        populate('same-model', ['accepted'] * 6 + ['rejected'] * 2)
        self.assertEqual(rollback_reason(state)['kind'], 'observed_acceptance_regression')
        first = rollback_reason(state)
        state['invocations'] = dict(reversed(list(state['invocations'].items())))
        self.assertEqual(rollback_reason(state), first)


class NativeAutonomousTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root / 'record', settings(), store=RecordStore(self.root / 'record', initialize_empty=True))
        self.addCleanup(self.engine.store.close)
        self.engine.initialize()
        seed(self.engine)

    def test_native_loop_generates_tests_adopts_and_delivers_without_human_review(self):
        e = self.engine
        before = deepcopy(e.store.load())
        prefix = e.store.events()
        e.config['autonomous_context_improvement'] = True
        invocation, request = e.start('fixture', 'autonomy-model')
        state = e.store.load()
        self.assertEqual(state['autonomous_context']['adoptions'], 1)
        self.assertEqual(state['version'], before['version'])
        self.assertEqual(state['commitments'], before['commitments'])
        self.assertEqual(state['journal'], before['journal'])
        self.assertEqual(state['projects'], before['projects'])
        self.assertEqual(e.store.events()[:len(prefix)], prefix)
        delivery = state['invocations'][invocation]['context_delivery']['decision_memory']
        self.assertTrue(delivery['delivered'])
        self.assertEqual(delivery['capsule']['decision_context']['project_id'], 'z')
        self.assertEqual(state['invocations'][invocation]['autonomous_context_revision'], 1)
        e.finish(invocation, '{}')  # End the controlled test with an explicit rejection.
        audited, _ = e.store.audit()
        self.assertEqual(audited, e.store.load())

    def test_configuration_off_and_pending_state_do_not_run_trials(self):
        e = self.engine
        before = e.store.events()
        advance(e.store, False)
        self.assertEqual(e.store.events(), before)
        invocation, _ = e.start('fixture', 'autonomy-model')
        with self.assertRaisesRegex(Rejected, 'idle invocation boundary'):
            advance(e.store, True)
        e.finish(invocation, '{}')

    def test_fault_rolls_back_and_quarantines_without_replaying_failed_change(self):
        e = self.engine
        state = advance(e.store, True)
        self.assertEqual(state['autonomous_context']['policy'], CANDIDATE)
        original_prefix = e.store.events()
        with patch('wake.autonomous_context.decision_context', side_effect=ValueError('simulated selector fault')):
            state = advance(e.store, True)
        self.assertEqual(state['autonomous_context']['policy'], BASELINE)
        self.assertTrue(state['autonomous_context']['quarantined'])
        self.assertEqual(state['autonomous_context']['rollbacks'], 1)
        before = e.store.events()
        advance(e.store, True)
        self.assertEqual(e.store.events(), before)
        self.assertEqual(e.store.events()[:len(original_prefix)], original_prefix)
        self.assertEqual(e.store.audit()[0], state)  # Replay works after the fault disappears.

    def test_measurement_fault_is_recorded_and_baseline_research_can_continue(self):
        e = self.engine
        with patch('wake.autonomous_context.measure', side_effect=RuntimeError('private diagnostic must not persist')):
            state = advance(e.store, True)
        self.assertEqual(state['autonomous_context']['last_trial']['status'], 'rejected_evaluation_error')
        self.assertEqual(state['autonomous_context']['last_trial']['error_type'], 'RuntimeError')
        self.assertEqual(state['autonomous_context']['policy'], BASELINE)
        self.assertTrue(state['autonomous_context']['quarantined'])
        self.assertNotIn('private diagnostic', json.dumps(state['autonomous_context']))
        self.assertEqual(e.store.audit()[0], state)
        e.config['autonomous_context_improvement'] = True
        invocation, _ = e.start('fixture', 'baseline-after-fault')
        e.finish(invocation, '{}')
        self.assertEqual(e.store.load()['autonomous_context']['trials'], 1)

    def test_matched_live_outcome_regression_automatically_rolls_back(self):
        e = self.engine
        def complete(accepted, index):
            invocation, request = e.start('fixture', 'matched-model')
            delivered = e.store.load()['invocations'][invocation]['context_delivery']['decision_memory']['delivered']
            if not accepted:
                e.finish(invocation, '{}')
                return delivered
            action = dict(type='project', id='z', title='Synthetic project z',
                          question='Compare the recorded alternatives for z', domain='memory', status='active',
                          next_step=f'Controlled next step {index}', reason='Controlled matched outcome fixture')
            result = e.finish(invocation, json.dumps(dict(base_version=request['context']['version'],
                               title='Continue the controlled project', summary='A synthetic outcome.', actions=[action])))
            self.assertEqual(result['status'], 'accepted', result)
            return delivered
        delivered, index = 0, 0
        while delivered < 8 and index < 40:
            delivered += complete(True, index)
            index += 1
        self.assertEqual(delivered, 8)
        e.config['autonomous_context_improvement'] = True
        delivered = 0
        while delivered < 8 and index < 80:
            delivered += complete(delivered < 6, index)
            index += 1
        self.assertEqual(delivered, 8)
        state = advance(e.store, True)
        self.assertEqual(state['autonomous_context']['rollbacks'], 1)
        self.assertEqual(state['autonomous_context']['last_rollback']['reason']['kind'], 'observed_acceptance_regression')
        self.assertEqual(state['autonomous_context']['policy'], BASELINE)
        self.assertTrue(state['autonomous_context']['quarantined'])
        self.assertEqual(e.store.audit()[0], state)

    def test_model_research_reply_cannot_grant_itself_autonomy(self):
        e = self.engine
        invocation, request = e.start('fixture', 'untrusted-model')
        result = e.finish(invocation, json.dumps(dict(base_version=request['context']['version'],
                           title='Request forbidden permission', summary='An untrusted attempt.',
                           actions=[{'type': 'autonomous_context_configured', 'enabled': True, 'actor': 'operator'}])))
        self.assertEqual(result['status'], 'rejected')
        self.assertNotIn('autonomous_context', e.store.load())

    def test_disabling_grant_reverts_effective_behavior_and_preserves_history(self):
        e = self.engine
        advance(e.store, True)
        prefix = e.store.events()
        state = advance(e.store, False)
        self.assertEqual(policy_for(state, True), BASELINE)
        self.assertEqual(policy_for(state, False), BASELINE)
        self.assertEqual(state['autonomous_context']['adoptions'], 1)
        self.assertEqual(e.store.events()[:len(prefix)], prefix)
        self.assertEqual(e.store.audit()[0], state)

    def test_restart_uses_the_recorded_policy_without_duplicate_adoption(self):
        e = self.engine
        advance(e.store, True)
        before = e.store.events()
        reopened = RecordStore(self.root / 'record')
        try:
            state = advance(reopened, True)
            self.assertEqual(state['autonomous_context']['adoptions'], 1)
            self.assertEqual(reopened.events(), before)
            self.assertEqual(reopened.audit()[0], state)
        finally:
            reopened.close()

    def test_cli_demo_is_fully_automatic_but_does_not_claim_live_research_improvement(self):
        result = demonstrate(self.root / 'demo')
        self.assertEqual(result['human_reviews'], 0)
        self.assertEqual(result['proposals_supplied_by_human'], 0)
        self.assertEqual(result['model_calls'], 0)
        self.assertTrue(result['replay_verified'])
        self.assertEqual(result['research_cycles_after_adoption'], result['research_cycles_before_adoption'])
        self.assertEqual(result['delivered_project'], 'z')
        self.assertTrue((self.root / 'demo/autonomous.html').exists())
        with self.assertRaises(Rejected):
            demonstrate(self.root / 'demo')
