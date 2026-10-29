"""Bounded instruments above the existing isolated runner and native writer."""
import uuid
from copy import copy
import json
import time
import hashlib
import os
from pathlib import Path

from ..event_format import digest
from ..governance import Rejected
from ..improvement_runner import DEFAULT_IMAGE, CleanupError, cleanup_containers, image_identity, run_program
from . import contracts as c
from .instruments import RUNNER, prepare, evaluate

# Capture source identity at module load; later edits cannot relabel this loaded
# executor. Hosted runs also supply their immutable checkout revision.
TRUSTED_SOURCE_DIGESTS={name:hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest()
    for name in ('workbench.py','contracts.py','state.py','instruments.py','hidden_system.py','correction.py')}
SOURCE_REVISION=os.environ.get('WAKE_SOURCE_REVISION')
TRANSPORT_SOURCE_DIGEST=hashlib.sha256((Path(__file__).parent.parent/'improvement_runner.py').read_bytes()).hexdigest()


class DockerWorkbench:
    def __init__(self,provider=None,store=None,checkpoint=None):
        self.provider=provider;self.store=store;self.checkpoint=checkpoint

    def trial_provider(self,model=None):
        """Freeze one compatible model across paired trials without fallback."""
        if not self.provider:return None
        selected=model or getattr(self.provider,'successful_model',None) or self.provider.model
        if not hasattr(self.provider,'models'):
            if selected!=self.provider.model:raise ValueError('The frozen model is unavailable from this provider')
            return self.provider
        if selected not in self.provider.models:raise ValueError('The frozen model is no longer in the approved provider chain')
        provider=copy(self.provider)
        provider.model=selected;provider.models=[selected];provider.request_limit=1
        provider.config={**getattr(provider,'config',{}),'model':selected,'gemini_fallback_models':[]}
        return provider

    def environment(self):
        environment={'image':DEFAULT_IMAGE,'image_id':image_identity(DEFAULT_IMAGE),'network':'none',
                'user':'65534:65534','memory_bytes':134217728,'cpus':.5,'process_limit':32,
                'output_limit':65536,'runtime_limit_seconds':60,'runner_digest':digest(RUNNER),
                'receipt_schema':c.EXECUTION,'replication_criterion':'measurement-profile@1',
                'prediction_comparison':'typed-scalars@1',
                'transport_source_digest':TRANSPORT_SOURCE_DIGEST,
                'trusted_source_digests':dict(TRUSTED_SOURCE_DIGESTS),'source_revision':SOURCE_REVISION}
        if self.provider:
            provider=self.trial_provider()
            environment.update(provider=provider.name,model=provider.model,provider_charged=provider.charged,trial_accounting=2,
                provider_configuration_digest=digest({key:value for key,value in getattr(provider,'config',{}).items()
                    if key in ('max_output_tokens','timeout_seconds','model','gemini_fallback_models')}))
        return environment

    def execute(self, item):
        execution_started=time.monotonic()
        attempt=item['attempts'][-1]
        result=run_program(item['protocol']['source'],attempt['execution_inputs'],item['review']['environment']['image_id'],
            timeout=item['protocol']['budget']['seconds'],name=attempt['containers'][0],runner=RUNNER)
        if item['protocol']['instrument']!='model-comparison' or result['status']!='completed':return result
        def failed(reason):
            return {'status':'failed','reason':reason,'wall_seconds':round(time.monotonic()-execution_started,4),
                'cleanup_confirmed':result['cleanup_confirmed'],
                'preparation_outputs':result['outputs'],'preparation_outputs_digest':digest(result['outputs'])}
        # Candidate code can prepare data only. It cannot change randomized
        # tasks, prompt conditions, scorer, provider config or paid-call count.
        if result['outputs'] not in (attempt['execution_inputs']['trials'],attempt['execution_inputs']):
            return failed('Preparation code altered the frozen paired trial inputs')
        from .correction import request
        rows=[]
        try:provider=self.trial_provider(item['review']['environment']['model'])
        except ValueError as error:return failed(str(error))
        previous=getattr(provider,'record_attempt',None)
        gate=getattr(provider,'request_gate',None)
        previous_purpose=getattr(gate,'purpose',None) if gate else None
        # One provider implementation/model, one request per trial; no fallback.
        if hasattr(provider,'models') and provider.models!=[provider.model]:
            return failed('Paired trials require a single model without fallback')
        try:
            if gate:gate.purpose='experiment'
            for trial in attempt['execution_inputs']['trials']:
                limits=getattr(provider,'config',{}).get('model_daily_call_limits',{})
                if provider.charged and provider.model in limits:
                    from datetime import datetime
                    from ..provider_pacing import native_usage, PACIFIC
                    day=datetime.now(PACIFIC).date().isoformat()
                    usage,_=native_usage(self.store.load(),day)
                    if usage.get(provider.model,0)>=limits[provider.model]:
                        raise ValueError('Frozen trial model daily allowance exhausted; no new trial call made')
                transport_attempts=[]
                def account(phase,evidence):
                    if phase=='started':transport_attempts.append(dict(evidence))
                    elif transport_attempts:transport_attempts[-1].update(evidence)
                if hasattr(provider,'record_attempt'):provider.record_attempt=account
                req=request(trial);invocation='science-'+uuid.uuid4().hex
                _append(self.store,'experiment_inference_started',item,attempt=attempt['id'],trial=trial['id'],
                    evidence={'request':req,'request_digest':digest(req),'provider':provider.name,'model':provider.model,'invocation':invocation})
                lifecycle=self.store.begin_invocation_lifecycle(invocation,req,provider.name,provider.model)
                started=time.monotonic()
                if hasattr(provider,'provider_requests_sent'):provider.provider_requests_sent=0
                try:
                    raw,metadata=lifecycle.invoke(lambda:provider.propose(req),effect_barrier=self.checkpoint)
                except Exception:
                    _append(self.store,'experiment_inference_finished',item,attempt=attempt['id'],trial=trial['id'],
                        evidence={'raw':'','metadata':{'transport_failed':True,'provider_attempts':transport_attempts,
                            'provider_requests_sent':getattr(provider,'provider_requests_sent',1)},
                                  'wall_seconds':round(time.monotonic()-started,4)})
                    if self.checkpoint:self.checkpoint()
                    raise
                lifecycle.proposal_received(digest(raw))
                elapsed=round(time.monotonic()-started,4)
                metadata={key:value for key,value in metadata.items() if key in ('usage','model_version','monetary_cost','fixture')}
                metadata['provider_attempts']=transport_attempts
                metadata['provider_requests_sent']=getattr(provider,'provider_requests_sent',1)
                _append(self.store,'experiment_inference_finished',item,attempt=attempt['id'],trial=trial['id'],
                    evidence={'raw':raw,'metadata':metadata,'wall_seconds':elapsed})
                lifecycle.governed(digest(raw),None,'untrusted measurement recorded; scientific scoring pending')
                lifecycle.complete(outcome='success',detail='untrusted measurement received: '+digest(raw))
                if self.checkpoint:self.checkpoint()
                rows.append({'id':trial['id'],'answer':json.loads(raw),'metadata':metadata,'wall_seconds':elapsed})
        except Exception as error:
            return failed('Inference trial failed: '+type(error).__name__+': '+str(error)[:500])
        finally:
            if hasattr(provider,'record_attempt'):provider.record_attempt=previous
            if gate:
                if previous_purpose is None:
                    del gate.purpose
                else:gate.purpose=previous_purpose
        return {'status':'completed','outputs':{'trials':rows},'cleanup_confirmed':result['cleanup_confirmed'],
                'wall_seconds':round(time.monotonic()-execution_started,4)}

    def cleanup(self, names):
        cleanup_containers(names)


