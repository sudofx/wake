# =============================================================================
# TESTING INTENT — gemini failover
#
# This file is executable documentation. Passing cases define behavior WAKE✳︎
# promises to preserve; rejection/failure cases define boundaries that future
# refactors must not weaken merely to make CI green. Read assertions as part of
# the architectural contract, not just as coverage machinery.
# =============================================================================

# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for gemini failover.
# Tests in WAKE✳︎ are part of the explanation of the system: successful cases show what authority is allowed,
# while rejection/failure cases show the boundaries that must remain intact during refactors.
# Prefer assertions that make the invariant obvious to a human or AI maintainer reading this file later.

"""Offline proofs of cross-model failover, durable receipts, and unchanged governance."""
import io
import json
import ssl
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

from wake.engine import DEFAULTS, Engine, config
from wake.governance import Rejected
from wake.providers import Gemini, Fixture, FREE_TIER_DAILY_QUOTA_ID
from wake.scheduling import wake_status
from wake.report import export


class Response:
    status = 200
    def __init__(self, raw):
        self.raw = raw
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self, maximum):
        return json.dumps({"candidates": [{"finishReason": "STOP", "content": {"parts": [{"text": self.raw}]}}]}).encode()


def failure(status, quota=None):
    body = {"error": {"code": status, "details": [{"violations": [{"quotaId": quota}]}]}}
    return urllib.error.HTTPError("https://example.invalid", status, "error", {}, io.BytesIO(json.dumps(body).encode()))


class FailoverTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.settings = {**DEFAULTS, "model": "gemini-3.8-flash", "free_tier_confirmed": True,
                         "gemini_fallback_models": ["gemini-3.5-flash", "gemini-3.1-flash-lite"],
                         "mission": "Explore big ideas through small useful projects."}
        self.engine = Engine(Path(self.temp.name) / "data", self.settings)
        self.env = patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"})
        self.env.start()
        self.requests = []

    def tearDown(self):
        self.engine.store.close()
        self.env.stop()
        self.temp.cleanup()

    def run_chain(self, outcomes, checkpoint=None):
        iterator = iter(outcomes)
        def send(req, **kwargs):
            self.requests.append(req)
            outcome = next(iterator)
            if isinstance(outcome, Exception):
                raise outcome
            if outcome == "valid":
                body = json.loads(req.data)
                context = json.loads(body["contents"][0]["parts"][0]["text"])
                raw, _ = Fixture().propose({"context": context})
                return Response(raw)
            return outcome
        with patch("urllib.request.urlopen", side_effect=send) as network:
            result = self.engine.run(Gemini(self.settings), checkpoint=checkpoint)
        state = self.engine.store.load()
        return result, state, state["invocations"][result["id"]], network

    def test_primary_success(self):
        result, state, item, network = self.run_chain(["valid"])
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(network.call_count, 1)
        self.assertEqual(item["provider_requests_sent"], 1)
        self.assertEqual(item["successful_model"], self.settings["model"])

    def test_successful_fallback_is_one_research_cycle_with_identical_payload(self):
        result, state, item, network = self.run_chain([failure(503), "valid"])
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(state["version"], 1)
        self.assertEqual(len(state["journal"]), 1)
        self.assertEqual(network.call_count, 2)
        self.assertEqual(item["provider_requests_sent"], 2)
        self.assertEqual(item["successful_model"], "gemini-3.5-flash")
        self.assertEqual([a["http_status"] for a in item["provider_attempts"]], [503, 200])
        self.assertEqual([a["result"] for a in item["provider_attempts"]], ["transient_failure", "success"])
        self.assertEqual([a["model"] for a in item["provider_attempts"]], [self.settings["model"], "gemini-3.5-flash"])
        self.assertEqual(self.requests[0].data, self.requests[1].data)
        self.assertNotEqual(self.requests[0].full_url, self.requests[1].full_url)
        generation = json.loads(self.requests[1].data)["generationConfig"]
        self.assertEqual(generation, {"responseMimeType": "application/json", "maxOutputTokens": 4096,
                                      "thinkingConfig": {"thinkingLevel": "low"}})
        for a in item["provider_attempts"]:
            self.assertGreaterEqual(a["elapsed_ms"], 0)
            self.assertEqual(a["request_payload_bytes"], len(self.requests[0].data))
        replayed, _ = self.engine.store.replay()
        self.assertEqual(replayed, state)
        status = wake_status(state)
        self.assertEqual(status["attempts_today"], 1)
        self.assertEqual(status["provider_requests_today"], 2)
        self.assertEqual(status["latest_attempt"]["provider_requests_sent"], 2)
        export(self.engine.store, Path(self.temp.name) / "site")
        page = (Path(self.temp.name) / "site" / "index.html").read_text()
        self.assertIn("Which version answers?", page)
        self.assertIn("gemini-3.8-flash", page)
        self.assertIn("gemini-3.5-flash", page)

    def test_all_unavailable_deduplicates_and_defers_without_research(self):
        self.settings["gemini_fallback_models"] += [self.settings["model"], "gemini-3.5-flash"]
        result, state, item, network = self.run_chain([failure(503), failure(503), failure(503)])
        self.assertEqual(result["status"], "deferred")
        self.assertEqual(state["version"], 0)
        self.assertFalse(state["journal"])
        self.assertEqual(network.call_count, 3)
        self.assertEqual(item["provider_requests_sent"], 3)
        self.assertEqual(len({r.full_url for r in self.requests}), 3)
        self.assertEqual([a["model"] for a in item["provider_attempts"]],
                         [self.settings["model"], "gemini-3.5-flash", "gemini-3.1-flash-lite"])
        self.assertEqual(result["provider_error"]["provider_requests_sent"], 3)

    def test_each_transient_http_code_can_fail_over(self):
        for status in (500, 502, 503, 504):
            with self.subTest(status=status):
                result, _, item, network = self.run_chain([failure(status), "valid"])
                self.assertEqual(result["status"], "accepted")
                self.assertEqual(network.call_count, 2)

    def test_auth_request_and_unclassified_quota_stop_chain(self):
        for status in (400, 401, 403, 404, 429):
            with self.subTest(status=status):
                result, _, item, network = self.run_chain([failure(status)])
                self.assertEqual(result["status"], "failed")
                self.assertEqual(network.call_count, 1)
                self.assertNotIn("quota_exhausted", item)

    def test_exact_quota_on_one_model_continues_to_next_model(self):
        result, state, item, network = self.run_chain(
            [failure(503), failure(429, FREE_TIER_DAILY_QUOTA_ID), "valid"])
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(network.call_count, 3)
        self.assertEqual(item["successful_model"], "gemini-3.1-flash-lite")
        self.assertEqual([a["result"] for a in item["provider_attempts"]],
                         ["transient_failure", "daily_quota", "success"])

    def test_exact_quota_on_last_available_model_defers(self):
        result, state, item, network = self.run_chain(
            [failure(503), failure(503), failure(429, FREE_TIER_DAILY_QUOTA_ID)])
        self.assertEqual(result["status"], "deferred")
        self.assertEqual(item["quota_exhausted"], "free_tier_daily")
        self.assertEqual(network.call_count, 3)
        self.assertEqual(item["provider_error"]["model"], "gemini-3.1-flash-lite")

    def test_transport_availability_fails_over_but_tls_configuration_does_not(self):
        for error in (TimeoutError(), urllib.error.URLError(ConnectionRefusedError())):
            result, _, _, network = self.run_chain([error, "valid"])
            self.assertEqual(result["status"], "accepted")
            self.assertEqual(network.call_count, 2)
        result, _, _, network = self.run_chain([urllib.error.URLError(ssl.SSLCertVerificationError())])
        self.assertEqual(result["status"], "failed")
        self.assertEqual(network.call_count, 1)

    def test_runtime_and_invalid_response_never_fail_over(self):
        for outcome in (RuntimeError("bug"), Response("not json")):
            result, _, item, network = self.run_chain([outcome])
            self.assertIn(result["status"], ("failed", "rejected"))
            self.assertEqual(network.call_count, 1)
            self.assertEqual(item["provider_requests_sent"], 1)

    def test_daily_ceiling_bounds_fallbacks_and_subsequent_wakes(self):
        self.settings["daily_call_limit"] = 2
        result, _, item, network = self.run_chain([failure(503), failure(503)])
        self.assertEqual(result["status"], "deferred")
        self.assertEqual(network.call_count, 2)
        with patch("urllib.request.urlopen") as network:
            with self.assertRaisesRegex(Rejected, "Daily call ceiling"):
                self.engine.run(Gemini(self.settings))
            network.assert_not_called()

    def test_checkpoint_failure_cannot_trigger_fallback(self):
        def checkpoint():
            if len(self.requests) == 1:
                raise RuntimeError("persistence failed")
        with self.assertRaisesRegex(RuntimeError, "persistence failed"):
            self.run_chain([failure(503), "valid"], checkpoint=checkpoint)
        self.assertEqual(len(self.requests), 1)
        item = next(iter(self.engine.store.load()["invocations"].values()))
        self.assertEqual(item["provider_requests_sent"], 1)
        self.assertEqual(len(item["provider_attempts"]), 1)

    def test_interruption_preserves_unknown_reservation_without_repeating_model(self):
        with patch("urllib.request.urlopen", side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                self.engine.run(Gemini(self.settings))
        self.engine.recover()
        state = self.engine.store.load()
        item = next(iter(state["invocations"].values()))
        self.assertEqual(item["status"], "recovered")
        self.assertEqual(item["provider_attempts"][0]["result"], "unknown")
        self.assertEqual(state["version"], 0)
        self.assertTrue(wake_status(state)["provider_request_counts_incomplete"])

    def test_unverified_request_compatibility_rejected_before_http(self):
        with patch("urllib.request.urlopen") as network:
            with self.assertRaisesRegex(Rejected, "compatibility"):
                Gemini({**self.settings, "gemini_fallback_models": ["gemini-2.5-flash"]})
            network.assert_not_called()

    def test_last_fallback_can_succeed_without_extra_research_cycles(self):
        result, state, item, network = self.run_chain([failure(503), failure(502), "valid"])
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(network.call_count, 3)
        self.assertEqual(item["successful_model"], "gemini-3.1-flash-lite")
        self.assertEqual(item["provider_requests_sent"], 3)
        self.assertEqual(state["version"], 1)
        self.assertEqual(len(state["journal"]), 1)
        self.assertEqual(len({r.data for r in self.requests}), 1)

    def test_governance_rejection_of_fallback_stops_without_version_advance(self):
        proposal = json.dumps({"base_version": 999, "title": "Bad version", "summary": "Rejected", "actions": []})
        result, state, item, network = self.run_chain([failure(503), Response(proposal)])
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(network.call_count, 2)
        self.assertEqual(item["provider_requests_sent"], 2)
        self.assertEqual(len(item["provider_attempts"]), 2)
        self.assertEqual(state["version"], 0)
        self.assertFalse(state["journal"])

    def test_attempt_results_are_checkpointed_before_next_model(self):
        snapshots = []
        def checkpoint():
            snapshots.append(self.engine.store.load())
        self.run_chain([failure(503), "valid"], checkpoint=checkpoint)
        attempts = [next(iter(s["invocations"].values())).get("provider_attempts", []) for s in snapshots]
        self.assertIn(["unknown"], [[a["result"] for a in group] for group in attempts])
        self.assertIn(["transient_failure"], [[a["result"] for a in group] for group in attempts])
        self.assertIn(["transient_failure", "unknown"], [[a["result"] for a in group] for group in attempts])

    def test_missing_key_never_sends_request(self):
        with patch.dict("os.environ", {}, clear=True), patch("wake.providers.load_env"), \
                patch("urllib.request.urlopen") as network:
            with self.assertRaisesRegex(Rejected, "GEMINI_API_KEY is missing"):
                Gemini(self.settings)
            network.assert_not_called()

    def test_repository_configuration_restores_historical_order(self):
        settings = config(Path(__file__).resolve().parents[1] / "wake.toml")
        self.assertEqual(settings["model"], "gemini-3.8-flash")
        self.assertEqual(settings["gemini_fallback_models"], ["gemini-3.5-flash", "gemini-3.1-flash-lite"])
        self.assertIn("WAKE✳︎", [topic["label"] for topic in settings["research_topics"]])
