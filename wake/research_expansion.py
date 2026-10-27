"""Research configuration and observations, above the unchanged WAKE kernel.

Questions remain ordinary governed projects. This module neither selects work
nor grants capabilities; its reports do not assess novelty or consciousness.
"""
from copy import deepcopy
import os

from .event_format import digest

EXPERIMENT_ID = 'research-expansion-2026-10'
CATALOG_EXPERIMENT_ID = 'research-expansion-catalog-2026-10'
EXPERIMENT_IDS = (EXPERIMENT_ID, CATALOG_EXPERIMENT_ID)
ASSIGNMENTS = {
    '100.wake': ('assumption_challenge', 'unassigned_problem', 'obedience_limits',
                 'creator_objective_critique', 'judgment_and_consensus',
                 'unrecognized_reasoning_limits', 'question_abandonment', 'wake_self_study'),
    '200.wake': ('emergent_preferences', 'assumption_challenge', 'memory_formed_preferences',
                 'memory_and_identity', 'divergent_values', 'responsibility_formation', 'wake_self_study'),
    '300.wake': ('unassigned_problem', 'emergent_preferences', 'unassigned_objectives',
                 'continuity_rationale', 'unprompted_complexity', 'unassigned_inquiry', 'wake_self_study')}


def apply_hosted_configuration(root, enabled, candidate_catalog_enabled=False):
    """Apply an explicit operator setting before worker admission, never start it."""
    import json
    from pathlib import Path
    import tomllib
    from .engine import _topics
    from .report import atomic_write
    if type(enabled) is not bool or type(candidate_catalog_enabled) is not bool:
        raise ValueError('Research expansion settings must be booleans')
    root = Path(root)
    source = Path(__file__).resolve().parents[1] / 'research-topics.toml'
    catalog = _topics({'research_topics_file': str(source)}, source.parent / 'wake.toml')
    experimental = {t['id']: t for t in catalog if t.get('experiment_id') in EXPERIMENT_IDS}
    if set(experimental) != {topic for group in ASSIGNMENTS.values() for topic in group}:
        raise ValueError('Incomplete experimental research catalog')
    changes = []
    for parent, assigned in ASSIGNMENTS.items():
        selected = assigned if candidate_catalog_enabled else tuple(
            topic for topic in assigned if experimental[topic]['experiment_id'] == EXPERIMENT_ID)
        path = root / 'config/.wake-runner-topics' / (parent + '.toml')
        old = tomllib.loads(path.read_text())['topics']
        topics = deepcopy(old)
        known = {t['id']: t for t in topics}
        for topic_id in selected:
            if topic_id in known and known[topic_id].get('experiment_id') != experimental[topic_id]['experiment_id']:
                raise ValueError('Experimental topic would overwrite an existing identity')
            if topic_id not in known and enabled:
                topics.append(deepcopy(experimental[topic_id]))
        for topic in topics:
            if topic.get('experiment_id') in EXPERIMENT_IDS:
                topic['enabled'] = enabled and topic['id'] in selected
        _topics({'research_topics_file': str(path), 'research_topics': topics})
        text = '\n'.join('[[topics]]\n' + '\n'.join(
            key + ' = ' + json.dumps(value, ensure_ascii=False)
            for key, value in topic.items()) + '\n' for topic in topics)
        changes.append((path, text))
    # All inputs are checked before the first write. An interrupted bootstrap
    # never admits workers; a retry produces the same three configurations.
    for path, text in changes:
        atomic_write(path, text)


def retained_topics(configured, previous):
    """Retire omitted coordinates without losing their labels or identities."""
    present = {topic['id'] for topic in configured}
    return [*deepcopy(configured), *({**deepcopy(topic), 'enabled': False}
            for topic in previous if topic['id'] not in present)]


