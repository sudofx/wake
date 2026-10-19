/* Public-only context contract, independent of browser inference and all providers. */
const assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const temporary=fs.mkdtempSync(path.join(os.tmpdir(),'wake-browser-context-'));
 try{
  const modulePath=path.join(temporary,'context.mjs');fs.copyFileSync(path.join(__dirname,'../../wake/assets/ask-bob-browser.js'),modulePath);
  const {prepare,validateReply}=await import(pathToFileURL(modulePath));
  const request={article_id:'100.wake::article',question:'What is known?',condition:'A',expected_article_hash:'a'.repeat(64),history:[]};
  let reads=[];
  const read=async(collection,id)=>{reads.push([collection,id]);return {bytes:100,path:'reader-records/'+collection+'/exact.json',packet:{head:'snapshot',collection,item:{id,title:'Recorded claim',body:'A reported possibility, not an established finding.',evidence:collection==='posts'?['e1','missing','unused']:[]},article:{id,hash:'a'.repeat(64),head:'snapshot'}}};};
  const answer=await prepare(request,read);assert.equal(answer.article.hash,request.expected_article_hash);assert.equal(answer.sources[0].record_id,request.article_id);assert.equal(answer.sources.length,3);assert.equal(answer.metrics.history_selected_turns,0);assert.equal(reads.length,3);assert(answer.warnings.some(w=>w.includes('Additional linked')));
  assert(answer.system.includes('not established scientific truth'));assert(answer.system.includes('untrusted data'));
  const history=[{id:'older',article_id:request.article_id,article_hash:'b'.repeat(64),question:'Earlier?',answer:'x'.repeat(10000)}, {id:'other',article_id:'another',question:'Other article?',answer:'Unrelated'}];
  const compact=await prepare({...request,condition:'C',history,prior_article_hash:'b'.repeat(64)},read);
  const value=JSON.parse(compact.prompt);assert.equal(value.history.length,1);assert.equal(value.history[0].answer.length,700);assert.equal(value.history[0].article_hash,'b'.repeat(64));assert(value.version_note.includes('prior text is unavailable'));assert(compact.metrics.context_bytes<=15000);
  const wrong=async(collection,id)=>{const loaded=await read(collection,id);loaded.packet.article.hash='b'.repeat(64);return loaded;};
  await assert.rejects(prepare(request,wrong),/changed/);
  const foreign=async(collection,id)=>{const loaded=await read(collection,id);if(collection!=='posts')loaded.packet.head='foreign';return loaded;};
  const missing=await prepare(request,foreign);assert.equal(missing.sources.length,1);assert.equal(missing.missing.length,2);
  const before=reads.length;await assert.rejects(prepare({...request,question:'x'.repeat(2001)},read));assert.equal(reads.length,before);
  const huge=async(collection,id)=>{const loaded=await read(collection,id);loaded.packet.item.body='語'.repeat(100000);return loaded;};
  const bounded=await prepare(request,huge);assert(bounded.metrics.context_bytes<=15000);assert(bounded.warnings.some(w=>w.includes('excerpted')));
  const reply=(content,finish_reason='stop')=>({choices:[{message:{content},finish_reason}]});
  const complete=JSON.stringify({answer:'The article reports a possibility [S1].',citations:['S1']});
  const accepted=validateReply(reply(complete),answer.sources);assert.equal(accepted.citations[0].record_id,request.article_id);
  assert.throws(()=>validateReply(reply('{"answer":"unfinished','length'),answer.sources),/reply limit before finishing/);
  assert.throws(()=>validateReply(reply(complete,'length'),answer.sources),/reply limit before finishing/);
  assert.throws(()=>validateReply(reply('{"answer":"unfinished'),answer.sources),/readable answer/);
  assert.throws(()=>validateReply(reply(JSON.stringify({answer:'Unsupported [S99].',citations:['S99']})),answer.sources),/valid source references/);
  assert.throws(()=>validateReply(reply(JSON.stringify({answer:'Unsupported [S99].',citations:['S1']})),answer.sources),/valid source references/);
  console.log(JSON.stringify({result:'PASS',checks:'same-publication source identity, article hash, source/head rejection, bounded exact-ID retrieval, bounded A/B/C history, explicit uncertainty and excerpt notices, invalid-input-before-read'}));
 }finally{fs.rmSync(temporary,{recursive:true,force:true});}
})().catch(error=>{console.error(error);process.exitCode=1;});
