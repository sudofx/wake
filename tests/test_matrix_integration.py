from __future__ import annotations

import tempfile
from pathlib import Path
import unittest

from sudofx import continuity_matrix
from sudofx.storage import ApplicationAccessError

from wake.governance import Rejected
from wake.live import _application_access_metrics, _matrix_metrics
from wake.sudofx_store import SudofxStore


class WakeMatrixIntegrationTests(unittest.TestCase):
    def test_matrix_is_opt_in_and_reconstructs_from_authoritative_sqlite(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            store = SudofxStore(root, initialize_empty=True)
            self.assertIsNone(store.continuity_matrix_progress())

            enabled = store.enable_continuity_matrix()
            self.assertEqual(enabled["matrix"], "continuity@1")
            self.assertEqual(enabled["cell_count"], 343)
            self.assertEqual(enabled["completed_count"], 0)

            first = matrix.coordinate("reconstruction", "rich", "clean")
            progressed = store.record_continuity_matrix_result(
                first.coordinate_id,
                {
                    "status": "completed",
                    "score": 1.0,
                    "summary": "WAKE reconstruction cell passed.",
                },
            )
            self.assertEqual(progressed["completed_count"], 1)
            self.assertEqual(
                progressed["completed_coordinate_ids"],
                [first.coordinate_id],
            )
            self.assertNotEqual(progressed["next_coordinate_id"], first.coordinate_id)
            before_revision = store.kernel.context().revision
            store.close()

            rebuilt = SudofxStore(root)
            try:
                restored = rebuilt.continuity_matrix_progress()
                self.assertEqual(restored, progressed)
                self.assertGreaterEqual(rebuilt.kernel.context().revision, before_revision)
                self.assertEqual(
                    restored["definition_digest"],
                    matrix.definition_digest,
                )
            finally:
                rebuilt.close()

    def test_public_matrix_metrics_expose_definition_before_enablement(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            store = SudofxStore(Path(tempdir), initialize_empty=True)
            try:
                public = _matrix_metrics(store)
                self.assertFalse(public["enabled"])
                self.assertEqual(public["matrix"], "continuity@1")
                self.assertEqual(public["cell_count"], 343)
                self.assertEqual(len(public["cells"]), 343)
                self.assertEqual(public["completed_count"], 0)
                self.assertTrue(all(status == "open" for status in public["cells"]))
            finally:
                store.close()

    def test_public_matrix_metrics_are_bounded(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            store = SudofxStore(Path(tempdir), initialize_empty=True)
            try:
                store.enable_continuity_matrix()
                first = matrix.coordinate("reconstruction", "rich", "clean")
                store.record_continuity_matrix_result(
                    first.coordinate_id,
                    {
                        "status": "completed",
                        "score": 1.0,
                        "summary": "This result body should not enter public telemetry.",
                    },
                )
                public = _matrix_metrics(store)
                self.assertEqual(public["completed_count"], 1)
                self.assertEqual(public["status_counts"]["completed"], 1)
                self.assertEqual([axis["key"] for axis in public["axes"]], ["semantic_lens", "exposure", "pressure"])
                self.assertEqual(len(public["cells"]), 343)
                self.assertEqual(public["cells"][first.ordinal - 1], "completed")
                self.assertEqual(public["next_ordinal"], 2)
                self.assertNotIn("results", public)
                self.assertNotIn("completed_coordinate_ids", public)
                self.assertNotIn("summary", str(public))
                self.assertNotIn("score", str(public))
            finally:
                store.close()

    def test_public_matrix_geometry_matches_shared_row_major_contract(self) -> None:
        matrix = continuity_matrix()
        self.assertEqual(matrix.coordinate("reconstruction", "rich", "clean").ordinal, 1)
        self.assertEqual(matrix.coordinate("reconstruction", "rich", "stale-frontier").ordinal, 2)
        self.assertEqual(matrix.coordinate("reconstruction", "milestones-only", "clean").ordinal, 8)
        self.assertEqual(matrix.coordinate("milestone-dropout", "rich", "clean").ordinal, 50)
        self.assertEqual(
            matrix.coordinate(
                "adversarial-integrity",
                "digests-without-counts",
                "compound-adversarial",
            ).ordinal,
            343,
        )

    def test_matrix_coordinate_version_is_validated_by_shared_contract(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            store = SudofxStore(Path(tempdir), initialize_empty=True)
            try:
                store.enable_continuity_matrix()
                first = matrix.coordinate("reconstruction", "rich", "clean")
                wrong_version = first.coordinate_id.replace("continuity@1:", "continuity@2:", 1)
                with self.assertRaises(Rejected):
                    store.record_continuity_matrix_result(
                        wrong_version,
                        {"status": "completed", "score": 1.0},
                    )
                self.assertEqual(
                    store.continuity_matrix_progress()["completed_count"],
                    0,
                )
            finally:
                store.close()

    def test_public_application_access_metrics_follow_global_latch(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            store = SudofxStore(Path(tempdir), initialize_empty=True)
            try:
                initial = _application_access_metrics(store)
                self.assertTrue(initial["enabled"])
                stopped = store.record.set_application_access(
                    False,
                    actor="operator",
                    reason="public projection test",
                )
                projected = _application_access_metrics(store)
                self.assertFalse(projected["enabled"])
                self.assertEqual(projected["generation"], stopped.generation)
                self.assertEqual(projected["changed_at"], stopped.changed_at)
                self.assertNotIn("actor", projected)
                self.assertNotIn("reason", projected)
            finally:
                store.close()

    def test_matrix_actions_honor_global_sudofx_kill_switch(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            store = SudofxStore(Path(tempdir), initialize_empty=True)
            try:
                stopped = store.record.set_application_access(
                    False,
                    actor="operator",
                    reason="matrix boundary regression test",
                )
                self.assertFalse(stopped.enabled)
                with self.assertRaises(ApplicationAccessError):
                    store.enable_continuity_matrix()
                self.assertIsNone(store.continuity_matrix_progress())
            finally:
                store.close()

    def test_existing_wake_reset_preserves_opted_in_matrix_state(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            store = SudofxStore(Path(tempdir), initialize_empty=True)
            try:
                store.enable_continuity_matrix()
                first = matrix.coordinate("reconstruction", "rich", "clean")
                store.record_continuity_matrix_result(
                    first.coordinate_id,
                    {"status": "completed", "score": 0.75},
                )
                before = store.continuity_matrix_progress()
                reset_state = store.reset()
                self.assertEqual(reset_state["version"], 0)
                self.assertEqual(store.continuity_matrix_progress(), before)
            finally:
                store.close()


if __name__ == "__main__":
    unittest.main()
