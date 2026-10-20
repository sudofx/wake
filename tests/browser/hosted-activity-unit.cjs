/* Exercise freshness and anonymous transport without a browser or model calls. */
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const source=fs.readFileSync('wake/assets/runtime-activity.js','utf8');
const tick=()=>new Promise(resolve=>setImmediate(resolve));
function environment(bound=true,node=true){
 const listeners={},requests=[],timers=[];
 const document={hidden:false,currentScript:{src:'https://sudofx.github.io/wake/nodes/100.wake/runtime-activity.js'},addEventListener:(k,v)=>{listeners[k]=v;}};
 const window={WAKE_DEPLOYMENT:{schema:1,mode:'standalone',snapshot_only:true,...(bound?{hosted_activity:{url:'https://wake-live-activity.coolgrove68.chatgpt.site/activity.json',installation_id:'installation'}}:{})},addEventListener:()=>{},dispatchEvent:()=>{}};window.parent=window;
 let response={schema:1,mode:'installation',installation_id:'installation',run_id:'123',source_revision:'a'.repeat(40),observed_at:new Date().toISOString(),members:[100,101,102,103,200,201,202,203,300,301,302,303].map(n=>({id:`${n}.wake`,runtime:{mode:'standalone',state:'running',activity_schema:1,capabilities:{live_activity:true},runtime_id:'worker-1',observed_at:new Date().toISOString(),activity:{stage:'provider',active:true,coordinate_id:'axis:1'}}}))};
 const globals={window,document,location:new URL(node?'https://sudofx.github.io/wake/nodes/100.wake/console.html':'https://sudofx.github.io/wake/console.html'),URL,Date,performance,AbortSignal,Event:class{},CustomEvent:class{},setInterval:()=>0,setTimeout:fn=>{timers.push(fn);return timers.length;},clearTimeout:()=>{},fetch:async(url,options)=>{requests.push({url:String(url),options});return {ok:true,json:async()=>response};}};
 vm.runInNewContext(source,globals);
 return {window,document,requests,timers,listeners,get response(){return response;},set response(v){response=v;}};
}
(async()=>{
 const ordinary=environment(false);await tick();assert.equal(ordinary.requests.length,0);
 const e=environment();await tick();assert.equal(e.requests.length,1);assert.equal(e.requests[0].options.credentials,'omit');assert.equal(e.requests[0].url,'https://wake-live-activity.coolgrove68.chatgpt.site/activity.json');
 assert.equal(e.window.WakeRuntimeActivity.activity.coordinate_id,'axis:1');
 e.response={...e.response,observed_at:'2000-01-01T00:00:00Z'};e.timers.shift()();await tick();assert.equal(e.window.WakeStatusSnapshot,null);assert.equal(e.window.WakeRuntimeActivity,null);
 e.document.hidden=true;e.listeners.visibilitychange();assert.equal(e.window.WakeStatusSnapshot,null);
 const root=environment(true,false);await tick();assert.equal(root.window.WakeRuntimeActivity,null);root.response={...root.response,coordinator:{active:{member:'100.wake',confirmed:true}}};root.timers.shift()();await tick();assert.equal(root.window.WakeRuntimeActivity.activity.stage,'provider');assert.equal(root.window.WakeRuntimeActivity.activity.coordinate_id,null,'unified view cannot animate another worker matrix');
 assert(e.requests.every(r=>!r.url.includes('/runtime.json')));
 console.log('PASS: explicit hosted activity, anonymous transport, stale/disconnected clearing; ordinary mirrors stay isolated.');
})().catch(e=>{console.error(e);process.exitCode=1;});
