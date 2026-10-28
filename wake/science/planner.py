"""Bounded experimental context and permission reconciliation; model proposes the next investigation."""
from copy import deepcopy
from ..event_format import canonical
from . import contracts as c
from .instruments import INSTRUMENTS

SYSTEM = '''
Experimental research is enabled through wake-scientific-research@1. Literature is background,
not a substitute for a test. When computation can challenge an uncertainty, propose a
hypothesis then an experiment using the scientific_research contract in context. Each action
has type, id, project, definition; definition is a finite JSON object. Accuracy,
probe_accuracy and holdout_accuracy are numeric fractions: predict value 1, not
boolean true. Choose seeds absent from consumed_holdout_seeds for the selected
instance; previous protocol inputs and seeds are supplied with each experiment.
Hypotheses
and protocols are immutable; change a hypothesis with a superseding revision and give every
experiment a new ID. For a revision REUSE the SAME hypothesis action id and set supersedes
to its existing integer revision. For a NEW hypothesis OMIT supersedes completely.
For a new experiment OMIT replicates unless copying an evaluated protocol exactly.
The runtime independently freezes, executes and scores approved work.
Never claim to have run code or supply an execution receipt. Receive actual results on later
wakes, distinguish failure/invalid measurement/inconclusive/contradiction/support, retain
negative evidence, then propose an interpretation, revision, replication, next test, or an
explicit suspend/close decision. Do not keep collecting sources when an informative executable
experiment is available. Never infer hidden scorer inputs. An unavailable instrument is a
capability blocker, not a scientific finding. A numeric-observation instrument has no independent
oracle: its output alone cannot establish validated scientific support. A finite sorting test
establishes accuracy only for its recorded cases. Novelty and acceptance counts are not discoveries.
'''


def configure(store, enabled):
    state=store.load()
    current=state.get('science')
    if state.get('charter') and (enabled or current) and (not current or current['enabled']!=enabled):
        store.append('scientific_configured',{'schema':c.SCHEMA,'base_version':state['version'],
                                            'actor':'operator','enabled':enabled})
    return store.load()


