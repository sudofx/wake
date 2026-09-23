import unittest
from app import analyse


class ObserverTests(unittest.TestCase):
    def test_repeated_rejection_becomes_recommendation(self):
        state = {"version": 3, "invocations": {"a": {"status": "rejected", "reason": "Bad evidence"},
                 "b": {"status": "rejected", "reason": "Bad evidence"}}, "commitments": {}}
        events = [{"kind": "rejected", "payload": {"id": "b", "raw_response": "{\"title\": \"Retry\", \"actions\": []}"}}]
        report = analyse(state, events, "abc")
        self.assertEqual(report["latest"]["proposal"]["title"], "Retry")
        self.assertIn("repeating rejection", report["recommendation"])


if __name__ == "__main__":
    unittest.main()
