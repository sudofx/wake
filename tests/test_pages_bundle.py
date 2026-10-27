"""The Pages subset is bounded presentation, never a replacement public record."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.pages_bundle import compact
from wake.installation_cli import NODE_IDS
from wake.reader_transport import record_path


class PagesBundleTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.site=Path(self.directory.name)
        self.manifest={'schema':1,'live':False,'installation_id':'fixture',
            'record_heads':{node:{'head':node,'version':1} for node in NODE_IDS},
            'presentation':{'data_transport':'github-pinned@1'}}
        for root in [self.site,*(self.site/'nodes'/node for node in NODE_IDS)]:
            root.mkdir(parents=True,exist_ok=True)
            (root/'installation.json').write_text(json.dumps(self.manifest))
            (root/'deployment.json').write_text(json.dumps({'public_data':{'repository':'example/wake'}}))
            (root/'reader-data.json').write_text(json.dumps({'head':'h','state':{'posts':{'latest':{'id':'latest'}}}}))
            (root/'head.txt').write_text('h')
            (root/'index.html').write_text('<head><script>window.WAKE_DEPLOYMENT={"public_data":{}};</script></head>')
            (root/'research-overview.json').write_text('{"head":"h"}')

    def test_keep_recent_packets_and_assets_without_full_archives(self):
        root=self.site
        for relative in [record_path('posts','latest'),
                         'reader-records/pages/journal/0.json',record_path('posts','old')]:
            path=root/relative;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('{"captured":"exact bytes"}')
        (root/'wake-data.json').write_text('complete archive')
        (root/'events.jsonl').write_text('complete events')
        before=(root/record_path('posts','latest')).read_bytes()
        result=compact(root)
        self.assertEqual(result['record_heads'],self.manifest['record_heads'])
        self.assertEqual((root/record_path('posts','latest')).read_bytes(),before)
        self.assertTrue((root/'reader-records/pages/journal/0.json').exists())
        self.assertIn('recent-overview',(root/'index.html').read_text())
        for name in ('wake-data.json', 'events.jsonl', record_path('posts','old')):
            self.assertFalse((root/name).exists(),name)
        self.assertEqual(json.loads((root/'nodes/100.wake/installation.json').read_text()),result)

    def test_optional_details_cannot_exceed_fixed_byte_limits(self):
        detail=self.site/record_path('posts','latest');detail.parent.mkdir(parents=True);detail.write_text('x'*100)
        with patch('scripts.pages_bundle.DETAIL_LIMIT',32):
            compact(self.site)
        self.assertFalse(detail.exists())
        self.assertTrue((self.site/'reader-data.json').exists())

    def test_refuse_native_records_before_any_pruning(self):
        (self.site/'record.sqlite').write_bytes(b'not a public export')
        (self.site/'wake-data.json').write_text('keep on rejection')
        with self.assertRaisesRegex(ValueError,'Native records'):
            compact(self.site)
        self.assertEqual((self.site/'wake-data.json').read_text(),'keep on rejection')