def context(state):
    science=state.get('science')
    if not science or not science['enabled']:
        return None
    hypotheses=sorted(science['hypotheses'].values(),key=lambda h:(h['revisions'][-1]['accepted_version'],h['id']),reverse=True)[:3]
    experiments=sorted(science['experiments'].values(),key=lambda e:(e['accepted_version'],e['id']),reverse=True)[:3]
    result={'schema':c.SCHEMA,'enabled':True,'instruments':INSTRUMENTS,
        'actions':{'hypothesis':{'definition_schema':c.HYPOTHESIS,
          'required':['schema','statement','kind','assumptions','predictions','falsification','provenance','uncertainty'],
          'types':{'schema':c.HYPOTHESIS,'kind':['empirical','exploratory'],'statement':'string',
                   'assumptions':['string'],'provenance':['existing evidence/notebook/experiment ID; [] when none'],
                   'predictions':[{'metric':'string','operator':'eq | gte | lte','value':'number, boolean, or string','tolerance':0}],
                   'falsification':'string describing observations against the claim','uncertainty':'string'},
          'prediction':{'metric':'accuracy','operator':'eq','value':1,'tolerance':0},
          'revisions':'Set supersedes to the prior integer revision; history is retained.'},
        'experiment':{'definition_schema':c.PROTOCOL,'required':['schema','hypothesis','revision','method','instrument','source','inputs','seeds','evaluator','success','stop','budget'],
          'python_entrypoint':'def experiment(inputs): ...; return finite JSON',
          'types':{'schema':c.PROTOCOL,'hypothesis':'existing or earlier-in-this-proposal hypothesis ID','revision':1,
                   'method':'string','instrument':'python','source':'Python source string, NOT a code fence',
                   'inputs':'object matching selected evaluator','seeds':[13,71,43],
                   'evaluator':{'id':'one installed evaluator ID'},'success':'prespecified success criteria string',
                   'stop':'stopping rule string','budget':{'seconds':20,'provider_calls':0}},
          'sort-correctness@1':{'inputs':{'cases_per_seed':4,'length':8,'magnitude':100},
            'delivery':'inputs.trials contains id and values; return one sorted list per trial. Labels are not supplied.'},
          'numeric-observation@1':{'delivery':'inputs.parameters and inputs.seeds; return {measurements:{metric:[samples]}}; unvalidated until independently checked.'},
          'hidden-relationship@1':{'inputs':{'instance':17,'probes':[3,5,8],'holdout_size':8},
            'delivery':'inputs.observations are initial x,y pairs; inputs.probes are your chosen x values; inputs.holdout contains id,x. Return {probe_predictions:[y],holdout_predictions:[y]} in input order. The scorer reveals observed responses only for your probes, and aggregate accuracy for holdout. Use fresh seeds in follow-ups. The mechanism is unknown to you; infer it from observations, never presume a revised explanation.'},
          'historical-correction@1':{'instrument':'model-comparison','inputs':{'cases_per_seed':6},
            'delivery':'Preparation must return the unchanged inputs.trials list or unchanged inputs object. Trusted runtime runs each frozen randomized A/B/C task using the same provider/model, then scores independent known answers. Six cases need 18 provider calls per seed; budget.provider_calls must cover this and never exceed 48. Metrics A_accuracy,B_accuracy,C_accuracy,accuracy_gain_B_over_A,accuracy_gain_C_over_B plus error detection/correction/false correction/evidence selection. The primary causal contrast must be frozen in your hypothesis.'},
          'replication':{'definition':{'schema':c.PROTOCOL,'replicates':'evaluated experiment ID'},
            'meaning':'Use a NEW experiment action id. Runtime copies the exact preserved protocol; do not reconstruct omitted code or parameters.'}},
        'research_direction':{'required':['next','reason','uncertainty','cost','stop'],
            'next':['collect','experiment'],'meaning':'Choose the next wake route. collect requests the existing external evidence planner; experiment permits hypotheses, design, analysis, revision or replication without compulsory retrieval.'},
        'experiment_interpretation':{'required':['experiment','interpretation','limitations','next_step'],'authority':'Model interpretation only'},
        'investigation_decision':{'required':['hypothesis','decision','uncertainty','reason','next_experiment','cost','stop_condition'],'decisions':['continue','suspend','close']}},
        'serialization':'Every action definition is a JSON object matching response_schema. Return the outer proposal as JSON with base_version,title,summary,actions. Do not use markdown fences. Use only exact field names and enum values above.',
        'hypotheses':[],'experiments':[],'recent_directions':deepcopy(science.get('directions',[])[-2:]),
        'experiment_index':[{'id':e['id'],'status':e['status'],'hypothesis':e['protocol']['hypothesis'],
            'revision':e['protocol']['revision']} for e in
            sorted(science['experiments'].values(),key=lambda e:e['accepted_version'])[-16:]],
        'convergence_decisions':deepcopy(science.get('decisions',[])[-3:]),
        'convergence_evidence':[convergence(science,h) for h in hypotheses],
        'consumed_holdout_seeds':{str(instance):sorted({seed for e in science['experiments'].values()
            if e['protocol']['evaluator']['id']=='hidden-relationship@1' and e['protocol']['inputs']['instance']==instance
            for seed in e['protocol']['seeds']})
            for instance in {e['protocol']['inputs']['instance'] for e in science['experiments'].values()
                             if e['protocol']['evaluator']['id']=='hidden-relationship@1'}}}
    prior=[i for i in state.get('invocations',{}).values() if i.get('status')=='rejected']
    if science.get('instrument_binding'):
        result['instrument_binding']=deepcopy(science['instrument_binding'])
        result['actions']['experiment']['hidden-relationship@1']['inputs']['instance']=science['instrument_binding']['instance']
    result['recent_rejection_feedback']=[{'reason':i.get('reason'),'invocation':i['id']} for i in prior[-2:]]
    for h in hypotheses:
        result['hypotheses'].append({'id':h['id'],'project':h['project'],'status':h['status'],
            'revision':len(h['revisions']),'definition':deepcopy(h['revisions'][-1]['definition']),
            'revision_action_identity':{'type':'hypothesis','id':h['id'],'project':h['project'],
                'supersedes_in_definition':len(h['revisions']),'omit_supersedes_for_new_ID':True}})
    for e in experiments:
        evaluation=deepcopy(e.get('evaluation'))
        if evaluation:
            details=evaluation.get('measurement_details',{})
            details.pop('by_trial',None)
            details.pop('by_case',None)
        result['experiments'].append({'id':e['id'],'project':e['project'],'status':e['status'],
            'hypothesis':e['protocol']['hypothesis'],'revision':e['protocol']['revision'],
            'protocol_digest':e['protocol']['protocol_digest'],'predictions':e['predictions'],
            'protocol_inputs':deepcopy(e['protocol']['inputs']),'protocol_seeds':e['protocol']['seeds'],
            'evaluator':e['protocol']['evaluator']['id'],
            'source_excerpt':e['protocol']['source'][:1600],
            'evaluation':evaluation,
            'blocked_reason':e.get('review',{}).get('reason') if e['status']=='blocked' else None,
            'last_execution':({key:value for key,value in e['attempts'][-1].get('receipt',{}).items()
                              if key in ('status','reason','wall_seconds','outputs_digest')} if e['attempts'] else None)})
    # Protected labels, hidden parameters and scorer artifacts never enter model context.
    while len(canonical(result))>10000 and (result['experiments'] or result['hypotheses']):
        if result['experiments']:result['experiments'].pop()
        else:result['hypotheses'].pop()
    return result


