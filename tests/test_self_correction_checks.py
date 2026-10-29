"""Restricted comparison never erases failures or accepts a missing/newly skipped test."""
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('correction_checks', Path(__file__).resolve().parents[1] / 'scripts/self_correction_checks.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class CorrectionCheckTests(unittest.TestCase):
    def test_comparison_retains_baseline_failures_and_rejects_every_new_regression(self):
        with tempfile.TemporaryDirectory() as temporary:
            base, candidate = Path(temporary) / 'base.log', Path(temporary) / 'candidate.log'
            def write(path, statuses):
                path.write_text('Fixture output\n' + checks.PREFIX + json.dumps({'schema': 1, 'tests_run': 3, 'outcomes': statuses}) + '\n')
            before = {'reader': 'success', 'unavailable_instrument': 'failure', 'optional': 'skipped'}
            write(base, before)
            write(candidate, before)
            with self.assertRaisesRegex(ValueError, 'improvement'):
                checks.compare(base, candidate, require_improvement=True)
            self.assertEqual(checks.compare(base, candidate)['restricted_baseline_failures'], {'unavailable_instrument': 'failure'})
            for status in ('failure', 'error', 'skipped', 'expected_failure', 'unexpected_success'):
                write(candidate, {**before, 'reader': status})
                with self.subTest(status=status), self.assertRaisesRegex(ValueError, 'regression|failures'):
                    checks.compare(base, candidate)
            write(candidate, {**before, 'unavailable_instrument': 'success'})
            checks.compare(base, candidate, require_improvement=True)
            write(candidate, {'missing_test': 'success'})
            with self.assertRaisesRegex(ValueError, 'identities'):
                checks.compare(base, candidate)
            candidate.write_text(checks.PREFIX + '{}\nAn untrusted trailing frame\n')
            with self.assertRaisesRegex(ValueError, 'final'):
                checks.report(candidate)

    def test_subtest_failure_is_retained(self):
        class Fixture(unittest.TestCase):
            def runTest(self):
                with self.subTest('fixture'):self.fail('Synthetic expected failure')
        result = checks.Results(io.StringIO(), False, 0)
        Fixture().run(result)
        self.assertEqual(sorted(result.outcomes.values()), ['failure', 'failure'])

    def test_new_failure_inside_an_already_failed_parent_is_rejected(self):
        class Fixture(unittest.TestCase):
            second_fails = False
            def runTest(self):
                with self.subTest('first'):self.fail('Existing synthetic failure')
                with self.subTest('second'):
                    if self.second_fails:self.fail('New synthetic regression')
        baseline = checks.Results(io.StringIO(), False, 0)
        candidate = checks.Results(io.StringIO(), False, 0)
        Fixture().run(baseline)
        changed = Fixture();changed.second_fails = True;changed.run(candidate)
        self.assertEqual(set(baseline.outcomes), set(candidate.outcomes))
        with tempfile.TemporaryDirectory() as temporary:
            paths = [Path(temporary) / label for label in ('base', 'candidate')]
            for path, result in zip(paths, (baseline, candidate)):
                result.outcomes['unaffected'] = 'success'
                path.write_text(checks.PREFIX + json.dumps({'schema':1, 'tests_run':1, 'outcomes':result.outcomes}))
            with self.assertRaisesRegex(ValueError, 'failures'):
                checks.compare(*paths)
