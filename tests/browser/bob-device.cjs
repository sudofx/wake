/* Public popup lifecycle with a controlled inference boundary, never a model download. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets'),requests=[];
const hash='a'.repeat(64),head='b'.repeat(64);
const guide={schema:1,head,article:{id:'story',hash,head},sources:[{id:'S1',label:'A bounded observation',url:'blog.html#blog/story',head,collection:'posts'}],passages:[{source:'S1',field:'lede',text:'The evaluation recorded twelve completed tasks. The historical notebook was unavailable; no memory benefit was established.',terms:['evaluation','recorded','twelve','completed','tasks','historical','notebook','unavailable','memory','benefit','established']}],omitted:[]};
const fake=`export const MODELS={best:{},capable:{}};export const cached=async choice=>localStorage.getItem('cached:'+choice)==='yes';let loaded=false;export const ready=()=>loaded;export const supported=async()=>true;export const stop=()=>{loaded=false;};export async function load(choice,report,signal){window.__loads=(window.__loads||0)+1;report('Downloading',{progress:.5});await new Promise(r=>setTimeout(r,20));if(signal.aborted)throw signal.reason;loaded=true;localStorage.setItem('cached:'+choice,'yes');}export async function generate(messages,{signal,onText}){window.__messages=messages;let answer=messages.at(-1).content==='uncited'?'The evaluation recorded twelve tasks.':'The evaluation recorded twelve tasks. [S1]';if(messages.at(-1).content==='slow'){await new Promise((r,j)=>{const t=setTimeout(r,10000);signal.addEventListener('abort',()=>{clearTimeout(t);j(signal.reason);},{once:true});});}onText(answer);await new Promise(r=>setTimeout(r,20));return{answer,complete:true,metrics:{latency_ms:42,first_token_ms:10}};}`;
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');requests.push(url.pathname);
 if(url.pathname==='/installation.json'){res.setHeader('Content-Type','application/json');res.end(JSON.stringify({installation_id:'device-fixture'}));return;}
 if(url.pathname.includes('/reader-records/journal/')){res.setHeader('Content-Type','application/json');res.end(JSON.stringify({head,collection:'journal',item:{invocation:'100.wake::w-journal',cycle:7,title:'Exact node journal',summary:'A dated entry.',origin:{node:'100.wake'}}}));return;}
 if(url.pathname.includes('/reader-records/guides/')){res.setHeader('Content-Type','application/json');res.end(JSON.stringify(guide));return;}
 if(url.pathname==='/ask-bob-gpu.js'){res.setHeader('Content-Type','text/javascript');res.end(fake);return;}
 const file=path.join(assets,url.pathname);if(!file.startsWith(assets+path.sep)){res.writeHead(404);res.end();return;}
 fs.readFile(file,(e,data)=>{if(e){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':'text/html');res.end(data);});
});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const base=`http://127.0.0.1:${server.address().port}`;
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const context=await browser.newContext({viewport:{width:390,height:844},hasTouch:true}),page=await context.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(base+`/bob-chat.html?article=story&hash=${hash}&theme=dark`);await page.waitForFunction(()=>!document.querySelector('#send').disabled);
  assert.equal(await page.evaluate(()=>window.__loads),undefined,'Opening Bob must not download a model');
  assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
  await page.getByRole('textbox',{name:'Message Bob'}).fill('What happened?');await page.getByRole('button',{name:'Send',exact:true}).click();
  assert.equal(await page.locator('article').count(),0);assert((await page.locator('#status').innerText()).includes('Open Bob'));
  await page.getByRole('button',{name:'Download Bob',exact:true}).click();await page.waitForFunction(()=>document.querySelector('#setup').hidden);
  await page.getByRole('button',{name:'Send',exact:true}).click();await page.waitForFunction(()=>document.querySelectorAll('.bob details').length===1);
  assert((await page.locator('.bob').innerText()).includes('twelve'));assert.equal(await page.evaluate(()=>window.__loads),1);
  await page.getByRole('textbox',{name:'Message Bob'}).fill('Why?');await page.getByRole('button',{name:'Send',exact:true}).click();await page.waitForFunction(()=>document.querySelectorAll('.bob details').length===2);
  const messages=await page.evaluate(()=>window.__messages);assert.equal(messages.filter(m=>m.role==='assistant').length,1);assert(messages[0].content.includes('historical notebook was unavailable'));
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  const saved=await page.evaluate(()=>localStorage.getItem('wake-bob-device-chat:device-fixture'));assert(JSON.parse(saved).story.turns.length===2);assert(Buffer.byteLength(saved)<=32768);
  await page.reload();await page.waitForFunction(()=>document.querySelectorAll('.bob').length===2);await page.getByRole('button',{name:'Use saved Bob',exact:true}).waitFor();assert.equal(await page.evaluate(()=>window.__loads),undefined);
  await page.getByRole('button',{name:'Use source search without a model'}).click();await page.getByRole('textbox',{name:'Message Bob'}).fill('What is the main point?');await page.getByRole('button',{name:'Send',exact:true}).click();await page.waitForFunction(()=>document.querySelectorAll('.bob').length===3&&!document.querySelector('#send').disabled);
  assert.equal(await page.evaluate(()=>window.__loads),undefined,'Source search must not start an inference worker');
  await page.getByRole('button',{name:'Clear chat',exact:true}).click();assert.equal(await page.locator('article').count(),0);
  assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('wake-bob-device-chat:device-fixture')).story),undefined);
  // Valid JSON with malformed rows must not poison future saves or sources.
  await page.evaluate(({hash})=>localStorage.setItem('wake-bob-device-chat:device-fixture',JSON.stringify({other:null,bad:{time:'invalid',version:hash,turns:[]},kept:{time:1,version:hash,turns:[{question:'Earlier',answer:'Earlier answer',sources:[null,{id:'S1',label:'Hostile',url:'https://outside.invalid/'}]}]}})),{hash});
  await page.reload();await page.waitForFunction(()=>!document.querySelector('#send').disabled);
  await page.getByRole('button',{name:'Use saved Bob',exact:true}).click();await page.waitForFunction(()=>document.querySelector('#setup').hidden);
  await page.getByRole('textbox',{name:'Message Bob'}).fill('uncited');await page.getByRole('button',{name:'Send',exact:true}).click();await page.waitForFunction(()=>!document.querySelector('#send').disabled);
  assert.equal(await page.locator('.bob summary').innerText(),'Sources Bob read','Uncited source material is not presented as model citations');
  assert((await page.locator('#status').innerText()).startsWith('On device'));
  const repaired=await page.evaluate(()=>JSON.parse(localStorage.getItem('wake-bob-device-chat:device-fixture')));
  assert.equal(repaired.other,undefined);assert.equal(repaired.bad,undefined);assert.equal(repaired.kept.turns[0].sources.length,0);assert.equal(repaired.story.turns.length,1);
  await page.reload();await page.waitForFunction(()=>document.querySelectorAll('.bob').length===1);
  assert.equal(await page.locator('.bob summary').innerText(),'Sources Bob read','Uncited-source labeling survives restoration');
  // A unified journal selects exact invocation data, while cycle numbers repeat.
  const journal=await page.evaluate(async({head})=>{const {prepareContext}=await import('./ask-bob-context.js');return prepareContext({collection:'journal',record:'100.wake::w-journal',head},'What changed?',[]);},{head});
  assert.equal(new URL(journal.sources[0].url).pathname,'/nodes/100.wake/index.html');assert.equal(new URL(journal.sources[0].url).hash,'#journal/cycle%3A7');
  // Both selections survive reload; an evicted cache must not be reported saved.
  await page.evaluate(()=>{localStorage.setItem('wake-bob-device-model','capable');localStorage.setItem('cached:capable','yes');});
  await page.reload();await page.getByRole('button',{name:'Use saved Bob',exact:true}).waitFor();assert.equal(await page.locator('#model').inputValue(),'capable');assert.equal(await page.evaluate(()=>window.__loads),undefined);
  await page.evaluate(()=>localStorage.removeItem('cached:capable'));await page.reload();await page.getByRole('button',{name:'Download Bob',exact:true}).waitFor();assert.equal(await page.locator('#model').inputValue(),'capable');
  // Actual launcher can create a themed same-origin popup without any provider API.
  await page.goto(base+'/bob-chat.html');await page.evaluate(async()=>{window.WAKE_DEPLOYMENT={snapshot_only:true};const s=document.createElement('script');s.src='ask-bob.js';document.body.append(s);await new Promise(r=>s.onload=r);document.body.insertAdjacentHTML('beforeend','<div id="fixture"><h1>Story</h1></div>');await WakeAskBob.mount(document.querySelector('#fixture'),{post:{id:'story',_reader_article:{hash:'a'.repeat(64)}}});});
  const popupPromise=page.waitForEvent('popup');await page.locator('.ask-bob-launch').click();const popup=await popupPromise;assert(new URL(popup.url()).pathname==='/bob-chat.html');assert(new URL(popup.url()).searchParams.get('article')==='story');await popup.close();
  assert(!requests.some(p=>p.startsWith('/ask-bob/')),'No anonymous service or provider endpoint is used');assert.deepEqual(errors,[]);
  console.log(JSON.stringify({result:'PASS',checks:'explicit download, streaming UI, bounded same-context history, malformed-storage recovery, uncited-source labeling, exact node journal citation, source search, clear, theme, mobile width, same-origin popup, no provider service'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
