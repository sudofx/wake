"""Versioned, bounded scientific proposals. Validation is deterministic and effect-free."""
import ast
import json
import math
import re
from copy import deepcopy

from ..event_format import digest, canonical
from ..governance import require

HYPOTHESIS = 'wake-hypothesis@1'
PROTOCOL = 'wake-experiment-protocol@1'
EXECUTION = 'wake-experiment-execution@2'
EVALUATION = 'wake-experiment-evaluation@1'
SCHEMA = 'wake-scientific-research@1'
MAX_CODE = 16000
MAX_INPUT = 24000


def fields(value, required, optional=(), label='Scientific object'):
    require(isinstance(value, dict), label + ' must be an object')
    missing=set(required)-set(value)
    unexpected=set(value)-set(required)-set(optional)
    require(not missing and not unexpected,
            label + ': missing fields '+','.join(sorted(missing))+'; unexpected fields '+','.join(sorted(unexpected)))


def text(value, label, maximum=4000, empty=False):
    require(isinstance(value, str) and (empty or value.strip()) and len(value) <= maximum,
            label + ' must be bounded text')


def identifier(value):
    require(isinstance(value, str) and re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_.-]{0,79}', value),
            'Scientific identifiers must be stable simple IDs')


def string_list(value, label, maximum=16):
    require(isinstance(value, list) and len(value) <= maximum, label + ' must be a bounded list')
    for item in value:
        text(item, label, 2000)


def parse_definition(value):
    if isinstance(value,dict):
        require(len(canonical(value))<=48000,'Definition exceeds the bound')
        return deepcopy(value)
    text(value, 'Definition', 48000)
    try:
        result = json.loads(value, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
    except (ValueError, TypeError) as error:
        raise ValueError('Definition must be finite JSON') from error
    require(isinstance(result, dict), 'Definition must be a JSON object')
    return result


def hypothesis(value):
    fields(value, ('schema', 'statement', 'kind', 'assumptions', 'predictions', 'falsification',
                   'provenance', 'uncertainty'),
           ('alternative', 'independent_variables', 'dependent_variables', 'controls', 'supersedes'))
    require(value['schema'] == HYPOTHESIS, 'Unsupported hypothesis schema')
    require(value['kind'] in ('exploratory', 'empirical'), 'Hypothesis kind must be exploratory or empirical')
    text(value['statement'], 'Hypothesis statement')
    for key in ('assumptions', 'provenance'):
        string_list(value[key], key)
    text(value['falsification'], 'Observations that would count against the hypothesis', empty=value['kind']=='exploratory')
    text(value['uncertainty'], 'Measurement uncertainty and limitations')
    require(isinstance(value['predictions'], list) and len(value['predictions']) <= 16, 'Bounded predictions required')
    if value['kind'] == 'empirical':
        require(bool(value['predictions']), 'An empirical hypothesis requires a measurable prediction')
    for prediction in value['predictions']:
        fields(prediction, ('metric', 'operator', 'value', 'tolerance'))
        text(prediction['metric'], 'Prediction metric', 80)
        require(prediction['operator'] in ('gte', 'lte', 'eq'), 'Unsupported prediction comparison')
        value_type=type(prediction['value'])
        require(value_type in (str,bool,int,float), 'Prediction values must be finite numeric or categorical scalars')
        if value_type in (int,float):
            require(math.isfinite(prediction['value']), 'Prediction must be finite')
        else:
            require(prediction['operator']=='eq', 'Categorical predictions require exact comparison')
            if value_type is str:text(prediction['value'],'Categorical prediction',1000)
        require(type(prediction['tolerance']) in (int,float) and math.isfinite(prediction['tolerance']) and
                prediction['tolerance']>=0, 'Prediction tolerance must be finite and non-negative')
        if value_type in (str,bool):
            require(prediction['tolerance']==0, 'Categorical predictions do not have numeric tolerance')
    for key in ('independent_variables', 'dependent_variables', 'controls'):
        if key in value:
            string_list(value[key], key)
    if 'alternative' in value:
        text(value['alternative'], 'Competing hypothesis', empty=True)
    if 'supersedes' in value:
        require(type(value['supersedes']) is int and value['supersedes'] >= 1, 'Supersession requires an earlier revision')
    return deepcopy(value)


def protocol(value):
    fields(value, ('schema', 'hypothesis', 'revision', 'method', 'instrument', 'source', 'inputs',
                   'seeds', 'evaluator', 'success', 'stop', 'budget'), ('replicates',))
    require(value['schema'] == PROTOCOL, 'Unsupported experiment protocol')
    identifier(value['hypothesis'])
    require(type(value['revision']) is int and value['revision'] >= 1, 'Exact hypothesis revision required')
    for key in ('method', 'success', 'stop'):
        text(value[key], key)
    text(value['instrument'], 'Instrument', 80)
    text(value['source'], 'Experimental code', MAX_CODE)
    try:
        tree = ast.parse(value['source'])
    except SyntaxError as error:
        raise ValueError('Experimental Python is invalid') from error
    require(any(isinstance(node, ast.FunctionDef) and node.name == 'experiment' for node in tree.body),
            'Experimental code must define experiment(inputs)')
    require(isinstance(value['inputs'],dict) and len(canonical(value['inputs'])) <= MAX_INPUT,
            'Experimental inputs must be a bounded JSON object')
    require(isinstance(value['seeds'], list) and 1 <= len(value['seeds']) <= 32 and
            all(type(seed) is int and 0 <= seed < 2**32 for seed in value['seeds']) and
            len(set(value['seeds'])) == len(value['seeds']), 'Use 1–32 distinct bounded seeds')
    fields(value['budget'], ('seconds', 'provider_calls'))
    require(type(value['budget']['seconds']) is int and 1 <= value['budget']['seconds'] <= 60,
            'Computational execution must be bounded to 1–60 seconds')
    require(type(value['budget']['provider_calls']) is int and 0 <= value['budget']['provider_calls'] <= 48,
            'Experimental inference budget must be explicit and bounded')
    fields(value['evaluator'], ('id',))
    text(value['evaluator']['id'], 'Evaluator identity', 80)
    if 'replicates' in value:
        identifier(value['replicates'])
    result = deepcopy(value)
    result['source_digest'] = digest(value['source'])
    result['inputs_digest'] = digest(value['inputs'])
    result['protocol_digest'] = digest(value)
    return result
