#!/usr/bin/env python3
"""Compare all candidate tests with the trusted base in identical restricted runners.

The independently checked base retains full CI, including its Docker instruments.
Restricted runners have no Docker socket; unavailable instruments must not be
misrepresented as successful candidate tests. Every baseline passing test must
still pass, with identical discovered test identities and no added skips.
"""
import argparse
import json
import os
from pathlib import Path
import sys
import unittest

PREFIX = 'WAKE_CORRECTION_TEST_REPORT='


class Results(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.outcomes = {}
        self.subtest_counts = {}

    def addSuccess(self, test):
        super().addSuccess(test)
        self.outcomes[test.id()] = 'success'

    def addFailure(self, test, error):
        super().addFailure(test, error)
        self.outcomes[test.id()] = 'failure'

    def addError(self, test, error):
        super().addError(test, error)
        self.outcomes[test.id()] = 'error'

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.outcomes[test.id()] = 'skipped'

    def addExpectedFailure(self, test, error):
        super().addExpectedFailure(test, error)
        self.outcomes[test.id()] = 'expected_failure'

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        self.outcomes[test.id()] = 'unexpected_success'

    def addSubTest(self, test, subtest, error):
        super().addSubTest(test, subtest, error)
        parent = test.id()
        self.subtest_counts[parent] = self.subtest_counts.get(parent, 0) + 1
        key = parent + '::subtest#' + str(self.subtest_counts[parent])
        status = 'success' if error is None else 'failure' if issubclass(error[0], test.failureException) else 'error'
        self.outcomes[key] = status
        if error is not None:
            self.outcomes[parent] = status


def record():
    suite = unittest.defaultTestLoader.discover('tests')
    result = unittest.TextTestRunner(verbosity=2, resultclass=Results).run(suite)
    # The trusted final frame follows all candidate subprocess output. No host
    # output mount, prior report or credential is exposed to candidate execution.
    print(PREFIX + json.dumps({'schema': 1, 'tests_run': result.testsRun, 'outcomes': result.outcomes}, sort_keys=True), flush=True)


def report(path):
    data = path.read_bytes()
    if len(data) > 16_000_000:
        raise ValueError('Oversized test report')
    last = data.decode('utf-8').rstrip().splitlines()[-1]
    if not last.startswith(PREFIX):
        raise ValueError('Missing trusted final test report')
    value = json.loads(last[len(PREFIX):])
    if value.get('schema') != 1 or not isinstance(value.get('outcomes'), dict) or not value['outcomes']:
        raise ValueError('Invalid test report')
    return value


def compare(baseline, candidate, *, require_improvement=False):
    before, after = report(baseline), report(candidate)
    if before['tests_run'] != after['tests_run'] or set(before['outcomes']) != set(after['outcomes']):
        raise ValueError('Candidate changed discovered test identities or count')
    if not any(status == 'success' for status in before['outcomes'].values()):
        raise ValueError('Baseline has no passing checks')
    regressions = [test for test, status in after['outcomes'].items()
                   if status != before['outcomes'][test]
                   and not (status == 'success' and before['outcomes'][test] in ('failure', 'error'))]
    if regressions:
        raise ValueError('Candidate introduced failures, errors or skips: ' + ', '.join(sorted(regressions)))
    improved = [test for test, status in before['outcomes'].items()
                if status in ('failure', 'error') and after['outcomes'][test] == 'success']
    if require_improvement and not improved:
        raise ValueError('Failed-CI repair must resolve at least one baseline failure; no improvement measured')
    existing = {test: status for test, status in before['outcomes'].items() if status in ('failure', 'error')}
    result = {'tests_run': after['tests_run'], 'regressions': 0, 'improved_tests': improved,
              'restricted_baseline_failures': existing,
              'boundary': 'Identical restricted environments; unchanged baseline failures are not passing tests. Automatic source application requires full exact-base CI separately; model proposals remain untrusted drafts.'}
    print(json.dumps(result, sort_keys=True))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['record', 'compare'])
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--candidate', type=Path)
    args = parser.parse_args()
    if args.operation == 'record':
        record()
    else:
        compare(args.baseline, args.candidate, require_improvement=os.environ.get('REQUIRE_IMPROVEMENT') == 'true')


if __name__ == '__main__':
    main()
