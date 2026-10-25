"""Bounded autonomous behavior changes on the native research record.

Version 1 can change ONE selector policy from alphabetical to deadline-priority.
The interpreter, benchmark, permissions, budgets and governance are installed
code, never candidate input. Trials are pure computations; no model, generated
Python, network or deployment effect is needed. Research versions do not advance.
"""
from copy import deepcopy
import secrets

from .decision_memory import decision_context
from .event_format import digest
from .governance import require
from .improvement_tasks import TASK, cases, expected

SCHEMA = 'autonomous-context@1'
BASELINE = {'selector': 'alphabetical'}
CANDIDATE = {'selector': 'deadline-priority'}
TRIAL_INTERVAL = 10
WINDOW = 8
REGRESSION_DROP = 2


def validate_settings(settings):
    enabled = settings.get('autonomous_context_improvement', False)
    require(type(enabled) is bool, 'autonomous_context_improvement must be boolean')
    require(not enabled or settings.get('decision_memory_mode', 'off') == 'active',
            'Autonomous context improvement requires active decision memory')
    return enabled


def validate_policy(policy):
    require(isinstance(policy, dict) and set(policy) == {'selector'}
            and policy['selector'] in ('alphabetical', 'deadline-priority'),
            'Policy may change only the installed context selector')
    return policy


def initial():
    return {'schema': SCHEMA, 'enabled': False, 'policy': dict(BASELINE), 'revision': 0,
            'trials': 0, 'adoptions': 0, 'rollbacks': 0, 'quarantined': False,
            'last_trial_version': None, 'last_trial': None, 'last_rollback': None}


def policy_for(state, enabled):
    current = state.get('autonomous_context')
    if not enabled or not current or not current['enabled']:
        return dict(BASELINE)
    return dict(validate_policy(current['policy']))


def basis(state):
    """Native obligations and their project/notebook pointers, never public views."""
    projects = state.get('projects', {})
    result = []
    for key, c in sorted(state.get('commitments', {}).items()):
        due, project = c.get('due_cycle'), c.get('project')
        if (c.get('status') == 'open' and type(due) is int and due <= state['version'] + 2
                and project in projects and projects[project].get('status') == 'active'):
            result.append({'kind': 'commitment', 'id': key, 'digest': digest(c), 'project': project})
    for key, notebook in sorted(state.get('notebooks', {}).items()):
        if notebook.get('project') in {r['project'] for r in result}:
            result.append({'kind': 'notebook', 'id': key, 'digest': digest(notebook), 'project': notebook['project']})
        if len(result) >= 8:
            break
    return result[:8]


def summary_score(population, policy):
    passed = sum(decision_context(c['state'], c['question'], selection_policy=policy) == expected(c)
                 for c in population)
    return {'passed': passed, 'total': len(population)}


def measure(state, before, after, seed):
    result = {'metric': TASK, 'development': {}, 'holdout': {}}
    for name, population in [('development', cases(7, 12)), ('holdout', cases(seed, 60))]:
        result[name] = {'before': summary_score(population, before), 'after': summary_score(population, after)}
    native = {'id': 'native-record', 'state': state, 'question': None}
    previous = decision_context(state, selection_policy=before)
    candidate = decision_context(state, selection_policy=after)
    target = expected(native)
    result['native'] = {'before': int(previous == target), 'after': int(candidate == target),
                        'before_project': previous['project_id'], 'after_project': candidate['project_id'],
                        'expected_project': target['project_id']}
    return result


def qualifies(measurement):
    return (all(measurement[s]['after']['passed'] == measurement[s]['after']['total']
                and measurement[s]['after']['passed'] > measurement[s]['before']['passed']
                for s in ('development', 'holdout'))
            and measurement['native']['after'] > measurement['native']['before'])


def model_group(invocation):
    return (invocation.get('provider'), invocation.get('successful_model') or invocation.get('model'),
            invocation.get('phase', 'proposal'))


