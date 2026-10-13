from __future__ import annotations

import tempfile
from pathlib import Path
import unittest

from wake.kernel import continuity_matrix
from wake.kernel.storage import ApplicationAccessError

from wake.governance import Rejected
from wake.record_store import RecordStore


class WakeMatrixIntegrationTests(unittest.TestCase):
    def test_matrix_is_opt_in_and_reconstructs_from_authoritative_sqlite(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            store = RecordStore(root, initialize_empty=True)
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

            rebuilt = RecordStore(root)
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

    def test_matrix_coordinate_version_is_validated_by_shared_contract(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            store = RecordStore(Path(tempdir), initialize_empty=True)
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

    def test_matrix_actions_honor_global_wake_kill_switch(self) -> None:
        with tempfile.TemporaryDirectory() as tempdir:
            store = RecordStore(Path(tempdir), initialize_empty=True)
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

    def test_existing_wake_reset_atomically_enables_fresh_campaign(self) -> None:
        matrix = continuity_matrix()
        with tempfile.TemporaryDirectory() as tempdir:
            store = RecordStore(Path(tempdir), initialize_empty=True)
            try:
                store.enable_continuity_matrix()
                first = matrix.coordinate("reconstruction", "rich", "clean")
                store.record_continuity_matrix_result(
                    first.coordinate_id,
                    {"status": "completed", "score": 0.75},
                )
                before = store.continuity_matrix_progress()
                history = store.record.history()
                reset_state = store.reset()
                self.assertEqual(reset_state["version"], 0)
                self.assertEqual(before["completed_count"], 1)
                self.assertEqual(store.record.history()[:-1], history)
                enabled = store.continuity_matrix_progress()
                self.assertEqual(enabled["completed_count"], 0)
                self.assertEqual(enabled["results"], {})
                store.audit()
            finally:
                store.close()


    def test_reset_rejection_preserves_previous_campaign_and_state(self):
        from unittest.mock import patch
        from wake.kernel import ApplicationDecision
        with tempfile.TemporaryDirectory() as folder:
            store = RecordStore(Path(folder), initialize_empty=True)
            try:
                store.enable_continuity_matrix()
                before = store.load()
                campaign = store.continuity_matrix_progress()
                with patch('wake.application.enable_continuity_matrix',
                           return_value=ApplicationDecision(False, reasons=('campaign rejected',))):
                    with self.assertRaises(Rejected): store.reset()
                self.assertEqual(store.load(), before)
                self.assertEqual(store.continuity_matrix_progress(), campaign)
                store.audit()
            finally:
                store.close()


if __name__ == "__main__":
    unittest.main()

class FairMatrixReportingTests(unittest.TestCase):
    def test_invalid_answer_is_not_a_fact_failure_and_columns_stay_contiguous(self):
        from wake.matrix import MATRIX, MATRIX_KEY, continuity_matrix_progress
        first = next(iter(MATRIX.coordinates()))
        envelope = {'extensions': {MATRIX_KEY: {'results': {first.coordinate_id: {'status': 'completed', 'score': 0, 'passed': False, 'checks': {'source_fidelity': False}, 'response_error': 'Missing probe'}}}}}
        before = envelope['extensions'][MATRIX_KEY]['results'][first.coordinate_id].copy()
        progress = continuity_matrix_progress(envelope)
        self.assertEqual(progress['invalid_response_count'], 1)
        self.assertEqual(progress['graded_failed_count'], 0)
        self.assertEqual(progress['failure_counts'], {})
        second = MATRIX.coordinate_by_id(progress['next_coordinate_id'])
        self.assertEqual(second.value_keys[:2], first.value_keys[:2])
        self.assertEqual(second.ordinal, first.ordinal + 1)
        self.assertEqual(envelope['extensions'][MATRIX_KEY]['results'][first.coordinate_id], before)

    def test_column_traversal_finishes_columns_and_skips_existing_results(self):
        from wake.matrix import MATRIX, MATRIX_KEY, continuity_matrix_progress
        coordinates = list(MATRIX.coordinates())
        results = {}
        envelope = {'extensions': {MATRIX_KEY: {'results': results}}}
        for cell in coordinates:
            progress = continuity_matrix_progress(envelope)
            self.assertEqual(progress['next_coordinate_id'], cell.coordinate_id)
            results[cell.coordinate_id] = {'status': 'completed', 'score': 1, 'passed': True}
        self.assertIsNone(continuity_matrix_progress(envelope)['next_coordinate_id'])
        del results[coordinates[11].coordinate_id]
        before = {key: dict(value) for key, value in results.items()}
        self.assertEqual(continuity_matrix_progress(envelope)['next_coordinate_id'], coordinates[11].coordinate_id)
        self.assertEqual(results, before)
