"""Trusted, versioned evaluation tasks; candidate code never receives the labels.

This first task compares context selection, not intelligence or scientific truth.
It deliberately keeps Attention ahead of commitment urgency. Extending the task
contract needs a new version, not new labels under an old benchmark identity.
"""
import random

TASK = 'commitment-context@1'
TARGET = 'wake/decision_memory.py'
FUNCTIONS = ('_clip', 'decision_context')

CONTRACT = (
    'Keep the existing decision_context interface and clipping. Select an active '
    'project in the current Attention topic when one exists. Within that group '
    '(or all active projects otherwise), prioritize the earliest open commitment '
    'due at or before version + 2. Ignore commitments for inactive/missing projects '
    'and non-integer deadlines. Break ties by project ID. Without such commitments, '
    'retain alphabetical project selection. Preserve explicit question overrides, '
    'focus, pending_action and topic semantics. This is a proposed policy experiment, '
    'not a claim that current selection violates its existing contract.'
)


def clip(value, size=360):
    value = str(value or '')
    return value if len(value) <= size else value[:size - 1] + '…'


def expected(case):
    """Independent task oracle; no baseline or candidate code is imported."""
    state, question = case['state'], case['question']
    attention = state.get('attention') or {}
    topic = attention.get('selected_topic') or attention.get('current', {}).get('selected_topic')
    projects = {k: p for k, p in state.get('projects', {}).items() if p['status'] == 'active'}
    group = {k: p for k, p in projects.items() if topic and p.get('domain') == topic} or projects
    due = {}
    for commitment in state.get('commitments', {}).values():
        deadline, project = commitment.get('due_cycle'), commitment.get('project')
        if (commitment.get('status') == 'open' and type(deadline) is int
                and deadline <= state['version'] + 2 and project in group):
            due[project] = min(deadline, due.get(project, deadline))
    selected = min(group, key=lambda key: (0, due[key], key) if key in due else (1, 0, key), default=None)
    project = group.get(selected, {})
    return {'project_id': selected, 'topic': topic or project.get('domain'),
            'question': clip(question or project.get('question') or state.get('objective') or state.get('focus'), 1000),
            'pending_action': clip(project.get('next_step')), 'focus': clip(state.get('focus'))}


def cases(seed, count):
    """Vary IDs, ordering, deadlines, Attention, overrides, and inactive projects."""
    rng = random.Random(seed)
    result = []
    for index in range(count):
        suffix = f'{rng.getrandbits(48):012x}'
        version = rng.randrange(5, 1000)
        projects = {
            f'a-{suffix}': {'status': 'active', 'domain': 'memory'},
            f'z-{suffix}': {'status': 'active', 'domain': 'memory'},
            f'b-{suffix}': {'status': 'active', 'domain': 'judgment'},
            f'c-{suffix}': {'status': 'completed', 'domain': 'memory'},
        }
        for key, p in projects.items():
            p.update(id=key, question=f'Investigate {key}', next_step=f'Next {key}')
        commitments = {
            'urgent': {'status': 'open', 'project': f'z-{suffix}', 'due_cycle': version - 1},
            'inactive': {'status': 'open', 'project': f'c-{suffix}', 'due_cycle': 0},
            'missing': {'status': 'open', 'project': 'missing', 'due_cycle': 0},
        }
        variant = index % 12
        attention = {'selected_topic': 'memory'}
        if variant == 1:
            commitments['urgent']['status'] = 'fulfilled'
        elif variant == 2:
            attention = {'current': {'selected_topic': 'judgment'}}
        elif variant == 3:
            commitments['urgent']['due_cycle'] = version + 3
        elif variant == 4:
            commitments['urgent']['due_cycle'] = version + 2
        elif variant == 5:
            commitments['urgent']['due_cycle'] = True
        elif variant == 6:
            commitments['earlier'] = {'status': 'open', 'project': f'a-{suffix}', 'due_cycle': version - 2}
        elif variant == 7:
            commitments['tie'] = {'status': 'open', 'project': f'a-{suffix}', 'due_cycle': version - 1}
        elif variant == 8:
            attention = {}
        elif variant == 9:
            projects = {}
        elif variant == 10:
            commitments['urgent']['due_cycle'] = str(version - 1)
        elif variant == 11:
            attention = {'selected_topic': 'absent'}
        keys = list(projects)
        rng.shuffle(keys)
        state = {'version': version, 'projects': {key: projects[key] for key in keys},
                 'commitments': commitments, 'attention': attention,
                 'objective': 'Fallback objective', 'focus': 'f' * (400 if index % 3 == 0 else 12)}
        result.append({'id': f'case-{index}', 'state': state,
                       'question': 'q' * 1100 if index % 4 == 0 else None})
    return result


def score(inputs, outputs):
    """Score complete answers externally; candidate-reported scores are ignored."""
    if not isinstance(outputs, list) or len(outputs) != len(inputs):
        raise ValueError('Candidate must return exactly one result per input')
    details = []
    for case, answer in zip(inputs, outputs):
        target = expected(case)
        valid = isinstance(answer, dict) and set(answer) == set(target)
        # Non-selection fields may change only as a consequence of the selected
        # project; the oracle checks the whole interface rather than one easy ID.
        passed = valid and answer == target
        details.append({'id': case['id'], 'passed': passed, 'expected': target, 'actual': answer})
    return {'passed': sum(item['passed'] for item in details), 'total': len(details), 'cases': details}
