"""The shared export seam installs navigation at each artifact's own root."""
from pathlib import Path
import tempfile
import unittest
from wake.report import _deployment_site


class InstallationNavigationTests(unittest.TestCase):
    def test_all_exported_pages_receive_one_selector_asset_with_relative_roots(self):
        shell = '<html><head></head><body><header class="masthead"></header><main></main></body></html>'
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for name in ('index.html', 'console.html', 'blog/post.html', 'questions/question.html'):
                page = target / name
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text(shell)
            _deployment_site(target, standalone=True)
            _deployment_site(target, standalone=True)
            for name in ('index.html', 'console.html', 'blog/post.html', 'questions/question.html'):
                with self.subTest(page=name):
                    content = (target / name).read_text()
                    self.assertEqual(content.count('installation-console.js?'), 1)
                    prefix = '../' if '/' in name else ''
                    self.assertIn(f'src="{prefix}installation-console.js?', content)
                    self.assertIn('class="brand-lockup"', content)
            self.assertTrue((target / 'installation-console.js').exists())
