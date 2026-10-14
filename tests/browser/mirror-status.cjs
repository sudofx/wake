/* Public mirrors have no execution light or status traffic, including hosted mode. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  for(const mode of ['standalone','hosted','before-paint']){
   const page=await browser.newPage(),requests=[];
   await page.clock.install();
   await page.route('**/*',route=>{const name=new URL(route.request().url()).pathname.split('/').at(-1);requests.push(name);
    if(name==='index.html'){route.fulfill({contentType:'text/html',body:`<!doctype html><html><head><script>window.WAKE_DEPLOYMENT={schema:1,mode:'${mode}',snapshot_only:true};document.documentElement.dataset.wakeSnapshotOnly='true';</script><link rel="stylesheet" href="masthead.css">${mode==='before-paint'?'':'<script src="nav.js" defer></script>'}</head><body><header class="masthead"><div class="brand-lockup">wake</div><nav class="compact-nav"></nav><div class="header-tools"><a class="actions-light" href="/runtime.json"><span class="actions-light-track"><i></i></span></a><label class="theme-switch"></label></div></header><main>Last uploaded data</main></body></html>`});return;}
    if(['masthead.css','nav.js'].includes(name)){route.fulfill({contentType:name.endsWith('.css')?'text/css':'text/javascript',body:fs.readFileSync(path.join(assets,name),'utf8')});return;}
    route.abort();
   });
   await page.goto('http://wake.test/index.html');assert.equal(await page.locator('.actions-light').evaluate(e=>getComputedStyle(e).display),'none');if(mode!=='before-paint')assert.equal(await page.locator('.actions-light').getAttribute('hidden'),'');
   await page.clock.fastForward(65000);await new Promise(resolve=>setTimeout(resolve,50));assert.deepEqual(requests.filter(name=>name!=='index.html'&&name!=='masthead.css'&&name!=='nav.js'),[]);await page.close();
  }
  const local=await browser.newPage(),requests=[];
  await local.route('**/*',route=>{const name=new URL(route.request().url()).pathname.split('/').at(-1);requests.push(name);if(name==='index.html'){route.fulfill({contentType:'text/html',body:'<html><head><script>window.WAKE_DEPLOYMENT={schema:1,mode:"standalone",snapshot_only:false};</script><link rel="stylesheet" href="masthead.css"><script src="nav.js" defer></script></head><body><header class="masthead"><nav class="compact-nav"></nav><div class="header-tools"><a class="actions-light"><span class="actions-light-track"><i></i></span></a></div></header></body></html>'});return;}if(name==='runtime.json'){route.fulfill({json:{state:'paused'}});return;}if(['masthead.css','nav.js'].includes(name)){route.fulfill({contentType:name.endsWith('.css')?'text/css':'text/javascript',body:fs.readFileSync(path.join(assets,name),'utf8')});return;}route.abort();});
  await local.goto('http://wake.test/index.html');await local.waitForFunction(()=>document.querySelector('.actions-light').dataset.state==='stopped');assert.notEqual(await local.locator('.actions-light').evaluate(e=>getComputedStyle(e).display),'none');assert(requests.includes('runtime.json'));await local.close();
  const processPage=await browser.newPage(),processErrors=[];processPage.on('pageerror',error=>processErrors.push(error.message));
  await processPage.route('**/*',route=>{const name=new URL(route.request().url()).pathname.split('/').at(-1);if(name==='index.html'){route.fulfill({contentType:'text/html',body:'<html><head><script>window.WAKE_DEPLOYMENT={schema:1,mode:"standalone",snapshot_only:true};</script><script src="process-field.js" defer></script></head><body><section class="process-field-panel"><canvas id="process-field-canvas" width="600" height="300"></canvas><div id="process-field-stages"></div><span id="process-field-status"></span><span id="process-field-trace"></span><p id="process-field-detail"></p><p id="process-field-selection"></p></section></body></html>'});return;}if(name==='process-field.js'){route.fulfill({contentType:'text/javascript',body:fs.readFileSync(path.join(assets,name),'utf8')});return;}if(name==='research-data.json'){route.fulfill({json:{projection_kind:'disposable-research-view',version:3,graph:{nodes:[],edges:[]},wakes:[]}});return;}route.abort();});
  await processPage.goto('http://wake.test/index.html');await processPage.waitForFunction(()=>document.querySelector('#process-field-status').textContent==='PUBLIC SNAPSHOT');assert.match(await processPage.locator('#process-field-detail').innerText(),/no current execution or live activity/);assert.deepEqual(processErrors,[]);await processPage.close();
  console.log('PASS: standalone and hosted mirrors hide execution light and send no runtime/GitHub status requests; local status remains visible and reads local runtime.');
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
