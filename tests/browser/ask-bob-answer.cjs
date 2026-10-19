/* A dead native worker must not hold the reader UI or the next question hostage. */
const assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {pathToFileURL}=require('node:url');
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
(async()=>{
 const directory=fs.mkdtempSync(path.join(os.tmpdir(),'wake-bob-answer-'));
 try{
  const file=path.join(directory,'answer.mjs');fs.copyFileSync(path.join(__dirname,'../../wake/assets/ask-bob-browser.js'),file);
  const {generateReply,validateReply}=await import(pathToFileURL(file));
  let exits=0,discards=0,nativeSignal;
  const hung={createChatCompletion:options=>{nativeSignal=options.abortSignal;return new Promise(()=>{});},exit:()=>{exits++;return new Promise(()=>{});}};
  await assert.rejects(generateReply(hung,{}, {timeoutMs:20,stallMs:100,discard:()=>discards++}),error=>error.name==='TimeoutError');
  assert.equal(exits,1);assert.equal(discards,1);assert(nativeSignal.aborted);
  const cancel=new AbortController();exits=0;
  const pending=generateReply(hung,{}, {signal:cancel.signal,timeoutMs:1000,stallMs:1000});
  cancel.abort();await assert.rejects(pending,error=>error.name==='AbortError');assert.equal(exits,1);
  await assert.rejects(generateReply(hung,{}, {signal:cancel.signal}),error=>error.name==='AbortError');
  let timer;
  const repeating={createChatCompletion:options=>{timer=setInterval(()=>options.onData({prompt_progress:{processed:10},choices:[]}),2);return new Promise(()=>{});},exit:async()=>clearInterval(timer)};
  await assert.rejects(generateReply(repeating,{}, {timeoutMs:500,stallMs:15}),/without progress/);
  const sources=[{id:'S1',record_id:'article'}],progress=[];
  let calls=0;
  const usable={createChatCompletion:async options=>{
   calls++;assert(options.stream);assert(options.return_progress);assert.equal(options.max_tokens,420);
   options.onData({prompt_progress:{processed:1},choices:[]});
   for(const content of ['{"answer":','"Recorded claim [S1].",','"citations":["S1"]}']){
    await delay(8);options.onData({choices:[{delta:{content},finish_reason:null}]});
   }
   options.onData({choices:[{delta:{},finish_reason:'stop'}]});
  },exit:async()=>{throw Error('A completed reply must keep the loaded model');}};
  for(let index=0;index<2;index++){
   const response=await generateReply(usable,{max_tokens:420},{timeoutMs:1000,stallMs:30,progress:value=>progress.push(value)});
   assert.equal(validateReply(response,sources).citations[0].record_id,'article');
  }
  assert.equal(calls,2);assert(progress.some(value=>value.includes('characters generated')));
  let late,lateReports=0;
  const lateCancel=new AbortController();
  const lateWorker={createChatCompletion:options=>{late=options.onData;return new Promise(()=>{});},exit:async()=>{}};
  const latePromise=generateReply(lateWorker,{}, {signal:lateCancel.signal,progress:()=>lateReports++});
  lateCancel.abort();await assert.rejects(latePromise,error=>error.name==='AbortError');const before=lateReports;
  late({choices:[{delta:{content:'Late unvalidated draft'},finish_reason:'stop'}]});assert.equal(lateReports,before);
  // Safari may suspend timers while backgrounded. Returning to the page must
  // enforce the wall-clock deadline without waiting for a suspended timer.
  const add=globalThis.addEventListener,remove=globalThis.removeEventListener,clock=Date.now,events=new Map();let now=0;
  try{
   globalThis.addEventListener=(type,handler)=>events.set(type,handler);globalThis.removeEventListener=type=>events.delete(type);Date.now=()=>now;
   const resumed=generateReply(hung,{}, {timeoutMs:1000,stallMs:1000});now=1001;events.get('pageshow')();
   await assert.rejects(resumed,error=>error.name==='TimeoutError');assert.equal(events.size,0);
  }finally{Date.now=clock;if(add)globalThis.addEventListener=add;else delete globalThis.addEventListener;if(remove)globalThis.removeEventListener=remove;else delete globalThis.removeEventListener;}
  console.log(JSON.stringify({result:'PASS',checks:'hard deadline and cancellation despite unresponsive native exit, progress stall, two replies per model, late draft rejection, deadline on Safari resume'}));
 }finally{fs.rmSync(directory,{recursive:true,force:true});}
})().catch(error=>{console.error(error);process.exitCode=1;});
