"""Mandatory provider slots never fail open or stall an eligible fallback."""
import os
import unittest
from unittest.mock import patch

from wake.group_coordinator import GroupProviderGate, group_provider_gate
from wake.installation_gate import InstallationCallCoordinator, InstallationSlotUnavailable
from wake.providers import ProviderCallPaused


class InstallationProviderGateTests(unittest.TestCase):
    def test_shared_limit_returns_immediately_and_cancels_queue(self):
        for reason in ("daily_quota", "rate_limited", "access_blocked"):
            gate = GroupProviderGate("http://controller", "100.wake")
            packets = []
            def reply(packet):
                packets.append(packet)
                return {"status": "queued", "reason": reason, "retry_after": 300}
            with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1"}), patch.object(gate, "_request", side_effect=reply), patch("wake.group_coordinator.time.sleep") as sleep:
                with self.assertRaises(InstallationSlotUnavailable) as raised:
                    with gate.request("gemini"):
                        self.fail("Unavailable model obtained a provider slot")
                self.assertEqual(raised.exception.outcome["provider_call_made"], False)
                self.assertEqual(raised.exception.retry_after_seconds, 300)
                self.assertEqual([packet["action"] for packet in packets], ["acquire", "cancel"])
                sleep.assert_not_called()

    def test_busy_longpoll_response_does_not_add_a_second_of_delay(self):
        gate = GroupProviderGate("http://controller", "100.wake")
        replies = [{"status": "queued", "reason": "busy", "retry_after": 1},
                   {"status": "granted", "token": "slot"}]
        with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1"}), patch.object(gate, "_request", side_effect=replies), patch("wake.group_coordinator.time.sleep") as sleep:
            self.assertEqual(gate._acquire("a" * 32, "gemini"), "slot")
            sleep.assert_called_once_with(.05)

    def test_controller_failure_and_missing_url_never_send_provider_call(self):
        with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1"}):
            for url in ("http://controller", ""):
                gate = GroupProviderGate(url, "100.wake")
                with patch.object(gate, "_request", side_effect=OSError("offline")):
                    with self.assertRaises(ProviderCallPaused):
                        with gate.request("gemini"):
                            self.fail("Controller bypassed")

    def test_installation_factory_without_controller_still_fails_closed(self):
        with patch.dict(os.environ, {"WAKE_INSTALLATION_WORKER": "1",
                                    "WAKE_GROUP_COORDINATOR_URL": "",
                                    "WAKE_PUBLIC_HOSTNAME": ""}):
            gate = group_provider_gate({})
            self.assertIsNotNone(gate)
            with self.assertRaises(ProviderCallPaused):
                with gate.request("gemini"):
                    self.fail("Missing installation configuration bypassed controller")

    def test_release_sends_only_current_request_outcome(self):
        gate = GroupProviderGate("http://controller", "100.wake")
        releases = []
        def reply(packet):
            if packet["action"] == "acquire":
                return {"status": "granted", "token": "slot"}
            releases.append(packet)
            return {"status": "released"}
        with patch.object(gate, "_request", side_effect=reply):
            with gate.request("first"):
                gate.outcome = {"result": "success"}
            with gate.request("second"):
                pass
        self.assertEqual(releases[0]["outcome"], {"result": "success"})
        self.assertEqual(releases[1]["outcome"], {})

    def test_restore_retains_limits_but_never_restores_grant(self):
        clock = lambda: 1791932400.0
        coordinator = InstallationCallCoordinator(clock=clock)
        key = ("wake", "100.wake", "request")
        grant = coordinator.acquire(key, "daily", 1)
        coordinator.release(key, grant["token"], {"result": "daily_quota"})
        grant = coordinator.acquire(key, "access", 1)
        coordinator.release(key, grant["token"], {"http_status": 403})
        coordinator.acquire(key, "active", 1)
        saved = coordinator.dump_state()
        self.assertNotIn("token", str(saved))
        restored = InstallationCallCoordinator(clock=clock)
        restored.restore_state(saved)
        self.assertIsNone(restored.status()["active"])
        self.assertEqual(restored.acquire(key, "daily", 1)["reason"], "daily_quota")
        self.assertTrue(restored.cancel_request(key))
        self.assertEqual(restored.acquire(key, "access", 1)["reason"], "access_blocked")

    def test_cancel_queued_request_cannot_cancel_active_holder(self):
        coordinator = InstallationCallCoordinator()
        key = ("wake", "100.wake", "request")
        coordinator.acquire(key, "gemini", 1)
        self.assertFalse(coordinator.cancel_request(key))
        self.assertIsNotNone(coordinator.status()["active"])

    def test_restore_refuses_live_queue_and_invalid_deadlines(self):
        coordinator = InstallationCallCoordinator()
        for value in (float("nan"), float("inf"), -1, "later"):
            with self.assertRaises(ValueError):
                coordinator.restore_state({"version": 1, "models": {"gemini": {"probe_at": value}}})
        coordinator.acquire(("wake", "100.wake", "request"), "gemini", 1)
        with self.assertRaises(RuntimeError):
            coordinator.restore_state({"version": 1, "models": {}})


if __name__ == "__main__":
    unittest.main()