def convergence(science,hypothesis):
    """Derive test readiness from retained measurements, never activity counts.

    This is planning evidence, not an authority gate or a declaration that an
    open scientific question is resolved. A model still proposes its next step.
    """
    revision=len(hypothesis['revisions'])
    experiments=[e for e in science['experiments'].values()
                 if e['protocol']['hypothesis']==hypothesis['id'] and e['protocol']['revision']==revision]
    pending=[e['id'] for e in experiments if e['status'] in ('proposed','approved','running','completed','cleanup_required')]
    evaluated=[e for e in experiments if e.get('evaluation')]
    supported=[e for e in evaluated if e['evaluation']['outcome']=='provisionally_supported']
    contradicted=[e for e in evaluated if e['evaluation']['outcome']=='contradicted']
    replicated=[e for e in evaluated if e['evaluation']['replication_status']=='replicated']
    blocked=[e['id'] for e in experiments if e['status'] in ('blocked','failed','interrupted','cleanup_required')]
    if pending:stage='awaiting_execution_or_evaluation'
    elif contradicted:stage='contradiction_requires_explanation_or_revision'
    elif supported:stage='bounded_comparison_complete' if replicated else 'independent_replication_needed'
    elif evaluated:stage='inconclusive_or_invalid_measurement'
    elif blocked:stage='capability_or_execution_blocked'
    else:stage='test_design_needed'
    return {'hypothesis':hypothesis['id'],'revision':revision,'stage':stage,'pending':pending,
        'supported_experiments':[e['id'] for e in supported],
        'contradicted_experiments':[e['id'] for e in contradicted],
        'replications':[e['id'] for e in replicated],'execution_blockers':blocked,
        'execution_seconds':sum(a.get('receipt',{}).get('wall_seconds',0) for e in experiments for a in e['attempts']),
        'remaining_uncertainty':hypothesis['revisions'][-1]['definition']['uncertainty'],
        'decision_rule':'Compare the feasible next distinguishing test, expected uncertainty reduction and cost against the frozen stop rule. Budget exhaustion or administrative closure is not scientific resolution.'}


def prefer_experiment(state):
    """Give the model a governed alternative to compulsory retrieval planning."""
    science=state.get('science',{})
    if not science.get('enabled'):return False
    directions=science.get('directions',[])
    if directions and directions[-1]['next']=='collect':return False
    return any(p.get('status')=='active' for p in state.get('projects',{}).values())
