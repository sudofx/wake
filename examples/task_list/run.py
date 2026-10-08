"""Executable kernel proof with its own record; never opens research authority.

Run from the repository root: python -m examples.task_list.run --data /tmp/wake-tasks
No provider, GitHub, network, or research package is needed. The supplied directory
belongs to this example and must not be a research installation's data directory.
"""
import argparse
import json
from pathlib import Path
import uuid

from wake.kernel import ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel
from wake.kernel.governance import Governance
from wake.kernel.record import Record
from .app import TASK_LIST


def demonstrate(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    # A distinct filename makes accidentally selecting a research directory
    # insufficient to open or modify its wake.sqlite authority.
    record = Record(directory / 'task-list.sqlite')
    registry = ApplicationRegistry((TASK_LIST,))
    host = ApplicationHost(Kernel(record, Governance(application_registry=registry)),
                           registry, TASK_LIST.application_id)
    task_id = uuid.uuid4().hex
    receipts = []
    for action, payload in (
        ('add', {'id': task_id, 'title': 'Verify independent kernel application'}),
        ('complete', {'id': 'missing-task'}),
        ('complete', {'id': task_id}),
    ):
        receipt = host.submit(ApplicationIntent(uuid.uuid4().hex, host.context().revision,
                                               action, payload))
        receipts.append({'status': receipt.status, 'reasons': receipt.reasons,
                         'revision': receipt.revision_after})
    audited = host.audit_context()
    assert audited == host.context(), 'Replay and current state disagree'
    return {'record': record.path, 'receipts': receipts, 'state': audited.state,
            'revision': audited.revision, 'replay_verified': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', required=True)
    args = parser.parse_args()
    print(json.dumps(demonstrate(args.data), indent=2))
