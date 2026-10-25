"""A fully automatic policy change in an explicitly new disposable native record."""
import html
import json
from pathlib import Path

from .autonomous_context import status
from .engine import DEFAULTS, Engine
from .event_format import digest
from .governance import require
from .record_store import RecordStore


def settings():
    return {**DEFAULTS, 'mission': 'Controlled context-selection demonstration; synthetic inputs, not scientific research.',
            'research_topics': [{'id': 'memory', 'label': 'Memory', 'query': 'memory commitments',
                                 'seed_question': 'Which recorded work should receive context?',
                                 'source_kind': 'web', 'enabled': True}], 'decision_memory_mode': 'active',
            'memory_mode': 'active', 'max_context_chars': 64000}


def seed(engine, *, commitment_project='z'):
    """Fixture data crosses the ordinary proposal/governance boundary."""
    invocation, request = engine.start('fixture', 'autonomous-context-demo')
    actions = [dict(type='project', id=key, title='Synthetic project ' + key,
                    question='Compare the recorded alternatives for ' + key, domain='memory', status='active',
                    next_step='Review sources for ' + key, reason='Controlled selection fixture') for key in ('a', 'z')]
    actions.append(dict(type='commit', id='due', project=commitment_project, due_cycle=2,
                        task='Review the recorded evidence for the promised project.', reason='Controlled inherited obligation'))
    result = engine.finish(invocation, json.dumps(dict(base_version=request['context']['version'],
                           title='Prepare a controlled fixture', summary='Two projects and one near-term commitment.', actions=actions)))
    require(result['status'] == 'accepted', 'Demonstration seed failed governance')


def demonstrate(output):
    root = Path(output).resolve()
    require(not root.exists(), 'Autonomous demonstration output must be new')
    root.mkdir(parents=True)
    engine = Engine(root / 'record', settings(), store=RecordStore(root / 'record', initialize_empty=True))
    try:
        with engine.store.lock():
            engine.initialize()
            seed(engine)
            before = engine.store.load()
            before_cycles = before['version']
            prefix = list(engine.store.events())
            # A one-time deployment grant, standing in for the installed setting.
            # No human/model provides or reviews the subsequent proposal.
            engine.config['autonomous_context_improvement'] = True
            invocation, request = engine.start('fixture', 'autonomous-context-demo')
            after = engine.store.load()
            adaptation = status(after)
            receipt = after['invocations'][invocation]['context_delivery']['decision_memory']
            selected = receipt['capsule']['decision_context']['project_id']
            require(adaptation['adoptions'] == 1 and selected == 'z' and after['version'] == before_cycles,
                    'Autonomous adoption did not affect delivered context correctly')
            result = engine.finish(invocation, json.dumps(dict(base_version=request['context']['version'],
                                  title='Continue the selected synthetic project', summary='Revise its next step; the obligation remains open.',
                                  actions=[dict(type='project', id='z', title='Synthetic project z',
                                                question='Compare the recorded alternatives for z', domain='memory', status='active',
                                                next_step='Compare provenance before revising the claim.',
                                                reason='Controlled next-step update after selection.')])) )
            require(result['status'] == 'accepted', 'Demonstration completion failed governance')
            final, head = engine.store.audit()
            require(engine.store.events()[:len(prefix)] == prefix, 'Prior history changed during adaptation')
            data = {'schema': 'autonomous-context-demo@1', 'fixture': True, 'model_calls': 0,
                    'human_reviews': 0, 'proposals_supplied_by_human': 0, 'replay_verified': True,
                    'earlier_history_preserved': True, 'head': head,
                    'research_cycles_before_adoption': before_cycles,
                    'research_cycles_after_adoption': after['version'],
                    'completed_fixture_cycles': final['version'], 'delivered_project': selected,
                    'invocation_policy_revision': after['invocations'][invocation]['autonomous_context_revision'],
                    'adaptation': adaptation, 'record': str(engine.store.path)}
    finally:
        engine.store.close()
    (root / 'result.json').write_text(json.dumps(data, indent=2))
    escaped = html.escape(json.dumps(data, indent=2))
    measurement = data['adaptation']['last_trial']['measurement']
    rows = ''.join(f'<tr><th>{name.title()}</th><td>{measurement[name]["before"]["passed"]} / {measurement[name]["before"]["total"]}</td>'
                   f'<td>{measurement[name]["after"]["passed"]} / {measurement[name]["after"]["total"]}</td></tr>'
                   for name in ('development', 'holdout'))
    page = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'">
<title>WAKE · Autonomous improvement</title><style>
*{{box-sizing:border-box}}body{{font:16px/1.6 system-ui,sans-serif;color:#183036;background:#f3f6f5;max-width:920px;margin:auto;padding:24px}}
h1{{font-size:clamp(30px,5vw,44px);line-height:1.2}}section{{background:white;padding:24px;border:1px solid #dbe3df;border-radius:16px;margin:24px 0}}
.label{{font-size:12px;letter-spacing:.12em;color:#526b60}}table{{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}}th,td{{padding:10px;text-align:left;border-bottom:1px solid #dbe3df}}
pre{{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px;max-height:500px;overflow:auto}}summary{{cursor:pointer}}code{{overflow-wrap:anywhere}}
</style><body><p class="label">WAKE · BOUNDED AUTONOMY</p><h1>An improvement adopted<br>without a human review.</h1>
<section><h2>Propose → measure → adopt → use</h2><p>WAKE read an obligation in its own record, generated a deadline-aware selection policy,
tested it, and began using it in the next model context. No person supplied the proposal or approved the change.</p>
<p><strong>Allowed change:</strong> one context-selection policy. <strong>Delivered result:</strong> project z, which owned the near-term obligation, received context priority.</p>
<table><tr><th>Fixed task</th><th>Before</th><th>After</th></tr>{rows}<tr><th>Current native fixture</th><td>Wrong project</td><td>Promised project</td></tr></table></section>
<section><h2>What can change</h2><p>The system can adopt the installed deadline-priority selector only after every benchmark case passes,
both suites improve, and the current native record also shows an improvement. Quota, governance, evaluator, permissions and executable source stay outside its change authority.</p>
<p>It monitors delivered context and matched provider/model outcomes. A guardrail failure or a drop of at least two accepted outcomes in matched eight-outcome windows triggers rollback and quarantines this change.</p>
<p>These are controlled synthetic inputs in a new native record. They demonstrate the autonomous mechanism, not a general intelligence gain or an improvement already running in hosted research.</p></section>
<section><h2>The record remains accountable</h2><p>Zero model calls · zero per-change human reviews · earlier history preserved · native replay verified.
The policy adoption itself added zero research cycles.</p><details><summary>Exact recorded demonstration</summary><pre>{escaped}</pre></details></section></body></html>'''
    (root / 'autonomous.html').write_text(page)
    return {**data, 'report': str(root / 'autonomous.html'), 'result_digest': digest(data)}