def _append(store, kind, item=None, **payload):
    state=store.load()
    return store.append(kind, {'schema':c.SCHEMA,'base_version':state['version'],
        **({'id':item['id'],'protocol_digest':item['protocol']['protocol_digest']} if item else {}), **payload})


def advance(store, workbench=None, *, enabled=None, checkpoint=None, crash_at=None,provider=None):
    """One bounded native transition/effect sequence at an idle invocation boundary.

    The caller holds the ordinary research writer lock. Running attempts from an
    earlier process are cleaned up, never silently retried or given measurements.
    """
    workbench=workbench or DockerWorkbench(provider,store,checkpoint)
    state=store.load()
    if state['pending'] is not None:
        raise Rejected('Scientific execution requires an idle research invocation')
    science=state.get('science')
    if enabled is not None and (science or enabled) and (not science or science['enabled']!=enabled):
        _append(store,'scientific_configured',actor='operator',enabled=enabled)
        state=store.load();science=state['science']
    if not science:
        return None
    # Cleanup remains available after permission revocation. It authorizes no new experiment.
    for item in sorted(science['experiments'].values(),key=lambda e:(e['accepted_version'],e['id'])):
        if item['status'] not in ('running','cleanup_required'):
            continue
        attempt=item['attempts'][-1]
        try:
            workbench.cleanup(attempt['containers'])
        except (CleanupError,OSError) as error:
            if item['status']=='running':
                receipt={'status':'cleanup_required','reason':str(error)[:1000],
                         'protocol_digest':item['protocol']['protocol_digest'],'inputs_digest':attempt['inputs_digest']}
                _append(store,'experiment_interrupted',item,attempt=attempt['id'],receipt=receipt)
            return {'status':'cleanup_required','id':item['id']}
        if item['status']=='cleanup_required':
            # Recovery is completed through a new interruption event, not a forged successful execution.
            receipt={'status':'interrupted','reason':'Confirmed removal of reserved containers; no measurements asserted',
                     'protocol_digest':item['protocol']['protocol_digest'],'inputs_digest':attempt['inputs_digest']}
        else:
            receipt={'status':'interrupted','reason':'Execution owner was interrupted; reserved containers removed',
                     'protocol_digest':item['protocol']['protocol_digest'],'inputs_digest':attempt['inputs_digest']}
        _append(store,'experiment_interrupted',item,attempt=attempt['id'],receipt=receipt)
        return {'status':'interrupted','id':item['id']}
    if not science['enabled']:
        return None
    for item in sorted(science['experiments'].values(),key=lambda e:(e['accepted_version'],e['id'])):
        if item['status']=='completed':
            report=evaluate(item)
            _append(store,'experiment_evaluated',item,attempt=item['attempts'][-1]['id'],evaluation=report)
            return {'status':'evaluated','id':item['id'],'evaluation':report}
        if item['status'] not in ('proposed','approved'):
            continue
        if item['status']=='proposed':
            try:
                inputs,protected=prepare(item['protocol'])
                if item['protocol']['instrument']=='model-comparison' and not getattr(workbench,'provider',None):
                    raise ValueError('Compatible inference provider unavailable for paired trials')
                environment=workbench.environment()
                if item['protocol'].get('replicates'):
                    prior=science['experiments'][item['protocol']['replicates']]
                    protected['replication_outputs_digest']=prior['attempts'][-1]['receipt']['outputs_digest']
                    if environment.get('replication_criterion')=='measurement-profile@1':
                        protected['replication_metrics_digest']=digest(prior['evaluation']['metrics'])
            except (ValueError,Rejected,OSError) as error:
                _append(store,'experiment_reviewed',item,decision='blocked',reason=str(error)[:1000],environment={},protected={})
                return {'status':'blocked','id':item['id'],'reason':str(error)[:1000]}
            _append(store,'experiment_reviewed',item,decision='approved',reason='Bounded installed instrument and scorer; frozen protocol validated',
                    environment=environment,protected=protected)
            item=store.load()['science']['experiments'][item['id']]
        else:
            inputs,_=prepare(item['protocol'])
            try:
                current_environment=workbench.environment()
                if current_environment!=item['review']['environment']:
                    raise ValueError('Trusted execution environment changed after review; no effect was started')
            except (ValueError,Rejected,OSError) as error:
                _append(store,'experiment_reviewed',item,decision='blocked',reason=str(error)[:1000],environment={},protected={})
                return {'status':'blocked','id':item['id'],'reason':str(error)[:1000]}
        attempt=uuid.uuid4().hex
        name='wake-improve-science-'+attempt
        _append(store,'experiment_started',item,attempt=attempt,containers=[name],execution_inputs=inputs,inputs_digest=digest(inputs))
        if checkpoint:
            checkpoint()  # A failed durability barrier prevents the computational effect.
        if crash_at=='before-execution':
            raise InterruptedError('Injected interruption before computational effect')
        item=store.load()['science']['experiments'][item['id']]
        try:
            execution=workbench.execute(item)
        except CleanupError:
            # Leave the reserved attempt running so recovery must confirm cleanup.
            raise
        if crash_at=='after-execution':
            raise InterruptedError('Injected interruption before result persistence')
        receipt={**execution,'schema':c.EXECUTION,'protocol_digest':item['protocol']['protocol_digest'],
                 'attempt_id':attempt,
                 'source_digest':item['protocol']['source_digest'],
                 'environment_digest':digest(item['review']['environment']),
                 'inputs_digest':item['attempts'][-1]['inputs_digest']}
        if receipt['status']=='completed':
            receipt['outputs_digest']=digest(receipt['outputs'])
        _append(store,'experiment_executed',item,attempt=attempt,receipt=receipt)
        if checkpoint:
            checkpoint()
        return {'status':receipt['status'],'id':item['id']}
    return None
