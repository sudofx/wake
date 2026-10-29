"""Self-correction observations use pinned evidence and bounded public metadata."""
from pathlib import Path
import shutil
import subprocess
import unittest


class SelfCorrectionReaderTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which('node'), 'Node required for reader contract checks')
    def test_snapshot_transport_refresh_and_public_workflow_observations(self):
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(['node', str(root / 'tests/browser/self-correction-reader-unit.cjs')],
                                cwd=root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_page_explains_automatic_checks_and_optional_override(self):
        root = Path(__file__).resolve().parents[1]
        page = (root / 'wake/assets/self-correction/index.html').read_text()
        self.assertIn('Run a check now', page)
        self.assertIn('leave the optional repair fields blank', page)
        self.assertIn('Trusted mechanical repairs can be applied automatically', page)
        self.assertIn('Model-authored source changes still need approval', page)
        self.assertIn('Advanced: request a specific source repair', page)
        self.assertIn('every ten minutes', page)
        self.assertNotIn('window.WAKE_DEPLOYMENT', page, 'Unbound/local template must stay same-origin')
