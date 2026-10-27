"""Reader cost is bounded; optional detail never becomes operational authority."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
import shutil
import subprocess

from wake.reader_transport import export_reader_transport, record_path, MAX_BOOTSTRAP_BYTES
from wake.domain_events import empty


class ReaderTransportTests(unittest.TestCase):
    def test_combined_catalog_keeps_all_node_topics_within_bootstrap_budget(self):
        from wake.research_expansion import ASSIGNMENTS
        import tomllib
        root = Path(__file__).resolve().parents[1]
        catalog = {t['id']: t for t in tomllib.loads((root / 'example.research-topics.toml').read_text())['topics']}
        packet = self.packet()
        from wake.installation_projection import build_unified_projection
        packets = {}
        for parent, assigned in ASSIGNMENTS.items():
            for suffix in range(4):
                node = parent[0] + str(suffix).zfill(2) + '.wake'
                local = deepcopy(packet)
                local['state']['research_topics'] = [catalog[t] for t in assigned]
                packets[node] = local
        projection = build_unified_projection(packets, {}, 'fixture')
        packet['state']['research_topics'] = projection['state']['research_topics']
        with tempfile.TemporaryDirectory() as directory:
            result = export_reader_transport(packet, Path(directory))
            topics = result['state']['research_topics']
            self.assertEqual(len(topics), 17)
            self.assertEqual(sum(len(t['origins']) for t in topics), 88)
            self.assertEqual({t['id'].split('::')[-1] for t in topics}, set(catalog))
            self.assertLessEqual((Path(directory) / 'reader-data.json').stat().st_size, MAX_BOOTSTRAP_BYTES)

    def packet(self):
        state = empty()
        state['invocations'] = {f'i-{i}': {'id': f'i-{i}', 'status': 'rejected',
            'time': '2026-10-17T10:00:00Z', 'provider': 'fixture',
            'provider_attempts': [{'detail': 'x' * 10000}]} for i in range(300)}
        state['evidence'] = {f'e-{i}': {'id': f'e-{i}', 'source': 'https://example.test/paper',
            'content': 'evidence' * 400} for i in range(100)}
        state['posts'] = {f'p-{i}': {'id': f'p-{i}', 'body': 'Exact published text. ' * 250,
            'title': 'A published story', 'created_by': 'i-1', 'evidence': ['e-1']} for i in range(40)}
        state['journal'] = [{'cycle': i, 'invocation': f'i-{i}', 'title': 'Journal',
                             'summary': 'Recorded summary'} for i in range(100)]
        return {'state': state, 'events': [], 'head': 'a' * 64,
                'generated': '2026-10-17T10:00:00Z', 'metrics': {'storage': {'event_count': 2000}}}

    def test_journal_context_distinguishes_nodes_with_the_same_cycle(self):
        packet = self.packet()
        packet['state']['journal'] = [
            {'cycle': 3, 'invocation': '100.wake::w-one', 'title': 'First node', 'summary': 'First summary'},
            {'cycle': 3, 'invocation': '101.wake::w-two', 'title': 'Second node', 'summary': 'Second summary'},
        ]
        with tempfile.TemporaryDirectory() as directory:
            export_reader_transport(packet, Path(directory))
            for row in packet['state']['journal']:
                detail = json.loads((Path(directory) / record_path('journal', row['invocation'])).read_text())
                self.assertEqual(detail['item'], row)
                self.assertEqual(detail['head'], packet['head'])

    def test_growing_evidence_and_attempt_bodies_do_not_travel_on_initial_load(self):
        packet = self.packet(); before = deepcopy(packet)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            export_reader_transport(packet, target)
            raw = (target / 'reader-data.json').read_bytes()
            self.assertLessEqual(len(raw), MAX_BOOTSTRAP_BYTES)
            overview = json.loads(raw)
            self.assertEqual(overview['metrics'], packet['metrics'])
            self.assertEqual(overview['reader_transport']['counts']['invocations'], 300)
            self.assertNotIn('provider_attempts', next(iter(overview['state']['invocations'].values())))
            self.assertNotIn('content', next(iter(overview['state']['evidence'].values())))
            for row in overview['state']['journal']:
                self.assertIn(row['invocation'], overview['state']['invocations'])
            detail = json.loads((target / record_path('posts', 'p-0')).read_text())
            self.assertEqual(detail['item'], packet['state']['posts']['p-0'])
            self.assertEqual(detail['related']['evidence']['e-1'], packet['state']['evidence']['e-1'])
            self.assertEqual(detail['related']['invocations']['i-1'], packet['state']['invocations']['i-1'])
            self.assertEqual(detail['head'], overview['head'])
        self.assertEqual(packet, before)

    def test_pagination_retains_all_exact_rows_and_journal_receipts(self):
        packet = self.packet()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory);export_reader_transport(packet, target)
            rows=[];index=0
            while index is not None:
                page=json.loads((target/f'reader-records/pages/journal/{index}.json').read_text())
                rows.extend(page['rows'])
                for row in page['rows']:
                    self.assertEqual(page['related']['invocations'][row['invocation']],
                                     packet['state']['invocations'][row['invocation']])
                index=page['next']
            self.assertEqual(rows,list(reversed(packet['state']['journal'])))
            selected=json.loads((target/record_path('journal','cycle:1')).read_text())
            self.assertEqual(selected['item']['invocation'],'i-1')

    def test_record_paths_are_injective_and_have_portable_segments(self):
        names=['../private', '100.wake::colon', '_3A', ':', '日本語', 'x'*500]
        paths=[record_path('evidence',name) for name in names]
        self.assertEqual(len(paths),len(set(paths)))
        for path in paths:
            self.assertTrue(path.startswith('reader-records/evidence/'))
            self.assertNotIn('..',path)
            self.assertTrue(all(len(part)<=69 for part in Path(path).parts[2:]))

    def test_recent_records_follow_recorded_time_not_canonical_id_order(self):
        packet=self.packet()
        packet['state']['invocations']['a-latest']={'id':'a-latest','time':'2030-01-01T00:00:00Z','status':'accepted'}
        packet['state']['invocations']=dict(sorted(packet['state']['invocations'].items()))
        packet['state']['commitments']={'old-open':{'id':'old-open','status':'open','task':'Still owed'}}
        with tempfile.TemporaryDirectory() as directory:
            overview=export_reader_transport(packet,Path(directory))
            self.assertIn('a-latest',overview['state']['invocations'])
            self.assertIn('old-open',overview['state']['commitments'])

    @unittest.skipUnless(shutil.which('node'), 'Node required for cold publication recovery')
    def test_cold_reader_recovers_matching_snapshot_without_mixing_generations(self):
        root=Path(__file__).parents[1]
        result=subprocess.run(['node',str(root/'tests/browser/reader-snapshot-recovery.cjs'),
                               str(root/'wake/assets/reader-data.js')],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('PASS',result.stdout)

    @unittest.skipUnless(shutil.which('node'), 'Node required for mixed exporter compatibility')
    def test_resident_old_exporter_template_does_not_break_before_runtime_adoption(self):
        source=Path(__file__).parents[1]/'wake/assets/index.html'
        program=r'''
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const html=fs.readFileSync(process.argv[1],'utf8');
const script=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(match=>match[1]).find(text=>text.includes('if(!window.WakeData)'));
(async()=>{
 const calls=[],window={};
 const fetch=async url=>{calls.push(url);return url==='reader-data.json'?{status:404}:{ok:true,json:async()=>({head:'old',state:{version:4}})}};
 vm.runInNewContext(script,{window,fetch});assert.equal((await window.WakeData).head,'old');
 assert.deepEqual(calls,['reader-data.json','wake-data.json']);
 const existing={state:{version:5}},ready={WakeData:Promise.resolve(existing)};
 vm.runInNewContext(script,{window:ready,fetch(){throw Error('New bootstrap downloaded twice');}});
 assert.equal(await ready.WakeData,existing);
})().catch(error=>{console.error(error);process.exitCode=1;});
'''
        subprocess.run(['node','-e',program,str(source)],check=True,capture_output=True,text=True)
