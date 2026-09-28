#!/usr/bin/env python3
# WAKE✳︎ MAINTAINER NOTE
#
# GitHub Actions entry point. It loads cloud state, runs one bounded wake, publishes artifacts, and reports status while preserving the durable branch as continuity.
#
# Explain intent, invariants, failure behavior, and architectural boundaries in comments.
# Future humans and models should be able to tell deliberate constraints from incidental implementation.

"""One cloud wake. Persist the call reservation remotely before sending to Gemini."""

import argparse
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
GIT_OPERATION_TIMEOUT_SECONDS = 20
sys.path.insert(0, str(ROOT))
from wake.engine import Engine, config
from wake.governance import Rejected
from wake.providers import Gemini, is_free_tier_daily_quota
from wake.research import collect
from wake.report import export, atomic_write
from wake.live import build_live_projection


from wake.scheduling import (
    SCHEDULED_WAKE_INTERVAL, SCHEDULED_TRANSIENT_RETRY_INTERVAL,
    daily_quota_next_eligible, transient_provider_deferred, scheduled_wake_due, wake_status,
)


def set_step_output(name, value):
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with Path(output).open("a") as stream:
            stream.write(f"{name}={value}\n")


def requires_operator_attention(result):
    """Separate research/provider outcomes from infrastructure failures worth paging a human."""
    status = result.get("status")
    # Research/governance rejections are expected quality-control outcomes:
    # preserve and publish them, but do not fail the GitHub workflow or page the operator.
    if status in ("accepted", "deferred", "waiting", "not_started", "rejected"):
        return False

    provider_error = result.get("provider_error", {})
    if provider_error.get("http_status") == 429:
        return False

    reason = str(result.get("reason", ""))
    quiet_prefixes = (
        "Gemini HTTP 429",
        "Gemini free-tier daily quota exhausted",
        "Daily call ceiling reached",
    )
    if reason.startswith(quiet_prefixes):
        return False

    return True


class StateBranch:
    def __init__(self, repository, checkout, branch="wake-state"):
        self.repository, self.checkout, self.branch = Path(repository), Path(checkout), branch

    def git(self, *args, cwd=None, check=True):
        return subprocess.run(["git", *args], cwd=cwd or self.repository, capture_output=True, text=True, check=check, timeout=GIT_OPERATION_TIMEOUT_SECONDS)

    def open(self):
        result = self.git("ls-remote", "--exit-code", "--heads", "origin", f"refs/heads/{self.branch}", check=False)
        if result.returncode == 0:
            self.git("fetch", "--no-tags", "origin", f"refs/heads/{self.branch}")
            self.git("worktree", "add", "--detach", str(self.checkout), "FETCH_HEAD")
            if not (self.checkout / "data/wake.sqlite3").exists():
                raise Rejected("Existing wake-state branch is missing its database; refusing to reset it")
        elif result.returncode == 2:
            self.git("worktree", "add", "--detach", str(self.checkout), "HEAD")
            self.git("switch", "--orphan", self.branch, cwd=self.checkout)
        else:
            raise Rejected("Cannot read remote state; no model call will be made")

    def checkpoint(self):
        # wake-state is authority, not a publication cache. Retire legacy
        # JSON/HTML projections from the current tree; SQLite is the sole
        # accumulating operational record.
        self.git("rm", "-r", "--ignore-unmatch", "events.jsonl", "state.json", "head.txt",
                 "operation.json", "site", cwd=self.checkout, check=False)
        self.git("add", "--force", "data/wake.sqlite3", cwd=self.checkout)
        if self.git("diff", "--cached", "--quiet", cwd=self.checkout, check=False).returncode == 0:
            return
        self.git("-c", "user.name=wake-bot", "-c", "user.email=wake-bot@users.noreply.github.com",
                 "commit", "-m", "Record durable wake state", cwd=self.checkout)
        # A state push can fail transiently after the model call has already completed.
        # Retry only the exact same Git ref update: this is idempotent if GitHub accepted
        # the first push but the runner lost the response, and it never force-pushes,
        # rebases, or replays the model call. Persistent conflicts still page the operator.
        last = None
        for attempt in range(1, 4):
            last = self.git("push", "origin", f"HEAD:refs/heads/{self.branch}",
                            cwd=self.checkout, check=False)
            if last.returncode == 0:
                if attempt > 1:
                    print(f"Durable state push succeeded on attempt {attempt}.")
                return
            detail = (last.stderr or last.stdout or "").strip()
            print(f"Durable state push attempt {attempt}/3 failed: {detail}", file=sys.stderr)
            if attempt < 3:
                time.sleep(2 ** (attempt - 1))
        raise subprocess.CalledProcessError(last.returncode, last.args,
                                            output=last.stdout, stderr=last.stderr)


