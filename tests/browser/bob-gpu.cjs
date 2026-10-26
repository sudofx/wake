/* Cancellation must settle independently of a hung import/worker. */
const fs=require('node:fs'),os=require('node:os'),path=require('node:path'),assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url'),assets=path.resolve(__dirname,'../../wake/assets');
(async()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'wake-bob-gpu-contract-'));
 try{
  fs.writeFileSync(path.join(root,'package.json'),'{"type":"module"}');
  for(const name of ['ask-bob-gpu.js','ask-bob-context.js','ask-bob-guide.js'])fs.copyFileSync(path.join(assets,name),path.join(root,name));
  fs.writeFileSync(path.join(root,'ask-bob-gpu-engine.js'),`await new Promise(r=>setTimeout(r,40));export async function hasModelInCache(id,config){globalThis.__cacheConfig=config;if(globalThis.__cacheHang)await new Promise(()=>{});return globalThis.__cached===id;}export class WebWorkerMLCEngine{constructor(worker,config){this.worker=worker;config.initProgressCallback({text:'Preparing',progress:1});this.chat={completions:{create:async function*(){yield{choices:[{delta:{content:'<think>\\n\\n</think>\\n\\n'}}]};yield{choices:[{delta:{content:'A bounded answer. [S1]'},finish_reason:'stop'}]};}}};}async reload(){if(globalThis.__reload)await globalThis.__reload();}interruptGenerate(){}}`);
  let created=0,terminated=0;
  global.Worker=class{constructor(){created++;}terminate(){terminated++;}};
  const adapter={features:new Set(['shader-f16']),limits:{maxStorageBufferBindingSize:268435456}};
  Object.defineProperty(globalThis,'navigator',{configurable:true,value:{gpu:{requestAdapter:async()=>adapter}}});
  const gpu=await import(pathToFileURL(path.join(root,'ask-bob-gpu.js')));
  assert.equal(gpu.visibleReply(' \n<think>private'),'');assert.equal(gpu.visibleReply('<thi'),'');assert.equal(gpu.visibleReply('<think>private</think>\nHello'),'Hello');
  await assert.rejects(gpu.load('unknown'),/available models/);
  const cancel=new AbortController(),loading=gpu.load('best',()=>{},cancel.signal);setTimeout(()=>cancel.abort(),5);
  await assert.rejects(loading,e=>e.name==='AbortError');await new Promise(r=>setTimeout(r,70));assert.equal(created,0,'Cancelled import must not start a late worker');
  globalThis.__cacheHang=true;const cacheAbort=new AbortController(),cachePending=gpu.cached('best',cacheAbort.signal);setTimeout(()=>cacheAbort.abort(),5);await assert.rejects(cachePending,e=>e.name==='AbortError');globalThis.__cacheHang=false;
  globalThis.__cached=gpu.MODELS.capable.id;assert.equal(await gpu.cached('capable'),true);assert.equal(await gpu.cached('best'),false);assert.equal(globalThis.__cacheConfig.cacheBackend,'cache');assert.equal(created,0,'Cache checks must not start workers');await gpu.load('best');assert(gpu.ready());let streamed='';const answer=await gpu.generate([{role:'user',content:'Question'}],{onText:s=>streamed=s});assert.equal(answer.answer,'A bounded answer. [S1]');assert.equal(streamed,answer.answer);assert.equal(answer.complete,true);
  gpu.stop();assert(!gpu.ready());assert.equal(terminated,1);
  let release;globalThis.__reload=()=>new Promise(r=>release=r);const other=new AbortController(),pending=gpu.load('best',()=>{},other.signal);await new Promise(r=>setTimeout(r,5));other.abort();await assert.rejects(pending,e=>e.name==='AbortError');release();await new Promise(r=>setTimeout(r,5));assert(!gpu.ready(),'Cancelled worker must not be adopted after a late reload');assert.equal(terminated,2);
  const context=await import(pathToFileURL(path.join(root,'ask-bob-context.js'))),sources=[{id:'S1'},{id:'S2'}];
  assert.deepEqual(context.citedSources('Both [S1, S2].',sources),sources);assert.throws(()=>context.citedSources('Unknown [S1, S99]',sources),/not supplied/);
  console.log(JSON.stringify({result:'PASS',checks:'no late worker after cancelled import/reload, streamed prose without thinking, explicit model allowlist, grouped citation identity'}));
 }finally{fs.rmSync(root,{recursive:true,force:true});}
})().catch(error=>{console.error(error);process.exitCode=1;});
