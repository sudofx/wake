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
 console.log('PASS: recent failure waits; prolonged failure explicitly reports a stall.');
})().catch(error=>{console.error(error);process.exitCode=1;});
