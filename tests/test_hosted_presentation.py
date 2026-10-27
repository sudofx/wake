"""Hosted presentation refresh cannot replace captured research or newer exports."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from wake.hosted_presentation import bind_hosted_status
from wake.installation_cli import NODE_IDS, upload_public_artifact


class HostedPresentationTests(unittest.TestCase):
    def test_refresh_preserves_snapshot_packets_and_nested_installation_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = {'live': False, 'installation_id': 'original-installation',
                        'record_heads': {n: {'version': i, 'head': n} for i, n in enumerate(NODE_IDS)},
                        'hosted_execution': {'source_revision': 'a' * 40, 'run_id': '123'}}
            (root / 'installation.json').write_text(json.dumps(manifest))
            (root / 'reader-data.json').write_bytes(b'{"private_bodies":false,"version":744}')
            (root / 'inspect').mkdir()
            packet = b'<html><head></head><body>hashed packet</body></html>'
            (root / 'inspect/index.html').write_bytes(packet)
            for relative, prefix, name in [('index.html', '', 'wake'),
                                           ('nodes/103.wake/blog/post.html', '../', '103.wake'),
                                           ('console.html', '', 'wake')]:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                deployment = {'schema': 1, 'snapshot_only': True, 'mode': 'standalone', 'instance_name': name, 'ask_bob': {'url': 'https://retired.invalid'}, 'hosted_activity': {'url': 'https://retired.invalid'}}
                page = ('<html><head><script>window.WAKE_DEPLOYMENT=' + json.dumps(deployment)
                        + ';window.WAKE_STANDALONE=true;</script>'
                        + f'<script src="{prefix}nav.js?v=old" defer></script>'
                        + f'<link rel="stylesheet" href="{prefix}theme.css?v=old">'
                        + f'<link rel="stylesheet" href="{prefix}masthead.css?v=old"></head>'
                        + '<body><header class="masthead"><nav class="compact-nav"></nav>'
                        + '<div class="header-tools"><label class="theme-switch"></label></div></header>'
                        + '<button id="reset-console-layout" type="button">Reset Console view</button></body></html>')
                path.write_text(page)
            # Reader pages inline shared navigation, unlike Console pages.
            index = root / 'index.html'
            index.write_text(index.read_text().replace('<script src="nav.js?v=old" defer></script>', '<script>/* inline navigation */</script>'))
            bound = bind_hosted_status(root, 'example/repo', 'b' * 40)
            self.assertEqual(bound['record_heads'], manifest['record_heads'])
            self.assertNotIn('retired.invalid', (root / 'index.html').read_text())
            self.assertNotIn('chatgpt.site', (root / 'index.html').read_text())
            self.assertTrue((root / 'self-correction/index.html').exists())
            self.assertIn('href="self-correction/"', (root / 'console.html').read_text())
            self.assertTrue((root / 'self-correction/self-correction.js').exists())
            self.assertEqual(bound['hosted_execution'], manifest['hosted_execution'])
            self.assertEqual((root / 'inspect/index.html').read_bytes(), packet)
            self.assertEqual((root / 'reader-data.json').read_bytes(), b'{"private_bodies":false,"version":744}')
            nested = (root / 'nodes/103.wake/blog/post.html').read_text()
            self.assertIn('"instance_name": "103.wake"', nested)
            self.assertIn('src="../hosted-status.js?', nested)
            self.assertTrue((root / 'nodes/103.wake/hosted-status.js').exists())
            self.assertIn('href="../theme.css?v='+('b'*12)+'"', nested)
            for name in ('theme.css', 'research.js', 'research.css'):
                self.assertEqual((root / 'nodes/103.wake' / name).read_bytes(),
                                 (Path(__file__).resolve().parents[1] / 'wake/assets' / name).read_bytes())
            bind_hosted_status(root, 'example/repo', 'b' * 40)
            self.assertEqual((root / 'index.html').read_text().count('class="actions-light"'), 1)
            self.assertEqual((root / 'console.html').read_text().count('class="self-correction-console-link"'), 1)
            self.assertEqual((root / 'index.html').read_text().count('src="hosted-status.js?'), 1)
            self.assertEqual((root / 'inspect/index.html').read_bytes(), packet)

    def test_presentation_refresh_rejects_an_advanced_public_parent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            remote, artifact = root / 'remote', root / 'artifact'
            remote.mkdir(); artifact.mkdir()
            def git(*args):
                return subprocess.check_output(['git', '-C', str(remote), *args], stderr=subprocess.DEVNULL, text=True).strip()
            git('init', '-b', 'wake-public')
            git('config', 'user.email', 'test@localhost'); git('config', 'user.name', 'test')
            (remote / 'data.json').write_text('old');git('add', '.');git('commit', '-m', 'old')
            captured = git('rev-parse', 'HEAD')
            (remote / 'data.json').write_text('new');git('commit', '-am', 'new')
            current = git('rev-parse', 'HEAD')
            (artifact / 'data.json').write_text('stale refresh')
            real_run = subprocess.run
            def run(args, **kwargs):
                if args[:4] == ['git', 'remote', 'add', 'origin']:
                    args = [*args[:4], str(remote)]
                return real_run(args, **kwargs)
            with patch('wake.installation_cli.subprocess.run', side_effect=run):
                with self.assertRaisesRegex(ValueError, 'snapshot advanced'):
                    upload_public_artifact(artifact, 'https://github.com/example/repo.git', 'wake-public', expected_head=captured)
            self.assertEqual(git('rev-parse', 'HEAD'), current)
            self.assertEqual((remote / 'data.json').read_text(), 'new')
