"""Regression checks for the public masthead and GitHub Actions link."""

from pathlib import Path
import unittest


ASSETS = Path(__file__).resolve().parents[1] / "wake" / "assets"


class MastheadPresentationTests(unittest.TestCase):
    def setUp(self):
        self.html = (ASSETS / "index.html").read_text()
        self.css = (ASSETS / "nav.css").read_text()

    def test_masthead_is_dark_only_and_has_no_theme_switch(self):
        self.assertNotIn('id="theme-toggle"', self.html)
        self.assertNotIn('class="data-switch theme-switch"', self.html)

    def test_actions_entry_has_repo_link_and_labeled_status(self):
        header = self.html.split('<header class="masthead">', 1)[1].split('</header>', 1)[0]
        self.assertIn('href="https://github.com/sudofx/wake"', header)
        self.assertIn('class="repo-link"', header)
        self.assertIn('href="https://github.com/sudofx/wake/actions"', header)
        self.assertIn('class="actions-light"', header)
        self.assertIn('class="actions-light-label"', header)
        self.assertIn('title="Checking…"', header)
        self.assertIn('Powered by sudofx', header)
        self.assertNotIn('Operator', header)
        for forbidden in ('owner-', 'operator-status', 'operator-actions-link',
                          'WAKE_CONTROL_URL', 'wake-owner-session',
                          'data-owner-start', 'data-owner-stop', 'data-owner-reset'):
            self.assertNotIn(forbidden, header)

    def test_actions_light_is_phone_safe_and_read_only(self):
        nav = (ASSETS / "nav.js").read_text()
        self.assertIn('.actions-light{box-sizing:border-box', self.css)
        self.assertIn('cursor:pointer', self.css)
        self.assertIn('@keyframes actions-light-pulse', self.css)
        self.assertIn('actions/workflows/wake-runner.yml', nav)
        self.assertIn('actions/workflows/operator-enable-continuity.yml/runs?per_page=10', nav)
        self.assertNotIn('actions/workflows/wake.yml/runs?branch=wake-runtime&per_page=10', nav)
        self.assertIn("['running','stopped','campaign']", nav)
        self.assertIn("state==='campaign'?'Campaign'", nav)
        self.assertIn('.actions-light[data-state="campaign"] .actions-light-track i', self.css)
        self.assertIn('.actions-light[data-state="campaign"] .actions-light-label', self.css)
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
