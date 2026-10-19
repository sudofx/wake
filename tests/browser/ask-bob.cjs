/* Actual browser privacy, navigation and bounded-history tests with offline replies. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets'),requests=[];
let browserMode=false;
let enabled=true,installation='fixture-installation',pending=null,longAnswer=false;
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');
 if(url.pathname==='/installation.json'){
  res.writeHead(browserMode?200:404,{'Content-Type':'application/json'});res.end(JSON.stringify({installation_id:installation}));return;
 }
 if(url.pathname==='/ask-bob-browser.js'){
  requests.push({browserRuntime:true});res.writeHead(200,{'Content-Type':'text/javascript'});
  res.end(`let cancel,loaded=false;export const ready=()=>loaded;export const cancelLoad=()=>cancel?.();export const load=async progress=>{if(window.__holdBrowserLoad)await new Promise((_,reject)=>cancel=()=>reject(new DOMException('Bob loading cancelled.','AbortError')));loaded=true;progress('Fixture browser model ready');};export const answer=async(body,signal,progress)=>{progress?.('Fixture drafting progress');if(window.__holdBrowserAnswer)await new Promise((_,reject)=>signal.addEventListener('abort',()=>{loaded=false;reject(new DOMException('Answer cancelled','AbortError'));},{once:true}));return {ok:true,answer:'Browser-only answer [S1]',article:{id:body.article_id,hash:body.expected_article_hash,head:'h'.repeat(64)},citations:[{id:'S1',label:'Article',url:'blog.html'}],metrics:{condition:body.condition},warnings:[],missing:[]};};`);return;
 }

 if(url.pathname==='/ask-bob/capabilities'){
  requests.push({capability:true});res.writeHead(enabled?200:404,{'Content-Type':'application/json'});res.end(JSON.stringify({enabled,token:'fixture-token',installation_id:installation}));return;
 }
 if(url.pathname==='/ask-bob'){
  let raw='';req.on('data',chunk=>raw+=chunk);req.on('end',()=>{
   const body=JSON.parse(raw);requests.push(body);if(body.question==='busy'){res.writeHead(200,{'Content-Type':'application/json'});res.end(JSON.stringify({ok:false,error:'busy'}));return;}assert.equal(req.headers['x-wake-reader-token'],'fixture-token');
   const answer={answer:longAnswer?'語'.repeat(6000):'<img src=x onerror="window.hostile=true"> A private answer.',citations:[{id:'safe',path:'/nodes/100.wake/evidence.html',label:'<script>source</script>'},{id:'bad',url:'javascript:window.hostile=true',title:'Bad'}],article:{id:body.article_id,hash:body.expected_article_hash,head:'h'.repeat(64)},metrics:{condition:body.condition,source_records:1,context_bytes:100,output_bytes:60,latency_ms:4,provider_tokens:{totalTokenCount:22}},missing:[],warnings:[]};
   const finish=()=>{res.writeHead(200,{'Content-Type':'application/json'});res.end(JSON.stringify(answer));};
   if(body.question==='slow')pending=finish;else finish();
  });return;
 }
 if(url.pathname==='/ask-bob.js'||url.pathname==='/ask-bob.css'){
  res.writeHead(200,{'Content-Type':url.pathname.endsWith('.js')?'text/javascript':'text/css'});res.end(fs.readFileSync(path.join(assets,url.pathname.slice(1))));return;
 }
 res.writeHead(200,{'Content-Type':'text/html'});res.end('<!doctype html><meta name="viewport" content="width=device-width"><link rel="stylesheet" href="/ask-bob.css"><main id="article"></main><script src="/ask-bob.js"></script>');
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 const base=`http://127.0.0.1:${server.address().port}`;
 try{
  const page=await browser.newPage({viewport:{width:390,height:844}}),errors=[];page.on('pageerror',error=>errors.push(error.message));
  const mount=async (id,hash='a'.repeat(64),open=true)=>{await page.evaluate(async ({id,hash})=>{document.querySelector('#article').replaceChildren();await window.WakeAskBob.mount(document.querySelector('#article'),{post:{id,_reader_article:{id,hash,head:'h'.repeat(64)}},head:'h'.repeat(64)});},{id,hash});if(await page.locator('.ask-bob').count()){assert.equal(await page.locator('.ask-bob').getAttribute('open'),null);if(open)await page.locator('.ask-bob > summary').click();}};
  const state=()=>page.evaluate(()=>{const key=Object.keys(localStorage).find(key=>key.startsWith('wake-ask-bob:'));return key?{key,value:JSON.parse(localStorage[key]),bytes:new TextEncoder().encode(localStorage[key]).length}:null;});
  const ask=async (question,mode='C')=>{await page.getByRole('combobox',{name:'Conversation context'}).selectOption(mode);await page.getByRole('textbox',{name:'Your question'}).fill(question);await page.getByRole('button',{name:'Ask Bob',exact:true}).click();await page.waitForFunction(()=>!document.querySelector('.ask-bob button[type=submit]').disabled);};
  enabled=true;await page.goto(base+'/blog.html');await page.evaluate(()=>window.WAKE_DEPLOYMENT={snapshot_only:true});const snapshotRequests=requests.length;await mount('snapshot-only');assert.equal(await page.locator('.ask-bob').count(),0);assert.equal(requests.length,snapshotRequests);assert.equal(await state(),null);
  browserMode=true;await page.goto(base+'/blog.html');await page.evaluate(()=>window.WAKE_DEPLOYMENT={snapshot_only:true});
  const publicBefore=requests.length;await mount('public-article');assert.equal(await page.locator('.ask-bob').count(),1);
  assert.equal(requests.length,publicBefore);assert(await page.getByRole('button',{name:'Ask Bob',exact:true}).isDisabled());
  assert((await page.locator('.ask-bob-note').innerText()).includes('No sign-in or API key'));
  await page.evaluate(()=>window.__holdBrowserLoad=true);
  await page.getByRole('button',{name:'Load Bob on this device (491 MB)',exact:true}).click();
  await page.getByRole('button',{name:'Cancel loading',exact:true}).click();
  await page.waitForFunction(()=>document.querySelector('.ask-bob-status').textContent.includes('cancelled'));
  assert(await page.getByRole('button',{name:'Ask Bob',exact:true}).isDisabled());
  assert(!(await page.getByRole('button',{name:'Load Bob on this device (491 MB)',exact:true}).isDisabled()));
  await page.evaluate(()=>window.__holdBrowserLoad=false);
  await page.getByRole('button',{name:'Load Bob on this device (491 MB)',exact:true}).click();
  await page.waitForFunction(()=>!document.querySelector('.ask-bob button[type=submit]').disabled);
  await ask('Explain this article');assert.equal(await page.locator('.ask-bob-answer').innerText(),'Browser-only answer [S1]');
  await ask('A second question');assert.equal(await page.locator('.ask-bob-answer').count(),2);
  await page.evaluate(()=>window.__holdBrowserAnswer=true);
  await page.getByRole('textbox',{name:'Your question'}).fill('Cancel this draft');await page.getByRole('button',{name:'Ask Bob',exact:true}).click();
  await page.waitForFunction(()=>document.querySelector('.ask-bob-status').textContent==='Fixture drafting progress');
  await page.getByRole('button',{name:'Cancel answer',exact:true}).click();
  await page.waitForFunction(()=>document.querySelector('.ask-bob-status').textContent.includes('Answer cancelled'));
  assert.equal(await page.locator('.ask-bob-answer').count(),2);assert(await page.getByRole('button',{name:'Ask Bob',exact:true}).isDisabled());
  assert(await page.getByRole('button',{name:'Load Bob on this device (491 MB)',exact:true}).isVisible());
  await page.evaluate(()=>window.__holdBrowserAnswer=false);await page.getByRole('button',{name:'Load Bob on this device (491 MB)',exact:true}).click();
  await page.waitForFunction(()=>!document.querySelector('.ask-bob button[type=submit]').disabled);await ask('Retry after cancellation');assert.equal(await page.locator('.ask-bob-answer').count(),3);
  assert.deepEqual(requests.slice(publicBefore),[{browserRuntime:true}]);
  await page.evaluate(()=>localStorage.clear());browserMode=false;
  enabled=false;await page.goto(base+'/blog.html');await mount('p1');assert.equal(await page.locator('.ask-bob').count(),0);assert.equal(await state(),null);
  enabled=true;await page.goto(base+'/nodes/100.wake/blog.html');const before=requests.length;await mount('p1');assert.equal(await page.locator('.ask-bob').count(),0);assert.equal(requests.length,before);
  await page.goto(base+'/blog.html');await mount('p1','a'.repeat(64),false);assert(!(await page.getByRole('textbox',{name:'Your question'}).isVisible()));await page.locator('.ask-bob > summary').focus();await page.keyboard.press('Enter');assert(await page.getByRole('textbox',{name:'Your question'}).isVisible());await page.keyboard.press('Enter');assert(!(await page.getByRole('textbox',{name:'Your question'}).isVisible()));await page.keyboard.press('Enter');assert(!(await page.getByRole('combobox',{name:'Your understanding of this article version'}).isDisabled()));assert.equal((await state()).value.articles[0].hash,'a'.repeat(64));assert(!Number.isNaN(Date.parse((await state()).value.articles[0].encountered_at)));
  await ask('busy');assert((await page.locator('.ask-bob-status').innerText()).includes('busy'));assert.equal((await state()).value.articles[0].turns.length,0);await ask('What is established?','A');assert.equal(await page.getByText('Response details',{exact:true}).count(),1);assert.equal(requests.at(-1).history.length,0);assert.equal(requests.at(-1).previous_article,null);
  assert.equal(await page.locator('.ask-bob-answer img').count(),0);assert.equal(await page.evaluate(()=>window.hostile),undefined);assert.equal(await page.locator('.ask-bob-conversation a').count(),1);
  assert((await page.locator('.ask-bob-answer').innerText()).includes('<img'));
  await page.getByRole('combobox',{name:'Your understanding of this article version'}).selectOption('understood');
  let saved=await state();assert.equal(saved.value.articles[0].hash,'a'.repeat(64));assert.equal(saved.value.articles[0].self_report,'understood');assert.equal(saved.value.articles[0].turns[0].understanding,'unknown');
  await mount('p2');await ask('How does it relate?','B');let packet=requests.at(-1);assert.equal(packet.previous_article.id,'p2');assert.equal(packet.previous_article.hash,'a'.repeat(64));assert.equal(packet.previous_article.self_report,null);assert.equal(packet.expected_article_hash,'a'.repeat(64));assert.equal(packet.history[0].article_id,'p1');
  await ask('Explain uncertainty','C');assert.equal(requests.at(-1).condition,'C');assert(requests.at(-1).history.length>0);
  await page.getByRole('combobox',{name:'Your understanding of this article version'}).selectOption('unsure');await mount('p2','b'.repeat(64));await ask('New article version');assert.equal(requests.at(-1).prior_article_hash,'a'.repeat(64));saved=await state();assert.equal(saved.value.articles.find(row=>row.id==='p2').self_report,null);let versions=saved.value.articles.find(row=>row.id==='p2').versions;assert.equal(versions[0].hash,'a'.repeat(64));assert(!Number.isNaN(Date.parse(versions[0].encountered_at)));for(const letter of ['c','d','e','f'])await mount('p2',letter.repeat(64));versions=(await state()).value.articles.find(row=>row.id==='p2').versions;assert.deepEqual(versions.map(row=>row.hash),['c','d','e'].map(letter=>letter.repeat(64)));assert(versions.every(row=>!Number.isNaN(Date.parse(row.encountered_at))));
  // Navigation discards a late answer, even when the DOM container survives.
  await page.getByRole('textbox',{name:'Your question'}).fill('slow');await page.getByRole('button',{name:'Ask Bob',exact:true}).click();while(!pending)await new Promise(resolve=>setTimeout(resolve,10));
  await page.evaluate(()=>location.hash='elsewhere');pending();pending=null;await page.waitForTimeout(80);assert(!(await state()).value.articles.flatMap(row=>row.turns).some(row=>row.question==='slow'));
  await mount('p3');await page.getByRole('textbox',{name:'Your question'}).fill('slow');await page.getByRole('button',{name:'Ask Bob',exact:true}).click();while(!pending)await new Promise(resolve=>setTimeout(resolve,10));await page.getByRole('button',{name:'Clear private browser history'}).click();pending();pending=null;await page.waitForTimeout(80);assert.equal(await state(),null);
  // New interactions can resume after clear without restoring old article context.
  await ask('Start over','B');assert.equal(requests.at(-1).previous_article.id,'p3');assert.equal(requests.at(-1).previous_article.self_report,null);assert.deepEqual(requests.at(-1).history,[]);
  longAnswer=true;for(let index=0;index<23;index++){await mount('bounded-'+index);await ask('Question '+index);}
  for(let index=0;index<12;index++)await ask('More '+index);
  saved=await state();assert(saved.bytes<=32768);assert(saved.value.articles.length<=20);assert(saved.value.articles.every(row=>row.turns.length<=10));assert(!saved.value.articles.some(row=>row.id==='p1'));
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  installation='another-installation';await page.goto(base+'/blog.html');await mount('isolated');assert.equal(await page.locator('.ask-bob-turn').count(),0);assert.equal((await page.evaluate(()=>Object.keys(localStorage).filter(key=>key.startsWith('wake-ask-bob:')))).length,2);
  // Malformed persisted JSON reports the gap and starts a bounded new history.
  await page.evaluate(()=>{const key=Object.keys(localStorage).find(key=>key.endsWith('another-installation'));localStorage.setItem(key,'{broken');});
  await page.goto(base+'/blog.html');await mount('after-corruption');assert((await page.locator('.ask-bob-status').innerText()).includes('could not be read'));assert.equal((await page.locator('.ask-bob-turn').count()),0);await ask('After missing context');assert.equal((await page.locator('.ask-bob-turn').count()),1);
  // Denied browser storage still permits an explicit in-memory conversation.
  const blocked=await browser.newPage();blocked.on('pageerror',error=>errors.push(error.message));await blocked.goto(base+'/blog.html');
  await blocked.evaluate(async()=>{for(const key of ['getItem','setItem','removeItem'])Storage.prototype[key]=()=>{throw new DOMException('Blocked','SecurityError');};await window.WakeAskBob.mount(document.querySelector('#article'),{post:{id:'blocked',_reader_article:{hash:'a'.repeat(64),head:'h'.repeat(64)}}});});
  await blocked.locator('.ask-bob > summary').click();assert((await blocked.locator('.ask-bob-status').innerText()).includes('storage is unavailable'));await blocked.getByRole('textbox',{name:'Your question'}).fill('In memory');await blocked.getByRole('button',{name:'Ask Bob',exact:true}).click();await blocked.locator('.ask-bob-answer').waitFor();assert((await blocked.locator('.ask-bob-status').innerText()).includes('storage is unavailable'));await blocked.getByRole('button',{name:'Clear private browser history'}).click();assert.equal(await blocked.locator('.ask-bob-turn').count(),0);await blocked.close();
  assert.deepEqual(errors,[]);console.log(JSON.stringify({result:'PASS',checks:'public browser inference opt-in with no answer API, absent installation/capability, node exclusion, A/B/C context, explicit version-bound self-report, hostile text/source URL safety, stale navigation, clear during request, history byte/article/turn caps, installation isolation, phone layout, collapsed keyboard disclosure, dated version history, invalid JSON and unavailable storage'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
