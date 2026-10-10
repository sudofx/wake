#!/usr/bin/env python3
# WAKE✳︎ MAINTAINER NOTE
#
# GitHub Actions entry point. It loads cloud state, runs one bounded wake, publishes artifacts, and reports status while preserving the durable branch as continuity.
#
# Explain intent, invariants, failure behavior, and architectural boundaries in comments.
# Future humans and models should be able to tell deliberate constraints from incidental implementation.

"""Execute only the promoted hosted runtime against wake-state authority.

    master and Pages are separate release lanes; a new web shell does not promote
    research code. Persist the invocation reservation remotely before provider
    effects, then checkpoint the outcome before publishing disposable wake-live.
    A green job can contain a governed rejection or deferral, not accepted work.
    """

import argparse
import gzip
import hashlib
import json
import os
import shutil
import sqlite3
import urllib.request
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

# GitHub rejects individual Git blobs at 100 MiB. Compact well before that
# hard boundary so a normal research turn cannot strand the authority branch.
GITHUB_BLOB_LIMIT_BYTES = 100 * 1024 * 1024
STATE_COMPACT_AT_BYTES = 90 * 1024 * 1024
STATE_ARCHIVE_NAME = "wake.sqlite.gz"
def compact_authority_for_checkpoint(
    path,
    *,
    compact_at=STATE_COMPACT_AT_BYTES,
):
    """Reclaim verified SQLite slack before transport packaging.

    The runtime authority remains SQLite. GitHub persistence is a transport
    concern handled separately so Git blob limits never redefine storage
    semantics.
    """
    path = Path(path)
    if not path.exists():
        return 0
    before = path.stat().st_size
    if before >= compact_at:
        Record(path).compact()
        after = path.stat().st_size
        print(f"Compacted WAKE authority before checkpoint: {before} -> {after} bytes.")
    else:
        after = before
    return after


def _sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def package_authority_for_git(
    sqlite_path,
    archive_path,
    *,
    hard_limit=GITHUB_BLOB_LIMIT_BYTES,
):
    """Create and verify the Git transport form of the SQLite authority.

    SQLite is still the only operational authority. The gzip file is merely a
    deterministic checkpoint package small enough for GitHub's per-blob limit.
    Verify by round-tripping the package and comparing exact bytes before it can
    be staged.
    """
    sqlite_path, archive_path = Path(sqlite_path), Path(archive_path)
    require_source = sqlite_path.exists()
    if not require_source:
        raise Rejected("Cannot package missing wake.sqlite authority")

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = archive_path.with_suffix(archive_path.suffix + ".tmp")
    restored = archive_path.with_suffix(archive_path.suffix + ".verify")
    try:
        with sqlite_path.open("rb") as source, temporary.open("wb") as raw_target:
            with gzip.GzipFile(fileobj=raw_target, mode="wb", compresslevel=6, mtime=0) as target:
                shutil.copyfileobj(source, target, length=1024 * 1024)
        compressed_bytes = temporary.stat().st_size
        if compressed_bytes >= hard_limit:
            raise Rejected(
                "Compressed WAKE authority still exceeds GitHub's 100 MiB "
                "single-file limit; no checkpoint or additional provider call is safe."
            )
        with gzip.open(temporary, "rb") as source, restored.open("wb") as target:
            shutil.copyfileobj(source, target, length=1024 * 1024)
        if _sha256(restored) != _sha256(sqlite_path):
            raise Rejected("Compressed WAKE authority failed byte-for-byte restore verification")
        temporary.replace(archive_path)
        return compressed_bytes
    finally:
        temporary.unlink(missing_ok=True)
        restored.unlink(missing_ok=True)