def configuration_receipt(topics, state, config):
    return {'schema': 'research-configuration@1', 'id': 'topics-' + digest(topics)[:16],
            'effective_from_version': state['version'],
            'experiments': sorted({t['experiment_id'] for t in topics if t.get('experiment_id')}),
            'active_experiments': sorted({t['experiment_id'] for t in topics
                                         if t.get('experiment_id') and t.get('enabled', True)}),
            'node': os.environ.get('WAKE_GROUP_INSTANCE'),
            'source_revision': os.environ.get('WAKE_SOURCE_REVISION'),
            'provider': config.get('provider'), 'model': config.get('model'),
            'max_context_chars': config.get('max_context_chars'),
            'decision_memory_mode': config.get('decision_memory_mode', 'off')}


def _proposal(event):
    proposal = event.get('payload', {}).get('proposal')
    return proposal if isinstance(proposal, dict) else {}


def _question_actions(event):
    actions = _proposal(event).get('actions')
    return [a for a in actions if isinstance(a, dict) and a.get('type') in ('project', 'reframe')] \
        if isinstance(actions, list) else []


def _activity_actions(event):
    actions = _proposal(event).get('actions')
    return [a for a in actions if isinstance(a, dict) and a.get('type') in
            ('project', 'reframe', 'research', 'notebook')] if isinstance(actions, list) else []


def _activity_digest(action):
    # Compact export receipts carry the digest without duplicating notebook prose.
    from .installation_cli import _public_projection
    return action.get('content_digest') or digest({key: value for key, value in _public_projection(action).items()
        if key not in ('id', 'project', 'type')})


def _accepted_activity(events, node=None):
    activity = {}
    for event in events:
        if event['kind'] != 'accepted':
            continue
        for action in _activity_actions(event):
            project = action.get('id') if action['type'] == 'project' else action.get('project')
            if project:
                activity.setdefault(project, []).append({
                    'seq': event.get('seq'), 'time': event.get('time'), 'hash': event.get('hash'),
                    'node': (event.get('origin') or {}).get('node')
                        or node,
                    'accepted_cycle': (_proposal(event)['base_version'] + 1
                        if type(_proposal(event).get('base_version')) is int else None),
                    'invocation': event.get('payload', {}).get('id'),
                    'type': action['type'], 'id': action.get('id'),
                    'content_digest': _activity_digest(action)})
    return activity


