import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.research import persistent_identifiers
from support import charter_settings


class AcquisitionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engine = Engine(Path(self.temp.name) / "data", charter_settings("Test acquisition receipts."))
        with self.engine.store.lock():
            self.engine.initialize()
            invocation, request = self.engine.start("fixture", "test")
            self.engine.finish(invocation, json.dumps({"base_version": request["context"]["version"], "title": "P", "summary": "Seed project", "actions": [{"type": "project", "id": "p", "title": "P", "question": "Q", "domain": "entropy", "status": "active", "next_step": "N", "reason": "R"}]}))

    def tearDown(self):
        self.engine.store.close(); self.temp.cleanup()

    def receipt(self, route, outcome):
        return {"project": "p", "domain": "entropy", "research_id": route,
                "route": route, "stage": "discovery", "outcome": outcome, "evidence": "e" + route[-1]}

    def test_distinct_no_progress_routes_become_capability_blocked(self):
        with self.engine.store.lock():
            for route in ("crossref:discovery", "openalex:discovery", "crossref:discovery", "openalex:discovery"):
                self.engine.store.append("acquisition_assessed", self.receipt(route, "no_progress"))
        summary = self.engine.store.load()["acquisition"]["p"]
        self.assertTrue(summary["capability_blocked"])
        self.assertEqual(summary["no_progress"], 4)
        self.assertGreater(summary["retry_after_version"], self.engine.store.load()["version"])

    def test_substantive_progress_clears_failure_count(self):
        with self.engine.store.lock():
            self.engine.store.append("acquisition_assessed", self.receipt("crossref:discovery", "no_progress"))
            self.engine.store.append("acquisition_assessed", self.receipt("crossref:source", "progress"))
        self.assertEqual(self.engine.store.load()["acquisition"]["p"]["no_progress"], 0)

    def test_discovery_identifiers_are_structured_for_later_retrieval(self):
        ids = persistent_identifiers({"excerpt": "DOI 10.1000/example.1; https://openalex.org/W12345"})
        self.assertIn("doi:10.1000/example.1", ids)
        self.assertIn("openalex:W12345", ids)

    def test_capability_block_can_record_a_distinct_frame_without_claiming_evidence(self):
        with self.engine.store.lock():
            self.engine.store.append("observation", {"id": "literal", "source": "https://example.org/literal",
                "content": "literal observation", "actor": "collector", "scope": "collected"})
            for route in ("crossref:discovery", "openalex:discovery", "crossref:discovery", "openalex:discovery"):
                self.engine.store.append("acquisition_assessed", self.receipt(route, "no_progress"))
            invocation, request = self.engine.start("fixture", "reframe")
            result = self.engine.finish(invocation, json.dumps({"base_version": request["context"]["version"],
                "title": "New strategy", "summary": "Keep the same unresolved question.", "actions": [{
                    "type": "reframe", "project": "p", "old_frame": "Find a broad overview.",
                    "new_frame": "Retrieve the exact DOI record.", "assumptions_changed": "Metadata may identify a retrievable source.",
                    "observations": ["literal"], "trigger": "Two discovery routes made no progress.",
                    "strategy": "Request one exact approved record.", "reason": "Try a different acquisition representation."}]}))
        frame = self.engine.store.load()["representations"]["p"][0]
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(frame["status"], "hypothesis")
        self.assertEqual(frame["observations"], ["literal"])

    def test_paraphrased_frame_is_not_a_new_representation(self):
        with self.engine.store.lock():
            for route in ("crossref:discovery", "openalex:discovery", "crossref:discovery", "openalex:discovery"):
                self.engine.store.append("acquisition_assessed", self.receipt(route, "no_progress"))
            invocation, request = self.engine.start("fixture", "reframe")
            proposal = {"base_version": request["context"]["version"], "title": "No change", "summary": "Test.", "actions": [{
                "type": "reframe", "project": "p", "old_frame": "same words", "new_frame": "same words",
                "assumptions_changed": "none", "observations": [], "trigger": "blocked", "strategy": "same", "reason": "Test."}]}
            result = self.engine.finish(invocation, json.dumps(proposal))
        self.assertEqual(result["status"], "rejected")

    def test_bounded_context_retains_capability_recovery(self):
        with self.engine.store.lock():
            for route in ("crossref:discovery", "openalex:discovery", "crossref:discovery", "openalex:discovery"):
                self.engine.store.append("acquisition_assessed", self.receipt(route, "no_progress"))
        state = self.engine.store.load()
        context = self.engine.bounded_context(state, {}, self.engine.working_set(state), 99999)
        self.assertEqual(context["representation_recovery"][0]["project"], "p")
        self.assertTrue(context["representation_recovery"][0]["capability"]["capability_blocked"])


if __name__ == "__main__": unittest.main()
