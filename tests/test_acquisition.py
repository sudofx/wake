import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.research import persistent_identifiers


class AcquisitionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engine = Engine(Path(self.temp.name) / "data", {**DEFAULTS, "mission": "Test acquisition receipts."})
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


if __name__ == "__main__": unittest.main()
