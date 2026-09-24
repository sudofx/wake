# =============================================================================
# TESTING INTENT — research
#
# This file is executable documentation. Passing cases define behavior WAKE✳︎
# promises to preserve; rejection/failure cases define boundaries that future
# refactors must not weaken merely to make CI green. Assertions should make the
# protected invariant understandable to both human and AI maintainers.
# =============================================================================
# WAKE✳︎ MAINTAINER NOTE
#
# Executable specification for research.
# Tests are documentation with teeth: passing cases define permitted behavior and rejection cases define protected boundaries.
# When changing implementation, preserve the reason behind an assertion rather than weakening it merely to make CI green.

"""Exercise scientific provenance, bounded autonomy and durable cloud handoffs offline."""

import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from scripts.github_wake import StateBranch
from wake.audit import verify_history
from wake.engine import DEFAULTS, Engine
from wake.governance import Rejected
from wake.providers import Fixture, RESEARCH_SYSTEM, schema_for_context
from wake.research import (
    allowed_url, collect, discovery_urls, evidence_role, host_tier,
    repository_sources, research_urls,
)
from wake.report import export
from support import charter_settings


def project(identifier="p", status="active"):
    return dict(type="project", id=identifier, title="Comparing explanations", question="What distinguishes the explanations?",
                domain="entropy", status=status, next_step="Compare collected sources", reason="A tractable question")


def notebook(evidence, findings="A bounded comparison [s1] [s2]."):
    return dict(type="notebook", id="n", project="p", title="A comparison", summary="A provisional distinction",
                findings=findings, limitations="Synthetic test sources, not scientific results.",
                next_questions="Obtain stronger evidence", evidence=evidence, reason="Make the distinction explicit")


