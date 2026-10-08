"""Protect the extraction seam through real execution, not a second kernel."""
import ast
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from examples.task_list.app import TASK_LIST
from wake.kernel import (ApplicationDefinition, ApplicationHost, ApplicationIntent,
                         ApplicationRegistry, Kernel)
from wake.kernel.governance import Governance
from wake.kernel.record import Record

ROOT = Path(__file__).resolve().parents[1]


class KernelBoundaryTests(unittest.TestCase):
    def test_kernel_imports_stay_inside_kernel_or_standard_library(self):
        for path in (ROOT / 'wake/kernel').glob('*.py'):
            tree = ast.parse(path.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    if node.level:
                        self.assertEqual(node.level, 1, str(path))
                        continue
                    module = (node.module or '').split('.')[0]
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        self.assertIn(alias.name.split('.')[0], sys.stdlib_module_names, str(path))
                    continue
                else:
                    continue
                self.assertIn(module, sys.stdlib_module_names, str(path))

    def test_example_runs_with_only_kernel_and_no_site_packages(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'wake').mkdir()
            shutil.copy(ROOT / 'wake/__init__.py', root / 'wake/__init__.py')
            shutil.copytree(ROOT / 'wake/kernel', root / 'wake/kernel')
            shutil.copytree(ROOT / 'examples/task_list', root / 'examples/task_list')
            output = subprocess.check_output(
                [sys.executable, '-S', '-m', 'examples.task_list.run', '--data', str(root / 'record')],
                cwd=root, text=True)
            result = json.loads(output)
            self.assertEqual([r['status'] for r in result['receipts']],
                             ['accepted', 'rejected', 'accepted'])
            self.assertTrue(result['replay_verified'])
            self.assertEqual(result['revision'], 2)
            self.assertFalse((root / 'record/wake.sqlite').exists())
            # Generic audit remains possible with no application installed.
            revision, state = Record(root / 'record/task-list.sqlite').full_replay()
            self.assertEqual(revision, 2)
            self.assertIn('app:example-task-list', state)

    def test_stale_duplicate_and_invalid_intents_preserve_state_with_receipts(self):
        with tempfile.TemporaryDirectory() as temp:
            record = Record(Path(temp) / 'tasks.sqlite')
            registry = ApplicationRegistry((TASK_LIST,))
            host = ApplicationHost(Kernel(record, Governance(application_registry=registry)),
                                   registry, TASK_LIST.application_id)
            first = ApplicationIntent('first', 0, 'add', {'id': 'a', 'title': 'A'})
            self.assertEqual(host.submit(first).status, 'accepted')
            before = host.context()
            for intent in (ApplicationIntent('stale', 0, 'complete', {'id': 'a'}),
                           ApplicationIntent('invalid', 1, 'complete', {'id': 'absent'}),
                           ApplicationIntent('duplicate-task', 1, 'add', {'id': 'a', 'title': 'B'})):
                self.assertEqual(host.submit(intent).status, 'rejected')
            self.assertEqual(host.context(), before)
            self.assertEqual(host.audit_context(), before)
            history = record.history()
            self.assertEqual(len(history), 4)
            # A proposal ID identifies one receipt. Retransmission fails before
            # append rather than manufacturing a second receipt for that ID.
            with self.assertRaisesRegex(ValueError, 'already recorded'):
                host.submit(first)
            self.assertEqual(host.context(), before)
            self.assertEqual(len(record.history()), 4)

    def test_two_applications_have_separate_state_and_version_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            record = Record(Path(temp) / 'tasks.sqlite')
            other = ApplicationDefinition('other-task-list', '1', TASK_LIST.actions)
            registry = ApplicationRegistry((TASK_LIST, other))
            kernel = Kernel(record, Governance(application_registry=registry))
            first = ApplicationHost(kernel, registry, TASK_LIST.application_id)
            second = ApplicationHost(kernel, registry, other.application_id)
            first.submit(ApplicationIntent('add-a', 0, 'add', {'id': 'a', 'title': 'A'}))
            self.assertIsNone(second.context().state)
            self.assertEqual(second.submit(ApplicationIntent('complete-a', 1, 'complete', {'id': 'a'})).status,
                             'rejected')
            changed = ApplicationDefinition(TASK_LIST.application_id, '2', TASK_LIST.actions)
            new_registry = ApplicationRegistry((changed,))
            migrated_host = ApplicationHost(Kernel(record, Governance(application_registry=new_registry)),
                                            new_registry, changed.application_id)
            with self.assertRaisesRegex(ValueError, 'migration required'):
                migrated_host.context()
            self.assertEqual(migrated_host.submit(ApplicationIntent('wrong-version', 1, 'add',
                                                                   {'id': 'b', 'title': 'B'})).status,
                             'rejected')
            self.assertEqual(first.context().state, {'a': {'title': 'A', 'completed': False}})
