"""Explicit fresh-record investigations; never reset an existing installation."""
import json
from pathlib import Path

from ..engine import DEFAULTS, Engine, config
from ..event_format import digest
from ..governance import require
from ..providers import Gemini
from ..record_store import RecordStore
from .hidden_system import observations
from .projection import project as scientific_projection, write_report


def configure_parser(sub):
    parser = sub.add_parser('science', help='Run or inspect governed computational research')
    commands = parser.add_subparsers(dest='science_command', required=True)
    investigation = commands.add_parser('investigate', help='Begin a bounded investigation in a NEW disposable native record')
    investigation.add_argument('--output', required=True)
    investigation.add_argument('--question', help='Unresolved computational question; defaults to a hidden-system benchmark')
    investigation.add_argument('--instance', type=int, default=17)
    investigation.add_argument('--calls', type=int, default=4, help='Maximum live provider calls, 1–12')
    investigation.add_argument('--model', help='Use a model from the configured approved Gemini chain')
    resume=commands.add_parser('resume',help='Continue an existing disposable investigation from its native record')
    resume.add_argument('--output',required=True)
    resume.add_argument('--calls',type=int,default=4)
    resume.add_argument('--model')
    demonstration=commands.add_parser('demonstrate',help='Run a scripted fixture with real isolated computation; zero live model calls')
    demonstration.add_argument('--output',required=True)
    demonstration.add_argument('--benchmark',choices=['correction','revision'],required=True)
    demonstration.add_argument('--instance',type=int,default=17)
    schema=commands.add_parser('schemas',help='Export the versioned portable scientific JSON Schemas')
    schema.add_argument('--output',required=True)
    report = commands.add_parser('report', help='Read native scientific evidence without provider calls')
    report.add_argument('--output', required=True)


def initialize(root, settings, question, instrument_binding=None):
    require(not root.exists(), 'Scientific investigation output must be new; existing records are never overwritten')
    root.mkdir(parents=True)
    experiment_settings = {**DEFAULTS, **settings, 'experimental_research_enabled': True,
        'same_wake_research': False, 'research_google_search': False,
        'research_topics': [{'id':'experimental-methods','label':'Experimental methods',
            'query':'computational experimental methods','seed_question':question[:600],'source_kind':'web','enabled':True}],
        'mission':question, 'objective':question, 'memory_mode':'active', 'decision_memory_mode':'active',
        'max_context_chars':64000, 'max_output_tokens':8192, 'gemini_fallback_models':[],
        'inquiry_drive_enabled':False, 'autonomous_context_improvement':False}
    engine = Engine(root/'record', experiment_settings, store=RecordStore(root/'record', initialize_empty=True))
    (root/'settings.json').write_text(json.dumps(experiment_settings,indent=2))
    with engine.store.lock():
        engine.initialize()
        invocation, request = engine.start('operator-fixture','scientific-question-initialization')
        result = engine.finish(invocation,json.dumps({'base_version':request['context']['version'],
            'title':'Open a controlled computational investigation','summary':'Operator supplies only the unresolved question; no hypothesis, code or revised explanation supplied.',
            'actions':[{'type':'project','id':'investigation','title':'Controlled computational investigation',
                'question':question,'domain':'experimental-methods','status':'active',
                'next_step':'Formulate a falsifiable hypothesis and propose a computational test.',
                'reason':'Explicit bounded scientific investigation'}]}))
        require(result['status']=='accepted', 'Scientific question initialization rejected: '+str(result))
        if instrument_binding:
            from .contracts import SCHEMA
            state=engine.store.load()
            engine.store.append('scientific_configured',{'schema':SCHEMA,'base_version':state['version'],
                'actor':'operator','enabled':True,'instrument_binding':instrument_binding})
    return engine


def investigate(output, settings, *, question=None, instance=17, calls=4, provider=None):
    require(type(calls) is int and 1<=calls<=12, 'Use an explicit budget of 1–12 planning calls')
    require(type(instance) is int and 0<=instance<2**32, 'Invalid hidden-system instance')
    instrument_binding={'evaluator':'hidden-relationship@1','instance':instance} if question is None else None
    question = question or (
        f'What input-output relationship governs artificial instrument instance {instance}? '
        f'Initial observations: {json.dumps(observations(instance))}. '
        'Infer an initial explanation from these observations and freeze testable predictions before execution. '
        'Use hidden-relationship@1 with this instance. Choose probes that can distinguish explanations beyond the observed range. '
        'Author Python experiment(inputs) that predicts responses for probes and holdout inputs. '
        'After actual measurements challenge a prediction, preserve it, revise the explanation from the new observations, '
        'and design a fresh-seed follow-up. The true mechanism is withheld. Do not claim discovery from a favorable finite test alone. '
        'Interpret actual results, state uncertainty, then propose a replication or close/suspend with a reason.')
    root=Path(output).resolve()
    engine=initialize(root,settings,question,instrument_binding)
    provider=provider or Gemini(engine.config)
    return drive(engine,root,question,calls,provider)


