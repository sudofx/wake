"""Regression checks for Console navigation, full-page tools, and 3D atmosphere."""

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

    def test_console_workspaces_are_full_browser_pages(self):
        self.assertIn("window.open(url.href,'wake-console-workspace')", self.tools)
        self.assertIn("location.assign(url.href)", self.tools)
        self.assertIn("(hover: hover) and (pointer: fine)", self.tools)
        self.assertNotIn("popup=yes", self.tools)
        self.assertNotIn("frame.src", self.tools)
        self.assertNotIn("workspace','tool", self.tools)

    def test_standalone_tool_pages_do_not_swallow_their_links(self):
        component = (ASSETS / "console-component.js").read_text()
        self.assertIn("if(parent===window)return", component)

    def test_console_has_no_embedded_tool_workspace(self):
        self.assertNotIn('id="console-tool-frame"', self.html)
        self.assertNotIn('id="close-console-tools"', self.html)
        self.assertNotIn('<iframe', self.html)
        self.assertNotIn("console-tool-window", self.html)
        self.assertIn("Complete research tools open as full browser pages.", self.html)

    def test_3d_map_uses_dark_nebula_behind_transparent_floor(self):
        self.assertIn("NEBULA CONSTELLATION BACKDROP", self.map3d_css)
        self.assertIn('url("backgrounds/nebula-desktop-1680x1050.webp?v=20261004-8")', self.map3d_css)
        self.assertIn("linear-gradient(rgba(0,0,0,.58),rgba(0,0,0,.58))", self.map3d_css)
        self.assertIn("#constellation-stage::before", self.map3d_css)
        self.assertIn("backdrop-filter:blur(18px) brightness(.56) saturate(.82)", self.map3d_css)
        self.assertIn("background-color:rgba(2,5,18,.30)!important", self.map3d_css)

    def test_3d_map_stylesheet_is_cache_busted(self):
        map3d_html = (ASSETS / "map3d.html").read_text()
        self.assertIn('href="map3d.css?v=20261004-9"', map3d_html)

    def test_wake_detail_tabs_stay_on_one_row_on_phones(self):
        self.assertIn(".wake-tabs{flex-wrap:nowrap;gap:3px;margin:10px 12px}", self.css)
        self.assertIn(".wake-tabs button{flex:1 1 0;min-width:0;min-height:32px;padding:5px 4px;font-size:9px;white-space:nowrap}", self.css)

    def test_console_loads_the_layout_controller(self):
        self.assertIn('<script src="console-layout.js" defer></script>', self.html)


if __name__ == "__main__":
    unittest.main()
