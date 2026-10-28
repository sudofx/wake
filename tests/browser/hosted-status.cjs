/* Explicit hosted observation stays separate from research and expires safely. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const cases=[
   ['active','in_progress',null,null,'research state unconfirmed'],
   ['disabled_manually','in_progress',null,'stopped','draining'],
   ['active','queued',null,'waiting','queued'],
   ['active','completed','success','idle','Between hosted batches'],
   ['active','completed','failure','waiting','automatic recovery'],
   ['active','completed','action_required','blocked','requires attention'],
  ];
  for(const [workflow,status,conclusion,state,label] of cases){
   const page=await browser.newPage(),requests=[];let fail=false;
   await page.clock.install();
   await page.route('**/*',route=>{
    const url=new URL(route.request().url()),name=url.pathname.split('/').at(-1);
    if(url.hostname==='api.github.com'){
     requests.push(url.href);assert.equal(route.request().method(),'GET');assert(!route.request().headers().authorization);
     if(fail)return route.fulfill({status:403,json:{message:'Rate limited'}});
     return route.fulfill({json:name==='runs'?{workflow_runs:[{path:'.github/workflows/research-worker.yml',head_branch:'master',status,conclusion}]}:{state:workflow}});
    }
    if(name==='index.html')return route.fulfill({contentType:'text/html',body:`<html data-wake-snapshot-only="true" data-wake-hosted-status="true"><head><script>window.WAKE_DEPLOYMENT={snapshot_only:true,mode:'standalone',hosted_status:{repository:'example/repo',workflow:'research-worker.yml',branch:'master'}};</script><link rel="stylesheet" href="masthead.css"><script src="nav.js" defer></script><script src="hosted-status.js" defer></script></head><body><header class="masthead"><nav class="compact-nav"></nav><div class="header-tools"><a class="actions-light"><span class="actions-light-track"><i></i></span></a></div></header></body></html>`});
    if(['nav.js','hosted-status.js','masthead.css'].includes(name))return route.fulfill({contentType:name.endsWith('.css')?'text/css':'text/javascript',body:fs.readFileSync(path.join(assets,name),'utf8')});
    throw new Error('Unexpected research/runtime request: '+url.href);
   });
   await page.goto('https://wake.test/index.html');
   await page.waitForFunction(state=>document.querySelector('.actions-light').dataset.state===(state||undefined),state);
   const light=page.locator('.actions-light');assert.notEqual(await light.evaluate(e=>getComputedStyle(e).display),'none');
   assert.match(await light.getAttribute('aria-label'),new RegExp(label));assert.equal(requests.length,2);
   assert.equal(await light.getAttribute('href'),'https://github.com/example/repo/actions/workflows/research-worker.yml');
   if(status==='in_progress' && workflow==='active'){
    await page.reload();await page.waitForFunction(()=>document.querySelector('.actions-light').getAttribute('data-state')===null);assert.equal(requests.length,2,'navigation reuses bounded cache');
    await page.clock.fastForward(120000);assert.equal(requests.length,2);
    fail=true;await page.clock.fastForward(61000);await page.waitForFunction(()=>document.querySelector('.actions-light').getAttribute('aria-label').includes('Status unavailable'));
    assert.equal(await light.getAttribute('data-state'),null,'failed reads remain unconfirmed');assert.equal(requests.length,4);
    await page.reload();await page.waitForFunction(()=>document.querySelector('.actions-light').getAttribute('aria-label').includes('Status unavailable'));assert.equal(requests.length,4,'unavailable observations also back off across navigation');
   }
   await page.close();
  }
  console.log('PASS: hosted batch states, anonymous bounded polling, navigation cache and unavailable clearing; no research/runtime traffic.');
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
