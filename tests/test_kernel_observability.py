"""Bounded diagnostics preserve full counts and historical failure meaning."""
from copy import deepcopy
import unittest

from wake.kernel.observability import build_application_observability


class DiagnosticRecord:
    def __init__(self):
        self.actions = tuple({
            'status': 'accepted', 'revision_after': revision,
            'proposal': {'operations': [{'action': 'apply_application', 'key': 'demo',
                                         'value': {'action': 'add'}}]},
        } for revision in range(1, 6))
        self.invocations = tuple(event for index, (outcome, detail) in enumerate((
            (None, 'effect_barrier:OSError'),
            ('effect_barrier_failure', 'effect_barrier:OSError'),
            ('provider_failure', 'OSError'),
        )) for event in (
            {'invocation_id': str(index), 'stage': 'context_delivered',
             'context_receipt': {'scope': {'kind': 'application', 'application_id': 'demo'}}},
            {'invocation_id': str(index), 'stage': 'attempt_started'},
            {'invocation_id': str(index), 'stage': 'failed', 'outcome': outcome, 'detail': detail},
        ))

    def full_replay(self):
        return 5, {'app:demo': {'application_version': '1'}}

    def history(self):
        return self.actions

    def invocation_history(self):
        return self.invocations


class KernelObservabilityTests(unittest.TestCase):
    def test_limits_bound_recent_lists_without_truncating_full_counts(self):
        record = DiagnosticRecord()
        before = deepcopy((record.actions, record.invocations))
        for limit in (0, -1, 1, 2, 20):
            with self.subTest(limit=limit):
                projection = build_application_observability(
                    record, recent_actions=limit, recent_invocations=limit)
                app = projection['applications'][0]
                self.assertEqual(len(app['actions']['recent']), min(5, max(0, limit)))
                self.assertEqual(len(app['invocations']['recent']), min(3, max(0, limit)))
                self.assertEqual(app['actions']['accepted'], 5)
                self.assertEqual(app['invocations']['failed'], 3)
                if limit > 0:
                    self.assertEqual(app['actions']['recent'][-1]['revision_after'], 5)
                    self.assertEqual(app['invocations']['recent'][-1]['invocation_id'], '2')
                self.assertFalse(projection['authoritative'])
        self.assertEqual((record.actions, record.invocations), before)

    def test_barrier_failures_include_legacy_details_without_double_counting(self):
        record = DiagnosticRecord()
        metrics = build_application_observability(record)['applications'][0]['invocations']
        self.assertEqual(metrics['effect_barrier_failures'], 2)
        self.assertEqual(metrics['provider_failures'], 1)
        self.assertEqual(metrics['attempts'], 3)
        self.assertEqual(metrics['completed'], 0)


if __name__ == '__main__':
    unittest.main()
