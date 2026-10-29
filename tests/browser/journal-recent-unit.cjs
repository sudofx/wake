/* Recover recent cross-node journals using only one selected public snapshot. */
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync('wake/assets/reader-data.js','utf8');
const ids=[100,101,102,103,200,201,202,203,300,301,302,303].map(n=>n+'.wake');
(async()=>{
 for(const invalid of [null,'head','receipt','unavailable']){
  const calls=[],old={head:'unified',state:{version:297,invocations:{'303.wake::old':{id:'303.wake::old',time:'2026-10-28T10:00:00Z'}},journal:[{cycle:24,invocation:'303.wake::old',title:'Old final-node row'}]},events:[],reader_transport:{schema:1}};
  const manifest={schema:1,live:false,installation_id:'fixture',nodes:ids.map(id=>({id,research:{status:id==='100.wake'?{last_accepted:{id:'new',time:'2026-10-29T13:58:00Z'}}:{}}})),record_heads:Object.fromEntries(ids.map(id=>[id,{head:'a'.repeat(64),version:25}]))};
  const packet={head:invalid==='head'?'b'.repeat(64):'a'.repeat(64),collection:'journal',item:{cycle:1,invocation:'new',title:'New work on another node'},related:{invocations:{new:{id:'new',status:invalid==='receipt'?'rejected':'accepted',finished:'2026-10-29T13:58:00Z',provider:'fixture',request:'DO NOT COPY REQUEST'}}}};
  const original=structuredClone(old),window={WAKE_DEPLOYMENT:{unified:true,snapshot_only:true,public_data:{installation_id:'fixture'}}};
  const fetch=async path=>{calls.push(path);if(invalid==='unavailable'&&path.startsWith('nodes/'))throw Error('Unavailable');return {ok:true,json:async()=>structuredClone(path==='reader-data.json'?old:path==='installation.json'?manifest:packet)}};
  vm.runInNewContext(source,{window,fetch,AbortSignal,TextEncoder,Set,Map,Date,document:{},setTimeout:()=>{throw Error('Snapshot must not poll')}});
  const data=await window.WakeData;
  assert.equal(data.state.version,297);assert.deepEqual(old,original);
  assert.equal(data.state.journal.length,invalid?1:2);
  if(!invalid){
   assert.equal(data.state.journal.at(-1).invocation,'100.wake::new');
   assert.equal(data.state.journal.at(-1).origin.head,manifest.record_heads['100.wake'].head);
   assert.equal(data.state.invocations['100.wake::new'].request,undefined);
  }
  assert(calls.every(path=>!path.includes('wake-data.json')&&!path.startsWith('http')),'No full archive or alternate transport');
 }
 {
  let active=0,maximum=0,details=0;
  const manifest={schema:1,live:false,installation_id:'fixture',nodes:ids.map((id,i)=>({id,research:{status:{last_accepted:{id:'new-'+i,time:new Date(Date.UTC(2026,9,29,13,i)).toISOString()}}}})),record_heads:Object.fromEntries(ids.map(id=>[id,{head:'a'.repeat(64)}]))};
  const window={WAKE_DEPLOYMENT:{unified:true,snapshot_only:true,public_data:{installation_id:'fixture'}}};
  const fetch=async path=>{
   if(path==='reader-data.json')return {ok:true,json:async()=>({head:'unified',state:{version:297,journal:[],invocations:{}},events:[],reader_transport:{schema:1}})};
   if(path==='installation.json')return {ok:true,json:async()=>manifest};
   details++;maximum=Math.max(maximum,++active);await new Promise(setImmediate);active--;
   const node=path.split('/')[1],id='new-'+ids.indexOf(node);
   return {ok:true,json:async()=>({head:'a'.repeat(64),collection:'journal',item:{cycle:1,invocation:id},related:{invocations:{[id]:{id,status:'accepted',time:'2026-10-29T13:00:00Z'}}}})};
  };
  vm.runInNewContext(source,{window,fetch,AbortSignal,TextEncoder,Set,Map,Date,document:{},setTimeout:()=>{throw Error('Snapshot must not poll')}});
  await window.WakeData;assert.equal(details,8);assert.equal(maximum,3);
 }
 console.log('PASS: cross-node recency, snapshot identity, missing data, receipt validation and bounded projection');
})().catch(e=>{console.error(e);process.exitCode=1});
