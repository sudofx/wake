#!/usr/bin/env python3
"""Read-only Phase E shadow migration proof against the current wake-state branch."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from sudofx import ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel, SubmissionProvenance
from sudofx.governance import Governance
from sudofx.record import Record

from scripts.github_wake import ROOT, StateBranch
from wake.engine import Engine, config
from wake.sudofx_application import WAKE_APPLICATION, verified_legacy_snapshot


def prove() -> dict[str, object]:
    """Verify current WAKE authority can be represented exactly by sudofx without cutover."""
    settings = config(ROOT / "wake.toml")
    with tempfile.TemporaryDirectory(prefix="wake-sudofx-shadow-") as folder:
        root = Path(folder)
        branch = StateBranch(ROOT, root / "wake-state")
        branch.open()
        engine = Engine(branch.checkout / "data", settings)
        try:
            payload = verified_legacy_snapshot(engine.store)
            legacy_state = payload["legacy_state"]

            registry = ApplicationRegistry((WAKE_APPLICATION,))
            record_path = root / "sudofx-shadow.sqlite"
            record = Record(record_path)
            kernel = Kernel(record, Governance(application_registry=registry))
            host = ApplicationHost(kernel, registry, "wake")
            receipt = host.submit(
                ApplicationIntent(
                    "wake-shadow-import",
                    0,
                    "import_legacy_snapshot",
                    payload,
                    rationale="Read-only Phase E equivalence proof",
                ),
                provenance=SubmissionProvenance(
                    "application",
                    "wake-shadow-migration",
                    "verified-wake-state-replay",
                ),
            )
            if receipt.status != "accepted":
                raise RuntimeError(f"sudofx shadow import rejected: {receipt.reasons}")

            imported = host.context().state
            if imported["state"] != legacy_state:
                raise RuntimeError("sudofx imported WAKE state differs from verified legacy replay")
            migration = imported["migration"]
            for field in ("legacy_head", "legacy_event_count", "legacy_state_digest", "legacy_version"):
                if migration[field] != payload[field]:
                    raise RuntimeError(f"migration metadata mismatch: {field}")

            replayed = Kernel(Record(record_path)).context().state["app:wake"]["state"]
            if replayed != imported:
                raise RuntimeError("fresh sudofx replay differs from imported WAKE application state")

            return {
                "status": "pass",
                "legacy_head": payload["legacy_head"],
                "legacy_event_count": payload["legacy_event_count"],
                "legacy_version": payload["legacy_version"],
                "legacy_state_digest": payload["legacy_state_digest"],
                "sudofx_revision": kernel.context().revision,
            }
        finally:
            engine.store.close()


if __name__ == "__main__":
    print(json.dumps(prove(), sort_keys=True))
