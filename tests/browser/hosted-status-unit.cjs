/* An expired recovery window must not promise an automatic restart forever. */
const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const source=fs.readFileSync('wake/assets/hosted-status.js','utf8');
const tick=()=>new Promise(resolve=>setImmediate(resolve));
(async()=>{
 for(const [age,state] of [[1,'waiting'],[16,'blocked']]){
  const light={dataset:{},setAttribute(k,v){this[k]=v;},removeAttribute(k){if(k==='data-state')delete this.dataset.state;}};
  const context={window:{WAKE_DEPLOYMENT:{hosted_status:{repository:'example/repo',workflow:'research-worker.yml',branch:'master'}},addEventListener(){}},
   document:{hidden:false,querySelector:()=>light,addEventListener(){}},navigator:{onLine:true},localStorage:{getItem:()=>null,setItem(){}},Date,JSON,AbortController,
   setTimeout:()=>0,clearTimeout(){},fetch:async url=>({ok:true,json:async()=>url.includes('/runs?')?{workflow_runs:[{path:'.github/workflows/research-worker.yml',head_branch:'master',status:'completed',conclusion:'failure',updated_at:new Date(Date.now()-age*60000).toISOString()}]}:{state:'active'}})};
  vm.runInNewContext(source,context);await tick();
  assert.equal(light.dataset.state,state);
  assert.match(light['aria-label'],new RegExp(state==='blocked'?'stalled; recovery needs attention':'Waiting for automatic recovery'));
 }

 // Disposable hosted workers stop after quota deferral; the research condition remains standby.
 {
  const callbacks={},light={dataset:{},setAttribute(k,v){this[k]=v;},removeAttribute(k){if(k==='data-state')delete this.dataset.state;}};
  const context={window:{WAKE_DEPLOYMENT:{hosted_status:{repository:'example/repo',workflow:'research-worker.yml',branch:'master'}},addEventListener(k,fn){callbacks[k]=fn;}},
   document:{hidden:false,querySelector:()=>light,addEventListener(){}},navigator:{onLine:true},localStorage:{getItem:()=>null,setItem(){}},Date,JSON,AbortController,
   setTimeout:()=>0,clearTimeout(){},fetch:async url=>({ok:true,json:async()=>url.includes('/runs?')?{workflow_runs:[{path:'.github/workflows/research-worker.yml',head_branch:'master',status:'completed',conclusion:'success'}]}:{state:'active'}})};
  vm.runInNewContext(source,context);await tick();
  const now=new Date().toISOString();
  const node=i=>({id:String(i),recorded_runtime:{state:'stopped',observed_at:now},research:{status:{latest:{status:'deferred',time:now,reason:'Gemini daily quotas exhausted; shared recovery scheduled'}}}});
  callbacks['wake-installation-snapshot']({detail:{live:false,hosted_execution:{research_start:{ok:true}},nodes:Array.from({length:12},(_,i)=>node(i))}});
  assert.equal(light.dataset.state,'standby','stopped workers with verified quota defer show purple');
  callbacks['wake-installation-snapshot']({detail:{live:false,hosted_execution:{research_start:{ok:false}},nodes:Array.from({length:12},(_,i)=>node(i))}});
  assert.notEqual(light.dataset.state,'standby','missing start acknowledgement cannot claim quota recovery');
 }
 // Green requires fresh running-node evidence belonging to the active batch.
 for(const [runId,nodeState,age,workflow,expected] of [
  ['55','running',0,'active','running'],
  ['54','running',0,'active',undefined],
  ['55','running',31,'active',undefined],
  ['55','standby',0,'active',undefined],
  ['55','running',0,'disabled_manually','stopped'],
 ]){
  const callbacks={},light={dataset:{},setAttribute(k,v){this[k]=v;},removeAttribute(k){if(k==='data-state')delete this.dataset.state;}};
  const context={window:{WAKE_DEPLOYMENT:{hosted_status:{repository:'example/repo',workflow:'research-worker.yml',branch:'master'}},addEventListener(k,fn){callbacks[k]=fn;}},
   document:{hidden:false,querySelector:()=>light,addEventListener(){}},navigator:{onLine:true},localStorage:{getItem:()=>context.saved||null,setItem(k,v){context.saved=v;}},Date,JSON,AbortController,
   setTimeout:()=>0,clearTimeout(){},fetch:async url=>({ok:true,json:async()=>url.includes('/runs?')?{workflow_runs:[{id:55,path:'.github/workflows/research-worker.yml',head_branch:'master',status:'in_progress'}]}:{state:workflow}})};
  vm.runInNewContext(source,context);await tick();
  assert.notEqual(light.dataset.state,'running','An Actions batch alone cannot establish node execution');
  callbacks['wake-installation-snapshot']({detail:{live:false,hosted_execution:{run_id:runId},nodes:Array.from({length:12},(_,i)=>({available:true,recorded_runtime:{state:i===0?nodeState:'standby',observed_at:new Date(Date.now()-age*60000).toISOString()}}))}});
  assert.equal(light.dataset.state,expected,`${runId}, ${nodeState}, ${age}, ${workflow}`);
  if(expected==='running')assert.match(light['aria-label'],/1 of 12 nodes recorded running/);
 }
 console.log('PASS: hosted recovery and quota-deferred stopped worker cases.');
})().catch(error=>{console.error(error);process.exitCode=1;});