def restore_authority_from_git(archive_path, sqlite_path):
    """Restore the Git transport package into the runtime SQLite path."""
    archive_path, sqlite_path = Path(archive_path), Path(sqlite_path)
    if not archive_path.exists():
        return False
    sqlite_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = sqlite_path.with_suffix(sqlite_path.suffix + ".restore")
    try:
        with gzip.open(archive_path, "rb") as source, temporary.open("wb") as target:
            shutil.copyfileobj(source, target, length=1024 * 1024)
        # Opening and replaying through Record validates the restored SQLite
        # structure before the runtime is allowed to use it.
        verify_existing_record(temporary)
        temporary.replace(sqlite_path)
        return True
    except (OSError, EOFError) as exc:
        raise Rejected("Stored WAKE authority package could not be restored safely") from exc
    finally:
        temporary.unlink(missing_ok=True)
sys.path.insert(0, str(ROOT))
from wake.engine import Engine, config
from wake.governance import Rejected
from wake.providers import Gemini
from wake.research import collect
from wake.live import build_live_projection
from wake.authority import open_authoritative_store, verify_existing_record
from wake.kernel.record import Record


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

    reason = str(result.get("reason", ""))
    if status == "paused" and reason.startswith((
        "Configured daily request limits reached",
        "Gemini free-tier daily quota exhausted",
        "Daily call ceiling reached",
    )):
        return False

    provider_error = result.get("provider_error", {})
    if provider_error.get("http_status") == 429:
        return False

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
        # Set by open(). A brand-new state branch is the only cloud path allowed
        # to initialize empty authority; an existing branch must contain one of
        # the supported database formats or fail closed.
        self.existed = None
        self.remote_head = None

    def git(self, *args, cwd=None, check=True):
        return subprocess.run(["git", *args], cwd=cwd or self.repository, capture_output=True, text=True, check=check, timeout=STATE_GIT_OPERATION_TIMEOUT_SECONDS)

    def open(self):
        result = self.git("ls-remote", "--exit-code", "--heads", "origin", f"refs/heads/{self.branch}", check=False)
        if result.returncode == 0:
            self.existed = True
            self.git("fetch", "--depth=1", "--no-tags", "origin", f"refs/heads/{self.branch}")
            self.git("worktree", "add", "--detach", str(self.checkout), "FETCH_HEAD")
            self.remote_head = self.git("rev-parse", "HEAD", cwd=self.checkout).stdout.strip()
            legacy = self.checkout / "data/wake.sqlite3"
            wake = self.checkout / "data/wake.sqlite"
            archive = self.checkout / "data" / STATE_ARCHIVE_NAME
            previous_archives = [
                path for path in (self.checkout / "data").glob("*.sqlite.gz")
                if path != archive
            ]
            if previous_archives:
                if archive.exists() or len(previous_archives) != 1:
                    raise Rejected("Ambiguous WAKE authority checkpoint packages")
                archive = previous_archives[0]
            if not wake.exists() and archive.exists():
                restore_authority_from_git(archive, wake)
            if not legacy.exists() and not list((self.checkout / "data").glob("*.sqlite")):
                raise Rejected(
                    "Existing wake-state branch is missing both legacy and wake authority; refusing to continue"
                )
        elif result.returncode == 2:
            self.existed = False
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
        # Physical SQLite slack is not semantic history. Reclaim it before the
        # authoritative blob approaches GitHub's hard single-file limit.
        # Record.compact() verifies SQLite integrity and complete wake replay
        # before returning, so a failed maintenance pass cannot be checkpointed.
        wake = self.checkout / "data/wake.sqlite"
        compact_authority_for_checkpoint(wake)
        archive = self.checkout / "data" / STATE_ARCHIVE_NAME
        if wake.exists():
            compressed_bytes = package_authority_for_git(wake, archive)
            print(
                f"Packaged WAKE SQLite authority for Git transport: "
                f"{wake.stat().st_size} -> {compressed_bytes} bytes."
            )

        # wake-state is authority, not a publication cache. Retire legacy
        # JSON/HTML projections from the current tree. After migration,
        # data/wake.sqlite is the sole accumulating operational record;
        # data/wake.sqlite3 remains frozen migration evidence only.
        self.git("rm", "-r", "--ignore-unmatch", "events.jsonl", "state.json", "head.txt",
                 "operation.json", "site", cwd=self.checkout, check=False)
        authority = (
            f"data/{STATE_ARCHIVE_NAME}"
            if archive.exists()
            else "data/wake.sqlite3"
        )
        if authority == f"data/{STATE_ARCHIVE_NAME}":
            # Retire previous transport filenames only after the canonical
            # package round-trip has verified. History stays inside SQLite.
            for previous in (self.checkout / "data").glob("*.sqlite.gz"):
                if previous != archive:
                    self.git("rm", "--ignore-unmatch", str(previous.relative_to(self.checkout)),
                             cwd=self.checkout, check=False)
            # The runtime database stays local to the worktree. Git stores only
            # the verified transport package, preventing GitHub blob limits from
            # becoming an accidental database-size ceiling.
            self.git(
                "rm", "--cached", "--ignore-unmatch", "data/*.sqlite",
                cwd=self.checkout, check=False,
            )
            self.git(
                "rm", "--ignore-unmatch", "data/wake.sqlite3",
                cwd=self.checkout, check=False,
            )
        self.git("add", "--force", authority, cwd=self.checkout)
        if self.git("diff", "--cached", "--quiet", cwd=self.checkout, check=False).returncode == 0:
            return
        self.git("-c", "user.name=wake-bot", "-c", "user.email=wake-bot@users.noreply.github.com",
                 "commit", "-m", "Record durable wake state", cwd=self.checkout)
        # Git is checkpoint transport, not the authority ledger. The hash-linked
        # SQLite record already contains the complete append-only history; retaining
        # every compressed database version in Git makes each cycle add hundreds of
        # MiB that cannot delta-compress effectively. Publish the exact committed
        # tree as a parentless snapshot so fresh clones fetch only current authority.
        tree = self.git("rev-parse", "HEAD^{tree}", cwd=self.checkout).stdout.strip()
        snapshot = self.git(
            "-c", "user.name=wake-bot", "-c", "user.email=wake-bot@users.noreply.github.com",
            "commit-tree", tree,
            cwd=self.checkout,
        ).stdout.strip()
        expected = self.remote_head or ""
        lease = f"--force-with-lease=refs/heads/{self.branch}:{expected}"
        # A state push can fail transiently after the model call has already completed.
        # Retry only the exact same leased ref update. If GitHub accepted the first
        # push but the runner lost the response, read-after-write recognizes the
        # published snapshot. A different remote head is a real conflict and fails
        # closed instead of overwriting another writer.
        last = None
        for attempt in range(1, 4):
            last = self.git("push", lease, "origin", f"{snapshot}:refs/heads/{self.branch}",
                            cwd=self.checkout, check=False)
            if last.returncode == 0:
                self.remote_head = snapshot
                self.git("reset", "--soft", snapshot, cwd=self.checkout)
                if attempt > 1:
                    print(f"Durable state push succeeded on attempt {attempt}.")
                return
            observed = self.git(
                "ls-remote", "--heads", "origin", f"refs/heads/{self.branch}",
                cwd=self.checkout, check=False,
            ).stdout.split()
            observed_head = observed[0] if observed else ""
            if observed_head == snapshot:
                self.remote_head = snapshot
                self.git("reset", "--soft", snapshot, cwd=self.checkout)
                print("Durable state push was already accepted by GitHub.")
                return
            if observed_head != expected:
                raise Rejected(
                    f"Remote {self.branch} changed during checkpoint; refusing to overwrite it"
                )
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
                # Research✳︎ is published from the same verified snapshot,
                # including source classification performed before text clipping.
                from wake.research_projection import build_research_projection
                research = payload.get("research") or build_research_projection(
                    payload["state"], payload.get("events", []), payload["head"],
                    generated=payload.get("generated"), metrics=payload.get("metrics"),
                    operation=payload.get("operation"), source=payload.get("source"),
                )
                if research.get("head") != payload["head"] or research.get("version") != payload["state"]["version"]:
                    raise ValueError("Research projection does not match the live record")
                (checkout / "research-data.json").write_text(
                    json.dumps(research, ensure_ascii=False, separators=(",", ":")) + "\n",
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
                subprocess.run(["git", "add", "live.json", "research-data.json", "map-data.json", "map3d-data.json", "map3d"],
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
    elif status in ("deferred", "paused") and (
        reason.startswith("Configured daily request limits reached")
        or reason.startswith("Gemini free-tier daily quota exhausted")
        or reason.startswith("Daily call ceiling reached")
    ):
        # Daily quota waits can exceed the maximum lifetime of a GitHub job.
        # The scheduled continuation watchdog reads wake-state after Pacific
        # midnight and dispatches one fresh attempt when the durable boundary passes.
        continue_now = False
    set_step_output("status", status or "unknown")
    set_step_output("continue_now", "true" if continue_now else "false")
    set_step_output("retry_after", str(retry_after))


def main(reset=False, enable_continuity_matrix=False):
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("This entry point runs in GitHub Actions. Use python -m wake for local work.")
    settings = config(ROOT / "wake.toml")
    result = {"status": "failed", "reason": "WAKE✳︎ did not complete"}
    with tempfile.TemporaryDirectory(prefix="wake-cloud-") as folder:
        branch = StateBranch(ROOT, Path(folder)/"state")
        branch.open()
        authority_store = open_authoritative_store(
            branch.checkout / "data",
            allow_initialize=branch.existed is False,
        )
        engine = Engine(branch.checkout/"data", settings, store=authority_store)

        def guarded_checkpoint():
            """Persist durable reservations before provider effects and results."""
            branch.checkpoint()

        try:
            # Stateful wakes are serialized: initialize/recover may append
            # durable events and must checkpoint before any provider request.
            with engine.store.lock():
                if reset:
                    # Preserve the exact pre-reset Git state as a convenience
                    # archive. wake itself also retains the prior governed
                    # generation, while active WAKE semantics restart at zero.
                    archive_branch = branch.archive_before_reset()
                    # Reset means exactly cycle/version zero. Do not immediately
                    # re-seed initialization events; the next deliberate cycle
                    # adopts current configuration and records that transition.
                    engine.store.reset()
                else:
                    engine.initialize()
                    engine.recover(explicit=True)
                    if enable_continuity_matrix:
                        engine.store.enable_continuity_matrix()
                    guarded_checkpoint()

            result_checkpointed = False
            try:
                if reset:
                    state = engine.store.load()
                    result = {"status": "not_started",
                              "reason": "WAKE reset to zero",
                              "reset": True,
                              "archive_branch": archive_branch,
                              "cycle": state["version"]}
                elif enable_continuity_matrix:
                    progress = engine.store.continuity_matrix_progress()
                    result = {
                        "status": "not_started",
                        "reason": "Continuity campaign enabled",
                        "continuity_matrix_enabled": True,
                        "matrix": progress,
                        "cycle": engine.store.load()["version"],
                    }
                else:
                    provider = Gemini(settings)
                    result = engine.run(provider, checkpoint=guarded_checkpoint, collector=collect)
                    # Enabled continuity campaigns travel inside this same
                    # provider response and are scored by Engine.finish. There is
                    # no second inference call or separate provider quota lane.
                    # Engine.run checkpoints the research terminal result and its
                    # governed matrix sidecar together.
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
                guarded_checkpoint()

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
    parser.add_argument("--enable-continuity-matrix", action="store_true",
                        help="Explicitly enable WAKE's continuity@1 campaign without calling a provider")
    args = parser.parse_args()
    if args.reset and not args.confirm_reset:
        raise SystemExit("--reset requires --confirm-reset")
    if args.reset and args.enable_continuity_matrix:
        raise SystemExit("--reset and --enable-continuity-matrix are mutually exclusive")
    try:
        sys.exit(main(
            reset=args.reset,
            enable_continuity_matrix=args.enable_continuity_matrix,
        ))
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        message = "Git state persistence failed. No force push or automatic model retry was attempted."
        if detail:
            message += f"\n{detail}"
        raise SystemExit(message) from None
