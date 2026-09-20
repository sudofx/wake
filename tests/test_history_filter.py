from pathlib import Path
import unittest


class HistoryFilterTests(unittest.TestCase):
    def test_squirrel_receipts_are_selectable_in_the_history_filter(self):
        page = (Path(__file__).parents[1] / "wake/assets/index.html").read_text()
        self.assertIn('<option>squirrel_assessed</option>', page)


if __name__ == "__main__":
    unittest.main()
