"""Regression checks for the public masthead and GitHub Actions link."""

from pathlib import Path
import unittest


ASSETS = Path(__file__).resolve().parents[1] / "wake" / "assets"


class MastheadPresentationTests(unittest.TestCase):
    def setUp(self):
        self.html = (ASSETS / "index.html").read_text()
        self.css = (ASSETS / "nav.css").read_text()

    def test_masthead_has_one_theme_switch(self):
        self.assertEqual(self.html.count('id="theme-toggle"'), 1)
        self.assertEqual(self.html.count('class="data-switch theme-switch"'), 1)

    def test_actions_entry_is_only_a_green_light_link(self):
        header = self.html.split('<header class="masthead">', 1)[1].split('</header>', 1)[0]
        self.assertIn('href="https://github.com/sudofx/wake/actions"', header)
        self.assertIn('class="actions-light"', header)
        self.assertNotIn('Operator', header)
        for forbidden in ('owner-', 'operator-status', 'operator-actions-link',
                          'WAKE_CONTROL_URL', 'wake-owner-session',
                          'data-owner-start', 'data-owner-stop', 'data-owner-reset'):
            self.assertNotIn(forbidden, header)

    def test_actions_light_is_phone_safe_without_runtime_state_css(self):
        self.assertIn('.actions-light{box-sizing:border-box', self.css)
        self.assertIn('@keyframes actions-light-pulse', self.css)
        self.assertNotIn('.owner-', self.css)
        self.assertNotIn('operator-status', self.css)

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
