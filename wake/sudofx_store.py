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
from .history import history_metrics, merge_history_metrics
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
            baseline = migration.get("history_baseline")
            if count and not isinstance(baseline, dict):
                raise IntegrityError("Imported WAKE history baseline is required when legacy SQLite is detached")
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

    def replay_record(self):
        """Return verified WAKE-compatible state, head, and event history."""
        state, head = self.replay()
        return state, head, self.events()

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

    def _baseline(self):
        baseline = self._envelope()["migration"].get("history_baseline")
        return baseline if isinstance(baseline, dict) else {}

    def events(self):
        """Return full history while legacy SQLite is attached, otherwise the bounded compatibility tail."""
        migration = self._envelope()["migration"]
        count = migration["import_legacy_event_count"]
        if self.legacy_store is not None:
            prefix = self.legacy_store.events()[:count]
        else:
            prefix = list(self._baseline().get("recent_events", []))
        return [*prefix, *self._post_migration_events()]

    def tail_events_all(self, limit):
        return self.events()[-max(0, limit):] if limit > 0 else []

    def tail_events(self, kinds, limit):
        if limit <= 0:
            return []
        allowed = set(kinds)
        return [event for event in self.events() if event["kind"] in allowed][-limit:]

    def event_counts_since(self, seq, kinds):
        migration = self._envelope()["migration"]
        imported = migration["import_legacy_event_count"]
        post = self._post_migration_events()
        if self.legacy_store is not None:
            selected = [
                event for event in [*self.legacy_store.events()[:imported], *post]
                if event["seq"] > seq
            ]
        elif seq >= imported:
            selected = [event for event in post if event["seq"] > seq]
        else:
            baseline = self._baseline()
            anchor = baseline.get("temporal_anchor_seq")
            suffix = baseline.get("temporal_suffix")
            if seq != anchor or not isinstance(suffix, dict):
                raise IntegrityError(
                    "Detached legacy history only supports the persisted temporal anchor or post-migration sequence queries"
                )
            post_selected = [event for event in post if event["seq"] > imported]
            base_kinds = suffix.get("kinds", {})
            counts = {kind: int(base_kinds.get(kind, 0)) for kind in kinds}
            for event in post_selected:
                if event["kind"] in counts:
                    counts[event["kind"]] += 1
            return {"total": int(suffix.get("total", 0)) + len(post_selected), "kinds": counts}
        counts = {kind: 0 for kind in kinds}
        for event in selected:
            if event["kind"] in counts:
                counts[event["kind"]] += 1
        return {"total": len(selected), "kinds": counts}

    def history_metrics(self):
        """Return complete aggregate metrics without requiring the legacy database at runtime."""
        post = self._post_migration_events()
        if self.legacy_store is not None:
            return history_metrics(
                [*self.legacy_store.events()[: self._envelope()["migration"]["import_legacy_event_count"]], *post],
                self.load(),
            )
        base = self._baseline().get("history_metrics", {})
        return merge_history_metrics(base, history_metrics(post, self.load()))

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
