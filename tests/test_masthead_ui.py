"""Regression checks for the public masthead/operator presentation boundary."""

from pathlib import Path
import unittest


ASSETS = Path(__file__).resolve().parents[1] / "wake" / "assets"


class MastheadPresentationTests(unittest.TestCase):
    def setUp(self):
        self.html = (ASSETS / "index.html").read_text()
        self.css = (ASSETS / "nav.css").read_text()

    def test_masthead_has_one_theme_switch_and_no_decorative_theme_glyph(self):
        self.assertEqual(self.html.count('id="theme-toggle"'), 1)
        self.assertEqual(self.html.count('class="data-switch theme-switch"'), 1)
        self.assertNotIn('class="theme-icon"', self.html)

    def test_operator_entry_is_a_plain_github_actions_link(self):
        header = self.html.split('<header class="masthead">', 1)[1].split('</header>', 1)[0]
        self.assertIn('href="https://github.com/sudofx/wake/actions"', header)
        self.assertIn('>Operator</span>', header)
        self.assertIn('aria-label="Open WAKE GitHub Actions"', header)
        self.assertEqual(header.count('class="owner-status-track"'), 1)
        self.assertEqual(header.count('class="owner-status-light"'), 1)

    def test_site_has_no_authenticated_operator_control_state_machine(self):
        for forbidden in (
            'WAKE_CONTROL_URL', 'wake-owner-session', '#wake-control=',
            'data-owner-start', 'data-owner-stop', 'data-owner-reset',
            '/api/start', '/api/stop', '/api/reset',
        ):
            self.assertNotIn(forbidden, self.html)

    def test_operator_link_is_phone_safe_and_visibly_neutral(self):
        self.assertIn('.operator-actions-link{width:auto', self.css)
        self.assertIn('text-transform:uppercase', self.css)
        self.assertIn('.operator-actions-link .owner-status-light{background:var(--green)', self.css)
        self.assertIn('.operator-actions-link{width:auto;min-width:0;padding:0 2px;gap:6px}', self.css)

    def test_live_projection_still_updates_without_operator_controls(self):
        self.assertIn('data.public_cycle=Number(data.state?.version||0)', self.html)
        self.assertIn("window.WakeApplyLive?.(next)", self.html)
        self.assertIn("setInterval(refreshLiveState,10000)", self.html)


if __name__ == "__main__":
    unittest.main()