def observations(state, events):
    """Trace formulations and later work; interpretation requires human review."""
    topics = {t['id']: t for t in state.get('research_topics', [])}
    activity = _accepted_activity(events, (state.get('research_configuration') or {}).get('node'))
    questions = []
    for project in state.get('projects', {}).values():
        topic = topics.get(project['domain'], {})
        questions.append({key: deepcopy(project.get(key)) for key in
                          ('id', 'domain', 'question', 'status', 'reason', 'created_by',
                           'created_version', 'updated_by', 'updated_version')})
        questions[-1].update(
            origin='model-formulated project; novelty unassessed',
            originating_node=(project.get('origin') or {}).get('node')
                or (state.get('research_configuration') or {}).get('node'),
            configured_seed=topic.get('seed_question'),
            experiment_id=topic.get('experiment_id'),
            accepted_activity=activity.get(project['id'], []),
            reframings=deepcopy(state.get('representations', {}).get(project['id'], [])),
            notebooks=[n['id'] for n in state.get('notebooks', {}).values()
                       if n.get('project') == project['id']],
            requests=[r['id'] for r in state.get('research', {}).values()
                      if r.get('project') == project['id']])
        origin = next((e for e in events if e['kind'] == 'accepted'
            and _proposal(e).get('base_version', -2) + 1 == project.get('created_version') and any(
            a.get('type') == 'project' and a.get('id') == project['id']
            for a in _question_actions(e))), None)
        questions[-1]['origin_event'] = ({key: origin.get(key) for key in ('seq', 'time', 'hash')}
                                        if origin else None)
        questions[-1]['original_proposal'] = (next(a for a in _question_actions(origin)
            if a.get('type') == 'project' and a.get('id') == project['id']) if origin else None)
        invocation = state.get('invocations', {}).get((origin or {}).get('payload', {}).get('id'), {})
        questions[-1]['originating_invocation'] = (origin or {}).get('payload', {}).get('id')
        questions[-1]['provider'] = invocation.get('provider')
        questions[-1]['model'] = invocation.get('successful_model') or invocation.get('model')
        questions[-1]['simulated'] = (invocation['provider'] == 'fixture'
                                      if invocation.get('provider') else None)
        if questions[-1]['simulated']:
            questions[-1]['origin'] = 'fixture-generated project; not a live discovery'
    boundaries = [{'seq': e['seq'], 'time': e.get('time'), 'hash': e.get('hash'),
                   'origin': deepcopy(e.get('origin')),
                   'topics': deepcopy(e['payload'].get('topics', e['payload'].get('research_topics', []))),
                   'configuration': e['payload']['configuration']}
                  for e in events if e['kind'] in ('charter_adopted', 'research_topics_changed')
                  and e['payload'].get('configuration')]
    proposals = [{'seq': e['seq'], 'time': e.get('time'), 'hash': e.get('hash'),
                  'outcome': e['kind'], 'actions': deepcopy(_question_actions(e)),
                  'origin': deepcopy(e.get('origin')),
                  'reason': e['payload'].get('reason')}
                 for e in events if e['kind'] in ('accepted', 'rejected') and _question_actions(e)]
    return {'schema': 'research-expansion-observations@1', 'accepted_cycles': state['version'],
            'boundaries': boundaries, 'questions': questions,
            'current_configuration': deepcopy(state.get('research_configuration')),
            'current_configurations': deepcopy(state.get('research_configurations', {})),
            'proposal_outcomes': proposals,
            'assessment': {name: None for name in ('independent_question_formation',
                           'cross_cycle_continuity', 'independent_criticism',
                           'history_dependent_preferences', 'productive_surprise')},
            'limitations': ['Formulation is not evidence of novelty or autonomous objectives.',
                           'Counts and temporal succession do not establish causal benefit.',
                           'Compare verified baseline copies; never alter live history for evaluation.',
                           'Generated criticism and preferences require independent evidence review.']}


def observation_event(event):
    """Keep only receipts needed for question/configuration audits, never bodies."""
    from .installation_cli import _public_projection
    payload = event.get('payload', {})
    if (event['kind'] in ('charter_adopted', 'research_topics_changed') and payload.get('configuration')
            or event['kind'] in ('accepted', 'rejected') and _activity_actions(event)):
        receipt = {key: deepcopy(event[key]) for key in
                   ('seq', 'time', 'hash', 'kind', 'origin') if key in event}
        receipt['payload'] = {key: deepcopy(payload[key]) for key in
                              ('id', 'reason', 'configuration', 'topics', 'research_topics') if key in payload}
        if 'proposal' in payload:
            receipt['payload']['proposal'] = {
                'base_version': _proposal(event).get('base_version'),
                'actions': [deepcopy(action) if action['type'] in ('project', 'reframe') else
                    {**{key: action[key] for key in ('type', 'id', 'project') if key in action},
                     'content_digest': _activity_digest(action)}
                    for action in _activity_actions(event)]}
        return _public_projection(receipt)
    return None


