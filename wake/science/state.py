"""Scientific state belongs to the research application's existing native record."""
from copy import deepcopy

from ..event_format import digest, canonical
from ..governance import require
from . import contracts as c

MODEL_ACTIONS = ('hypothesis', 'experiment', 'experiment_interpretation', 'investigation_decision','research_direction')
EVENTS = ('scientific_configured', 'experiment_reviewed', 'experiment_started',
          'experiment_executed', 'experiment_evaluated', 'experiment_interrupted',
          'experiment_inference_started','experiment_inference_finished')


def initial():
    return {'schema': c.SCHEMA, 'enabled': False, 'hypotheses': {}, 'experiments': {}, 'decisions': [],'directions':[]}


def apply_action(state, action, invocation):
    require(state.get('charter'), 'Scientific actions require the research application')
    science = deepcopy(state.get('science') or initial())
    require(science['enabled'], 'Experimental research capability is not enabled')
    c.fields(action, ('type', 'id', 'project', 'definition'))
    c.identifier(action['id'])
    require(action['project'] in state.get('projects', {}), 'Scientific work must belong to an existing project')
    value = c.parse_definition(action['definition'])
    project = action['project']
    origin = {'invocation': invocation, 'accepted_version': state['version'] + 1}
    if action['type'] == 'hypothesis':
        value = c.hypothesis(value)
        old = science['hypotheses'].get(action['id'])
        revisions = deepcopy(old['revisions']) if old else []
        if old:
            require(old['project'] == project and value.get('supersedes') == len(revisions),
                    f'A hypothesis revision must supersede its exact previous version in the same project: reuse id {action["id"]} with supersedes={len(revisions)}')
            require(digest(value) != revisions[-1]['definition_digest'], 'A revision must change the hypothesis')
        else:
            require('supersedes' not in value, 'A new hypothesis cannot supersede missing history. Omit supersedes for a new ID; '
                    'to revise an existing hypothesis reuse one of these project IDs: '+','.join(
                        h['id'] for h in science['hypotheses'].values() if h['project']==project)[:500])
        available = set(state.get('evidence', {})) | set(state.get('notebooks', {})) | set(science['experiments'])
        require(set(value['provenance']) <= available, 'Hypothesis provenance must name recorded evidence or experiments')
        revisions.append({'revision': len(revisions)+1, 'definition': value,
                          'definition_digest': digest(value), 'status':'exploratory' if value['kind']=='exploratory' else 'untested', **origin})
        science['hypotheses'][action['id']] = {'id': action['id'], 'project': project,
            'status': 'exploratory' if value['kind']=='exploratory' else 'untested', 'revisions': revisions}
    elif action['type'] == 'experiment':
        require(action['id'] not in science['experiments'], 'Experiment IDs cannot be reused or overwritten')
        if set(value)=={'schema','replicates'}:
            require(value['schema']==c.PROTOCOL,'Unsupported replication request schema')
            prior=science['experiments'].get(value['replicates'])
            require(prior and prior['project']==project and prior['status']=='evaluated',
                    'Replication reference requires an evaluated experiment in the same project')
            value={**{key:deepcopy(item) for key,item in prior['protocol'].items()
                      if key not in ('source_digest','inputs_digest','protocol_digest','replicates')},
                   'replicates':value['replicates']}
        value = c.protocol(value)
        binding=science.get('instrument_binding')
        if binding:
            require(value['evaluator']['id']==binding['evaluator'] and
                    value['inputs'].get('instance')==binding['instance'],
                    'Experiment must use the operator-bound benchmark instrument and instance')
        from .instruments import INSTRUMENTS, prepare
        if value['instrument'] in INSTRUMENTS and value['evaluator']['id'] in INSTRUMENTS[value['instrument']]:
            prepare(value)  # Pure design validation, never an execution or provider effect.
        h = science['hypotheses'].get(value['hypothesis'])
        require(h and h['project'] == project and value['revision'] <= len(h['revisions']),
                'Experiment must reference an exact recorded hypothesis revision in its project')
        revision = h['revisions'][value['revision']-1]
        require(revision['definition']['kind'] == 'empirical', 'Exploratory questions must become testable before execution')
        if value.get('replicates'):
            prior = science['experiments'].get(value['replicates'])
            require(prior and prior['status'] == 'evaluated', 'Replication requires a completed evaluated experiment')
            frozen = {key: item for key, item in value.items() if key not in ('replicates','protocol_digest')}
            previous = {key: item for key,item in prior['protocol'].items() if key not in ('replicates','protocol_digest')}
            require(frozen == previous, 'Independent replication must preserve the exact recorded protocol')
        elif value['evaluator']['id']=='hidden-relationship@1':
            used={seed for previous in science['experiments'].values()
                  if previous['protocol']['evaluator']['id']=='hidden-relationship@1'
                  and previous['protocol']['inputs'].get('instance')==value['inputs'].get('instance')
                  for seed in previous['protocol']['seeds']}
            require(not used.intersection(value['seeds']), 'A consumed hidden-system holdout seed cannot be optimized against again')
        science['experiments'][action['id']] = {'id': action['id'], 'project': project,
            'status': 'proposed', 'protocol': value, 'hypothesis_digest': revision['definition_digest'],
            'predictions': deepcopy(revision['definition']['predictions']), 'attempts': [], 'interpretations': [], **origin}
    elif action['type'] == 'experiment_interpretation':
        c.fields(value, ('experiment', 'interpretation', 'limitations', 'next_step'))
        item = science['experiments'].get(value['experiment'])
        require(item and item['project'] == project and item['status'] == 'evaluated',
                'Interpretation requires evaluated measurements in the same project')
        require(not any(i['id'] == action['id'] for e in science['experiments'].values() for i in e['interpretations']),
                'Interpretation IDs cannot be reused')
        for key in ('interpretation', 'limitations', 'next_step'):
            c.text(value[key], key)
        item['interpretations'].append({'id': action['id'], **value, **origin,
                                       'classification': 'model_interpretation'})
    elif action['type']=='research_direction':
        c.fields(value,('next','reason','uncertainty','cost','stop'))
        require(value['next'] in ('collect','experiment'), 'Choose external collection or computational experimentation')
        for key in ('reason','uncertainty','cost','stop'):c.text(value[key],key)
        directions=science.setdefault('directions',[])
        require(not any(d['id']==action['id'] for d in directions),'Research direction ID already exists')
        directions.append({'id':action['id'],'project':project,**value,**origin})
    elif action['type'] == 'investigation_decision':
        c.fields(value, ('hypothesis', 'decision', 'uncertainty', 'reason', 'next_experiment', 'cost', 'stop_condition'))
        h = science['hypotheses'].get(value['hypothesis'])
        require(h and h['project'] == project, 'Investigation decision requires its recorded hypothesis')
        require(value['decision'] in ('continue','suspend','close'), 'Unknown investigation decision')
        for key in ('uncertainty','reason','next_experiment','cost','stop_condition'):
            c.text(value[key], key, empty=key=='next_experiment' and value['decision']!='continue')
        require(not any(d['id']==action['id'] for d in science['decisions']), 'Decision identity already exists')
        science['decisions'].append({'id':action['id'], **value, **origin})
        h['investigation_status'] = value['decision']
    state['science'] = science
    return state


