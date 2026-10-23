/* Actual exported reader, with all node/status observations unavailable. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const site=process.argv[2];if(!site)throw Error('Usage: reader-transport.cjs <exported site>');
const full=JSON.parse(fs.readFileSync(path.join(site,'wake-data.json'))),requests=[];
let failDetails=false;
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');requests.push(url.pathname);
 if(/runtime|installation\.json/.test(url.pathname)){res.writeHead(503);res.end();return;}
 if(failDetails&&url.pathname.includes('/reader-records/')&&!url.pathname.includes('/pages/')){res.writeHead(503);res.end();return;}
 const file=path.join(site,url.pathname==='/'?'index.html':url.pathname.slice(1));
 if(!file.startsWith(site+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile()){res.writeHead(404);res.end();return;}
 res.setHeader('Content-Type',file.endsWith('.html')?'text/html':file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':'application/json');
 res.end(fs.readFileSync(file));
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const page=await browser.newPage({viewport:{width:390,height:844}}),errors=[];page.on('pageerror',error=>errors.push(error.message));
  const base=`http://127.0.0.1:${server.address().port}/`;
  const topic=(full.state.research_topics||[]).find(t=>(t.origins||[]).some(o=>o.node+'::'+o.id!==t.id));
  if(topic){
   const origin=topic.origins.find(o=>o.node+'::'+o.id!==topic.id);
   await page.goto(base+'projects.html#projects/topic:'+encodeURIComponent(origin.node+'::'+origin.id));
   await page.locator('#pet-projects .topic-filter-note').waitFor();
   assert((await page.locator('#pet-projects .topic-filter-note').innerText()).includes(topic.label.toLowerCase()),'Historical node-qualified topic aliases resolve to the merged catalog');
  }
  const started=Date.now();await page.goto(base,{waitUntil:'domcontentloaded'});await page.locator('#attention-question').waitFor();
  const ready=Date.now()-started;assert(ready<3000,`Reader ready in ${ready}ms despite unavailable observations`);
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Phone has no horizontal overflow');
  const post=Object.values(full.state.posts).find(post=>post.status!=='superseded');
  if(post){
   failDetails=true;await page.goto(base+'blog.html#blog/'+encodeURIComponent(post.id));
   await page.locator('[data-reader-error]').waitFor();
   failDetails=false;await page.getByRole('button',{name:'Retry loading details'}).click();
   await page.locator('.blog-reading').waitFor();assert((await page.locator('.blog-reading').innerText()).includes(post.title));
  }
  await page.goto(base+'journal.html');await page.locator('#entries .entry').first().waitFor();
  if(full.state.journal.length>24){const before=await page.locator('#entries .entry').count();await page.getByRole('button',{name:'Load older journal'}).click();await page.waitForFunction(before=>document.querySelectorAll('#entries .entry').length>before,before);}
  const evidence=Object.values(full.state.evidence)[0];
  if(evidence){await page.goto(base+'evidence.html#evidence/'+encodeURIComponent(evidence.id));await page.locator('.evidence-card').first().waitFor();assert((await page.locator('.evidence-card').first().innerText()).includes(evidence.source));}
  const notebook=Object.values(full.state.notebooks)[0];
  if(notebook){await page.goto(base+'projects.html#projects/notebook:'+encodeURIComponent(notebook.id));await page.locator('.notebook-reading').waitFor();assert((await page.locator('.notebook-reading').innerText()).includes(notebook.title));}
  assert(!requests.some(url=>/^\/(wake-data|research-data)\.json$/.test(url)),'No full archive downloaded for ordinary reader navigation');
  assert(!requests.some(url=>url==='/group/bob.json'),'Accepted reader posts do not wait for group transport');
  assert.deepEqual(errors,[]);
  console.log(JSON.stringify({result:'PASS',homepage_ready_ms:ready,reader_bytes:fs.statSync(path.join(site,'reader-data.json')).size,full_archive_bytes:fs.statSync(path.join(site,'wake-data.json')).size,checks:'phone home, exact blog/evidence/notebook details, journal, unavailable nodes, no archive fetch'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
