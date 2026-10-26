/* Real browser transport across separate interface and immutable data versions. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const script=fs.readFileSync(path.resolve(__dirname,'../../wake/assets/public-data.js'));
const binding={schema:1,snapshot_only:true,public_data:{repository:'example/wake',branch:'wake-public',installation_id:'fixture',prefix:''}};
const server=http.createServer((req,res)=>{
 if(req.url.startsWith('/wake/public-data.js')){res.setHeader('Content-Type','text/javascript');res.end(script);return;}
 if(req.url.startsWith('/wake/reader-data.json')){res.setHeader('Content-Type','application/json');res.end('{"version":"bundled"}');return;}
 res.setHeader('Content-Type','text/html');res.end('<!doctype html><head><script>window.WAKE_DEPLOYMENT='+JSON.stringify(binding)+'</script><script src="/wake/public-data.js"></script></head><body><main>Unchanged interface</main></body>');
});
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const base=`http://127.0.0.1:${server.address().port}/wake/`,browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const context=await browser.newContext(),page=await context.newPage(),seen=[];let latest='a'.repeat(40),failDiscovery=false,wrongIdentity=false;
  await context.route('https://api.github.com/**',route=>{if(failDiscovery==='slow')return;seen.push(route.request().url());return route.fulfill({status:failDiscovery?403:200,json:{object:{sha:latest,type:'commit'}}});});
  await context.route('https://raw.githubusercontent.com/**',route=>{
   const url=new URL(route.request().url());seen.push(url.href);
   if(url.pathname.endsWith('/installation.json'))return route.fulfill({json:{schema:1,installation_id:wrongIdentity?'other':'fixture',live:false,nodes:Array(12).fill({}),record_heads:Object.fromEntries(Array.from({length:12},(_,i)=>[i,{}]))}});
   if(url.pathname.endsWith('/research-data.json'))return route.fulfill({status:404,body:'missing'});
   return route.fulfill({json:{version:url.pathname.split('/')[3]}});
  });
  await page.goto(base);await page.evaluate(()=>WakePublicData.ready);
  const read=()=>page.evaluate(async()=>{const r=await WakePublicData.fetch('reader-data.json');return r.json();});
  assert.equal((await read()).version,'a'.repeat(40));
  latest='b'.repeat(40);assert.equal((await read()).version,'a'.repeat(40),'A document must never mix public commits');
  const timestamp=await page.evaluate(()=>JSON.parse(localStorage.getItem('wake-public-snapshot:example/wake:fixture')).time);
  const discovery=seen.filter(s=>s.includes('api.github.com')).length;
  await page.reload();await page.evaluate(()=>WakePublicData.ready);assert.equal((await read()).version,'a'.repeat(40));
  assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('wake-public-snapshot:example/wake:fixture')).time),timestamp,'Navigating must not extend the discovery TTL');
  assert.equal(seen.filter(s=>s.includes('api.github.com')).length,discovery,'Reopening within cache TTL must not consume another API request');
  await page.evaluate(()=>localStorage.clear());await page.reload();await page.evaluate(()=>WakePublicData.ready);
  assert.equal((await read()).version,'b'.repeat(40),'New data must load without changing the interface');
  await page.evaluate(()=>{const a=document.createElement('a');a.id='download';a.href='installation.json';a.textContent='Download';document.body.append(a);});await page.waitForFunction(()=>document.querySelector('#download').href.startsWith('https://raw.githubusercontent.com/'));assert((await page.locator('#download').getAttribute('href')).includes('b'.repeat(40)));
  await page.evaluate(()=>{const a=document.createElement('a');a.id='inspection';a.href='inspect/index.html';document.body.append(a);});await page.waitForFunction(()=>document.querySelector('#inspection').href.endsWith('/inspect/packet.md'));
  const pinned=await page.evaluate(()=>WakePublicData.pin(new URL('bob-chat.html',location.href)).href);
  latest='c'.repeat(40);const before=seen.filter(s=>s.includes('api.github.com')).length;
  const popup=await context.newPage();await popup.goto(pinned);await popup.evaluate(()=>WakePublicData.ready);
  assert.equal(await popup.evaluate(()=>WakePublicData.revision),'b'.repeat(40));assert.equal(seen.filter(s=>s.includes('api.github.com')).length,before);
  const missing=await page.evaluate(async()=>{const r=await WakePublicData.fetch('research-data.json');return r.status;});assert.equal(missing,404,'Missing pinned packets must not fall back to a different bundled snapshot');
  for(const url of ['https://outside.invalid/data.json','../secret.json','runtime.json','reader-records/execute.js','inspect/index.html']){
   assert(await page.evaluate(async url=>{try{await WakePublicData.fetch(url);return false;}catch{return true;}},url));
  }
  wrongIdentity=true;await page.evaluate(()=>{const frame=document.createElement('iframe');frame.src='./';document.body.append(frame);});await page.waitForFunction(()=>document.querySelector('iframe').contentWindow.WakePublicData?.mode==='unavailable');assert.equal(await page.evaluate(()=>WakePublicData.mode),'published');await page.evaluate(()=>document.querySelector('iframe').remove());wrongIdentity=false;
  // A bounded initial discovery failure selects one readable bundled generation.
  failDiscovery=true;await page.evaluate(()=>localStorage.clear());await page.reload();await page.evaluate(()=>WakePublicData.ready);
  assert.equal(await page.evaluate(()=>WakePublicData.mode),'bundled');assert.equal((await read()).version,'bundled');await page.locator('#public-data-notice').waitFor();
  const bundled=await page.evaluate(()=>WakePublicData.pin(new URL('bob-chat.html',location.href)).href);
  failDiscovery=false;const fallbackLookups=seen.length;await popup.goto(bundled);await popup.evaluate(()=>WakePublicData.ready);assert.equal(await popup.evaluate(()=>WakePublicData.mode),'bundled');assert.equal(seen.length,fallbackLookups);
  await page.evaluate(()=>{const frame=document.createElement('iframe');frame.src='./';document.body.append(frame);});await page.waitForFunction(()=>document.querySelector('iframe').contentWindow.WakePublicData?.mode==='bundled');assert.equal(seen.length,fallbackLookups);
  failDiscovery='slow';await page.evaluate(()=>localStorage.clear());await page.reload();const slow=await page.evaluate(async()=>{const response=await WakePublicData.fetch('reader-data.json',{signal:AbortSignal.timeout(8000)});return response.json();});assert.equal(slow.version,'bundled','Slow discovery must leave time to read the fallback');failDiscovery=false;
  wrongIdentity=true;await page.reload();await page.evaluate(()=>WakePublicData.ready);assert.equal(await page.evaluate(()=>WakePublicData.mode),'bundled');
  await popup.goto(pinned);assert(await popup.evaluate(async()=>{try{await WakePublicData.ready;return false;}catch{return true;}}),'An unavailable pinned popup must not substitute other sources');
  console.log(JSON.stringify({result:'PASS',checks:'unchanged interface reads new data, immutable document version, shared discovery cache, popup version, missing packet isolation, identity validation, readable failure fallback'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
