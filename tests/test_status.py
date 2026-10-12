# =============================================================================
# TESTING INTENT — status
#
# This file is executable documentation. Passing cases define behavior WAKE✳︎
# promises to preserve; rejection/failure cases define boundaries that future
# refactors must not weaken merely to make CI green. Assertions should make the
# protected invariant understandable to both human and AI maintainers.
# =============================================================================
# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for status.
# Tests are documentation with teeth: passing cases define permitted behavior and rejection cases define protected boundaries.
# When changing implementation, preserve the reason behind an assertion rather than weakening it merely to make CI green.

"""Public research progress is derived from receipts, independently of publication."""
from datetime import datetime, timezone
import unittest
from wake.scheduling import wake_status
from wake.providers import FREE_TIER_DAILY_QUOTA_ID, FREE_TIER_MINUTE_QUOTA_ID

class StatusTests(unittest.TestCase):
    def test_latest_failure_does_not_replace_last_accepted_and_quota_reset_is_visible(self):
        accepted = dict(id="a", time="2026-09-14T08:00:00+00:00", status="accepted", charged=True, quota_day="2026-09-14")
        deferred = dict(id="b", time="2026-09-14T09:00:00+00:00", status="deferred", charged=True, quota_day="2026-09-14", reason="Gemini temporarily unavailable")
        state = dict(version=1, invocations={"a":accepted,"b":deferred}, pending=None)
        now = datetime(2026,9,14,9,1,tzinfo=timezone.utc)
        result = wake_status(state, now=now)
        self.assertEqual(result["last_accepted"]["id"], "a")
        self.assertEqual(result["latest_attempt"]["id"], "b")
        self.assertEqual(
            datetime.fromisoformat(result["next_eligible"]),
            datetime(2026,9,14,9,0,15,tzinfo=timezone.utc),
        )
        limited = wake_status(state, daily_call_limit=2, now=now)
        self.assertEqual(datetime.fromisoformat(limited["next_eligible"]).astimezone(timezone.utc), datetime(2026,9,15,7,tzinfo=timezone.utc))
        state["pending"] = "b"
        self.assertIsNone(wake_status(state, now=now)["next_eligible"])

    def test_unknown_reservation_is_visible_as_a_conservative_request_slot(self):
        interrupted = dict(
            id="a", time="2026-09-14T08:00:00+00:00", status="recovered",
            charged=True, quota_day="2026-09-14", provider_requests_sent=0,
            provider_attempts=[dict(model="gemini-test", result="unknown")],
        )
        state = dict(version=0, invocations={"a": interrupted}, pending=None)
        result = wake_status(state, now=datetime(2026,9,14,8,1,tzinfo=timezone.utc))
        self.assertEqual(result["attempts_today"], 1)
        self.assertEqual(result["provider_requests_today"], 0)
        self.assertEqual(result["provider_request_slots_today"], 1)
        self.assertTrue(result["provider_request_counts_incomplete"])

    def test_confirmed_requests_and_slots_match_when_attempts_are_complete(self):
        completed = dict(
            id="a", time="2026-09-14T08:00:00+00:00", status="accepted",
            charged=True, quota_day="2026-09-14", provider_requests_sent=2,
            provider_attempts=[
                dict(model="gemini-a", result="transient_failure"),
                dict(model="gemini-b", result="success"),
            ],
        )
        state = dict(version=1, invocations={"a": completed}, pending=None)
        result = wake_status(state, now=datetime(2026,9,14,8,1,tzinfo=timezone.utc))
        self.assertEqual(result["provider_requests_today"], 2)
        self.assertEqual(result["provider_request_slots_today"], 2)
        self.assertFalse(result["provider_request_counts_incomplete"])

    def test_per_model_quota_mode_has_no_aggregate_ceiling(self):
        completed = dict(id="a", time="2026-09-14T08:00:00+00:00", status="accepted", charged=True, quota_day="2026-09-14", provider_requests_sent=2)
        state = dict(version=1, invocations={"a": completed}, pending=None)
        result = wake_status(state, daily_call_limit=None, now=datetime(2026,9,14,8,1,tzinfo=timezone.utc))
        self.assertIsNone(result["daily_call_limit"])
        self.assertEqual(result["provider_request_slots_today"], 2)

    def test_configured_daily_limit_waits_until_midnight(self):
        quota = dict(id="q", time="2026-09-14T18:00:00+00:00", status="deferred",
                     charged=True, quota_day="2026-09-14", quota_exhausted="configured_daily_limit",
                     provider_requests_sent=20, reason="Configured daily request limits reached")
        state = dict(version=1, invocations={"q": quota}, pending=None)
        before = wake_status(state, daily_call_limit=20,
                             now=datetime(2026, 9, 15, 6, 59, tzinfo=timezone.utc))
        after = wake_status(state, daily_call_limit=20,
                            now=datetime(2026, 9, 15, 7, 1, tzinfo=timezone.utc))
        self.assertTrue(before["quota_standby"])
        self.assertFalse(after["quota_standby"])
        self.assertEqual(after["quota_standby_until"], "2026-09-15T07:00:00+00:00")

    def test_provider_daily_quota_stays_purple_but_does_not_gate_scheduled_retry(self):
        quota = dict(
            id="q", time="2026-09-14T18:00:00+00:00", status="deferred",
            charged=True, quota_day="2026-09-14", quota_exhausted="free_tier_daily",
            provider_requests_sent=4,
            reason="Gemini free-tier daily quotas exhausted for available models",
        )
        state = dict(version=0, invocations={"q": quota}, pending=None)
        before_reset = wake_status(state, daily_call_limit=None,
                                   now=datetime(2026, 9, 14, 18, 1, tzinfo=timezone.utc))
        after_reset = wake_status(state, daily_call_limit=None,
                                  now=datetime(2026, 9, 15, 7, 1, tzinfo=timezone.utc))
        for result in (before_reset, after_reset):
            self.assertTrue(result["provider_quota_limited"])
            self.assertTrue(result["quota_standby"])
            self.assertIsNone(result["next_eligible"])
            self.assertIsNone(result["quota_standby_until"])

        recovered = dict(id="ok", time="2026-09-15T07:02:00+00:00", status="accepted",
                         charged=True, quota_day="2026-09-15", provider_requests_sent=1)
        cleared = wake_status(dict(version=1, invocations={"q": quota, "ok": recovered}, pending=None),
                              daily_call_limit=None,
                              now=datetime(2026, 9, 15, 7, 3, tzinfo=timezone.utc))
        self.assertFalse(cleared["provider_quota_limited"])
        self.assertFalse(cleared["quota_standby"])

    def test_per_minute_quota_response_is_visible_until_later_success(self):
        limited = dict(
            id="limited", time="2026-09-14T09:00:00+00:00", status="deferred",
            charged=True, quota_day="2026-09-14", provider_requests_sent=1,
            provider_attempts=[dict(model="gemini-model", result="rate_limited")],
            reason="Gemini temporarily unavailable due to a per-minute model limit; wake deferred",
        )
        state = dict(version=0, invocations={"limited": limited}, pending=None)
        status = wake_status(state, daily_call_limit=None,
                             now=datetime(2026, 9, 14, 9, 1, tzinfo=timezone.utc))
        self.assertTrue(status["provider_quota_limited"])
        self.assertTrue(status["quota_standby"])

    def test_model_fallback_quota_does_not_pause_the_installation(self):
        daily_attempt = dict(
            model="gemini-primary", result="daily_quota",
            provider_error={"details": [{"violations": [{"quotaId": FREE_TIER_DAILY_QUOTA_ID}]}]},
        )
        minute_attempt = dict(
            model="gemini-fallback", result="rate_limited",
            provider_error={"details": [{"violations": [{"quotaId": FREE_TIER_MINUTE_QUOTA_ID}]}]},
        )
        fallback_success = dict(
            id="accepted", time="2026-09-14T09:00:00+00:00", status="accepted",
            charged=True, quota_day="2026-09-14", provider_requests_sent=2,
            provider_attempts=[daily_attempt, dict(model="gemini-fallback", result="success")],
        )
        now = datetime(2026, 9, 14, 9, 0, 10, tzinfo=timezone.utc)
        succeeded = wake_status(
            dict(version=1, invocations={"accepted": fallback_success}, pending=None),
            daily_call_limit=None, now=now,
        )
        self.assertFalse(succeeded["quota_standby"])
        self.assertIsNone(succeeded["next_eligible"])

        rate_limited = dict(
            id="limited", time="2026-09-14T09:00:00+00:00", status="deferred",
            charged=True, quota_day="2026-09-14", provider_requests_sent=2,
            provider_attempts=[daily_attempt, minute_attempt],
            reason="Gemini temporarily unavailable due to a per-minute model limit; wake deferred",
            provider_error={
                "retry_after_seconds": 22,
                "provider_error": {"details": [{"violations": [{"quotaId": FREE_TIER_MINUTE_QUOTA_ID}]}]},
                "provider_attempts": [daily_attempt, minute_attempt],
            },
        )
        waiting = wake_status(
            dict(version=0, invocations={"limited": rate_limited}, pending=None),
            daily_call_limit=None, now=now,
        )
        self.assertTrue(waiting["quota_standby"])
        self.assertTrue(waiting["provider_quota_limited"])
        self.assertEqual(
            datetime.fromisoformat(waiting["next_eligible"]),
            datetime(2026, 9, 14, 9, 0, 22, tzinfo=timezone.utc),
        )

    def test_empty_state_has_no_invented_success(self):
        result = wake_status(dict(version=0, invocations={}, pending=None))
        self.assertIsNone(result["last_accepted"])
        self.assertIsNone(result["latest_attempt"])

class DailyProviderWaitTests(unittest.TestCase):
    def test_explicit_daily_wait_expires_at_midnight_but_minute_limit_does_not(self):
        from wake.scheduling import wake_status
        from datetime import datetime, timezone
        item = {'id': 'q', 'time': '2026-10-12T21:00:00+00:00', 'status': 'deferred', 'charged': True, 'quota_day': '2026-10-12', 'quota_exhausted': 'free_tier_daily', 'provider_requests_sent': 4, 'provider_attempts': [{'result': 'daily_quota'}]}
        state = {'version': 1, 'pending': None, 'invocations': {'q': item}}
        result = wake_status(state, None, datetime(2026,10,12,22,tzinfo=timezone.utc), wait_provider_daily=True)
        self.assertEqual(result['next_eligible'], '2026-10-13T07:00:00+00:00')
        self.assertIsNone(wake_status(state, None, datetime(2026,10,13,7,tzinfo=timezone.utc), wait_provider_daily=True)['next_eligible'])
        item.pop('quota_exhausted'); item['provider_attempts'] = [{'result': 'rate_limited'}]
        self.assertIsNone(wake_status(state, None, datetime(2026,10,12,22,tzinfo=timezone.utc), wait_provider_daily=True)['next_eligible'])
