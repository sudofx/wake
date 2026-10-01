"""Phase E migration evidence: WAKE domain meaning crosses into sudofx without cutover."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from sudofx import ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel, SubmissionProvenance
from sudofx.governance import Governance
from sudofx.record import Record

from wake.engine import DEFAULTS, Engine
from wake.governance import Rejected, transition
from wake.sudofx_application import WAKE_APPLICATION, verified_legacy_snapshot


class SudofxMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root / "wake-data", dict(DEFAULTS))
        with self.engine.store.lock():
            self.engine.initialize()

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def _sudofx_host(self):
        registry = ApplicationRegistry((WAKE_APPLICATION,))
        record = Record(self.root / "sudofx.sqlite")
        kernel = Kernel(record, Governance(application_registry=registry))
        return kernel, ApplicationHost(kernel, registry, "wake")

    def test_verified_legacy_state_imports_once_and_survives_application_removal(self):
        """Verified WAKE replay should become one replayable sudofx application state."""
        payload = verified_legacy_snapshot(self.engine.store)
        legacy_state, legacy_head, events = self.engine.store.replay_record()
        kernel, host = self._sudofx_host()

        receipt = host.submit(
            ApplicationIntent("wake-import", 0, "import_legacy_snapshot", payload),
            provenance=SubmissionProvenance(
                "application",
                "wake-migration",
                "verified-legacy-replay",
            ),
        )
        self.assertEqual(receipt.status, "accepted")
        imported = host.context().state
        self.assertEqual(imported["state"], legacy_state)
        self.assertEqual(imported["migration"]["legacy_head"], legacy_head)
        self.assertEqual(imported["migration"]["legacy_event_count"], len(events))
        self.assertEqual(imported["migration"]["legacy_version"], legacy_state["version"])

        # Removing WAKE application code must not break generic sudofx replay.
        replayed = Kernel(Record(self.root / "sudofx.sqlite")).context().state["app:wake"]
        self.assertEqual(replayed["state"]["state"], legacy_state)
        self.assertEqual(replayed["state"]["migration"]["legacy_head"], legacy_head)

        duplicate = host.submit(
            ApplicationIntent("wake-import-again", 1, "import_legacy_snapshot", payload)
        )
        self.assertEqual(duplicate.status, "rejected")
        self.assertIn("already imported", " ".join(duplicate.reasons))

    def test_import_rejects_tampered_replay_state_digest(self):
        """Migration provenance must bind the imported state bytes it describes."""
        payload = verified_legacy_snapshot(self.engine.store)
        payload["legacy_state"] = {**payload["legacy_state"], "focus": "tampered"}
        _, host = self._sudofx_host()
        receipt = host.submit(
            ApplicationIntent("wake-import-tampered", 0, "import_legacy_snapshot", payload)
        )
        self.assertEqual(receipt.status, "rejected")
        self.assertIn("digest does not match", " ".join(receipt.reasons))

    def test_governed_proposal_matches_legacy_transition_exactly(self):
        """WAKE policy stays above the kernel while sudofx owns the accepted state."""
        payload = verified_legacy_snapshot(self.engine.store)
        _, host = self._sudofx_host()
        imported = host.submit(
            ApplicationIntent("wake-import-equivalence", 0, "import_legacy_snapshot", payload)
        )
        self.assertEqual(imported.status, "accepted")
        legacy_state = payload["legacy_state"]
        proposal = {
            "base_version": legacy_state["version"],
            "title": "Preserve a governed obligation",
            "summary": "Exercise existing WAKE commitment governance through the sudofx app seam.",
            "actions": [
                {
                    "type": "commit",
                    "id": "phase-e-equivalence",
                    "task": "Continue the migration with behavioral equivalence evidence.",
                    "due_cycle": legacy_state["version"] + 3,
                    "reason": "Keep the next migration step durable across process replacement.",
                }
            ],
        }
        expected = transition(legacy_state, proposal, "phase-e-equivalence")

        receipt = host.submit(
            ApplicationIntent(
                "wake-governed-equivalence",
                1,
                "apply_governed_proposal",
                {"invocation": "phase-e-equivalence", "proposal": proposal},
            ),
            provenance=SubmissionProvenance(
                "application", "wake-migration", "behavioral-equivalence"
            ),
        )
        self.assertEqual(receipt.status, "accepted")
        self.assertEqual(host.context().state["state"], expected)
        self.assertEqual(
            host.context().state["state"]["commitments"]["phase-e-equivalence"]["task"],
            "Continue the migration with behavioral equivalence evidence.",
        )

    def test_governed_proposal_rejects_exact_legacy_stale_write(self):
        """A legacy WAKE rejection must stay a rejection at the sudofx authority boundary."""
        payload = verified_legacy_snapshot(self.engine.store)
        _, host = self._sudofx_host()
        host.submit(ApplicationIntent("wake-import-stale", 0, "import_legacy_snapshot", payload))
        stale = {
            "base_version": payload["legacy_state"]["version"] - 1,
            "title": "Stale proposal",
            "summary": "This must fail the same WAKE optimistic-concurrency rule.",
            "actions": [],
        }
        with self.assertRaisesRegex(Rejected, "Stale or invalid base_version"):
            transition(payload["legacy_state"], stale, "stale-legacy")

        receipt = host.submit(
            ApplicationIntent(
                "wake-governed-stale",
                1,
                "apply_governed_proposal",
                {"invocation": "stale-app", "proposal": stale},
            )
        )
        self.assertEqual(receipt.status, "rejected")
        self.assertIn("Stale or invalid base_version", " ".join(receipt.reasons))
        self.assertEqual(host.context().state["state"], payload["legacy_state"])


if __name__ == "__main__":
    unittest.main()
