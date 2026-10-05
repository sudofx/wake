"""Regression checks for Console navigation and explicit pop-out behavior."""

from pathlib import Path
import unittest


ASSETS = Path(__file__).resolve().parents[1] / "wake" / "assets"


class ConsolePresentationTests(unittest.TestCase):
    def setUp(self):
        self.nav = (ASSETS / "nav.js").read_text()
        self.tools = (ASSETS / "console-tools.js").read_text()
        self.layout = (ASSETS / "console-layout.js").read_text()
        self.css = (ASSETS / "research.css").read_text()
        self.html = (ASSETS / "console.html").read_text()

    def test_console_navigation_does_not_auto_open_a_window(self):
        self.assertNotIn("window.open(", self.nav)
        self.assertNotIn("DETACHABLE CONSOLE LINKS", self.nav)

    def test_deeper_console_tools_stay_in_page_by_default(self):
        self.assertNotIn("window.open(", self.tools)
        self.assertNotIn("popWorkspace", self.tools)
        self.assertIn("panel.hidden=false", self.tools)

    def test_console_popout_is_explicit_and_next_to_reset_layout(self):
        self.assertIn('id="reset-console-layout"', self.layout)
        self.assertIn('id="popout-console"', self.layout)
        self.assertIn("Pop out console", self.layout)
        self.assertIn("url.searchParams.set('workspace','detached')", self.layout)
        self.assertIn("window.open(", self.layout)
        self.assertNotIn("if(!detached)return", self.layout)

    def test_popout_stays_desktop_only(self):
        self.assertIn("@media(pointer:coarse)", self.css)
        self.assertIn("#popout-console{display:none!important}", self.css)

    def test_console_loads_the_layout_controller(self):
        self.assertIn('<script src="console-layout.js" defer></script>', self.html)


if __name__ == "__main__":
    unittest.main()
