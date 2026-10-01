"""Phase E migration evidence: WAKE domain meaning crosses into sudofx without cutover."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from sudofx import ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel, SubmissionProvenance
from sudofx.governance import Governance
from sudofx.record import Record

from wake.engine import DEFAULTS, Engine
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


if __name__ == "__main__":
    unittest.main()
