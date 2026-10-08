"""Inspection telemetry cannot affect authority or invent active coordinates."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import threading
import unittest
import urllib.request
from functools import partial
from http.server import ThreadingHTTPServer

from wake.activity import RuntimeActivity
from wake.engine import DEFAULTS, Engine
from wake.providers import Fixture
from wake.record_store import RecordStore
from wake.standalone import Website
from wake.research_projection import build_research_projection

ROOT = Path(__file__).resolve().parents[1]


class RuntimeActivityTests(unittest.TestCase):
    def test_real_probe_reports_exact_coordinate_and_clears_after_receipt(self):
        with tempfile.TemporaryDirectory() as temp:
            store = RecordStore(temp, initialize_empty=True)
            engine = Engine(temp, dict(DEFAULTS), store=store)
            engine.initialize();store.enable_continuity_matrix()
            expected = store.continuity_matrix_progress()['next_coordinate_id']
            events=[]; activity=RuntimeActivity()
            def observe(**event):
                events.append(event);activity.update(**event)
            class InspectingFixture(Fixture):
                def propose(self, request):
                    current=activity.snapshot()['activity']
                    self_test.assertEqual(current['stage'], 'provider')
                    self_test.assertEqual(current['coordinate_id'], expected)
                    self_test.assertEqual(request['context']['continuity_probe']['campaign']['coordinate_id'], expected)
                    return super().propose(request)
            self_test=self
            result=engine.run(InspectingFixture(), activity=observe)
            self.assertEqual(result['status'], 'accepted')
            self.assertIn('continuity', [event['stage'] for event in events])
            self.assertEqual(events[-1], {'stage': 'idle'})
            self.assertIsNone(activity.snapshot()['activity']['coordinate_id'])
            self.assertFalse(activity.snapshot()['activity']['active'])
            self.assertEqual(store.continuity_matrix_progress()['completed_count'], 1)
            store.close()

    def test_observer_failure_does_not_change_governance(self):
        with tempfile.TemporaryDirectory() as temp:
            store=RecordStore(temp, initialize_empty=True)
            engine=Engine(temp, dict(DEFAULTS), store=store)
            def broken(**event):
                raise RuntimeError('Display unavailable')
            self.assertEqual(engine.run(Fixture(), activity=broken)['status'], 'accepted')
            self.assertEqual(store.load()['version'], 1)
            store.close()

    def test_failed_provider_clears_live_coordinate(self):
        with tempfile.TemporaryDirectory() as temp:
            store=RecordStore(temp, initialize_empty=True)
            engine=Engine(temp, dict(DEFAULTS), store=store)
            engine.initialize();store.enable_continuity_matrix()
            activity=RuntimeActivity()
            class FailedFixture(Fixture):
                def propose(self, request):
                    raise RuntimeError('provider failed')
            self.assertEqual(engine.run(FailedFixture(), activity=activity.update)['status'], 'failed')
            self.assertFalse(activity.snapshot()['activity']['active'])
            self.assertIsNone(activity.snapshot()['activity']['coordinate_id'])
            store.close()

    def test_export_contains_every_console_script_including_live_channel(self):
        import re
        from wake.report import export
        with tempfile.TemporaryDirectory() as temp:
            store=RecordStore(Path(temp)/'data', initialize_empty=True)
            engine=Engine(Path(temp)/'data', dict(DEFAULTS), store=store)
            engine.initialize()
            site=Path(temp)/'site';export(store, site)
            page=(site/'console.html').read_text()
            sources=re.findall(r'<script src="([^"?]+)',page)
            self.assertIn('runtime-activity.js', sources)
            for source in sources:
                self.assertTrue((site/source).is_file(), source)
            store.close()

    def test_runtime_endpoint_exposes_only_inspection_fields_and_fresh_samples(self):
        with tempfile.TemporaryDirectory() as temp:
            server=ThreadingHTTPServer(('127.0.0.1', 0), partial(Website, directory=temp))
            server.runtime_status={'mode':'standalone', 'state':'running'}
            server.activity=RuntimeActivity()
            server.snapshot_generation=1
            server.activity.update(stage='provider', invocation_id='invocation-public', coordinate_id='cell-public')
            thread=threading.Thread(target=server.serve_forever);thread.start()
            try:
                with urllib.request.urlopen(f'http://127.0.0.1:{server.server_port}/runtime.json') as response:
                    value=json.load(response)
                    self.assertIn('no-store', response.headers['Cache-Control'])
                self.assertTrue(value['capabilities']['live_activity'])
                self.assertEqual(value['activity']['coordinate_id'], 'cell-public')
                self.assertNotIn('request', value)
                self.assertNotIn('context', value)
                sample=server.activity.snapshot();sample['activity']['stage']='tampered'
                self.assertEqual(server.activity.snapshot()['activity']['stage'], 'provider')
            finally:
                server.shutdown();thread.join();server.server_close()

    def test_published_pending_probe_is_recorded_not_live(self):
        with tempfile.TemporaryDirectory() as temp:
            store=RecordStore(temp, initialize_empty=True)
            engine=Engine(temp, dict(DEFAULTS), store=store)
            engine.initialize();store.enable_continuity_matrix()
            invocation, request=engine.start('fixture','fixture',False)
            state=store.load()
            projection=build_research_projection(state, store.events(), store.head())
            recorded=projection['recorded_activity']
            self.assertEqual(recorded['invocation_id'], invocation)
            self.assertEqual(recorded['coordinate_id'], request['context']['continuity_probe']['campaign']['coordinate_id'])
            self.assertFalse(recorded['active'])
            engine.finish(invocation, Fixture().propose(request)[0])
            projection=build_research_projection(store.load(), store.events(), store.head())
            self.assertIsNone(projection['recorded_activity']['coordinate_id'])
            store.close()

    @unittest.skipUnless(shutil.which('node'), 'Node required for production browser code')
    def test_browser_polls_only_explicit_local_mode_and_clears_lost_activity(self):
        program=r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const source=fs.readFileSync(process.argv[1],'utf8');
(async()=>{
for(const mode of ['standalone','hosted',undefined]){
 let fail=false,requests=0,now=0;const intervals=[];
 const status={mode:'standalone',state:'running',activity_schema:1,runtime_id:'runtime',observed_at:'2026-10-08T18:00:00Z',capabilities:{live_activity:true},activity:{stage:'provider',active:true,coordinate_id:'real-cell'}};
 const window={WAKE_DEPLOYMENT:mode?{schema:1,mode}:undefined,dispatchEvent(){}};
 const context={window,document:{hidden:false,addEventListener(){}},performance:{now:()=>now},CustomEvent:class{},AbortController,
 setTimeout:()=>1,clearTimeout(){},setInterval:(fn,ms)=>intervals.push({fn,ms}),fetch:async()=>{requests++;if(fail)throw Error();return {ok:true,json:async()=>status};}};
 vm.runInNewContext(source,context);await new Promise(resolve=>setImmediate(resolve));
 assert.equal(requests,mode==='standalone'?1:0);
 if(mode==='standalone'){
  assert.equal(window.WakeRuntimeActivity.activity.coordinate_id,'real-cell');
  now=10000;intervals.find(x=>x.ms===1000).fn();assert.equal(window.WakeRuntimeActivity,null);
  fail=true;await intervals.find(x=>x.ms===3000).fn();assert.equal(window.WakeRuntimeActivity,null);
  assert.equal(window.WakeRuntimeActivityView({...status,state:'paused'}).activity.coordinate_id,null);
  assert.equal(window.WakeRuntimeActivityView({...status,capabilities:{}}),null);
  assert.equal(window.WakeRuntimeActivityView({...status,state:'invented'}),null);
 }
}
})().catch(error=>{console.error(error);process.exit(1)});
'''
        subprocess.run(['node','-e',program,str(ROOT/'wake/assets/runtime-activity.js')], check=True)

    @unittest.skipUnless(shutil.which('node'), 'Node required for canvas renderer execution')
    def test_cube_live_overlay_is_separate_from_selection_and_stops_on_clear(self):
        program=r'''
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const source=fs.readFileSync(process.argv[1],'utf8');
for(const reduced of [false,true]){
 let clock=0;const timers=new Map(),arcs=[];
 const ctx=new Proxy({arc:(x,y,r)=>arcs.push(r)}, {get:(obj,key)=>key in obj?obj[key]:(()=>{}),set:(obj,key,value)=>(obj[key]=value,true)});
 const canvas={clientWidth:640,clientHeight:380,dataset:{},getContext:()=>ctx,closest:()=>null,addEventListener(){}};
 const window={};let next=0;
 const context={window,document:{hidden:false,body:{},documentElement:{},getElementById:()=>null,addEventListener(){}},
 matchMedia:query=>({matches:query.includes('reduced-motion')&&reduced}),devicePixelRatio:1,
 performance:{now:()=>clock},getComputedStyle:()=>({getPropertyValue:()=> '#4bd59a'}),
 setTimeout:fn=>{timers.set(++next,fn);return next},clearTimeout:id=>timers.delete(id),
 requestAnimationFrame:()=>1,ResizeObserver:class{observe(){}},MutationObserver:class{observe(){}},
 IntersectionObserver:class{constructor(fn){this.fn=fn}observe(){this.fn([{isIntersecting:true}])}}};
 vm.runInNewContext(source,context);
 const cube=window.WakeResearchCube(canvas),matrix={axes:[{label:'Q',values:[1]},{label:'V',values:[1]},{label:'O',values:[1]}],cells:[{id:'active',ordinal:1,position:[3,3,3],score:.5,status:'completed'},{id:'selected',ordinal:2,position:[2,2,2],score:1,status:'completed'}]};
 cube.update(matrix);cube.select('selected');const original=JSON.stringify(matrix);
 cube.setActivity('active');assert.equal(canvas.dataset.liveCoordinate,'active');assert.equal(canvas.dataset.selected,'selected');
 assert(arcs.some(r=>r>=13&&r<=18));assert.equal(timers.size,reduced?0:1);
 assert.equal(JSON.stringify(matrix),original);cube.setActivity('unknown');assert.equal(canvas.dataset.liveCoordinate,'');assert.equal(timers.size,0);
 cube.setActivity('active');cube.setActivity('');assert.equal(timers.size,0);
}
'''
        subprocess.run(['node','-e',program,str(ROOT/'wake/assets/research-scene.js')], check=True)
