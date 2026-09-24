import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.governance import Rejected, _enforce_squirrel_rotation
from wake.providers import RESEARCH_SYSTEM, schema_for_context
from wake.squirrel import (
    ATTENTION_SATURATION_THRESHOLD, COOLDOWN_OTHER_ATTEMPTS,
    HARD_REJECTION_THRESHOLD, assessment, plan,
)
from support import charter_settings


class SquirrelTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engine = Engine(Path(self.temp.name) / "data", charter_settings("Test deterministic attention recovery."))
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

    def test_productive_attention_saturates_without_erasing_progress(self):
        state = {
            "charter": "test",
            "research_topics": [{"id": "entropy"}, {"id": "comedy"}],
            "projects": {
                "p": {"id": "p", "domain": "entropy", "status": "active",
                      "updated_version": 1, "question": "q", "next_step": "n"}
            },
            "invocations": {},
            "squirrel": {"counters": {}, "deferred": {}},
            "evidence": {},
        }
        for index in range(ATTENTION_SATURATION_THRESHOLD):
            invocation = f"w-{index}"
            state["invocations"][invocation] = {"squirrel": {"selected_topic": "entropy"}}
            receipt = assessment(state, invocation, "accepted", {
                "actions": [{"type": "notebook", "project": "p"}],
            })
            state["squirrel"] = {
                "counters": receipt["counters"],
                "deferred": receipt["deferred"],
                "attention": receipt["attention"],
            }

        self.assertTrue(receipt["durable_progress"])
        self.assertTrue(receipt["attention_saturation_triggered"])
        self.assertEqual(receipt["attention"]["accepted_streak"], ATTENTION_SATURATION_THRESHOLD)
        self.assertEqual(receipt["deferred"]["entropy"]["cause"], "attention_saturation")
        self.assertEqual(plan(state)["selected_topic"], "comedy")

    def test_new_evidence_does_not_cancel_attention_saturation_cooldown(self):
        state = {
            "charter": "test",
            "research_topics": [{"id": "entropy"}, {"id": "comedy"}],
            "projects": {"p": {"id": "p", "domain": "entropy", "status": "active", "updated_version": 1}},
            "invocations": {"old": {"base_version": 5}},
            "squirrel": {
                "counters": {},
                "deferred": {
                    "entropy": {
                        "deferred_by": "old",
                        "cause": "attention_saturation",
                        "other_topic_attempts": 0,
                    }
                },
                "attention": {"topic": "entropy", "accepted_streak": ATTENTION_SATURATION_THRESHOLD},
            },
            "evidence": {
                "new": {
                    "actor": "collector", "scope": "collected", "version": 6,
                    "content": json.dumps({"topic_domain": "entropy"}),
                }
            },
        }
        self.assertEqual(plan(state)["selected_topic"], "comedy")

    def test_rotation_skips_fully_capability_blocked_domain(self):
        state = {
            "charter": "test",
            "research_topics": [
                {"id": "wake_analysis", "enabled": True},
                {"id": "information_thermodynamics", "enabled": True},
                {"id": "entropy", "enabled": True},
            ],
            "projects": {
                "wake": {"id": "wake", "domain": "wake_analysis", "status": "active", "updated_version": 5},
                "landauer": {"id": "landauer", "domain": "information_thermodynamics", "status": "active", "updated_version": 4},
            },
            "acquisition": {"landauer": {"capability_blocked": True}},
            "evidence": {},
            "invocations": {},
            "squirrel": {
                "counters": {},
                "deferred": {
                    "wake_analysis": {
                        "deferred_by": "old",
                        "cause": "attention_saturation",
                        "other_topic_attempts": 0,
                    }
                },
            },
        }
        directive = plan(state)
        self.assertEqual(directive["selected_topic"], "entropy")
        self.assertTrue(directive["enforce_selected_topic"])
        self.assertIn("information_thermodynamics", directive["capability_blocked_topics"])

    def test_governance_rotation_rejects_substantive_work_on_deferred_topic(self):
        state = {
            "charter": "test",
            "invocations": {
                "w": {"squirrel": {"selected_topic": "entropy", "enforce_selected_topic": True}}
            },
        }
        candidate = {
            "projects": {
                "wake": {"id": "wake", "domain": "wake_analysis", "status": "active"}
            }
        }
        with self.assertRaisesRegex(Rejected, "Squirrel rotation requires substantive work on entropy"):
            _enforce_squirrel_rotation(
                state, "w",
                {"type": "research", "id": "r", "project": "wake",
                 "query": "q", "domain": "wake_analysis", "reason": "r"},
                candidate,
            )

    def test_rotation_allows_parking_old_project_to_free_capacity(self):
        state = {
            "charter": "test",
            "invocations": {
                "w": {"squirrel": {"selected_topic": "entropy", "enforce_selected_topic": True}}
            },
        }
        candidate = {
            "projects": {
                "wake": {"id": "wake", "domain": "wake_analysis", "status": "active"}
            }
        }
        _enforce_squirrel_rotation(
            state, "w",
            {"type": "project", "id": "wake", "title": "Wake", "question": "q",
             "domain": "wake_analysis", "status": "parked", "next_step": "later", "reason": "rotate"},
            candidate,
        )

    def test_schema_preflights_research_to_enforced_topic(self):
        context = {
            "research_topics": [{"id": "wake_analysis"}, {"id": "entropy"}],
            "projects": [],
            "commitments": [],
            "evidence": [],
            "blog_notebooks": {},
            "squirrel": {"selected_topic": "entropy", "enforce_selected_topic": True},
        }
        schema = schema_for_context(context)
        choices = schema["properties"]["actions"]["items"]["anyOf"]
        research = next(a for a in choices if a["properties"]["type"]["enum"] == ["research"])
        self.assertEqual(research["properties"]["domain"]["enum"], ["entropy"])



if __name__ == "__main__":
    unittest.main()
