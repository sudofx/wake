/* Reader chat lifecycle, privacy and bounded history with offline generation. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets'),requests=[];
let browserMode=false,enabled=true,installation='fixture-installation',pending=null,longAnswer=false;
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');
 if(url.pathname==='/installation.json'){
  res.writeHead(browserMode?200:404,{'Content-Type':'application/json'});res.end(JSON.stringify({installation_id:installation}));return;
 }
 if(url.pathname==='/ask-bob-browser.js'){
  requests.push({browserRuntime:true});res.writeHead(200,{'Content-Type':'text/javascript'});
  res.end(`let loaded=false;export const ready=()=>loaded;export const cancelLoad=()=>{};
   export const load=async(progress,signal)=>{window.__loads=(window.__loads||0)+1;
    progress('download',{stage:'download',fraction:.4});
    if(window.__holdBrowserLoad)await new Promise(()=>{});
    if(signal?.aborted)throw signal.reason;loaded=true;progress('ready',{stage:'ready'});};
   export const answer=async(body,signal,progress)=>{window.__body=body;progress('drafting',{stage:'answer',characters:12});
    if(window.__holdBrowserAnswer)await new Promise((_,reject)=>signal.addEventListener('abort',()=>{loaded=false;reject(signal.reason);},{once:true}));
    return {ok:true,answer:'Browser-only answer [S1]',article:{id:body.article_id,hash:body.expected_article_hash,head:'h'.repeat(64)},citations:[{id:'S1',label:'Article',url:'blog.html'}],metrics:{condition:body.condition},warnings:[],missing:[]};};`);return;
 }
 if(url.pathname==='/ask-bob/capabilities'){
  requests.push({capability:true});res.writeHead(enabled?200:404,{'Content-Type':'application/json'});res.end(JSON.stringify({enabled,token:'fixture-token',installation_id:installation}));return;
 }
 if(url.pathname==='/ask-bob'){
  let raw='';req.on('data',chunk=>raw+=chunk);req.on('end',()=>{
   const body=JSON.parse(raw);requests.push(body);
   if(body.question==='busy'){res.writeHead(200,{'Content-Type':'application/json'});res.end(JSON.stringify({ok:false,error:'busy'}));return;}
   assert.equal(req.headers['x-wake-reader-token'],'fixture-token');
   const result={answer:longAnswer?'語'.repeat(6000):'<img src=x onerror="window.hostile=true"> A private answer.',citations:[{id:'safe',path:'/nodes/100.wake/evidence.html',label:'<script>source</script>'},{id:'bad',url:'javascript:window.hostile=true',title:'Bad'}],article:{id:body.article_id,hash:body.expected_article_hash,head:'h'.repeat(64)},missing:[],warnings:[]};
   const finish=()=>{res.writeHead(200,{'Content-Type':'application/json'});res.end(JSON.stringify(result));};
   if(body.question==='slow')pending=finish;else finish();
  });return;
 }
 if(url.pathname==='/ask-bob.js'||url.pathname==='/ask-bob.css'){
  res.writeHead(200,{'Content-Type':url.pathname.endsWith('.js')?'text/javascript':'text/css'});res.end(fs.readFileSync(path.join(assets,url.pathname.slice(1))));return;
 }
 res.writeHead(200,{'Content-Type':'text/html; charset=utf-8'});res.end('<!doctype html><meta name="viewport" content="width=device-width"><link rel="stylesheet" href="/ask-bob.css"><main id="article"></main><script src="/ask-bob.js"></script>');
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 const base=`http://127.0.0.1:${server.address().port}`;
 try{
  const page=await browser.newPage({viewport:{width:375,height:812}}),errors=[];page.on('pageerror',error=>errors.push(error.message));
  const mount=async(id,hash='a'.repeat(64))=>page.evaluate(async({id,hash})=>{
   document.querySelector('#article').replaceChildren();await window.WakeAskBob.mount(document.querySelector('#article'),{post:{id,_reader_article:{id,hash,head:'h'.repeat(64)}},head:'h'.repeat(64)});
  },{id,hash});
  const state=()=>page.evaluate(()=>{const key=Object.keys(localStorage).find(key=>key.startsWith('wake-ask-bob:'));return key?{value:JSON.parse(localStorage[key]),bytes:new TextEncoder().encode(localStorage[key]).length}:null;});
  const send=async text=>{await page.getByRole('textbox',{name:'Message Bob'}).fill(text);await page.getByRole('button',{name:'Send',exact:true}).click();};
  const done=()=>page.waitForFunction(()=>!document.querySelector('.ask-bob button[type=submit]').disabled);
  const ask=async text=>{await send(text);await done();};
  const clear=async()=>{await page.getByText('About this chat',{exact:true}).click();await page.getByRole('button',{name:'Clear chat',exact:true}).click();};
  enabled=true;await page.goto(base+'/blog.html');await page.evaluate(()=>window.WAKE_DEPLOYMENT={snapshot_only:true});const before=requests.length;await mount('missing-installation');assert.equal(await page.locator('.ask-bob').count(),0);assert.equal(requests.length,before);assert.equal(await state(),null);
  browserMode=true;await page.goto(base+'/blog.html');await page.evaluate(()=>window.WAKE_DEPLOYMENT={snapshot_only:true});const publicBefore=requests.length;await mount('public-article');
  assert.equal(requests.length,publicBefore,'Reading never starts model download');assert(await page.getByRole('textbox',{name:'Message Bob'}).isVisible());assert(!(await page.getByRole('button',{name:'Send',exact:true}).isDisabled()));
  assert.equal(await page.locator('.ask-bob select').count(),0);assert.equal(await page.getByRole('button',{name:/Load Bob/}).count(),0);
  await page.evaluate(()=>window.__holdBrowserLoad=true);await send('First question');
  await page.waitForFunction(()=>document.querySelector('.ask-bob progress').value===.4);
  assert.equal(await page.locator('.ask-bob-user p').innerText(),'First question');assert(await page.getByRole('button',{name:'Stop',exact:true}).isVisible());
  if(process.env.WAKE_BROWSER_ARTIFACT_DIR)await page.screenshot({path:path.join(process.env.WAKE_BROWSER_ARTIFACT_DIR,'chat-downloading-phone.png')});
  await page.getByRole('button',{name:'Stop',exact:true}).click();await done();assert((await page.locator('.ask-bob-status').innerText()).includes('Stopped'));assert.equal(await page.locator('.ask-bob-answer').count(),0);assert(await page.locator('.ask-bob-activity').isHidden());
  await page.evaluate(()=>window.__holdBrowserLoad=false);await page.getByRole('button',{name:'Retry',exact:true}).click();await done();assert.equal(await page.locator('.ask-bob-answer').innerText(),'Browser-only answer [S1]');
  await ask('A second question');assert.equal(await page.locator('.ask-bob-answer').count(),2);
  if(process.env.WAKE_BROWSER_ARTIFACT_DIR)await page.screenshot({path:path.join(process.env.WAKE_BROWSER_ARTIFACT_DIR,'chat-replies-phone.png')});assert.equal(await page.evaluate(()=>window.__body.condition),'C');assert.equal(await page.evaluate(()=>window.__body.history.length),1);
  await page.evaluate(()=>window.__holdBrowserAnswer=true);await send('Cancel this draft');await page.waitForFunction(()=>document.querySelector('.ask-bob-progress-line').textContent.includes('12 characters'));
  await page.getByRole('button',{name:'Stop',exact:true}).click();await done();assert.equal(await page.locator('.ask-bob-answer').count(),2);
  await page.evaluate(()=>window.__holdBrowserAnswer=false);await page.getByRole('button',{name:'Retry',exact:true}).click();await done();assert.equal(await page.locator('.ask-bob-answer').count(),3);
  // Safari can suspend timers. Resuming must enforce the original wall-clock
  // deadline even when a module/worker promise never settles or honors abort.
  await page.evaluate(()=>window.__holdBrowserLoad=true);await send('Timeout while preparing');
  await page.evaluate(()=>{window.__realNow=Date.now;Date.now=()=>window.__realNow()+600001;document.dispatchEvent(new Event('visibilitychange'));});
  await done();assert((await page.locator('.ask-bob-status').innerText()).includes('too long to prepare'));assert(await page.locator('.ask-bob-activity').isHidden());
  await page.evaluate(()=>{Date.now=window.__realNow;window.__holdBrowserLoad=false;});await page.getByRole('button',{name:'Retry',exact:true}).click();await done();
  assert.deepEqual(requests.slice(publicBefore),[{browserRuntime:true}],'No answer API in public browser mode');
  await page.evaluate(()=>localStorage.clear());browserMode=false;enabled=false;await page.goto(base+'/blog.html');await mount('p1');assert.equal(await page.locator('.ask-bob').count(),0);
  enabled=true;await page.goto(base+'/nodes/100.wake/blog.html');const nodeBefore=requests.length;await mount('p1');assert.equal(await page.locator('.ask-bob').count(),0);assert.equal(requests.length,nodeBefore);
  await page.goto(base+'/blog.html');await mount('p1');assert((await state()).value.articles[0].hash==='a'.repeat(64));
  await ask('busy');assert((await page.locator('.ask-bob-status').innerText()).includes('busy'));assert.equal((await state()).value.articles[0].turns.length,0);
  await ask('What is established?');assert.equal(requests.at(-1).condition,'C');assert.deepEqual(requests.at(-1).history,[]);
  assert.equal(await page.locator('.ask-bob-answer img').count(),0);assert.equal(await page.evaluate(()=>window.hostile),undefined);assert.equal(await page.locator('.ask-bob-conversation a').count(),1);assert((await page.locator('.ask-bob-answer').innerText()).includes('<img'));
  let saved=await state();assert.equal(saved.value.articles[0].self_report,null);assert.equal(saved.value.articles[0].turns[0].understanding,'unknown');
  await mount('p2');await ask('New article');assert.deepEqual(requests.at(-1).history,[],'No unrelated article chat sent');await ask('Follow-up');assert.equal(requests.at(-1).history.length,1);
  await mount('p2','b'.repeat(64));await ask('New article version');assert.equal(requests.at(-1).prior_article_hash,'a'.repeat(64));saved=await state();assert.equal(saved.value.articles.find(row=>row.id==='p2').versions[0].hash,'a'.repeat(64));
  await send('slow');while(!pending)await new Promise(resolve=>setTimeout(resolve,10));await page.evaluate(()=>location.hash='elsewhere');pending();pending=null;await page.waitForTimeout(60);assert(!(await state()).value.articles.flatMap(row=>row.turns).some(row=>row.question==='slow'));
  await mount('p3');await send('slow');while(!pending)await new Promise(resolve=>setTimeout(resolve,10));await clear();pending();pending=null;await done();assert.equal(await state(),null);await ask('Start over');assert.deepEqual(requests.at(-1).history,[]);
  longAnswer=true;for(let index=0;index<23;index++){await mount('bounded-'+index);await ask('Question '+index);}for(let index=0;index<12;index++)await ask('More '+index);
  saved=await state();assert(saved.bytes<=32768);assert(saved.value.articles.length<=20);assert(saved.value.articles.every(row=>row.turns.length<=10));
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));assert(await page.locator('.ask-bob-conversation').evaluate(node=>node.scrollHeight>node.clientHeight));
  installation='another-installation';await page.goto(base+'/blog.html');await mount('isolated');assert.equal(await page.locator('.ask-bob-turn').count(),0);
  await page.evaluate(()=>{const key=Object.keys(localStorage).find(key=>key.endsWith('another-installation'));localStorage.setItem(key,'{broken');});await page.goto(base+'/blog.html');await mount('after-corruption');await page.getByText('About this chat',{exact:true}).click();assert((await page.locator('.ask-bob-privacy').innerText()).includes('could not be read'));await ask('After missing context');assert.equal(await page.locator('.ask-bob-turn').count(),1);
  const blocked=await browser.newPage();blocked.on('pageerror',error=>errors.push(error.message));await blocked.goto(base+'/blog.html');await blocked.evaluate(async()=>{for(const key of ['getItem','setItem','removeItem'])Storage.prototype[key]=()=>{throw new DOMException('Blocked','SecurityError');};await window.WakeAskBob.mount(document.querySelector('#article'),{post:{id:'blocked',_reader_article:{hash:'a'.repeat(64),head:'h'.repeat(64)}}});});await blocked.getByRole('textbox',{name:'Message Bob'}).fill('In memory');await blocked.getByRole('button',{name:'Send',exact:true}).click();await blocked.locator('.ask-bob-answer').waitFor();await blocked.getByText('About this chat',{exact:true}).click();assert((await blocked.locator('.ask-bob-privacy').innerText()).includes('storage is unavailable'));await blocked.close();
  assert.deepEqual(errors,[]);console.log(JSON.stringify({result:'PASS',checks:'automatic first-send loading, real download progress, no selectors, stop and automatic retry, preparation deadline on resume despite ignored abort, same-article chat context, no public answer API, source URL/text safety, clear/navigation, bounded storage, phone width and scrolling'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
