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
from wake.kernel.record import Record


class CloudWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project, self.remote = self.root/"project", self.root/"remote.git"
        self.git("init", self.project)
        self.git("init", "--bare", self.remote)
        # Cloud operations also invoke Git directly. Disable maintenance in
        # both disposable repositories so detached writers cannot race cleanup.
        for repository in (self.project, self.remote):
            self.git("-C", repository, "config", "gc.auto", "0")
            self.git("-C", repository, "config", "maintenance.auto", "false")
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

    def run_cloud(self, provider, reset=False, enable_continuity_matrix=False):
        with patch.object(github_wake, "ROOT", self.project), \
             patch.object(github_wake, "config", return_value=dict(DEFAULTS)), \
             patch.object(github_wake, "Gemini", return_value=provider), \
             patch.object(github_wake, "collect", lambda engine: None), \
             patch.dict("os.environ", {"GITHUB_ACTIONS": "true"}):
            return github_wake.main(
                reset=reset,
                enable_continuity_matrix=enable_continuity_matrix,
            )

    def test_checkpoint_maintenance_compacts_verified_wake_authority(self):
        """Physical SQLite maintenance must preserve replay while reclaiming checkpoint slack."""
        database = self.root / "maintenance" / "wake.sqlite"
        database.parent.mkdir(parents=True)
        record = Record(database)
        before = record.full_replay()

        after_bytes = github_wake.compact_authority_for_checkpoint(
            database,
            compact_at=0,
        )

        self.assertGreater(after_bytes, 0)
        self.assertEqual(Record(database).full_replay(), before)

    def test_checkpoint_transport_fails_closed_above_hard_limit(self):
        """A compressed authority blob that cannot fit GitHub must stop before push."""
        database = self.root / "oversize" / "wake.sqlite"
        archive = self.root / "oversize" / github_wake.STATE_ARCHIVE_NAME
        database.parent.mkdir(parents=True)
        Record(database)
        github_wake.compact_authority_for_checkpoint(database, compact_at=0)
        with self.assertRaisesRegex(Rejected, "100 MiB"):
            github_wake.package_authority_for_git(
                database,
                archive,
                hard_limit=1,
            )

    def test_cloud_cycle_persists_wake_as_authoritative_state(self):
        """The GitHub execution path must checkpoint wake, not a competing WAKE engine store."""
        self.assertEqual(self.run_cloud(Fixture("cloud-wake-authority")), 0)
        tree = self.git(
            "--git-dir", self.remote, "ls-tree", "-r", "--name-only", "wake-state"
        ).stdout.splitlines()
        self.assertIn("data/wake.sqlite.gz", tree)
        self.assertNotIn("data/wake.sqlite", tree)
        self.assertNotIn("data/wake.sqlite3", tree)
        live = self.live()
        self.assertEqual(live["source"]["authority"], "wake SQLite")
        self.assertEqual(live["source"]["database"], "wake.sqlite")
        # A fresh checkout restores the transport package into runtime SQLite.
        checkout = self.root / "restored-state"
        branch = github_wake.StateBranch(self.project, checkout)
        branch.open()
        try:
            self.assertTrue((checkout / "data/wake.sqlite").exists())
            self.assertTrue((checkout / "data/wake.sqlite.gz").exists())
            Record(checkout / "data/wake.sqlite").full_replay()
        finally:
            self.git("-C", self.project, "worktree", "remove", "--force", checkout)

    def test_continuity_enablement_is_governed_provider_free_and_durable(self):
        """Operator opt-in must use the authority lane without spending a provider request."""
        self.assertEqual(self.run_cloud(Fixture("matrix-seed")), 0)

        class NeverCall(Fixture):
            def propose(self, request):
                raise AssertionError("Continuity enablement must not call a provider")

        self.assertEqual(
            self.run_cloud(NeverCall("matrix-never"), enable_continuity_matrix=True),
            0,
        )
        live = self.live()
        self.assertEqual(live["operation"]["reason"], "Continuity campaign enabled")
        self.assertTrue(live["operation"]["continuity_matrix_enabled"])
        matrix = live["research"]["matrix"]
        self.assertTrue(matrix["reported"])
        self.assertTrue(matrix["enabled"])
        self.assertEqual(matrix["completed"], 0)
        self.assertEqual(len(matrix["cells"]), 343)

        checkout = self.root / "matrix-restored-state"
        branch = github_wake.StateBranch(self.project, checkout)
        branch.open()
        try:
            store = github_wake.open_authoritative_store(checkout / "data")
            try:
                progress = store.continuity_matrix_progress()
                self.assertEqual(progress["matrix"], "continuity@1")
                self.assertEqual(progress["completed_count"], 0)
                self.assertEqual(progress["cell_count"], 343)
            finally:
                store.close()
        finally:
            self.git("-C", self.project, "worktree", "remove", "--force", checkout)

    def test_state_checkpoints_replace_git_transport_history(self):
        """SQLite keeps the ledger; Git exposes only the latest parentless package."""
        self.assertEqual(self.run_cloud(Fixture("first-checkpoint")), 0)
        first = self.git(
            "--git-dir", self.remote, "rev-parse", "wake-state"
        ).stdout.strip()
        self.assertEqual(
            self.git("--git-dir", self.remote, "rev-list", "--count", "wake-state").stdout.strip(),
            "1",
        )

        self.assertEqual(self.run_cloud(Fixture("second-checkpoint")), 0)
        second = self.git(
            "--git-dir", self.remote, "rev-parse", "wake-state"
        ).stdout.strip()
        self.assertNotEqual(first, second)
        self.assertEqual(
            self.git("--git-dir", self.remote, "rev-list", "--count", "wake-state").stdout.strip(),
            "1",
        )
        self.assertEqual(
            self.git("--git-dir", self.remote, "show", "-s", "--format=%P", second).stdout.strip(),
            "",
        )

        checkout = self.root / "latest-state"
        branch = github_wake.StateBranch(self.project, checkout)
        branch.open()
        try:
            record = Record(checkout / "data/wake.sqlite")
            revision, state = record.full_replay()
            events = record.history()
            self.assertGreater(revision, 0)
            self.assertIsInstance(state, dict)
            self.assertGreater(len(events), 0)
        finally:
            self.git("-C", self.project, "worktree", "remove", "--force", checkout)

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
        archive_branch = operation["archive_branch"]
        self.assertTrue(archive_branch.startswith("wake-archive-"))
        archived_refs = self.git("--git-dir", self.remote, "for-each-ref",
                                 "refs/heads/wake-archive-*", "--format=%(refname:short)").stdout.splitlines()
        self.assertIn(archive_branch, archived_refs)

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
        restart = (root/".github/workflows/operator-restart.yml").read_text()
        continuity = (root/".github/workflows/operator-enable-continuity.yml").read_text()

        # Research execution is isolated from development and Pages.
        self.assertIn("github.ref_name == 'wake-runtime'", workflow)
        self.assertIn("REQUESTED_RUNTIME_REF", workflow)
        self.assertIn('REQUESTED_RUNTIME_REF" != "$GITHUB_SHA', workflow)
        self.assertIn("group: wake-authority", workflow)
        self.assertIn("live_projection_updated: ${{ steps.cycle.outputs.live_projection_updated }}", workflow)
        self.assertIn("public live projection did not update", workflow)
        self.assertIn("--ref wake-runtime", workflow)
        self.assertNotIn("deploy-pages", workflow)
        self.assertNotIn("upload-pages-artifact", workflow)
        self.assertIn("group: wake-pages", pages)
        self.assertNotIn("GEMINI_API_KEY", pages)
        self.assertNotIn("WAKE_CONTROL_URL", pages)
        self.assertNotIn("WAKE_CONTROL_URL", workflow)

        # GitHub Actions is the complete operator boundary.
        self.assertIn("name: WAKE✳︎ - Start", start)
        self.assertIn("wake-runner.yml/enable", start)
        self.assertIn("gh workflow run wake.yml", start)
        self.assertIn("git/ref/heads/wake-runtime", start)
        self.assertIn('.head_sha==\\\"$runtime_sha\\\"', start)
        self.assertIn("name: WAKE✳︎ - Stop", stop)
        self.assertIn("wake-runner.yml/disable", stop)
        self.assertIn("/cancel", stop)
        self.assertIn("Wait until research is fully stopped", stop)
        self.assertIn("did not fully stop even after force-cancel fallback", stop)
        self.assertIn("stale zero-job ghosts were ignored", stop)
        self.assertIn("real work was force-cancelled", stop)
        self.assertIn("git/ref/heads/wake-runtime", stop)
        self.assertIn('.head_sha==\\\"$runtime_sha\\\"', stop)
        self.assertIn("git/ref/heads/wake-runtime", promotion)
        self.assertIn('.head_sha==\\\"$runtime_sha\\\"', promotion)
        self.assertIn("/force-cancel", stop)
        self.assertIn("name: WAKE✳︎ - Restart", restart)
        self.assertIn("git/ref/heads/wake-runtime", restart)
        self.assertIn('.head_sha==\\\"$runtime_sha\\\"', restart)
        self.assertIn("/force-cancel", restart)
        self.assertIn("name: WAKE✳︎ - Enable continuity campaign", continuity)
        self.assertIn("group: wake-operator-control", continuity)
        self.assertIn("wake-runner.yml/disable", continuity)
        self.assertIn("enable_continuity_matrix=true", continuity)
        self.assertIn("python -m unittest discover", continuity)
        self.assertIn("git/refs/heads/wake-runtime", continuity)
        self.assertIn("enable_continuity_matrix:", workflow)
        self.assertIn("--enable-continuity-matrix", workflow)
        # GitHub can retain queued workflow ghosts that never acquired a job.
        # Operator controls must ignore only old zero-job ghosts while still
        # treating fresh queued work and every run with jobs as active.
        for control in (start, stop, restart, promotion, continuity):
            self.assertIn("job_count", control)
            self.assertIn("age_seconds", control)
            self.assertIn('"queued"', control)
            self.assertIn("-ge 120", control)
            self.assertIn("Ignoring stale queued zero-job WAKE run", control)
        self.assertNotIn("push:\n    branches: [master]", restart)
        self.assertIn("group: wake-operator-control", promotion)
        self.assertIn("wake-runner.yml", promotion)
        self.assertIn("continuation latch is open", promotion.lower())
        self.assertIn("name: WAKE✳︎ - [RESET]", reset)
        self.assertNotIn('confirm_reset', reset)
        self.assertIn("wake-runner.yml/disable", reset)
        self.assertIn('reset=true', reset)
        self.assertIn('name: "WAKE✳︎ — Internal only: keep-running switch"', runner)
        self.assertNotIn("gh workflow run wake.yml", runner)
        self.assertIn("workflow_call:", runner)
        self.assertNotIn("workflow_dispatch:", runner)
        self.assertNotIn("2>/dev/null || true", workflow)
        self.assertNotIn("wake-runner.yml/disable\" >/dev/null || true", reset)
        self.assertNotIn("scheduled:", workflow)
        self.assertNotIn("publish_after:", workflow)
        self.assertNotIn("publish_only", github_wake.__dict__)
        runtime_source = (root/"scripts/github_wake.py").read_text()
        self.assertNotIn("--publish-only", runtime_source)
        self.assertNotIn("--scheduled", runtime_source)
        self.assertNotIn("--record-only", runtime_source)

        # Promotion remains the only explicit runtime adoption boundary.
        self.assertIn("WAKE✳︎ - promote", promotion)
        self.assertIn('branch=wake-runtime', promotion)
        self.assertIn('.status!=\\\"completed\\\"', promotion)
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
        self.assertIn('class="wordmark" href="index.html"', report)
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
