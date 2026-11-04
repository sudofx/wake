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
    def test_retired_help_removed_from_captured_pages_and_inspection_retired(self):
        from wake.reader_presentation import remove_retired_reader
        old = ('<html><head><script>/*\n * WAKE✳︎ plain-language help.\n */'
               'window.WakeHelp={};</script><script src="../help.js?v=old"></script></head>'
               '<body><button class="help-trigger" data-help="blog">?</button>'
               '<div id="help-layer" hidden><section id="help-panel">'
               '<div class="help-copy">obsolete explanation</div></section></div>'
               '<section id="evidence-content">Why does this happen?</section></body></html>')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in ('index.html', 'nodes/103.wake/index.html', 'inspect/index.html'):
                page = root / relative
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text(old)
            (root / 'help.js').write_text('retired')
            remove_retired_reader(root)
            self.assertFalse((root / 'help.js').exists())
            for relative in ('index.html', 'nodes/103.wake/index.html'):
                page = (root / relative).read_text()
                self.assertNotIn('help-', page)
                self.assertNotIn('WakeHelp', page)
                self.assertNotIn('help.js', page)
                self.assertIn('Why does this happen?', page)
                self.assertIn('evidence-content', page)
            self.assertFalse((root / 'inspect/index.html').exists())
            remove_retired_reader(root)
            self.assertFalse((root / 'inspect/index.html').exists())

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
            (root / 'self-correction').mkdir()
            (root / 'self-correction/index.html').write_bytes(packet)
            (root / 'scientific-research.html').write_bytes(packet)
            (root / 'scientific-research.json').write_bytes(b'{"retained":true}')
            for prefix in (root, root / 'nodes/103.wake'):
                backgrounds = prefix / 'backgrounds'
                backgrounds.mkdir(parents=True)
                for name in ('ant-soil-v1.png', 'ant-sand-v2.png'):
                    (backgrounds / name).write_bytes(b'retired terrain')
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
                path.write_text(page.replace('</body>', '<a href="inspect/index.html">Inspection</a>'
                    '<a href="self-correction/">Self-correction</a>'
                    '<a href="scientific-research.html">Experiments</a></body>'))
            # Reader pages inline shared navigation, unlike Console pages.
            index = root / 'index.html'
            index.write_text(index.read_text().replace('<script src="nav.js?v=old" defer></script>', '<script>/* inline navigation */</script>'))
            # Captured snapshots still contain the removed conversation bundle.
            retired = root / 'ask-bob-engine.wasm'
            retired.write_bytes(b'retired model engine')
            (root / 'bob-chat.html').write_text('<html><head></head></html>')
            guide = root / 'reader-records/guides/old.json'
            guide.parent.mkdir(parents=True)
            guide.write_text('{"obsolete":"derived conversation passages"}')
            index.write_text(index.read_text().replace('</head>',
                '<link rel="stylesheet" href="ask-bob.css"><script>'
                '/* Private browser conversation views; never research authority or exported state. */'
                'window.WakeAskBob={};'
                '/* Render exported research records and reader navigation; browser interactions never mutate authority. */'
                '</script></head>'))
            bound = bind_hosted_status(root, 'example/repo', 'b' * 40)
            self.assertFalse(retired.exists())
            self.assertFalse((root / 'bob-chat.html').exists())
            self.assertFalse(guide.exists())
            self.assertNotIn('WakeAskBob', index.read_text())
            self.assertNotIn('ask-bob.css', index.read_text())
            self.assertEqual(bound['record_heads'], manifest['record_heads'])
            experiment = (root / 'ant-experiment.html').read_text()
            self.assertIn('"presentation_revision": "' + 'b' * 40 + '"', experiment)
            self.assertNotIn('src="public-data.js', experiment)
            self.assertNotIn('runtime-activity.js', experiment)
            for name in ('ant-farm.html', 'ant-experiment.html'):
                page = (root / name).read_text()
                self.assertEqual(page.count('<header class="masthead">'), 1, name)
                self.assertIn('src="nav.js?', page, name)
                self.assertNotIn('src="public-data.js', page, name)
                self.assertNotIn('"public_data"', page, name)
                for label in ('Explore', 'Research', 'Journal', 'Bob’s Blog', 'GitHub'):
                    self.assertIn('>' + label + '</a>', page, (name, label))
            self.assertIn('src="public-data.js', index.read_text())
            self.assertIn('src="ant-farm.js?v=' + 'b' * 12, (root / 'ant-farm.html').read_text())
            self.assertFalse(list(root.rglob('ant-soil-v1.png')))
            self.assertFalse(list(root.rglob('ant-sand-v2.png')))
            self.assertTrue((root / 'backgrounds/ant-body-v1.png').is_file())
            self.assertTrue((root / 'ant-experiment.js').is_file())
            self.assertNotIn('retired.invalid', (root / 'index.html').read_text())
            self.assertNotIn('chatgpt.site', (root / 'index.html').read_text())
            self.assertEqual((root / 'reader-data.json').read_bytes(), b'{"private_bodies":false,"version":744}')
            nested = (root / 'nodes/103.wake/blog/post.html').read_text()
            self.assertIn('"instance_name": "103.wake"', nested)
            self.assertIn('src="../hosted-status.js?', nested)
            self.assertIn('src="../hosted-status.js?v='+('b'*12)+'"', nested)
            self.assertTrue((root / 'nodes/103.wake/hosted-status.js').exists())
            self.assertIn('href="../theme.css?v='+('b'*12)+'"', nested)
            for name in ('theme.css', 'research.js', 'research.css'):
                self.assertEqual((root / 'nodes/103.wake' / name).read_bytes(),
                                 (Path(__file__).resolve().parents[1] / 'wake/assets' / name).read_bytes())
            bind_hosted_status(root, 'example/repo', 'b' * 40)
            self.assertEqual((root / 'index.html').read_text().count('class="actions-light"'), 1)
            self.assertNotIn('self-correction-console-link', (root / 'console.html').read_text())
            self.assertEqual((root / 'index.html').read_text().count('src="hosted-status.js?'), 1)
            self.assertFalse((root / 'inspect/index.html').exists())
            self.assertNotIn('inspect/index.html', index.read_text())
            self.assertNotIn('self-correction/', index.read_text())
            self.assertNotIn('scientific-research.html', index.read_text())
            self.assertEqual((root / 'scientific-research.json').read_bytes(), b'{"retained":true}')
            self.assertFalse((root / 'self-correction/index.html').exists())
            self.assertFalse((root / 'scientific-research.html').exists())

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
