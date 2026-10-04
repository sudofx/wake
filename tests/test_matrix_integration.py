from __future__ import annotations

import tempfile
from pathlib import Path
import unittest

from sudofx import continuity_matrix
from sudofx.storage import ApplicationAccessError

from wake.governance import Rejected
from wake.live import build_live_projection
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

    def test_live_projection_exposes_matrix_progress_as_derived_data(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            store = SudofxStore(Path(tempdir), initialize_empty=True)
            try:
                self.assertIsNone(build_live_projection(store)["matrix_progress"])
                store.enable_continuity_matrix()
                first = matrix.coordinate("reconstruction", "rich", "clean")
                store.record_continuity_matrix_result(
                    first.coordinate_id,
                    {"status": "completed", "score": 1.0},
                )
                projection = build_live_projection(store)
                self.assertFalse(projection["authoritative"])
                self.assertEqual(projection["matrix_progress"]["completed_count"], 1)
                self.assertEqual(projection["matrix_progress"]["cell_count"], 343)
            finally:
                store.close()

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
