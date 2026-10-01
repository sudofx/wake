"""Phase E migration evidence: WAKE domain meaning crosses into sudofx without cutover."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from sudofx import ApplicationHost, ApplicationIntent, ApplicationRegistry, Kernel, SubmissionProvenance
from sudofx.governance import Governance
from sudofx.record import Record

from wake.engine import DEFAULTS, Engine, govern_proposal
from wake.governance import Rejected, transition
from wake.store import digest, reduce_event
from wake.sudofx_store import SudofxStore
from wake.providers import Fixture
from wake.live import build_live_projection
from wake.report import export
from wake.sudofx_application import WAKE_APPLICATION, verified_legacy_snapshot
from support import charter_settings


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
        # Compact mode preserves the action envelope without pretending the
        # domain state can be interpreted when WAKE code is absent.
        replayed = Kernel(Record(self.root / "sudofx.sqlite")).context().state["app:wake"]
        self.assertEqual(replayed["storage"], "event_log")
        self.assertEqual(len(replayed["events"]), 1)
        self.assertNotIn("state", replayed)

        registry = ApplicationRegistry((WAKE_APPLICATION,))
        reinstalled_kernel = Kernel(
            Record(self.root / "sudofx.sqlite"),
            Governance(application_registry=registry),
        )
        reinstalled = ApplicationHost(
            reinstalled_kernel,
            registry,
            "wake",
        ).context().state
        self.assertEqual(reinstalled["state"], legacy_state)
        self.assertEqual(reinstalled["migration"]["legacy_head"], legacy_head)

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
        durable = host.kernel.context().state["app:wake"]
        self.assertEqual(durable["storage"], "event_log")
        self.assertEqual(len(durable["events"]), 2)
        value = host.kernel.record.history()[-1]["proposal"]["operations"][0]["value"]
        self.assertNotIn("next_state", value)
        self.assertEqual(len(value["result_digest"]), 64)
        self.assertEqual(
            host.context().state["state"]["commitments"]["phase-e-equivalence"]["task"],
            "Continue the migration with behavioral equivalence evidence.",
        )

    def test_sudofx_app_reuses_full_wake_policy_including_research_id_assignment(self):
        """Policy outside raw transition must remain identical during migration."""
        research_engine = Engine(
            self.root / "wake-research",
            charter_settings("Exercise full WAKE application policy through sudofx."),
        )
        try:
            with research_engine.store.lock():
                research_engine.initialize()
            payload = verified_legacy_snapshot(research_engine.store)
            _, host = self._sudofx_host()
            imported = host.submit(
                ApplicationIntent("wake-import-full-policy", 0, "import_legacy_snapshot", payload)
            )
            self.assertEqual(imported.status, "accepted")

            proposal = {
                "base_version": payload["legacy_state"]["version"],
                "title": "Open one bounded research request",
                "summary": "Prove WAKE-owned normalization remains above the sudofx kernel.",
                "actions": [
                    {
                        "type": "project",
                        "id": "phase-e-project",
                        "title": "Entropy comparison",
                        "question": "What distinguishes major entropy definitions?",
                        "domain": "entropy",
                        "status": "active",
                        "next_step": "Collect one bounded source set",
                        "reason": "Exercise the existing WAKE research policy.",
                    },
                    {
                        "type": "research",
                        "project": "phase-e-project",
                        "query": "major entropy definitions comparison",
                        "domain": "entropy",
                        "reason": "Gather evidence for the bounded comparison.",
                    },
                ],
            }
            normalized, expected, _, _ = govern_proposal(
                payload["legacy_state"], "app-policy", proposal
            )
            expected_research_id = "research-app-policy-2"
            self.assertEqual(normalized["actions"][1]["id"], expected_research_id)

            receipt = host.submit(
                ApplicationIntent(
                    "wake-full-policy-equivalence",
                    1,
                    "apply_governed_proposal",
                    {"invocation": "app-policy", "proposal": proposal},
                )
            )
            self.assertEqual(receipt.status, "accepted")
            migrated_state = host.context().state["state"]
            self.assertEqual(migrated_state, expected)
            self.assertIn(expected_research_id, migrated_state["research"])
            self.assertEqual(
                migrated_state["research"][expected_research_id]["project"],
                "phase-e-project",
            )
        finally:
            research_engine.store.close()

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


    def test_sudofx_authoritative_event_path_matches_legacy_invocation_transition(self) -> None:
        """A WAKE invocation can advance through sudofx without writing the legacy Store."""
        payload = verified_legacy_snapshot(self.engine.store)
        _, host = self._sudofx_host()
        imported = host.submit(
            ApplicationIntent("wake-event-import", 0, "import_legacy_snapshot", payload)
        )
        self.assertEqual(imported.status, "accepted")

        invocation = "phase-e-native-event"
        start_payload = {
            "id": invocation,
            "provider": "fixture",
            "model": "fixture",
            "charged": False,
            "quota_day": "2026-10-01",
            "base_version": payload["legacy_state"]["version"],
            "request": {"bounded": True},
        }
        started = host.submit(
            ApplicationIntent(
                "wake-event-start",
                1,
                "append_legacy_event",
                {
                    "kind": "invocation_started",
                    "payload": start_payload,
                    "time": "2026-10-01T19:20:00+00:00",
                },
            )
        )
        self.assertEqual(started.status, "accepted")
        started_envelope = host.context().state
        started_state = started_envelope["state"]
        self.assertEqual(started_state["pending"], invocation)
        self.assertEqual(started_state["invocations"][invocation]["status"], "pending")

        proposal = {
            "base_version": started_state["version"],
            "title": "Advance under sudofx authority",
            "summary": "Exercise WAKE policy while sudofx owns the durable event.",
            "actions": [
                {
                    "type": "commit",
                    "id": "phase-e-native-authority",
                    "task": "Preserve the migration boundary evidence.",
                    "due_cycle": started_state["version"] + 3,
                    "reason": "Prove the compatibility path before live cutover.",
                }
            ],
        }
        normalized, governed_state, editorial, rotation_filter = govern_proposal(
            started_state, invocation, proposal
        )
        self.assertIsNone(editorial)
        self.assertIsNone(rotation_filter)
        fields = ["version", "beliefs", "commitments", "journal"]
        accepted_payload = {
            "id": invocation,
            "proposal": normalized,
            "raw_response": "fixture",
            "metadata": {},
            "result_hash": digest({key: governed_state[key] for key in fields}),
            "hash_fields": fields,
        }

        accepted = host.submit(
            ApplicationIntent(
                "wake-event-accepted",
                2,
                "append_legacy_event",
                {
                    "kind": "accepted",
                    "payload": accepted_payload,
                    "time": "2026-10-01T19:20:01+00:00",
                },
            )
        )
        self.assertEqual(accepted.status, "accepted")
        final_envelope = host.context().state

        expected_event = {
            "seq": started_envelope["migration"]["legacy_event_count"] + 1,
            "time": "2026-10-01T19:20:01+00:00",
            "kind": "accepted",
            "payload": accepted_payload,
            "prev_hash": started_envelope["migration"]["legacy_head"],
        }
        expected_event["hash"] = digest(expected_event)
        expected_state = reduce_event(started_state, expected_event)

        self.assertEqual(final_envelope["state"], expected_state)
        self.assertEqual(final_envelope["state"]["pending"], None)
        self.assertEqual(
            final_envelope["state"]["invocations"][invocation]["status"],
            "accepted",
        )
        self.assertEqual(
            final_envelope["state"]["commitments"]["phase-e-native-authority"]["task"],
            "Preserve the migration boundary evidence.",
        )
        self.assertEqual(
            final_envelope["migration"]["legacy_head"],
            expected_event["hash"],
        )
        self.assertEqual(
            final_envelope["migration"]["legacy_event_count"],
            payload["legacy_event_count"] + 2,
        )


    def test_full_wake_fixture_cycle_writes_only_to_sudofx_after_migration(self) -> None:
        """Normal WAKE orchestration can advance while the legacy database stays frozen."""
        legacy_before_state, legacy_before_head, legacy_before_events = self.engine.store.replay_record()
        legacy_count = len(legacy_before_events)

        store = SudofxStore(
            self.root / "sudofx-authority",
            legacy_store=self.engine.store,
        )
        migrated = Engine(
            self.root / "unused-legacy-path",
            dict(DEFAULTS),
            store=store,
        )
        try:
            result = migrated.run(Fixture("phase-e-sudofx-authority"))
            self.assertEqual(result["status"], "accepted")

            legacy_after_state, legacy_after_head, legacy_after_events = self.engine.store.replay_record()
            self.assertEqual(len(legacy_after_events), legacy_count)
            self.assertEqual(legacy_after_head, legacy_before_head)
            self.assertEqual(legacy_after_state, legacy_before_state)

            migrated_state = store.load()
            self.assertEqual(migrated_state["version"], legacy_before_state["version"] + 1)
            self.assertIsNone(migrated_state["pending"])
            self.assertTrue(
                any(
                    item.get("status") == "accepted"
                    for item in migrated_state["invocations"].values()
                )
            )
            self.assertGreater(
                store._envelope()["migration"]["legacy_event_count"],
                legacy_count,
            )
            self.assertGreater(store.kernel.context().revision, 1)

            projection = build_live_projection(
                store,
                operation={"status": result["status"]},
                runtime_ref="phase-e-sudofx-test",
            )
            self.assertEqual(projection["source"]["authority"], "sudofx SQLite")
            self.assertEqual(projection["source"]["database"], "sudofx.sqlite")
            self.assertEqual(projection["state"]["version"], migrated_state["version"])
            self.assertEqual(
                projection["metrics"]["storage"]["event_count"],
                len(store.events()),
            )

            export(store, self.root / "sudofx-site")
            self.assertTrue((self.root / "sudofx-site" / "index.html").is_file())
            self.assertTrue((self.root / "sudofx-site" / "events.md").is_file())

            legacy_export_state, legacy_export_head, legacy_export_events = (
                self.engine.store.replay_record()
            )
            self.assertEqual(legacy_export_state, legacy_before_state)
            self.assertEqual(legacy_export_head, legacy_before_head)
            self.assertEqual(len(legacy_export_events), legacy_count)

            fresh = SudofxStore(
                self.root / "sudofx-authority",
                legacy_store=self.engine.store,
            )
            try:
                self.assertEqual(fresh.load(), migrated_state)
                self.assertEqual(fresh.head(), store.head())
                self.assertEqual(
                    len(fresh.events()),
                    fresh._envelope()["migration"]["legacy_event_count"],
                )
            finally:
                fresh.close()
        finally:
            store.close()


if __name__ == "__main__":
    unittest.main()
