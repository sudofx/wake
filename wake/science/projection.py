"""Derived scientific audit trail. No projected prose can change a verdict."""
from copy import deepcopy
import html
import json
from pathlib import Path

from ..event_format import digest
from .planner import convergence
from ..provider_pacing import scientific_request_totals


def project(state, head=None):
    science=state.get('science',{})
    hypotheses=science.get('hypotheses',{})
    experiments=science.get('experiments',{})
    rows=[]
    cost=0;unknown_durations=0
    trial_requests,unresolved_trials=scientific_request_totals(state)
    for item in experiments.values():
        invocation=state.get('invocations',{}).get(item['invocation'],{})
        delivery=invocation.get('context_delivery',{})
        proposer={key:invocation.get(key) for key in ('id','provider','model','successful_model','request_hash')}
        proposer['context_identity']={key:delivery.get(key) for key in
            ('mode','memory_digest','delivered_context_chars','delivered_request_chars')}
        evaluation=item.get('evaluation',{})
        attempts=item['attempts']
        for attempt in attempts:
            duration=attempt.get('receipt',{}).get('wall_seconds')
            if duration is None:
                unknown_durations+=1
                cost+=sum(t.get('response',{}).get('wall_seconds',0) for t in attempt.get('inference',[]))
            else:cost+=duration
        rows.append({'id':item['id'],'project':item['project'],
            'proposer':proposer,
            'question':state['projects'][item['project']]['question'],
            'hypothesis':deepcopy(hypotheses[item['protocol']['hypothesis']]),
            'frozen_predictions':deepcopy(item['predictions']), 'hypothesis_digest':item['hypothesis_digest'],
            'protocol':deepcopy(item['protocol']), 'status':item['status'],
            'executions':[{'id':a['id'],'started':a['started'],'finished':a.get('finished'),
                'inputs_digest':a['inputs_digest'],'receipt':deepcopy(a.get('receipt'))} for a in attempts],
            'environment':deepcopy(item.get('review',{}).get('environment')),
            'evaluation':deepcopy(evaluation),'interpretations':deepcopy(item['interpretations']),
            'next_steps':[deepcopy(d) for d in science.get('decisions',[]) if d['hypothesis']==item['protocol']['hypothesis']],
            'evidence_kind':'synthetic_benchmark' if item['protocol']['evaluator']['id'] in ('sort-correctness@1','hidden-relationship@1','historical-correction@1') else 'computational_observation'})
    evaluations=[e['evaluation'] for e in experiments.values() if 'evaluation' in e]
    interpretable=sum(e['measurement_validity']=='validated' and e['outcome'] in ('provisionally_supported','contradicted') for e in evaluations)
    revisions=[h for h in hypotheses.values() if len(h['revisions'])>1 and any(
        e.get('evaluation',{}).get('outcome')=='contradicted' and e['protocol']['hypothesis']==h['id'] and
        e['protocol']['revision']<len(h['revisions']) for e in experiments.values())]
    return {'schema':'wake-scientific-audit@1','source':{'head':head,'version':state['version'],'authority':'native WAKE record'},
        'enabled':science.get('enabled',False),'hypotheses':deepcopy(list(hypotheses.values())), 'investigations':rows,
        'convergence_evidence':[convergence(science,h) for h in hypotheses.values()],
        'metrics':{'hypotheses_formulated':sum(len(h['revisions']) for h in hypotheses.values()),
            'falsifiable_hypotheses':sum(r['definition']['kind']=='empirical' for h in hypotheses.values() for r in h['revisions']),
            'approved_experiments':sum(e.get('review',{}).get('environment') is not None and bool(e.get('review',{}).get('environment')) for e in experiments.values()),
            'completed_executions':sum(a['status']=='completed' for e in experiments.values() for a in e['attempts']),
            'valid_measurements':sum(e['measurement_validity']=='validated' for e in evaluations),
            'inconclusive_outcomes':sum(e['outcome']=='inconclusive' for e in evaluations),
            'contradicted_predictions':sum(p['satisfied'] is False for e in evaluations for p in e.get('predictions',[])),
            'successful_replications':sum(e['replication_status']=='replicated' for e in evaluations),
            'failed_replications':sum(e['replication_status']=='replication_failed' for e in evaluations),
            'revisions_after_negative_evidence':len(revisions),
            'verified_hypothesis_revisions':sum(any(e['protocol']['hypothesis']==h['id'] and e['protocol']['revision']==len(h['revisions']) and e.get('evaluation',{}).get('outcome')=='provisionally_supported' for e in experiments.values()) for h in revisions),
            'open_uncertainties':sum(h.get('investigation_status')!='close' for h in hypotheses.values()),
            'closed_investigations':sum(h.get('investigation_status')=='close' for h in hypotheses.values()),
            'recorded_uncertainties':len(hypotheses),
            'provider_trial_requests':trial_requests,'provider_trial_requests_unresolved':unresolved_trials,
            'known_execution_seconds':round(cost,4),'unknown_execution_durations':unknown_durations,
            'execution_seconds':None if unknown_durations else round(cost,4),
            'execution_seconds_per_interpretable_result':cost/interpretable if interpretable and not unknown_durations else None},
        'limits':['Finite computational evidence does not establish a general theorem or natural-science discovery.',
                  'Closing an investigation is an administrative stop; its recorded scientific uncertainty remains.',
                  'Execution validity, measurement validity, model interpretation and replication are separate fields.',
                  'Token and monetary costs are unavailable unless a provider reports them; they are never inferred as zero.']}


