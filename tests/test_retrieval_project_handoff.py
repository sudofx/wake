import json
import unittest

from wake.retrieval import build_retrieval_shadow


class ProjectFairRetrievalTests(unittest.TestCase):
    def source(self, identifier, domain, version):
        return identifier, {
            "id": identifier,
            "actor": "collector",
            "scope": "collected",
            "version": version,
            "source": f"https://example.org/{identifier}",
            "content": json.dumps({
                "verification_required": True,
                "evidence_role": "source",
                "topic_domain": domain,
                "source_identity": f"work:{identifier}",
                "excerpt": f"usable source for {domain}",
            }),
        }

    def test_active_project_source_survives_newer_global_evidence_churn(self):
        old_id, old = self.source("old-observer-source", "observer", 1)
        evidence = {old_id: old}
        for index in range(8):
            identifier, item = self.source(f"new-humor-{index}", "humor", index + 2)
            evidence[identifier] = item

        state = {
            "version": 20,
            "projects": {
                "observer-project": {
                    "id": "observer-project",
                    "domain": "observer",
                    "status": "active",
                },
                "humor-project": {
                    "id": "humor-project",
                    "domain": "humor",
                    "status": "active",
                },
            },
            "research_topics": [
                {"id": "observer"},
                {"id": "humor"},
            ],
            "attention": {"selected_topic": "observer"},
            "evidence": evidence,
            "beliefs": {},
            "notebooks": {},
            "commitments": {},
        }

        retrieval = build_retrieval_shadow(state, {"beliefs": []})

        self.assertIn("old-observer-source", retrieval["evidence_ids"])
        handoffs = [
            item for item in retrieval["candidates"]
            if item["trigger"] == "project_source_handoff"
        ]
        self.assertEqual(
            {item["record"]["id"] for item in handoffs},
            {"observer-project", "humor-project"},
        )
        self.assertEqual(handoffs[0]["record"]["id"], "observer-project")

    def test_discovery_record_does_not_become_project_synthesis_handoff(self):
        state = {
            "version": 2,
            "projects": {
                "p": {"id": "p", "domain": "observer", "status": "active"},
            },
            "research_topics": [{"id": "observer"}],
            "attention": {"selected_topic": "observer"},
            "evidence": {
                "lead": {
                    "id": "lead",
                    "actor": "collector",
                    "scope": "collected",
                    "version": 1,
                    "source": "https://example.org/lead",
                    "content": json.dumps({
                        "evidence_role": "discovery",
                        "topic_domain": "observer",
                    }),
                },
            },
            "beliefs": {},
            "notebooks": {},
            "commitments": {},
        }

        retrieval = build_retrieval_shadow(state, {"beliefs": []})

        self.assertNotIn("lead", retrieval["evidence_ids"])
        self.assertFalse(any(
            item["trigger"] == "project_source_handoff"
            for item in retrieval["candidates"]
        ))


if __name__ == "__main__":
    unittest.main()
