# =============================================================================
# TESTING INTENT — cloud workflow
#
# This file is executable documentation. Passing cases define behavior WAKE✳︎
# promises to preserve; rejection/failure cases define boundaries that future
# refactors must not weaken merely to make CI green. Read assertions as part of
# the architectural contract, not just as coverage machinery.
# =============================================================================

# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for cloud workflow.
# Tests in WAKE✳︎ are part of the explanation of the system: successful cases show what authority is allowed,
# while rejection/failure cases show the boundaries that must remain intact during refactors.
# Prefer assertions that make the invariant obvious to a human or AI maintainer reading this file later.

"""A failed inference is publishable; a failed state checkpoint is not."""

from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import call, patch

from scripts import github_wake
from wake.audit import verify_history
from wake.engine import DEFAULTS
from wake.governance import Rejected
from wake.providers import Fixture, Gemini


class CloudWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project, self.remote = self.root/"project", self.root/"remote.git"
        self.git("init", self.project)
        self.git("init", "--bare", self.remote)
        (self.project/"README.md").write_text("Source files must never be the Pages artifact.")
        self.git("-C", self.project, "add", "README.md")
        self.git("-C", self.project, "-c", "user.name=test", "-c", "user.email=test@example.com", "commit", "-m", "Source")
        self.git("-C", self.project, "remote", "add", "origin", self.remote)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.run(["git", *map(str,args)], check=True, capture_output=True, text=True)

    def live(self):
        return json.loads(
            self.git("--git-dir", self.remote, "show", "wake-live:live.json").stdout)

    def run_cloud(self, provider, publish_only=False, scheduled=False, reset=False):
        with patch.object(github_wake, "ROOT", self.project), \
             patch.object(github_wake, "config", return_value=dict(DEFAULTS)), \
             patch.object(github_wake, "Gemini", return_value=provider), \
             patch.object(github_wake, "collect", lambda engine: None), \
             patch.dict("os.environ", {"GITHUB_ACTIONS": "true"}):
            return github_wake.main(publish_only=publish_only, scheduled=scheduled, reset=reset)

    def test_cloud_reset_returns_to_zero_without_calling_provider(self):
        self.assertEqual(self.run_cloud(Fixture()), 0)
        before = self.live()["state"]
        self.assertGreater(before["version"], 0)

        stale = self.project / "site" / "blog" / "stale.html"
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.write_text("old artifact")

        class NeverCall(Fixture):
            def propose(self, request):
                raise AssertionError("Reset must not call a model")

        self.assertEqual(self.run_cloud(NeverCall(), reset=True), 0)

        state = self.live()["state"]
        self.assertEqual(state["version"], 0)
        self.assertEqual(state["journal"], [])
        self.assertEqual(state["posts"], {})
        self.assertEqual(state["invocations"], {})
        self.assertTrue(stale.exists())

        operation = self.live()["operation"]
        self.assertTrue(operation["reset"])
        self.assertEqual(operation["status"], "not_started")

    def test_access_limit_failure_is_counted_exported_visible_but_not_action_failure(self):
        class Failure(Fixture):
            charged = True
            calls = 0
            def propose(self, request):
                self.calls += 1
                raise Rejected("Gemini HTTP 429; wake attempt counted")
        provider = Failure()
        self.assertEqual(self.run_cloud(provider), 0)
        self.assertEqual(provider.calls, 1)
        public = self.live()["state"]
        self.assertEqual(len(public["invocations"]), 1)
        self.assertTrue(next(iter(public["invocations"].values()))["charged"])
        operation = self.live()["operation"]
        self.assertEqual(operation["status"], "failed")
        self.assertIn("429", operation["reason"])
        self.assertFalse((self.project/"site/index.html").exists())

    def test_attention_policy_keeps_expected_provider_pressure_green(self):
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "failed", "reason": "Gemini HTTP 429; wake attempt counted"}))
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "failed", "reason": "quota",
             "provider_error": {"http_status": 429}}))
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "deferred", "reason": "Gemini temporarily unavailable; wake deferred"}))
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "paused", "reason": "Daily call ceiling reached; no request sent"}))
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "paused", "reason": "Gemini free-tier daily quota exhausted for this model until Pacific midnight; no request sent"}))

    def test_attention_policy_still_fails_auth_and_unexpected_runtime_conditions(self):
        self.assertTrue(github_wake.requires_operator_attention(
            {"status": "failed", "reason": "Gemini HTTP 401; wake attempt counted",
             "provider_error": {"http_status": 401}}))
        self.assertTrue(github_wake.requires_operator_attention(
            {"status": "paused", "reason": "GEMINI_API_KEY is missing"}))
        self.assertTrue(github_wake.requires_operator_attention(
            {"status": "failed", "reason": "Provider failed (ValueError); no automatic retry"}))
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "rejected", "reason": "Invalid proposal"}))

    def test_transient_provider_outage_is_deferred_not_failed(self):
        from wake.providers import TransientProviderError
        class Busy(Fixture):
            charged = True
            calls = 0
            def propose(self, request):
                self.calls += 1
                raise TransientProviderError("Gemini temporarily unavailable; wake deferred")
        provider = Busy()
        self.assertEqual(self.run_cloud(provider), 0)
        self.assertEqual(provider.calls, 1)
        public = self.live()["state"]
        invocation = next(iter(public["invocations"].values()))
        self.assertEqual(invocation["status"], "deferred")
        self.assertIsNone(public["pending"])
        operation = self.live()["operation"]
        self.assertEqual(operation["status"], "deferred")
        self.assertIn("temporarily unavailable", operation["reason"])

    def test_republishing_preserves_the_accepted_wake_without_calling_gemini(self):
        self.assertEqual(self.run_cloud(Fixture()), 0)
        before = self.live()
        with patch.object(github_wake, "Gemini", side_effect=AssertionError("No model initialization")), \
             patch.object(github_wake, "ROOT", self.project), \
             patch.object(github_wake, "config", return_value=dict(DEFAULTS)), \
             patch.object(github_wake, "collect", side_effect=AssertionError("No collection")), \
             patch.dict("os.environ", {"GITHUB_ACTIONS":"true"}):
            self.assertEqual(github_wake.main(publish_only=True), 0)
        after = json.loads((self.project/"site/state.json").read_text())
        self.assertEqual(before["state"]["version"], after["version"])
        self.assertEqual(before["head"], (self.project/"site/head.txt").read_text().strip())
        result = json.loads((self.project/"site/operation.json").read_text())
        self.assertEqual(result["status"], "accepted")
        self.assertTrue(result["publication_only"])

    def test_backup_schedule_skips_a_recent_wake_without_calling_provider(self):
        class ChargedFixture(Fixture):
            charged = True
        self.assertEqual(self.run_cloud(ChargedFixture()), 0)
        class NeverCall(Fixture):
            charged = True
            def propose(self, request): raise AssertionError("Recent scheduled wake must suppress the model call")
        provider = NeverCall()
        self.assertEqual(self.run_cloud(provider, scheduled=True), 0)
        public = self.live()["state"]
        self.assertEqual(len(public["invocations"]), 1)

    def test_scheduled_due_uses_normal_guard_but_retries_deferred_outages_soon(self):
        now = datetime.now(timezone.utc)
        state = {"invocations": {"wake": {
            "charged": True, "status": "accepted",
            "time": (now - timedelta(minutes=56)).isoformat(), "reason": ""
        }}}
        due, _ = github_wake.scheduled_wake_due(state, now=now)
        self.assertTrue(due)

        state["invocations"]["wake"].update(status="accepted", time=now.isoformat(), reason="")
        due, next_eligible = github_wake.scheduled_wake_due(state, now=now)
        self.assertFalse(due)
        self.assertEqual(next_eligible, now + timedelta(minutes=5))

        state["invocations"]["wake"].update(
            status="deferred",
            reason="Gemini temporarily unavailable; wake deferred",
            time=(now - timedelta(minutes=11)).isoformat())
        due, _ = github_wake.scheduled_wake_due(state, now=now)
        self.assertTrue(due)

        state["invocations"]["wake"]["time"] = (now - timedelta(minutes=4)).isoformat()
        due, next_eligible = github_wake.scheduled_wake_due(state, now=now)
        self.assertFalse(due)
        self.assertEqual(next_eligible, now + timedelta(minutes=1))

    def test_scheduled_daily_quota_waits_until_pacific_midnight(self):
        # 2026-09-14 06:50 UTC is 2026-09-13 23:50 Pacific.
        item = {
            "charged": True,
            "provider": "gemini",
            "model": "gemini-3.8-flash",
            "status": "failed",
            "quota_day": "2026-09-13",
            "time": datetime(2026, 9, 14, 6, 50, tzinfo=timezone.utc).isoformat(),
            "reason": "Gemini HTTP 429; wake attempt counted",
            "provider_error": {
                "http_status": 429,
                "provider_error": {
                    "details": [{"violations": [{
                        "quotaId": "GenerateRequestsPerDayPerProjectPerModel-FreeTier",
                        "quotaValue": "20",
                    }]}],
                },
            },
        }
        state = {"invocations": {"wake": item}}
        before = datetime(2026, 9, 14, 6, 55, tzinfo=timezone.utc)
        due, next_eligible = github_wake.scheduled_wake_due(state, now=before)
        self.assertFalse(due)
        self.assertEqual(next_eligible, datetime(2026, 9, 14, 7, 0, tzinfo=timezone.utc))

        # Once Pacific midnight passes, the quota guard releases immediately rather
        # than imposing the ordinary 55-minute wake spacing.
        after = datetime(2026, 9, 14, 7, 1, tzinfo=timezone.utc)
        due, next_eligible = github_wake.scheduled_wake_due(state, now=after)
        self.assertTrue(due)
        self.assertEqual(next_eligible, datetime(2026, 9, 14, 7, 0, tzinfo=timezone.utc))

    def test_failed_checkpoint_never_exports_or_calls_provider(self):
        class NeverCall(Fixture):
            def propose(self, request): raise AssertionError("Provider must not be called")
        with patch.object(github_wake.StateBranch, "checkpoint", side_effect=OSError("Push failed")):
            with self.assertRaises(OSError): self.run_cloud(NeverCall())
        self.assertFalse((self.project/"site/index.html").exists())

    def test_runtime_isolation_contract(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root/".github/workflows/wake.yml").read_text()
        pages = (root/".github/workflows/pages.yml").read_text()
        runner = (root/".github/workflows/wake-runner.yml").read_text()
        promotion = (root/".github/workflows/promote-runtime.yml").read_text()
        worker = (root/"control-worker/worker.mjs").read_text()

        # Research execution is isolated from development and Pages.
        self.assertIn("github.ref_name == 'wake-runtime'", workflow)
        self.assertIn("REQUESTED_RUNTIME_REF", workflow)
        self.assertIn('REQUESTED_RUNTIME_REF" != "$GITHUB_SHA', workflow)
        self.assertIn("group: wake-authority", workflow)
        self.assertIn("--ref wake-runtime", workflow)
        self.assertNotIn("deploy-pages", workflow)
        self.assertNotIn("upload-pages-artifact", workflow)
        self.assertIn("group: wake-pages", pages)
        self.assertNotIn("GEMINI_API_KEY", pages)

        # Bootstrap and operator actions never adopt master as executable runtime.
        self.assertIn("never mutates wake-runtime", runner)
        self.assertNotIn("git push --force", runner)
        self.assertNotIn('runtime_ref: "master"', worker)
        self.assertIn("ref: RUNNER_REF", worker)

        # Operator state is derived from two GitHub truths: the runner workflow
        # is the durable continuation latch, and only non-completed
        # wake-runtime runs count as execution. Stop closes the latch before
        # cancellation, reset refuses active work, and Start reopens the latch.
        self.assertIn('runnerWorkflow.state === "active"', worker)
        self.assertIn('run.head_branch === RUNNER_REF', worker)
        self.assertIn('run.status !== "completed"', worker)
        self.assertIn('"running" : "draining"', worker)
        self.assertIn('"stopped" : "disabled"', worker)
        self.assertIn('/enable', worker)
        self.assertIn('/disable', worker)
        self.assertLess(worker.index("await disableRunner(env, session, githubFetch);"),
                        worker.index("const cancelledRuns = await cancelRuns(env, session, githubFetch);"))
        self.assertIn("Stop WAKE✳︎ and wait for active runtime work to finish before resetting", worker)
        self.assertIn("RUNNER_WORKFLOW}/dispatches", worker)

        # Promotion is the only explicit runtime adoption boundary and refuses
        # to move the runtime branch while a real runtime cycle is active.
        self.assertIn("promote runtime", promotion.lower())
        self.assertIn('branch=wake-runtime', promotion)
        self.assertIn('.status!="completed"', promotion)
        self.assertIn("python -m unittest discover", promotion)
        self.assertIn("git/refs/heads/wake-runtime", promotion)

    def test_wordmark_navigation_is_deployment_portable(self):
        root = Path(__file__).resolve().parents[1]
        for relative in ("wake/assets/index.html", "wake/assets/map.html", "wake/assets/map3d.html"):
            page = (root/relative).read_text()
            self.assertNotIn('href="https://sudofx.github.io/wake/"', page)
            self.assertIn('class="wordmark" href="index.html"', page)
        report = (root/"wake/report.py").read_text()
        self.assertNotIn('href=\\\"https://sudofx.github.io/wake/\\\"', report)
        self.assertIn('class=\\\"wordmark\\\" href=\\\"index.html\\\"', report)
        self.assertIn('class=\\\"wordmark\\\" href=\\\"../index.html\\\"', report)

    def test_transient_diagnostics_survive_cloud_export_and_redact_credentials(self):
        import io
        import urllib.error
        failures = [urllib.error.HTTPError("https://example", 503, "busy", {"Retry-After": "30"},
                    io.BytesIO(json.dumps({"error": {"code": 503, "status": "UNAVAILABLE",
                        "message": "overloaded test-secret", "api_key": "test-secret"}}).encode())) for _ in range(4)]
        with patch.dict("os.environ", {"GEMINI_API_KEY": "test-secret"}), \
             patch("urllib.request.urlopen", side_effect=failures) as network:
            provider = Gemini({**DEFAULTS, "free_tier_confirmed": True})
            self.assertEqual(self.run_cloud(provider), 0)
            self.assertEqual(network.call_count, 1)
        state = self.live()["state"]
        item = next(iter(state["invocations"].values()))
        error = item["provider_error"]
        self.assertEqual(error["http_status"], 503)
        self.assertEqual(error["category"], "server")
        self.assertEqual(error["retry_after"], "30")
        self.assertEqual(error["provider_requests_sent"], 1)
        self.assertEqual(item["provider_requests_sent"], 1)
        self.assertEqual(state["version"], 0)
        self.assertEqual(error["provider_error"]["status"], "UNAVAILABLE")
        self.assertNotIn("test-secret", json.dumps(self.live()))
        self.assertNotIn("api_key", error["provider_error"])
        operation = self.live()["operation"]
        self.assertEqual(operation["wake_status"]["latest_attempt"]["status"], "deferred")
        self.assertIsNone(operation["wake_status"]["last_accepted"])
        self.assertIsNotNone(operation["wake_status"]["next_eligible"])

    def test_timeout_and_connection_diagnostics_are_distinct(self):
        import urllib.error
        from wake.providers import TransientProviderError
        for failure, category in ((TimeoutError("private text"), "timeout"),
                                  (urllib.error.URLError(ConnectionRefusedError(61, "private text")), "connection")):
            with self.subTest(category=category), patch.dict("os.environ", {"GEMINI_API_KEY": "test-key"}), \
                 patch("urllib.request.urlopen", side_effect=failure) as network:
                with self.assertRaises(TransientProviderError) as caught:
                    Gemini({**DEFAULTS, "free_tier_confirmed": True}).propose({"system": "rules", "context": {}})
                self.assertEqual(caught.exception.details["category"], category)
                self.assertEqual(caught.exception.details["provider_requests_sent"], 1)
                self.assertEqual(network.call_count, 1)
                self.assertNotIn("private text", json.dumps(caught.exception.details))

    def test_provider_schema_prevents_the_observed_mixed_project_shape(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, maximum):
                return json.dumps({"candidates":[{"finishReason":"STOP", "content":{"parts":[{"text":"{}"}]}}]}).encode()
        with patch.dict("os.environ", {"GEMINI_API_KEY":"test-key"}), patch("urllib.request.urlopen", return_value=Response()) as network:
            Gemini({**DEFAULTS, "free_tier_confirmed":True}).propose({"system":"rules", "context":{}})
        body = json.loads(network.call_args.args[0].data)
        self.assertNotIn("responseJsonSchema", body["generationConfig"])
        schema = json.loads(body["systemInstruction"]["parts"][0]["text"].split("Response contract (JSON Schema):\n")[1])
        variants = {s["properties"]["type"]["enum"][0]:s for s in schema["properties"]["actions"]["items"]["anyOf"]}
        project = variants["project"]
        self.assertEqual(set(project["properties"]), set("type id title question domain status next_step reason".split()))
        self.assertIn("status", project["required"])
        self.assertFalse(project["additionalProperties"])
        self.assertIn("domain", variants["research"]["required"])
        self.assertNotIn("findings", variants["research"]["properties"])


if __name__ == "__main__": unittest.main()
