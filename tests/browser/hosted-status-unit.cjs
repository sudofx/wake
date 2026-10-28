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
 console.log('PASS: hosted recovery and quota-deferred stopped worker cases.');
})().catch(error=>{console.error(error);process.exitCode=1;});
