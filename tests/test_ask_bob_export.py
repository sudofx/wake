"""Reader assistance assets ship as inert presentation, never Console controls."""
from pathlib import Path
import tempfile
import unittest

from wake.domain_events import empty
from wake.installation_cli import _copy_public_site
from wake.report import export


class AskBobExportTests(unittest.TestCase):
    def test_export_and_filtered_mirror_include_reader_assets_without_console_mount(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / 'site'
            export(destination=site, projection={'state': empty(), 'head': 'a' * 64,
                                                'events': []}, browser_only=True)
            self.assertIn('window.WakeAskBob', (site / 'index.html').read_text())
            self.assertIn('ask-bob.css', (site / 'index.html').read_text())
            self.assertNotIn('WakeAskBob', (site / 'console.html').read_text())
            mirror = root / 'mirror'
            _copy_public_site(site, mirror)
            for name in ('ask-bob.js', 'ask-bob.css'):
                self.assertEqual((mirror / name).read_bytes(), (site / name).read_bytes())
            self.assertIn('window.WakeAskBob', (mirror / 'index.html').read_text())
