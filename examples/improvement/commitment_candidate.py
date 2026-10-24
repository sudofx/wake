"""Reference proposal for commitment-context@1; NOT installed in WAKE research.

This human-readable candidate illustrates the first experiment. A different model
or human can submit a different implementation through the same JSON interface.
"""


def _clip(value, size=360):
    value = str(value or '')
    return value if len(value) <= size else value[:size - 1] + '…'


def decision_context(state, question=None):
    attention = state.get('attention') or {}
    topic = attention.get('selected_topic') or attention.get('current', {}).get('selected_topic')
    deadlines = {}
    for commitment in state.get('commitments', {}).values():
        project, due = commitment.get('project'), commitment.get('due_cycle')
        if (commitment.get('status') == 'open' and isinstance(project, str)
                and type(due) is int and due <= state.get('version', 0) + 2):
            deadlines[project] = min(deadlines.get(project, due), due)
    # Attention wins before urgency; deadlines never grant a topic override.
    active = sorted((p for p in state.get('projects', {}).values() if p.get('status') == 'active'),
                    key=lambda p: (0 if topic and p.get('domain') == topic else 1,
                                   p['id'] not in deadlines,
                                   deadlines.get(p['id'], 0), p['id']))
    project = active[0] if active else {}
    return {'project_id': project.get('id'), 'topic': topic or project.get('domain'),
            'question': _clip(question or project.get('question') or state.get('objective') or state.get('focus'), 1000),
            'pending_action': _clip(project.get('next_step')),
            'focus': _clip(state.get('focus'))}
