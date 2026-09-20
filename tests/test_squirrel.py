import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.providers import RESEARCH_SYSTEM
from wake.squirrel import COOLDOWN_OTHER_ATTEMPTS, HARD_REJECTION_THRESHOLD, assessment, plan


class SquirrelTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engine = Engine(Path(self.temp.name) / "data", {
            **DEFAULTS, "mission": "Test deterministic attention recovery.",
        })
        with self.engine.store.lock():
            self.engine.initialize()

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def reject(self):
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "test")
            result = self.engine.finish(invocation, "not-json")
        self.assertEqual(result["status"], "rejected")
        return request

    def test_fifth_hard_rejection_defers_topic_and_preserves_state(self):
        for _ in range(HARD_REJECTION_THRESHOLD):
            request = self.reject()
        state = self.engine.store.load()
        topic = request["context"]["squirrel"]["selected_topic"]
        self.assertIn(topic, state["squirrel"]["deferred"])
        self.assertEqual(state["squirrel"]["counters"][topic], HARD_REJECTION_THRESHOLD)
        self.assertEqual(state["commitments"], {})
        self.assertTrue(all(item["actor"] == "runtime" for item in state["evidence"].values()))
        receipt = state["squirrel"]["last_receipt"]
        self.assertEqual(receipt["triggered_topics"], [topic])

    def test_alternate_topic_is_selected_then_cooldown_restores_original(self):
        for _ in range(HARD_REJECTION_THRESHOLD):
            self.reject()
        original = self.engine.store.load()["squirrel"]["last_receipt"]["selected_topic"]
        for _ in range(COOLDOWN_OTHER_ATTEMPTS):
            request = self.reject()
            self.assertNotEqual(request["context"]["squirrel"]["selected_topic"], original)
        state = self.engine.store.load()
        self.assertNotIn(original, state["squirrel"]["deferred"])
        self.assertIn(original, state["squirrel"]["last_receipt"]["restored_topics"])

    def test_bounded_context_keeps_squirrel_directive(self):
        original_context = self.engine.context
        self.engine.context = lambda state, receipt: {**original_context(state, receipt), "noise": "x" * 60000}
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "cleanup"})
        self.assertEqual(request["context"]["context_mode"], "bounded")
        self.assertTrue(request["context"]["squirrel"]["active"])

    def test_reset_is_a_fresh_empty_squirrel_runtime(self):
        self.assertEqual(self.engine.store.load()["squirrel"], {"counters": {}, "deferred": {}})

    def test_provider_instruction_cannot_turn_squirrel_into_a_governance_exception(self):
        self.assertIn("temporary attention directive", RESEARCH_SYSTEM)
        self.assertIn("do not cancel, weaken, or reinterpret", RESEARCH_SYSTEM)
        self.assertIn("not permission to bypass", RESEARCH_SYSTEM)

    def test_durable_project_advancement_resets_a_topic_counter(self):
        state = {
            "charter": "test", "squirrel": {"counters": {"entropy": 4}, "deferred": {}},
            "projects": {"p": {"id": "p", "domain": "entropy", "next_step": "Old step"}},
            "invocations": {"w": {"squirrel": {"selected_topic": "entropy"}}},
        }
        receipt = assessment(state, "w", "accepted", {
            "actions": [{"type": "project", "id": "p", "next_step": "A different step"}],
        })
        self.assertTrue(receipt["durable_progress"])
        self.assertEqual(receipt["counters"]["entropy"], 0)

    def test_new_collected_topic_evidence_restores_eligibility_early(self):
        state = {
            "charter": "test", "research_topics": [{"id": "entropy"}, {"id": "comedy"}],
            "projects": {"p": {"id": "p", "domain": "entropy", "status": "active", "updated_version": 1}},
            "invocations": {"old": {"base_version": 1}, "w": {"squirrel": {"selected_topic": "entropy"}}},
            "squirrel": {"counters": {"entropy": 5}, "deferred": {"entropy": {"deferred_by": "old", "other_topic_attempts": 0}}},
            "evidence": {"new": {"actor": "collector", "scope": "collected", "version": 2,
                                    "content": json.dumps({"topic_domain": "entropy"})}},
        }
        self.assertEqual(plan(state)["selected_topic"], "entropy")
        self.assertIn("entropy", assessment(state, "w", "accepted", {"actions": []})["restored_topics"])


if __name__ == "__main__":
    unittest.main()
