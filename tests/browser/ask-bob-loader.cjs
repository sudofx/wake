/* Native startup may never settle; cancellation and retry must still terminate it. */
const assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {pathToFileURL}=require('node:url');
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
(async()=>{
 const temporary=fs.mkdtempSync(path.join(os.tmpdir(),'wake-browser-loader-'));
 try{
  const modulePath=path.join(temporary,'loader.mjs');fs.copyFileSync(path.join(__dirname,'../../wake/assets/ask-bob-browser.js'),modulePath);
  const {initialize,needsPrivateMemory}=await import(pathToFileURL(modulePath));
  const isolated=Object.getOwnPropertyDescriptor(globalThis,'crossOriginIsolated');
  try{
   Object.defineProperty(globalThis,'crossOriginIsolated',{value:false,configurable:true});assert(needsPrivateMemory());
   Object.defineProperty(globalThis,'crossOriginIsolated',{value:true,configurable:true});assert.equal(needsPrivateMemory(),typeof SharedArrayBuffer!=='function');
  }finally{if(isolated)Object.defineProperty(globalThis,'crossOriginIsolated',isolated);else delete globalThis.crossOriginIsolated;}
  const fake = spec => ({...spec,modelManager:{getModelOrDownload:async()=>({open:async()=>[]})},
   loadModel:async(_blobs,options)=>spec.loadModelFromUrl('fixture://model',options)});
  let exits=0,receivedSignal;
  const hung=fake({loadModelFromUrl:async(_url,options)=>{receivedSignal=options.signal;return new Promise(()=>{});},exit:async()=>{exits++;}});
  await assert.rejects(initialize(async()=>hung,'fixture://model',{stallMs:15}),/stopped after/);
  assert.equal(exits,1);assert(receivedSignal.aborted);
  const successful=fake({loadModelFromUrl:async(_url,options)=>{assert.equal(options.n_gpu_layers,0);assert.equal(options.n_batch,128);assert.equal(options.warmup,false);},exit:async()=>{throw Error('Successful startup must stay alive');}});
  assert.equal(await initialize(async()=>successful,'fixture://same-cached-model',{stallMs:20}),successful);
  const cancel=new AbortController();exits=0;
  const pending=initialize(async()=>hung,'fixture://model',{stallMs:100,signal:cancel.signal});
  await delay(1);cancel.abort();await assert.rejects(pending,error=>error.name==='AbortError');assert.equal(exits,1);
  // A late module import cannot start another worker after cancellation.
  let lateLoads=0;exits=0;
  await assert.rejects(initialize(async()=>{await delay(30);return {loadModelFromUrl:async()=>{lateLoads++;},exit:async()=>{exits++;}};},'fixture://model',{stallMs:10}),/stopped after/);
  await delay(35);assert.equal(lateLoads,0);assert.equal(exits,1);
  // A stuck engine repeating the same progress callback must still time out.
  let tick;
  const repeating=fake({loadModelFromUrl:async(_url,options)=>{tick=setInterval(()=>options.progressCallback({loaded:10,total:10}),2);return new Promise(()=>{});},exit:async()=>clearInterval(tick)});
  await assert.rejects(initialize(async()=>repeating,'fixture://model',{stallMs:15}),/stopped after/);
  let progress=[];
  const advancing=fake({loadModelFromUrl:async(_url,options)=>{for(let i=1;i<=4;i++){await delay(10);options.progressCallback({loaded:i,total:4});}},exit:async()=>{throw Error('Unexpected exit');}});
  assert.equal(await initialize(async()=>advancing,'fixture://model',{stallMs:25,progress:text=>progress.push(text)}),advancing);
  assert(progress.some(text=>text.includes('Opening downloaded')));
  // Slow but continuously advancing downloads still have an absolute limit.
  let advancingTick;
  const endlessDownload={modelManager:{getModelOrDownload:async(_model,options)=>{
    let loaded=0;advancingTick=setInterval(()=>options.progressCallback({loaded:++loaded,total:10000}),2);
    return new Promise(()=>{});
  }},exit:async()=>clearInterval(advancingTick)};
  await assert.rejects(initialize(async()=>endlessDownload,'fixture://slow',{timeoutMs:25,stallMs:100}),error=>error.name==='TimeoutError');
  const details=[];
  const downloadThenPrepare={modelManager:{getModelOrDownload:async(_model,options)=>{
    options.progressCallback({loaded:20,total:100});options.progressCallback({loaded:100,total:100});
    return {open:async()=>[]};
  }},loadModel:async()=>{},exit:async()=>{}};
  await initialize(async()=>downloadThenPrepare,'fixture://progress',{progress:(_text,detail)=>details.push(detail)});
  assert(details.some(detail=>detail.stage==='download'&&detail.fraction===.2));
  assert(details.some(detail=>detail.stage==='prepare'&&detail.fraction===1));
  // Worker.onerror can be logged without settling the native task promise.
  // It must reject immediately rather than wait for the stall deadline.
  exits=0;
  await assert.rejects(initialize(async({fail})=>fake({
   loadModelFromUrl:async()=>{setTimeout(()=>fail({message:'WebAssembly memory allocation failed'}),1);return new Promise(()=>{});},
   exit:async()=>{exits++;}
  }),'fixture://model',{stallMs:1000}),/Bob engine stopped: WebAssembly memory allocation failed/);
  assert.equal(exits,1);
  const failedCache={modelManager:{getModelOrDownload:async()=>({open:async()=>{throw new DOMException('Could not read saved file','NotReadableError');}})},exit:async()=>{}};
  await assert.rejects(initialize(async()=>failedCache,'fixture://cache',{stallMs:100}),/Bob failed while opening downloaded bob: Could not read saved file/);
  let nativeLoads=0;
  const stuckCache={modelManager:{getModelOrDownload:async()=>({open:async()=>new Promise(()=>{})})},
   loadModel:async()=>{nativeLoads++;},exit:async()=>{}};
  await assert.rejects(initialize(async()=>stuckCache,'fixture://cached-model',{stallMs:15}),/opening downloaded bob/);
  assert.equal(nativeLoads,0);
  console.log(JSON.stringify({result:'PASS',checks:'bounded startup, worker termination, retry without cache deletion, cancellation, late-factory cancellation, identical-progress stall, advancing-download progress'}));
 }finally{fs.rmSync(temporary,{recursive:true,force:true});}
})().catch(error=>{console.error(error);process.exitCode=1;});
