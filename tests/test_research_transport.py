"""Console cost follows its overview, never retained provider transcript size."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from wake.research_transport import export_research_transport, MAX_OVERVIEW_BYTES, MAX_WAKE_SUMMARIES


ROOT = Path(__file__).resolve().parents[1]


class ResearchTransportTests(unittest.TestCase):
    def projection(self, size=1):
        return {
            'projection_kind': 'disposable-research-view', 'head': 'record-head', 'version': 7,
            'metrics': {'completed': 123456, 'outcomes': {'accepted': 17}},
            'matrix': {'cells': [{'id': 'cell', 'score': 0.7, 'origin': {'node': '301.wake'}}]},
            'wakes': [{
                'id': '../../unsafe/wake', 'status': 'accepted', 'origin': {'node': '301.wake'},
                'context': {'available': True, 'fields': ['objective', 'evidence'],
                            'characters': size, 'system': 'x' * size,
                            'request': {'context': {'objective': 'Question', 'evidence': 'x' * size}}},
                'attempts': [{'elapsed_ms': 1200, 'usage': {'promptTokenCount': 100}}],
                'response': 'r' * size, 'events': [{'kind': 'accepted', 'hash': 'terminal'}],
                'receipt': {'available': True, 'hash': 'terminal'},
                'proposal': {'summary': 'Recorded result'},
            }],
        }

    def test_large_transcripts_stay_out_of_initial_load_and_selected_detail_is_exact(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            small = self.projection(1)
            export_research_transport(small, root)
            small_size = (root / 'research-overview.json').stat().st_size
            original = self.projection(2_000_000)
            before = deepcopy(original)
            overview = export_research_transport(original, root)
            self.assertEqual(original, before)
            self.assertLess((root / 'research-overview.json').stat().st_size, small_size + 100)
            self.assertEqual(overview['metrics'], original['metrics'])
            self.assertEqual(overview['matrix'], original['matrix'])
            wake = overview['wakes'][0]
            self.assertEqual(wake['origin'], {'node': '301.wake'})
            self.assertEqual(wake['attempts'], original['wakes'][0]['attempts'])
            self.assertNotIn('request', wake['context'])
            self.assertNotIn('system', wake['context'])
            self.assertNotIn('response', wake)
            self.assertNotIn('events', wake)
            self.assertEqual(wake['context_allocation']['results'], 2_000_002)
            self.assertRegex(wake['detail_url'], r'^research-details/[a-f0-9]{64}\.json$')
            detail = json.loads((root / wake['detail_url']).read_text())
            self.assertEqual(detail['wake'], {k:v for k,v in original['wakes'][0].items() if k != 'origin'})
            # Regenerating identical data keeps the immutable link stable.
            self.assertEqual(export_research_transport(original, root)['wakes'][0]['detail_url'], wake['detail_url'])
            original['head'] = 'later-head'
            original['version'] += 1
            original['wakes'][0]['origin']['head'] = 'later-node-head'
            self.assertEqual(export_research_transport(original, root)['wakes'][0]['detail_url'], wake['detail_url'])

    def test_summary_limit_preserves_every_exported_chart_measurement(self):
        data = self.projection()
        data['wakes'] = [{**deepcopy(data['wakes'][0]), 'id': f'wake-{i}',
                          'context_delivery': {'delivered_request_chars': 20, 'rich_context_chars': 100,
                                               'request_compression_ratio': 0.2, 'unused_large_metadata': 'x' * 10000}}
                         for i in range(100)]
        data['evidence_quality'] = {'distinct_works': 40, 'reused_works': [1, 2],
                                    'notebooks': ['history' * 10000] * 100}
        with tempfile.TemporaryDirectory() as directory:
            overview = export_research_transport(data, directory)
            self.assertEqual(len(overview['wakes']), MAX_WAKE_SUMMARIES)
            self.assertEqual(len(overview['chart_wakes']), 100)
            self.assertEqual(overview['transport']['wake_trace_count'], 100)
            self.assertEqual(sum(attempt['elapsed_ms'] for row in overview['chart_wakes'] for attempt in row['attempts']), 120000)
            self.assertNotIn('unused_large_metadata', overview['chart_wakes'][0]['context_delivery'])
            self.assertNotIn('notebooks', overview['evidence_quality'])
            self.assertEqual(overview['evidence_quality']['reused_works_count'], 2)
            self.assertLessEqual((Path(directory) / 'research-overview.json').stat().st_size, MAX_OVERVIEW_BYTES)

    def test_missing_event_evidence_remains_missing_in_both_transports(self):
        data = self.projection()
        wake = data['wakes'][0]
        wake.update(context={'available': False, 'fields': [], 'request': {}, 'characters': None},
                    response=None, receipt={'available': False}, events=[])
        with tempfile.TemporaryDirectory() as directory:
            overview = export_research_transport(data, directory)
            row = overview['wakes'][0]
            self.assertFalse(row['context']['available'])
            self.assertFalse(row['receipt']['available'])
            self.assertNotIn('context_allocation', row)
            detail = json.loads((Path(directory) / row['detail_url']).read_text())['wake']
            self.assertIsNone(detail['response'])
            self.assertEqual(detail['events'], [])

    @unittest.skipUnless(shutil.which('node'), 'Node is required for browser transport contract')
    def test_browser_shares_overview_and_fetches_only_valid_selected_details(self):
        program = r"""
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const source=fs.readFileSync(process.argv[1],'utf8').split('// Expensive view objects')[0];
const key='research-details/'+ 'a'.repeat(64)+'.json';
const wake={id:'100::invocation',detail_url:key},projection={head:'h',version:1,projection_kind:'disposable-research-view',wakes:[wake]};
const calls=[],responses=new Map([['research-overview.json',projection],[key,{schema:1,projection_head:'h',projection_version:1,wake:{id:wake.id,response:'exact output'}}]]);
let unavailable=0;
const scope={window:{},AbortSignal,fetch:async url=>{calls.push(url);if(unavailable&&url==='research-overview.json')return {ok:false,status:unavailable};return {ok:true,json:async()=>responses.get(url),text:async()=> 'h'};}};
vm.runInNewContext(source,scope);
(async()=>{
 const api=scope.window.WakeViewData;
 const [one,two]=await Promise.all([api.research(),api.research()]);
 assert.equal(one,two);assert.deepEqual(calls,['research-overview.json']);
 const [detail,again]=await Promise.all([api.wake(one,wake),api.wake(one,wake)]);
 assert.equal(detail.response,'exact output');assert.equal(detail,again);assert.deepEqual(calls,['research-overview.json',key]);
 await assert.rejects(api.wake(one,{...wake,detail_url:'https://outside.example/detail.json'}),/Unsafe/);
 await assert.rejects(api.wake(one,{...wake,detail_url:'../private.json'}),/Unsafe/);
 // A failed overview on a new export must not trigger an enormous archive load.
 unavailable=503;scope.window={};vm.runInNewContext(source,scope);
 await assert.rejects(scope.window.WakeViewData.research(),/503/);
 assert(!calls.includes('research-data.json'));
 // Historical exports without the overview retain explicit 404 compatibility.
 unavailable=404;responses.set('research-data.json',projection);scope.window={};vm.runInNewContext(source,scope);
 assert.equal((await scope.window.WakeViewData.research()).head,'h');
 assert.equal(calls.at(-1),'research-data.json');
 // An immutable link carrying another snapshot is never shown as this wake.
 responses.set(key,{schema:1,wake:{id:'other-wake'}});
 await assert.rejects(scope.window.WakeViewData.wake(projection,wake),/does not match/);
})().catch(error=>{console.error(error);process.exitCode=1;});
"""
        subprocess.run(['node', '-e', program, str(ROOT / 'wake/assets/runtime-activity.js')], check=True)


if __name__ == '__main__':
    unittest.main()
