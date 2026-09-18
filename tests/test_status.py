"""Public research progress is derived from receipts, independently of publication."""
from datetime import datetime, timezone
import unittest
from wake.scheduling import wake_status

class StatusTests(unittest.TestCase):
    def test_latest_failure_does_not_replace_last_accepted_and_backoff_is_visible(self):
        accepted = dict(id="a", time="2026-09-14T08:00:00+00:00", status="accepted", charged=True, quota_day="2026-09-14")
        deferred = dict(id="b", time="2026-09-14T09:00:00+00:00", status="deferred", charged=True, quota_day="2026-09-14", reason="Gemini temporarily unavailable")
        state = dict(version=1, invocations={"a":accepted,"b":deferred}, pending=None)
        now = datetime(2026,9,14,9,1,tzinfo=timezone.utc)
        result = wake_status(state, now=now)
        self.assertEqual(result["last_accepted"]["id"], "a")
        self.assertEqual(result["latest_attempt"]["id"], "b")
        self.assertEqual(result["next_eligible"], "2026-09-14T09:10:00+00:00")
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

    def test_per_model_quota_mode_has_no_aggregate_ceiling(self):\n        completed = dict(id="a", time="2026-09-14T08:00:00+00:00", status="accepted", charged=True, quota_day="2026-09-14", provider_requests_sent=2)\n        state = dict(version=1, invocations={"a": completed}, pending=None)\n        result = wake_status(state, daily_call_limit=None, now=datetime(2026,9,14,8,1,tzinfo=timezone.utc))\n        self.assertIsNone(result["daily_call_limit"])\n        self.assertEqual(result["provider_request_slots_today"], 2)\n\n    def test_empty_state_has_no_invented_success(self):
        result = wake_status(dict(version=0, invocations={}, pending=None))
        self.assertIsNone(result["last_accepted"])
        self.assertIsNone(result["latest_attempt"])
