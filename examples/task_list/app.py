"""Small deterministic application; imports only the public kernel contract.

The evaluator is deliberately storage- and provider-free. Rejections carry a
reason and leave state untouched. Changing stored meaning requires a new version
and an explicit migration rather than quietly changing historical evaluation.
"""
from wake.kernel import ApplicationAction, ApplicationDecision, ApplicationDefinition


def add(state, payload):
    if not isinstance(payload, dict):
        return ApplicationDecision(False, reasons=('task input must be an object',))
    task_id, title = payload.get('id'), payload.get('title')
    if not isinstance(task_id, str) or not task_id.strip():
        return ApplicationDecision(False, reasons=('task id is required',))
    if not isinstance(title, str) or not title.strip():
        return ApplicationDecision(False, reasons=('task title is required',))
    tasks = dict(state or {})
    if task_id in tasks:
        return ApplicationDecision(False, reasons=('task id already exists',))
    tasks[task_id] = {'title': title, 'completed': False}
    return ApplicationDecision(True, tasks)


def complete(state, payload):
    if not isinstance(payload, dict) or not isinstance(payload.get('id'), str):
        return ApplicationDecision(False, reasons=('task id is required',))
    tasks = dict(state or {})
    task_id = payload['id']
    if task_id not in tasks:
        return ApplicationDecision(False, reasons=('task does not exist',))
    if tasks[task_id]['completed']:
        return ApplicationDecision(False, reasons=('task is already completed',))
    tasks[task_id] = {**tasks[task_id], 'completed': True}
    return ApplicationDecision(True, tasks)


TASK_LIST = ApplicationDefinition(
    application_id='example-task-list', version='1',
    actions=(ApplicationAction('add', add), ApplicationAction('complete', complete)),
)
