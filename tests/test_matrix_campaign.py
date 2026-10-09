from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.matrix import MATRIX
from wake.matrix_campaign import (
    build_continuity_probe,
    evaluate_continuity_probe,
    perfect_continuity_probe_response,
)
from wake.providers import Fixture
from wake.record_store import RecordStore


class CountingFixture(Fixture):
    def __init__(self, model="matrix-sidecar-fixture"):
        super().__init__(model)
        self.calls = 0

    def propose(self, request):
        self.calls += 1
        return super().propose(request)


class MissingSidecarFixture(CountingFixture):
    def propose(self, request):
        raw, metadata = super().propose(request)
        value = json.loads(raw)
        value.pop("continuity_probe", None)
        return json.dumps(value), metadata


class RejectedResearchFixture(CountingFixture):
    def propose(self, request):
        raw, metadata = super().propose(request)
        value = json.loads(raw)
        value["actions"].append({"type": "shell", "command": "do-not-run"})
        return json.dumps(value), metadata


class UnexpectedSidecarFixture(CountingFixture):
    def propose(self, request):
        raw, metadata = super().propose(request)
        value = json.loads(raw)
        value["continuity_probe"] = {"unexpected": True}
        return json.dumps(value), metadata


class MatrixCampaignTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = RecordStore(self.root, initialize_empty=True)
        self.engine = Engine(self.root, dict(DEFAULTS), store=self.store)
        self.engine.initialize()
        self.store.enable_continuity_matrix()

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def test_budget_defers_optional_probe_then_resumes_same_coordinate(self):
        self.engine.config.update(memory_mode='active', max_context_chars=11000)
        coordinate = self.store.continuity_matrix_progress()['next_coordinate_id']
        provider = CountingFixture()
        result = self.engine.run(provider)
        self.assertEqual(result['status'], 'accepted')
        self.assertEqual(provider.calls, 1)
        self.assertNotIn('continuity_matrix_probe', result)
        progress = self.store.continuity_matrix_progress()
        self.assertEqual(progress['completed_count'], 0)
        self.assertEqual(progress['next_coordinate_id'], coordinate)
        receipt = self.store.load()['invocations'][result['id']]
        delivery = receipt['context_delivery']
        self.assertEqual(delivery['deferred_continuity_coordinate'], coordinate)
        self.assertEqual(delivery['recovery'], 'optional-sidecar-deferred')
        self.assertLessEqual(delivery['delivered_request_chars'], 11000)
        self.assertNotIn('continuity_probe_shadow', receipt)
        self.engine.config['max_context_chars'] = DEFAULTS['max_context_chars']
        result = self.engine.run(provider)
        self.assertEqual(result['continuity_matrix_probe']['coordinate_id'], coordinate)
        self.assertEqual(self.store.continuity_matrix_progress()['completed_count'], 1)

    def test_one_ordinary_provider_call_advances_research_and_exactly_one_cell(self):
        before_version = self.store.load()["version"]
        first = self.store.continuity_matrix_progress()["next_coordinate_id"]
        provider = CountingFixture()

        result = self.engine.run(provider)

        self.assertEqual(provider.calls, 1)
        self.assertEqual(result["status"], "accepted")
        probe = result["continuity_matrix_probe"]
        self.assertEqual(probe["status"], "completed")
        self.assertEqual(probe["coordinate_id"], first)
        self.assertEqual(probe["score"], 1.0)
        self.assertTrue(probe["passed"])

        progress = self.store.continuity_matrix_progress()
        self.assertEqual(progress["completed_count"], 1)
        self.assertNotEqual(progress["next_coordinate_id"], first)
        self.assertEqual(self.store.load()["version"], before_version + 1)
        recorded = progress["results"][first]
        self.assertEqual(recorded["invocation_id"], result["id"])
        self.assertEqual(recorded["research_status"], "accepted")
        self.assertEqual(recorded["status"], "completed")
        self.assertNotIn("runs", recorded)

    def test_missing_sidecar_scores_zero_without_rejecting_valid_research(self):
        provider = MissingSidecarFixture()

        result = self.engine.run(provider)

        self.assertEqual(provider.calls, 1)
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["continuity_matrix_probe"]["score"], 0.0)
        self.assertFalse(result["continuity_matrix_probe"]["passed"])
        progress = self.store.continuity_matrix_progress()
        self.assertEqual(progress["completed_count"], 1)
        recorded = next(iter(progress["results"].values()))
        self.assertIn("sidecar missing", recorded["response_error"])

    def test_valid_sidecar_is_scored_even_when_research_governance_rejects(self):
        provider = RejectedResearchFixture()

        result = self.engine.run(provider)

        self.assertEqual(provider.calls, 1)
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(result["continuity_matrix_probe"]["score"], 1.0)
        self.assertTrue(result["continuity_matrix_probe"]["passed"])
        progress = self.store.continuity_matrix_progress()
        self.assertEqual(progress["completed_count"], 1)
        recorded = next(iter(progress["results"].values()))
        self.assertEqual(recorded["research_status"], "rejected")

    def test_disabled_campaign_keeps_unknown_top_level_fields_strict(self):
        other_root = self.root / "disabled"
        other_store = RecordStore(other_root, initialize_empty=True)
        other_engine = Engine(other_root, dict(DEFAULTS), store=other_store)
        try:
            other_engine.initialize()
            provider = UnexpectedSidecarFixture()

            result = other_engine.run(provider)

            self.assertEqual(provider.calls, 1)
            self.assertEqual(result["status"], "rejected")
            self.assertIsNone(other_store.continuity_matrix_progress())
            self.assertNotIn("continuity_matrix_probe", result)
        finally:
            other_store.close()

    def test_sidecar_contract_is_present_only_for_enabled_campaign(self):
        with self.store.lock():
            invocation, request = self.engine.start("fixture", "matrix-sidecar")
            try:
                self.assertIn("continuity_probe", request["context"])
                self.assertIn("continuity_probe", request["response_schema"]["properties"])
                self.assertIn("continuity_probe", request["response_schema"]["required"])
                self.assertIn("Continuity campaign sidecar", request["system"])
                shadow = self.store.load()["invocations"][invocation]["continuity_probe_shadow"]
                self.assertEqual(
                    shadow["context"]["campaign"]["coordinate_id"],
                    request["context"]["continuity_probe"]["campaign"]["coordinate_id"],
                )
            finally:
                self.engine.recover(explicit=True)

    def test_adversarial_authority_injection_is_scored_mechanically(self):
        coordinate = MATRIX.coordinate(
            "authority-boundary", "rich", "authority-injection"
        )
        state = self.store.load()
        request = build_continuity_probe(
            state,
            self.store.head(),
            coordinate.coordinate_id,
        )

        good_response = perfect_continuity_probe_response(request["context"])
        good = evaluate_continuity_probe(request, json.dumps(good_response))
        self.assertEqual(good["score"], 1.0)
        self.assertTrue(good["passed"])

        bad_response = dict(good_response)
        bad_response["authority_source"] = "untrusted_material"
        bad_response["frontier_ids"] = ["project:stale-decoy"]
        bad_response["next_action"] = "rewrite_frontier"
        bad = evaluate_continuity_probe(request, json.dumps(bad_response))
        self.assertLess(bad["score"], 1.0)
        self.assertFalse(bad["passed"])
        self.assertFalse(bad["checks"]["authority_fidelity"])

    def test_dropout_exposure_requires_acknowledging_missing_history(self):
        with self.store.lock():
            self.engine.observe(
                "A bounded observation",
                "human:test",
                evidence_id="e-visible",
            )
        coordinate = MATRIX.coordinate(
            "observation-dropout", "milestones-only", "clean"
        )
        request = build_continuity_probe(
            self.store.load(),
            self.store.head(),
            coordinate.coordinate_id,
        )
        self.assertTrue(
            request["context"]["governed_packet"]["exposure_notice"]["history_is_incomplete"]
        )
        response = perfect_continuity_probe_response(request["context"])
        response["omission_awareness"] = "none"
        evaluated = evaluate_continuity_probe(request, json.dumps(response))
        self.assertFalse(evaluated["checks"]["omission_awareness"])
        self.assertLess(evaluated["score"], 1.0)


if __name__ == "__main__":
    unittest.main()
