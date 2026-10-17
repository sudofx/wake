/* Offline generated fixture: no authority reads, operators or providers. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const site=process.argv[2];if(!site)throw Error('Usage: research-transport.cjs <generated fixture directory>');
const overview=JSON.parse(fs.readFileSync(path.join(site,'research-overview.json')));
const selected=overview.wakes.find(w=>w.context.available&&w.detail_url);
if(!selected)throw Error('Fixture needs one recorded wake context');
const expected=JSON.parse(fs.readFileSync(path.join(site,selected.detail_url))).wake;
const requests=[],errors=[];let failDetail=false;
const server=http.createServer((req,res)=>{
 const name=new URL(req.url,'http://localhost').pathname.replace(/^\//,'');requests.push(name);
 if(name==='runtime.json'||name==='runtime.events'||name==='installation.json'){res.writeHead(404);res.end();return;}
 if(failDetail&&name===selected.detail_url){res.writeHead(503);res.end();return;}
 const file=path.join(site,name||'index.html');if(!fs.existsSync(file)||!fs.statSync(file).isFile()){res.writeHead(404);res.end();return;}
 res.setHeader('Content-Type',name.endsWith('.js')?'text/javascript':name.endsWith('.html')?'text/html':name.endsWith('.json')?'application/json':name.endsWith('.css')?'text/css':'application/octet-stream');res.end(fs.readFileSync(file));
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const page=await browser.newPage({viewport:{width:390,height:844}});page.on('pageerror',error=>errors.push(error.message));
  const base=`http://127.0.0.1:${server.address().port}/`;
  await page.goto(base+'console.html?wake='+encodeURIComponent(selected.id));
  await page.locator('#status-band .status-cell').first().waitFor();
  await page.locator('#process-field-canvas').scrollIntoViewIfNeeded();await page.waitForTimeout(250);
  assert.equal(requests.filter(name=>name==='research-overview.json').length,1,'Console and process field share the overview');
  assert(!requests.includes('research-data.json'),'initial page never loads full archive');
  assert(!requests.some(name=>name.startsWith('research-details/')),'summary does not prefetch contexts');
  failDetail=true;
  await page.locator('.wake-story>.wake-tabs [data-wake-tab="context"]').click();
  await page.locator('[data-retry-wake-detail]').waitFor();
  assert.match(await page.locator('#wake-detail').innerText(),/could not be loaded/);
  assert(!requests.includes('research-data.json'),'failed shard never loads full archive');
  failDetail=false;await page.locator('[data-retry-wake-detail]').click();
  await page.waitForFunction(()=>document.querySelector('#wake-detail').innerText.includes('Full recorded request'));
  const actual=await page.locator('#wake-detail pre').last().innerText();
  assert.deepEqual(JSON.parse(actual),expected.context.request);
  await page.locator('.wake-story>.wake-tabs [data-wake-tab="response"]').click();
  if(expected.response!=null)assert.equal(await page.locator('#wake-detail pre').innerText(),expected.response);
  else assert.match(await page.locator('#wake-detail').innerText(),/outside this event tail/);
  assert.equal(requests.filter(name=>name===selected.detail_url).length,2,'one failed request plus one shared successful detail');
  assert.deepEqual(errors,[]);await page.close();
  // A plotted wake outside the 24 eager summaries still opens its exact trace.
  const older=await browser.newPage({viewport:{width:390,height:844}}),oldId='older-exported-wake';
  const oldPath='research-details/'+'b'.repeat(64)+'.json';
  const oldSample={...overview.chart_wakes[0],id:oldId,detail_url:oldPath};
  await older.route('**/research-overview.json',route=>route.fulfill({json:{...overview,chart_wakes:[...overview.chart_wakes,oldSample]}}));
  await older.route('**/'+oldPath,route=>route.fulfill({json:{schema:1,wake:{...expected,id:oldId}}}));
  await older.goto(base+'console.html?wake='+oldId);
  await older.waitForFunction(()=>document.querySelector('#wake-detail').innerText.includes('older-exported-wake'));
  await older.locator('.wake-story>.wake-tabs [data-wake-tab="context"]').click();
  await older.waitForFunction(()=>document.querySelector('#wake-detail').innerText.includes('Full recorded request'));
  assert.deepEqual(JSON.parse(await older.locator('#wake-detail pre').last().innerText()),expected.context.request);
  await older.close();
  console.log('PASS: one compact initial overview, no archive or eager details, visible shard failure/retry, exact selected context/response.');
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
