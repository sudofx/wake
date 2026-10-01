#!/usr/bin/env python3
# WAKE✳︎ MAINTAINER NOTE
#
# GitHub Actions entry point. It loads cloud state, runs one bounded wake, publishes artifacts, and reports status while preserving the durable branch as continuity.
#
# Explain intent, invariants, failure behavior, and architectural boundaries in comments.
# Future humans and models should be able to tell deliberate constraints from incidental implementation.

"""One cloud wake. Persist the call reservation remotely before sending to Gemini."""

import argparse
import json
import os
from pathlib import Path
from datetime import datetime, timezone
import subprocess
import sys
import tempfile
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
STATE_GIT_OPERATION_TIMEOUT_SECONDS = 90
LIVE_GIT_OPERATION_TIMEOUT_SECONDS = 20
LIVE_PROJECTION_WALL_SECONDS = 30
sys.path.insert(0, str(ROOT))
from wake.engine import Engine, config
from wake.governance import Rejected
from wake.providers import Gemini
from wake.research import collect
from wake.live import build_live_projection
from wake.authority import open_authoritative_store


from wake.scheduling import TRANSIENT_RETRY_DELAY, wake_status


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
        return subprocess.run(["git", *args], cwd=cwd or self.repository, capture_output=True, text=True, check=check, timeout=STATE_GIT_OPERATION_TIMEOUT_SECONDS)

    def open(self):
        result = self.git("ls-remote", "--exit-code", "--heads", "origin", f"refs/heads/{self.branch}", check=False)
        if result.returncode == 0:
            self.git("fetch", "--depth=1", "--no-tags", "origin", f"refs/heads/{self.branch}")
            self.git("worktree", "add", "--detach", str(self.checkout), "FETCH_HEAD")
            legacy = self.checkout / "data/wake.sqlite3"
            sudofx = self.checkout / "data/sudofx.sqlite"
            if not legacy.exists() and not sudofx.exists():
                raise Rejected(
                    "Existing wake-state branch is missing both legacy and sudofx databases; refusing to continue"
                )
        elif result.returncode == 2:
            self.git("worktree", "add", "--detach", str(self.checkout), "HEAD")
            self.git("switch", "--orphan", self.branch, cwd=self.checkout)
        else:
            raise Rejected("Cannot read remote state; no model call will be made")

    def archive_before_reset(self):
        """Preserve the exact pre-reset authority on a named remote branch.

        This is cheaper and safer than copying the SQLite blob into the new run:
        the archived branch points at the already-existing wake-state commit.
        """
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        archive_branch = f"wake-archive-{stamp}"
        head = self.git("rev-parse", "HEAD", cwd=self.checkout).stdout.strip()
        if not head:
            raise Rejected("Cannot identify current wake-state head for archival reset")
        self.git("push", "origin", f"{head}:refs/heads/{archive_branch}", cwd=self.checkout)
        return archive_branch

    def checkpoint(self):
        # wake-state is authority, not a publication cache. Retire legacy
        # JSON/HTML projections from the current tree. After migration,
        # data/sudofx.sqlite is the sole accumulating operational record;
        # data/wake.sqlite3 remains frozen migration evidence only.
        self.git("rm", "-r", "--ignore-unmatch", "events.jsonl", "state.json", "head.txt",
                 "operation.json", "site", cwd=self.checkout, check=False)
        authority = (
            "data/sudofx.sqlite"
            if (self.checkout / "data/sudofx.sqlite").exists()
            else "data/wake.sqlite3"
        )
        if authority == "data/sudofx.sqlite":
            # The verified legacy chain has already been copied into sudofx.
            # Remove the old database from the active authority branch so there
            # is exactly one durable operational database after cutover.
            self.git(
                "rm", "--ignore-unmatch", "data/wake.sqlite3",
                cwd=self.checkout, check=False,
            )
        self.git("add", "--force", authority, cwd=self.checkout)
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


def _projection_timeout(deadline):
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise TimeoutError("Live projection exceeded its wall-clock budget")
    return max(1, min(LIVE_GIT_OPERATION_TIMEOUT_SECONDS, remaining))


