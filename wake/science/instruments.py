"""Trusted computational instruments and independent scorers, never candidate code."""
import math
import random
import statistics

from ..event_format import digest, canonical
from ..governance import require
from . import contracts as c

INSTRUMENTS = {'python': ('sort-correctness@1', 'numeric-observation@1', 'hidden-relationship@1'),
               'model-comparison':('historical-correction@1',)}
RUNNER = '''import importlib.util,json
spec=importlib.util.spec_from_file_location("candidate","/experiment/program.py")
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
inputs=json.load(open("/experiment/inputs.json"))
print(json.dumps(module.experiment(inputs),allow_nan=False))
'''


def prepare(protocol):
    """Freeze exact computational inputs and protected labels before execution."""
    require(protocol['instrument'] in INSTRUMENTS and protocol['evaluator']['id'] in INSTRUMENTS[protocol['instrument']],
            'Instrument/evaluator is unavailable in this runtime')
    if protocol['evaluator']['id']=='historical-correction@1':
        from .correction import prepare as prepare_correction
        return prepare_correction(protocol)
    if protocol['evaluator']['id'] == 'hidden-relationship@1':
        from .hidden_system import prepare as prepare_hidden
        return prepare_hidden(protocol)
    if protocol['evaluator']['id'] == 'sort-correctness@1':
        c.fields(protocol['inputs'], ('cases_per_seed','length','magnitude'))
        for key, high in [('cases_per_seed',32),('length',128),('magnitude',1000000)]:
            require(type(protocol['inputs'][key]) is int and 1<=protocol['inputs'][key]<=high, 'Sorting input bounds exceeded')
        trials=[]
        for seed in protocol['seeds']:
            rng=random.Random(seed)
            for index in range(protocol['inputs']['cases_per_seed']):
                magnitude=protocol['inputs']['magnitude']
                trials.append({'id':f'{seed}-{index}','values':[rng.randint(-magnitude,magnitude) for _ in range(protocol['inputs']['length'])]})
        require(len(canonical({'trials': trials})) <= 64000, 'Prepared execution inputs exceed the bound')
        return {'trials':trials}, {'oracle_digest':digest([sorted(t['values']) for t in trials])}
    return {'parameters':protocol['inputs'],'seeds':protocol['seeds']}, {}


def _measure(item):
    attempt=item['attempts'][-1]
    output=attempt['receipt']['outputs']
    if item['protocol']['evaluator']['id']=='historical-correction@1':
        from .correction import measure
        return measure(item)
    if item['protocol']['evaluator']['id']=='hidden-relationship@1':
        from .hidden_system import measure
        return measure(item)
    if item['protocol']['evaluator']['id']=='sort-correctness@1':
        expected=[sorted(t['values']) for t in attempt['execution_inputs']['trials']]
        require(isinstance(output,list) and len(output)==len(expected),
                'A sorting instrument must return one list per input trial')
        for values in output:
            require(isinstance(values,list) and len(values)<=128 and all(type(x) is int for x in values), 'Invalid sorting measurement')
        correct=[a==b for a,b in zip(output,expected)]
        return {'accuracy':sum(correct)/len(correct),'cases':len(correct),'errors':len(correct)-sum(correct),'all_correct':all(correct)}, 'validated', {
            'method':'Independent host-side exact oracle; protected answers never mounted',
            'scope':'Accuracy on these finite seeded arrays, not general algorithm correctness',
            'by_case':correct}
    c.fields(output, ('measurements',))
    require(isinstance(output['measurements'],dict) and 1<=len(output['measurements'])<=16, 'Bounded numeric measurements required')
    metrics={}
    for name,values in output['measurements'].items():
        c.text(name,'Measurement name',80)
        require(isinstance(values,list) and 1<=len(values)<=1024 and
                all(type(x) in (int,float) and math.isfinite(x) for x in values), 'Measurements must be finite bounded samples')
        metrics[name]=statistics.mean(values)
    return metrics,'unvalidated',{'method':'Host-side means of instrument-reported samples',
        'scope':'No independent measurement oracle; execution and numerical summaries do not validate the instrument'}


def evaluate(item):
    """Recomputable scorer; published model interpretation cannot change a verdict."""
    attempt=item['attempts'][-1]
    require(attempt['receipt']['status']=='completed', 'A failed execution cannot test the hypothesis')
    report={'schema':c.EVALUATION,'protocol_digest':item['protocol']['protocol_digest'],
            'evaluator':item['protocol']['evaluator']['id'], 'execution_valid':True,
            'outputs_digest':attempt['receipt']['outputs_digest'], 'replication_status':'not_attempted'}
    try:
        metrics,validity,detail=_measure(item)
    except (ValueError,TypeError,KeyError) as error:
        return {**report,'measurement_validity':'invalid','outcome':'invalid_measurement',
                'metrics':{},'reason':str(error)[:1000]}
    comparisons=[]
    for prediction in item['predictions']:
        measured=metrics.get(prediction['metric'])
        if measured is None:
            comparisons.append({'prediction':prediction,'measurement':None,'satisfied':None})
            continue
        target,tolerance=prediction['value'],prediction['tolerance']
        satisfied=(measured==target if type(target) in (str,bool) else measured>=target-tolerance if prediction['operator']=='gte' else
                   measured<=target+tolerance if prediction['operator']=='lte' else abs(measured-target)<=tolerance)
        comparisons.append({'prediction':prediction,'measurement':measured,'satisfied':satisfied})
    outcome='inconclusive'
    if validity=='validated' and comparisons and all(x['satisfied'] is not None for x in comparisons):
        outcome='provisionally_supported' if all(x['satisfied'] for x in comparisons) else 'contradicted'
    if item['protocol'].get('replicates'):
        previous=item['review']['protected'].get('replication_outputs_digest')
        if 'replication_metrics_digest' in item['review']['protected']:
            match=item['review']['protected']['replication_metrics_digest']==digest(metrics)
            report['replication_criterion']='Exact independently scored measurement profile; runtime/usage metadata may differ'
        else:match=previous==report['outputs_digest']
        report['replication_status']=('replicated' if match else 'replication_failed') if validity=='validated' else 'inconclusive'
    return {**report,'measurement_validity':validity,'outcome':outcome,'metrics':metrics,
            'predictions':comparisons,'measurement_details':detail,
            'scorer_digest':digest({'schema':c.EVALUATION,'evaluator':report['evaluator'],'metrics':metrics,'predictions':comparisons})}