class LiveProjectionBranch:
    """Replace one public-safe projection without creating a history chain."""

    def __init__(self, repository, branch="wake-live"):
        self.repository = Path(repository)
        self.branch = branch

    def publish(self, payload):
        with tempfile.TemporaryDirectory(prefix="wake-live-") as folder:
            checkout = Path(folder) / "live"
            subprocess.run(["git", "worktree", "add", "--detach", str(checkout), "HEAD"],
                           cwd=self.repository, check=True, capture_output=True, text=True, timeout=GIT_OPERATION_TIMEOUT_SECONDS)
            try:
                local_branch = f"{self.branch}-refresh-{uuid.uuid4().hex}"
                subprocess.run(["git", "checkout", "--orphan", local_branch], cwd=checkout,
                               check=True, capture_output=True, text=True)
                subprocess.run(["git", "rm", "-rf", "--ignore-unmatch", "."], cwd=checkout,
                               check=False, capture_output=True, text=True)
                (checkout / "live.json").write_text(
                    json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n",
                    encoding="utf-8",
                )
                subprocess.run(["git", "add", "live.json"], cwd=checkout, check=True)
                subprocess.run([
                    "git", "-c", "user.name=wake-bot",
                    "-c", "user.email=wake-bot@users.noreply.github.com",
                    "commit", "-m", "Refresh disposable WAKE live projection",
                ], cwd=checkout, check=True, capture_output=True, text=True, timeout=GIT_OPERATION_TIMEOUT_SECONDS)
                subprocess.run(["git", "push", "--force", "origin", f"HEAD:refs/heads/{self.branch}"],
                               cwd=checkout, check=True, capture_output=True, text=True, timeout=GIT_OPERATION_TIMEOUT_SECONDS)
            finally:
                subprocess.run(["git", "worktree", "remove", "--force", str(checkout)],
                               cwd=self.repository, check=False, capture_output=True, text=True, timeout=GIT_OPERATION_TIMEOUT_SECONDS)


def continuation_outputs(result):
    """Expose chain control from the authoritative result, never from live projection."""
    status = result.get("status")
    reason = str(result.get("reason", ""))
    continue_now = status in ("accepted", "rejected")
    retry_after = 0
    if status == "deferred" and reason.startswith("Gemini temporarily unavailable"):
        continue_now = True
        retry_after = 15
    set_step_output("status", status or "unknown")
    set_step_output("continue_now", "true" if continue_now else "false")
    set_step_output("retry_after", str(retry_after))


