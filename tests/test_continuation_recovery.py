"""A transport watchdog must not override operator/application stops or duplicate work."""
from datetime import datetime, timedelta, timezone
import unittest
from unittest.mock import patch
from scripts import repair_continuation
from scripts.repair_continuation import recovery_reason


class ContinuationRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc)
        self.run = dict(id=1, head_sha='live', head_branch='wake-runtime',
                        created_at=(self.now-timedelta(minutes=10)).isoformat(),
                        status='completed', conclusion='failure')

    def test_failed_handoff_can_resume_exact_runtime(self):
        jobs = {1: [dict(name='continue-again', conclusion='failure')]}
        self.assertEqual(recovery_reason([self.run], jobs, 'live', self.now), 'successor-dispatch-failed')
        self.assertIsNone(recovery_reason([self.run], jobs, 'new-runtime', self.now))

    def test_application_failure_or_manual_cancellation_does_not_restart(self):
        self.assertIsNone(recovery_reason([self.run], {1: [dict(name='wake', conclusion='failure'),
                            dict(name='continue-again', conclusion='skipped')]}, 'live', self.now))
        self.run['conclusion'] = 'cancelled'
        self.assertIsNone(recovery_reason([self.run], {}, 'live', self.now))

    def test_active_or_fresh_queued_run_prevents_duplicate_dispatch(self):
        jobs = {1: [dict(name='continue-again', conclusion='failure')]}
        active = {**self.run, 'id': 2, 'status': 'in_progress'}
        self.assertIsNone(recovery_reason([self.run, active], jobs, 'live', self.now))
        active.update(status='queued', created_at=self.now.isoformat())
        self.assertIsNone(recovery_reason([self.run, active], jobs, 'live', self.now))

    def test_stale_zero_job_entry_does_not_mask_timed_out_attempt(self):
        self.run['conclusion'] = 'timed_out'
        stale = {**self.run, 'id': 2, 'status': 'queued'}
        self.assertEqual(recovery_reason([self.run, stale], {}, 'live', self.now), 'execution-timeout')

    def test_latest_attempt_with_application_failure_overrules_old_timeout(self):
        self.run['conclusion'] = 'timed_out'
        later = {**self.run, 'id': 2, 'created_at': self.now.isoformat(), 'conclusion': 'failure'}
        self.assertIsNone(recovery_reason([self.run, later], {}, 'live', self.now))

    def test_quota_resume_is_due_only_after_midnight_and_once_per_pacific_date(self):
        due = datetime(2026, 9, 15, 7, 0, tzinfo=timezone.utc)
        self.assertIsNone(repair_continuation.quota_resume_token(due.isoformat(), due-timedelta(minutes=1)))
        self.assertEqual(repair_continuation.quota_resume_token(due.isoformat(), due+timedelta(minutes=1)),
                         'quota-resume-2026-09-15')
        self.assertIsNone(repair_continuation.quota_resume_token(due.isoformat(), due+timedelta(hours=3)))
        self.assertIsNone(repair_continuation.quota_resume_token(None, due+timedelta(minutes=1)))
        self.assertTrue(repair_continuation.in_quota_check_window(due+timedelta(hours=2)))
        self.assertFalse(repair_continuation.in_quota_check_window(due+timedelta(hours=3)))

    def test_closed_operator_latch_never_dispatches(self):
        with patch.dict('os.environ', {'GITHUB_REPOSITORY': 'fixture/wake'}), \
             patch.object(repair_continuation, 'api', return_value={'state': 'disabled_manually'}) as read, \
             patch.object(repair_continuation.subprocess, 'run') as dispatch:
            repair_continuation.main()
        read.assert_called_once()
        dispatch.assert_not_called()

    def test_concurrent_stop_wins_before_recovery_dispatch(self):
        reads = 0
        def api(repository, path):
            nonlocal reads
            if path == 'actions/workflows/wake-runner.yml':
                reads += 1
                return {'state': 'active' if reads == 1 else 'disabled_manually'}
            if 'operator-' in path or 'promote-runtime' in path:
                return {'workflow_runs': []}
            if path == 'git/ref/heads/wake-runtime':
                return {'object': {'sha': 'live'}}
            if '/jobs?' in path:
                return {'jobs': [dict(name='continue-again', conclusion='failure')]}
            return {'workflow_runs': [self.run]}
        with patch.dict('os.environ', {'GITHUB_REPOSITORY': 'fixture/wake'}), \
             patch.object(repair_continuation, 'api', side_effect=api), \
             patch.object(repair_continuation.subprocess, 'run') as dispatch:
            repair_continuation.main()
        dispatch.assert_not_called()
