"""Native governance, frozen protocols, real instruments and honest scientific outcomes."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from wake.autonomous_demo import settings, seed
from wake.engine import Engine
from wake.record_store import RecordStore
from wake.governance import Rejected
from wake.event_format import digest
from wake.science import contracts as c
from wake.science.workbench import advance, DockerWorkbench
from wake.science.instruments import evaluate


def hypothesis():
    return {'schema':c.HYPOTHESIS,'kind':'empirical','statement':'The candidate correctly sorts the seeded integer arrays.',
            'assumptions':['Finite integer arrays within the prespecified bounds.'],
            'predictions':[{'metric':'accuracy','operator':'eq','value':1,'tolerance':0}],
            'falsification':'Any returned sequence differs from the independently sorted input.',
            'provenance':[],'uncertainty':'Finite test cases cannot prove correctness for arbitrary inputs.'}


def protocol(source='def experiment(inputs):\n return [sorted(t["values"]) for t in inputs["trials"]]'):
    return {'schema':c.PROTOCOL,'hypothesis':'h-sort','revision':1,'method':'Paired checks against a withheld exact oracle.',
            'instrument':'python','source':source,'inputs':{'cases_per_seed':4,'length':8,'magnitude':100},
            'seeds':[13,71,43], 'evaluator':{'id':'sort-correctness@1'},
            'success':'All finite cases match the independent exact answer.',
            'stop':'Close after this finite comparison or suspend on execution failure.',
            'budget':{'seconds':20,'provider_calls':0}}


class RecordedWorkbench:
    """Transport fixture for governance tests, explicitly not execution-isolation evidence."""
    def __init__(self, bad=False):
        self.bad=bad
        self.calls=0
    def environment(self):
        return {'image_id':'fixture-transport','fixture':True}
    def execute(self,item):
        self.calls+=1
        values=item['attempts'][-1]['execution_inputs']['trials']
        return {'status':'completed','outputs':[[] if self.bad else sorted(t['values']) for t in values], 'wall_seconds':0}
    def cleanup(self,names):
        pass


class ScientificFixtureCase(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.engine=Engine(self.root/'record',{**settings(),'experimental_research_enabled':True},store=RecordStore(self.root/'record',initialize_empty=True))
        self.addCleanup(self.engine.store.close)
        self.engine.initialize();seed(self.engine)
        advance(self.engine.store,RecordedWorkbench(),enabled=True)
    def submit(self,actions):
        invocation,request=self.engine.start('fixture','scientific-contract-test')
        return self.engine.finish(invocation,json.dumps({'base_version':request['context']['version'],
            'title':'Scientific protocol fixture','summary':'Synthetic contract test; no live model behavior claimed.','actions':actions}))
    def action(self,kind,identifier,definition):
        return {'type':kind,'id':identifier,'project':'a','definition':json.dumps(definition)}
    def propose(self,source=None):
        p=protocol() if source is None else protocol(source)
        result=self.submit([self.action('hypothesis','h-sort',hypothesis()),self.action('experiment','e-sort',p)])
        self.assertEqual(result['status'],'accepted',result)


class ScientificResearchTests(ScientificFixtureCase):
    def test_convergence_uses_current_revision_evidence_and_retains_uncertainty(self):
        from wake.science.planner import convergence
        self.propose()
        def signal():
            science=self.engine.store.load()['science']
            return convergence(science,science['hypotheses']['h-sort'])
        self.assertEqual(signal()['stage'],'awaiting_execution_or_evaluation')
        runner=RecordedWorkbench(bad=True);advance(self.engine.store,runner);advance(self.engine.store,runner)
        self.assertEqual(signal()['stage'],'contradiction_requires_explanation_or_revision')
        revised=hypothesis();revised['supersedes']=1
        self.assertEqual(self.submit([self.action('hypothesis','h-sort',revised)])['status'],'accepted')
        self.assertEqual(signal()['stage'],'test_design_needed')
        self.assertTrue(signal()['remaining_uncertainty'])

    def test_protocol_frozen_revision_and_replayed_native_history(self):
        self.propose();before=deepcopy(self.engine.store.load()['science'])
        changed=protocol();changed['success']='Make it look good after seeing the answer.'
        self.assertEqual(self.submit([self.action('experiment','e-sort',changed)])['status'],'rejected')
        self.assertEqual(before,self.engine.store.load()['science'])
        revision=hypothesis();revision['supersedes']=1;revision['statement']='Revised claim with narrower coverage.'
        self.assertEqual(self.submit([self.action('hypothesis','h-sort',revision)])['status'],'accepted')
        state=self.engine.store.load()['science'];self.assertEqual(len(state['hypotheses']['h-sort']['revisions']),2)
        self.assertEqual(state['experiments']['e-sort']['predictions'],hypothesis()['predictions'])
        self.assertEqual(self.engine.store.audit()[0],self.engine.store.load())
    def test_negative_result_cannot_be_overwritten_by_interpretation(self):
        self.propose();runner=RecordedWorkbench(bad=True)
        self.assertEqual(advance(self.engine.store,runner)['status'],'completed')
        result=advance(self.engine.store,runner);self.assertEqual(result['evaluation']['outcome'],'contradicted')
        self.assertEqual(result['evaluation']['measurement_validity'],'validated')
        interpretation={'experiment':'e-sort','interpretation':'This contradicts our prediction.',
                        'limitations':'Finite fixture only.','next_step':'Try a corrected algorithm on fresh arrays.'}
        self.assertEqual(self.submit([self.action('experiment_interpretation','i-sort',interpretation)])['status'],'accepted')
        self.assertEqual(self.engine.store.load()['science']['hypotheses']['h-sort']['status'],'contradicted')
        self.assertEqual(runner.calls,1)
        self.assertEqual(self.engine.store.audit()[0],self.engine.store.load())
    def test_failed_execution_is_not_scientific_contradiction(self):
        self.propose();runner=RecordedWorkbench()
        runner.execute=lambda item:{'status':'failed','reason':'Synthetic execution failure'}
        self.assertEqual(advance(self.engine.store,runner)['status'],'failed')
        self.assertIsNone(advance(self.engine.store,runner))
        self.assertEqual(self.engine.store.load()['science']['hypotheses']['h-sort']['status'],'untested')
    def test_restart_cleans_exact_attempt_without_duplicate_effect(self):
        self.propose();runner=RecordedWorkbench()
        with self.assertRaises(InterruptedError):advance(self.engine.store,runner,crash_at='after-execution')
        self.assertEqual(runner.calls,1)
        self.assertEqual(advance(self.engine.store,runner)['status'],'interrupted')
        self.assertEqual(runner.calls,1)
        self.assertEqual(self.engine.store.audit()[0],self.engine.store.load())
    def test_failed_durability_barrier_prevents_execution(self):
        self.propose();runner=RecordedWorkbench()
        def fail():raise OSError('Synthetic checkpoint failure')
        with self.assertRaises(OSError):advance(self.engine.store,runner,checkpoint=fail)
        self.assertEqual(runner.calls,0)
        self.assertEqual(advance(self.engine.store,runner)['status'],'interrupted')
    def test_unknown_capability_blocks_without_host_fallback(self):
        self.propose();s=self.engine.store.load()
        # Use a fresh native proposal rather than editing its stored protocol.
        p=protocol();p['instrument']='unavailable-service'
        self.assertEqual(self.submit([self.action('experiment','e-blocked',p)])['status'],'accepted')
        runner=RecordedWorkbench();advance(self.engine.store,runner);advance(self.engine.store,runner)
        result=advance(self.engine.store,runner)
        self.assertEqual(result['status'],'blocked');self.assertEqual(runner.calls,1)
    def test_model_cannot_grant_capability_or_submit_execution_receipts(self):
        for kind in ['scientific_configured','experiment_started','experiment_executed','experiment_evaluated']:
            self.assertEqual(self.submit([self.action(kind,'forged',{})])['status'],'rejected')
        p=protocol();p['evaluation']={'outcome':'supported'}
        self.assertEqual(self.submit([self.action('hypothesis','h-sort',hypothesis()),self.action('experiment','e-forged',p)])['status'],'rejected')
        self.assertNotIn('h-sort',self.engine.store.load()['science']['hypotheses'])
    def test_independent_replication_is_separate_and_exact(self):
        self.propose();runner=RecordedWorkbench();advance(self.engine.store,runner);advance(self.engine.store,runner)
        p=protocol();p['replicates']='e-sort'
        self.assertEqual(self.submit([self.action('experiment','e-replicate',p)])['status'],'accepted')
        advance(self.engine.store,runner)
        result=advance(self.engine.store,runner)
        self.assertEqual(result['evaluation']['replication_status'],'replicated')
        self.assertEqual(runner.calls,2)
    def test_reference_only_replication_reconstructs_the_exact_native_protocol(self):
        self.propose();runner=RecordedWorkbench();advance(self.engine.store,runner);advance(self.engine.store,runner)
        reference={'schema':c.PROTOCOL,'replicates':'e-sort'}
        self.assertEqual(self.submit([self.action('experiment','reference-replication',reference)])['status'],'accepted')
        advance(self.engine.store,runner);result=advance(self.engine.store,runner)['evaluation']
        self.assertEqual(result['replication_status'],'replicated')
        state=self.engine.store.load()['science']['experiments']
        self.assertEqual(state['e-sort']['protocol']['source_digest'],state['reference-replication']['protocol']['source_digest'])
    def test_invalid_and_unvalidated_measurements_remain_distinct(self):
        self.propose();runner=RecordedWorkbench();runner.execute=lambda item:{'status':'completed','outputs':{'not':'a measurement'}}
        advance(self.engine.store,runner)
        self.assertEqual(advance(self.engine.store,runner)['evaluation']['outcome'],'invalid_measurement')
        p=protocol('def experiment(inputs):\n return {"measurements":{"accuracy":[1,1,1]}}')
        p['evaluator']={'id':'numeric-observation@1'};p['inputs']={}
        self.assertEqual(self.submit([self.action('experiment','e-unvalidated',p)])['status'],'accepted')
        runner.execute=lambda item:{'status':'completed','outputs':{'measurements':{'accuracy':[1,1,1]}}}
        advance(self.engine.store,runner);r=advance(self.engine.store,runner)['evaluation']
        self.assertEqual(r['outcome'],'inconclusive');self.assertEqual(r['measurement_validity'],'unvalidated')
    def test_real_docker_computation_and_native_scoring(self):
        self.propose();runner=DockerWorkbench()
        try:runner.environment()
        except (ValueError,OSError):self.skipTest('Reviewed Docker image unavailable')
        self.assertEqual(advance(self.engine.store,runner)['status'],'completed')
        report=advance(self.engine.store,runner)['evaluation']
        self.assertEqual(report['metrics']['accuracy'],1)
        self.assertEqual(report['outcome'],'provisionally_supported')
        item=self.engine.store.load()['science']['experiments']['e-sort']
        self.assertNotIn('expected',item['attempts'][0]['execution_inputs'])
        self.assertEqual(self.engine.store.audit()[0],self.engine.store.load())

    def test_replayed_receipt_cannot_complete_a_new_reserved_attempt(self):
        self.propose();runner=RecordedWorkbench();advance(self.engine.store,runner);advance(self.engine.store,runner)
        old=self.engine.store.load()['science']['experiments']['e-sort']['attempts'][-1]['receipt']
        p=protocol();p['replicates']='e-sort'
        self.assertEqual(self.submit([self.action('experiment','e-replay',p)])['status'],'accepted')
        with self.assertRaises(InterruptedError):advance(self.engine.store,runner,crash_at='before-execution')
        state=self.engine.store.load();item=state['science']['experiments']['e-replay'];attempt=item['attempts'][-1]
        forged=deepcopy(old);forged['protocol_digest']=item['protocol']['protocol_digest']
        forged['environment_digest']=digest(item['review']['environment'])
        with self.assertRaises(ValueError):
            self.engine.store.append('experiment_executed',{'schema':c.SCHEMA,'base_version':state['version'],
                'id':item['id'],'protocol_digest':item['protocol']['protocol_digest'],'attempt':attempt['id'],'receipt':forged})
        self.assertEqual(self.engine.store.load()['science']['experiments']['e-replay']['status'],'running')
        advance(self.engine.store,runner)

    def test_forged_evaluation_cannot_replace_a_negative_result(self):
        self.propose();runner=RecordedWorkbench(bad=True);advance(self.engine.store,runner)
        state=self.engine.store.load();item=state['science']['experiments']['e-sort']
        forged=evaluate(item);forged['outcome']='provisionally_supported'
        with self.assertRaises(ValueError):
            self.engine.store.append('experiment_evaluated',{'schema':c.SCHEMA,'base_version':state['version'],
                'id':item['id'],'protocol_digest':item['protocol']['protocol_digest'],
                'attempt':item['attempts'][-1]['id'],'evaluation':forged})
        self.assertEqual(advance(self.engine.store,runner)['evaluation']['outcome'],'contradicted')

    def test_later_support_does_not_erase_an_unrevised_contradiction(self):
        self.propose();runner=RecordedWorkbench(bad=True);advance(self.engine.store,runner);advance(self.engine.store,runner)
        p=protocol();p['seeds']=[101]
        self.assertEqual(self.submit([self.action('experiment','favorable',p)])['status'],'accepted')
        runner.bad=False;advance(self.engine.store,runner)
        self.assertEqual(advance(self.engine.store,runner)['evaluation']['outcome'],'provisionally_supported')
        self.assertEqual(self.engine.store.load()['science']['hypotheses']['h-sort']['status'],'contradicted')

class ScientificPlannerFixture:
    """Scripted research provider: tests orchestration, never claimed as discovery."""
    name='fixture'
    model='scientific-planner-a'
    charged=False
    def __init__(self):self.requests=[]
    def propose(self,request):
        self.requests.append(deepcopy(request))
        science=request['context']['scientific_research']
        experiments={e['id']:e for e in science['experiments']}
        def action(kind,identifier,value):return {'type':kind,'id':identifier,'project':'a','definition':json.dumps(value)}
        if not experiments:
            p=protocol('def experiment(inputs):\n return [t["values"] for t in inputs["trials"]]')
            actions=[action('hypothesis','h-sort',hypothesis()),action('experiment','e-sort',p)]
        elif experiments.get('e-sort',{}).get('evaluation',{}).get('outcome')=='contradicted' and 'e-revised' not in experiments:
            h=hypothesis();h.update(supersedes=1,statement='An explicitly sorted candidate corrects the observed ordering errors.',provenance=['e-sort'])
            p=protocol();p.update(revision=2,seeds=[101,203,307])
            actions=[action('experiment_interpretation','i-negative',{'experiment':'e-sort','interpretation':'The unsorted output contradicted the frozen prediction.',
                'limitations':'Synthetic arrays; general correctness remains unresolved.','next_step':'Compare a revised algorithm on fresh seeds.'}),
                action('hypothesis','h-sort',h),action('experiment','e-revised',p)]
        else:
            actions=[action('investigation_decision','close-finite-test',{'hypothesis':'h-sort','decision':'close',
                'uncertainty':'Arbitrary inputs and scaling remain untested.','reason':'The prespecified finite comparison completed.',
                'next_experiment':'','cost':'No further fixture calls.','stop_condition':'Close this finite investigation without claiming general correctness.'})]
        return json.dumps({'base_version':request['context']['version'],'title':'Fixture experimental next step',
                           'summary':'Deterministic orchestration test; not live scientific discovery.','actions':actions}),{'fixture':True}


class AlternatePlannerFixture:
    """Separate JSON transport implementation, not a vendor claim."""
    name='alternate-fixture'
    model='scientific-planner-b'
    charged=False
    def propose(self,request):
        payload={'base_version':request['context']['version'],'title':'Independent fixture transport',
            'summary':'A distinct implementation exercises the same governed scientific contract.',
            'actions':[{'type':'hypothesis','id':'h-alternate','project':'a','definition':json.dumps(hypothesis())}]}
        return json.dumps(payload),{'fixture':True}


class ScientificIntegrationTests(ScientificFixtureCase):
    def test_scientific_contract_and_negative_evidence_fit_the_hosted_context_budget(self):
        from wake.providers import provider_input_budget
        self.propose();runner=RecordedWorkbench(bad=True)
        advance(self.engine.store,runner);advance(self.engine.store,runner)
        self.engine.config['max_context_chars']=48000
        invocation,request=self.engine.start('fixture','bounded-scientific-revision')
        self.assertGreaterEqual(provider_input_budget(request,48000)['remaining_chars'],0)
        science=request['context']['scientific_research']
        self.assertEqual(science['hypotheses'][0]['id'],'h-sort')
        self.assertEqual(science['experiments'][0]['evaluation']['outcome'],'contradicted')
        self.engine.finish(invocation,'{}')

    def test_ordinary_wakes_execute_negative_revision_and_positive_followup(self):
        provider=ScientificPlannerFixture()
        results=[]
        for _ in range(6):results.append(self.engine.run(provider))
        self.assertEqual([r['status'] for r in results],['accepted','experiment_completed','experiment_evaluated',
                                                       'accepted','experiment_completed','experiment_evaluated'])
        state=self.engine.store.load()
        self.assertEqual(state['science']['experiments']['e-sort']['evaluation']['outcome'],'contradicted')
        self.assertEqual(state['science']['experiments']['e-revised']['evaluation']['outcome'],'provisionally_supported')
        self.assertEqual(len(provider.requests),2)
        for request in provider.requests:
            context=request['context']['scientific_research']
            self.assertTrue(context['enabled'])
            self.assertNotIn('\"protected\":',json.dumps(context))
            kinds=[choice['properties']['type']['enum'][0] for choice in request['response_schema']['properties']['actions']['items']['anyOf']]
            self.assertIn('experiment',kinds)
        self.assertEqual(self.engine.store.audit()[0],state)
    def test_two_distinct_provider_implementations_deliver_the_same_contract(self):
        for provider in (ScientificPlannerFixture(),AlternatePlannerFixture()):
            # Each implementation supplies a real proposal through the ordinary
            # invocation boundary. Neither is live cross-vendor evidence.
            result=self.engine.run(provider)
            if result.get('scientific_research'):
                self.engine.run(provider)
                result=self.engine.run(provider)
            self.assertEqual(result['status'],'accepted',result)
        self.assertIn('h-alternate',self.engine.store.load()['science']['hypotheses'])
