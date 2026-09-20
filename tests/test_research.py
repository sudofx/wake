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
from wake.providers import Fixture, RESEARCH_SYSTEM
from wake.research import WAKE_SOURCES, allowed_url, collect, discovery_urls
from wake.report import export


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
        self.engine = Engine(self.root/"data", {**DEFAULTS, "mission":"Explore big ideas through small useful projects."})
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
        legacy = Engine(self.root/"legacy", {**DEFAULTS, "mission":"Explore big ideas.", "pet_name":"Wake"})
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
                   {"id": "new_topic", "label": "A new topic", "query": "new topic"}]
        self.engine.config["research_topics"] = changed
        with self.engine.store.lock():
            state = self.engine.initialize()
            invocation, request = self.engine.start("fixture", "topic-test")
            self.engine.store.append("recovered", {"id": invocation, "reason": "Test cleanup"})
        self.assertEqual(state["research_topics"], changed)
        self.assertEqual([event["kind"] for event in self.engine.store.events()].count("research_topics_changed"), 1)
        self.assertIn("new_topic", [topic["id"] for topic in request["context"]["research_topics"]])
        variants = request["response_schema"]["properties"]["actions"]["items"]["anyOf"]
        project_schema = next(item for item in variants if item["properties"]["type"]["enum"] == ["project"])
        self.assertIn("new_topic", project_schema["properties"]["domain"]["enum"])

    def test_wake_topic_is_a_rotating_breadcrumb_not_a_system_instruction(self):
        settings = {**DEFAULTS, "mission": "Follow useful questions.",
                    "research_topics": [{"id": "wake_analysis", "label": "WAKE✳︎", "query": "WAKE"}]}
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

        other = Engine(self.root/"other", {**DEFAULTS, "mission":"test"})
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

    def test_two_fetches_of_same_url_are_not_two_sources(self):
        self.propose([project()])
        self.source("s1", "https://plato.stanford.edu/entries/consciousness/")
        self.source("s2", "https://plato.stanford.edu/entries/consciousness/")
        self.assertEqual(self.propose([notebook(["s1", "s2"])])["status"], "rejected")

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
        self.assertIn("font-variant-emoji:text", html)
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
        receipt = self.engine.store.events()[-1]["payload"]
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
        engine = Engine(self.root/"editorial", {**DEFAULTS, "mission":"Explore.", "editorial_notes":[note]})
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

    def test_verified_notebook_requires_same_topic_corroboration(self):
        with self.engine.store.lock():
            for identifier in ("s1", "s2"):
                self.engine.store.append("observation", dict(
                    id=identifier, source="https://plato.stanford.edu/entries/"+identifier,
                    content=json.dumps({"scope":"synthetic test fixture",
                                        "excerpt":"bounded comparison cellular automata explanations",
                                        "verification_required":True,
                                        "topic_domain":"entropy"}),
                    actor="collector", scope="collected"))
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"])])["status"], "accepted")

    def test_verified_notebook_rejects_cross_topic_evidence(self):
        with self.engine.store.lock():
            for identifier, domain in (("s1", "entropy"), ("s2", "music")):
                self.engine.store.append("observation", dict(
                    id=identifier, source="https://plato.stanford.edu/entries/"+identifier,
                    content=json.dumps({"scope":"synthetic test fixture",
                                        "excerpt":"bounded comparison cellular automata explanations",
                                        "verification_required":True, "topic_domain":domain}),
                    actor="collector", scope="collected"))
        self.assertEqual(self.propose([project(), notebook(["s1", "s2"])])["status"], "rejected")

    def test_topic_discovery_rotates_between_independent_indexes(self):
        topic = {"id": "music", "label": "Music", "query": "music"}
        even = discovery_urls(topic, 0)
        odd = discovery_urls(topic, 1)
        self.assertEqual(len(even), 2)
        self.assertIn("api.crossref.org", even[0])
        self.assertIn("api.openalex.org", even[1])
        self.assertEqual(odd, list(reversed(even)))

    def test_wake_discovery_stays_repository_scoped_and_can_discover_unlisted_files(self):
        topic = {"id": "wake_analysis", "label": "WAKE✳︎", "query": "WAKE✳︎ sudofx/wake"}
        routes = discovery_urls(topic, 7)
        self.assertEqual(len(routes), 2)
        self.assertTrue(all(
            url.startswith("https://raw.githubusercontent.com/sudofx/wake/")
            or url.startswith("https://api.github.com/repos/sudofx/wake/")
            for url in routes
        ))
        self.assertIn(
            "https://api.github.com/repos/sudofx/wake/git/trees/master?recursive=1",
            list(WAKE_SOURCES.values()),
        )
        self.assertEqual(
            allowed_url("https://raw.githubusercontent.com/sudofx/wake/master/tests/unlisted_future_test.py"),
            "https://raw.githubusercontent.com/sudofx/wake/master/tests/unlisted_future_test.py",
        )

    def test_source_url_allowlist_and_input_types(self):
        for url in ("http://arxiv.org/", "https://127.0.0.1/", "https://arxiv.org.evil.example/", "https://a@arxiv.org/", "https://arxiv.org:444/", {}, None):
            with self.subTest(url=url), self.assertRaises(ValueError): allowed_url(url)
        self.assertEqual(allowed_url("https://arxiv.org/abs/1234.56789"), "https://arxiv.org/abs/1234.56789")

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