class LiveProjectionBranch:
    """Replace one public-safe projection without creating a history chain."""

    def __init__(self, repository, branch="wake-live"):
        self.repository = Path(repository)
        self.branch = branch

    def publish(self, payload):
        deadline = time.monotonic() + LIVE_PROJECTION_WALL_SECONDS
        with tempfile.TemporaryDirectory(prefix="wake-live-") as folder:
            checkout = Path(folder) / "live"
            subprocess.run(["git", "worktree", "add", "--detach", str(checkout), "HEAD"],
                           cwd=self.repository, check=True, capture_output=True, text=True, timeout=_projection_timeout(deadline))
            try:
                local_branch = f"{self.branch}-refresh-{uuid.uuid4().hex}"
                subprocess.run(["git", "checkout", "--orphan", local_branch], cwd=checkout,
                               check=True, capture_output=True, text=True, timeout=_projection_timeout(deadline))
                subprocess.run(["git", "rm", "-rf", "--ignore-unmatch", "."], cwd=checkout,
                               check=False, capture_output=True, text=True, timeout=_projection_timeout(deadline))
                (checkout / "live.json").write_text(
                    json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n",
                    encoding="utf-8",
                )

                # MAP and 3D MAP are disposable projections of the same public
                # snapshot. Publish them atomically with live.json so Reset and
                # every accepted cycle have one visible version across all views.
                from wake.provenance import build_map, build_map3d_projection, map3d_shard_filename
                graph = build_map(payload["state"], payload.get("events", []), payload["head"], replay_history=False)
                (checkout / "map-data.json").write_text(
                    json.dumps(graph, ensure_ascii=False, separators=(",", ":")) + "\n",
                    encoding="utf-8",
                )
                graph3d_shell, graph3d_shards = build_map3d_projection(graph)
                (checkout / "map3d-data.json").write_text(
                    json.dumps(graph3d_shell, ensure_ascii=False, separators=(",", ":")) + "\n",
                    encoding="utf-8",
                )
                shard_dir = checkout / "map3d"
                shard_dir.mkdir(parents=True, exist_ok=True)
                for parent, shard in graph3d_shards.items():
                    (shard_dir / map3d_shard_filename(parent)).write_text(
                        json.dumps(shard, ensure_ascii=False, separators=(",", ":")) + "\n",
                        encoding="utf-8",
                    )
                subprocess.run(["git", "add", "live.json", "map-data.json", "map3d-data.json", "map3d"],
                               cwd=checkout, check=True, timeout=_projection_timeout(deadline))
                subprocess.run([
                    "git", "-c", "user.name=wake-bot",
                    "-c", "user.email=wake-bot@users.noreply.github.com",
                    "commit", "-m", "Refresh disposable WAKE live projection",
                ], cwd=checkout, check=True, capture_output=True, text=True, timeout=_projection_timeout(deadline))
                subprocess.run(["git", "push", "--force", "origin", f"HEAD:refs/heads/{self.branch}"],
                               cwd=checkout, check=True, capture_output=True, text=True, timeout=_projection_timeout(deadline))
            finally:
                try:
                    subprocess.run(["git", "worktree", "remove", "--force", str(checkout)],
                                   cwd=self.repository, check=False, capture_output=True, text=True, timeout=5)
                except Exception:
                    pass


def continuation_outputs(result):
    """Expose chain control from the authoritative result, never from live projection."""
    status = result.get("status")
    reason = str(result.get("reason", ""))
    continue_now = status in ("accepted", "rejected")
    retry_after = 0
    if status == "deferred" and reason.startswith("Gemini temporarily unavailable"):
        continue_now = True
        retry_after = int(TRANSIENT_RETRY_DELAY.total_seconds())
    elif status == "deferred" and (
        reason.startswith("Configured daily request limits reached")
        or reason.startswith("Gemini free-tier daily quota exhausted")
        or reason.startswith("Daily call ceiling reached")
    ):
        next_eligible = result.get("wake_status", {}).get("next_eligible")
        if next_eligible:
            try:
                eligible_at = datetime.fromisoformat(str(next_eligible).replace("Z", "+00:00"))
                retry_after = max(0, int((eligible_at - datetime.now(timezone.utc)).total_seconds()))
                continue_now = True
            except (TypeError, ValueError):
                pass
    set_step_output("status", status or "unknown")
    set_step_output("continue_now", "true" if continue_now else "false")
    set_step_output("retry_after", str(retry_after))


def main(reset=False):
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("This entry point runs in GitHub Actions. Use python -m wake for local work.")
    settings = config(ROOT / "wake.toml")
    result = {"status": "failed", "reason": "WAKE✳︎ did not complete"}
    with tempfile.TemporaryDirectory(prefix="wake-cloud-") as folder:
        branch = StateBranch(ROOT, Path(folder)/"state")
        branch.open()
        authority_store = open_authoritative_store(branch.checkout / "data")
        engine = Engine(branch.checkout/"data", settings, store=authority_store)
        try:
            # Stateful wakes are serialized: initialize/recover may append
            # durable events and must checkpoint before any provider request.
            with engine.store.lock():
                if reset:
                    # Preserve the exact pre-reset Git state as a convenience
                    # archive. sudofx itself also retains the prior governed
                    # generation, while active WAKE semantics restart at zero.
                    archive_branch = branch.archive_before_reset()
                    # Reset means exactly cycle/version zero. Do not immediately
                    # re-seed initialization events; the next deliberate cycle
                    # adopts current configuration and records that transition.
                    engine.store.reset()
                else:
                    engine.initialize()
                    engine.recover(explicit=True)
                    branch.checkpoint()

            result_checkpointed = False
            try:
                if reset:
                    state = engine.store.load()
                    result = {"status": "not_started",
                              "reason": "WAKE reset to zero",
                              "reset": True,
                              "archive_branch": archive_branch,
                              "cycle": state["version"]}
                else:
                    provider = Gemini(settings)
                    result = engine.run(provider, checkpoint=branch.checkpoint, collector=collect)
                    # Engine.run checkpoints every terminal provider/governance result.
                    # Do not immediately re-stage/re-hash the growing SQLite blob again.
                    result_checkpointed = True
            except Rejected as exc:
                result = {"status": "paused", "reason": str(exc)}

            result["wake_status"] = wake_status(
                engine.store.load(),
                None if settings.get("model_daily_call_limits") else settings["daily_call_limit"],
            )

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
        finally:
            engine.store.close()

    print(json.dumps(result))
    return 0 if not requires_operator_attention(result) else 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reset", action="store_true",
                        help="Archive current durable state, then reset active cloud state to WAKE 0")
    parser.add_argument("--confirm-reset", action="store_true",
                        help="Required confirmation for --reset")
    args = parser.parse_args()
    if args.reset and not args.confirm_reset:
        raise SystemExit("--reset requires --confirm-reset")
    try:
        sys.exit(main(reset=args.reset))
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        message = "Git state persistence failed. No force push or automatic model retry was attempted."
        if detail:
            message += f"\n{detail}"
        raise SystemExit(message) from None