def write_report(evidence, path):
    escaped=lambda value:html.escape(json.dumps(value,indent=2,ensure_ascii=False))
    rows=[]
    for e in evidence['investigations']:
        protocol=e['protocol']
        revision=e['hypothesis']['revisions'][protocol['revision']-1]
        rows.append(f'''<article><h2>{html.escape(e['id'])}</h2>
<p>{html.escape(e['question'])}</p><p>Evidence: {html.escape(e['evidence_kind'])} · Status: {html.escape(e['status'])}</p>
<h3>Hypothesis and frozen prediction</h3><pre>{escaped(revision)}</pre><pre>{escaped(e['frozen_predictions'])}</pre>
<h3>Experimental protocol</h3><details><summary>Method, executable code and digests</summary><pre>{escaped(protocol)}</pre></details>
<h3>Proposal and context provenance</h3><details><summary>Provider, model and recorded context delivery</summary><pre>{escaped(e['proposer'])}</pre></details>
<h3>Actual execution and measurements</h3><pre>{escaped(e['executions'])}</pre>
<h3>Independent evaluation</h3><pre>{escaped(e['evaluation'] or 'Not evaluated')}</pre>
<h3>Model interpretation</h3><pre>{escaped(e['interpretations'] or 'No interpretation recorded')}</pre>
<h3>Next step and remaining uncertainty</h3><pre>{escaped(e['next_steps'] or 'No convergence decision recorded')}</pre></article>''')
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'">
<title>WAKE · Experimental research audit</title><style>body{font:16px/1.6 system-ui;background:#07141c;color:#d7eef5;max-width:1000px;margin:auto;padding:24px}article{border:1px solid #365362;padding:20px;margin:24px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}h1,h2,h3{line-height:1.3}</style>
<h1>Experimental research audit</h1><p>Recorded measurements and independent scoring are distinct from model interpretation. This page is a read-only projection.</p><p><a style="color:#9cdcff" href="index.html">Return to WAKE</a></p>'''
    page+='<pre>'+escaped(evidence['source'])+'</pre><h2>Scientific progress</h2><pre>'+escaped(evidence['metrics'])+'</pre>'
    page+='<h2>Convergence and unresolved questions</h2><pre>'+escaped(evidence.get('convergence_evidence',[]))+'</pre>'
    page+=''.join(rows) if rows else '<p>No experimental outcomes recorded.</p>'
    page+='<h2>Limits</h2><pre>'+escaped(evidence['limits'])+'</pre></html>'
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(page)
