import unittest

from wake.application_policy import freshen_duplicate_blog_titles_preflight


class BlogTitlePolicyTests(unittest.TestCase):
    def test_duplicate_standalone_title_is_repaired_deterministically(self):
        state = {
            "version": 126,
            "posts": {
                "old": {"id": "old", "title": "Same tape. Fresh deck."},
            },
        }
        proposal = {
            "summary": "Keep valid work moving.",
            "actions": [{
                "type": "blog",
                "id": "new",
                "project": "",
                "title": "  same tape.   fresh deck. ",
                "lede": "Lede",
                "body": "Body",
                "notebooks": [],
                "evidence": [],
                "reason": "Reflection",
                "reflection_cycle": 127,
            }],
        }

        normalized, note = freshen_duplicate_blog_titles_preflight(state, proposal)

        self.assertEqual(
            normalized["actions"][0]["title"],
            "same tape. fresh deck. — Wake 127",
        )
        self.assertEqual(note["blog_title_repairs"][0]["original"], "same tape. fresh deck.")
        self.assertIn("raw provider response remains preserved", normalized["summary"])

    def test_correction_title_is_not_rewritten(self):
        state = {
            "version": 126,
            "posts": {"old": {"id": "old", "title": "Same title"}},
        }
        proposal = {
            "summary": "Correction.",
            "actions": [{
                "type": "blog",
                "id": "correction",
                "project": "p",
                "title": "Same title",
                "supersedes": "old",
            }],
        }

        normalized, note = freshen_duplicate_blog_titles_preflight(state, proposal)

        self.assertIs(normalized, proposal)
        self.assertIsNone(note)


if __name__ == "__main__":
    unittest.main()
