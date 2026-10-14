/* Isolated generated fixture. No operator controls, authority access or providers. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const site=process.argv[2];if(!site)throw Error('Usage: performance-status.cjs <generated fixture directory>');
let state='paused',online=true,streams=0,runtimeRequests=0,projectionRequests=0,manifestRequests=0;
const clients=new Set(),initial=JSON.parse(fs.readFileSync(path.join(site,'research-data.json')));let projection=initial;
const runtime=()=>({mode:'standalone',state,activity_schema:1,runtime_id:'fixture',snapshot_generation:1,observed_at:new Date().toISOString(),capabilities:{live_activity:true},activity:{stage:'idle',active:false}});
const packet=()=>({mode:'installation',research:'running',state,members:[{id:'100.wake',runtime:runtime(),head:projection.head}],head:projection.head,capabilities:{live_activity:false,status_stream:true}});
const manifest=()=>({schema:1,live:true,installation_id:'fixture',generated:new Date().toISOString(),nodes:[{id:'100.wake',role:'parent',available:true,runtime:runtime(),snapshot:{head:projection.head,version:projection.version,generated:projection.generated},research:projection}]});
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost'),name=path.basename(url.pathname);
 if(name==='runtime.events'){streams++;res.writeHead(200,{'Content-Type':'text/event-stream','Cache-Control':'no-store'});clients.add(res);res.write('data: '+JSON.stringify(packet())+'\n\n');req.on('close',()=>clients.delete(res));return;}
 if(name==='runtime.json'){runtimeRequests++;res.setHeader('Content-Type','application/json');res.end(JSON.stringify(packet()));return;}
 if(name==='installation.json'){manifestRequests++;res.setHeader('Content-Type','application/json');res.end(JSON.stringify(manifest()));return;}
 if(name==='head.txt'){res.end(projection.head+'\n');return;}
 if(name==='research-data.json'){projectionRequests++;res.setHeader('Content-Type','application/json');res.end(JSON.stringify(projection));return;}
 const relative=url.pathname.replace(/^\/wake\//,''),file=path.join(site,relative||'index.html');if(!fs.existsSync(file)||!fs.statSync(file).isFile()){res.writeHead(404);res.end();return;}
 const type=name.endsWith('.js')?'text/javascript':name.endsWith('.css')?'text/css':name.endsWith('.html')?'text/html':'application/octet-stream';res.setHeader('Content-Type',type);
 let body=fs.readFileSync(file);if(url.searchParams.has('mirror')&&type==='text/html')body=body.toString().replace(/window.WAKE_DEPLOYMENT=(\{[^;]+\})/,(_,value)=>'window.WAKE_DEPLOYMENT='+JSON.stringify({...JSON.parse(value),snapshot_only:true}));res.end(body);
});
const tick=setInterval(()=>{if(online)for(const res of clients)res.write('data: '+JSON.stringify(packet())+'\n\n');},500);
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));const base=`http://127.0.0.1:${server.address().port}/wake/`;const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const page=await browser.newPage({viewport:{width:390,height:844}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(base+'console.html');await page.locator('#status-band .status-cell').first().waitFor();
  const light=page.locator('.installation-node-menu a[data-node="100.wake"] .installation-node-status');await light.waitFor({state:'attached'});
  await page.waitForFunction(()=>window.WakeStatusSnapshot?.members?.length===1);
  assert.equal(streams,1);assert.equal(projectionRequests,1,'Console and process field must share one projection request');
  const before=runtimeRequests;await page.waitForTimeout(3500);assert.equal(runtimeRequests,before,'healthy stream must not poll status');
  assert.equal(await page.locator('#matrix-cube').getAttribute('data-wake-initialized'),null,'offscreen cube stays uninstantiated');
  assert.equal(await page.locator('#research-map').innerHTML(),'','offscreen landscape stays unrendered');
  assert.equal(await page.locator('#compression svg').count(),0,'offscreen chart stays unrendered');
  assert.equal(await page.locator('#activity-chart').getAttribute('data-latest-initialized'),null,'hidden history does not initialize scrolling before rendering');
  await page.locator('#matrix-cube').evaluate(canvas=>canvas.closest('.panel').classList.add('module-collapsed'));
  await page.locator('.matrix-panel').scrollIntoViewIfNeeded();await page.waitForTimeout(300);
  assert.equal(await page.locator('#matrix-cube').getAttribute('data-wake-initialized'),null,'collapsed cube stays uninstantiated');
  await page.locator('#matrix-cube').evaluate(canvas=>canvas.closest('.panel').classList.remove('module-collapsed'));
  await page.locator('#matrix-cube').scrollIntoViewIfNeeded();await page.waitForFunction(()=>document.querySelector('#matrix-cube').dataset.wakeInitialized==='true');
  await page.locator('#map-stage').scrollIntoViewIfNeeded();await page.waitForFunction(()=>document.querySelector('#research-map').childElementCount>0);
  await page.locator('#activity-chart').scrollIntoViewIfNeeded();await page.waitForFunction(()=>document.querySelector('#activity-chart').dataset.latestInitialized==='true');
  assert(await page.locator('#activity-chart').evaluate(chart=>Math.abs(chart.scrollLeft-(chart.scrollWidth-chart.clientWidth))<2),'revealed history starts at its latest edge');
  state='running';await page.waitForFunction(()=>document.querySelector('.installation-node-menu a[data-node="100.wake"] .installation-node-status').dataset.state==='running');
  projection={...initial,head:'b'.repeat(64)};await page.waitForFunction(()=>window.WakeStatusSnapshot.head==='b'.repeat(64));await page.waitForTimeout(3500);assert.equal(projectionRequests,2,'head change fetches the projection once');
  online=false;for(const res of clients)res.destroy();clients.clear();await page.waitForFunction(()=>document.querySelector('.installation-node-menu a[data-node="100.wake"] .installation-node-status').dataset.state==='unknown');
  online=true;await page.waitForFunction(()=>document.querySelector('.installation-node-menu a[data-node="100.wake"] .installation-node-status').dataset.state==='running');
  assert.deepEqual(errors,[]);await page.close();
  online=true;const mirror=await browser.newPage({viewport:{width:390,height:844}});const counts=[streams,runtimeRequests];await mirror.goto(base+'console.html?mirror=1');await mirror.locator('#status-band .status-cell').first().waitFor();await mirror.waitForTimeout(3500);assert.deepEqual([streams,runtimeRequests],counts,'public snapshot must open no status connection');await mirror.close();
  console.log('PASS: one shared stream, one initial projection, no unchanged status polls, head-triggered data refresh, lazy canvas, disconnect clearing, no hosted live channel.');
 }finally{for(const res of clients)res.destroy();clearInterval(tick);await browser.close();server.close();}
})().catch(e=>{console.error(e);clearInterval(tick);for(const res of clients)res.destroy();server.close();process.exitCode=1;});
