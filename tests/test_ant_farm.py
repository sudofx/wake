"""The habitat ships as separate presentation with no authority transport."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from wake.domain_events import empty
from wake.report import export
from wake.installation_cli import _copy_public_site


class AntFarmTests(unittest.TestCase):
    def test_habitat_and_navigation_survive_filtered_public_export(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory) / 'site'
            export(destination=site, projection={'state': empty(), 'head': 'a' * 64,
                                               'events': []}, browser_only=True)
            mirror = Path(directory) / 'public'
            _copy_public_site(site, mirror)
            for name in ('ant-farm.css', 'ant-colony.js', 'ant-drawing.js', 'ant-farm.js', 'bob-markdown.js'):
                self.assertEqual((mirror / name).read_bytes(), (site / name).read_bytes())
            habitat = (mirror / 'ant-farm.html').read_text()
            self.assertIn('window.WAKE_DEPLOYMENT=', habitat)
            self.assertNotIn('runtime-activity.js', habitat)
            self.assertNotIn('masthead.css', habitat)
            self.assertIn('snapshot_only', habitat)
            self.assertIn('href="ant-farm.html"', (mirror / 'index.html').read_text())
            self.assertIn('href="ant-farm.html"', (mirror / 'blog.html').read_text())

    @unittest.skipUnless(shutil.which('node'), 'Node is required')
    def test_colony_mechanisms_and_resume(self):
        result = subprocess.run(['node', '--test', str(Path(__file__).parent / 'browser/ant-colony.cjs'), str(Path(__file__).parent / 'browser/ant-storage.cjs'), str(Path(__file__).parent / 'browser/bob-markdown.cjs')],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
