#!/usr/bin/env python3
"""Migrate the live WAKE authority branch to the sudofx database without provider access."""

from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]

from github_wake import StateBranch
from wake.authority import open_authoritative_store


def main() -> int:
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("This migration entry point runs only in GitHub Actions.")

    with tempfile.TemporaryDirectory(prefix="wake-authority-migrate-") as folder:
        branch = StateBranch(ROOT, Path(folder) / "state")
        branch.open()

        data_dir = branch.checkout / "data"
        legacy_path = data_dir / "wake.sqlite3"
        sudofx_path = data_dir / "sudofx.sqlite"
        source_format = "sudofx" if sudofx_path.exists() else "legacy"

        store = open_authoritative_store(data_dir)
        try:
            state = store.load()
            head = store.head()
            event_count = len(store.events())
            revision = store.kernel.context().revision
            health = store.record.health()
        finally:
            store.close()

        reopened = open_authoritative_store(data_dir)
        try:
            assert reopened.load() == state
            assert reopened.head() == head
            assert len(reopened.events()) == event_count
            assert reopened.kernel.context().revision == revision
        finally:
            reopened.close()

        assert sudofx_path.exists(), "sudofx authority database was not created"
        assert not legacy_path.exists(), "legacy WAKE database still exists after verified migration"

        database_bytes_before_checkpoint = sudofx_path.stat().st_size

        # Use the same verified checkpoint boundary as normal research.
        # StateBranch.checkpoint() compacts sudofx.sqlite once it reaches the
        # maintenance threshold and fails closed if the verified result still
        # cannot fit GitHub's single-file limit.
        branch.checkpoint()
        database_bytes_after_checkpoint = sudofx_path.stat().st_size

        tracked = set(
            branch.git("ls-tree", "-r", "--name-only", "HEAD", cwd=branch.checkout)
            .stdout.splitlines()
        )
        assert "data/sudofx.sqlite" in tracked
        assert "data/wake.sqlite3" not in tracked

        result = {
            "source_format": source_format,
            "authority": "sudofx",
            "event_count": event_count,
            "accepted_revision": revision,
            "record_health_revision": health["revision"],
            "database_bytes_before_checkpoint": database_bytes_before_checkpoint,
            "database_bytes_after_checkpoint": database_bytes_after_checkpoint,
            "checkpoint_reclaimed_bytes": (
                database_bytes_before_checkpoint - database_bytes_after_checkpoint
            ),
            "single_authority_database": True,
            "provider_accessed": False,
        }
        print(json.dumps(result, sort_keys=True))
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            with Path(summary).open("a", encoding="utf-8") as out:
                out.write("## WAKE authority migration\n\n")
                for key, value in result.items():
                    out.write(f"- **{key}**: {value}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
