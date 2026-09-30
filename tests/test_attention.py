import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine, _rotation_preflight
from wake.governance import Rejected, _enforce_attention_rotation
from wake.providers import RESEARCH_SYSTEM, schema_for_context
from wake.attention import (
    ATTENTION_SATURATION_THRESHOLD, COOLDOWN_OTHER_ATTEMPTS,
    HARD_REJECTION_THRESHOLD, assessment, plan,
)
from support import charter_settings


class AttentionTests(unittest.TestCase):
    def test_legacy_squirrel_event_replays_into_attention_state(self):
        from wake.store import reduce_event
        state = {
            "version": 0, "objective": "test", "focus": "continuity",
            "beliefs": {}, "commitments": {}, "evidence": {}, "journal": [], "posts": {},
            "invocations": {"w": {"status": "accepted"}}, "pending": None,
            "attention": {"counters": {}, "deferred": {}},
            "projects": {}, "notebooks": {}, "research": {}, "charter": "test",
            "acquisition": {}, "representations": {},
        }
        event = {
            "seq": 1, "time": "2026-01-01T00:00:00+00:00", "kind": "squirrel_assessed",
            "payload": {
                "invocation": "w", "terminal": "accepted",
                "counters": {"entropy": 1}, "deferred": {},
                "attention": {"topic": "entropy", "accepted_streak": 1},
            },
        }
        replayed = reduce_event(state, event, historical=True)
        self.assertEqual(replayed["attention"]["counters"]["entropy"], 1)
        self.assertNotIn("squirrel", replayed)

    def test_attention_preflight_preserves_due_system_wide_bob_post(self):
        state = {
            "journal": [],
            "posts": {},
            "projects": {},
            "research_topics": [{"id": "entropy", "enabled": True}],
            "acquisition": {},
            "invocations": {
                "w": {
                    "attention": {
                        "enforce_selected_topic": True,
                        "selected_topic": "entropy",
                    }
                }
            },
        }
        blog = {
            "type": "blog",
            "id": "bob-introduction",
            "project": "",
            "reflection_cycle": 1,
        }
        proposal = {
            "base_version": 0,
            "title": "Bob says hello",
            "summary": "Establish the public correspondent.",
            "actions": [blog],
        }
        normalized, withheld = _rotation_preflight(state, "w", proposal)
        self.assertEqual(normalized["actions"], [blog])
        self.assertIsNone(withheld)


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
        topic = request["context"]["attention"]["selected_topic"]
        self.assertIn(topic, state["attention"]["deferred"])
        self.assertEqual(state["attention"]["counters"][topic], HARD_REJECTION_THRESHOLD)
        self.assertEqual(state["commitments"], {})
        self.assertTrue(all(item["actor"] == "runtime" for item in state["evidence"].values()))
        receipt = state["attention"]["last_receipt"]
        self.assertEqual(receipt["triggered_topics"], [topic])

    def test_alternate_topic_is_selected_then_cooldown_restores_original(self):
        for _ in range(HARD_REJECTION_THRESHOLD):
            self.reject()
        original = self.engine.store.load()["attention"]["last_receipt"]["selected_topic"]
        for _ in range(COOLDOWN_OTHER_ATTEMPTS):
            request = self.reject()
            self.assertNotEqual(request["context"]["attention"]["selected_topic"], original)
        state = self.engine.store.load()
        self.assertNotIn(original, state["attention"]["deferred"])
        self.assertIn(original, state["attention"]["last_receipt"]["restored_topics"])

    def test_bounded_context_keeps_attention_directive(self):
        original_context = self.engine.context
        self.engine.context = lambda state, receipt: {**original_context(state, receipt), "noise": "x" * 60000}
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "cleanup"})
        self.assertEqual(request["context"]["context_mode"], "bounded")
        self.assertTrue(request["context"]["attention"]["active"])

    def test_reset_is_a_fresh_empty_attention_runtime(self):
        self.assertEqual(self.engine.store.load()["attention"], {"counters": {}, "deferred": {}})

    def test_provider_instruction_cannot_turn_attention_into_a_governance_exception(self):
        self.assertIn("temporary attention directive", RESEARCH_SYSTEM)
        self.assertIn("do not cancel, weaken, or reinterpret", RESEARCH_SYSTEM)
        self.assertIn("not permission to bypass", RESEARCH_SYSTEM)
        self.assertIn("reactivate that exact project", RESEARCH_SYSTEM)
        self.assertIn("do not create a replacement project", RESEARCH_SYSTEM)

    def test_durable_project_advancement_resets_a_topic_counter(self):
        state = {
            "charter": "test", "attention": {"counters": {"entropy": 4}, "deferred": {}},
            "projects": {"p": {"id": "p", "domain": "entropy", "next_step": "Old step"}},
            "invocations": {"w": {"attention": {"selected_topic": "entropy"}}},
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
            "invocations": {"old": {"base_version": 1}, "w": {"attention": {"selected_topic": "entropy"}}},
            "attention": {"counters": {"entropy": 5}, "deferred": {"entropy": {"deferred_by": "old", "other_topic_attempts": 0}}},
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
            "attention": {"counters": {}, "deferred": {}},
            "evidence": {},
        }
        for index in range(ATTENTION_SATURATION_THRESHOLD):
            invocation = f"w-{index}"
            state["invocations"][invocation] = {"attention": {"selected_topic": "entropy"}}
            receipt = assessment(state, invocation, "accepted", {
                "actions": [{"type": "notebook", "project": "p"}],
            })
            state["attention"] = {
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
            "attention": {
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

    def test_saturation_does_not_expire_after_three_other_topic_attempts(self):
        state = {
            "charter": "test",
            "research_topics": [{"id": "entropy"}, {"id": "comedy"}],
            "projects": {
                "p": {"id": "p", "domain": "entropy", "status": "active", "updated_version": 5},
                "c": {"id": "c", "domain": "comedy", "status": "active", "updated_version": 6},
            },
            "invocations": {},
            "attention": {
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
            "evidence": {},
        }
        for index in range(COOLDOWN_OTHER_ATTEMPTS):
            invocation = f"other-{index}"
            state["invocations"][invocation] = {"attention": {"selected_topic": "comedy"}}
            receipt = assessment(state, invocation, "accepted", {
                "actions": [{"type": "research", "id": f"r-{index}", "project": "c",
                             "query": "q", "domain": "comedy", "reason": "r"}],
            })
            state["attention"] = {
                "counters": receipt["counters"],
                "deferred": receipt["deferred"],
                "attention": receipt["attention"],
            }

        self.assertIn("entropy", state["attention"]["deferred"])
        self.assertEqual(state["attention"]["deferred"]["entropy"]["other_topic_attempts"],
                         COOLDOWN_OTHER_ATTEMPTS)
        self.assertEqual(plan(state)["selected_topic"], "comedy")

    def test_external_notebook_releases_saturated_topic(self):
        state = {
            "charter": "test",
            "research_topics": [{"id": "entropy"}, {"id": "comedy"}],
            "projects": {
                "p": {"id": "p", "domain": "entropy", "status": "active", "updated_version": 5},
                "c": {"id": "c", "domain": "comedy", "status": "active", "updated_version": 6},
            },
            "invocations": {
                "w": {"attention": {"selected_topic": "comedy"}},
            },
            "attention": {
                "counters": {},
                "deferred": {
                    "entropy": {
                        "deferred_by": "old",
                        "cause": "attention_saturation",
                        "other_topic_attempts": 7,
                    }
                },
                "attention": {"topic": "comedy", "accepted_streak": 2},
            },
            "evidence": {},
        }
        receipt = assessment(state, "w", "accepted", {
            "actions": [{"type": "notebook", "id": "nb-c", "project": "c"}],
        })
        self.assertIn("entropy", receipt["restored_topics"])
        self.assertNotIn("entropy", receipt["deferred"])


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
            "attention": {
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
                "w": {"attention": {"selected_topic": "entropy", "enforce_selected_topic": True}}
            },
        }
        candidate = {
            "projects": {
                "wake": {"id": "wake", "domain": "wake_analysis", "status": "active"}
            }
        }
        with self.assertRaisesRegex(Rejected, "Attention rotation requires substantive work on entropy"):
            _enforce_attention_rotation(
                state, "w",
                {"type": "research", "id": "r", "project": "wake",
                 "query": "q", "domain": "wake_analysis", "reason": "r"},
                candidate,
            )

    def test_rotation_allows_parking_old_project_to_free_capacity(self):
        state = {
            "charter": "test",
            "invocations": {
                "w": {"attention": {"selected_topic": "entropy", "enforce_selected_topic": True}}
            },
        }
        candidate = {
            "projects": {
                "wake": {"id": "wake", "domain": "wake_analysis", "status": "active"}
            }
        }
        _enforce_attention_rotation(
            state, "w",
            {"type": "project", "id": "wake", "title": "Wake", "question": "q",
             "domain": "wake_analysis", "status": "parked", "next_step": "later", "reason": "rotate"},
            candidate,
        )

    def test_schema_preflights_research_to_enforced_topic(self):
        context = {
            "research_topics": [{"id": "wake_analysis"}, {"id": "entropy"}],
            "projects": [
                {"id": "e", "title": "Entropy", "question": "q",
                 "domain": "entropy", "status": "active", "next_step": "n"}
            ],
            "commitments": [],
            "evidence": [],
            "blog_notebooks": {},
            "attention": {"selected_topic": "entropy", "enforce_selected_topic": True},
        }
        schema = schema_for_context(context)
        choices = schema["properties"]["actions"]["items"]["anyOf"]
        research = next(a for a in choices if a["properties"]["type"]["enum"] == ["research"])
        self.assertEqual(research["properties"]["domain"]["enum"], ["entropy"])
        self.assertEqual(research["properties"]["project"]["enum"], ["e"])

    def test_full_capacity_rotation_schema_requires_parking_first(self):
        context = {
            "research_topics": [
                {"id": "information_thermodynamics"},
                {"id": "neurodivergence"},
                {"id": "quantum_mechanics"},
                {"id": "psychology"},
            ],
            "projects": [
                {"id": "wake", "title": "Wake", "question": "q1",
                 "domain": "wake_analysis", "status": "active", "next_step": "n1"},
                {"id": "thermo", "title": "Thermo", "question": "q2",
                 "domain": "information_thermodynamics", "status": "active", "next_step": "n2"},
                {"id": "neuro", "title": "Neuro", "question": "q3",
                 "domain": "neurodivergence", "status": "active", "next_step": "n3"},
            ],
            "commitments": [],
            "evidence": [],
            "blog_notebooks": {},
            "attention": {"selected_topic": "quantum_mechanics", "enforce_selected_topic": True},
        }
        choices = schema_for_context(context)["properties"]["actions"]["items"]["anyOf"]
        projects = [a for a in choices if a["properties"]["type"]["enum"] == ["project"]]
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0]["properties"]["id"]["enum"], ["wake"])
        self.assertEqual(projects[0]["properties"]["status"]["enum"], ["parked"])
        self.assertFalse(any(a["properties"]["type"]["enum"] == ["research"] for a in choices))
        self.assertFalse(any(a["properties"]["type"]["enum"] == ["notebook"] for a in choices))

    def test_rotation_reactivates_parked_selected_project_before_new_project(self):
        context = {
            "research_topics": [{"id": "consciousness"}, {"id": "entropy"}],
            "projects": [
                {"id": "old-consciousness", "title": "Scientific Theories of Consciousness",
                 "question": "What observations do major theories of consciousness explain?",
                 "domain": "consciousness", "status": "parked", "next_step": "Compare theories"},
                {"id": "entropy-active", "title": "Entropy", "question": "q",
                 "domain": "entropy", "status": "active", "next_step": "n"},
            ],
            "commitments": [],
            "evidence": [],
            "blog_notebooks": {},
            "attention": {"selected_topic": "consciousness", "enforce_selected_topic": True},
        }
        choices = schema_for_context(context)["properties"]["actions"]["items"]["anyOf"]
        projects = [a for a in choices if a["properties"]["type"]["enum"] == ["project"]]
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0]["properties"]["id"]["enum"], ["old-consciousness"])
        self.assertEqual(projects[0]["properties"]["status"]["enum"], ["active"])
        self.assertFalse(any(a["properties"]["type"]["enum"] == ["research"] for a in choices))

    def test_rotation_without_selected_project_waits_before_research(self):
        context = {
            "research_topics": [{"id": "quantum_mechanics"}],
            "projects": [],
            "commitments": [],
            "evidence": [],
            "blog_notebooks": {},
            "attention": {"selected_topic": "quantum_mechanics", "enforce_selected_topic": True},
        }
        choices = schema_for_context(context)["properties"]["actions"]["items"]["anyOf"]
        project_action = next(a for a in choices if a["properties"]["type"]["enum"] == ["project"])
        self.assertEqual(project_action["properties"]["domain"]["enum"], ["quantum_mechanics"])
        self.assertFalse(any(a["properties"]["type"]["enum"] == ["research"] for a in choices))
        self.assertFalse(any(a["properties"]["type"]["enum"] == ["notebook"] for a in choices))


    def test_removed_active_topic_forces_rotation_without_reset(self):
        state = {
            "charter": "test",
            "research_topics": [
                {"id": "entropy", "enabled": True},
                {"id": "comedy", "enabled": True},
            ],
            "projects": {
                "wake": {
                    "id": "wake",
                    "domain": "wake_analysis",
                    "status": "active",
                    "updated_version": 99,
                }
            },
            "acquisition": {},
            "evidence": {},
            "invocations": {},
            "attention": {"counters": {}, "deferred": {}},
        }
        directive = plan(state)
        self.assertIn(directive["selected_topic"], {"entropy", "comedy"})
        self.assertTrue(directive["current_topic_unconfigured"])
        self.assertTrue(directive["rotation_required"])
        self.assertTrue(directive["enforce_selected_topic"])
        self.assertIn("no longer configured", directive["reason"])



    def test_initial_topic_selection_is_order_independent_and_receipt_driven(self):
        topics = [
            {"id": "entropy", "enabled": True},
            {"id": "comedy", "enabled": True},
            {"id": "music", "enabled": True},
        ]
        base = {
            "charter": "test", "version": 0, "projects": {}, "acquisition": {},
            "invocations": {}, "attention": {"counters": {}, "deferred": {}},
        }
        state_a = {**base, "research_topics": topics, "evidence": {
            "receipt": {"id": "r-randomized", "actor": "runtime", "source": "runtime:continuity"}
        }}
        state_b = {**base, "research_topics": list(reversed(topics)), "evidence": {
            "receipt": {"id": "r-randomized", "actor": "runtime", "source": "runtime:continuity"}
        }}
        first = plan(state_a)
        reordered = plan(state_b)
        self.assertEqual(first["selected_topic"], reordered["selected_topic"])
        self.assertEqual(first["topic_selection_method"], "receipt_hash_uniform_index")
        self.assertEqual(first["topic_selection_candidates"], ["comedy", "entropy", "music"])
        self.assertFalse(first["enforce_selected_topic"])

        selections = set()
        for index in range(32):
            varied = {**base, "research_topics": topics, "evidence": {
                "receipt": {"id": f"r-{index}", "actor": "runtime", "source": "runtime:continuity"}
            }}
            selections.add(plan(varied)["selected_topic"])
        self.assertGreater(len(selections), 1)

    def test_rotation_preflight_salvages_selected_topic_from_mixed_proposal(self):
        state = {
            "research_topics": [{"id": "entropy", "label": "Entropy", "enabled": True}],
            "projects": {
                "wake": {
                    "id": "wake", "title": "Wake", "question": "q",
                    "domain": "wake_analysis", "status": "active",
                    "next_step": "n", "updated_version": 10,
                },
                "thermo": {
                    "id": "thermo", "title": "Thermo", "question": "q2",
                    "domain": "information_thermodynamics", "status": "active",
                    "next_step": "n2", "updated_version": 9,
                },
            },
            "invocations": {
                "w": {"attention": {
                    "selected_topic": "entropy",
                    "enforce_selected_topic": True,
                    "capability_blocked_topics": ["information_thermodynamics"],
                }}
            },
        }
        proposal = {
            "base_version": 56,
            "title": "Mixed",
            "summary": "mixed",
            "actions": [
                {"type": "notebook", "id": "nb-wake", "project": "wake"},
                {"type": "resolve", "id": "old", "status": "fulfilled",
                 "evidence": ["e"], "reason": "old"},
                {"type": "research", "id": "r-entropy", "project": "thermo",
                 "query": "entropy", "domain": "entropy", "reason": "selected"},
            ],
        }
        normalized, receipt = _rotation_preflight(state, "w", proposal)
        self.assertEqual([a["type"] for a in normalized["actions"]], ["research"])
        self.assertEqual(normalized["actions"][0]["domain"], "entropy")
        self.assertEqual(receipt["withheld_count"], 2)
        self.assertEqual(receipt["selected_topic"], "entropy")

    def test_rotation_preflight_inserts_capacity_park_before_new_project(self):
        state = {
            "research_topics": [
                {"id": "entropy", "label": "Entropy", "enabled": True},
                {"id": "neurodivergence", "label": "Neurodivergence", "enabled": True},
            ],
            "projects": {
                "wake": {
                    "id": "wake", "title": "Wake", "question": "q1",
                    "domain": "wake_analysis", "status": "active",
                    "next_step": "n1", "updated_version": 10,
                },
                "thermo": {
                    "id": "thermo", "title": "Thermo", "question": "q2",
                    "domain": "information_thermodynamics", "status": "active",
                    "next_step": "n2", "updated_version": 11,
                },
                "neuro": {
                    "id": "neuro", "title": "Neuro", "question": "q3",
                    "domain": "neurodivergence", "status": "active",
                    "next_step": "n3", "updated_version": 12,
                },
            },
            "invocations": {
                "w": {"attention": {
                    "selected_topic": "entropy",
                    "enforce_selected_topic": True,
                    "capability_blocked_topics": ["information_thermodynamics"],
                }}
            },
        }
        proposal = {
            "base_version": 56,
            "title": "Entropy",
            "summary": "start",
            "actions": [
                {"type": "project", "id": "entropy-p", "title": "Entropy",
                 "question": "q", "domain": "entropy", "status": "active",
                 "next_step": "research", "reason": "selected"},
                {"type": "research", "id": "entropy-r", "project": "entropy-p",
                 "query": "entropy definitions", "domain": "entropy", "reason": "selected"},
            ],
        }
        normalized, receipt = _rotation_preflight(state, "w", proposal)
        self.assertEqual(normalized["actions"][0]["id"], "wake")
        self.assertEqual(normalized["actions"][0]["status"], "parked")
        self.assertEqual(normalized["actions"][1]["id"], "entropy-p")
        self.assertTrue(receipt["inserted_capacity_park"])



if __name__ == "__main__":
    unittest.main()
