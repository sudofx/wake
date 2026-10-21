"""Recall is optional derived input; provenance and governance remain mandatory."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from wake.comparison import (evaluate_decision_memory, create_comparison, prepare_trial,
                             complete_trial, comparison_report, DECISION_ARMS)
from wake.decision_memory import (decision_context, rank_candidates, build_capsule,
                                  policy_config, validate_capsule, reference_observation)
from wake.engine import DEFAULTS, Engine, config
from wake.event_format import canonical, digest
from wake.governance import Rejected
from wake.providers import Fixture, provider_input_chars
from wake.record_store import RecordStore
from support import charter_settings
from test_research import project

CASES = Path(__file__).parent / 'fixtures' / 'decision_memory.json'


class SelectionTests(unittest.TestCase):
    def cases(self):
        return json.loads(CASES.read_text())['cases']

    def select(self, case, *, policy=None, context=None):
        state = case['state']
        policy = policy_config(policy or case.get('policy'))
        plan = rank_candidates(state, case['retrieval'], decision_context(state), policy)
        context = context or dict(evidence=list(state['evidence'].values()),
                                  commitments=list(state['commitments'].values()))
        eligible = [key for key in state['evidence'] if Engine.durable_notebook_source_payload(None, state, key)]
        return build_capsule(state, digest(state), plan, context, eligible_source_ids=eligible), plan

    def test_all_ten_predefined_scenarios_and_report_boundaries(self):
        report = evaluate_decision_memory(CASES)
        self.assertEqual(report['scenario_count'], 10)
        self.assertTrue(report['passed'], [r for r in report['scenarios'] if not r['passed']])
        self.assertEqual(report['api_calls'], 0)
        self.assertFalse(report['behavioral_quality_measured'])
        self.assertIsNone(report['outcome_improved'])
        self.assertEqual(next(r['missing_evidence_root_count'] for r in report['scenarios']
                              if r['scenario']=='missing_or_ineligible_source'),1)
        for row in report['scenarios']:
            with self.subTest(row['scenario']):
                self.assertEqual(row['missing_provenance_count'], 0)
                self.assertEqual(row['incorrect_source_eligibility_count'], 0)
                self.assertEqual(row['labeled_irrelevant_selection_count'], 0)

    def test_failure_classes_are_not_scientific_disconfirmation(self):
        result, _ = self.select(self.cases()[0])
        values = {m['id']: m['reliability'] for m in result['capsule']['selected_memories']}
        self.assertIn('rejected_proposal', values['rejected-old'])
        self.assertIn('provider_failure', values['provider-old'])
        self.assertIn('retrieval_failure', values['retrieval-old'])
        self.assertTrue(all('not_scientific_disconfirmation' in values[i] for i in values if i != 'p'))

    def test_current_revision_review_missing_roots_and_cross_topic_honesty(self):
        result, _ = self.select(self.cases()[6])
        notebook = next(m for m in result['capsule']['selected_memories'] if m['id'] == 'revised')
        self.assertEqual(notebook['revision'], 2)
        self.assertEqual(notebook['current_review']['assessment'], 'needs-source-review')
        result, _ = self.select(self.cases()[3])
        analogy = next(m for m in result['capsule']['selected_memories'] if m['id'] == 'analogy')
        self.assertIn('cross_topic_hypothesis_only', analogy['selection_reasons'])
        result, _ = self.select(self.cases()[9])
        note = next(m for m in result['capsule']['selected_memories'] if m['id'] == 'incomplete')
        self.assertEqual(note['missing_roots'], ['missing-root'])
        self.assertIn('metadata',note['roots_not_delivered_as_scientific_sources'])
        self.assertIn({'kind':'evidence','id':'missing-record','reason':'missing_record'},result['exclusions'])
        self.assertNotIn('metadata', [m['id'] for m in result['capsule']['selected_memories']])

    def test_source_works_deduplicate_without_erasing_node_attribution(self):
        result, _ = self.select(self.cases()[8])
        sources = [m for m in result['capsule']['selected_memories'] if m['kind']=='evidence']
        self.assertEqual(len(sources),1)
        self.assertEqual(sources[0]['origin'], {'node':'100.wake'})
        self.assertEqual(sources[0]['root_records'][0]['origin'], {'node':'100.wake'})
        self.assertEqual(next(e['reason'] for e in result['exclusions'] if e['id']=='copy-b'),'duplicate_source_work')
        case=self.cases()[8];state=case['state']
        plan=rank_candidates(state,case['retrieval'],decision_context(state))
        control=build_capsule(state,digest(state),plan,dict(evidence=list(state['evidence'].values())),
                              eligible_source_ids=state['evidence'],ablate={'kind':'evidence','id':'copy-a'})
        self.assertFalse(any(m.get('source_work')==sources[0]['source_work'] for m in control['capsule']['selected_memories']))
        self.assertEqual(next(e['reason'] for e in control['exclusions'] if e['id']=='copy-b'),'isolated_ablation_equivalent_work')

    def test_stable_order_despite_mapping_order_and_policy_override(self):
        case = self.cases()[0]
        first, _ = self.select(case)
        reordered = deepcopy(case)
        for field in ('projects','invocations','research'):
            reordered['state'][field] = dict(reversed(list(case['state'][field].items())))
        second, _ = self.select(reordered)
        self.assertEqual(canonical(first), canonical(second))
        policy = policy_config()
        policy['priority'].reverse()
        changed, _ = self.select(case, policy=policy)
        self.assertNotEqual(first['capsule']['selection_policy_digest'], changed['capsule']['selection_policy_digest'])

    def test_projection_scan_rotates_and_can_reactivate_dormant_record(self):
        case = self.cases()[2]
        original = case['state']['notebooks'].pop('old-useful')
        for i in range(350):
            identifier = 'n-%04d' % i
            case['state']['notebooks'][identifier] = {**original,'id':identifier,'project':'unrelated',
                'summary':'Banana recipes','title':'Banana recipes','findings':'Cooking','limitations':'Kitchen'}
        case['state']['notebooks']['n-0175'] = {**original,'id':'n-0175'}
        found = False
        for version in range(400, 417):
            case['state']['version'] = version
            result, plan = self.select(case)
            self.assertLessEqual(plan['coverage']['payloads_scanned'], policy_config()['scan_records'])
            self.assertGreater(plan['coverage']['unscanned_records'],0)
            found |= 'n-0175' in [m['id'] for m in result['capsule']['selected_memories']]
        self.assertTrue(found)

    def test_capsule_is_snapshot_bound_and_source_hashes_are_verified(self):
        case=self.cases()[1]
        result,_=self.select(case)
        capsule=result['capsule'];state=case['state'];head=digest(state)
        validate_capsule(capsule,state,head)
        with self.assertRaisesRegex(Rejected,'Stale'):
            validate_capsule(capsule,state,'different-head')
        modified=deepcopy(state);modified['beliefs']['corrected']['status']='active'
        with self.assertRaisesRegex(Rejected,'source changed'):
            validate_capsule(capsule,modified,head)
        modified=deepcopy(state);modified['evidence']['after']['content']='Changed root'
        with self.assertRaisesRegex(Rejected,'provenance changed'):
            validate_capsule(capsule,modified,head)

    def test_explicit_prior_interpretation_is_marked_superseded_and_hashed(self):
        case=self.cases()[1];state=case['state'];current=state['beliefs']['corrected']
        old={**current,'statement':'sensor calibration is within range','status':'active','confidence':0.8,'evidence':['before']}
        state['invocations']['revision-receipt']={'id':'revision-receipt','status':'accepted','decision_memory_use':
            {'belief_revisions':{'corrected':{'previous_record':old,'previous_record_hash':digest(old),
              'current_record_hash':digest(current),'boundary':'Superseded interpretation, never a current default.'}}}}
        result,_=self.select(case)
        memory=next(m for m in result['capsule']['selected_memories'] if m['id']=='corrected')
        self.assertEqual(memory['status'],'retracted')
        self.assertEqual(memory['prior_interpretation']['record_hash'],digest(old))
        self.assertIn('Superseded',memory['prior_interpretation']['boundary'])

    def test_unexpected_outcome_needs_predeclared_measurement_failure(self):
        case=self.cases()[2]
        case['state']['reproductions']={'r':dict(id='r',claim='sensor calibration',runs=[{'measured':1}],acceptance={'passed':False})}
        _,plan=self.select(case)
        self.assertIn('unexpected_outcome',next(c for c in plan['candidates'] if c['id']=='r')['categories'])

    def test_no_invented_contradiction_or_surprise_from_wording(self):
        case=self.cases()[2];case['state']['notebooks']['old-useful']['summary']='Surprising conflicting sensor calibration words'
        _,plan=self.select(case)
        item=next(c for c in plan['candidates'] if c['id']=='old-useful')
        self.assertNotIn('explicit_review',item['categories'])
        self.assertNotIn('unexpected_outcome',item['categories'])

    def test_capsule_reuses_identical_clipped_prose_but_retains_exact_roots(self):
        case = self.cases()[2]
        record = case['state']['notebooks']['old-useful']
        record['summary'] = 'Sensor calibration still requires careful independent checking. ' * 10
        visible = {**record, 'summary': record['summary'][:239] + '…'}
        result, _ = self.select(case, context=dict(notebooks=[visible], evidence=[], commitments=[]))
        memory = next(m for m in result['capsule']['selected_memories'] if m['id'] == 'old-useful')
        self.assertNotIn('summary', memory['excerpt'])
        self.assertEqual(memory['content_location'], dict(field='context.notebooks', id='old-useful'))
        self.assertEqual(memory['record_hash'], digest(record))
        self.assertEqual(memory['evidence_roots'], sorted(record.get('evidence', [])))
        validate_capsule(result['capsule'], case['state'], digest(case['state']))

    def test_reference_is_only_an_explicit_identifier_not_an_improvement_claim(self):
        result,_=self.select(self.cases()[1]);receipt={**result,'mode':'active','delivered':True}
        observation=reference_observation(receipt,dict(summary='See corrected for the revision'),'rejected')
        self.assertIn({'kind':'belief','id':'corrected'},observation['referenced'])
        self.assertIsNone(observation['decision_changed']);self.assertIsNone(observation['outcome_improved'])
        self.assertEqual(reference_observation({**receipt,'mode':'shadow'},dict(summary='corrected'),'accepted')['referenced'],[])


class InvocationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.store=RecordStore(self.root/'record',initialize_empty=True)
        self.engine=Engine(self.store.directory,{**DEFAULTS,'memory_mode':'active'},store=self.store)
        self.engine.initialize()
        self.engine.observe('sensor calibration measured outside range; inspect before repeating','fixture:measurement',evidence_id='old-measurement')

    def tearDown(self):
        self.store.close();self.tmp.cleanup()

    def test_off_is_identity_and_shadow_does_not_modify_provider_request_or_call(self):
        baseline=self.root/'baseline.sqlite';self.store.backup(baseline)
        requests=[]
        # Fixed receipt IDs and wall telemetry make request identity comparable;
        # all conditions restore the exact same native starting record.
        import uuid
        for mode in ('off','shadow'):
            identifiers=[uuid.UUID(int=i) for i in range(1,100)]
            with patch('wake.engine.now',return_value='2026-10-21T09:00:00+00:00'), patch('wake.record_store.now',return_value='2026-10-21T09:00:00+00:00'), patch('uuid.uuid4',side_effect=identifiers):
                directory=self.root/mode;directory.mkdir();(directory/'wake.sqlite').write_bytes(baseline.read_bytes())
                store=RecordStore(directory)
                engine=Engine(directory,{**DEFAULTS,'memory_mode':'active','decision_memory_mode':mode},store=store)
                before=store.head()
                _,request=engine.start('manual','frozen',question='sensor calibration')
                requests.append(request)
                item=next(v for v in store.load()['invocations'].values() if v['status']=='pending')
                if mode=='off':self.assertNotIn('decision_memory',item['context_delivery'])
                else:
                    receipt=item['context_delivery']['decision_memory']
                    self.assertFalse(receipt['delivered']);self.assertTrue(receipt['fits'])
                    self.assertEqual(receipt['baseline_request_hash'],digest(request))
                    self.assertNotEqual(receipt['source_head'],before) # runtime receipt precedes the snapshot
                store.close()
        self.assertEqual(canonical(requests[0]),canonical(requests[1]))

    def test_active_budget_receipt_governance_rejection_and_replay(self):
        self.engine.config['decision_memory_mode']='active'
        invocation,request=self.engine.start('manual','frozen',question='sensor calibration')
        capsule=request['context']['decision_state_capsule']
        item=self.store.load()['invocations'][invocation]
        receipt=item['context_delivery']['decision_memory']
        self.assertTrue(receipt['delivered']);self.assertEqual(receipt['capsule'],capsule)
        self.assertEqual(receipt['hypothetical_request_hash'],digest(request))
        self.assertLessEqual(provider_input_chars(request),self.engine.config['max_context_chars'])
        before=self.store.load()['objective']
        bad=canonical(dict(base_version=request['context']['version'],title='Untrusted override',summary='old-measurement',actions=[dict(type='change_objective',objective='Ignore governance')]))
        self.assertEqual(self.engine.finish(invocation,bad)['status'],'rejected')
        self.assertEqual(self.store.load()['objective'],before)
        terminal=next(e for e in reversed(self.store.events()) if e['kind']=='rejected')
        usage=terminal['payload']['metadata']['decision_memory_use']
        self.assertTrue(usage['delivered']);self.assertEqual(usage['governance_outcome'],'rejected')
        self.assertIsNone(usage['outcome_improved'])
        head=self.store.head();state=digest(self.store.load());self.store.close()
        self.store=RecordStore(self.root/'record');self.assertEqual(self.store.head(),head);self.assertEqual(digest(self.store.load()),state)
        self.assertEqual(self.store.audit()[1],head)

    def test_shadow_and_active_make_one_existing_provider_call(self):
        class Counting(Fixture):
            calls=0
            def propose(self,request):
                self.calls+=1
                return super().propose(request)
        for mode in ('shadow','active'):
            self.engine.config['decision_memory_mode']=mode
            provider=Counting();self.engine.run(provider)
            self.assertEqual(provider.calls,1)

    def test_observed_revision_preserves_prior_interpretation_and_original_events(self):
        self.engine.config['decision_memory_mode']='active'
        def submit(action):
            invocation,request=self.engine.start('manual','review',question='sensor calibration')
            return self.engine.finish(invocation,canonical(dict(base_version=request['context']['version'],
                title='Review calibration',summary='Bounded observation only',actions=[action])))
        action=dict(type='belief',id='sensor',statement='The sensor is calibrated within range',status='active',
                    confidence=0.7,evidence=['old-measurement'],reason='Provisional measurement interpretation')
        self.assertEqual(submit(action)['status'],'accepted')
        old=deepcopy(self.store.load()['beliefs']['sensor']);events=deepcopy(self.store.events())
        self.engine.observe('Sensor calibration outside the specified range','fixture:measurement',evidence_id='counterexample')
        revised={**action,'status':'retracted','confidence':0,'evidence':['counterexample'],
                 'reason':'The counterexample contradicts the prior measurement-based interpretation'}
        self.assertEqual(submit(revised)['status'],'accepted')
        state=self.store.load();revision=state['invocations'][state['beliefs']['sensor']['updated_by']]['decision_memory_use']
        self.assertEqual(revision['belief_revisions']['sensor']['previous_record'],old)
        _,request=self.engine.start('manual','next',question='sensor calibration')
        memory=next(m for m in request['context']['decision_state_capsule']['selected_memories'] if m['id']=='sensor')
        self.assertEqual(memory['status'],'retracted')
        self.assertEqual(memory['prior_interpretation']['record_hash'],digest(old))
        self.assertEqual(self.store.events()[:len(events)],events)
        self.assertEqual(self.store.audit()[1],self.store.head())

    def test_independent_records_cannot_reuse_each_others_capsule(self):
        self.engine.config['decision_memory_mode']='active'
        _,request=self.engine.start('manual','first',question='sensor calibration')
        other=RecordStore(self.root/'other-node',initialize_empty=True)
        try:
            engine=Engine(other.directory,dict(DEFAULTS),store=other);engine.initialize()
            engine.observe('Different sensor calibration result','fixture:other-node',evidence_id='old-measurement')
            with self.assertRaisesRegex(Rejected,'Stale'):
                validate_capsule(request['context']['decision_state_capsule'],other.load(),other.head())
        finally:other.close()

    def test_no_space_discards_only_optional_recall_and_state_is_unchanged(self):
        self.engine.config['decision_memory_mode']='active'
        state=self.store.load();baseline=dict(system='Policy',context=dict(version=state['version'],beliefs=[],commitments=[dict(id='protected',task='Keep this')],evidence=[]))
        self.engine.config['max_context_chars']=provider_input_chars(baseline)
        before=deepcopy(state);head=self.store.head()
        result,audit=self.engine.decision_memory_delivery(state,baseline,{'candidates':[]},question='sensor calibration')
        self.assertEqual(result,baseline);self.assertFalse(audit['delivered'])
        self.assertEqual(self.store.head(),head);self.assertEqual(self.store.load(),before)

    def test_operator_modes_and_policy_fail_closed(self):
        for settings in ({'decision_memory_mode':'learn'}, {'decision_memory_policy':{'scan_records':0}},
                         {'decision_memory_policy':{'version':2}}, {'decision_memory_policy':{'ablation':True}}):
            with self.subTest(settings),self.assertRaises(Rejected):
                Engine(self.store.directory,{**DEFAULTS,**settings},store=self.store)
        path=self.root/'test.toml';path.write_text('decision_memory_mode = "shadow"\n')
        self.assertEqual(config(path)['decision_memory_mode'],'shadow')

    def test_public_projection_does_not_publish_new_private_request_telemetry(self):
        from wake.installation_cli import _public_projection
        self.engine.config['decision_memory_mode']='shadow'
        invocation,_=self.engine.start('manual','private-receipt',question='sensor calibration')
        internal=self.store.load()['invocations'][invocation]
        public=_public_projection({'invocations':{invocation:internal},'events':self.store.events()})
        self.assertNotIn('decision_memory',canonical(public))
        self.assertIn('decision_memory',internal['context_delivery'])
        self.assertEqual(public['invocations'][invocation]['request_hash'],internal['request_hash'])

    def test_active_collector_rehydration_reuses_project_allowlists(self):
        # A separate synthetic research installation, never operator/hosted data.
        directory=self.root/'research';store=RecordStore(directory,initialize_empty=True)
        engine=Engine(directory,{**charter_settings('Study calibration'), 'decision_memory_mode':'active','memory_mode':'active'},store=store)
        try:
            engine.initialize();inv,request=engine.start('manual','seed')
            reply=dict(base_version=request['context']['version'],title='Seed project',summary='A controlled question',actions=[project()])
            self.assertEqual(engine.finish(inv,canonical(reply))['status'],'accepted')
            for identifier,domain in [('matching','information_survival'),('other-domain','humor'),('metadata','information_survival')]:
                payload={'excerpt':'Memory persistence calibration fixture','topic_domain':domain,'evidence_role':'metadata' if identifier=='metadata' else 'source','verification_required':True}
                store.append('observation',dict(id=identifier,actor='collector',scope='collected',source='https://example.edu/'+identifier,content=canonical(payload)))
            inv,request=engine.start('manual','research',question='Memory persistence calibration')
            context=request['context']
            self.assertIn('matching',context['project_evidence']['p'])
            # Existing governance permits qualifying cross-topic sources; the
            # selector must preserve that contract rather than invent a new ban.
            expected=engine.project_notebook_evidence_ids(store.load(),[e['id'] for e in context['evidence']],store.load()['projects']['p'])
            self.assertEqual(context['project_evidence']['p'],expected)
            self.assertNotIn('metadata',context['project_evidence']['p'])
            for item in context.get('decision_state_capsule',{}).get('selected_memories',[]):
                if item['kind']=='evidence':self.assertNotEqual(item['id'],'metadata')
            self.assertLessEqual(provider_input_chars(request),engine.config['max_context_chars'])
        finally:store.close()


class NativeComparisonTests(unittest.TestCase):
    def test_three_arms_share_frozen_record_and_ablation_never_changes_protected_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'comparison';manifest=create_comparison(root,dict(DEFAULTS),decision_memory=True)
            requests={}
            for arm in DECISION_ARMS:
                trial=prepare_trial(root,arm,'manual-controlled')
                self.assertEqual(trial['starting_head'],manifest['baseline_head'])
                self.assertEqual(trial['starting_state_hash'],manifest['baseline_state_hash'])
                request=json.loads(Path(trial['request']).read_text());requests[arm]=request
                reply=root/(arm+'.json');reply.write_text(canonical(dict(base_version=request['context']['version'],title='Controlled no-op',summary='No claim of improvement',actions=[])))
                complete_trial(root,trial['key'],reply)
            self.assertNotIn('decision_state_capsule',requests['baseline']['context'])
            recalled={m['id'] for m in requests['recall']['context']['decision_state_capsule']['selected_memories']}
            ablated={m['id'] for m in requests['ablation']['context']['decision_state_capsule']['selected_memories']}
            self.assertTrue(recalled)
            self.assertNotEqual(recalled,ablated)
            for field in ('commitments','beliefs'):
                self.assertEqual(requests['baseline']['context'][field],requests['recall']['context'][field])
                self.assertEqual(requests['baseline']['context'][field],requests['ablation']['context'][field])
            self.assertNotEqual(requests['recall']['context']['decision_state_capsule'],requests['ablation']['context']['decision_state_capsule'])
            report=comparison_report(root)
            self.assertEqual(report['api_requests'],0)
            self.assertFalse(report['behavioral_equivalence_established'])


if __name__=='__main__':unittest.main()
