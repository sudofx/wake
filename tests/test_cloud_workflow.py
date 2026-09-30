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

import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from scripts import github_wake
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

    def run_cloud(self, provider, reset=False):
        with patch.object(github_wake, "ROOT", self.project), \
             patch.object(github_wake, "config", return_value=dict(DEFAULTS)), \
             patch.object(github_wake, "Gemini", return_value=provider), \
             patch.object(github_wake, "collect", lambda engine: None), \
             patch.dict("os.environ", {"GITHUB_ACTIONS": "true"}):
            return github_wake.main(reset=reset)

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
        start = (root/".github/workflows/operator-start.yml").read_text()
        stop = (root/".github/workflows/operator-stop.yml").read_text()
        reset = (root/".github/workflows/operator-reset.yml").read_text()

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
        self.assertNotIn("WAKE_CONTROL_URL", pages)
        self.assertNotIn("WAKE_CONTROL_URL", workflow)

        # GitHub Actions is the complete operator boundary.
        self.assertIn("name: WAKE✳︎ — Start research", start)
        self.assertIn("wake-runner.yml/enable", start)
        self.assertIn("gh workflow run wake.yml", start)
        self.assertIn("name: WAKE✳︎ — Stop research", stop)
        self.assertIn("wake-runner.yml/disable", stop)
        self.assertIn("/cancel", stop)
        self.assertIn("name: WAKE✳︎ — Reset WAKE to 0", reset)
        self.assertIn('confirm_reset', reset)
        self.assertIn("wake-runner.yml/disable", reset)
        self.assertIn('reset=true', reset)
        self.assertIn('name: "WAKE✳︎ — Internal only: keep-running switch"', runner)
        self.assertNotIn("gh workflow run wake.yml", runner)
        self.assertIn("workflow_call:", runner)
        self.assertNotIn("workflow_dispatch:", runner)
        self.assertNotIn("scheduled:", workflow)
        self.assertNotIn("publish_after:", workflow)
        self.assertNotIn("publish_only", github_wake.__dict__)
        runtime_source = (root/"scripts/github_wake.py").read_text()
        self.assertNotIn("--publish-only", runtime_source)
        self.assertNotIn("--scheduled", runtime_source)
        self.assertNotIn("--record-only", runtime_source)

        # Promotion remains the only explicit runtime adoption boundary.
        self.assertIn("WAKE✳︎ — Make new code live", promotion)
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
