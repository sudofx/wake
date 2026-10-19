"""Reader assistance assets ship as inert presentation, never Console controls."""
from pathlib import Path
import json
import hashlib
import shutil
import subprocess
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
            for name in ('ask-bob.js', 'ask-bob.css', 'ask-bob-browser.js', 'ask-bob-engine.js',
                         'ask-bob-engine.wasm', 'ask-bob-engine.LICENSE.txt', 'ask-bob-engine.json'):
                if name.endswith('.json'):
                    self.assertEqual(json.loads((mirror / name).read_text()), json.loads((site / name).read_text()))
                else:
                    self.assertEqual((mirror / name).read_bytes(), (site / name).read_bytes())
            self.assertIn('window.WakeAskBob', (mirror / 'index.html').read_text())

    def test_vendored_browser_engine_has_verified_bytes_and_license(self):
        assets = Path(__file__).resolve().parents[1] / 'wake/assets'
        manifest = json.loads((assets / 'ask-bob-engine.json').read_text())
        self.assertEqual(manifest['license'], 'MIT')
        for name, digest in manifest['files'].items():
            self.assertEqual(hashlib.sha256((assets / name).read_bytes()).hexdigest(), digest)
        self.assertIn('Permission is hereby granted', (assets / 'ask-bob-engine.LICENSE.txt').read_text())
        self.assertEqual((assets / 'ask-bob-engine.wasm').read_bytes()[:4], b'\x00asm')

    @unittest.skipUnless(shutil.which('node'), 'Node is required for the browser context contract')
    def test_browser_context_uses_only_bounded_version_matched_public_sources(self):
        script = Path(__file__).parent / 'browser/ask-bob-context.cjs'
        result = subprocess.run(['node', str(script)], check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout)['result'], 'PASS')
