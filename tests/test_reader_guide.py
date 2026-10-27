"""Default reader answers are literal, bounded public passages, without inference."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from wake.reader_guide import build_guide, refresh_public_reader, MAX_GUIDE_BYTES
from wake.reader_transport import export_reader_transport, record_path
from wake.domain_events import empty

class ReaderGuideTests(unittest.TestCase):
    def fixture(self):
        post={'id':'article','title':'A test of memory','lede':'The study compares two memory conditions.',
              'body':'First paragraph.\n\n'+('Unrelated background.\n\n'*30)+'Retrieval failed when the historical notebook was unavailable. The result remains uncertain.',
              'evidence':['e'],'notebooks':['n'],'project':'p'}
        state=empty();state.update(posts={'article':post},evidence={'e':{'id':'e','content':'The controlled trial compared recall with memory included and withheld.'}},
             notebooks={'n':{'id':'n','body':'A revised notebook describes retrieval failures.', 'limitations':'The evaluation assumes a fixed environment.'}},projects={'p':{'id':'p','question':'Does memory affect recall?'}})
        return post,state
    def test_export_is_bounded_literal_and_public_only(self):
        post,state=self.fixture();guide=build_guide(post,state,'head')
        self.assertLessEqual(len(json.dumps(guide,ensure_ascii=False,separators=(',',':')).encode()),MAX_GUIDE_BYTES)
        self.assertTrue(any('historical notebook' in p['text'] for p in guide['passages']))
        self.assertEqual({s['collection'] for s in guide['sources']},{'posts','evidence','notebooks','projects'})
        with tempfile.TemporaryDirectory() as d:
            export_reader_transport({'state':state,'head':'head','events':[]},d)
            self.assertEqual(json.loads((Path(d)/record_path('guides','article')).read_text()),guide)
        post['body']='語'*100000
        guide=build_guide(post,state,'head')
        self.assertLessEqual(len(json.dumps(guide,ensure_ascii=False,separators=(',',':')).encode()),MAX_GUIDE_BYTES)
    def test_limitations_survive_large_findings_and_all_node_notebooks_are_included(self):
        post,state=self.fixture()
        state['notebooks']['n']['findings']='\n\n'.join(f'Finding {index}.' for index in range(100))
        guide=build_guide(post,state,'head')
        self.assertTrue(any(p['field']=='limitations' and 'fixed environment' in p['text'] for p in guide['passages']))
        post.update(notebooks=[],evidence=[],project='',editorial_references=[])
        for number in (100,101,102,103,200,201,202,203,300,301,302,303):
            member=f'{number}.wake';identifier=member+'::n';state['notebooks'][identifier]={'id':identifier,'limitations':'Requires independent replication.'}
            post['editorial_references'].append([{'member':member,'notebook_id':'n','sources':[{'record_url':f'/nodes/{member}/evidence.html#evidence/e1'},{'record_url':f'/nodes/{member}/evidence.html#evidence/e2'}]}])
        guide=build_guide(post,state,'head')
        self.assertEqual(len([source for source in guide['sources'] if source['collection']=='notebooks']),12)

    def test_clipped_structured_source_is_a_reference_not_raw_answer_text(self):
        post,state=self.fixture()
        state['evidence']['e'].update(source='https://example.org/paper',content='{"excerpt":"clipped')
        guide=build_guide(post,state,'head')
        source=next(row for row in guide['sources'] if row['record_id']=='e')
        self.assertEqual(source['label'],'https://example.org/paper')
        self.assertFalse(any(row['source']==source['id'] for row in guide['passages']))
        self.assertTrue(any(row['reason']=='structured excerpt unavailable' for row in guide['omitted']))

    def test_shared_editorial_references_resolve_public_node_details(self):
        post,state=self.fixture()
        post.update(notebooks=[],evidence=[],project='')
        state['notebooks']['100.wake::n']=dict(state['notebooks']['n'],id='100.wake::n')
        post['editorial_references']=[[{'member':'100.wake','notebook_id':'n','record_url':'/nodes/100.wake/projects.html#projects/notebook:n'}]]
        guide=build_guide(post,state,'head')
        self.assertIn('100.wake::n',[source['record_id'] for source in guide['sources']])
        self.assertTrue(any('revised notebook' in row['text'] for row in guide['passages']))

    def test_presentation_refresh_preserves_archive_and_rejects_mixed_heads(self):
        post,state=self.fixture()
        with tempfile.TemporaryDirectory() as d:
            site=Path(d);packet={'head':'same','state':state,'events':[]}
            original=json.dumps(packet).encode();(site/'wake-data.json').write_bytes(original)
            (site/'reader-data.json').write_text(json.dumps({'head':'same'}))
            (site/'ask-bob.js').write_text('/* old chat */')
            (site/'blog.html').write_text('<script src="reader-data.js"></script><script>/* old chat */</script><script>/* Homepage reading experience and browser-local Ask Bob interface. */oldPet()</script>')
            refresh_public_reader(site)
            self.assertEqual((site/'wake-data.json').read_bytes(),original)
            self.assertIn('ask-bob-guide.js',(site/'blog.html').read_text())
            self.assertIn('data-bob-collection="notebooks"',(site/'blog.html').read_text())
            self.assertNotIn('oldPet()', (site/'blog.html').read_text())
            self.assertIn('reader-data.js?v=20261027-autoload',(site/'blog.html').read_text())
            self.assertTrue((site/record_path('guides',post['id'])).exists())
            (site/'reader-data.json').write_text(json.dumps({'head':'other'}))
            with self.assertRaisesRegex(ValueError,'captured snapshot'):
                refresh_public_reader(site)

    @unittest.skipUnless(shutil.which('node'),'Node required for actual retrieval execution')
    def test_answers_and_download_guards(self):
        post,state=self.fixture()
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'guide.json').write_text(json.dumps(build_guide(post,state,'head')))
            shutil.copy(Path(__file__).resolve().parents[1]/'wake/assets/ask-bob-guide.js',root/'guide.mjs')
            result=subprocess.run(['node',str(Path(__file__).parent/'browser/ask-bob-guide.cjs'),str(root)],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn('PASS',result.stdout)
