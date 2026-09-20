import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.research import ALLOWED_ALT_HOSTS, allowed_discovery_url, allowed_url, collect, discovery_urls


class AlternateHostTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.engine = Engine(Path(self.temp.name) / "data", {**DEFAULTS, "mission": "Test host tiers."})
        with self.engine.store.lock():
            self.engine.initialize()

    def tearDown(self):
        self.engine.store.close()
        self.temp.cleanup()

    def test_alt_hosts_are_discovery_only_and_not_verification_hosts(self):
        url = "https://en.wikipedia.org/w/api.php?action=query"
        self.assertIn("en.wikipedia.org", ALLOWED_ALT_HOSTS)
        self.assertEqual(allowed_discovery_url(url), url)
        with self.assertRaises(ValueError):
            allowed_url(url)

    def test_initial_neutral_query_uses_alt_host_and_is_stamped_discovery(self):
        topic = self.engine.store.load()["research_topics"][0]
        self.assertTrue(discovery_urls(topic)[0].startswith("https://en.wikipedia.org/"))
        with self.engine.store.lock():
            collect(self.engine, fetcher=lambda url: {"url": url, "scope": "fixture", "excerpt": "A sufficiently long idea-pool result for an initial research direction."})
        observations = [item for item in self.engine.store.load()["evidence"].values()
                        if item.get("actor") == "collector"]
        payload = json.loads(observations[0]["content"])
        self.assertEqual(payload["host_tier"], "discovery")
        self.assertEqual(payload["evidence_role"], "discovery")

    def test_model_followups_cannot_request_an_alt_host(self):
        with self.engine.store.lock():
            invocation, request = self.engine.start("fixture", "test")
            proposal = {"base_version": request["context"]["version"], "title": "Invalid host", "summary": "Test boundary",
                        "actions": [{"type": "project", "id": "p", "title": "P", "question": "Q", "domain": "comedy", "status": "active", "next_step": "N", "reason": "R"},
                                    {"type": "research", "id": "r", "project": "p", "query": "test", "domain": "comedy", "url": "https://en.wikipedia.org/wiki/Comedy", "reason": "Must fail"}]}
            result = self.engine.finish(invocation, json.dumps(proposal))
        self.assertEqual(result["status"], "rejected")


if __name__ == "__main__":
    unittest.main()
