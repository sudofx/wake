/* Private-memory selection keeps the current native API and cache unchanged. */
const assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const temporary=fs.mkdtempSync(path.join(os.tmpdir(),'wake-bob-private-'));
 try{
  const modulePath=path.join(temporary,'adapter.mjs');fs.copyFileSync(path.join(__dirname,'../../wake/assets/ask-bob-private.js'),modulePath);
  const {privateEngine}=await import(pathToFileURL(modulePath));
  const manager={},config={logger:{}},nativeReply={choices:[{message:{content:'verified native reply'}}]};
  class Native {
   constructor(paths,options){assert.deepEqual(paths,{default:'owned-private.wasm'});assert.equal(options,config);this.modelManager=manager;}
   getWorkerResources(){throw Error('Default shared-memory resources must not be used');}
   async createChatCompletion(options){assert.equal(options,'native request');return nativeReply;}
  }
  const engine=privateEngine(Native,{wasm:'owned-private.wasm',worker:'owned-private.js'},config);
  assert(engine instanceof Native);assert.equal(engine.modelManager,manager);
  assert.deepEqual(engine.getWorkerResources(),{wasmPath:'owned-private.wasm',jsPath:'owned-private.js',compat:true,noWebGPU:true});
  // No protocol, tokenizer, grammar, cache-key or cancellation translation.
  assert.equal(await engine.createChatCompletion('native request'),nativeReply);
  console.log(JSON.stringify({result:'PASS',checks:'private wasm32 worker resources, CPU-only ABI, unchanged native completion API and model manager'}));
 }finally{fs.rmSync(temporary,{recursive:true,force:true});}
})().catch(error=>{console.error(error);process.exitCode=1;});
