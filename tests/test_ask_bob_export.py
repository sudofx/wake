"""Reader assistance assets ship as inert presentation, never Console controls."""
from pathlib import Path
import json
import hashlib
import os
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
            for name in ('ask-bob.js', 'ask-bob.css', 'ask-bob-browser.js', 'ask-bob-guide.js', 'ask-bob-engine.js',
                         'ask-bob-engine.wasm', 'ask-bob-engine-compat.js', 'ask-bob-engine-compat.wasm',
                         'ask-bob-engine.LICENSE.txt', 'ask-bob-engine.json', 'ask-bob-private.js',
                         'ask-bob-engine-private.js', 'ask-bob-engine-private.wasm', 'ask-bob-engine-private.LICENSE.txt'):
                if name.endswith('.json'):
                    self.assertEqual(json.loads((mirror / name).read_text()), json.loads((site / name).read_text()))
                else:
                    self.assertEqual((mirror / name).read_bytes(), (site / name).read_bytes())
            self.assertIn('window.WakeAskBob', (mirror / 'index.html').read_text())
            for name in ('bob-chat.html', 'bob-chat.js', 'bob-chat.css', 'ask-bob-context.js',
                         'ask-bob-gpu.js', 'ask-bob-gpu-worker.js', 'ask-bob-gpu-engine.js',
                         'ask-bob-gpu-2b.wasm', 'ask-bob-gpu-4b.wasm'):
                if name.endswith('.html'):
                    self.assertIn('bob-chat.js', (mirror / name).read_text())
                    self.assertIn('"snapshot_only": true', (mirror / name).read_text())
                else:
                    self.assertEqual((mirror / name).read_bytes(), (site / name).read_bytes())
            node_view = root / 'node-view'
            _copy_public_site(site, node_view, include_reader_inference=False)
            self.assertTrue((node_view / 'index.html').exists())
            self.assertFalse(list(node_view.glob('ask-bob-engine*')))
            self.assertEqual((node_view / 'ask-bob.js').read_bytes(), (site / 'ask-bob.js').read_bytes())

    def test_vendored_browser_engine_has_verified_bytes_and_license(self):
        assets = Path(__file__).resolve().parents[1] / 'wake/assets'
        manifest = json.loads((assets / 'ask-bob-engine.json').read_text())
        self.assertEqual(manifest['license'], 'MIT')
        for name, digest in manifest['files'].items():
            self.assertEqual(hashlib.sha256((assets / name).read_bytes()).hexdigest(), digest)
        self.assertIn('Permission is hereby granted', (assets / 'ask-bob-engine.LICENSE.txt').read_text())
        self.assertEqual((assets / 'ask-bob-engine.wasm').read_bytes()[:4], b'\x00asm')
        # A file named single-thread can still import shared memory. Check the
        # actual private build's WASM memory flags rather than trusting its name.
        binary = (assets / 'ask-bob-engine-private.wasm').read_bytes()
        def unsigned(offset):
            value = shift = 0
            while True:
                byte = binary[offset]
                offset += 1
                value |= (byte & 127) << shift
                if not byte & 128:
                    return value, offset
                shift += 7
        offset, found_memory = 8, False
        while offset < len(binary):
            section = binary[offset]
            length, start = unsigned(offset + 1)
            if section == 5:
                count, cursor = unsigned(start)
                self.assertEqual(count, 1)
                flags, _ = unsigned(cursor)
                self.assertFalse(flags & 2, 'Public fallback must not require shared memory')
                found_memory = True
            offset = start + length
        self.assertTrue(found_memory, 'Expected a defined private WASM memory')

    def test_gpu_engine_and_models_are_pinned_with_verified_local_bytes(self):
        assets = Path(__file__).resolve().parents[1] / 'wake/assets'
        manifest = json.loads((assets / 'ask-bob-gpu-engine.json').read_text())
        self.assertEqual(manifest['license'], 'Apache-2.0')
        for name, digest in manifest['files'].items():
            self.assertEqual(hashlib.sha256((assets / name).read_bytes()).hexdigest(), digest)
        for model in manifest['models']:
            self.assertRegex(model['revision'], r'^[a-f0-9]{40}$')
            self.assertEqual((assets / model['model_lib']).read_bytes()[:4], b'\x00asm')
            self.assertIn(model['revision'], (assets / 'ask-bob-gpu.js').read_text())

    @unittest.skipUnless(shutil.which('node'), 'Node required for GPU lifecycle contracts')
    def test_gpu_cancellation_and_citation_identity(self):
        result = subprocess.run(['node', str(Path(__file__).parent / 'browser/bob-gpu.cjs')],
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    @unittest.skipUnless(shutil.which('node') and os.environ.get('PLAYWRIGHT_MODULE'),
                         'Opt-in popup acceptance requires Playwright')
    def test_device_chat_lifecycle_and_private_context(self):
        result = subprocess.run(['node', str(Path(__file__).parent / 'browser/bob-device.cjs')],
                                capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    @unittest.skipUnless(shutil.which('node'), 'Node is required for the browser context contract')
    def test_browser_context_uses_only_bounded_version_matched_public_sources(self):
        script = Path(__file__).parent / 'browser/ask-bob-context.cjs'
        result = subprocess.run(['node', str(script)], check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout)['result'], 'PASS')

    @unittest.skipUnless(shutil.which('node'), 'Node is required for the browser startup contract')
    def test_browser_startup_can_cancel_stalled_workers_and_retry(self):
        script = Path(__file__).parent / 'browser/ask-bob-loader.cjs'
        result = subprocess.run(['node', str(script)], capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)['result'], 'PASS')

    @unittest.skipUnless(shutil.which('node'), 'Node is required for the private-memory contract')
    def test_private_memory_adapter_keeps_cache_and_generation_boundaries(self):
        script = Path(__file__).parent / 'browser/ask-bob-private.cjs'
        result = subprocess.run(['node', str(script)], check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout)['result'], 'PASS')

    @unittest.skipUnless(shutil.which('node'), 'Node is required for the answer lifecycle contract')
    def test_browser_answer_can_stop_a_dead_worker_and_accept_multiple_replies(self):
        script = Path(__file__).parent / 'browser/ask-bob-answer.cjs'
        result = subprocess.run(['node', str(script)], capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)['result'], 'PASS')
