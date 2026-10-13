/* Offline installation fixture: no provider calls, record writes, or runtime controls. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),http=require('node:http'),fs=require('node:fs'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets'),now=new Date().toISOString();
const research={status:{accepted_cycles:3,pending:false},metrics:{outcomes:{accepted:3,rejected:1,deferred:0,failed:0}},activity:[{id:'fixture-receipt',status:'accepted',time:now,model:'fixture-model'}],wakes:[{id:'fixture-receipt',receipt:{available:true,seq:4,hash:'fixture-hash'}}]};
let live=true,offline=false;
const manifest=()=>({schema:1,installation_id:'wake',generated:now,live,nodes:[{id:'100.wake',role:'parent',parent:null,available:true,snapshot:{head:'head-parent',version:3,generated:now},runtime:{state:'paused',observed_at:now,activity:{stage:'idle'}},research},{id:'101.wake',role:'child',parent:'100.wake',available:false,snapshot:null,runtime:null,research:null}]});
const server=http.createServer((req,res)=>{const url=new URL(req.url,'http://localhost');if(url.pathname.endsWith('/installation.json')){if(offline){res.writeHead(503);res.end();return;}res.setHeader('content-type','application/json');res.end(JSON.stringify(manifest()));return;}const name=path.basename(url.pathname);if(name==='console.html'){res.setHeader('content-type','text/html');res.end(url.pathname.includes('/nodes/')?'<html><body><div class="console-overview"><div></div></div><script src="installation-console.js"></script></body></html>':fs.readFileSync(path.join(assets,'installation.html')));return;}const file=path.join(assets,name);if(!fs.existsSync(file)){res.writeHead(404);res.end();return;}res.setHeader('content-type',name.endsWith('.js')?'text/javascript':name.endsWith('.css')?'text/css':'text/plain');res.end(fs.readFileSync(file));});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const base=`http://127.0.0.1:${server.address().port}/wake/`;
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const page=await browser.newPage(),errors=[];page.on('pageerror',error=>errors.push(error.message));
  await page.goto(base+'console.html');await page.locator('#installation-nodes tr').first().waitFor();
  assert.equal(await page.locator('#installation-nodes tr').count(),2);assert.match(await page.locator('#installation-nodes tr').nth(1).innerText(),/Unavailable/);
  assert.match(await page.locator('#installation-summary').innerText(),/available nodes only/);
  assert.match(await page.locator('#installation-live').innerText(),/idle/);
  assert.equal(await page.locator('#installation-receipts a').getAttribute('href'),base+'nodes/100.wake/console.html?wake=fixture-receipt');
  for(const viewport of [{width:1440,height:1100},{width:390,height:844}]){await page.setViewportSize(viewport);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));assert.equal(await page.locator('.masthead').evaluate(e=>getComputedStyle(e).position),'fixed');}
  await page.screenshot({path:'/tmp/wake-installation-console-mobile.png',fullPage:true});
  await page.locator('.installation-node-picker select').selectOption(base+'nodes/100.wake/console.html');await page.waitForURL('**/nodes/100.wake/console.html');
  await page.locator('.installation-node-picker select option').nth(2).waitFor({state:'attached'});assert.equal(await page.locator('.installation-node-picker select').inputValue(),base+'nodes/100.wake/console.html');
  await page.locator('.installation-node-picker select').selectOption(base+'console.html');await page.waitForURL('**/wake/console.html');
  offline=true;await page.waitForTimeout(5500);assert.match(await page.locator('#installation-notice').innerText(),/Connection unavailable/);assert.match(await page.locator('#installation-live').innerText(),/unavailable/);
  offline=false;live=false;await page.reload();await page.locator('#installation-nodes tr').first().waitFor();assert.match(await page.locator('#installation-freshness').innerText(),/Published mirror/);assert.match(await page.locator('#installation-live').innerText(),/unavailable/);assert.equal(await page.locator('button').count(),0);
  await page.setViewportSize({width:1440,height:1100});await page.screenshot({path:'/tmp/wake-installation-console-desktop.png',fullPage:true});assert.deepEqual(errors,[]);
  console.log('PASS: node switching preserves hosted subpaths; missing snapshots remain unknown; receipts are attributed; disconnect clears live claims; mirror has no controls; mobile has no page overflow; masthead remains fixed.');
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
