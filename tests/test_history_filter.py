from pathlib import Path
import unittest


class HistoryFilterTests(unittest.TestCase):
    def test_history_filter_is_populated_from_all_exported_event_kinds(self):
        page = (Path(__file__).parents[1] / "wake/assets/index.html").read_text()
        script = (Path(__file__).parents[1] / "wake/assets/app.js").read_text()
        self.assertIn('id="event-filter"', page)
        self.assertIn('data.events.map(event=>event.kind)', script)
        self.assertIn('eventSelect.append(option)', script)


if __name__ == "__main__":
    unittest.main()
