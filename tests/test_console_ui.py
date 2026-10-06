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
        self.research = (ASSETS / "research.js").read_text()

    def test_console_navigation_stays_in_page(self):
        self.assertNotIn("window.open(", self.nav)
        self.assertNotIn("DETACHABLE CONSOLE LINKS", self.nav)

    def test_console_reset_view_restores_default_landscape_width(self):
        self.assertIn("const STORAGE='wake-console-workspace-v3'", self.layout)
        self.assertIn('>Reset view</button>', self.layout)
        self.assertIn("panel.matches('.map-panel,.notebook-panel,.process-field-panel')?12", self.layout)
        self.assertIn('.console-module-grid>.map-panel[data-span="12"]', self.css)
        self.assertIn('grid-column:1/-1!important', self.css)

    def test_console_screenshot_repairs_stay_authoritative(self):
        self.assertIn('.console-module-grid>.process-field-panel{margin-bottom:16px!important}', self.css)
        self.assertIn('.console-module-grid .module-size{display:inline-flex!important}', self.css)
        self.assertIn('.research-page .chart-key .accepted{color:var(--cyan)!important}', self.css)
        self.assertIn('.console-module-grid>.map-panel{', self.css)
        self.assertIn("wake=selectedWake||(projection?.wakes||[]).find", (ASSETS / "process-field.js").read_text())
        self.assertIn("detail:{recordId,wakeId,wake}", self.research)

    def test_console_itself_has_no_popout_control(self):
        self.assertIn('id="reset-console-layout"', self.layout)
        self.assertNotIn('id="popout-console"', self.layout)
        self.assertNotIn("Pop out console", self.layout)
        self.assertNotIn("window.open(", self.layout)

    def test_console_workspaces_are_full_browser_pages(self):
        self.assertIn("window.open(url.href,'wake-console-workspace')", self.tools)
        self.assertIn("location.assign(url.href)", self.tools)
        self.assertIn("(hover: hover) and (pointer: fine)", self.tools)
        self.assertIn("popup=yes,width=", self.tools)
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
        self.assertIn("linear-gradient(rgba(0,0,0,.70),rgba(0,0,0,.70))", self.map3d_css)
        self.assertIn("#constellation-stage::before", self.map3d_css)
        self.assertIn("backdrop-filter:blur(18px)", self.map3d_css)
        self.assertIn("background-color:rgba(2,5,18,.08)!important", self.map3d_css)

    def test_3d_map_stylesheet_is_cache_busted(self):
        map3d_html = (ASSETS / "map3d.html").read_text()
        self.assertRegex(map3d_html, r'href="map3d\.css\?v=[^"]+"')

    def test_wake_detail_tabs_stay_on_one_row_on_phones(self):
        self.assertIn(".wake-tabs{flex-wrap:nowrap;gap:3px;margin:10px 12px}", self.css)
        self.assertIn(".wake-tabs button{flex:1 1 0;min-width:0;min-height:32px;padding:5px 4px;font-size:9px;white-space:nowrap}", self.css)

    def test_cube_tracks_recorded_wake_and_record_selections(self):
        self.assertIn("function matrixCellForWake(id)", self.research)
        self.assertIn("function syncCubeToWake(id)", self.research)
        self.assertIn("function syncCubeToRecord(id)", self.research)
        self.assertIn("syncCubeToWake(id);renderWake()", self.research)
        self.assertIn("syncCubeToRecord(id);renderMap()", self.research)

    def test_console_loads_the_layout_controller(self):
        self.assertRegex(self.html, r'<script src="console-layout\.js\?v=[^"]+" defer></script>')



    def test_process_field_is_a_modular_console_panel(self):
        self.assertIn("'#main > .process-field-panel'", self.layout)
        self.assertIn('class="module-drag"', self.layout)
        self.assertIn('class="module-size"', self.layout)
        self.assertIn('class="module-collapse"', self.layout)

    def test_landscape_is_graph_only(self):
        self.assertNotIn('id="graph-mode"', self.html)
        self.assertNotIn('id="list-mode"', self.html)
        self.assertNotIn('id="map-list"', self.html)

    def test_motion_and_desktop_inspector_repairs_are_present(self):
        self.assertIn("motionButton.dataset.motionBound", self.research)
        self.assertIn("window.dispatchEvent(new CustomEvent('wake-global-motion'", self.research)
        self.assertIn("DESKTOP INSPECTION RAIL", self.css)


    def test_horizontal_history_surfaces_are_scrollable_and_latest_first(self):
        self.assertIn("AUTHORITATIVE SCROLL + MODULE CHROME", self.css)
        self.assertIn("overflow-x:auto!important", self.css)
        self.assertIn("el.scrollLeft=el.scrollWidth-el.clientWidth", self.research)
        self.assertIn("const el=$('activity-chart')", self.research)

    def test_mobile_deep_tools_open_new_tabs(self):
        self.assertIn("window.open(url.href,'_blank','noopener')", self.tools)

if __name__ == "__main__":
    unittest.main()
