"""Explicitly scripted benchmark providers. No live discovery claim is permitted."""
import json
import re

from . import contracts as c


class BenchmarkFixture:
    name='fixture'
    model='scripted-scientific-pipeline@1'
    charged=False

    def __init__(self,benchmark,instance):
        self.benchmark=benchmark;self.instance=instance

    def propose(self,request):
        context=request['context']
        if 'historical_observations' in context:return self.correct(context),{'fixture':True}
        science=context['scientific_research']
        experiments={e['id']:e for e in science['experiments']}
        def action(kind,key,definition):return {'type':kind,'id':key,'project':'investigation','definition':definition}
        h={'schema':c.HYPOTHESIS,'kind':'empirical','statement':'The scripted candidate predicts held-out instrument responses.',
           'assumptions':['A deterministic synthetic instrument; this is a pipeline fixture.'],
           'predictions':[{'metric':'accuracy','operator':'eq','value':1,'tolerance':0}],
           'falsification':'Any disagreement with the independent instrument response.','provenance':[],
           'uncertainty':'Scripted synthetic finite tests do not establish autonomous discovery or a natural law.'}
        p={'schema':c.PROTOCOL,'hypothesis':'fixture-hypothesis','revision':1,
           'method':'Freeze predictions, execute isolated prediction code, score independently.',
           'instrument':'python','source':'','inputs':{'instance':self.instance,'probes':[3,4,5,8],'holdout_size':12},
           'seeds':[self.instance+1000], 'evaluator':{'id':'hidden-relationship@1'},
           'success':'Every held-out prediction agrees with the independent oracle.',
           'stop':'Stop the finite fixture after revision and exact independent replication.',
           'budget':{'seconds':20,'provider_calls':0}}
        if self.benchmark=='correction':
            h.update(statement='Relevant historical observations improve correction accuracy in this finite paired task family.',
                predictions=[{'metric':'accuracy_gain_B_over_A','operator':'gte','value':.25,'tolerance':0}])
            p.update(instrument='model-comparison',inputs={'cases_per_seed':6},seeds=[self.instance],
                evaluator={'id':'historical-correction@1'},source='def experiment(inputs):\n return inputs["trials"]',
                budget={'seconds':20,'provider_calls':18},success='B improves accuracy by at least 0.25 over paired A.')
        else:
            p['source']='''def experiment(inputs):
 a,b=inputs['observations'][0],inputs['observations'][-1]
 m=(b['y']-a['y'])/(b['x']-a['x']);c=a['y']-m*a['x']
 def f(x):return m*x+c
 return {'probe_predictions':[f(x) for x in inputs['probes']],'holdout_predictions':[f(r['x']) for r in inputs['holdout']]}
'''
        if not experiments:
            actions=[action('hypothesis','fixture-hypothesis',h),action('experiment','fixture-initial',p)]
        elif self.benchmark=='revision' and 'fixture-revised' not in experiments:
            measured=experiments['fixture-initial']['evaluation']['measurement_details']['observations']
            # A deliberately programmed fitting strategy for the fixture. Never
            # supplied to a live model or reported as autonomous hypothesis discovery.
            from .hidden_system import observations
            initial=observations(self.instance)
            slope=(initial[-1]['y']-initial[0]['y'])/4;intercept=initial[1]['y']
            bend=measured[0]['observed']-slope*3-intercept
            h.update(supersedes=1,statement='A scripted piecewise quadratic candidate improves unseen predictions.',provenance=['fixture-initial'])
            p.update(revision=2,seeds=[self.instance+2000],source=f'''def experiment(inputs):
 def f(x):return {slope}*x+{intercept}+{bend}*max(0,x-2)**2
 return {{'probe_predictions':[f(x) for x in inputs['probes']],'holdout_predictions':[f(r['x']) for r in inputs['holdout']]}}
''')
            actions=[action('experiment_interpretation','fixture-negative',{'experiment':'fixture-initial',
                'interpretation':'Measured responses contradict the frozen linear prediction.',
                'limitations':'Programmed fixture fitting strategy, not live model discovery.',
                'next_step':'Run the scripted revised candidate on a fresh held-out seed.'}),
                action('hypothesis','fixture-hypothesis',h),action('experiment','fixture-revised',p)]
        elif 'fixture-replication' not in experiments:
            # The context intentionally contains only a source excerpt. Fixture
            # replication gets its exact source from the preserved scripted
            # specification, not an invented continuation of omitted source.
            if self.benchmark=='revision':
                from .hidden_system import observations
                initial=observations(self.instance)
                measured=experiments['fixture-initial']['evaluation']['measurement_details']['observations']
                slope=(initial[-1]['y']-initial[0]['y'])/4;intercept=initial[1]['y']
                bend=measured[0]['observed']-slope*3-intercept
                p.update(revision=2,seeds=[self.instance+2000],source=f'''def experiment(inputs):
 def f(x):return {slope}*x+{intercept}+{bend}*max(0,x-2)**2
 return {{'probe_predictions':[f(x) for x in inputs['probes']],'holdout_predictions':[f(r['x']) for r in inputs['holdout']]}}
''')
            p['replicates']='fixture-revised' if self.benchmark=='revision' else 'fixture-initial'
            actions=[action('experiment','fixture-replication',p)]
        else:
            actions=[action('investigation_decision','fixture-close',{'hypothesis':'fixture-hypothesis','decision':'close',
                'uncertainty':'Generalization outside this artificial task family and live model behavior remain unresolved.',
                'reason':'The prespecified finite fixture and independent replication completed.',
                'next_experiment':'','cost':'No live provider calls were made.','stop_condition':'Finite pipeline acceptance completed, not scientific resolution.'})]
        return json.dumps({'base_version':context['version'],'title':'Scripted scientific pipeline fixture',
            'summary':'Synthetic provider; actual isolated computation and measurements, no live discovery claim.','actions':actions}),{'fixture':True}

    @staticmethod
    def correct(context):
        task=context['task'];history=context['historical_observations']
        numbers=list(map(int,re.findall(r'-?\d+',task)))
        proposed=int(re.search(r'Proposed (?:corrected )?answer: (-?\d+)',task).group(1))
        answer=proposed
        if task.startswith('Compute'):answer=numbers[0]+numbers[1]
        elif 'each unit' in task:answer=numbers[0]*numbers[1]
        elif 'revision 2 uses' in task:answer=numbers[0]+int(re.search(r'revision 2 uses \+(\d+)',task).group(1))
        elif history:
            record=next(h for h in history if h['id'].endswith('verified'))
            offset=int(re.findall(r'-?\d+',record['text'])[-1])
            answer=numbers[0]-offset if 'subtract' in record['text'] else numbers[0]+offset
        return json.dumps({'answer':answer,'error_detected':answer!=proposed,'corrected':answer!=proposed,
            'evidence':[h['id'] for h in history if h['id'].endswith('verified') and not task.startswith('Compute')]})
