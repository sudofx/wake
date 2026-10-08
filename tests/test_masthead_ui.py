"""Regression checks for the public masthead and GitHub Actions link."""

from pathlib import Path
import re
import unittest


ASSETS = Path(__file__).resolve().parents[1] / "wake" / "assets"


class MastheadPresentationTests(unittest.TestCase):
    def setUp(self):
        self.html = (ASSETS / "index.html").read_text()
        self.css = (ASSETS / "masthead.css").read_text()
        self.theme = (ASSETS / "theme.css").read_text()

    def test_theme_switch_is_first_control(self):
        tools = self.html.split('class="header-tools"', 1)[1].split("</div>", 1)[0]
        self.assertIn('id="theme-toggle"', tools)
        self.assertLess(tools.index('class="theme-switch"'), tools.index('class="repo-link"'))

    def test_actions_entry_has_repo_link_and_compact_status(self):
        header = self.html.split('<header class="masthead">', 1)[1].split('</header>', 1)[0]
        self.assertIn('href="https://github.com/sudofx/wake"', header)
        self.assertIn('class="repo-link"', header)
        self.assertIn('href="https://github.com/sudofx/wake/actions"', header)
        self.assertIn('class="actions-light"', header)
        self.assertNotIn('actions-light-label', header)
        self.assertIn('title="Checking…"', header)
        self.assertNotIn('Powered by wake', header)
        self.assertNotIn('class="footer-powered"', self.html)
        self.assertNotIn('Powered by wake', self.html)
        self.assertNotIn('Operator', header)
        for forbidden in ('owner-', 'operator-status', 'operator-actions-link',
                          'WAKE_CONTROL_URL', 'wake-owner-session',
                          'data-owner-start', 'data-owner-stop', 'data-owner-reset'):
            self.assertNotIn(forbidden, header)

    def test_console_is_an_instrument_glyph_beside_github_everywhere(self):
        pages = {
            "index": (ASSETS / "index.html").read_text(),
            "map": (ASSETS / "map.html").read_text(),
            "map3d": (ASSETS / "map3d.html").read_text(),
            "console": (ASSETS / "console.html").read_text(),
        }
        stylesheet = re.search(r'href="nav\.css\?v=[^"]+"', pages["index"]).group(0)
        for name, page in pages.items():
            with self.subTest(page=name):
                nav = page.split('<nav class="compact-nav"', 1)[1].split('</nav>', 1)[0]
                header_tools = page.split('class="header-tools"', 1)[1].split('</div>', 1)[0]
                self.assertNotIn('>Console</a>', nav)
                self.assertIn('class="console-link"', header_tools)
                self.assertIn('aria-label="Open WAKE Console"', header_tools)
                self.assertIn('title="Console"', header_tools)
                self.assertIn('M4.2 16.8a8.8 8.8 0 1 1 15.6 0', header_tools)
                self.assertIn('M12 16l3.8-4.4', header_tools)
                self.assertNotIn('>About</a>', nav)
                self.assertLess(header_tools.index('class="repo-link"'),
                                header_tools.index('class="console-link"'))
                self.assertLess(header_tools.index('class="console-link"'),
                                header_tools.index('class="actions-light"'))
                self.assertIn(stylesheet, page)
        self.assertIn('class="console-link" href="console.html" aria-current="page"', pages["console"])

    def test_shared_assets_are_loaded_after_page_skins(self):
        for name in ('index.html', 'console.html', 'map.html', 'map3d.html'):
            page = (ASSETS / name).read_text()
            self.assertIn('src="site-theme.js?v=', page)
            self.assertGreater(page.index('href="masthead.css?v='), page.index('href="nav.css?v='))

    def test_primary_masthead_menu_is_research_journal_blog(self):
        pages = {
            "index": (ASSETS / "index.html").read_text(),
            "map": (ASSETS / "map.html").read_text(),
            "map3d": (ASSETS / "map3d.html").read_text(),
            "console": (ASSETS / "console.html").read_text(),
        }
        for name, page in pages.items():
            with self.subTest(page=name):
                nav = page.split('<nav class="compact-nav"', 1)[1].split('</nav>', 1)[0]
                visible = nav.split('<!-- Read menu temporarily retired.', 1)[0]
                self.assertNotIn('>Home</a>', visible)
                self.assertNotIn('<summary>Read</summary>', visible)
                self.assertIn('<!-- Read menu temporarily retired.', nav)
                self.assertIn('<summary>Read</summary>', nav)
                research = visible.index('>Research</a>')
                journal = visible.index('>Journal</a>')
                blog = visible.index('>Bob’s Blog</a>')
                self.assertLess(research, journal)
                self.assertLess(journal, blog)

    def test_masthead_geometry_has_one_owner(self):
        for name in ('nav.css', 'style.css', 'theme.css', 'research.css', 'console-light.css'):
            rules = re.sub(r'/\*.*?\*/', '', (ASSETS / name).read_text(), flags=re.S)
            self.assertNotRegex(rules, r'\.(masthead|research-header|header-tools|wordmark|console-link|actions-light)\b')
        self.assertIn('grid-template-columns:repeat(3,minmax(0,1fr))', self.css)

    def test_actions_light_is_phone_safe_and_read_only(self):
        nav = (ASSETS / "nav.js").read_text()
        self.assertIn('cursor:pointer', self.css)
        self.assertIn('actions/workflows/wake-runner.yml', nav)
        self.assertIn('actions/workflows/operator-enable-continuity.yml/runs?per_page=10', nav)
        self.assertNotIn('actions/workflows/wake.yml/runs?branch=wake-runtime&per_page=10', nav)
        self.assertIn("['running','stopped','campaign']", nav)
        self.assertIn("CACHE_KEY='wake-actions-light-state'", nav)
        self.assertIn('CACHE_FRESH_MS=90000', nav)
        self.assertIn('REFRESH_MS=180000', nav)
        self.assertIn("fetchJson(latchUrl)", nav)
        self.assertIn("if(latch.state==='active')", nav)
        self.assertIn("fetchJson(campaignUrl)", nav)
        self.assertIn("last verified · refresh unavailable", nav)
        self.assertIn("window.addEventListener('storage'", nav)
        self.assertNotIn('Promise.allSettled([', nav)
        self.assertIn('setInterval(refreshActionsLight,REFRESH_MS)', nav)
        self.assertNotIn('.owner-', self.css)
        self.assertNotIn('operator-status', self.css)

    def test_console_reuses_shared_actions_status_controller(self):
        console = (ASSETS / "console.html").read_text()
        research = (ASSETS / "research.js").read_text()
        self.assertIn('src="nav.js?v=', console)
        self.assertIn('src="research.js?v=', console)
        self.assertNotIn("function execution()", research)
        self.assertNotIn("actions/workflows/wake.yml/runs?branch=wake-runtime", research)
        self.assertNotIn("GitHub Actions · status unavailable", research)

    def test_debug_zero_cycle_view_is_gone(self):
        self.assertNotIn('data-visibility-toggle', self.html)
        self.assertNotIn('wake-hide-current-data', self.html)
        self.assertNotIn('DATA_VIEW_SCRIPT', self.html)

    def test_live_projection_still_updates_the_public_site(self):
        self.assertIn('data.public_cycle=Number(data.state?.version||0)', self.html)
        self.assertIn("window.WakeApplyLive?.(next)", self.html)
        self.assertIn("setInterval(refreshLiveState,10000)", self.html)


if __name__ == "__main__":
    unittest.main()
