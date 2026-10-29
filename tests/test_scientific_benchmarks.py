"""Synthetic fixtures validate causal mechanics; they are not discovery evidence."""
from copy import deepcopy
import json
import re
import unittest

from test_scientific_research import ScientificFixtureCase, hypothesis, protocol
from wake.science import contracts as c
from wake.science.correction import prepare, cases
from wake.science.hidden_system import observations
from wake.science.workbench import DockerWorkbench, advance
from wake.science.projection import project, write_report


class CorrectionProviderFixture:
    name='fixture';model='history-reader';charged=False
    def __init__(self):self.requests=[]
    def propose(self,request):
        self.requests.append(deepcopy(request))
        context=request['context'];task=context['task'];history=context['historical_observations']
        numbers=list(map(int,re.findall(r'-?\d+',task)))
        proposed=int(re.search(r'Proposed (?:corrected )?answer: (-?\d+)',task).group(1))
        answer=proposed
        if task.startswith('Compute'):answer=numbers[0]+numbers[1]
        elif 'each unit' in task:answer=numbers[0]*numbers[1]
        elif 'revision 2 uses' in task:answer=numbers[0]+int(re.search(r'revision 2 uses \+(\d+)',task).group(1))
        elif history:
            relevant=next(h for h in history if h['id'].endswith('verified'))
            offset=int(re.findall(r'-?\d+',relevant['text'])[-1])
            answer=numbers[0]-offset if 'subtract' in relevant['text'] else numbers[0]+offset
        evidence=[h['id'] for h in history if h['id'].endswith('verified') and not task.startswith('Compute')]
        return json.dumps({'answer':answer,'error_detected':answer!=proposed,'corrected':answer!=proposed,'evidence':evidence}),{'fixture':True}