def main(publish_only=False, scheduled=False, reset=False, record_only=False):
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("This entry point runs in GitHub Actions. Use python -m wake for local work.")
    settings = config(ROOT / "wake.toml")
    result = {"status": "failed", "reason": "WAKE✳︎ did not complete"}
    with tempfile.TemporaryDirectory(prefix="wake-cloud-") as folder:
        branch = StateBranch(ROOT, Path(folder)/"state")
        branch.open()
        engine = Engine(branch.checkout/"data", settings)
        try:
            # Publication refreshes are read-only consumers of the durable record.
            # They may run concurrently with research because they never initialize,
            # recover, append, repair, checkpoint, or push wake-state. Configuration
            # adoption therefore remains part of the next serialized stateful wake.
            if publish_only and not reset:
                state, verified_head, verified_events = engine.store.replay_record()
                latest = next(reversed(state["invocations"].values()), None)
                result = ({"status": latest["status"], "id": latest["id"], "reason": latest.get("reason", "")}
                          if latest else {"status": "not_started", "reason": "Waiting for the first research wake"})
                if latest and latest["status"] == "accepted":
                    result["cycle"] = state["version"]
                result["publication_only"] = True
                result["wake_status"] = wake_status(
                    state,
                    None if settings.get("model_daily_call_limits") else settings["daily_call_limit"],
                )
                # Reuse the previous published artifact as a cache of immutable
                # presentation files. export() overwrites current shells/data but
                # can leave already-converted historical route shells untouched.
                shutil.rmtree(ROOT / "site", ignore_errors=True)
                export(
                    engine.store, ROOT / "site", operation=result, browser_only=True,
                    record_snapshot=(state, verified_head, verified_events),
                )
                atomic_write(ROOT / "site/operation.json", json.dumps(result, indent=2))
                atomic_write(ROOT / "site/.nojekyll", "")
                print(json.dumps(result))
                return 0

            # Stateful wakes remain serialized: initialize/recover may append
            # durable events and must checkpoint before any provider request.
            with engine.store.lock():
                if reset:
                    # Reset means exactly cycle/version zero. Do not immediately
                    # re-seed initialization events; the next deliberate cycle
                    # adopts current configuration and records that transition.
                    engine.store.reset()
                else:
                    engine.initialize()
                    engine.recover(explicit=True)
                    branch.checkpoint()
            if scheduled and not reset:
                due, next_eligible = scheduled_wake_due(engine.store.load())
                if not due:
                    result = {"status": "waiting",
                              "reason": "A recent wake or provider quota window suppresses this call.",
                              "next_eligible": next_eligible.isoformat()}
                    set_step_output("skipped", "true")
                    continuation_outputs(result)
                    print(json.dumps(result))
                    return 0
            result_checkpointed = False
            try:
                if reset:
                    state = engine.store.load()
                    result = {"status": "not_started",
                              "reason": "WAKE reset to zero",
                              "reset": True,
                              "cycle": state["version"]}
                else:
                    provider = Gemini(settings)
                    result = engine.run(provider, checkpoint=branch.checkpoint, collector=collect)
                    # Engine.run checkpoints every terminal provider/governance result.
                    # Do not immediately re-stage/re-hash the growing SQLite blob again.
                    result_checkpointed = True
            except Rejected as exc:
                result = {"status": "paused", "reason": str(exc)}
            result["wake_status"] = wake_status(engine.store.load(), None if settings.get("model_daily_call_limits") else settings["daily_call_limit"])
            if not publish_only:
                # Engine.run already made ordinary terminal results durable. Reset
                # and exceptional paused paths still need an explicit checkpoint.
                if not result_checkpointed:
                    branch.checkpoint()
                runtime_ref = os.environ.get("WAKE_RUNTIME_REF", "")
                try:
                    payload = build_live_projection(engine.store, operation=result, runtime_ref=runtime_ref)
                    LiveProjectionBranch(ROOT).publish(payload)
                    set_step_output("live_projection_updated", "true")
                except Exception as exc:
                    # Projection failure cannot roll back or invalidate SQLite,
                    # and it must not prevent the authoritative chain continuing.
                    set_step_output("live_projection_updated", "false")
                    print(json.dumps({"live_projection_updated": False, "error": str(exc)}), file=sys.stderr)
                continuation_outputs(result)
                set_step_output("publication_skipped", "true")
        finally:
            engine.store.close()
    print(json.dumps(result))
    return 0 if publish_only or not requires_operator_attention(result) else 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish-only", action="store_true", help="Publish the existing record without a model call")
    parser.add_argument("--scheduled", action="store_true", help="Skip duplicate cron events covered by a recent wake")
    parser.add_argument("--record-only", action="store_true",
                        help="Persist the durable wake and compact receipt without rebuilding derived reports")
    parser.add_argument("--reset", action="store_true",
                        help="Irreversibly reset durable cloud state to WAKE 0")
    parser.add_argument("--confirm-reset", action="store_true",
                        help="Required confirmation for --reset")
    args = parser.parse_args()
    if args.reset and not args.confirm_reset:
        raise SystemExit("--reset requires --confirm-reset")
    try:
        sys.exit(main(publish_only=args.publish_only, scheduled=args.scheduled, reset=args.reset, record_only=args.record_only))
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        message = "Git state persistence failed. No force push or automatic model retry was attempted."
        if detail:
            message += f"\n{detail}"
        raise SystemExit(message) from None
