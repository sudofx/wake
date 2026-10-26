import json
from pathlib import Path
import tempfile
import unittest

from wake.recovery_demo import (BASELINE, adjust, demonstrate, fixture_host,
                                observe_fixture, submit)


class RecoveryDemoTests(unittest.TestCase):
    def test_recovery_and_failure_records_replay_and_leave_baseline_restored(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'fixture'
            result = demonstrate(root)
            self.assertEqual(result['production_changes'], 0)
            self.assertEqual(result['model_calls'], 0)
            self.assertEqual(result['research_records_opened'], 0)
            self.assertEqual(result['forbidden_proposal_status'], 'rejected')
            for scenario in result['scenarios'].values():
                self.assertTrue(scenario['replay_verified'])
                self.assertEqual(scenario['state']['settings'], BASELINE)
                self.assertIsNone(scenario['state']['trial'])
            recovery = result['scenarios']['temporary_rate_limit']
            self.assertEqual(recovery['baseline_rate_limited_requests'], 3)
            self.assertEqual(recovery['adjusted_rate_limited_requests'], 2)
            self.assertEqual([c['status'] for c in recovery['state']['changes']],
                             ['applied', 'verified', 'reverted'])
            before = (root / 'result.json').read_bytes()
            with self.assertRaises(FileExistsError):
                demonstrate(root)
            self.assertEqual((root / 'result.json').read_bytes(), before)

    def test_allowlist_rejections_are_recorded_without_changing_settings(self):
        with tempfile.TemporaryDirectory() as folder:
            host = fixture_host(Path(folder) / 'record.sqlite')
            submit(host, 'initialize', {'fixture': True})
            # Establish eligible observations without the automatic proposer.
            for at in (0, 1):
                submit(host, 'observe', {'at': at, 'signal': 'rate_limited', 'enabled': True})
            for payload in ({'setting': 'governance_enabled', 'value': 0},
                            {'setting': 'retry_delay_seconds', 'value': 10000},
                            {'setting': 'retry_delay_seconds', 'value': True},
                            {'setting': 'max_concurrent_requests', 'value': 3}):
                before = host.context().state
                self.assertEqual(submit(host, 'adjust', payload).status, 'rejected')
                self.assertEqual(host.context().state, before)
            self.assertEqual(host.audit_context(), host.context())

    def test_single_trial_pause_cooldown_and_clock_guards(self):
        with tempfile.TemporaryDirectory() as folder:
            host = fixture_host(Path(folder) / 'record.sqlite')
            submit(host, 'initialize', {'fixture': True})
            observe_fixture(host, 0, 'timeout')
            self.assertEqual(host.context().state['settings'], BASELINE)
            observe_fixture(host, 1, 'timeout')
            self.assertEqual(host.context().state['settings']['max_concurrent_requests'], 1)
            self.assertEqual(submit(host, 'adjust', {'setting': 'retry_delay_seconds', 'value': 4}).status, 'rejected')
            observe_fixture(host, 2, 'no_observation', enabled=False)
            for at in (3, 4, 5):
                observe_fixture(host, at, 'timeout')
            self.assertIsNone(host.context().state['trial'])
            self.assertEqual(host.context().state['settings'], BASELINE)
            for at in (0, float('nan'), float('inf'), True):
                self.assertEqual(submit(host, 'observe', {'at': at, 'signal': 'timeout', 'enabled': True}).status, 'rejected')
            self.assertEqual(host.audit_context(), host.context())


if __name__ == '__main__':
    unittest.main()