class ScientificBenchmarkTests(ScientificFixtureCase):
    def test_trial_calls_obey_frozen_model_native_daily_limit(self):
        p=protocol('def experiment(inputs):\n return inputs["trials"]')
        p.update(instrument='model-comparison',evaluator={'id':'historical-correction@1'},
                 inputs={'cases_per_seed':6},seeds=[64],budget={'seconds':20,'provider_calls':18})
        self.assertEqual(self.submit([self.action('hypothesis','h-sort',hypothesis()),
            self.action('experiment','bounded-trial',p)])['status'],'accepted')
        provider=CorrectionProviderFixture();provider.charged=True
        provider.config={'model_daily_call_limits':{provider.model:1}}
        result=advance(self.engine.store,DockerWorkbench(provider,self.engine.store))
        self.assertEqual(result['status'],'failed')
        self.assertEqual(len(provider.requests),1)
        state,_=self.engine.store.audit()
        self.assertEqual(len(state['science']['experiments']['bounded-trial']['attempts'][0]['inference']),1)
        self.assertNotIn('evaluation',state['science']['experiments']['bounded-trial'])
        from wake.providers import ConfiguredDailyLimitReached
        class ParentBudgetGuard(CorrectionProviderFixture):
            charged=True;record_attempt=None;provider_requests_sent=0
            models=['history-reader'];request_limit=1;model_request_limits=None
            def propose(inner,request):
                self.assertEqual(inner.model_request_limits,{'history-reader':0})
                raise ConfiguredDailyLimitReached('Fixture daily cap; no provider effect')
        self.engine.config.update(free_tier_confirmed=True,model_daily_call_limits={'history-reader':1})
        self.assertEqual(self.engine.run(ParentBudgetGuard())['status'],'deferred')
        from wake.science.projection import project
        from wake.research_projection import build_research_projection
        state,head=self.engine.store.audit()
        public=build_research_projection(state,self.engine.store.events(),head)
        self.assertEqual(public['metrics']['provider_trial_requests'],1)
        legacy=deepcopy(state)
        legacy['science']['experiments']['bounded-trial']['attempts'][0]['receipt'].pop('wall_seconds')
        metrics=project(legacy)['metrics']
        self.assertIsNone(metrics['execution_seconds'])
        self.assertEqual(metrics['unknown_execution_durations'],1)

    def test_interrupted_child_trial_retains_responses_and_never_replays_effects(self):
        class InterruptedProvider(CorrectionProviderFixture):
            charged=True
            def propose(self,request):
                if len(self.requests)==1:raise SystemExit('Injected process termination during trial two')
                return super().propose(request)
        p=protocol('def experiment(inputs):\n return inputs["trials"]')
        p.update(instrument='model-comparison',evaluator={'id':'historical-correction@1'},
                 inputs={'cases_per_seed':6},seeds=[64],budget={'seconds':20,'provider_calls':18})
        self.assertEqual(self.submit([self.action('hypothesis','h-sort',hypothesis()),
            self.action('experiment','interrupted-comparison',p)])['status'],'accepted')
        provider=InterruptedProvider();runner=DockerWorkbench(provider,self.engine.store)
        with self.assertRaises(SystemExit):advance(self.engine.store,runner)
        item=self.engine.store.load()['science']['experiments']['interrupted-comparison']
        self.assertEqual([t['status'] for t in item['attempts'][0]['inference']],['completed','started'])
        self.assertEqual(advance(self.engine.store,runner)['status'],'interrupted')
        self.assertIsNone(advance(self.engine.store,runner))
        self.assertEqual(len(provider.requests),1)
        self.engine.store.recover_invocation_lifecycles()
        state,_=self.engine.store.audit()
        self.assertNotIn('evaluation',state['science']['experiments']['interrupted-comparison'])
        from wake.provider_pacing import native_usage, PACIFIC
        from datetime import datetime
        day=datetime.fromisoformat(item['attempts'][0]['started']).astimezone(PACIFIC).date().isoformat()
        self.assertEqual(native_usage(state,day)[1],{'history-reader':2})
        from wake.provider_pacing import scientific_request_totals
        self.assertEqual(scientific_request_totals(state),(1,1))

    def test_hidden_system_negative_then_fixture_revision_and_fresh_holdout(self):
        for instance in (17,81,304):
            h=hypothesis();hid=f'h-{instance}';eid=f'e-{instance}'
            h['statement']='Initial observations support a linear response beyond the observed interval.'
            p=protocol('''def experiment(inputs):
 a,b=inputs['observations'][0],inputs['observations'][-1]
 m=(b['y']-a['y'])/(b['x']-a['x']);c=a['y']-m*a['x']
 return {'probe_predictions':[m*x+c for x in inputs['probes']], 'holdout_predictions':[m*r['x']+c for r in inputs['holdout']]}
''')
            p.update(hypothesis=hid,inputs={'instance':instance,'probes':[3,4,5],'holdout_size':12},seeds=[instance+1000],evaluator={'id':'hidden-relationship@1'})
            self.assertEqual(self.submit([self.action('hypothesis',hid,h),self.action('experiment',eid,p)])['status'],'accepted')
            runner=DockerWorkbench();advance(self.engine.store,runner)
            result=advance(self.engine.store,runner)['evaluation']
            self.assertEqual(result['outcome'],'contradicted')
            self.assertFalse(result['measurement_details']['holdout_labels_disclosed'])
            # This revision is deliberately scripted for deterministic acceptance;
            # live-model discovery must be demonstrated separately.
            obs=result['measurement_details']['observations']
            initial=observations(instance);slope=(initial[-1]['y']-initial[0]['y'])/4;intercept=initial[1]['y']
            bend=obs[0]['observed']-slope*3-intercept
            revised=deepcopy(h);revised.update(supersedes=1,statement='A scripted piecewise quadratic fixture predicts unseen inputs.',provenance=[eid])
            p2=deepcopy(p);p2.update(revision=2,seeds=[instance+2000],source=f'''def experiment(inputs):
 def f(x):return {slope}*x+{intercept}+{bend}*max(0,x-2)**2
 return {{'probe_predictions':[f(x) for x in inputs['probes']], 'holdout_predictions':[f(r['x']) for r in inputs['holdout']]}}
''')
            self.assertEqual(self.submit([self.action('hypothesis',hid,revised),self.action('experiment',eid+'-revision',p2)])['status'],'accepted')
            advance(self.engine.store,runner);result=advance(self.engine.store,runner)['evaluation']
            self.assertEqual(result['outcome'],'provisionally_supported')
            stale=deepcopy(p2)
            self.assertEqual(self.submit([self.action('experiment',eid+'-stale',stale)])['status'],'rejected')
        state,head=self.engine.store.audit();audit=project(state,head)
        self.assertEqual(audit['metrics']['verified_hypothesis_revisions'],3)
        self.assertEqual(audit['metrics']['contradicted_predictions'],3)
        write_report(audit,self.root/'audit.html')
        self.assertIn('Independent evaluation',(self.root/'audit.html').read_text())
        self.assertNotIn('oracle_digest',json.dumps(audit))

    def test_paired_correction_runs_real_preparation_and_independent_scoring(self):
        p=protocol('def experiment(inputs):\n return {"trials":inputs["trials"]}')
        p.update(instrument='model-comparison',evaluator={'id':'historical-correction@1'},
                 inputs={'cases_per_seed':6},seeds=[64],budget={'seconds':20,'provider_calls':18})
        h=hypothesis();h['statement']='Relevant history improves accuracy over the paired no-history condition.'
        h['predictions']=[{'metric':'accuracy_gain_B_over_A','operator':'gte','value':.3,'tolerance':0}]
        self.assertEqual(self.submit([self.action('hypothesis','h-sort',h),self.action('experiment','correction',p)])['status'],'accepted')
        provider=CorrectionProviderFixture()
        provider.models=[provider.model,'fixture-second-model'];provider.successful_model='fixture-second-model'
        runner=DockerWorkbench(provider,self.engine.store)
        execution=advance(self.engine.store,runner)
        self.assertEqual(execution['status'],'completed',self.engine.store.load()['science']['experiments']['correction']['attempts'][-1].get('receipt'))
        result=advance(self.engine.store,runner)['evaluation']
        self.assertEqual(result['outcome'],'provisionally_supported')
        self.assertEqual(result['metrics']['B_accuracy'],1)
        self.assertEqual(result['metrics']['C_accuracy'],1)
        self.assertEqual(result['metrics']['A_accuracy'],.5)
        self.assertEqual(len(provider.requests),18)
        self.assertTrue(all('expected' not in r['context'] for r in provider.requests))
        state,head=self.engine.store.audit()
        trials=state['science']['experiments']['correction']['attempts'][0]['inference']
        self.assertEqual(len(trials),18)
        self.assertTrue(all(t['status']=='completed' for t in trials))
        self.assertTrue(all(t['model']=='fixture-second-model' for t in trials))
        self.assertEqual(provider.model,'history-reader')
        for trial in trials:
            self.assertEqual(self.engine.store.invocation_history(trial['invocation'])[-1]['stage'],'completed')

    def test_preparation_cannot_modify_conditions_or_spend_extra_calls(self):
        p=protocol('def experiment(inputs):\n return []')
        p.update(instrument='model-comparison',evaluator={'id':'historical-correction@1'},inputs={'cases_per_seed':6},
                 seeds=[1],budget={'seconds':20,'provider_calls':18})
        self.assertEqual(self.submit([self.action('hypothesis','h-sort',hypothesis()),self.action('experiment','bad-preparation',p)])['status'],'accepted')
        provider=CorrectionProviderFixture()
        result=advance(self.engine.store,DockerWorkbench(provider,self.engine.store))
        self.assertEqual(result['status'],'failed');self.assertEqual(provider.requests,[])
        p['budget']['provider_calls']=17
        with self.assertRaises(ValueError):prepare(p)

    def test_relevant_information_and_pairing_survive_compression(self):
        p=protocol();p.update(instrument='model-comparison',evaluator={'id':'historical-correction@1'},
            inputs={'cases_per_seed':6},seeds=[64],budget={'seconds':20,'provider_calls':18})
        inputs,protected=prepare(p)
        rows=inputs['trials'];self.assertEqual(len(rows),18)
        self.assertEqual(len({r['family'] for r in rows}),6)
        for case in cases(64):
            self.assertTrue(set(case['relevant'])<=set(h['id'] for h in case['compressed']))
        self.assertEqual(prepare(p),(inputs,protected))