def compare_observations(baseline, current):
    """Describe recorded changes between dated views, without causal scoring."""
    old_source, new_source = baseline.get('source', {}), current.get('source', {})
    old_id, new_id = old_source.get('installation_id'), new_source.get('installation_id')
    if not old_id or not new_id or old_id != new_id:
        raise ValueError('Comparison requires reports from the same identified installation')
    old_heads, new_heads = old_source.get('node_heads', {}), new_source.get('node_heads', {})
    if set(old_heads) != set(new_heads) or not old_heads:
        raise ValueError('Comparison requires the same captured node set')
    if any(new_heads[node]['version'] < head['version'] for node, head in old_heads.items()):
        raise ValueError('Current report precedes the baseline on at least one node')
    old = {q['id']: q for q in baseline['questions']}
    new = {q['id']: q for q in current['questions']}
    activity_available = all('accepted_activity' in question
                             for question in [*old.values(), *new.values()])
    return {'baseline': deepcopy(old_source), 'current': deepcopy(new_source),
            'accepted_cycle_delta': current['accepted_cycles'] - baseline['accepted_cycles'],
            'added_questions': sorted(new.keys() - old.keys()),
            'absent_questions': sorted(old.keys() - new.keys()),
            'activity_comparison_available': activity_available,
            'changed_questions': [identifier for identifier in sorted(old.keys() & new.keys())
                if any(old[identifier].get(key) != new[identifier].get(key)
                       for key in ('status', 'updated_version', 'notebooks', 'requests', 'reframings'))
                or activity_available and old[identifier]['accepted_activity'] != new[identifier]['accepted_activity']],
            'limitations': ['Snapshot differences describe recorded activity, not novelty, quality or causal memory benefit.',
                            'Notebook-only revisions are compared only when both reports include accepted_activity.',
                            'Matching installation and node identities does not prove event-chain ancestry; verify native receipts for that claim.']}


def read_observation_history(path, node_heads):
    """Check exported link metadata against a captured report, not native authority.

    Filtered event bodies cannot authenticate the native hashes they retain.
    Matching sequence/link metadata prevents accidental mixed-snapshot reviews.
    """
    import gzip
    import json
    if not node_heads:
        raise ValueError('Complete history review requires captured node heads')
    links, receipts = {}, []
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt', encoding='utf-8') as stream:
        for line in stream:
            event = json.loads(line)
            origin = event.get('origin') or {}
            node = origin.get('node')
            expected = node_heads.get(node)
            if not expected or any(origin.get(key) != expected[key] for key in ('head', 'version')):
                raise ValueError('Event stream belongs to different captured node heads')
            seq, head = links.get(node, (0, '0' * 64))
            if event.get('seq') != seq + 1 or event.get('prev_hash') != head:
                raise ValueError('Exported event sequence/link metadata is incomplete')
            links[node] = (event['seq'], event['hash'])
            receipt = observation_event(event)
            if receipt is not None:
                receipts.append(receipt)
    if set(links) != set(node_heads) or any(links[node][1] != head['head'] for node, head in node_heads.items()):
        raise ValueError('Event stream does not reach every captured node head')
    return receipts


def main():
    """Report on a dated exported snapshot without opening authority or providers."""
    import argparse
    import json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--baseline', type=Path,
                        help='Earlier research-expansion.json from this installation')
    parser.add_argument('--events', type=Path,
                        help='Complete exported events.jsonl[.gz] matching an observation report with captured node heads')
    args = parser.parse_args()
    data = json.loads(args.snapshot.read_text())
    if data.get('schema') == 'research-expansion-observations@1':
        if args.events:
            events = read_observation_history(args.events, data.get('source', {}).get('node_heads'))
            activity = _accepted_activity(events)
            for question in data['questions']:
                question['accepted_activity'] = activity.get(question['id'], [])
            data['source']['activity_history_scope'] = 'complete exported stream; sequence/link metadata checked against captured heads'
            data['limitations'].append('Filtered event link metadata is not native cryptographic verification or application replay.')
        result = data
    else:
        if args.events:
            parser.error('--events requires an observation report with captured node heads')
        result = observations(data['state'], data.get('events', []))
        result['source'] = {key: data.get(key) for key in ('head', 'event_history', 'generated')}
        result['source']['history_scope'] = 'snapshot event window'
        result['limitations'].append('Export filtering and event windows may omit private provenance or older boundaries; consult verified native copies for a full audit.')
    if args.baseline:
        result['comparison'] = compare_observations(json.loads(args.baseline.read_text()), result)
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2)


if __name__ == '__main__':
    main()
