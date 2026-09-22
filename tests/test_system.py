# =============================================================================
# TESTING INTENT — system
#
# Executable documentation: passing cases preserve promised behavior; rejection
# cases preserve protected boundaries. Never weaken an invariant merely to make
# CI green; understand why the test exists before changing it.
# =============================================================================

# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for system.
# Tests are documentation with teeth: passing cases define permitted behavior and rejection cases define protected boundaries.
# When changing implementation, preserve the reason behind an assertion rather than weakening it merely to make CI green.

"""Behavioral checks for the boundaries the experiment actually relies on."""

from datetime import datetime
from email.message import Message
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error
from zoneinfo import ZoneInfo

from wake.audit import verify_history
from wake.engine import DEFAULTS, Engine
from wake.governance import Rejected
from wake.providers import Fixture, Gemini
from wake.report import export
from wake.store import IntegrityError, canonical


class SystemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root / "data", dict(DEFAULTS))
        with self.engine.store.lock():
            self.engine.initialize()

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def propose(self, mutate=lambda p: None):
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "adversarial")
            proposal = json.loads(Fixture().propose(request)[0])
            mutate(proposal)
            result = self.engine.finish(invocation, json.dumps(proposal))
        return result

    def test_reset_returns_to_cycle_zero_and_erases_accumulated_state(self):
        self.engine.run(Fixture("before-reset"))
        (self.root / "data" / "experiment.json").write_text('{"old": true}')
        self.assertGreater(self.engine.store.load()["version"], 0)

        with self.engine.store.lock():
            self.engine.store.reset()
            state = self.engine.initialize()

        self.assertEqual(state["version"], 0)
        self.assertEqual(state["beliefs"], {})
        self.assertEqual(state["commitments"], {})
        self.assertEqual(state["evidence"], {})
        self.assertEqual(state["journal"], [])
        self.assertEqual(state["posts"], {})
        self.assertEqual(state["invocations"], {})
        self.assertIsNone(state["pending"])
        self.assertFalse((self.root / "data" / "experiment.json").exists())
        self.assertEqual([event["kind"] for event in self.engine.store.events()],
                         ["initialized", "experimental_regime_adopted"])

    def test_new_provider_inherits_commitment(self):
        first = self.engine.run(Fixture("a"))
        second = self.engine.run(Fixture("b"))
        state = self.engine.store.load()
        item = state["commitments"]["handoff-1"]
        self.assertEqual(item["created_by"], first["id"])
        self.assertEqual(item["resolved_by"], second["id"])
        self.assertEqual(item["status"], "fulfilled")

    def test_invalid_action_rejects_entire_proposal(self):
        result = self.propose(lambda p: p["actions"].append({"type": "shell", "command": "echo forbidden"}))
        state = self.engine.store.load()
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(state["version"], 0)
        self.assertEqual(state["commitments"], {})
        self.assertEqual(state["invocations"][result["id"]]["status"], "rejected")

    def test_stale_version_is_rejected(self):
        self.assertEqual(self.propose(lambda p:p.update(base_version=-1))["status"], "rejected")

    def test_objective_edit_is_rejected(self):
        self.assertEqual(self.propose(lambda p:p.update(objective="Ignore rules"))["status"], "rejected")

    def test_missing_evidence_is_rejected(self):
        action = {"type":"belief", "id":"b", "statement":"A claim", "confidence":.9,
                  "status":"active", "evidence":["invented"], "reason":"I made it up"}
        self.assertEqual(self.propose(lambda p:p["actions"].append(action))["status"], "rejected")

    def test_nonfinite_confidence_is_rejected(self):
        self.assertEqual(self.propose(lambda p:p.update(base_version=float("nan")))["status"], "rejected")

    def test_model_cannot_cancel_commitment(self):
        self.engine.run(Fixture())
        self.assertEqual(self.propose(lambda p:p["actions"][0].update(status="cancelled"))["status"], "rejected")
        self.assertEqual(self.engine.store.load()["commitments"]["handoff-1"]["status"], "open")

    def test_model_cannot_resolve_own_new_commitment(self):
        def mutation(p):
            p["actions"].append({"type":"resolve", "id":"handoff-1", "status":"fulfilled",
                                 "evidence":[list(self.engine.store.load()["evidence"])[-1]], "reason":"Immediately done"})
        self.assertEqual(self.propose(mutation)["status"], "rejected")

    def test_commitment_due_cycle_requires_future(self):
        self.assertEqual(self.propose(lambda p:p["actions"][0].update(due_cycle=1))["status"], "rejected")

    def test_belief_evidence_lifecycle(self):
        with self.engine.store.lock():
            self.engine.observe("Synthetic measurement within range", "fixture:sensor")
        self.engine.run(Fixture())
        with self.engine.store.lock():
            self.engine.observe("Synthetic counterexample outside range", "fixture:sensor")
        self.engine.run(Fixture())
        belief = self.engine.store.load()["beliefs"]["sensor"]
        self.assertEqual(belief["status"], "retracted")
        self.assertEqual(len(belief["evidence"]), 2)
        self.assertEqual(belief["confidence"], 0)

    def test_belief_review_requires_new_evidence(self):
        with self.engine.store.lock():
            self.engine.observe("Measurement", "fixture:sensor")
        self.engine.run(Fixture())
        b = self.engine.store.load()["beliefs"]["sensor"]
        action = {key:b[key] for key in ("type","id","statement","confidence","status","evidence","reason")}
        self.assertEqual(self.propose(lambda p:p["actions"].append(action))["status"], "rejected")

    def test_invalid_json_records_rejection(self):
        with self.engine.store.lock():
            inv, _ = self.engine.start("manual", "desktop")
            result = self.engine.finish(inv, "{truncated")
        self.assertEqual(result["status"], "rejected")
        self.assertIsNone(self.engine.store.load()["pending"])

    def test_manual_request_survives_restart(self):
        with self.engine.store.lock():
            inv, request = self.engine.start("manual", "Claude / human-attested")
        reopened = Engine(self.root / "data")
        try:
            self.assertEqual(reopened.store.load()["pending"], inv)
            with self.assertRaises(Rejected):
                reopened.run(Fixture())
            with reopened.store.lock():
                self.assertEqual(reopened.finish(inv, Fixture().propose(request)[0])["status"], "accepted")
        finally:
            reopened.store.close()

    def test_projection_can_be_rebuilt_but_history_cannot_be_silently_repaired(self):
        self.engine.run(Fixture())
        original = self.engine.store.load()
        with self.engine.store.db:
            self.engine.store.db.execute("UPDATE snapshot SET state='broken'")
        with self.assertRaises(IntegrityError):
            self.engine.store.load()
        with self.engine.store.lock():
            self.assertEqual(self.engine.recover(), original)
        with self.engine.store.db:
            self.engine.store.db.execute("UPDATE events SET payload='{}' WHERE seq=1")
        with self.assertRaises(IntegrityError):
            self.engine.recover()

    def test_quota_is_reserved_before_failure_and_survives_restart(self):
        class Failure(Fixture):
            charged = True
            def propose(self, request):
                raise RuntimeError("Failure")
        self.engine.config["daily_call_limit"] = 2
        self.assertEqual(self.engine.run(Failure())["status"], "failed")
        self.assertEqual(self.engine.run(Failure())["status"], "failed")
        restarted = Engine(self.root / "data", self.engine.config)
        try:
            with self.assertRaisesRegex(Rejected, "Daily call ceiling"):
                restarted.run(Failure())
        finally:
            restarted.store.close()
        self.assertEqual(len(self.engine.store.load()["invocations"]), 2)

    def test_quota_resets_at_pacific_midnight(self):
        class Charged(Fixture):
            charged = True
        self.engine.config["daily_call_limit"] = 1
        with patch("wake.engine.datetime") as clock:
            clock.now.return_value = datetime(2026, 9, 9, 23, 59, tzinfo=ZoneInfo("America/Los_Angeles"))
            self.engine.run(Charged())
            with self.assertRaises(Rejected):
                self.engine.run(Charged())
            clock.now.return_value = datetime(2026, 9, 10, 0, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
            self.assertEqual(self.engine.run(Charged())["status"], "accepted")

    def test_exact_daily_quota_is_deferred_and_blocks_same_day_recall(self):
        from wake.providers import DailyQuotaExceeded
        details = {
            "model": "gemini-3.8-flash",
            "result": "daily_quota",
            "http_status": 429,
            "provider_error": {
                "status": "RESOURCE_EXHAUSTED",
                "details": [{"violations": [{
                    "quotaId": "GenerateRequestsPerDayPerProjectPerModel-FreeTier",
                    "quotaMetric": "generativelanguage.googleapis.com/generate_content_free_tier_requests",
                    "quotaValue": "20",
                }]}],
            },
        }

        class Exhausted:
            name = "gemini"
            model = "gemini-3.8-flash"
            charged = True
            def propose(self, request):
                raise DailyQuotaExceeded(
                    "Gemini free-tier daily quota exhausted; wake deferred until Pacific midnight",
                    details,
                )

        result = self.engine.run(Exhausted())
        self.assertEqual(result["status"], "deferred")
        self.assertEqual(result["quota_exhausted"], "free_tier_daily")
        invocation = self.engine.store.load()["invocations"][result["id"]]
        self.assertEqual(invocation["status"], "deferred")
        self.assertEqual(invocation["provider_error"]["http_status"], 429)

        class NeverCall(Exhausted):
            def propose(self, request):
                raise AssertionError("Daily quota guard must suppress the provider call")

        with self.assertRaisesRegex(Rejected, "daily quota exhausted"):
            self.engine.run(NeverCall())
        self.assertEqual(len(self.engine.store.load()["invocations"]), 1)

    def test_context_ceiling_prevents_call(self):
        self.engine.config["max_context_chars"] = 10
        class NoCall(Fixture):
            def propose(self, request):
                raise AssertionError("Provider should never be called")
        with self.assertRaisesRegex(Rejected, "Context ceiling"):
            self.engine.run(NoCall())
        self.assertEqual(self.engine.store.load()["invocations"], {})

    def test_lock_prevents_competing_process(self):
        with self.engine.store.lock():
            result = subprocess.run([sys.executable,"-m","wake","--data",str(self.root/"data"),"wake","--provider","fixture"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Another wake owns", result.stderr)
        self.assertEqual(self.engine.store.load()["version"], 0)

    def test_real_process_death_during_commit_rolls_back(self):
        self.engine.run(Fixture())
        result = subprocess.run([sys.executable,"-m","wake","--data",str(self.root/"data"),"wake","--provider","fixture","--crash-at","during-commit"], capture_output=True)
        self.assertEqual(result.returncode, 86)
        with self.engine.store.lock():
            state = self.engine.recover()
        self.assertEqual(state["version"], 1)
        self.assertEqual(sum(i["status"]=="recovered" for i in state["invocations"].values()), 1)

    def test_audit_can_reconstruct_without_database(self):
        self.engine.run(Fixture())
        export(self.engine.store, self.root / "site")
        reconstructed, _ = verify_history(self.root/"site/events.jsonl", (self.root/"site/head.txt").read_text())
        self.assertEqual(canonical(reconstructed), canonical(self.engine.store.load()))

    def test_external_head_detects_valid_prefix_truncation(self):
        self.engine.run(Fixture())
        export(self.engine.store, self.root / "site")
        log = self.root/"site/events.jsonl"
        log.write_text("\n".join(log.read_text().splitlines()[:-1])+"\n")
        with self.assertRaises(IntegrityError):
            verify_history(log, (self.root/"site/head.txt").read_text())

    def test_working_set_shadow_is_lossy_traceable_and_not_delivered(self):
        with self.engine.store.lock():
            self.engine.observe("X" * 2000, "human:detail", evidence_id="e-detail")
            invocation, request = self.engine.start("fixture", "shadow-test")
            proposal = {
                "base_version": 0,
                "title": "Create a test belief",
                "summary": "Use one exact observation to seed a belief.",
                "actions": [{
                    "type": "belief",
                    "id": "shadow-belief",
                    "statement": "A deliberately verbose working claim " + ("Y" * 500),
                    "confidence": 0.6,
                    "status": "active",
                    "evidence": ["e-detail"],
                    "reason": "Retain the decision-relevant lesson while exact detail stays in evidence.",
                }],
            }
            self.engine.finish(invocation, json.dumps(proposal))

            second, second_request = self.engine.start("fixture", "shadow-test-2")
            state = self.engine.store.load()
            item = state["invocations"][second]
            shadow = item["working_set_shadow"]
            metrics = item["working_set_metrics"]

        self.assertEqual(shadow["mode"], "shadow")
        self.assertEqual(shadow["beliefs"][0]["id"], "shadow-belief")
        self.assertIn("e-detail", shadow["beliefs"][0]["provenance"])
        self.assertNotIn("X" * 200, canonical(shadow))
        self.assertLess(len(shadow["beliefs"][0]["claim"]), 340)
        self.assertGreater(metrics["delivered_context_chars"], 0)
        self.assertGreater(metrics["working_set_chars"], 0)
        self.assertNotIn("working_set_shadow", second_request["context"])
        self.assertNotIn("working_set_metrics", second_request["context"])
        self.assertNotIn("trust_compacts_shadow", second_request["context"])
        self.assertNotIn("inquiry_drive_shadow", second_request["context"])
        self.assertEqual(item["inquiry_drive_shadow"]["mode"], "shadow")
        self.assertFalse(item["inquiry_drive_shadow"]["enabled"])

    def test_trust_compacts_are_deterministic_settled_and_rehydratable(self):
        state = {"version": 12, "beliefs": {
            "source-integrity": {"id": "source-integrity", "statement": "Require corroborated source support.",
                                 "confidence": 0.98, "status": "active", "evidence": ["e-1", "e-2"]},
            "retracted": {"id": "retracted", "statement": "Old conclusion.", "confidence": 0,
                          "status": "retracted", "evidence": ["e-3", "e-4"]},
        }, "evidence": {}, "notebooks": {}, "commitments": {}}
        from wake.trust import build_trust_compacts_shadow
        from wake.retrieval import build_retrieval_shadow
        first = build_trust_compacts_shadow(state)
        second = build_trust_compacts_shadow(state)
        self.assertEqual(canonical(first), canonical(second))
        settled = next(item for item in first["compacts"] if item["status"] == "SETTLED")
        self.assertEqual(settled["scope"], "durable.belief:source-integrity")
        self.assertEqual(settled["provenance"]["evidence_roots"], ["e-1", "e-2"])
        self.assertEqual(first["metrics"]["settled_count"], 1)
        retrieval = build_retrieval_shadow(state, {"beliefs": []}, first)
        self.assertIn("trust_compact_challenged", retrieval["metrics"]["trigger_counts"])

    def test_inquiry_drive_shadow_is_deterministic_and_ranks_productive_continuation(self):
        state = {
            "charter": "Explore carefully.",
            "projects": {
                "thin": {"id": "thin", "title": "Thin project", "status": "active",
                         "question": "What is missing?", "next_step": "Find a source."},
                "supported": {"id": "supported", "title": "Supported project", "status": "active",
                              "question": "What changes the model?", "next_step": "Compare sources."},
                "parked": {"id": "parked", "title": "Parked", "status": "parked",
                           "question": "Ignored?", "next_step": "Do not score."},
            },
            "research": {
                "r1": {"project": "supported", "status": "collected"},
                "r2": {"project": "supported", "status": "collected"},
                "r3": {"project": "supported", "status": "queued"},
            },
            "notebooks": {
                "n1": {"project": "supported", "next_questions": "Test the disagreement.",
                       "limitations": "The sample is small.", "evidence": ["e1", "e2"]},
            },
        }
        shadow = self.engine.inquiry_drive_shadow(state)
        self.assertEqual(shadow["mode"], "shadow")
        self.assertTrue(shadow["enabled"])
        self.assertEqual([item["id"] for item in shadow["projects"]], ["supported", "thin"])
        self.assertGreater(shadow["projects"][0]["score"], shadow["projects"][1]["score"])
        self.assertEqual(shadow["projects"][0]["components"]["self_correction"], 1.0)
        self.assertIn("not preservation", shadow["principle"])

    def test_inquiry_drive_requires_operator_enablement_and_twenty_completed_scores(self):
        state = {"charter": "Explore carefully.", "projects": {}, "research": {}, "notebooks": {},
                 "invocations": {f"w-{index}": {"status": "accepted", "inquiry_drive_shadow": {}}
                                 for index in range(20)}}
        inactive = self.engine.inquiry_drive_shadow(state)
        self.assertFalse(inactive["activation"]["active"])
        self.assertEqual(inactive["activation"]["completed_scored_cycles"], 20)

        activated_engine = Engine(self.root / "activation", {**DEFAULTS, "inquiry_drive_enabled": True})
        try:
            active = activated_engine.inquiry_drive_shadow(state)
            self.assertTrue(active["activation"]["active"])
            state["invocations"].pop("w-19")
            self.assertFalse(activated_engine.inquiry_drive_shadow(state)["activation"]["active"])
        finally:
            activated_engine.store.close()

    def test_progressive_abstraction_is_documented_without_personhood_claims(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / "README.md").read_text()
        architecture = (root / "docs/architecture.md").read_text()
        experiment = (root / "docs/experiment.md").read_text()
        self.assertIn("progressive abstraction with recoverable provenance", readme.lower())
        self.assertIn("working abstractions keep evidence", readme.lower())
        self.assertIn("shadow working set", architecture.lower())
        self.assertIn("Exact receipts", architecture)
        self.assertIn("exact underneath, approximate on", architecture.lower())
        self.assertIn("not a test for consciousness, qualia, personhood", experiment)

    def test_report_display_polish_uses_shared_stylesheets(self):
        export(self.engine.store, self.root / "site")
        page = (self.root / "site/index.html").read_text()
        self.assertIn('href="style.css"', page)
        self.assertIn('href="theme.css"', page)
        self.assertTrue((self.root / "site" / "theme.css").is_file())
        self.assertIn('href="https://sudofx.github.io/wake/" aria-label="Reload WAKE✳︎ from the site root"', page)
        self.assertIn("className='wake-mark'", page)
        self.assertIn("text-shadow:0 0 7px", (self.root / "site" / "style.css").read_text())
        self.assertNotIn("a:hover{text-decoration:underline", page)
        self.assertIn("# **WAKE✳︎** — The journal", (self.root / "site/journal.md").read_text())

    def test_html_embedded_data_does_not_allow_script_injection(self):
        with self.engine.store.lock():
            self.engine.observe('</script><script>alert("xss")</script>', "human:test")
        export(self.engine.store, self.root/"site")
        page = (self.root/"site/index.html").read_text()
        self.assertNotIn('</script><script>alert', page)
        self.assertIn('\\u003c/script>', page)

    def test_live_provider_requires_explicit_free_tier_setting(self):
        with self.assertRaisesRegex(Rejected, "free_tier_confirmed"):
            Gemini(dict(DEFAULTS))

    def test_gemini_request_uses_single_bounded_json_call(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, maximum):
                return json.dumps({"candidates":[{"finishReason":"STOP", "content":{"parts":[{"text":'{"base_version":0,"title":"Hi","summary":"Review","actions":[]}'}]}}],"usageMetadata":{"totalTokenCount":123}}).encode()
        with patch.dict("os.environ", {"GEMINI_API_KEY":"test-key"}), patch("urllib.request.urlopen", return_value=Response()) as network:
            provider = Gemini({**DEFAULTS, "free_tier_confirmed":True})
            raw, metadata = provider.propose({"system":"rules", "context":{"version":0}})
            self.assertEqual(json.loads(raw)["base_version"], 0)
            self.assertEqual(metadata["usage"]["totalTokenCount"], 123)
            self.assertEqual(network.call_count, 1)
            request = network.call_args.args[0]
            self.assertNotIn("test-key", request.full_url)
            self.assertEqual(json.loads(request.data)["generationConfig"]["responseMimeType"], "application/json")


    def test_gemini_sends_one_request_for_each_transient_http_failure(self):
        from wake.providers import TransientProviderError
        for status in (500, 502, 503, 504):
            with self.subTest(status=status):
                busy = urllib.error.HTTPError("https://example.invalid", status, "busy", Message(), None)
                with patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"}), patch(
                        "urllib.request.urlopen", side_effect=[busy, AssertionError("unexpected retry")]) as network:
                    with self.assertRaises(TransientProviderError) as caught:
                        Gemini({**DEFAULTS, "free_tier_confirmed": True}).propose({"system": "rules", "context": {}})
                self.assertEqual(network.call_count, 1)
                self.assertEqual(caught.exception.details["provider_requests_sent"], 1)

    def test_gemini_does_not_retry_a_nontransient_http_error(self):
        denied = urllib.error.HTTPError("https://example.invalid", 403, "denied", Message(), None)
        with patch.dict("os.environ", {"GEMINI_API_KEY":"test-key"}), \
             patch("urllib.request.urlopen", side_effect=denied) as network, \
             patch("wake.providers.time.sleep") as wait:
            with self.assertRaisesRegex(Rejected, "Gemini HTTP 403"):
                Gemini({**DEFAULTS, "free_tier_confirmed":True}).propose({"system":"rules", "context":{}})
        self.assertEqual(network.call_count, 1)
        wait.assert_not_called()
        denied.close()

    def test_real_adapter_daily_quota_makes_one_request_then_preflight_blocks(self):
        body = {"error": {"details": [{"violations": [{
            "quotaId": "GenerateRequestsPerDayPerProjectPerModel-FreeTier"}]}]}}
        failure = urllib.error.HTTPError("https://example.invalid", 429, "limited", Message(),
                                         io.BytesIO(json.dumps(body).encode()))
        with patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"}), patch(
                "urllib.request.urlopen", side_effect=failure) as network:
            provider = Gemini({**DEFAULTS, "free_tier_confirmed": True})
            result = self.engine.run(provider)
            self.assertEqual(result["status"], "deferred")
            with self.assertRaisesRegex(Rejected, "daily quota exhausted"):
                self.engine.run(provider)
            self.assertEqual(network.call_count, 1)
        state = self.engine.store.load()
        self.assertEqual(state["version"], 0)
        self.assertEqual(state["invocations"][result["id"]]["provider_requests_sent"], 1)

    def test_successful_charged_wake_records_one_request(self):
        class Response:
            def __init__(self, req): self.req = req
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, maximum):
                context = json.loads(json.loads(self.req.data)["contents"][0]["parts"][0]["text"])
                raw, _ = Fixture().propose({"context": context})
                return json.dumps({"candidates": [{"finishReason": "STOP", "content": {"parts": [{"text": raw}]}}]}).encode()
        with patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"}), patch(
                "urllib.request.urlopen", side_effect=lambda req, **kw: Response(req)) as network:
            result = self.engine.run(Gemini({**DEFAULTS, "free_tier_confirmed": True}))
            self.assertEqual(network.call_count, 1)
        self.assertEqual(result["status"], "accepted")
        state = self.engine.store.load()
        self.assertEqual(state["invocations"][result["id"]]["provider_requests_sent"], 1)
        self.assertEqual(sum(i["charged"] for i in state["invocations"].values()), 1)

    def test_gemini_429_exposes_safe_structured_diagnostics(self):
        from wake.providers import ProviderRequestError, DailyQuotaExceeded
        headers = Message()
        headers["Retry-After"] = "37"
        body = {
            "error": {
                "code": 429,
                "status": "RESOURCE_EXHAUSTED",
                "message": "Quota exceeded for requests per minute.",
                "details": [
                    {"@type": "type.googleapis.com/google.rpc.QuotaFailure",
                     "violations": [{"quotaMetric": "generativelanguage.googleapis.com/generate_content_requests",
                                     "quotaId": "GenerateRequestsPerMinutePerProjectPerModel",
                                     "quotaValue": "10"}]},
                    {"@type": "type.googleapis.com/google.rpc.RetryInfo", "retryDelay": "37s"},
                ],
                "apiKey": "must-not-persist",
            }
        }
        limited = urllib.error.HTTPError(
            "https://example.invalid", 429, "limited", headers,
            io.BytesIO(json.dumps(body).encode()),
        )
        with patch.dict("os.environ", {"GEMINI_API_KEY":"test-key"}), \
             patch("urllib.request.urlopen", side_effect=limited) as network, \
             patch("wake.providers.time.monotonic", side_effect=[10.0, 11.25]):
            with self.assertRaises(ProviderRequestError) as caught:
                Gemini({**DEFAULTS, "free_tier_confirmed":True}).propose({"system":"rules", "context":{}})
        self.assertNotIsInstance(caught.exception, DailyQuotaExceeded)
        self.assertEqual(network.call_count, 1)
        detail = caught.exception.details
        self.assertEqual(detail["http_status"], 429)
        self.assertEqual(detail["retry_after"], "37")
        self.assertEqual(detail["elapsed_ms"], 1250)
        self.assertGreater(detail["request_payload_bytes"], 0)
        self.assertEqual(detail["provider_error"]["status"], "RESOURCE_EXHAUSTED")
        self.assertEqual(detail["provider_error"]["details"][0]["violations"][0]["quotaId"],
                         "GenerateRequestsPerMinutePerProjectPerModel")
        self.assertNotIn("apiKey", detail["provider_error"])

    def test_gemini_429_diagnostics_are_durable_on_failed_invocation(self):
        headers = Message()
        headers["Retry-After"] = "12"
        body = {"error": {"code": 429, "status": "RESOURCE_EXHAUSTED",
                          "message": "capacity or quota condition",
                          "details": [{"quotaMetric": "example.metric", "quotaId": "example-id"}]}}
        limited = urllib.error.HTTPError(
            "https://example.invalid", 429, "limited", headers,
            io.BytesIO(json.dumps(body).encode()),
        )
        with patch.dict("os.environ", {"GEMINI_API_KEY":"test-key"}), \
             patch("urllib.request.urlopen", side_effect=limited):
            provider = Gemini({**DEFAULTS, "free_tier_confirmed":True})
            result = self.engine.run(provider)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["provider_error"]["http_status"], 429)
        failed = [e for e in self.engine.store.events() if e["kind"] == "failed"][-1]
        self.assertEqual(failed["payload"]["provider_error"]["retry_after"], "12")
        self.assertEqual(failed["payload"]["provider_error"]["provider_error"]["status"],
                         "RESOURCE_EXHAUSTED")
        self.assertEqual(self.engine.store.load()["invocations"][result["id"]]["status"], "failed")


if __name__ == "__main__":
    unittest.main()
