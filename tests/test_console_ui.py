"""Regression checks for Console navigation, workspace pop-outs, and 3D atmosphere."""

from pathlib import Path
import unittest


ASSETS = Path(__file__).resolve().parents[1] / "wake" / "assets"


class ConsolePresentationTests(unittest.TestCase):
    def setUp(self):
        self.nav = (ASSETS / "nav.js").read_text()
        self.tools = (ASSETS / "console-tools.js").read_text()
        self.layout = (ASSETS / "console-layout.js").read_text()
        self.css = (ASSETS / "research.css").read_text()
        self.map3d_css = (ASSETS / "map3d.css").read_text()
        self.html = (ASSETS / "console.html").read_text()

    def test_console_navigation_stays_in_page(self):
        self.assertNotIn("window.open(", self.nav)
        self.assertNotIn("DETACHABLE CONSOLE LINKS", self.nav)

    def test_console_itself_has_no_popout_control(self):
        self.assertIn('id="reset-console-layout"', self.layout)
        self.assertNotIn('id="popout-console"', self.layout)
        self.assertNotIn("Pop out console", self.layout)
        self.assertNotIn("window.open(", self.layout)

    def test_deeper_console_workspace_pops_out_by_default_on_desktop(self):
        self.assertIn("popWorkspace", self.tools)
        self.assertIn("window.open(", self.tools)
        self.assertIn("url.searchParams.set('workspace','tool')", self.tools)
        self.assertIn("workspaceMode!=='tool'&&desktopPointer()", self.tools)
        self.assertIn("(hover: hover) and (pointer: fine)", self.tools)

    def test_workspace_window_cannot_be_covered_by_console_masthead(self):
        self.assertIn("html.console-tool-window body>.research-header.masthead", self.css)
        self.assertIn("display:none!important", self.css)
        self.assertIn("html.console-tool-window #main>.console-tools", self.css)
        self.assertIn("inset:0!important", self.css)

    def test_3d_map_uses_dark_nebula_behind_transparent_floor(self):
        self.assertIn("NEBULA CONSTELLATION BACKDROP", self.map3d_css)
        self.assertIn('url("backgrounds/nebula-desktop-1680x1050.webp?v=20261004-8")', self.map3d_css)
        self.assertIn("linear-gradient(rgba(0,0,0,.58),rgba(0,0,0,.58))", self.map3d_css)
        self.assertIn("#constellation-stage::before", self.map3d_css)
        self.assertIn("backdrop-filter:blur(18px) brightness(.56) saturate(.82)", self.map3d_css)
        self.assertIn("background-color:rgba(2,5,18,.30)!important", self.map3d_css)

    def test_console_loads_the_layout_controller(self):
        self.assertIn('<script src="console-layout.js" defer></script>', self.html)


if __name__ == "__main__":
    unittest.main()
