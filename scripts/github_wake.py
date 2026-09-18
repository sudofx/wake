#!/usr/bin/env python3
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

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from wake.engine import Engine, config
from wake.governance import Rejected
from wake.providers import Gemini, is_free_tier_daily_quota
from wake.research import collect
from wake.report import export, atomic_write


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
    if status in ("accepted", "deferred", "waiting", "not_started"):
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
        return subprocess.run(["git", *args], cwd=cwd or self.repository, capture_output=True, text=True, check=check)

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
        self.git("add", "--force", "data/wake.sqlite3", cwd=self.checkout)
        if self.git("diff", "--cached", "--quiet", cwd=self.checkout, check=False).returncode == 0:
            return
        self.git("-c", "user.name=wake-bot", "-c", "user.email=wake-bot@users.noreply.github.com",
                 "commit", "-m", "Record durable wake state", cwd=self.checkout)
        self.git("push", "origin", f"HEAD:refs/heads/{self.branch}", cwd=self.checkout)


def main(publish_only=False, scheduled=False, reset=False):
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("This entry point runs in GitHub Actions. Use python -m wake for local work.")
    settings = config(ROOT / "wake.toml")
    result = {"status": "failed", "reason": "WAKE✳︎ did not complete"}
    with tempfile.TemporaryDirectory(prefix="wake-cloud-") as folder:
        branch = StateBranch(ROOT, Path(folder)/"state")
        branch.open()
        engine = Engine(branch.checkout/"data", settings)
        try:
            # Initialize/recover and publish a valid empty or recovered journal even if setup fails.
            with engine.store.lock():
                if reset:
                    engine.store.reset()
                engine.initialize()
                engine.recover(explicit=True)
                # A reset is committed only after its fresh export is ready.
                if not reset:
                    branch.checkpoint()
            if scheduled and not reset:
                due, next_eligible = scheduled_wake_due(engine.store.load())
                if not due:
                    result = {"status": "waiting",
                              "reason": "A recent wake or provider quota window suppresses this call.",
                              "next_eligible": next_eligible.isoformat()}
                    set_step_output("skipped", "true")
                    print(json.dumps(result))
                    return 0
            try:
                if reset:
                    state = engine.store.load()
                    result = {"status": "not_started",
                              "reason": "WAKE reset to zero",
                              "reset": True,
                              "cycle": state["version"]}
                elif publish_only:
                    state = engine.store.load()
                    latest = next(reversed(state["invocations"].values()), None)
                    result = ({"status": latest["status"], "id": latest["id"], "reason": latest.get("reason", "")}
                              if latest else {"status": "not_started", "reason": "Waiting for the first research wake"})
                    if latest and latest["status"] == "accepted":
                        result["cycle"] = state["version"]
                    result["publication_only"] = True
                else:
                    provider = Gemini(settings)
                    result = engine.run(provider, checkpoint=branch.checkpoint, collector=collect)
            except Rejected as exc:
                result = {"status": "paused", "reason": str(exc)}
            result["wake_status"] = wake_status(engine.store.load(), None if settings.get("model_daily_call_limits") else settings["daily_call_limit"])
            if reset:
                shutil.rmtree(ROOT / "site", ignore_errors=True)
            export(engine.store, ROOT / "site", operation=result)
            atomic_write(ROOT / "site/operation.json", json.dumps(result, indent=2))
            atomic_write(ROOT / "site/.nojekyll", "")
            # Persist an inspectable text export alongside the exact SQLite state.
            for name in ("events.jsonl", "state.json", "head.txt"):
                atomic_write(branch.checkout/name, (ROOT/"site"/name).read_text())
            # This fallback stays readable through htmlpreview even before Pages is enabled.
            shutil.rmtree(branch.checkout/"site", ignore_errors=True)
            shutil.copytree(ROOT/"site", branch.checkout/"site")
            branch.git("add", "events.jsonl", "state.json", "head.txt", "site", cwd=branch.checkout)
            branch.checkpoint()
        finally:
            engine.store.close()
    print(json.dumps(result))
    return 0 if publish_only or not requires_operator_attention(result) else 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish-only", action="store_true", help="Publish the existing record without a model call")
    parser.add_argument("--scheduled", action="store_true", help="Skip duplicate cron events covered by a recent wake")
    parser.add_argument("--reset", action="store_true",
                        help="Irreversibly reset durable cloud state to WAKE 0")
    parser.add_argument("--confirm-reset", action="store_true",
                        help="Required confirmation for --reset")
    args = parser.parse_args()
    if args.reset and not args.confirm_reset:
        raise SystemExit("--reset requires --confirm-reset")
    try:
        sys.exit(main(publish_only=args.publish_only, scheduled=args.scheduled, reset=args.reset))
    except subprocess.CalledProcessError:
        raise SystemExit("Git state persistence failed. No force push or automatic model retry was attempted.") from None
