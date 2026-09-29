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

    def test_operator_entry_is_status_light_and_settings_remains_accessible(self):
        header = self.html.split('<header class="masthead">', 1)[1].split('</header>', 1)[0]
        self.assertNotIn('Operator sign in', header)
        self.assertNotIn('>Operator<', header)
        self.assertNotIn('STATE PERSISTS', header)
        self.assertNotIn('⚙︎', header)
        self.assertEqual(header.count('class="owner-status-track"'), 2)
        self.assertEqual(header.count('class="owner-status-light"'), 2)
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

    def test_status_light_uses_required_flat_colors_and_motion(self):
        self.assertIn('background:#307444', self.css)
        self.assertIn('background:#d65e6c', self.css)
        self.assertIn('background:#e7c35a', self.css)
        self.assertIn('@keyframes owner-light-pulse', self.css)
        self.assertIn('@keyframes owner-light-blink', self.css)
        self.assertIn('prefers-reduced-motion:reduce', self.css)
        self.assertNotIn('settings-glyph', self.html)
        self.assertIn("ownerMenuLabel.textContent='Settings'", self.html)

    def test_status_light_follows_authentication_and_runtime_contract(self):
        self.assertIn("if(!session())setOwnerLight(publicCycle>0?'running':'idle')", self.html)
        self.assertIn("setOwnerLight(mode==='running'?'running':labels[mode]?'stopped':'unknown')", self.html)
        self.assertIn('data.public_cycle=Number(data.state?.version||0)', self.html)
        self.assertIn('syncPublicLight(next)', self.html)

    def test_status_track_matches_theme_switch_geometry(self):
        self.assertIn('.data-switch-track,.owner-status-track{width:34px;height:18px', self.css)
        self.assertIn('.data-switch-track i,.owner-status-light{display:block;width:12px;height:12px', self.css)
        self.assertIn('.theme-switch .data-switch-track,.owner-status-track{width:42px;height:24px', self.css)
        self.assertIn('.theme-switch .data-switch-track i,.owner-status-light{width:16px;height:16px', self.css)

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
