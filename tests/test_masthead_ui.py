"""Regression checks for the public masthead/operator presentation boundary."""

from pathlib import Path
import re
import unittest


ASSETS = Path(__file__).resolve().parents[1] / "wake" / "assets"


class MastheadPresentationTests(unittest.TestCase):
    def setUp(self):
        self.html = (ASSETS / "index.html").read_text()
        self.css = (ASSETS / "style.css").read_text()
        self.js = (ASSETS / "app.js").read_text()

    def test_masthead_has_one_theme_switch_and_no_decorative_theme_glyph(self):
        self.assertEqual(self.html.count('id="theme-toggle"'), 1)
        self.assertEqual(self.html.count('class="data-switch theme-switch"'), 1)
        self.assertNotIn('class="theme-icon"', self.html)
        self.assertNotRegex(self.html, r'[☀☼☾◐◑]')

    def test_operator_entry_is_cog_only_and_status_stays_inside_settings_panel(self):
        header = self.html.split('<header class="masthead">', 1)[1].split('</header>', 1)[0]
        self.assertNotIn('Operator sign in', header)
        self.assertNotIn('>Operator<', header)
        self.assertNotIn('STATE PERSISTS', header)
        self.assertNotIn('owner-menu-toggle i', header)
        self.assertEqual(header.count('class="settings-glyph"'), 2)
        self.assertIn('data-owner-control-status', header)
        self.assertIn('data-owner-identity', header)
        self.assertIn('aria-label="Open Settings"', header)
        self.assertIn('title="Settings"', header)

    def test_login_and_authenticated_settings_entries_cannot_render_together(self):
        self.assertIn('.owner-menu-toggle[hidden]', self.css)
        self.assertIn('.owner-login[hidden]', self.css)
        self.assertIn('display:none!important', self.css)
        self.assertIn('ownerMenuToggle.hidden=true', self.html)
        self.assertIn('ownerLogin.hidden=false', self.html)
        self.assertIn('ownerLogin.hidden=true', self.html)
        self.assertIn('ownerMenuToggle.hidden=false', self.html)

    def test_no_green_status_dot_or_operator_status_label_on_cog(self):
        self.assertIn('.owner-menu-toggle i{display:none!important}', self.css)
        self.assertNotIn("ownerMenuToggle?.classList.toggle('is-active'", self.html)
        self.assertIn("ownerMenuLabel.textContent='Settings'", self.html)

    def test_operator_controls_follow_runtime_state_machine(self):
        self.assertIn("const mode=state.mode||", self.html)
        self.assertIn("state.enabled===false?'disabled':'stopped'", self.html)
        self.assertIn("const controls=state.controls||fallbackControls", self.html)
        self.assertIn("ownerStart.disabled=controls.start!==true", self.html)
        self.assertIn("ownerStop.disabled=controls.stop!==true", self.html)
        self.assertIn("ownerReset.disabled=controls.reset!==true", self.html)
        self.assertIn("running:'Running now'", self.html)
        self.assertIn("draining:'Stopping…'", self.html)
        self.assertIn("stopped:'Stopped'", self.html)
        self.assertIn("disabled:'Disabled'", self.html)


if __name__ == "__main__":
    unittest.main()
