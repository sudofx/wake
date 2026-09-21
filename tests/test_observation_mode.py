import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.rejected import rejected_html
from wake.research import collect


class ObservationModeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engine = Engine(Path(self.temp.name) / "data", {
            **DEFAULTS, "mission": "Gather a wider sample.",
            "observation_mode": True, "research_collection_budget": 6,
        })
        with self.engine.store.lock():
            self.engine.initialize()

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def test_mode_collects_a_distinct_bounded_topic_sample(self):
        with self.engine.store.lock():
            collect(self.engine, fetcher=lambda url: {"url": url, "scope": "fixture", "excerpt": "A sufficiently long collected observation for overnight review."})
        collected = [e for e in self.engine.store.load()["evidence"].values() if e.get("actor") == "collector"]
        self.assertEqual(len(collected), min(
            self.engine.config["research_collection_budget"],
            len(self.engine.config["research_topics"])))
        domains = {json.loads(item["content"])["topic_domain"] for item in collected}
        self.assertEqual(len(domains), len(collected))

    def test_rejection_is_public_counterfactual_not_accepted_state(self):
        with self.engine.store.lock():
            invocation, _ = self.engine.start("fixture", "test")
            result = self.engine.finish(invocation, "not-json")
        state = self.engine.store.load()
        event = next(event for event in reversed(self.engine.store.events()) if event["kind"] == "rejected")
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(state["version"], 0)
        self.assertTrue(event["payload"]["observation_receipt"]["would_have_been_flagged"])
        self.assertIn("Observation mode", rejected_html(state, self.engine.store.events()))


if __name__ == "__main__":
    unittest.main()