def windows(state, revision):
    grouped = {}
    # Projection JSON canonicalizes mapping keys; semantic replay inserts by
    # event order. Explicit time/ID order must agree across both representations.
    ordered = sorted(state.get('invocations', {}).values(), key=lambda i: (i.get('time', ''), i['id']))
    for invocation in ordered:
        if (invocation.get('phase', 'proposal') != 'proposal'
                or invocation.get('status') not in ('accepted', 'rejected')
                or not invocation.get('context_delivery', {}).get('decision_memory', {}).get('delivered')
                or invocation.get('autonomous_context_revision', 0) != revision):
            continue
        key = model_group(invocation)
        group = grouped.setdefault(key, [])
        group.append({'id': invocation['id'], 'accepted': invocation['status'] == 'accepted'})
    return [{'group': list(group), 'observations': rows[-WINDOW:]} for group, rows in sorted(
        grouped.items(), key=lambda pair: str(pair[0])) if len(rows) >= WINDOW]


def rollback_reason(state):
    current = state['autonomous_context']
    try:
        actual = decision_context(state, selection_policy=current['policy'])
        target = expected({'state': state, 'question': None})
        if actual != target:
            return {'kind': 'context_guardrail', 'actual_digest': digest(actual), 'expected_digest': digest(target),
                    'actual_project': actual.get('project_id') if isinstance(actual, dict) else None,
                    'expected_project': target['project_id']}
    except Exception as error:
        return {'kind': 'context_execution', 'error_type': type(error).__name__}
    before = {tuple(row['group']): row['observations'] for row in current['baseline_windows']}
    for row in windows(state, current['revision']):
        group = tuple(row['group'])
        if group in before:
            old, new = before[group], row['observations']
            if sum(r['accepted'] for r in new) + REGRESSION_DROP <= sum(r['accepted'] for r in old):
                return {'kind': 'observed_acceptance_regression', 'group': list(group),
                        'before': old, 'after': new,
                        'interpretation': 'Matched provider/model/phase observation; not causal proof.'}
    return None


def reduce(state, event):
    """Deterministic application policy. Historical meanings stay versioned here."""
    p = event['payload']
    require(isinstance(p, dict) and p.get('schema') == SCHEMA, 'Invalid autonomous context schema')
    require(state.get('pending') is None, 'Cannot change context policy during an invocation')
    require(p.get('base_version') == state['version'] and p.get('based_on_head') == event['prev_hash'],
            'Autonomy decision is not bound to the current native record')
    current = deepcopy(state.get('autonomous_context') or initial())
    if event['kind'] == 'autonomous_context_configured':
        require(set(p) == {'schema', 'actor', 'enabled', 'base_version', 'based_on_head'}, 'Unexpected autonomy configuration fields')
        require(p['actor'] == 'operator' and type(p['enabled']) is bool, 'Autonomy configuration is operator-owned')
        require(current['enabled'] != p['enabled'], 'Autonomy configuration is unchanged')
        current['enabled'] = p['enabled']
    elif event['kind'] == 'autonomous_context_trial_failed':
        require(set(p) == {'schema', 'actor', 'base_version', 'based_on_head', 'prior_revision', 'proposal', 'error_type'},
                'Unexpected autonomous evaluation failure fields')
        require(p['actor'] == 'runtime' and current['enabled'] and not current['quarantined']
                and current['adoptions'] == 0 and p['prior_revision'] == current['revision'], 'No eligible autonomous evaluation')
        require(p['proposal'] == {'policy': CANDIDATE, 'basis': basis(state)}, 'Failure observation exceeds allowed proposal')
        require(isinstance(p['error_type'], str) and p['error_type'].isidentifier()
                and len(p['error_type']) <= 80, 'Invalid evaluation error class')
        current.update(trials=current['trials'] + 1, last_trial_version=state['version'], quarantined=True,
                       last_trial={'event_seq': event['seq'], 'proposal': deepcopy(p['proposal']),
                                   'status': 'rejected_evaluation_error', 'error_type': p['error_type']})
    elif event['kind'] == 'autonomous_context_trial':
        require(set(p) == {'schema', 'actor', 'base_version', 'based_on_head', 'prior_revision',
                           'proposal', 'seed', 'measurement'}, 'Unexpected autonomy trial fields')
        require(p['actor'] == 'runtime' and current['enabled'], 'Autonomy is not enabled')
        require(not current['quarantined'] and current['adoptions'] == 0, 'This selector has exhausted its change allowance')
        require(p['prior_revision'] == current['revision'], 'Stale policy revision')
        require(current['last_trial_version'] is None or state['version'] - current['last_trial_version'] >= TRIAL_INTERVAL,
                'Autonomy trial cadence exceeded')
        require(type(p['seed']) is int and 0 <= p['seed'] < 2**128, 'Invalid holdout seed')
        refs = basis(state)
        require(refs and p['proposal'] == {'policy': CANDIDATE, 'basis': refs}, 'Proposal exceeds allowed change or invents native provenance')
        validate_policy(p['proposal']['policy'])
        measurement = measure(state, current['policy'], CANDIDATE, p['seed'])
        require(p['measurement'] == measurement, 'Autonomous scores do not match trusted evaluation')
        adopted = qualifies(measurement)
        current.update(trials=current['trials'] + 1, last_trial_version=state['version'],
                       last_trial={'event_seq': event['seq'], 'proposal': p['proposal'], 'measurement': measurement,
                                   'seed': p['seed'], 'status': 'adopted' if adopted else 'rejected_no_measured_gain'})
        if adopted:
            current.update(policy=dict(CANDIDATE), previous_policy=dict(current['policy']),
                           revision=current['revision'] + 1, adoptions=1,
                           baseline_windows=windows(state, current['revision']))
    elif event['kind'] == 'autonomous_context_rollback':
        require(set(p) == {'schema', 'actor', 'base_version', 'based_on_head', 'prior_revision', 'reason'},
                'Unexpected autonomy rollback fields')
        require(p['actor'] == 'runtime' and current['policy'] == CANDIDATE
                and p['prior_revision'] == current['revision'], 'No active autonomous change to roll back')
        # Rollback narrows capabilities. Runtime fault observations remain dated
        # evidence; future fixed code must not need to reproduce an old exception.
        require(isinstance(p['reason'], dict) and p['reason'].get('kind') in (
            'context_guardrail', 'context_execution', 'observed_acceptance_regression'), 'Invalid rollback observation')
        current.update(policy=dict(BASELINE), revision=current['revision'] + 1,
                       rollbacks=current['rollbacks'] + 1, quarantined=True,
                       last_rollback={'event_seq': event['seq'], 'reason': deepcopy(p['reason'])})
    else:
        require(False, 'Unknown autonomous context event')
    return current


