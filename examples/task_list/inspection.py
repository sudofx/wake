"""Generate static inspection evidence from the actual offline task-list example.

Run: python -S -m examples.task_list.inspection --output demo.json
Only a fresh temporary example record is opened. Receipt IDs, timestamps and hash
bytes are preserved; deterministic semantics do not imply identical run bytes.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

from wake.kernel.applications import application_key, application_state
from wake.kernel.record import Record

from .app import TASK_LIST
from .run import demonstrate

FORMAT = 'wake-kernel-inspection@1'


def source_metadata():
    root = Path(__file__).resolve().parents[2]
    files = [root / 'wake/__init__.py', *sorted((root / 'wake/kernel').glob('*.py')),
             root / 'examples/task_list/app.py', root / 'examples/task_list/run.py',
             Path(__file__).resolve(), root / 'tests/test_kernel_boundary.py',
             root / 'tests/test_inspection_demo.py']
    hashes = [{'path': str(path.relative_to(root)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
              for path in files if path.is_file()]
    revision, dirty = None, None
    try:
        revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root,
                                           stderr=subprocess.DEVNULL, text=True, timeout=5).strip()
        dirty = bool(subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=normal'],
                                            cwd=root, stderr=subprocess.DEVNULL, timeout=5))
    except (OSError, subprocess.SubprocessError):
        pass
    return {'git_revision': revision, 'dirty': dirty, 'files': hashes,
            'scope': 'Exact listed source-file bytes; Git revision is descriptive, not proof that a dirty checkout matches its commit.'}


def build_demo():
    """Capture actual receipts and verified replay without retaining SQLite."""
    with tempfile.TemporaryDirectory(prefix='wake-inspection-example-') as directory:
        result = demonstrate(directory)
        record = Record(Path(directory) / 'task-list.sqlite')
        events = list(record.history())
        revision, envelopes = record.full_replay()
        state = application_state(TASK_LIST, envelopes[application_key(TASK_LIST.application_id)])
        replay_matches = revision == result['revision'] and state == result['state']
        checks = {
            'expected_decisions': [row['status'] for row in events] == ['accepted', 'rejected', 'accepted'],
            'expected_revisions': [row['revision_after'] for row in events] == [1, 1, 2],
            'rejected_state_unchanged': events[1]['revision_before'] == events[1]['revision_after'] == 1,
            'full_replay_matches_current_state': replay_matches and result['replay_verified'],
            'research_record_absent': not (Path(directory) / 'wake.sqlite').exists(),
        }
        if not all(checks.values()):
            raise ValueError('Task-list inspection fixture did not meet its expected contract')
        return {
            'format': FORMAT, 'scenario': 'task-list-three-decisions',
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'source': source_metadata(),
            'application': {'id': TASK_LIST.application_id, 'version': TASK_LIST.version},
            'reproduction': {
                'command': 'python -S -m examples.task_list.inspection --output demo.json',
                'example_command': 'python -S -m examples.task_list.run --data FRESH_TEMPORARY_DIRECTORY',
                'requirements': ['Python 3.11 or later', 'standard library only', 'this source checkout'],
            },
            'events': events,
            'result': {'receipts': result['receipts'], 'state': state, 'revision': revision,
                       'replay_verified': replay_matches, 'head': events[-1]['event_hash']},
            'checks': checks,
            'limits': [
                'Offline synthetic task-list demonstration, not accepted research or a live service.',
                'Application rules and decision semantics are deterministic; UUIDs, receipt timestamps and exact hashes vary between runs.',
                'Hashes detect edits relative to retained bytes and head; they do not authenticate the author or prevent replacement of the entire artifact.',
                'The artifact records checks performed during generation; a static page does not rerun the kernel.',
                'No model or provider is called, and no research record is opened.',
            ],
        }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args(argv)
    if args.output.suffix != '.json':
        parser.error('--output must name a JSON artifact')
    artifact = build_demo()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Publish complete bytes only; failed generation leaves an existing artifact.
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=args.output.parent,
                                     prefix='.inspection-', delete=False) as stream:
        temporary = Path(stream.name)
        try:
            json.dump(artifact, stream, ensure_ascii=False, sort_keys=True, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        os.replace(temporary, args.output)
    finally:
        temporary.unlink(missing_ok=True)
    print(json.dumps({'format': FORMAT, 'checks_passed': all(artifact['checks'].values())}))


if __name__ == '__main__':
    main()
