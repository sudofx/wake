"""Portable JSON Schemas; deterministic validators remain authoritative."""
from copy import deepcopy
from . import contracts as c

def obj(properties,optional=()):
    return {'type':'object','properties':properties,'required':[k for k in properties if k not in optional],
            'additionalProperties':False}

TEXT={'type':'string','maxLength':4000}
TEXTS={'type':'array','items':TEXT,'maxItems':16}
PREDICTION=obj({'metric':{'type':'string','maxLength':80},'operator':{'type':'string','enum':['gte','lte','eq']},
    'value':{'anyOf':[{'type':'number'},{'type':'boolean'},{'type':'string'}]},
    'tolerance':{'type':'number','minimum':0}})
HYPOTHESIS=obj({'schema':{'type':'string','enum':[c.HYPOTHESIS]},'statement':TEXT,
    'kind':{'type':'string','enum':['empirical','exploratory']},'assumptions':TEXTS,
    'predictions':{'type':'array','items':PREDICTION,'maxItems':16},'falsification':TEXT,
    'provenance':TEXTS,'uncertainty':TEXT,'alternative':TEXT,'independent_variables':TEXTS,
    'dependent_variables':TEXTS,'controls':TEXTS,'supersedes':{'type':'integer','minimum':1}},
    ('alternative','independent_variables','dependent_variables','controls','supersedes'))
PROTOCOL=obj({'schema':{'type':'string','enum':[c.PROTOCOL]},'hypothesis':{'type':'string'},
    'revision':{'type':'integer','minimum':1},'method':TEXT,'instrument':{'type':'string'},
    'source':{'type':'string','maxLength':c.MAX_CODE},'inputs':{'type':'object'},
    'seeds':{'type':'array','items':{'type':'integer','minimum':0,'maximum':2**32-1},'minItems':1,'maxItems':32},
    'evaluator':obj({'id':{'type':'string'}}),'success':TEXT,'stop':TEXT,
    'budget':obj({'seconds':{'type':'integer','minimum':1,'maximum':60},
                  'provider_calls':{'type':'integer','minimum':0,'maximum':48}}),'replicates':{'type':'string'}},('replicates',))

DIGEST={'type':'string','pattern':'^[0-9a-f]{64}$'}
EXECUTION={'type':'object','required':['schema','status','protocol_digest','source_digest','environment_digest','inputs_digest','attempt_id'],
    'properties':{'schema':{'const':c.EXECUTION},'status':{'enum':['completed','failed']},
        **{key:DIGEST for key in ('protocol_digest','source_digest','environment_digest','inputs_digest','outputs_digest')},
        'attempt_id':{'type':'string'},'outputs':{},'reason':TEXT,'wall_seconds':{'type':'number','minimum':0},
        'output_bytes':{'type':'integer','minimum':0},'cleanup_confirmed':{'type':'boolean'}},
    'allOf':[{'if':{'properties':{'status':{'const':'completed'}}},'then':{'required':['outputs','outputs_digest']}}]}
EVALUATION={'type':'object','required':['schema','protocol_digest','evaluator','execution_valid','outputs_digest',
    'replication_status','measurement_validity','outcome','metrics'],
    'properties':{'schema':{'const':c.EVALUATION},'protocol_digest':DIGEST,'outputs_digest':DIGEST,
        'evaluator':{'type':'string'},'execution_valid':{'const':True},
        'measurement_validity':{'enum':['validated','unvalidated','invalid']},
        'outcome':{'enum':['provisionally_supported','contradicted','inconclusive','invalid_measurement']},
        'replication_status':{'enum':['not_attempted','replicated','replication_failed','inconclusive']},'metrics':{'type':'object'}}}

def documents():
    return {name:{'$schema':'https://json-schema.org/draft/2020-12/schema','$id':name,**deepcopy(value)}
            for name,value in ((c.HYPOTHESIS,HYPOTHESIS),(c.PROTOCOL,PROTOCOL),(c.EXECUTION,EXECUTION),(c.EVALUATION,EVALUATION))}

def action_definition(kind):
    if kind=='hypothesis':return deepcopy(HYPOTHESIS)
    if kind=='experiment':return {'anyOf':[deepcopy(PROTOCOL),obj({'schema':{'const':c.PROTOCOL},'replicates':{'type':'string'}})]}
    if kind=='experiment_interpretation':return obj({key:TEXT for key in ('experiment','interpretation','limitations','next_step')})
    if kind=='research_direction':return obj({'next':{'type':'string','enum':['collect','experiment']},
        **{key:TEXT for key in ('reason','uncertainty','cost','stop')}})
    return obj({'decision':{'type':'string','enum':['continue','suspend','close']},
        **{key:TEXT for key in ('hypothesis','uncertainty','reason','next_experiment','cost','stop_condition')}})