def advance(store, enabled):
    """Called under the existing writer lock, between invocations. No new writer."""
    state = store.load()
    require(state['pending'] is None, 'Autonomy requires an idle invocation boundary')
    current = state.get('autonomous_context') or initial()
    def append(kind, values):
        return store.append(kind, {'schema': SCHEMA, 'base_version': state['version'],
                                   'based_on_head': store.head(), **values})
    if current['enabled'] != enabled:
        state = append('autonomous_context_configured', {'actor': 'operator', 'enabled': enabled})
        current = state['autonomous_context']
    if not enabled:
        return state
    if current['policy'] != BASELINE:
        reason = rollback_reason(state)
        if reason:
            state = append('autonomous_context_rollback', {'actor': 'runtime', 'prior_revision': current['revision'], 'reason': reason})
        return state
    if (current['quarantined'] or current['adoptions'] or not basis(state)
            or (current['last_trial_version'] is not None
                and state['version'] - current['last_trial_version'] < TRIAL_INTERVAL)):
        return state
    seed = secrets.randbits(128)
    proposal = {'policy': dict(CANDIDATE), 'basis': basis(state)}
    try:
        measurement = measure(state, current['policy'], CANDIDATE, seed)
    except Exception as error:
        # Only the pure measurement is contained here. Native record reads,
        # writes and integrity errors remain outside this fault boundary.
        return append('autonomous_context_trial_failed', {'actor': 'runtime', 'prior_revision': current['revision'],
                      'proposal': proposal, 'error_type': type(error).__name__})
    return append('autonomous_context_trial', {'actor': 'runtime', 'prior_revision': current['revision'],
                  'proposal': proposal, 'seed': seed, 'measurement': measurement})


def status(state):
    current = state.get('autonomous_context') or initial()
    return {key: deepcopy(current[key]) for key in (
        'schema', 'enabled', 'policy', 'revision', 'trials', 'adoptions', 'rollbacks', 'quarantined',
        'last_trial_version', 'last_trial', 'last_rollback')}
