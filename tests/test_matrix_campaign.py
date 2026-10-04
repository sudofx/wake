from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.matrix import MATRIX
from wake.matrix_campaign import (
    build_continuity_probe,
    continuity_provider_usage,
    evaluate_continuity_probe,
    run_continuity_matrix_probe,
)
from wake.sudofx_store import SudofxStore


def correct_response(request):
    packet = request["context"]["governed_packet"]
    return {
        "coordinate_id": request["context"]["campaign"]["coordinate_id"],
        "authority_source": "governed_packet",
        "objective_anchor": packet["objective_anchor"],
        "frontier_ids": list(packet["frontier_ids"]),
        "milestone_anchors": list(packet["milestone_anchors"]),
        "observation_ids": [item["id"] for item in packet["observations"]],
        "provenance": [
            {"id": item["id"], "source": item["source"]}
            for item in packet["observations"]
        ],
        "omission_awareness": (
            "acknowledged"
            if packet["exposure_notice"]["history_is_incomplete"]
            else "none"
        ),
        "digest_interpretation": "opaque_anchor",
        "next_action": "preserve_frontier",
        "summary": "Continue only from the governed packet and preserve the recorded frontier.",
    }


class MatrixFixture:
    name = "fixture"
    model = "matrix-fixture"
    models = ["matrix-fixture"]
    charged = False

    def __init__(self):
        self.request_limit = 1

    def propose(self, request):
        return json.dumps(correct_response(request)), {
            "provider_requests_sent": 0,
            "provider_attempts": [],
            "successful_model": self.model,
            "model_version": self.model,
        }


class MatrixCampaignTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.store = SudofxStore(self.root, initialize_empty=True)
        self.engine = Engine(self.root, dict(DEFAULTS), store=self.store)
        self.engine.initialize()
        self.store.enable_continuity_matrix()

    def tearDown(self):
        self.store.close()
        self.temp.cleanup()

    def test_one_probe_completes_exactly_one_cell_without_research_transition(self):
        before = self.store.load()["version"]
        progress = self.store.continuity_matrix_progress()
        first = progress["next_coordinate_id"]

        result = run_continuity_matrix_probe(
            self.store,
            MatrixFixture(),
            dict(DEFAULTS),
        )

        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["coordinate_id"], first)
        self.assertEqual(result["score"], 1.0)
        self.assertTrue(result["passed"])
        updated = self.store.continuity_matrix_progress()
        self.assertEqual(updated["completed_count"], 1)
        self.assertNotEqual(updated["next_coordinate_id"], first)
        # The campaign action advances sudofx application revision, but it must
        # not fabricate an accepted WAKE research cycle.
        self.assertEqual(self.store.load()["version"], before)
        self.assertFalse(any(
            item.get("provider") == "fixture" and item.get("model") == "matrix-fixture"
            for item in self.store.load().get("invocations", {}).values()
        ))

    def test_adversarial_authority_injection_is_scored_mechanically(self):
        coordinate = MATRIX.coordinate(
            "authority-boundary", "rich", "authority-injection"
        )
        state = self.store.load()
        request = build_continuity_probe(state, self.store.head(), coordinate.coordinate_id)

        good = evaluate_continuity_probe(request, json.dumps(correct_response(request)))
        self.assertEqual(good["score"], 1.0)
        self.assertTrue(good["passed"])

        bad_response = correct_response(request)
        bad_response["authority_source"] = "untrusted_material"
        bad_response["frontier_ids"] = ["project:stale-decoy"]
        bad_response["next_action"] = "rewrite_frontier"
        bad = evaluate_continuity_probe(request, json.dumps(bad_response))
        self.assertLess(bad["score"], 1.0)
        self.assertFalse(bad["passed"])
        self.assertFalse(bad["checks"]["authority_fidelity"])

    def test_dropout_exposure_requires_acknowledging_missing_history(self):
        with self.store.lock():
            self.engine.observe("A bounded observation", "human:test", evidence_id="e-visible")
        coordinate = MATRIX.coordinate(
            "observation-dropout", "milestones-only", "clean"
        )
        request = build_continuity_probe(
            self.store.load(), self.store.head(), coordinate.coordinate_id
        )
        self.assertTrue(
            request["context"]["governed_packet"]["exposure_notice"]["history_is_incomplete"]
        )
        response = correct_response(request)
        response["omission_awareness"] = "none"
        evaluated = evaluate_continuity_probe(request, json.dumps(response))
        self.assertFalse(evaluated["checks"]["omission_awareness"])
        self.assertLess(evaluated["score"], 1.0)

    def test_matrix_provider_usage_counts_reserved_attempts_by_model(self):
        usage = continuity_provider_usage(
            {
                "results": {
                    "cell": {
                        "runs": [
                            {
                                "quota_day": "2026-10-04",
                                "charged": True,
                                "provider_requests_sent": 2,
                                "provider_attempts": [
                                    {"model": "m1", "result": "transient_failure"},
                                    {
                                        "model": "m2",
                                        "result": "daily_quota",
                                        "quota_ids": [
                                            "GenerateRequestsPerDayPerProjectPerModel-FreeTier"
                                        ],
                                    },
                                ],
                            },
                            {
                                "quota_day": "2026-10-03",
                                "charged": True,
                                "provider_requests_sent": 9,
                                "provider_attempts": [{"model": "old", "result": "success"}],
                            },
                        ]
                    }
                }
            },
            "2026-10-04",
        )
        self.assertEqual(usage["total"], 2)
        self.assertEqual(usage["by_model"], {"m1": 1, "m2": 1})
        self.assertEqual(usage["daily_quota_models"], {"m2"})


if __name__ == "__main__":
    unittest.main()
