"""Inspection remains attributable static presentation through public delivery."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from urllib.parse import urljoin, urlsplit

from tests import test_installation_projection as fixtures
from wake.inspection import CANONICAL_ROOT, PUBLIC_FILES, export_inspection, validate_inspection
from wake.installation_cli import _copy_public_site, package_public_history
from wake.installation_site import export_unified_site, export_unified_history


class InspectionExportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.packets, _, self.projection = fixtures.InstallationProjectionTests().build()
        self.site = self.root / 'site'
        export_unified_site(self.projection, self.site)

    def test_manifest_exact_resources_claims_and_dated_snapshot(self):
        manifest = validate_inspection(self.site)
        self.assertEqual(manifest['format'], 'wake-inspection@1')
        self.assertEqual(manifest['version'], 1)
        self.assertIsNone(manifest['uploaded_at'])
        self.assertIsNone(manifest['source']['executing_revision'])
        self.assertFalse(manifest['snapshot']['authoritative'])
        self.assertEqual(set(manifest['snapshot']['node_heads']), {'100', '101'})
        self.assertTrue(manifest['published_records'])
        self.assertLessEqual(len(manifest['published_records']), 5)
        for item in manifest['resources']:
            raw = (self.site / 'inspect' / item['url']).read_bytes()
            self.assertEqual(item['sha256'], hashlib.sha256(raw).hexdigest())
            self.assertEqual(item['bytes'], len(raw))
            self.assertEqual(item['canonical_url'], urljoin(CANONICAL_ROOT, item['url']))
        for item in manifest['published_records']:
            self.assertTrue(urlsplit(urljoin(CANONICAL_ROOT, item['url'])).path.startswith('/wake/reader-records/'))
        packet = (self.site / 'inspect/packet.md').read_text()
        self.assertIn((self.site / 'inspect/demo.json').read_text(), packet)
        self.assertLess(len(packet.encode()), 65536)
        self.assertIn('href="inspect/index.html"', (self.site / 'index.html').read_text())
        self.assertNotIn('href="inspect/index.html"', (self.site / 'console.html').read_text())
        self.assertNotIn('<script', (self.site / 'inspect/index.html').read_text())

    def test_public_copy_and_gzip_packaging_keep_hashed_bytes_and_private_exclusions(self):
        (self.site / 'inspect/private.md').write_text('PRIVATE-INSPECTION-SENTINEL')
        (self.site / 'inspect/nested').mkdir()
        (self.site / 'inspect/nested/demo.json').write_text('{"secret":"PRIVATE-INSPECTION-SENTINEL"}')
        (self.site / '.wake-continuity').mkdir()
        (self.site / '.wake-continuity/checkpoint.md').write_text('PRIVATE-CONTINUITY-SENTINEL')
        mirror = self.root / 'mirror'
        _copy_public_site(self.site, mirror)
        self.assertEqual({p.name for p in (mirror / 'inspect').iterdir()}, PUBLIC_FILES)
        validate_inspection(mirror)
        for name in PUBLIC_FILES:
            self.assertEqual((mirror / 'inspect' / name).read_bytes(), (self.site / 'inspect' / name).read_bytes())
        self.assertFalse((mirror / '.wake-continuity').exists())
        generations = {}
        for node, snapshot in self.packets.items():
            directory = self.root / node
            directory.mkdir()
            (directory / 'events.jsonl').write_text(''.join(json.dumps(e) + '\n' for e in snapshot['events']))
            generations[node] = directory
        export_unified_history(generations, self.packets, mirror)
        package_public_history(mirror, threshold=1)
        validate_inspection(mirror)
        self.assertTrue((mirror / 'events.jsonl.gz').exists())
        self.assertFalse(list(mirror.rglob('*.sqlite')))

    def test_hash_and_navigation_corruption_fail(self):
        demo = self.site / 'inspect/demo.json'
        demo.write_text(demo.read_text() + ' ')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            validate_inspection(self.site)
        export_inspection(self.site, self.projection)
        page = self.site / 'inspect/index.html'
        page.write_text(page.read_text().replace('href="README.md"', 'href="/inspect/missing.md"'))
        manifest_path = self.site / 'inspect/manifest.json'
        manifest = json.loads(manifest_path.read_text())
        for resource in manifest['resources']:
            if resource['id'] == 'index':
                resource.update(sha256=hashlib.sha256(page.read_bytes()).hexdigest(), bytes=page.stat().st_size)
        manifest_path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'navigation link'):
            validate_inspection(self.site)

    def test_exact_record_identity_and_symlinks_fail(self):
        manifest = validate_inspection(self.site)
        path = self.site / 'inspect' / manifest['published_records'][0]['url']
        packet = json.loads(path.read_text())
        packet['head'] = 'different-generation'
        path.write_text(json.dumps(packet))
        with self.assertRaisesRegex(ValueError, 'identity mismatch'):
            validate_inspection(self.site)
        packet['head'] = manifest['snapshot']['head']
        path.write_text(json.dumps(packet))
        demo = self.site / 'inspect/demo.json'
        saved = self.root / 'demo.json'
        demo.rename(saved)
        demo.symlink_to(saved)
        with self.assertRaises(ValueError):
            validate_inspection(self.site)

    def test_both_existing_node_identity_forms_and_no_invented_examples(self):
        projection = dict(self.projection)
        projection['source'] = dict(projection['source'])
        projection['source']['node_heads'] = {node + '.wake': value for node, value in projection['source']['node_heads'].items()}
        manifest = export_inspection(self.site, projection)
        self.assertEqual(set(manifest['snapshot']['node_heads']), {'100.wake', '101.wake'})
        for pointer in manifest['published_records']:
            (self.site / 'inspect' / pointer['url']).unlink()
        manifest = export_inspection(self.site, projection)
        self.assertEqual(manifest['published_records'], [])
        self.assertIn('No matching bounded example records', (self.site / 'inspect/evidence.md').read_text())


if __name__ == '__main__':
    unittest.main()
