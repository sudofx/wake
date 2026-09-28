import json
from pathlib import Path
import tempfile
import unittest

from wake.engine import DEFAULTS, Engine
from wake.research import collect, exact_identifier_url, persistent_identifiers, candidate_source_urls, route_source_identity
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

    def test_routing_progress_clears_acquisition_failure_without_claiming_research(self):
        with self.engine.store.lock():
            for route in ("crossref:discovery", "openalex:discovery", "crossref:discovery"):
                self.engine.store.append("acquisition_assessed", self.receipt(route, "no_progress"))
            receipt = self.receipt("crossref:metadata", "routing_progress")
            receipt["persistent_identifiers"] = ["doi:10.1000/example"]
            self.engine.store.append("acquisition_assessed", receipt)
        summary = self.engine.store.load()["acquisition"]["p"]
        self.assertEqual(summary["no_progress"], 0)
        self.assertFalse(summary["capability_blocked"])
        self.assertEqual(summary["last_receipt"]["outcome"], "routing_progress")

    def test_discovery_identifiers_are_structured_for_later_retrieval(self):
        ids = persistent_identifiers({
            "excerpt": (
                "DOI 10.1000/example.1; DOI 10.1098/rspa.1991.0138; "
                "https://openalex.org/W12345; https://arxiv.org/abs/2512.02221; PMC1790863"
            ),
            "externalIds": {"PubMed": "17299597"},
        })
        self.assertIn("doi:10.1000/example.1", ids)
        self.assertIn("doi:10.1098/rspa.1991.0138", ids)
        self.assertIn("openalex:W12345", ids)
        self.assertIn("arxiv:2512.02221", ids)
        self.assertNotIn("arxiv:1991.0138", ids)
        self.assertIn("pmc:PMC1790863", ids)
        self.assertIn("pmid:17299597", ids)

    def test_retrieval_routes_encode_primary_work_identity(self):
        self.assertEqual(
            route_source_identity("https://api.crossref.org/works/10.1000%2Fexample.1"),
            "doi:10.1000/example.1",
        )
        self.assertEqual(
            route_source_identity("https://api.openalex.org/works/W12345"),
            "openalex:W12345",
        )
        self.assertEqual(
            route_source_identity("https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC1790863/unicode"),
            "pmc:PMC1790863",
        )

    def test_persistent_identifiers_map_to_exact_approved_records(self):
        self.assertEqual(
            exact_identifier_url("doi:10.1000/example.1"),
            "https://api.crossref.org/works/10.1000%2Fexample.1",
        )
        self.assertEqual(
            exact_identifier_url("openalex:W12345"),
            "https://api.openalex.org/works/W12345",
        )
        self.assertIn("id_list=2512.02221", exact_identifier_url("arxiv:2512.02221"))
        self.assertIn("/BioC_json/PMC1790863/unicode", exact_identifier_url("pmc:PMC1790863"))
        self.assertIn("/BioC_json/17299597/unicode", exact_identifier_url("pmid:17299597"))
        self.assertIsNone(exact_identifier_url("unknown:value"))

    def test_collector_promotes_metadata_lead_to_readable_source_without_model_translation(self):
        calls = []
        exact = "https://api.crossref.org/works/10.1000%2Fexample.1"
        readable = "https://www.frontiersin.org/articles/10.3389/example/full"
        def fetcher(url):
            calls.append(url)
            if url == exact:
                return {"url": url, "scope": "Crossref bibliographic metadata",
                        "excerpt": f"publisher landing page {readable} DOI 10.1000/example.1"}
            return {"url": url, "scope": "readable publisher article",
                    "excerpt": "substantive readable source material " * 20}

        with self.engine.store.lock():
            receipt = self.receipt("crossref:discovery", "no_progress")
            receipt["persistent_identifiers"] = ["doi:10.1000/example.1"]
            self.engine.store.append("acquisition_assessed", receipt)
            collect(self.engine, fetcher=fetcher)
            state = self.engine.store.load()
            self.assertIn(readable, state["acquisition"]["p"]["source_candidates"])
            self.assertEqual(state["acquisition"]["p"]["no_progress"], 0)
            self.assertEqual(state["acquisition"]["p"]["last_receipt"]["outcome"], "routing_progress")
            collect(self.engine, fetcher=fetcher)

        self.assertIn(exact, calls)
        self.assertIn(readable, calls)
        state = self.engine.store.load()
        self.assertEqual(state["acquisition"]["p"]["no_progress"], 0)
        promoted = [e for e in state["evidence"].values() if e.get("source") == readable]
        self.assertEqual(len(promoted), 1)
        payload = json.loads(promoted[0]["content"])
        self.assertEqual(payload["evidence_role"], "source")
        self.assertEqual(payload["topic_domain"], "entropy")
        self.assertEqual(payload["source_identity"], "doi:10.1000/example.1")
        self.assertEqual(
            state["acquisition"]["p"]["source_candidate_identities"][readable],
            "doi:10.1000/example.1",
        )

    def test_candidate_source_urls_keep_allowlisted_https_pdf_routes(self):
        urls = candidate_source_urls({
            "excerpt": (
                "https://api.crossref.org/works/10.1000/example "
                "https://www.frontiersin.org/articles/example/full "
                "https://www.frontiersin.org/articles/example/file.pdf"
            )
        })
        self.assertEqual(urls, [
            "https://www.frontiersin.org/articles/example/full",
            "https://www.frontiersin.org/articles/example/file.pdf",
        ])

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