class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.engine = Engine(self.root/"data", charter_settings("Explore big ideas through small useful projects."))
        with self.engine.store.lock():
            self.engine.initialize()

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def propose(self, actions):
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "research-test")
            return self.engine.finish(invocation, json.dumps(dict(base_version=request["context"]["version"],
                title="Research fixture", summary="Offline boundary test", actions=actions)))

    def source(self, identifier, url=None, status="collected", source_scope="synthetic test fixture"):
        with self.engine.store.lock():
            self.engine.store.append("observation", dict(id=identifier, source=url or "https://plato.stanford.edu/entries/"+identifier,
                content=json.dumps({"scope":source_scope, "excerpt":"Only a fixture"}), actor="collector", scope=status))

    def test_existing_pet_name_is_migrated_through_an_audited_event(self):
        legacy = Engine(self.root/"legacy", charter_settings("Explore big ideas.", pet_name="Wake"))
        try:
            with legacy.store.lock():
                legacy.initialize()
            legacy.config["pet_name"] = "WAKE✳"
            with legacy.store.lock():
                state = legacy.initialize()
            self.assertEqual(state["pet_name"], "WAKE✳")
            event = legacy.store.events()[-1]
            self.assertEqual(event["kind"], "pet_renamed")
            self.assertEqual(event["payload"], {"pet_name": "WAKE✳", "actor": "operator"})
            reconstructed, _ = legacy.store.replay()
            self.assertEqual(reconstructed, state)
        finally:
            legacy.store.close()

    def test_topic_file_changes_become_audited_configuration(self):
        changed = [*self.engine.config["research_topics"],
                   {"id": "new_topic", "label": "A new topic", "query": "new topic",
                    "seed_question": "What concrete question should start this topic?"}]
        self.engine.config["research_topics"] = changed
        with self.engine.store.lock():
            state = self.engine.initialize()
            invocation, request = self.engine.start("fixture", "topic-test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})
        self.assertEqual(state["research_topics"], changed)
        self.assertEqual(set(state["topic_colors"]), {topic["id"] for topic in changed})
        self.assertEqual(len(set(state["topic_colors"].values())), len(changed))
        self.assertEqual([event["kind"] for event in self.engine.store.events()].count("research_topics_changed"), 1)
        new_topic = next(topic for topic in request["context"]["research_topics"] if topic["id"] == "new_topic")
        self.assertEqual(new_topic["seed_question"], "What concrete question should start this topic?")
        self.assertIn({"topic": "new_topic", "question": "What concrete question should start this topic?"},
                      request["context"]["seed_questions"])
        self.assertEqual(request["context"]["seed_question_metrics"]["available"], len(changed))
        variants = request["response_schema"]["properties"]["actions"]["items"]["anyOf"]
        project_schema = next(item for item in variants if item["properties"]["type"]["enum"] == ["project"])
        self.assertIn("new_topic", project_schema["properties"]["domain"]["enum"])

    def test_disabled_topic_is_not_exposed_for_new_work(self):
        disabled = {
            "id": "disabled_topic", "label": "Disabled", "query": "disabled",
            "seed_question": "Should not be offered.", "enabled": False, "source_kind": "web",
        }
        self.engine.config["research_topics"] = [*self.engine.config["research_topics"], disabled]
        with self.engine.store.lock():
            state = self.engine.initialize()
            invocation, request = self.engine.start("fixture", "disabled-topic-test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})
        self.assertIn("disabled_topic", [topic["id"] for topic in state["research_topics"]])
        self.assertNotIn("disabled_topic", [topic["id"] for topic in request["context"]["research_topics"]])
        variants = request["response_schema"]["properties"]["actions"]["items"]["anyOf"]
        project_schema = next(item for item in variants if item["properties"]["type"]["enum"] == ["project"])
        self.assertNotIn("disabled_topic", project_schema["properties"]["domain"]["enum"])

    def test_project_name_is_configuration_driven(self):
        renamed = Engine(self.root/"renamed", charter_settings("Explore.", project_name="Project Star"))
        try:
            with renamed.store.lock():
                state = renamed.initialize()
                invocation, request = renamed.start("fixture", "identity-test")
                renamed.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})
            self.assertEqual(state["pet_name"], "Project Star")
            self.assertEqual(request["context"]["project_name"], "Project Star")
        finally:
            renamed.store.close()

    def test_seed_question_is_initial_condition_not_repeated_instruction(self):
        topic = next(item for item in self.engine.config["research_topics"] if item["id"] == "entropy")
        self.engine.config["research_topics"] = [
            {**item, **({"seed_question": "What distinguishes the major entropy definitions?"}
                       if item["id"] == "entropy" else {})}
            for item in self.engine.config["research_topics"]
        ]
        with self.engine.store.lock():
            state = self.engine.initialize()
            before = self.engine.context(state, "seed-before")
            seeded = next(item for item in before["research_topics"] if item["id"] == "entropy")
            self.assertIn("seed_question", seeded)
            self.engine.store.append("project_adopted", {
                "id": "seeded-entropy", "title": "Seeded entropy project",
                "question": seeded["seed_question"], "domain": "entropy",
                "status": "active", "next_step": "Collect qualifying evidence.",
                "reason": "Start from the configured seed.", "actor": "operator"
            })
            after = self.engine.context(self.engine.store.load(), "seed-after")
        entropy = next(item for item in after["research_topics"] if item["id"] == "entropy")
        self.assertNotIn("seed_question", entropy)
        self.assertNotIn("entropy", [item["topic"] for item in after["seed_questions"]])
        self.assertGreaterEqual(after["seed_question_metrics"]["started"], 1)
        self.assertEqual(topic["id"], "entropy")

    def test_bob_reflection_is_due_on_each_tenth_accepted_wake(self):
        state = self.engine.store.load()

        state["version"] = 9
        tenth_cycle = self.engine.context(state, "test-receipt")
        self.assertEqual(tenth_cycle["bob_reflection_cycle"], 10)
        self.assertTrue(tenth_cycle["bob_reflection_due"])
        schema = schema_for_context(tenth_cycle)
        blog_schema = next(item for item in schema["properties"]["actions"]["items"]["anyOf"]
                           if item["properties"]["type"]["enum"] == ["blog"])
        self.assertIn("reflection_cycle", blog_schema["required"])
        self.assertEqual(blog_schema["properties"]["reflection_cycle"]["enum"], [10])

        # Legacy reflection posts created exactly on the milestone still count
        # as fulfilled, so historical records replay without migration.
        state["posts"] = {"cycle-10": {"created_version": 10}}
        state["version"] = 10
        eleventh_cycle = self.engine.context(state, "test-receipt")
        self.assertFalse(eleventh_cycle["bob_reflection_due"])

        state["version"] = 19
        twentieth_cycle = self.engine.context(state, "test-receipt")
        self.assertEqual(twentieth_cycle["bob_reflection_cycle"], 20)
        self.assertTrue(twentieth_cycle["bob_reflection_due"])

    def test_missed_bob_reflection_remains_due_until_valid_post_is_accepted(self):
        state = self.engine.store.load()
        state["version"] = 11
        state["posts"] = {}
        context = self.engine.context(state, "overdue-reflection")
        self.assertTrue(context["bob_reflection_due"])
        self.assertEqual(context["bob_reflection_cycle"], 10)

    def test_context_compaction_deduplicates_schema_allowlists(self):
        self.engine.config["max_context_chars"] = 30000
        with self.engine.store.lock():
            self.engine.initialize()
            self.engine.store.append("project_adopted", {
                "id": "p", "title": "P", "question": "Q", "domain": "entropy",
                "status": "active", "next_step": "N", "reason": "R", "actor": "operator"
            })
            for i in range(6):
                self.engine.store.append("observation", {
                    "id": f"s{i}", "source": f"https://example.org/{i}",
                    "content": json.dumps({"verification_required": True, "topic_domain": "entropy", "excerpt": "x" * 2000}),
                    "actor": "collector", "scope": "collected"
                })
            invocation, request = self.engine.start("fixture", "compact-allowlists")
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})

        self.assertIn("project_evidence", request["context"])
        self.assertTrue(all("resolution_evidence" in c for c in request["context"]["commitments"]))

    def test_context_compaction_rebuilds_schema_from_compacted_context(self):
        calls = []

        def schema(context):
            calls.append(context)
            if len(calls) == 1:
                return {"type": "object", "padding": "x" * self.engine.config["max_context_chars"]}
            return {"type": "object", "marker": "rebuilt"}

        with patch("wake.engine.schema_for_context", side_effect=schema):
            with self.engine.store.lock():
                invocation, request = self.engine.start("fixture", "schema-compaction-test")
                self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})

        self.assertEqual(len(calls), 2)
        self.assertEqual(request["response_schema"], {"type": "object", "marker": "rebuilt"})
        self.assertLessEqual(
            len(json.dumps(request, sort_keys=True, separators=(",", ":"))),
            self.engine.config["max_context_chars"],
        )

    def test_context_overflow_uses_auditable_bounded_working_set(self):
        # The normal rich request may grow without rewriting any durable state.
        # Its final overflow is the one controlled condition that switches the
        # provider view to the deterministic working representation.
        original_context = self.engine.context
        def oversized_context(state, receipt):
            return {**original_context(state, receipt), "noise": "X" * 60000}
        with patch.object(self.engine, "context", side_effect=oversized_context):
            with self.engine.store.lock():
                invocation, request = self.engine.start("fixture", "bounded-context-test")
                item = self.engine.store.load()["invocations"][invocation]
                self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})

        self.assertEqual(request["context"]["context_mode"], "bounded")
        self.assertNotIn("noise", request["context"])
        self.assertEqual(item["context_delivery"]["mode"], "bounded")
        self.assertGreater(item["context_delivery"]["rich_context_chars"], 48000)
        self.assertGreater(item["context_delivery"]["delivered_context_chars"], 0)
        self.assertTrue(item["context_delivery"]["omitted_categories"])
        self.assertEqual(item["inquiry_drive_shadow"]["mode"], "shadow")
        self.assertNotIn("trust_compacts_shadow", request["context"])

    def test_context_exposes_project_scoped_notebook_evidence(self):
        with self.engine.store.lock():
            self.engine.store.append("project_adopted", {
                "id": "p-wake", "title": "WAKE", "question": "Q", "domain": "wake_analysis",
                "status": "active", "next_step": "N", "reason": "R", "actor": "operator"
            })
            self.engine.store.append("project_adopted", {
                "id": "p-neuro", "title": "Neuro", "question": "Q", "domain": "neurodivergence",
                "status": "active", "next_step": "N", "reason": "R", "actor": "operator"
            })
            self.engine.store.append("observation", {
                "id": "wake-src", "source": "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
                "content": json.dumps({"verification_required": True, "topic_domain": "wake_analysis"}),
                "actor": "collector", "scope": "collected"
            })
            self.engine.store.append("observation", {
                "id": "neuro-src", "source": "https://example.org/neuro",
                "content": json.dumps({"verification_required": True, "topic_domain": "neurodivergence"}),
                "actor": "collector", "scope": "collected"
            })
            invocation, request = self.engine.start("fixture", "project-evidence-test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})

        self.assertIn("wake-src", request["context"]["project_evidence"]["p-wake"])
        self.assertNotIn("neuro-src", request["context"]["project_evidence"]["p-wake"])
        self.assertIn("neuro-src", request["context"]["project_evidence"]["p-neuro"])
        self.assertIn("wake-src", request["context"]["project_evidence"]["p-neuro"])

    def test_truncated_discovery_never_becomes_project_evidence(self):
        with self.engine.store.lock():
            self.engine.store.append("project_adopted", {
                "id": "p", "title": "Entropy project", "question": "Q", "domain": "entropy",
                "status": "active", "next_step": "Collect source evidence",
                "reason": "Exercise durable metadata filtering", "actor": "operator"
            })
            self.engine.store.append("observation", {
                "id": "discovery-long",
                "source": "https://api.crossref.org/works?query=entropy",
                "content": json.dumps({
                    "verification_required": True,
                    "topic_domain": "entropy",
                    "evidence_role": "discovery",
                    "scope": "search metadata",
                    "excerpt": "x" * 5000,
                }),
                "actor": "collector", "scope": "collected"
            })
            invocation, request = self.engine.start("fixture", "truncated-discovery-test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})

        delivered = next(item for item in request["context"]["evidence"] if item["id"] == "discovery-long")
        self.assertTrue(delivered["context_excerpt"])
        self.assertNotIn("discovery-long", request["context"]["project_evidence"]["p"])

    def test_retrieval_ignores_unrelated_visible_source_when_project_domain_is_missing(self):
        with self.engine.store.lock():
            self.engine.store.append("project_adopted", {
                "id": "p", "title": "Entropy project", "question": "Q", "domain": "entropy",
                "status": "active", "next_step": "Synthesize entropy evidence",
                "reason": "Exercise project-aware retrieval", "actor": "operator"
            })
            self.engine.store.append("observation", {
                "id": "entropy-old",
                "source": "https://api.crossref.org/works/10.1000/entropy",
                "content": json.dumps({
                    "verification_required": True,
                    "topic_domain": "entropy",
                    "evidence_role": "source",
                    "scope": "abstract metadata",
                    "excerpt": "entropy statistical mechanics Shannon comparison",
                }),
                "actor": "collector", "scope": "collected"
            })
            # Newer source evidence from another domain makes project_evidence
            # non-empty under the cross-topic allowance, but must not suppress
            # recovery of the project's own older source.
            self.engine.store.append("observation", {
                "id": "neuro-new",
                "source": "https://api.crossref.org/works/10.1000/neuro",
                "content": json.dumps({
                    "verification_required": True,
                    "topic_domain": "neurodivergence",
                    "evidence_role": "source",
                    "scope": "abstract metadata",
                    "excerpt": "neurodiversity clinical model comparison",
                }),
                "actor": "collector", "scope": "collected"
            })
            self.engine.store.append("observation", {
                "id": "discovery-new",
                "source": "https://api.crossref.org/works?query=entropy",
                "content": json.dumps({
                    "verification_required": True,
                    "topic_domain": "entropy",
                    "evidence_role": "discovery",
                    "scope": "search metadata",
                    "excerpt": "entropy search result",
                }),
                "actor": "collector", "scope": "collected"
            })
            invocation, request = self.engine.start("fixture", "project-aware-rehydrate-test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})

        self.assertIn("neuro-new", request["context"]["project_evidence"]["p"])
        self.assertIn("entropy-old", request["context"]["project_evidence"]["p"])
        self.assertIn("entropy-old", request["context"]["retrieval_rehydration"]["evidence_ids"])
        self.assertNotIn("discovery-new", request["context"]["project_evidence"]["p"])

    def test_retrieval_rehydrates_older_qualifying_notebook_source(self):
        with self.engine.store.lock():
            self.engine.store.append("project_adopted", {
                "id": "p", "title": "Entropy project", "question": "Q", "domain": "entropy",
                "status": "active", "next_step": "Synthesize qualifying evidence",
                "reason": "Exercise retrieval rehydration", "actor": "operator"
            })
            self.engine.store.append("observation", {
                "id": "qualifying-old",
                "source": "https://api.crossref.org/works/10.1000/example",
                "content": json.dumps({
                    "verification_required": True,
                    "topic_domain": "entropy",
                    "evidence_role": "source",
                    "scope": "abstract metadata",
                    "excerpt": "entropy statistical mechanics bounded comparison",
                }),
                "actor": "collector", "scope": "collected"
            })
            # Fill the ordinary recent collector window with discovery-only
            # records. The older qualifying source must still be selected by
            # retrieval rather than being starved by newer search-result noise.
            for i in range(8):
                self.engine.store.append("observation", {
                    "id": f"discovery-{i}",
                    "source": f"https://api.crossref.org/works?query=entropy-{i}",
                    "content": json.dumps({
                        "verification_required": True,
                        "topic_domain": "entropy",
                        "evidence_role": "discovery",
                        "scope": "search metadata",
                        "excerpt": "entropy search result",
                    }),
                    "actor": "collector", "scope": "collected"
                })
            invocation, request = self.engine.start("fixture", "retrieval-rehydrate-test")
            item = self.engine.store.load()["invocations"][invocation]
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})

        visible = {item["id"] for item in request["context"]["evidence"]}
        self.assertIn("qualifying-old", visible)
        self.assertIn("qualifying-old", request["context"]["project_evidence"]["p"])
        self.assertIn("qualifying-old", request["context"]["retrieval_rehydration"]["evidence_ids"])
        self.assertIn("qualifying-old", item["retrieval_shadow"]["evidence_ids"])
        self.assertFalse(any(
            evidence_id.startswith("discovery-")
            for evidence_id in request["context"]["project_evidence"]["p"]
        ))

    def test_context_exposes_nonruntime_post_commitment_resolution_evidence(self):
        with self.engine.store.lock():
            self.engine.store.append("observation", {
                "id": "pre", "source": "fixture:pre", "content": "old", "actor": "human"
            })
            invocation, request = self.engine.start("fixture", "commit-seed")
            proposal = json.loads(Fixture().propose(request)[0])
            proposal["actions"] = [{
                "type": "commit", "id": "c", "task": "Review new evidence",
                "due_cycle": request["context"]["version"] + 2, "reason": "Test temporal gate"
            }]
            self.engine.finish(invocation, json.dumps(proposal))
            self.engine.store.append("observation", {
                "id": "post", "source": "fixture:post", "content": "new", "actor": "human"
            })
            second, second_request = self.engine.start("fixture", "commit-check")
            self.engine.store.append("recovered", {"id": second, "reason": "Test cleanup"})

        commitment = next(item for item in second_request["context"]["commitments"] if item["id"] == "c")
        self.assertIn("post", commitment["resolution_evidence"])
        self.assertNotIn("pre", commitment["resolution_evidence"])

    def test_schema_constrains_resolve_to_eligible_commitment_evidence(self):
        context = {
            "research_topics": [],
            "projects": [],
            "blog_notebooks": {},
            "commitments": [{
                "id": "c1",
                "resolution_evidence": ["new-1", "new-2"],
            }],
        }
        schema = schema_for_context(context)
        choices = schema["properties"]["actions"]["items"]["anyOf"]
        resolves = [item for item in choices if item["properties"]["type"]["enum"] == ["resolve"]]
        self.assertEqual(len(resolves), 1)
        self.assertEqual(resolves[0]["properties"]["id"]["enum"], ["c1"])
        self.assertEqual(
            resolves[0]["properties"]["evidence"]["items"]["enum"],
            ["new-1", "new-2"],
        )

    def test_schema_constrains_reframe_observations_to_visible_evidence_ids(self):
        context = {
            "research_topics": [],
            "projects": [{"id": "p", "domain": "entropy"}],
            "evidence": [
                {"id": "source-a", "actor": "collector"},
                {"id": "runtime-b", "actor": "runtime"},
            ],
            "blog_notebooks": {},
            "commitments": [],
        }
        schema = schema_for_context(context)
        choices = schema["properties"]["actions"]["items"]["anyOf"]
        reframe = next(item for item in choices if item["properties"]["type"]["enum"] == ["reframe"])
        self.assertEqual(
            reframe["properties"]["observations"]["items"]["enum"],
            ["runtime-b", "source-a"],
        )
        self.assertEqual(reframe["properties"]["project"]["enum"], ["p"])

    def test_schema_omits_reframe_when_no_visible_evidence_exists(self):
        context = {
            "research_topics": [],
            "projects": [{"id": "p", "domain": "entropy"}],
            "evidence": [],
            "blog_notebooks": {},
            "commitments": [],
        }
        schema = schema_for_context(context)
        choices = schema["properties"]["actions"]["items"]["anyOf"]
        self.assertFalse(any(
            item["properties"]["type"]["enum"] == ["reframe"]
            for item in choices
        ))

    def test_reframe_prompt_defines_observations_as_existing_evidence_ids(self):
        self.assertIn("observations is an array of EXISTING evidence IDs", RESEARCH_SYSTEM)
        self.assertIn("observations MUST contain only exact IDs already present in context.evidence", RESEARCH_SYSTEM)

    def test_overdue_resolution_requires_post_commitment_evidence_instruction(self):
        self.assertIn("recorded at or after that commitment's", RESEARCH_SYSTEM)
        self.assertIn("Do not cite only older evidence in resolve", RESEARCH_SYSTEM)

    def test_overdue_commitments_prioritize_synthesis_before_more_research(self):
        self.assertIn("completing that work takes priority over starting", RESEARCH_SYSTEM)
        self.assertIn("synthesize it into the relevant notebook and resolve", RESEARCH_SYSTEM)
        self.assertIn("Do not treat \"more sources would be nice\" as a sufficient gap.", RESEARCH_SYSTEM)

    def test_wake_topic_is_a_rotating_breadcrumb_not_a_system_instruction(self):
        settings = {**DEFAULTS, "mission": "Follow useful questions.",
                    "research_topics": [{"id": "self_study", "label": "Self study", "query": "runtime",
                                         "enabled": True, "source_kind": "repository",
                                         "repository": "sudofx/wake"}]}
        engine = Engine(self.root/"breadcrumb", settings)
        calls = []
        try:
            with engine.store.lock():
                engine.initialize()
                collect(engine, fetcher=lambda url: calls.append(url) or
                        {"url": url, "scope": "fixture", "excerpt": "A sufficiently long test source excerpt for collection."})
            self.assertEqual(calls, ["https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1"])
            self.assertNotIn("source-controlled", RESEARCH_SYSTEM.lower())
            self.assertNotIn("wake_analysis", RESEARCH_SYSTEM.lower())
        finally:
            engine.store.close()

    def test_new_projects_are_bounded_and_rejection_is_atomic(self):
        result = self.propose([project(str(i)) for i in range(4)])
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(self.engine.store.load()["projects"], {})
        self.assertEqual(self.propose([project(str(i)) for i in range(3)])["status"], "accepted")

    def test_project_can_queue_research_in_another_configured_topic(self):
        action = dict(type="research", id="q", project="p", query="symmetry breaking",
                      domain="entropy", reason="Test a cross-topic relationship")
        self.assertEqual(self.propose([project(), action])["status"], "accepted")

    def test_project_can_research_its_retired_original_topic(self):
        self.assertEqual(self.propose([project()])["status"], "accepted")
        self.engine.config["research_topics"] = [
            topic for topic in self.engine.config["research_topics"] if topic["id"] != "entropy"]
        with self.engine.store.lock():
            self.engine.initialize()
        action = dict(type="research", id="q", project="p", query="cellular automata",
                      domain="entropy", reason="Continue the existing investigation")
        self.assertEqual(self.propose([action])["status"], "accepted")

    def test_completion_requires_a_notebook(self):
        self.propose([project()])
        self.assertEqual(self.propose([project(status="completed")])["status"], "rejected")

    def test_notebooks_reject_receipts_and_failed_sources(self):
        self.propose([project()])
        self.source("s1")
        self.source("s2", status="failed")
        self.assertEqual(self.propose([notebook(["s1", "s2"])])["status"], "rejected")
        receipt = next(e["id"] for e in self.engine.store.load()["evidence"].values() if e["actor"] == "runtime")
        self.assertEqual(self.propose([notebook(["s1", receipt])])["status"], "rejected")

    def test_wake_repository_urls_are_repo_scoped(self):
        good = "https://raw.githubusercontent.com/sudofx/wake/master/README.md"
        self.assertEqual(allowed_url(good), good)
        with self.assertRaises(ValueError):
            allowed_url("https://raw.githubusercontent.com/other/repo/master/README.md")

    def test_wake_analysis_notebook_requires_wake_repository_sources(self):
        self.source("r1", "https://raw.githubusercontent.com/sudofx/wake/master/README.md")
        self.source("r2", "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md")
        action = project(); action["domain"] = "wake_analysis"
        self.assertEqual(self.propose([action, notebook(["r1", "r2"])])["status"], "accepted")

        other = Engine(self.root/"other", charter_settings("test"))
        original = self.engine
        try:
            with other.store.lock(): other.initialize()
            self.engine = other
            self.source("s1")
            self.source("s2", "https://api.crossref.org/works?query=test")
            action = project(); action["domain"] = "wake_analysis"
            self.assertEqual(self.propose([action, notebook(["s1", "s2"])])["status"], "rejected")
        finally:
            self.engine = original
            other.store.close()

    def test_wake_analysis_notebook_schema_excludes_external_evidence(self):
        context = {
            "projects": [{"id": "wake", "domain": "wake_analysis"},
                         {"id": "other", "domain": "entropy"}],
            "evidence": [
                {"id": "wake-source", "actor": "collector",
                 "source": "https://raw.githubusercontent.com/sudofx/wake/master/wake/store.py"},
                {"id": "external-source", "actor": "collector",
                 "source": "https://api.crossref.org/works?query=wake"},
            ],
            "project_evidence": {
                "wake": ["wake-source"],
                "other": ["wake-source", "external-source"],
            },
        }
        alternatives = schema_for_context(context)["properties"]["actions"]["items"]["anyOf"]
        notebooks = [item for item in alternatives if item["properties"]["type"]["enum"] == ["notebook"]]
        wake = next(item for item in notebooks if item["properties"]["project"]["enum"] == ["wake"])
        other = next(item for item in notebooks if item["properties"]["project"]["enum"] == ["other"])
        self.assertEqual(wake["properties"]["evidence"]["items"]["enum"], ["wake-source"])
        self.assertEqual(other["properties"]["evidence"]["items"]["enum"], ["external-source", "wake-source"])

    def test_wake_source_context_is_distinct_and_bounded(self):
        action = project(); action["domain"] = "wake_analysis"
        self.assertEqual(self.propose([action])["status"], "accepted")
        urls = [
            "https://raw.githubusercontent.com/sudofx/wake/master/README.md",
            "https://raw.githubusercontent.com/sudofx/wake/master/docs/architecture.md",
            "https://raw.githubusercontent.com/sudofx/wake/master/wake/store.py",
            "https://raw.githubusercontent.com/sudofx/wake/master/wake/provenance.py",
            "https://raw.githubusercontent.com/sudofx/wake/master/wake/engine.py",
        ]
        for index, url in enumerate(urls):
            self.source(f"wake-{index}", url)
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "source-budget")
            self.engine.store.append("failed", {"id": invocation, "reason": "Test cleanup"})
        sources = [item for item in request["context"]["evidence"]
                   if item.get("actor") == "collector"
                   and item["source"].startswith("https://raw.githubusercontent.com/sudofx/wake/")]
        self.assertEqual(len(sources), 4)
        self.assertEqual(len({item["source"] for item in sources}), 4)
        self.assertLessEqual(len(json.dumps(request, sort_keys=True, separators=(",", ":"))),
                             self.engine.config["max_context_chars"])

    def test_provisional_notebook_can_use_one_collected_source(self):
        self.propose([project()])
        self.source("s1", "https://plato.stanford.edu/entries/consciousness/")
        result = self.propose([notebook(["s1"], "A bounded comparison follows the collected source [s1].")])
        self.assertEqual(result["status"], "accepted")
        export(self.engine.store, self.root/"site")
        rendered = (self.root/"site/notebooks/n.md").read_text()
        self.assertIn("Evidence profile · 1 distinct source URL", rendered)

    def test_single_source_notebook_does_not_lower_blog_promotion_gate(self):
        self.source("s1")
        result = self.propose([project(), notebook(["s1"], "A bounded comparison follows [s1]."),
                               self.blog(evidence=["s1"])])
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["editorial"]["status"], "withheld")
        self.assertIn("n", self.engine.store.load()["notebooks"])
        self.assertEqual(self.engine.store.load()["posts"], {})

    def test_revision_requires_changed_findings_and_new_evidence(self):
        self.source("s1")
        self.source("s2")
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"])])["status"], "accepted")
        self.assertEqual(self.propose([notebook(["s1", "s2"], "Changed")])["status"], "rejected")
        self.source("s3")
        self.assertEqual(self.propose([notebook(["s1", "s3"], "Changed with evidence [s3]."), project(status="completed")])["status"], "accepted")
        export(self.engine.store, self.root/"site")
        reconstructed, _ = verify_history(self.root/"site/events.jsonl", (self.root/"site/head.txt").read_text())
        self.assertEqual(reconstructed, self.engine.store.load())
        self.assertEqual(reconstructed["notebooks"]["n"]["revision"], 2)
        self.assertIn("Changed with evidence", (self.root/"site/notebooks/n.md").read_text())

    def test_sources_and_notebook_text_cannot_inject_scripts(self):
        self.source("s1")
        self.source("s2")
        self.propose([project(), notebook(["s1", "s2"], '</script><script>alert("no")</script>')])
        export(self.engine.store, self.root/"site")
        self.assertNotIn('</script><script>alert', (self.root/"site/index.html").read_text())

    def blog(self, evidence=("s1", "s2"), **changes):
        action = dict(type="blog", id="post-one", project="p", title="The useful disagreement",
            lede="Two sources describe the same problem from different angles.",
            body=("The notebook exposed a useful disagreement between the collected accounts. "
                  "Neither source settles the question alone, and the limitation matters. "
                  "The interesting result is the shape of the disagreement: each account measures "
                  "a different part of the problem, so treating them as direct rivals would hide "
                  "what each can actually support. The next investigation should test that gap."),
            notebooks=["n"], evidence=list(evidence),
            reason="A new source-backed notebook exposed a substantive disagreement worth explaining.",
            lens="Good observation leaves room for the observed to change the map.")
        action.update(changes)
        return action

    def test_boring_wake_produces_no_blog_post(self):
        self.assertEqual(self.propose([project()])["status"], "accepted")
        self.assertEqual(self.engine.store.load()["posts"], {})

    def test_tenth_accepted_wake_cannot_advance_without_valid_bob_reflection(self):
        self.assertEqual(self.propose([project()])["status"], "accepted")
        for _ in range(8):
            self.assertEqual(self.propose([])["status"], "accepted")
        self.assertEqual(self.engine.store.load()["version"], 9)

        missing = self.propose([])
        self.assertEqual(missing["status"], "rejected")
        self.assertIn("Bob reflection for accepted wake 10 is mandatory", missing["reason"])
        self.assertEqual(self.engine.store.load()["version"], 9)

        body = (
            "I'm Bob, the public correspondent for WAKE✳. WAKE✳ carries durable research state "
            "across disposable model invocations, and I will write here when the record produces "
            "something worth sharing. This is the first public reflection. Across the first ten "
            "accepted wakes, the useful pattern is not a claim of consciousness or hidden memory; "
            "it is the visible tension between persistent obligations, evidence gates, provider "
            "availability, and disposable model calls. The record shows what survived each handoff "
            "and where the process remained blocked. My job is to translate those receipts without "
            "turning continuity into a stronger claim than the evidence supports."
        )
        reflection = self.blog(
            id="bob-cycle-10", notebooks=[], evidence=[], reflection_cycle=10,
            title="What survived the first ten wakes",
            lede="A first look at the durable journey rather than a research result.",
            body=body,
            reason="The mandatory ten-cycle milestone calls for a public reflection on the durable journey.",
            lens="The interesting part is the boundary between continuity of record and continuity of mind."
        )
        accepted = self.propose([reflection])
        self.assertEqual(accepted["status"], "accepted")
        post = self.engine.store.load()["posts"]["bob-cycle-10"]
        self.assertEqual(post["reflection_cycle"], 10)
        self.assertEqual(post["created_version"], 10)

    def test_significant_notebook_can_create_a_durable_blog_post(self):
        self.source("s1")
        self.source("s2")
        result = self.propose([project(), notebook(["s1", "s2"]), self.blog()])
        self.assertEqual(result["status"], "accepted")
        state = self.engine.store.load()
        self.assertEqual(state["posts"]["post-one"]["created_by"], result["id"])
        reconstructed, _ = self.engine.store.replay()
        self.assertEqual(reconstructed["posts"], state["posts"])
        export(self.engine.store, self.root/"site")
        markdown = (self.root/"site/blog/post-one.md").read_text()
        html = (self.root/"site/index.html").read_text()
        standalone = (self.root/"site/blog/post-one.html").read_text()
        self.assertIn("Bob's Lens — philosophical reflection", markdown)
        self.assertIn("Exact wake and decision", markdown)
        self.assertIn("The useful disagreement", html)
        self.assertIn("font-variant-emoji:text", (Path(__file__).resolve().parents[1]/"wake/assets/style.css").read_text())
        self.assertIn("font-variant-emoji:text", standalone)
        self.assertIn("WAKE✳︎", standalone)

    def test_historical_blog_wordmark_is_normalized_only_in_presentation(self):
        self.source("s1")
        self.source("s2")
        body = (
            "Hello. I'm Bob, the public correspondent for WAKE✳. "
            "This historical record deliberately stores the bare mark while the browser export "
            "normalizes it to the text presentation. " * 4
        )
        result = self.propose([project(), notebook(["s1", "s2"]), self.blog(body=body)])
        self.assertEqual(result["status"], "accepted")
        state = self.engine.store.load()
        self.assertIn("WAKE✳.", state["posts"]["post-one"]["body"])
        export(self.engine.store, self.root/"site")
        standalone = (self.root/"site/blog/post-one.html").read_text()
        markdown = (self.root/"site/blog/post-one.md").read_text()
        index = (self.root/"site/index.html").read_text()
        self.assertIn('<strong class="wake-mark">WAKE✳︎</strong>.', standalone)
        self.assertIn("**WAKE✳︎**.", markdown)
        self.assertIn("replaceAll('WAKE✳︎','WAKE✳').replaceAll('WAKE✳','WAKE✳︎')", index)

    def test_invalid_blog_is_withheld_while_research_is_accepted_and_replayable(self):
        self.source("s1")
        self.source("s2")
        bad = self.blog(["s1", "missing"])
        result = self.propose([project(), notebook(["s1", "s2"]), bad])
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["editorial"]["status"], "withheld")
        state = self.engine.store.load()
        self.assertIn("p", state["projects"])
        self.assertIn("n", state["notebooks"])
        self.assertEqual(state["posts"], {})
        receipt = next(event["payload"] for event in reversed(self.engine.store.events()) if event["kind"] == "accepted")
        self.assertEqual(receipt["editorial"]["action"], bad)
        self.assertEqual(len(receipt["proposal"]["actions"]), 2)
        self.assertEqual(len(json.loads(receipt["raw_response"])["actions"]), 3)
        self.assertIn("withheld", state["journal"][-1]["summary"])
        export(self.engine.store, self.root/"site")
        reconstructed, _ = verify_history(self.root/"site/events.jsonl", (self.root/"site/head.txt").read_text())
        self.assertEqual(reconstructed, state)

    def test_blog_withholding_never_bypasses_research_or_envelope_validation(self):
        self.source("s1")
        self.source("s2")
        for actions in ([project(), notebook(["s1", "missing"]), self.blog()],
                        [self.blog(), project()], [project(), self.blog(), self.blog()],
                        [project(str(i)) for i in range(12)] + [self.blog()],
                        [self.blog()]):
            with self.subTest(actions=actions):
                self.assertEqual(self.propose(actions)["status"], "rejected")
                self.assertEqual(self.engine.store.load()["version"], 0)
                self.assertEqual(self.engine.store.load()["projects"], {})

    def test_existing_durable_notebook_can_support_a_later_blog_post(self):
        self.source("s1")
        self.source("s2")
        self.propose([project(), notebook(["s1", "s2"])])
        self.assertEqual(self.propose([self.blog()])["status"], "accepted")
        self.assertIn("post-one", self.engine.store.load()["posts"])

    def test_blog_context_survives_fresh_invocation_without_full_bodies(self):
        self.source("s1")
        self.source("s2")
        self.propose([project(), notebook(["s1", "s2"]), self.blog()])
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "fresh")
            context = request["context"]["recent_blog"]
            self.assertEqual(context[0]["id"], "post-one")
            self.assertNotIn("body", context[0])
            available = request["context"]["blog_notebooks"]
            self.assertEqual(available["p"][0]["id"], "n")
            self.assertEqual(available["p"][0]["evidence"], ["s1", "s2"])
            self.assertIn("status", context[0])
            self.assertEqual(request["context"]["editorial_notes"], [])
            self.engine.store.append("failed", {"id": invocation, "reason": "test cleanup"})

    def test_editorial_review_notes_reach_fresh_invocations_without_becoming_evidence(self):
        note = ("Review Bob post post-one for possible overstatement; if evidence supports a narrower "
                "claim, publish a transparent correction rather than rewriting history.")
        engine = Engine(self.root/"editorial", charter_settings("Explore.", editorial_notes=[note]))
        try:
            with engine.store.lock():
                engine.initialize()
                invocation, request = engine.start("fixture", "editorial-test")
                self.assertEqual(request["context"]["editorial_notes"], [note])
                self.assertFalse(any(item.get("source") == "operator:editorial"
                                     for item in request["context"]["evidence"]))
                engine.store.append("failed", {"id": invocation, "reason": "test cleanup"})
        finally:
            engine.store.close()

    def test_blog_does_not_add_a_provider_call(self):
        self.source("s1")
        self.source("s2")
        outer = self
        class OneCall(Fixture):
            calls = 0
            def propose(self, request):
                self.calls += 1
                proposal = dict(base_version=request["context"]["version"], title="Research fixture",
                    summary="One model response contains research and optional editorial work.",
                    actions=[project(), notebook(["s1", "s2"]), outer.blog()])
                return json.dumps(proposal), {"simulated": True}
        provider = OneCall()
        self.assertEqual(self.engine.run(provider)["status"], "accepted")
        self.assertEqual(provider.calls, 1)
        self.assertIn("post-one", self.engine.store.load()["posts"])

    def test_quantum_metaphor_cannot_masquerade_as_scientific_causation(self):
        self.source("s1")
        self.source("s2")
        bad = self.blog(body=("Quantum mechanics proves empathy and explains relationships. " * 20))
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"]), bad])["status"], "accepted")
        self.assertEqual(self.engine.store.load()["posts"], {})

    def test_honest_quantum_boundary_is_allowed(self):
        self.source("s1")
        self.source("s2")
        safe = self.blog(body=("Quantum mechanics does not explain consciousness. "
                               "The useful connection here is a philosophical prompt about observation, "
                               "uncertainty, and the limits of intuition. The research notebook keeps "
                               "measurement separate from interpretation and links every claim to its "
                               "source. That boundary is part of the result, not a footnote. " * 2))
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"]), safe])["status"], "accepted")

    def test_abstract_only_sources_cannot_support_inflated_certainty(self):
        self.source("s1", source_scope="abstract only")
        self.source("s2", source_scope="preprint abstract")
        inflated = self.blog(body=("The sources provide definitive and conclusive proof. " * 10))
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"]), inflated])["status"], "accepted")
        self.assertEqual(self.engine.store.load()["posts"], {})

    def test_blog_rejects_contested_synthesis_presented_as_established_fact(self):
        self.source("s1")
        self.source("s2")
        self.propose([project(), notebook(["s1", "s2"])])
        for body in (
            "The literature separates agency and consciousness along clean functional fault lines. " * 6,
            "External scaffolding allows genuine epistemic self-governance without consciousness. " * 6,
            "The collected literature demonstrates that agency does not require consciousness. " * 6,
        ):
            with self.subTest(body=body[:50]):
                result = self.propose([project(), self.blog(body=body)])
                self.assertEqual(result["status"], "accepted")
                self.assertEqual(result["editorial"]["status"], "withheld")
                self.assertEqual(self.engine.store.load()["posts"], {})

    def test_blog_allows_explicitly_calibrated_synthesis(self):
        self.source("s1")
        self.source("s2")
        body = (
            "Our reading of the collected sources suggests a useful functional distinction between "
            "metacognitive regulation and phenomenal consciousness. The notebook treats that as a "
            "provisional synthesis rather than proof that the concepts are cleanly separable in every "
            "theory or implementation. One interpretation is that external records can support some "
            "forms of error regulation without settling whether that deserves the stronger label of "
            "epistemic agency. The distinction is useful precisely because the broader philosophical "
            "question remains open."
        )
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"]), self.blog(body=body)])["status"], "accepted")

    def test_stricter_blog_policy_does_not_invalidate_accepted_history_on_replay(self):
        self.source("s1")
        self.source("s2")
        body = ("External scaffolding allows genuine epistemic self-governance without consciousness. " * 6)
        # Simulate an event accepted before the newer overclaim policy existed.
        with patch("wake.governance._blog_language", return_value=None):
            result = self.propose([project(), notebook(["s1", "s2"]), self.blog(body=body)])
        self.assertEqual(result["status"], "accepted")
        replayed, _ = self.engine.store.replay()
        self.assertIn("post-one", replayed["posts"])
        self.assertIn("genuine epistemic self-governance", replayed["posts"]["post-one"]["body"])
        export(self.engine.store, self.root/"site")
        audited, _ = verify_history(self.root/"site/events.jsonl", (self.root/"site/head.txt").read_text())
        self.assertEqual(audited, replayed)
        graph = json.loads((self.root/"site/map-data.json").read_text())
        self.assertIn("blog:post-one", graph["blogs"])

    def test_correction_preserves_the_original_post(self):
        self.source("s1")
        self.source("s2")
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"]), self.blog()])["status"], "accepted")
        self.source("s3")
        correction = self.blog(id="post-two", evidence=["s1", "s3"], supersedes="post-one",
            title="A correction to the useful disagreement",
            body=("A newly collected source changes how the earlier disagreement should be described. "
                  "The original post remains in the record, but this note replaces its conclusion. "
                  "The evidence now supports a narrower comparison and leaves the broader claim open. "
                  "That is a meaningful change rather than a cosmetic rewrite, and the linked notebook "
                  "records the new source, revised finding, limitation, and next question."))
        revised = notebook(["s1", "s3"], "A narrower comparison follows the new evidence [s1] [s3].")
        self.assertEqual(self.propose([revised, correction])["status"], "accepted")
        posts = self.engine.store.load()["posts"]
        self.assertEqual(posts["post-one"]["status"], "superseded")
        self.assertEqual(posts["post-one"]["superseded_by"], "post-two")
        self.assertEqual(posts["post-two"]["supersedes"], "post-one")

    def test_collector_attempts_two_requests_and_records_failures(self):
        actions = [project()]+[dict(type="research", id=f"q{i}", project="p", query="consciousness", domain="entropy", reason="Compare") for i in range(4)]
        self.propose(actions)
        calls=[]
        def fetch(url):
            calls.append(url)
            if len(calls)==1: raise OSError("Unavailable")
            return dict(url=url, scope="synthetic test fixture", excerpt="Test source")
        with self.engine.store.lock(): collect(self.engine, fetcher=fetch)
        state=self.engine.store.load()
        self.assertEqual(len(calls), 2)
        configured = {topic["id"] for topic in state["research_topics"]}
        collected_domains = {
            json.loads(e["content"]).get("topic_domain")
            for e in state["evidence"].values()
            if e.get("scope") == "collected" and e.get("actor") == "collector"
        }
        self.assertTrue(collected_domains <= configured)
        self.assertEqual(len(collected_domains), 1)  # first fetch failed; second succeeded
        statuses = [r["status"] for r in state["research"].values()]
        self.assertEqual(statuses.count("failed"), 1)
        self.assertEqual(statuses.count("queued"), 3)
        collected = [e for e in state["evidence"].values() if e.get("scope") == "collected" and e.get("actor") == "collector"]
        payload = json.loads(collected[-1]["content"])
        self.assertIs(payload["verification_required"], True)
        self.assertIn(payload["topic_domain"], configured)


    def test_queued_followup_gets_one_slot_and_neutral_discovery_keeps_one(self):
        self.propose([project(), dict(type="research", id="q-follow", project="p",
            query="cellular automata symmetry followup", domain="entropy", reason="Continue active work")])
        calls = []
        with patch("wake.research.secrets.SystemRandom.choice", side_effect=lambda seq: seq[0]), \
             patch("wake.research.secrets.SystemRandom.sample", side_effect=lambda seq, n: list(seq)[:n]):
            with self.engine.store.lock():
                collect(self.engine, fetcher=lambda url: calls.append(url) or
                        {"url": url, "scope": "fixture", "excerpt": "A sufficiently long test source excerpt."})
        self.assertEqual(len(calls), 2)
        self.assertTrue(any("cellular+automata+symmetry+followup" in url or
                            "cellular%20automata%20symmetry%20followup" in url for url in calls))
        self.assertTrue(any("query=symmetry" not in url and "search=symmetry" not in url for url in calls))
        self.assertEqual(self.engine.store.load()["research"]["q-follow"]["status"], "collected")

    def test_queued_exact_source_url_is_not_replaced_by_another_search(self):
        exact = "https://api.crossref.org/works/10.1016%2Fj.example.2026.01.001"
        self.propose([project(), dict(type="research", id="q-exact", project="p",
            query="entropy sensory processing", domain="entropy", url=exact,
            reason="Inspect the individual paper selected from discovery")])
        calls = []
        with patch("wake.research.secrets.SystemRandom.choice", side_effect=lambda seq: seq[0]), \
             patch("wake.research.secrets.SystemRandom.sample", side_effect=lambda seq, n: list(seq)[:n]):
            with self.engine.store.lock():
                collect(self.engine, fetcher=lambda url: calls.append(url) or
                        {"url": url, "scope": "fixture", "excerpt": "A sufficiently long source record."})
        self.assertIn(exact, calls)
        evidence = next(e for e in self.engine.store.load()["evidence"].values() if e["source"] == exact)
        self.assertEqual(json.loads(evidence["content"])["evidence_role"], "source")

    def test_discovery_results_cannot_qualify_a_notebook(self):
        with self.engine.store.lock():
            for identifier in ("s1", "s2"):
                self.engine.store.append("observation", dict(
                    id=identifier, source="https://api.crossref.org/works?query=entropy",
                    content=json.dumps({"scope":"search metadata", "excerpt":"entropy sensory processing autism",
                                        "verification_required":True, "topic_domain":"entropy",
                                        "evidence_role":"discovery"}),
                    actor="collector", scope="collected"))
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"])])["status"], "rejected")

    def test_attention_nudge_avoids_active_project_domain_every_fourth_invocation(self):
        self.propose([project()])
        # Four completed invocations trigger the attention nudge on collection.
        for _ in range(3):
            self.propose([])
        calls = []
        with patch("wake.research.secrets.SystemRandom.choice", side_effect=lambda seq: seq[0]), \
             patch("wake.research.secrets.SystemRandom.sample", side_effect=lambda seq, n: list(seq)[:n]):
            with self.engine.store.lock():
                collect(self.engine, fetcher=lambda url: calls.append(url) or
                        {"url": url, "scope": "fixture", "excerpt": "A sufficiently long test source excerpt."})
        self.assertEqual(len(calls), 2)
        self.assertNotIn("query=symmetry", calls[0])

    def test_retired_followups_do_not_exhaust_queue_capacity(self):
        actions = [project()]+[dict(type="research", id=f"q{i}", project="p", query="follow up",
            domain="entropy", reason="Test queue lifecycle") for i in range(4)]
        self.propose(actions)
        for _ in range(4):
            with self.engine.store.lock():
                collect(self.engine, fetcher=lambda url: dict(url=url, scope="fixture",
                    excerpt="cellular automata bounded comparison evidence"))
        self.assertTrue(all(item["status"] == "collected"
                            for item in self.engine.store.load()["research"].values()))
        result = self.propose([dict(type="research", id="q-next", project="p", query="next follow up",
            domain="entropy", reason="Queue remains usable")])
        self.assertEqual(result["status"], "accepted")

    def test_notebook_rejects_unrelated_sources_as_corroboration(self):
        with self.engine.store.lock():
            for identifier in ("s1", "s2"):
                self.engine.store.append("observation", dict(
                    id=identifier, source="https://plato.stanford.edu/entries/"+identifier,
                    content=json.dumps({"scope":"synthetic test fixture", "excerpt":"Only a fixture",
                                        "verification_required":True}),
                    actor="collector", scope="collected"))
        proposal = [project(), notebook(["s1", "s2"], "Volcanic aerosols measurably cool global surface temperatures.")]
        self.assertEqual(self.propose(proposal)["status"], "rejected")

    def test_verified_notebook_accepts_single_same_topic_source(self):
        with self.engine.store.lock():
            self.engine.store.append("observation", dict(
                id="s1", source="https://plato.stanford.edu/entries/s1",
                content=json.dumps({"scope":"synthetic test fixture",
                                    "excerpt":"bounded comparison cellular automata explanations",
                                    "verification_required":True,
                                    "topic_domain":"entropy"}),
                actor="collector", scope="collected"))
        findings = "A bounded comparison of cellular automata explanations follows [s1]."
        self.assertEqual(self.propose([project(), notebook(["s1"], findings)])["status"], "accepted")

    def test_verified_notebook_accepts_material_cross_topic_evidence(self):
        with self.engine.store.lock():
            self.engine.store.append("observation", dict(
                id="s1", source="https://plato.stanford.edu/entries/s1",
                content=json.dumps({"scope":"synthetic test fixture",
                                    "excerpt":"bounded comparison cellular automata explanations",
                                    "verification_required":True, "topic_domain":"music"}),
                actor="collector", scope="collected"))
        findings = "A bounded comparison of cellular automata explanations follows [s1]."
        self.assertEqual(self.propose([project(), notebook(["s1"], findings)])["status"], "accepted")

    def test_topic_discovery_rotates_between_independent_indexes(self):
        topic = {"id": "music", "label": "Music", "query": "music"}
        even = discovery_urls(topic, 0)
        odd = discovery_urls(topic, 1)
        self.assertEqual(len(even), 2)
        self.assertIn("en.wikipedia.org", even[0])
        self.assertIn("api.crossref.org", even[1])
        self.assertEqual(odd[0], even[0])
        self.assertIn("api.openalex.org", odd[1])

    def test_repository_topic_capability_is_configured_not_name_bound(self):
        topic = {"id": "self_study", "label": "Self study", "query": "runtime architecture",
                 "enabled": True, "source_kind": "repository", "repository": "sudofx/wake"}
        routes = discovery_urls(topic, 7)
        self.assertEqual(len(routes), 2)
        self.assertTrue(all(
            url.startswith("https://raw.githubusercontent.com/sudofx/wake/")
            or url.startswith("https://api.github.com/repos/sudofx/wake/")
            for url in routes
        ))
        self.assertIn(
            "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
            list(repository_sources("sudofx/wake").values()),
        )
        self.assertEqual(
            allowed_url("https://raw.githubusercontent.com/sudofx/wake/master/tests/unlisted_future_test.py"),
            "https://raw.githubusercontent.com/sudofx/wake/master/tests/unlisted_future_test.py",
        )

    def test_source_url_allowlist_and_input_types(self):
        for url in ("http://arxiv.org/", "https://127.0.0.1/", "https://arxiv.org.evil.example/", "https://a@arxiv.org/", "https://arxiv.org:444/", {}, None):
            with self.subTest(url=url), self.assertRaises(ValueError): allowed_url(url)
        self.assertEqual(allowed_url("https://arxiv.org/abs/1234.56789"), "https://arxiv.org/abs/1234.56789")

    def test_broader_trusted_source_hosts_are_allowed(self):
        urls = [
            "https://api.datacite.org/dois/10.1234/example",
            "https://www.frontiersin.org/journals/neuroscience/articles/10.3389/example/full",
            "https://eric.ed.gov/?id=EJ123456",
            "https://academic.oup.com/example",
            "https://www.cambridge.org/core/journals/example",
            "https://royalsocietypublishing.org/doi/10.1098/example",
            "https://www.biomedcentral.com/articles/example",
            "https://www.bmj.com/content/example",
            "https://jamanetwork.com/journals/example/fullarticle/example",
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(allowed_url(url), url)

    def test_index_rotation_includes_semantic_scholar_and_datacite(self):
        routes = research_urls("neurodiversity paradigm", "neurodivergence", attempts=0)
        self.assertEqual(len(routes), 4)
        self.assertTrue(any("api.crossref.org" in url for url in routes))
        self.assertTrue(any("api.openalex.org" in url for url in routes))
        self.assertTrue(any("api.semanticscholar.org" in url for url in routes))
        self.assertTrue(any("api.datacite.org" in url for url in routes))
        rotated = research_urls("neurodiversity paradigm", "neurodivergence", attempts=1)
        self.assertNotEqual(routes[0], rotated[0])

    def test_broad_index_queries_remain_discovery_only(self):
        routes = research_urls("working memory", "psychology", attempts=0)
        self.assertTrue(all(evidence_role(url) == "discovery" for url in routes))
        self.assertEqual(
            evidence_role("https://api.datacite.org/dois/10.1234/example"),
            "source",
        )

    def test_host_tiers_distinguish_fulltext_metadata_preprint_and_publishers(self):
        self.assertEqual(host_tier("https://www.frontiersin.org/articles/example"), "verification-fulltext")
        self.assertEqual(host_tier("https://api.datacite.org/dois/10.1234/example"), "verification-metadata")
        self.assertEqual(host_tier("https://arxiv.org/abs/1234.56789"), "preprint")
        self.assertEqual(host_tier("https://academic.oup.com/example"), "verification-publisher")

    def test_failed_remote_checkpoint_prevents_model_request(self):
        class NeverCall(Fixture):
            charged=True
            def propose(self, request): raise AssertionError("Model must not be called")
        def failure(): raise OSError("Push failed")
        with self.assertRaises(OSError): self.engine.run(NeverCall(), checkpoint=failure)
        self.assertIsNotNone(self.engine.store.load()["pending"])


class CloudPersistenceTests(unittest.TestCase):
    def test_new_runner_recovers_reserved_attempt_without_refund(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            def git(*args): return subprocess.run(["git", *map(str,args)],check=True,capture_output=True,text=True)
            remote, runner = root/"remote.git", root/"runner"
            git("init","--bare",remote)
            git("init",runner)
            (runner/"README.md").write_text("Source stays separate")
            git("-C",runner,"add","README.md")
            git("-C",runner,"-c","user.name=test","-c","user.email=test@example.com","commit","-m","Source")
            git("-C",runner,"remote","add","origin",remote)
            branch=StateBranch(runner,root/"state-one")
            branch.open()
            settings={**DEFAULTS,"daily_call_limit":1}
            engine=Engine(branch.checkout/"data",settings)
            try:
                with engine.store.lock():
                    engine.initialize()
                    engine.start("gemini","test",charged=True)
                    branch.checkpoint()
            finally: engine.store.close()
            # A genuinely separate clone reads only the remotely checkpointed record.
            git("clone","--branch","wake-state",remote,root/"fresh-runner")
            other=StateBranch(root/"fresh-runner",root/"state-two")
            other.open()
            reopened=Engine(other.checkout/"data",settings)
            try:
                with reopened.store.lock():
                    state=reopened.recover()
                    self.assertEqual(next(iter(state["invocations"].values()))["status"],"recovered")
                    with self.assertRaisesRegex(Rejected,"Daily call ceiling"):
                        reopened.start("gemini","test",charged=True)
                self.assertFalse((other.checkout/"README.md").exists())
            finally: reopened.store.close()


    def test_public_persona_is_explicitly_a_translation_layer(self):
        from wake.providers import RESEARCH_SYSTEM
        self.assertIn("public-facing translation layer", RESEARCH_SYSTEM)
        self.assertIn("persona must never be presented as the mechanism", RESEARCH_SYSTEM)
        self.assertIn("Optimize for signal over exhaustiveness", RESEARCH_SYSTEM)
        self.assertIn("re-expand the compressed explanation into the exact receipts", RESEARCH_SYSTEM)
if __name__ == "__main__": unittest.main()