def drive(engine,root,question,calls,provider):
    require(type(calls) is int and 1<=calls<=12, 'Use an explicit budget of 1–12 planning calls')
    results=[]
    used=0
    try:
        for _ in range(calls*4+4):
            # Finish deterministic work even when the inference allowance is spent.
            science=engine.store.load().get('science',{})
            pending=any(e['status'] in ('proposed','approved','running','completed','cleanup_required')
                        for e in science.get('experiments',{}).values())
            if used>=calls and not pending:break
            result=engine.run(provider)
            results.append(result)
            if not result.get('scientific_research'):
                used+=max(1,getattr(provider,'provider_requests_sent',1))
            summary={'step':len(results),'status':result['status'],'id':result.get('id')}
            if result.get('reason'):summary['reason']=result['reason'][:500]
            print(json.dumps(summary),flush=True)
            if result['status'] in ('deferred','failed','cleanup_required'):break
            science=engine.store.load().get('science',{})
            if science.get('decisions') and science['decisions'][-1]['decision'] in ('close','suspend') and not pending:break
        state,head=engine.store.audit()
        evidence=scientific_projection(state,head)
        report={'schema':'wake-scientific-investigation-run@1','fixture':not provider.charged,
            'provider':provider.name,'model':provider.model,'planning_calls':used,'budget_calls':calls,
            'replay_verified':True,'head':head,'record':str(engine.store.path),
            'question':question,'steps':results,'evidence':evidence}
        (root/'result.json').write_text(json.dumps(report,indent=2))
        archive=root/'runs';archive.mkdir(exist_ok=True)
        (archive/(digest(report)+'.json')).write_text(json.dumps(report,indent=2))
        write_report(evidence,root/'scientific-research.html')
        return report
    finally:
        engine.store.close()


def execute(args):
    if args.science_command=='schemas':
        from .schemas import documents
        path=Path(args.output);path.mkdir(parents=True,exist_ok=True)
        for name,document in documents().items():(path/(name+'.json')).write_text(json.dumps(document,indent=2)+'\n')
        return {'schemas':list(documents()),'output':str(path.resolve())}
    if args.science_command=='demonstrate':
        from .fixtures import BenchmarkFixture
        question=None if args.benchmark=='revision' else 'Does relevant historical context improve correction of previous errors in a prespecified paired A/B/C task family?'
        return investigate(args.output,DEFAULTS,question=question,instance=args.instance,calls=6,
            provider=BenchmarkFixture(args.benchmark,args.instance))
    if args.science_command=='resume':
        root=Path(args.output).resolve()
        require((root/'settings.json').is_file() and (root/'record/wake.sqlite').is_file(),
                'Resume requires an existing scientific investigation and its saved settings')
        settings=json.loads((root/'settings.json').read_text())
        if args.model:
            approved=config(args.config)
            require(args.model in {approved['model'],*approved.get('gemini_fallback_models',[])},'Model is not in approved chain')
            settings['model']=args.model
        engine=Engine(root/'record',settings,store=RecordStore(root/'record'))
        question=next(iter(engine.store.load()['projects'].values()))['question']
        return drive(engine,root,question,args.calls,Gemini(settings))
    if args.science_command=='investigate':
        settings=config(args.config)
        approved={settings['model'],*settings.get('gemini_fallback_models',[])}
        if args.model:
            require(args.model in approved,'Select a model from the approved configured Gemini chain')
            settings['model']=args.model
        return investigate(args.output,settings,question=args.question,instance=args.instance,calls=args.calls)
    from ..authority import open_authoritative_store
    store=open_authoritative_store(args.data or 'data')
    try:
        state,head=store.audit()
        evidence=scientific_projection(state,head)
        write_report(evidence,Path(args.output))
        return evidence
    finally:store.close()
