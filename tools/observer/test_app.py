import unittest
from app import analyse, analyst_prompt


class ObserverTests(unittest.TestCase):
    def test_repeated_rejection_becomes_recommendation(self):
        state = {"version": 3, "invocations": {"a": {"status": "rejected", "reason": "Bad evidence"},
                 "b": {"status": "rejected", "reason": "Bad evidence"}}, "commitments": {}}
        events = [{"kind": "rejected", "payload": {"id": "b", "raw_response": "{\"title\": \"Retry\", \"actions\": []}"}}]
        report = analyse(state, events, "abc")
        self.assertEqual(report["latest"]["proposal"]["title"], "Retry")
        self.assertIn("repeating rejection", report["recommendation"])

    def test_repeated_provider_deferral_is_not_called_rejection(self):
        attempt = {"model": "gemini-test", "http_status": 503, "result": "transient_failure",
                   "request_payload_bytes": 52000, "category": "server",
                   "provider_error": {"message": "high demand"}}
        state = {"version": 2, "invocations": {
            "a": {"status": "deferred", "reason": "Gemini temporarily unavailable; wake deferred",
                  "provider_attempts": [attempt]},
            "b": {"status": "deferred", "reason": "Gemini temporarily unavailable; wake deferred",
                  "provider_attempts": [attempt]},
        }, "commitments": {}}
        report = analyse(state, [], "abc")
        self.assertIn("Provider availability", report["recommendation"])
        self.assertNotIn("repeating rejection", report["recommendation"])
        self.assertEqual(report["recent_provider_attempts"][-1]["request_payload_bytes"], 52000)

    def test_analyst_prompt_forbids_payload_and_cross_class_causal_leaps(self):
        prompt = analyst_prompt({"recent_provider_attempts": []})
        self.assertIn("do not invent causal links", prompt)
        self.assertIn("governance rejection are different event classes", prompt)
        self.assertIn("Do not infer that request payload size", prompt)
        self.assertIn("compare recent successful and failed provider attempts", prompt)
        self.assertIn("Prefer passive, non-invasive checks", prompt)
        self.assertIn("Do not recommend synthetic probe requests", prompt)


if __name__ == "__main__":
    unittest.main()
