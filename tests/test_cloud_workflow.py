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

    def run_cloud(self, provider, publish_only=False, scheduled=False):
        with patch.object(github_wake, "ROOT", self.project), \
             patch.object(github_wake, "config", return_value=dict(DEFAULTS)), \
             patch.object(github_wake, "Gemini", return_value=provider), \
             patch.object(github_wake, "collect", lambda engine: None), \
             patch.dict("os.environ", {"GITHUB_ACTIONS": "true"}):
            return github_wake.main(publish_only=publish_only, scheduled=scheduled)

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
        public = json.loads(self.git("--git-dir", self.remote, "show", "wake-state:site/state.json").stdout)
        self.assertEqual(len(public["invocations"]), 1)
        self.assertTrue(next(iter(public["invocations"].values()))["charged"])
        operation = json.loads(self.git("--git-dir", self.remote, "show", "wake-state:site/operation.json").stdout)
        self.assertEqual(operation["status"], "failed")
        self.assertIn("429", operation["reason"])
        self.assertTrue((self.project/"site/index.html").is_file())
        verify_history(self.project/"site/events.jsonl", (self.project/"site/head.txt").read_text())

    def test_attention_policy_keeps_expected_provider_pressure_green(self):
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "failed", "reason": "Gemini HTTP 429; wake attempt counted"}))
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "failed", "reason": "quota",
             "provider_error": {"http_status": 429}}))
        self.assertFalse(github_wake.requires_operator_attention(
            {"status": "deferred", "reason": "Gemini temporarily unavailable after 4 attempts; wake deferred"}))
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
        self.assertTrue(github_wake.requires_operator_attention(
            {"status": "rejected", "reason": "Invalid proposal"}))

    def test_transient_provider_outage_is_deferred_not_failed(self):
        from wake.providers import TransientProviderError
        class Busy(Fixture):
            charged = True
            calls = 0
            def propose(self, request):
                self.calls += 1
                raise TransientProviderError("Gemini temporarily unavailable after 4 attempts; wake deferred")
        provider = Busy()
        self.assertEqual(self.run_cloud(provider), 0)
        self.assertEqual(provider.calls, 1)
        public = json.loads(self.git("--git-dir", self.remote, "show", "wake-state:site/state.json").stdout)
        invocation = next(iter(public["invocations"].values()))
        self.assertEqual(invocation["status"], "deferred")
        self.assertIsNone(public["pending"])
        operation = json.loads(self.git("--git-dir", self.remote, "show", "wake-state:site/operation.json").stdout)
        self.assertEqual(operation["status"], "deferred")
        self.assertIn("temporarily unavailable", operation["reason"])
        verify_history(self.project/"site/events.jsonl", (self.project/"site/head.txt").read_text())

    def test_republishing_preserves_the_accepted_wake_without_calling_gemini(self):
        self.assertEqual(self.run_cloud(Fixture()), 0)
        before = json.loads((self.project/"site/state.json").read_text())
        with patch.object(github_wake, "Gemini", side_effect=AssertionError("No model initialization")), \
             patch.object(github_wake, "ROOT", self.project), \
             patch.object(github_wake, "config", return_value=dict(DEFAULTS)), \
             patch.object(github_wake, "collect", side_effect=AssertionError("No collection")), \
             patch.dict("os.environ", {"GITHUB_ACTIONS":"true"}):
            self.assertEqual(github_wake.main(publish_only=True), 0)
        after = json.loads((self.project/"site/state.json").read_text())
        self.assertEqual(before, after)
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
        public = json.loads(self.git("--git-dir", self.remote, "show", "wake-state:state.json").stdout)
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
        self.assertEqual(next_eligible, now + timedelta(minutes=55))

        state["invocations"]["wake"].update(
            status="deferred",
            reason="Gemini temporarily unavailable after 4 attempts; wake deferred",
            time=(now - timedelta(minutes=11)).isoformat())
        due, _ = github_wake.scheduled_wake_due(state, now=now)
        self.assertTrue(due)

        state["invocations"]["wake"]["time"] = (now - timedelta(minutes=5)).isoformat()
        due, next_eligible = github_wake.scheduled_wake_due(state, now=now)
        self.assertFalse(due)
        self.assertEqual(next_eligible, now + timedelta(minutes=5))

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

    def test_workflow_publishes_generated_reports_even_after_provider_failure(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root/".github/workflows/wake.yml").read_text()
        report = workflow.split("- name: Confirm report is ready", 1)[1].split("- name:", 1)[0]
        self.assertIn("steps.cycle.outputs.skipped != 'true'", report)
        self.assertNotIn("steps.cycle.outcome", report)
        self.assertIn("test -f site/index.html", report)
        self.assertIn("needs.wake.outputs.report_ready == 'true'", workflow)
        self.assertIn("if: always() && steps.cycle.outcome == 'failure'", workflow)
        self.assertIn("Fail only when operator attention is required", workflow)
        self.assertIn("path: site", workflow)
        self.assertIn("github-pages-${{ github.run_id }}-${{ github.run_attempt }}", workflow)
        self.assertIn("cron: '12,27,42,57 * * * *'", workflow)
        self.assertIn("python scripts/github_wake.py --scheduled", workflow)
        self.assertIn("artifact_name: ${{ needs.wake.outputs.artifact_name }}", workflow)
        self.assertNotIn("rotate-cover", workflow)
        self.assertNotIn("rotate_cover", workflow)
        self.assertNotIn("scripts/covers.py --cycle", workflow)
        self.assertNotIn("git add README.md", workflow)
        self.assertNotIn("git push --force", workflow)
        self.assertFalse((root/".github/workflows/static.yml").exists())
        self.assertFalse((root/".github/workflows/jekyll-gh-pages.yml").exists())

    def test_gemini_retries_transient_503s_before_succeeding(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, maximum):
                return json.dumps({"candidates":[{"finishReason":"STOP", "content":{"parts":[{"text":"{}"}]}}]}).encode()

        import urllib.error
        first = urllib.error.HTTPError("https://example", 503, "busy", None, None)
        second = urllib.error.HTTPError("https://example", 503, "busy", None, None)
        with patch.dict("os.environ", {"GEMINI_API_KEY":"test-key"}), \
             patch("urllib.request.urlopen", side_effect=[first, second, Response()]) as network, \
             patch("wake.providers.time.sleep") as sleep:
            Gemini({**DEFAULTS, "free_tier_confirmed":True}).propose({"system":"rules", "context":{}})
        self.assertEqual(network.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(15), call(30)])

    def test_gemini_defers_after_transient_retries_are_exhausted(self):
        from wake.providers import TransientProviderError
        import urllib.error
        failures = [urllib.error.HTTPError("https://example", 503, "busy", None, None) for _ in range(4)]
        with patch.dict("os.environ", {"GEMINI_API_KEY":"test-key"}), \
             patch("urllib.request.urlopen", side_effect=failures), \
             patch("wake.providers.time.sleep"):
            with self.assertRaisesRegex(TransientProviderError, "temporarily unavailable"):
                Gemini({**DEFAULTS, "free_tier_confirmed":True}).propose({"system":"rules", "context":{}})

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
