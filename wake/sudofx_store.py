"""
Transitional WAKE Store interface backed by the sudofx authoritative database.

The legacy WAKE database is accepted only as a verified, read-only migration
source. Every post-migration mutation is an application intent committed to
sudofx. Historical query methods combine the frozen imported legacy prefix with
WAKE-compatible events reconstructed from sudofx application action inputs.
"""

from __future__ import annotations

import fcntl
import uuid
from contextlib import contextmanager
from pathlib import Path

from sudofx import (
    ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel,
    SubmissionProvenance,
)
from sudofx.governance import Governance
from sudofx.record import Record

from .store import IntegrityError, digest, now
from .sudofx_application import WAKE_APPLICATION, verified_legacy_snapshot


class SudofxStore:
    """Present the narrow WAKE Store protocol while sudofx owns new durability."""

    def __init__(self, directory, *, legacy_store=None):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / "sudofx.sqlite"
        self.record = Record(self.path)
        self.registry = ApplicationRegistry((WAKE_APPLICATION,))
        self.kernel = Kernel(self.record, Governance(application_registry=self.registry))
        self.host = ApplicationHost(self.kernel, self.registry, "wake")
        self.legacy_store = legacy_store
        if self.host.context().state is None:
            if legacy_store is None:
                raise IntegrityError("A verified legacy WAKE store is required for first migration")
            payload = verified_legacy_snapshot(legacy_store)
            receipt = self.host.submit(
                ApplicationIntent(
                    "wake-legacy-import-" + str(payload["legacy_head"])[:16],
                    self.kernel.context().revision,
                    "import_legacy_snapshot",
                    payload,
                    rationale="Initialize WAKE application from verified legacy replay",
                ),
                provenance=SubmissionProvenance(
                    "application", "wake-sudofx-store", "verified-legacy-migration"
                ),
            )
            if receipt.status != "accepted":
                raise IntegrityError("sudofx rejected verified WAKE migration: " + "; ".join(receipt.reasons))
        self._verify_legacy_prefix()

    def _envelope(self):
        value = self.host.context().state
        if not isinstance(value, dict) or not isinstance(value.get("state"), dict):
            raise IntegrityError("WAKE application state is unavailable")
        return value

    def _verify_legacy_prefix(self):
        migration = self._envelope()["migration"]
        count = migration.get("import_legacy_event_count")
        head = migration.get("import_legacy_head")
        if self.legacy_store is None:
            if count:
                raise IntegrityError("Legacy WAKE history source is required for compatibility queries")
            return
        events = self.legacy_store.events()
        if not isinstance(count, int) or count < 0 or count > len(events):
            raise IntegrityError("Imported WAKE event count does not match legacy history")
        observed = events[count - 1]["hash"] if count else "0" * 64
        if observed != head:
            raise IntegrityError("Imported WAKE head does not match legacy history prefix")

    def close(self):
        """No persistent connection is retained by sudofx Record."""

    @contextmanager
    def lock(self):
        """Serialize whole WAKE turns, including provider calls, without durable flat state."""
        with (self.directory / "writer.lock").open("a") as lock:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                from .governance import Rejected
                raise Rejected("Another wake owns this state directory; no call was made") from None
            try:
                yield
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)

    def load(self, repair=False):
        return self._envelope()["state"]

    def replay(self):
        envelope = self._envelope()
        return envelope["state"], envelope["migration"]["legacy_head"]

    def projection(self):
        return self.replay()

    def head(self):
        return self._envelope()["migration"]["legacy_head"]

    def append(self, kind, payload, crash=False):
        if crash:
            raise RuntimeError("Crash injection is not supported by the transitional sudofx store")
        revision = self.kernel.context().revision
        receipt = self.host.submit(
            ApplicationIntent(
                f"wake-event-{revision + 1}-{uuid.uuid4().hex[:12]}",
                revision,
                "append_legacy_event",
                {"kind": kind, "payload": payload, "time": now()},
                rationale="WAKE compatibility event committed through sudofx",
            ),
            provenance=SubmissionProvenance(
                "application", "wake-engine", "sudofx-authoritative-store"
            ),
        )
        if receipt.status != "accepted":
            from .governance import Rejected
            raise Rejected("; ".join(receipt.reasons) or f"sudofx rejected WAKE event: {kind}")
        return self.load()

    def _post_migration_events(self):
        envelope = self._envelope()
        migration = envelope["migration"]
        seq = migration["import_legacy_event_count"]
        head = migration["import_legacy_head"]
        result = []
        for receipt in self.record.history():
            if receipt["status"] != "accepted":
                continue
            operations = receipt["proposal"].get("operations", [])
            if len(operations) != 1:
                continue
            operation = operations[0]
            if operation.get("action") != "apply_application" or operation.get("key") != "wake":
                continue
            value = operation.get("value", {})
            if value.get("action") != "append_legacy_event":
                continue
            item = value.get("input")
            if not isinstance(item, dict):
                continue
            seq += 1
            event = {
                "seq": seq,
                "time": item["time"],
                "kind": item["kind"],
                "payload": item["payload"],
                "prev_hash": head,
            }
            event["hash"] = digest(event)
            head = event["hash"]
            result.append(event)
        if head != migration["legacy_head"] or seq != migration["legacy_event_count"]:
            raise IntegrityError("sudofx WAKE compatibility event projection does not match durable migration head")
        return result

    def events(self):
        migration = self._envelope()["migration"]
        count = migration["import_legacy_event_count"]
        prefix = [] if self.legacy_store is None else self.legacy_store.events()[:count]
        return [*prefix, *self._post_migration_events()]

    def tail_events_all(self, limit):
        return self.events()[-max(0, limit):] if limit > 0 else []

    def tail_events(self, kinds, limit):
        if limit <= 0:
            return []
        allowed = set(kinds)
        return [event for event in self.events() if event["kind"] in allowed][-limit:]

    def event_counts_since(self, seq, kinds):
        selected = [event for event in self.events() if event["seq"] > seq]
        counts = {kind: 0 for kind in kinds}
        for event in selected:
            if event["kind"] in counts:
                counts[event["kind"]] += 1
        return {"total": len(selected), "kinds": counts}

    def performance_snapshot(self):
        health = self.record.health()
        return {
            "authority": "sudofx",
            "event_count": self._envelope()["migration"]["legacy_event_count"],
            "sudofx_revision": health["revision"],
            "sudofx_database_bytes": health["database_bytes"],
            "trusted_projection_active": True,
        }

    def backup(self, destination):
        target = Path(destination)
        if target.exists():
            from .governance import Rejected
            raise Rejected("Backup destination already exists")
        self.record.backup_to(target)
        return target
