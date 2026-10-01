"""
Transitional WAKE Store interface backed by the sudofx authoritative database.

The legacy WAKE database is accepted only as a verified, read-only migration
source. Every post-migration mutation is an application intent committed to
sudofx. Historical query methods combine the frozen imported legacy prefix with
WAKE-compatible events reconstructed from sudofx application action inputs.
"""

from __future__ import annotations

import fcntl
import os
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


class _CrashInjectableRecordStore:
    """Wrap the public sudofx storage contract with a fixture-only pre-commit failpoint."""

    def __init__(self, record):
        self.record = record
        self.crash_next_write = False

    def read_transaction(self):
        return self.record.read_transaction()

    @contextmanager
    def write_transaction(self):
        armed = self.crash_next_write
        self.crash_next_write = False
        with self.record.write_transaction() as transaction:
            yield transaction
            if armed:
                # Exit while the delegated transaction is still open. SQLite (or
                # any future compliant backend) must publish none of the staged
                # mutation when the process disappears before context success.
                os._exit(86)

    def history(self):
        return self.record.history()

    def projection_snapshot(self, history_limit=50):
        return self.record.projection_snapshot(history_limit)


class SudofxStore:
    """Present the narrow WAKE Store protocol while sudofx owns new durability."""

    def __init__(self, directory, *, legacy_store=None):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path = self.directory / "sudofx.sqlite"
        self.record = Record(self.path)
        self._kernel_store = _CrashInjectableRecordStore(self.record)
        self.registry = ApplicationRegistry((WAKE_APPLICATION,))
        self.kernel = Kernel(self._kernel_store, Governance(application_registry=self.registry))
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
        if legacy_store is not None:
            self._archive_legacy_history(legacy_store.events())
        self._verify_legacy_prefix()

    def _envelope(self):
        value = self.host.context().state
        if not isinstance(value, dict) or not isinstance(value.get("state"), dict):
            raise IntegrityError("WAKE application state is unavailable")
        return value

    def _archive_legacy_history(self, events):
        """Copy the verified pre-migration event chain into the sudofx event log once."""
        migration = self._envelope()["migration"]
        target_count = migration["import_legacy_event_count"]
        target_head = migration["import_legacy_head"]
        if len(events) != target_count:
            raise IntegrityError("Legacy WAKE history length changed after verified migration")
        observed_head = events[-1]["hash"] if events else "0" * 64
        if observed_head != target_head:
            raise IntegrityError("Legacy WAKE history head changed after verified migration")

        archived = int(migration.get("archive_event_count", 0))
        while archived < target_count:
            chunk = events[archived : min(target_count, archived + 50)]
            revision = self.kernel.context().revision
            receipt = self.host.submit(
                ApplicationIntent(
                    f"wake-legacy-archive-{archived + 1}-{archived + len(chunk)}",
                    revision,
                    "import_legacy_event_chunk",
                    {"events": chunk},
                    rationale="Move verified legacy WAKE history into the single sudofx database",
                ),
                provenance=SubmissionProvenance(
                    "application", "wake-sudofx-store", "verified-legacy-history-archive"
                ),
            )
            if receipt.status != "accepted":
                raise IntegrityError(
                    "sudofx rejected verified WAKE history archive: " + "; ".join(receipt.reasons)
                )
            archived += len(chunk)

    def _archived_legacy_events(self):
        """Reconstruct the exact imported legacy prefix from sudofx action inputs."""
        migration = self._envelope()["migration"]
        target_count = migration.get("import_legacy_event_count")
        target_head = migration.get("import_legacy_head")
        if not migration.get("archive_complete"):
            raise IntegrityError("Legacy WAKE history archive is incomplete")

        result = []
        head = "0" * 64
        expected_seq = 1
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
            if value.get("action") != "import_legacy_event_chunk":
                continue
            item = value.get("input", {})
            events = item.get("events") if isinstance(item, dict) else None
            if not isinstance(events, list):
                raise IntegrityError("Archived WAKE event chunk is malformed")
            for event in events:
                if not isinstance(event, dict):
                    raise IntegrityError("Archived WAKE event is malformed")
                if event.get("seq") != expected_seq or event.get("prev_hash") != head:
                    raise IntegrityError("Archived WAKE event chain is not contiguous")
                body = {key: item for key, item in event.items() if key != "hash"}
                if digest(body) != event.get("hash"):
                    raise IntegrityError("Archived WAKE event hash is invalid")
                result.append(event)
                expected_seq += 1
                head = event["hash"]

        if len(result) != target_count or head != target_head:
            raise IntegrityError("Archived WAKE history does not match imported migration boundary")
        return result

    def _verify_legacy_prefix(self):
        migration = self._envelope()["migration"]
        import_count = migration.get("import_legacy_event_count")
        import_head = migration.get("import_legacy_head")
        if (
            migration.get("archive_event_count") != import_count
            or migration.get("archive_head") != import_head
        ):
            raise IntegrityError("Imported WAKE history has not been fully archived into sudofx")
        self._archived_legacy_events()
        if self.legacy_store is not None:
            events = self.legacy_store.events()
            if not isinstance(import_count, int) or import_count < 0 or import_count > len(events):
                raise IntegrityError("Imported WAKE event count does not match legacy history")
            observed = events[import_count - 1]["hash"] if import_count else "0" * 64
            if observed != import_head:
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

    def reset(self):
        """Start WAKE Zero through the governed application boundary."""
        revision = self.kernel.context().revision
        receipt = self.host.submit(
            ApplicationIntent(
                f"wake-reset-{revision + 1}-{uuid.uuid4().hex[:12]}",
                revision,
                "reset_to_zero",
                {
                    "actor": "operator",
                    "reason": "Operator requested WAKE reset to cycle zero.",
                },
                rationale="Create a new active WAKE generation without deleting prior sudofx history",
            ),
            provenance=SubmissionProvenance(
                "human", "wake-operator", "explicit-reset"
            ),
        )
        if receipt.status != "accepted":
            from .governance import Rejected
            raise Rejected("; ".join(receipt.reasons) or "sudofx rejected WAKE reset")
        return self.load()

    def append(self, kind, payload, crash=False):
        if crash:
            self._kernel_store.crash_next_write = True
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
        generation = migration.get("active_generation", 0)
        if generation:
            seq = 0
            head = "0" * 64
        else:
            seq = migration["import_legacy_event_count"]
            head = migration["import_legacy_head"]

        result = []
        active = generation == 0
        current_generation = 0
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
            action = value.get("action")
            if action == "reset_to_zero":
                current_generation += 1
                active = current_generation == generation
                if active:
                    seq = 0
                    head = "0" * 64
                    result = []
                continue
            if action != "append_legacy_event" or not active:
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
            raise IntegrityError(
                "sudofx WAKE active event projection does not match durable generation head"
            )
        return result

    def _baseline(self):
        baseline = self._envelope()["migration"].get("history_baseline")
        return baseline if isinstance(baseline, dict) else {}

    def events(self):
        """Return the complete event history for the active WAKE generation."""
        migration = self._envelope()["migration"]
        if migration.get("active_generation", 0):
            return self._post_migration_events()
        return [*self._archived_legacy_events(), *self._post_migration_events()]

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

    def history_metrics(self):
        """Derive complete metrics from exact history stored in the sudofx database."""
        return history_metrics(self.events(), self.load())

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
