"""An installation cannot overlap model requests or bypass shared quota gates."""

from datetime import datetime
import threading
import unittest
from zoneinfo import ZoneInfo

from wake.installation_gate import InstallationCallCoordinator


class Clock:
    def __init__(self, local="2026-10-13T12:00:00"):
        self.now = datetime.fromisoformat(local).replace(tzinfo=ZoneInfo("America/Los_Angeles")).timestamp()

    def __call__(self):
        return self.now


class InstallationGateTests(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()
        self.gate = InstallationCallCoordinator(clock=self.clock, queue_ttl=100000)

    def acquire(self, member, model="gemini"):
        return self.gate.acquire(("wake", member, "request"), model, 1)

    def release(self, member, grant, outcome=None):
        return self.gate.release(("wake", member, "request"), grant["token"], outcome)

    def test_lease_expiry_never_opens_an_active_call(self):
        grant = self.acquire("a")
        self.clock.now += 10000
        self.assertEqual(self.acquire("b")["status"], "queued")
        self.assertEqual(self.acquire("a"), grant)
        self.assertFalse(self.gate.release(("wake", "a", "request"), "wrong"))
        self.assertEqual(self.acquire("b")["status"], "queued")
        self.assertTrue(self.release("a", grant))
        self.assertEqual(self.acquire("b")["status"], "granted")

    def test_release_persists_before_opening_slot(self):
        grant = self.acquire("a")
        saved = []
        def persist(packet):
            self.assertIsNotNone(self.gate.active)
            self.assertTrue(packet["models"]["gemini"]["daily"])
            saved.append(packet)
        self.assertTrue(self.gate.release(("wake", "a", "request"), grant["token"],
                                         {"result": "daily_quota"}, persist=persist))
        self.assertEqual(len(saved), 1)
        self.assertIsNone(self.gate.status()["active"])

    def test_release_persistence_failure_keeps_slot_held(self):
        grant = self.acquire("a")
        def persist(packet):
            raise OSError("Cannot persist schedule")
        with self.assertRaises(OSError):
            self.gate.release(("wake", "a", "request"), grant["token"],
                              {"result": "daily_quota"}, persist=persist)
        self.assertTrue(self.gate.status()["active"]["release_unresolved"])
        self.assertEqual(self.acquire("b", "alternate")["status"], "queued")
        self.assertTrue(self.gate.release(("wake", "a", "request"), grant["token"],
                                         persist=lambda packet: None))
        self.assertEqual(self.acquire("b", "alternate")["status"], "granted")

    def test_fifo_and_no_artificial_spacing(self):
        first = self.acquire("a")
        self.acquire("b")
        self.acquire("c")
        self.release("a", first, {"result": "success"})
        self.assertEqual(self.acquire("c")["reason"], "fifo")
        second = self.acquire("b")
        self.release("b", second, {"result": "http_failure", "http_status": 500})
        self.assertEqual(self.acquire("c")["status"], "granted")

    def test_concurrent_acquire_grants_exactly_one(self):
        barrier = threading.Barrier(12)
        answers = []
        def acquire(index):
            barrier.wait()
            answers.append(self.acquire(str(index)))
        threads = [threading.Thread(target=acquire, args=(index,)) for index in range(12)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(sum(item["status"] == "granted" for item in answers), 1)

    def test_only_confirmed_member_death_can_cancel_held_grant(self):
        self.acquire("a")
        self.acquire("b")
        self.assertEqual(self.gate.cancel_member("other"), 0)
        self.assertEqual(self.acquire("b")["status"], "queued")
        self.assertEqual(self.gate.cancel_member("a"), 1)
        self.assertEqual(self.acquire("b")["status"], "granted")

    def test_daily_probe_is_shared_and_eligible_models_bypass_blocked_head(self):
        first = self.acquire("a")
        self.release("a", first, {"result": "daily_quota"})
        self.assertEqual(self.acquire("b")["reason"], "daily_quota")
        other = self.acquire("c", "other-model")
        self.assertEqual(other["status"], "granted")
        self.release("c", other)
        self.clock.now = Clock("2026-10-13T23:55:00").now
        self.assertEqual(self.acquire("d")["reason"], "fifo")
        probe = self.acquire("b")
        self.release("b", probe, {"result": "daily_quota"})
        self.assertEqual(self.acquire("d")["retry_after"], 300)
        self.clock.now += 299
        self.assertEqual(self.acquire("d")["status"], "queued")
        self.clock.now += 1
        probe = self.acquire("d")
        self.assertEqual(probe["status"], "granted")
        self.release("d", probe, {"result": "success"})
        self.assertEqual(self.acquire("e")["status"], "granted")

    def test_daily_quota_id_alone_triggers_shared_daily_schedule(self):
        first = self.acquire("a")
        self.release("a", first, {"http_status": 429,
            "quota_ids": ["GenerateRequestsPerDayPerProjectPerModel-FreeTier"]})
        self.assertEqual(self.acquire("b")["reason"], "daily_quota")

    def test_malformed_outcome_cannot_hold_completed_call(self):
        first = self.acquire("a")
        self.release("a", first, {"result": {}, "category": [],
                                  "retry_after_seconds": float("nan")})
        self.assertEqual(self.acquire("b")["status"], "granted")

    def test_failed_recovery_probe_keeps_daily_throttle(self):
        first = self.acquire("a")
        self.release("a", first, {"result": "daily_quota"})
        self.clock.now = Clock("2026-10-13T23:55:00").now
        probe = self.acquire("b")
        self.release("b", probe, {"result": "transient_failure", "http_status": 503})
        self.assertEqual(self.acquire("c")["retry_after"], 300)

    def test_minute_retry_after_and_access_blocks_are_model_scoped(self):
        first = self.acquire("a")
        self.release("a", first, {"result": "rate_limited", "http_status": 429,
                                  "retry_after_seconds": 22})
        self.assertEqual(self.acquire("b")["retry_after"], 22)
        self.clock.now += 22
        grant = self.acquire("b")
        self.release("b", grant, {"http_status": 403})
        self.assertEqual(self.acquire("c")["reason"], "access_blocked")
        alternate = self.acquire("d", "alternate")
        self.assertEqual(alternate["status"], "granted")
        self.release("d", alternate)
        self.gate.clear_model("gemini")
        self.assertEqual(self.acquire("c")["status"], "granted")

    def test_status_and_outcome_exclude_tokens_and_raw_content(self):
        grant = self.acquire("a")
        self.assertNotIn(grant["token"], str(self.gate.status()))
        self.release("a", grant, {"result": "success", "prompt": "secret",
                                  "response": "secret", "credentials": "secret"})
        self.assertNotIn("secret", str(self.gate.status()))

    def test_abandoned_queued_ticket_expires_but_holder_does_not(self):
        gate = InstallationCallCoordinator(clock=self.clock, queue_ttl=10)
        gate.acquire(("wake", "a", "request"), "gemini", 1)
        gate.acquire(("wake", "b", "request"), "gemini", 1)
        self.clock.now += 11
        self.assertEqual(gate.status()["queued"], 0)
        self.assertEqual(gate.status()["active"]["member"], "a")

    def test_schedule_tracks_pacific_dst(self):
        for date in ("2026-07-13", "2026-12-13"):
            clock = Clock(date + "T12:00:00")
            gate = InstallationCallCoordinator(clock=clock)
            key = ("wake", "a", "request")
            grant = gate.acquire(key, "gemini", 1)
            gate.release(key, grant["token"], {"result": "daily_quota"})
            self.assertEqual(gate.status()["models"]["gemini"]["probe_at"],
                             Clock(date + "T23:55:00").now)


if __name__ == "__main__":
    unittest.main()
