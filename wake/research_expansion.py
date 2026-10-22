"""Research configuration and observations, above the unchanged WAKE kernel.

Questions remain ordinary governed projects. This module neither selects work
nor grants capabilities; its reports do not assess novelty or consciousness.
"""
from copy import deepcopy
import os

from .event_format import digest

EXPERIMENT_ID = 'research-expansion-2026-10'
ASSIGNMENTS = {'100.wake': ('assumption_challenge', 'unassigned_problem'),
               '200.wake': ('emergent_preferences', 'assumption_challenge'),
               '300.wake': ('unassigned_problem', 'emergent_preferences')}


def apply_hosted_configuration(root, enabled):
    """Apply an explicit operator setting before worker admission, never start it."""
    import json
    from pathlib import Path
    import tomllib
    from .engine import _topics
    from .report import atomic_write
    if type(enabled) is not bool:
        raise ValueError('Research expansion enabled must be a boolean')
    root = Path(root)
    source = Path(__file__).resolve().parents[1] / 'research-topics.toml'
    catalog = _topics({'research_topics_file': str(source)}, source.parent / 'wake.toml')
    experimental = {t['id']: t for t in catalog if t.get('experiment_id') == EXPERIMENT_ID}
    if set(experimental) != {topic for group in ASSIGNMENTS.values() for topic in group}:
        raise ValueError('Incomplete experimental research catalog')
    changes = []
    for parent, assigned in ASSIGNMENTS.items():
        path = root / 'config/.wake-runner-topics' / (parent + '.toml')
        old = tomllib.loads(path.read_text())['topics']
        topics = deepcopy(old)
        known = {t['id']: t for t in topics}
        for topic_id in assigned:
            if topic_id in known and known[topic_id].get('experiment_id') != EXPERIMENT_ID:
                raise ValueError('Experimental topic would overwrite an existing identity')
            if topic_id not in known and enabled:
                topics.append(deepcopy(experimental[topic_id]))
        for topic in topics:
            if topic.get('experiment_id') == EXPERIMENT_ID:
                topic['enabled'] = enabled and topic['id'] in assigned
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


def observations(state, events):
    """Trace formulations and later work; interpretation requires human review."""
    topics = {t['id']: t for t in state.get('research_topics', [])}
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
            reframings=deepcopy(state.get('representations', {}).get(project['id'], [])),
            notebooks=[n['id'] for n in state.get('notebooks', {}).values()
                       if n.get('project') == project['id']],
            requests=[r['id'] for r in state.get('research', {}).values()
                      if r.get('project') == project['id']])
        origin = next((e for e in events if e['kind'] == 'accepted'
            and e['payload'].get('proposal', {}).get('base_version', -2) + 1 == project.get('created_version') and any(
            a.get('type') == 'project' and a.get('id') == project['id']
            for a in e['payload'].get('proposal', {}).get('actions', []))), None)
        questions[-1]['origin_event'] = ({key: origin.get(key) for key in ('seq', 'time', 'hash')}
                                        if origin else None)
        questions[-1]['original_proposal'] = (next(a for a in origin['payload']['proposal']['actions']
            if a.get('type') == 'project' and a.get('id') == project['id']) if origin else None)
        invocation = state.get('invocations', {}).get((origin or {}).get('payload', {}).get('id'), {})
        questions[-1]['provider'] = invocation.get('provider')
        questions[-1]['simulated'] = invocation.get('provider') == 'fixture'
        if questions[-1]['simulated']:
            questions[-1]['origin'] = 'fixture-generated project; not a live discovery'
    boundaries = [{'seq': e['seq'], 'time': e.get('time'), 'hash': e.get('hash'),
                   'configuration': e['payload']['configuration']}
                  for e in events if e['kind'] in ('charter_adopted', 'research_topics_changed')
                  and e['payload'].get('configuration')]
    proposals = [{'seq': e['seq'], 'time': e.get('time'), 'hash': e.get('hash'),
                  'outcome': e['kind'], 'actions': [deepcopy(a) for a in
                  e['payload'].get('proposal', {}).get('actions', [])
                  if a.get('type') in ('project', 'reframe')],
                  'reason': e['payload'].get('reason')}
                 for e in events if e['kind'] in ('accepted', 'rejected') and any(
                     a.get('type') in ('project', 'reframe')
                     for a in e['payload'].get('proposal', {}).get('actions', []))]
    return {'schema': 'research-expansion-observations@1', 'accepted_cycles': state['version'],
            'boundaries': boundaries, 'questions': questions,
            'current_configuration': deepcopy(state.get('research_configuration')),
            'proposal_outcomes': proposals,
            'assessment': {name: None for name in ('independent_question_formation',
                           'cross_cycle_continuity', 'independent_criticism',
                           'history_dependent_preferences', 'productive_surprise')},
            'limitations': ['Formulation is not evidence of novelty or autonomous objectives.',
                           'Counts and temporal succession do not establish causal benefit.',
                           'Compare verified baseline copies; never alter live history for evaluation.',
                           'Generated criticism and preferences require independent evidence review.']}


def main():
    """Report on a dated exported snapshot without opening authority or providers."""
    import argparse
    import json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument('--snapshot', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.snapshot.read_text())
    result = observations(data['state'], data.get('events', []))
    result['source'] = {key: data.get(key) for key in ('head', 'event_history', 'generated')}
    result['limitations'].append('Export filtering and event windows may omit private provenance or older boundaries; consult verified native copies for a full audit.')
    with args.output.open('x') as stream:
        json.dump(result, stream, indent=2)


if __name__ == '__main__':
    main()