def reduce(state, event):
    science = deepcopy(state.get('science') or initial())
    p, kind = event['payload'], event['kind']
    require(p.get('schema') == c.SCHEMA and p.get('base_version') == state['version'],
            'Scientific event schema/version mismatch')
    require(state.get('pending') is None, 'Experiment transitions require an idle research writer')
    if kind == 'scientific_configured':
        c.fields(p, ('schema','base_version','actor','enabled'),('instrument_binding',))
        require(state.get('charter') and p['actor']=='operator' and type(p['enabled']) is bool, 'Experimental capability is operator-owned')
        science['enabled'] = p['enabled']
        if 'instrument_binding' in p:
            c.fields(p['instrument_binding'],('evaluator','instance'))
            require(p['instrument_binding']['evaluator']=='hidden-relationship@1' and
                    type(p['instrument_binding']['instance']) is int and 0<=p['instrument_binding']['instance']<2**32,
                    'Invalid benchmark instrument binding')
            require(not science['experiments'] and not science.get('instrument_binding'),
                    'A benchmark binding must be frozen before any experiment')
            science['instrument_binding']=deepcopy(p['instrument_binding'])
        return science
    c.identifier(p.get('id'))
    item = science['experiments'].get(p['id'])
    require(item and p.get('protocol_digest') == item['protocol']['protocol_digest'], 'Missing or changed frozen protocol')
    base = ('schema','base_version','id','protocol_digest')
    if kind == 'experiment_reviewed':
        c.fields(p, (*base,'decision','reason','environment','protected'))
        require(science['enabled'] and item['status'] in ('proposed','blocked'), 'Experiment cannot be reviewed in this state')
        require(p['decision'] in ('approved','blocked'), 'Invalid deterministic design review')
        c.text(p['reason'], 'Review reason')
        require(isinstance(p['protected'], dict) and len(canonical(p['protected'])) <= 32000, 'Protected scoring input is bounded')
        if p['decision']=='approved':
            from .instruments import prepare
            _, protected=prepare(item['protocol'])
            if item['protocol'].get('replicates'):
                previous=science['experiments'][item['protocol']['replicates']]
                protected['replication_outputs_digest']=previous['attempts'][-1]['receipt']['outputs_digest']
                if p['environment'].get('replication_criterion')=='measurement-profile@1':
                    protected['replication_metrics_digest']=digest(previous['evaluation']['metrics'])
            require(p['protected']==protected, 'Design review must bind the independently derived scoring identity')
            require(isinstance(p['environment'],dict) and isinstance(p['environment'].get('image_id'),str)
                    and p['environment']['image_id'], 'Approved execution requires an environment identity')
        item.update(status=p['decision'], review={'reason':p['reason'],'environment':p['environment'],
                                                 'protected':deepcopy(p['protected']), 'event':event['seq']})
    elif kind == 'experiment_started':
        c.fields(p, (*base,'attempt','containers','execution_inputs','inputs_digest'))
        require(science['enabled'] and item['status']=='approved', 'Only approved experiments may run')
        c.identifier(p['attempt'])
        require(not any(a['id']==p['attempt'] for e in science['experiments'].values() for a in e['attempts']),
                'Execution attempt identity already used')
        require(isinstance(p['containers'],list) and 1<=len(p['containers'])<=4 and
                all(isinstance(name,str) and name.startswith('wake-improve-science-') for name in p['containers']),
                'Bounded disposable execution identities required')
        require(digest(p['execution_inputs']) == p['inputs_digest'] and len(canonical(p['execution_inputs'])) <= 64000,
                'Execution inputs must be bounded and content-bound')
        from .instruments import prepare
        require(p['execution_inputs']==prepare(item['protocol'])[0], 'Execution inputs must match the frozen instrument preparation')
        item['attempts'].append({'id':p['attempt'],'status':'running','containers':p['containers'],
            'execution_inputs':deepcopy(p['execution_inputs']), 'inputs_digest':p['inputs_digest'], 'started':event['time']})
        item['status']='running'
    elif kind in ('experiment_inference_started','experiment_inference_finished'):
        c.fields(p,(*base,'attempt','trial','evidence'))
        require(science['enabled'] and item['status']=='running' and item['attempts'][-1]['id']==p['attempt'],
                'Trial evidence needs its active reserved execution')
        require(item['protocol']['instrument']=='model-comparison','Only the governed inference instrument can record trials')
        attempt=item['attempts'][-1]
        trials=attempt.setdefault('inference',[])
        frozen=attempt['execution_inputs']['trials']
        if kind=='experiment_inference_started':
            require(len(trials)<len(frozen) and p['trial']==frozen[len(trials)]['id'] and
                    (not trials or trials[-1]['status']=='completed'), 'Trial identity/order is stale or replayed')
            require(len(trials)<item['protocol']['budget']['provider_calls'], 'Experiment inference allowance exhausted')
            from .correction import request
            expected=request(frozen[len(trials)])
            c.fields(p['evidence'],('request','request_digest','provider','model','invocation'))
            require(p['evidence']['request']==expected and p['evidence']['request_digest']==digest(expected),
                    'Task context or scoring conditions changed after protocol freeze')
            environment=item['review']['environment']
            require(p['evidence']['provider']==environment.get('provider') and p['evidence']['model']==environment.get('model'),
                    'Paired trial provider/model must match approved environment')
            trials.append({'id':p['trial'],'status':'started',
                **({'started_at':event['time']} if environment.get('trial_accounting')==1 else {}),
                **deepcopy(p['evidence'])})
        else:
            require(trials and trials[-1]['id']==p['trial'] and trials[-1]['status']=='started', 'Stale or duplicate inference response')
            require(isinstance(p['evidence'],dict) and len(canonical(p['evidence']))<=16000,'Inference receipt exceeds its bound')
            c.fields(p['evidence'],('raw','metadata','wall_seconds'))
            trials[-1].update(status='completed',response=deepcopy(p['evidence']))
    elif kind in ('experiment_executed','experiment_interrupted'):
        c.fields(p, (*base,'attempt','receipt'))
        require((item['status']=='running' or kind=='experiment_interrupted' and item['status']=='cleanup_required') and item['attempts'][-1]['id']==p['attempt'], 'Stale or replayed execution receipt')
        receipt=p['receipt']
        require(isinstance(receipt,dict) and len(canonical(receipt))<=80000, 'Execution receipt must be bounded')
        require(receipt.get('protocol_digest')==p['protocol_digest'] and
                receipt.get('inputs_digest')==item['attempts'][-1]['inputs_digest'], 'Receipt provenance mismatch')
        require(receipt.get('status') in ('completed','failed','interrupted','cleanup_required'), 'Invalid execution status')
        if kind=='experiment_interrupted':
            require(receipt['status'] in ('interrupted','cleanup_required'), 'Recovery cannot invent an execution result')
        else:
            require(receipt['status'] in ('completed','failed'), 'Execution result is not terminal')
        if kind=='experiment_executed':
            required_schema=item['review']['environment'].get('receipt_schema')
            require(receipt.get('schema') in (c.EXECUTION,'wake-experiment-execution@1'), 'Unsupported execution receipt')
            if required_schema:
                require(receipt['schema']==required_schema,'Execution receipt schema differs from the approved runtime')
            if receipt['schema']==c.EXECUTION:
                require(receipt.get('attempt_id')==p['attempt'],'Execution receipt belongs to a different reserved attempt')
            require(receipt.get('source_digest')==item['protocol']['source_digest'] and
                    receipt.get('environment_digest')==digest(item['review']['environment']), 'Executed code/environment identity mismatch')
        if receipt['status']=='completed':
            require('outputs' in receipt and receipt.get('outputs_digest')==digest(receipt['outputs']), 'Measurement artifact hash mismatch')
            if item['protocol']['instrument']=='model-comparison':
                import json
                inference=item['attempts'][-1].get('inference',[])
                require(len(inference)==len(item['attempts'][-1]['execution_inputs']['trials']) and
                        all(t['status']=='completed' for t in inference),'Inference experiment has incomplete trial evidence')
                measured={'trials':[{'id':t['id'],'answer':json.loads(t['response']['raw']),
                    'metadata':t['response']['metadata'],'wall_seconds':t['response']['wall_seconds']} for t in inference]}
                require(receipt['outputs']==measured,'Inference measurements must derive from durable responses')
        item['attempts'][-1].update(status=receipt['status'],receipt=deepcopy(receipt),finished=event['time'])
        item['status']='completed' if receipt['status']=='completed' else receipt['status']
    elif kind == 'experiment_evaluated':
        c.fields(p, (*base,'attempt','evaluation'))
        require(item['status']=='completed' and item['attempts'][-1]['id']==p['attempt'], 'Evaluation needs a completed execution')
        from .instruments import evaluate
        expected=evaluate(item)
        require(p['evaluation']==expected, 'Evaluation must be independently recomputed from frozen inputs and measurements')
        item.update(status='evaluated',evaluation=expected)
        h=science['hypotheses'][item['protocol']['hypothesis']]
        outcomes=[e['evaluation']['outcome'] for e in science['experiments'].values() if
                  e['protocol']['hypothesis']==item['protocol']['hypothesis'] and
                  e['protocol']['revision']==item['protocol']['revision'] and 'evaluation' in e]
        status='contradicted' if 'contradicted' in outcomes else expected['outcome']
        h['revisions'][item['protocol']['revision']-1]['status']=status
        if item['protocol']['revision']==len(h['revisions']):
            h['status']=status
    else:
        raise ValueError('Unknown scientific lifecycle event')
    return science
