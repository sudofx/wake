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

    def test_empty_state_has_no_invented_success(self):
        result = wake_status(dict(version=0, invocations={}, pending=None))
        self.assertIsNone(result["last_accepted"])
        self.assertIsNone(result["latest_attempt"])
