/* Automatic chat with controlled inference: no model choices or cache gate. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets'),requests=[];
const hash='a'.repeat(64),head='b'.repeat(64);
const guide={schema:1,head,article:{id:'story',hash,head},sources:[{id:'S1',label:'A bounded observation',url:'blog.html#blog/story',head,collection:'posts'}],passages:[{source:'S1',field:'lede',text:'The evaluation recorded twelve completed tasks. The historical notebook was unavailable; no memory benefit was established.',terms:['evaluation','recorded','twelve','completed','tasks','historical','notebook','unavailable','memory','benefit','established']}],omitted:[]};
const fake=`export const MODELS={starter:{},best:{},capable:{}};let loaded;export const current=()=>loaded;export const cached=async()=>{throw Error('Cache access denied fixture');};export const ready=()=>Boolean(loaded);export const stop=()=>{loaded=undefined;};function wait(signal,kind){return new Promise((resolve,reject)=>{window[kind]=resolve;signal?.addEventListener('abort',()=>reject(signal.reason),{once:true});});}export async function load(choice,report,signal){window.__loads??=[];window.__loads.push(choice);report('Preparing',{progress:.5});if(choice==='starter'&&window.__slowStartup)await wait(signal,'__openStarter');if(choice==='best'&&window.__upgradeFailure)throw Error('Upgrade memory failure fixture');if(signal.aborted)throw signal.reason;loaded=choice;}export async function prefetch(choice,signal){window.__prefetches=(window.__prefetches||0)+1;if(window.__networkFailure)throw Error('Network unavailable fixture');await wait(signal,'__finishPrefetch');}export async function generate(messages,{signal,onText}){window.__messages=messages;window.__answerModels??=[];window.__answerModels.push(loaded);if(messages.at(-1).content.endsWith('slow'))await wait(signal,'__finishReply');const answer=messages.at(-1).content.endsWith('uncited')?'Twelve tasks were completed.':'The evaluation recorded twelve tasks. [S1]';onText(answer);return{answer,complete:true,metrics:{latency_ms:42}};}`;
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');requests.push(url.pathname);
 if(url.pathname==='/installation.json'){res.setHeader('Content-Type','application/json');res.end(JSON.stringify({installation_id:'device-fixture'}));return;}
 if(url.pathname.includes('/reader-records/journal/')){res.setHeader('Content-Type','application/json');res.end(JSON.stringify({head,collection:'journal',item:{invocation:'100.wake::w-journal',cycle:7,title:'Exact node journal',summary:'A dated entry.',origin:{node:'100.wake'}}}));return;}
 if(url.pathname.includes('/reader-records/guides/')){res.setHeader('Content-Type','application/json');res.end(JSON.stringify(guide));return;}
 if(url.pathname==='/ask-bob-gpu.js'){res.setHeader('Content-Type','text/javascript');res.end(fake);return;}
 const file=path.join(assets,url.pathname);if(!file.startsWith(assets+path.sep)){res.writeHead(404);res.end();return;}
 fs.readFile(file,(e,data)=>{if(e){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':file.endsWith('.svg')?'image/svg+xml':'text/html');res.end(data);});
});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const base=`http://127.0.0.1:${server.address().port}`;
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const context=await browser.newContext({viewport:{width:390,height:844},hasTouch:true}),page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));
  await context.addInitScript(()=>{window.__slowStartup=true;});
  const url=base+`/bob-chat.html?article=story&hash=${hash}&theme=dark`;
  await page.goto(url);await page.waitForFunction(()=>window.__openStarter);
  assert.equal(await page.locator('select,#download,#setup,#change-model').count(),0);
  assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
  assert.equal(await page.locator('.avatar').evaluate(el=>el.tagName==='IMG'&&el.complete&&el.naturalWidth>0&&getComputedStyle(el).borderRadius==='50%'),true);
  await page.getByRole('textbox',{name:'Message Bob'}).fill('What is WAKE?');const start=Date.now();await page.getByRole('button',{name:'Send',exact:true}).click();
  await page.waitForFunction(()=>document.querySelector('.bob .prose')?.textContent.includes('lab notebook'));
  assert(Date.now()-start<1500,'Published introduction must work while inference is still loading');
  assert.equal(await page.locator('.bob summary').innerText(),'Published introduction');
  assert.equal(await page.evaluate(()=>window.__answerModels),undefined,'Immediate explanation must not wait for a model');
  await page.getByRole('textbox',{name:'Message Bob'}).fill('What happened?');await page.getByRole('button',{name:'Send',exact:true}).click();
  await page.evaluate(()=>{window.__slowStartup=false;window.__openStarter();});
  await page.waitForFunction(()=>document.querySelectorAll('.bob details').length===2&&!document.querySelector('#send').disabled);
  assert.deepEqual(await page.evaluate(()=>window.__loads),['starter']);assert.deepEqual(await page.evaluate(()=>window.__answerModels),['starter']);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  // Keep one compact engine across replies, with no background larger download.
  await page.getByRole('textbox',{name:'Message Bob'}).fill('slow');await page.getByRole('button',{name:'Send',exact:true}).click();await page.waitForFunction(()=>window.__finishReply);
  assert.equal(await page.evaluate(()=>window.__prefetches),undefined);
  await page.evaluate(()=>window.__finishReply());await page.waitForFunction(()=>!document.querySelector('#send').disabled);
  assert.deepEqual(await page.evaluate(()=>window.__loads),['starter']);
  await page.getByRole('textbox',{name:'Message Bob'}).fill('Why?');await page.getByRole('button',{name:'Send',exact:true}).click();await page.waitForFunction(()=>document.querySelectorAll('.bob details').length===4&&!document.querySelector('#send').disabled);
  assert.equal(await page.evaluate(()=>window.__answerModels.at(-1)),'starter');
  const messages=await page.evaluate(()=>window.__messages);assert.equal(messages.filter(m=>m.role==='assistant').length,3);assert(messages[0].content.includes('15-year-old'));assert(messages.at(-1).content.includes('historical notebook was unavailable'));
  const stored=await page.evaluate(()=>localStorage.getItem('wake-bob-device-chat:device-fixture'));assert.equal(JSON.parse(stored).story.turns.length,4);assert(Buffer.byteLength(stored)<=32768);
  // Restore labels and chat without waiting for preparation or checking cache.
  await page.reload();await page.waitForFunction(()=>document.querySelectorAll('.bob').length===4);assert.equal(await page.locator('.bob summary').first().innerText(),'Published introduction');
  await page.getByRole('button',{name:'Clear chat',exact:true}).click();assert.equal(await page.locator('article').count(),0);
  await page.getByRole('textbox',{name:'Message Bob'}).fill('Keep this question');await page.getByRole('button',{name:'Send',exact:true}).click();await page.getByRole('button',{name:'Stop',exact:true}).click();await page.waitForFunction(()=>!document.querySelector('#send').disabled);assert.equal(await page.locator('#question').inputValue(),'Keep this question');
  // Retrying an interrupted question reuses its pair of bubbles.
  const userCount=await page.locator('.you').count();
  await page.getByRole('button',{name:'Send',exact:true}).click();await page.getByRole('button',{name:'Stop',exact:true}).click();await page.waitForFunction(()=>!document.querySelector('#send').disabled);
  assert.equal(await page.locator('.you').count(),userCount);
  await page.evaluate(()=>localStorage.setItem('wake-bob-upgrade-opening',String(Date.now())));await page.reload();await page.waitForFunction(()=>window.__openStarter);await page.evaluate(()=>{window.__slowStartup=false;window.__openStarter();});await page.waitForTimeout(50);assert.equal(await page.evaluate(()=>window.__prefetches),undefined);
  await page.getByRole('textbox',{name:'Message Bob'}).fill('uncited');await page.getByRole('button',{name:'Send',exact:true}).click();await page.waitForFunction(()=>document.querySelector('.bob summary')?.textContent==='Sources Bob read');
  const journal=await page.evaluate(async({head})=>{const {prepareContext}=await import('./ask-bob-context.js');return prepareContext({collection:'journal',record:'100.wake::w-journal',head},'What changed?',[]);},{head});assert.equal(new URL(journal.sources[0].url).pathname,'/nodes/100.wake/index.html');
  await page.evaluate(({hash})=>localStorage.setItem('wake-bob-device-chat:device-fixture',JSON.stringify({other:null,bad:{time:'invalid',version:hash,turns:[]},kept:{time:1,version:hash,turns:[{question:'Earlier',answer:'Earlier answer',sources:[null,{id:'S1',label:'Hostile',url:'https://outside.invalid/'}]}]}})),{hash});
  await page.reload();await page.waitForFunction(()=>window.__openStarter);await page.evaluate(()=>{window.__slowStartup=false;window.__openStarter();});
  await page.locator('#question').fill('uncited');await page.locator('#send').click();await page.waitForFunction(()=>!document.querySelector('#send').disabled);
  const repaired=await page.evaluate(()=>JSON.parse(localStorage.getItem('wake-bob-device-chat:device-fixture')));assert.equal(repaired.other,undefined);assert.equal(repaired.bad,undefined);assert.equal(repaired.kept.turns[0].sources.length,0);
  await page.screenshot({path:'/tmp/wake-bob-automatic-phone.png'});
  // The actual launcher still opens the themed, version-bound popup.
  await page.goto(base+'/bob-chat.html');await page.evaluate(async()=>{window.WAKE_DEPLOYMENT={snapshot_only:true};const s=document.createElement('script');s.src='ask-bob.js';document.body.append(s);await new Promise(r=>s.onload=r);document.body.insertAdjacentHTML('beforeend','<div id="fixture"><h1>Story</h1></div>');await WakeAskBob.mount(document.querySelector('#fixture'),{post:{id:'story',_reader_article:{hash:'a'.repeat(64)}}});});
  const opened=page.waitForEvent('popup');await page.locator('.ask-bob-launch').click();const popup=await opened;assert.equal(new URL(popup.url()).pathname,'/bob-chat.html');assert.equal(new URL(popup.url()).searchParams.get('article'),'story');await popup.close();
  assert(!requests.some(p=>p.startsWith('/ask-bob/')));assert.deepEqual(errors,[]);
  console.log(JSON.stringify({result:'PASS',checks:'automatic start, no setup/model controls, immediate grounded introduction, queued first question, cache-denied path, single compact engine without upgrades, history continuity, retry bubble identity, cancellation, source labels, exact node citation, mobile layout'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
