/* Real browser checks for responsive habitat, observer playback and personal saves. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets'),{Colony}=require(path.join(assets,'ant-colony.js'));
const mine=new Colony(9876).save(),caretaker=require('../../scripts/bob_ant_farm.cjs');
const packet=caretaker.advancePacket(caretaker.bootstrap({sourceRevision:'a'.repeat(40),at:'2026-10-26T18:00:00Z'}),{sourceRevision:'a'.repeat(40),at:'2026-10-26T19:00:00Z',ticks:120});
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');
 if(url.pathname==='/bob-ant-farm.json'){res.setHeader('Content-Type','application/json');res.end(JSON.stringify(packet));return;}
 if(url.pathname==='/ant-farm.html'){const html=fs.readFileSync(path.join(assets,'ant-farm.html'),'utf8');res.setHeader('Content-Type','text/html');res.end(html.replace('<head>',`<head><script>window.WAKE_DEPLOYMENT={bob_ant_farm:{preview_path:'bob-ant-farm.json'}};window.__bobPacket=${JSON.stringify(packet)};const originalFetch=window.fetch;window.fetch=(...args)=>{if(String(args[0]).includes('bob-ant-farm.json')){window.__bobReads=(window.__bobReads||0)+1;if(window.__failBob)return Promise.reject(Error('Unavailable fixture'));}return originalFetch(...args);};</script>`));return;}

 const file=path.join(assets,url.pathname);if(!file.startsWith(assets+path.sep)){res.writeHead(404);res.end();return;}
 fs.readFile(file,(error,data)=>{if(error){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':file.endsWith('.png')?'image/png':file.endsWith('.webp')?'image/webp':'text/html');res.end(data);});
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const context=await browser.newContext({viewport:{width:1200,height:900},timezoneId:'America/Los_Angeles',hasTouch:true}),page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message));await context.addInitScript(value=>localStorage.setItem('wake-ant-colony@2',value),JSON.stringify(mine));
  await page.clock.install({time:new Date('2026-10-26T19:00:00Z')});const base=`http://127.0.0.1:${server.address().port}/ant-farm.html`;
  await page.goto(base);await page.locator('#habitat').waitFor({state:'visible'});
  assert.equal(await page.locator('#farm-choice').inputValue(),'bob');assert.equal(await page.locator('#trails').getAttribute('aria-pressed'),'false');
  assert.equal(await page.locator('#feed').evaluate(el=>el.hidden&&el.disabled),true);assert.equal(await page.locator('#new-colony').evaluate(el=>el.hidden),true);
  assert.equal(await page.locator('#pause').innerText(),'');assert.equal(await page.locator('#fullscreen').innerText(),'');assert.equal(await page.locator('#pause svg,#fullscreen svg').count(),2);
  await page.getByRole('button',{name:'Pause playback',exact:true}).click();assert.equal(await page.getByRole('button',{name:'Play playback',exact:true}).count(),1);
  const untouched=await page.evaluate(()=>localStorage.getItem('wake-ant-colony@2')),originalPacket=await page.evaluate(()=>JSON.stringify(window.__bobPacket));
  await page.evaluate(()=>{document.querySelector('#feed').onclick();document.querySelector('#confirm-reset').onclick();});await page.waitForTimeout(150);
  assert.equal(await page.evaluate(()=>localStorage.getItem('wake-ant-colony@2')),untouched);assert.equal(await page.evaluate(()=>JSON.stringify(window.__bobPacket)),originalPacket);
  await page.locator('#farm-choice').selectOption('mine');await page.getByRole('button',{name:'Pause simulation',exact:true}).click();
  const alpha=await page.locator('#habitat').evaluate(canvas=>canvas.getContext('2d').getImageData(20,5,1,1).data[3]);assert.ok(alpha<60,'Glass above the soil reveals room scenery');
  assert.equal(await page.locator('.habitat-case').evaluate(el=>getComputedStyle(el).backgroundColor),'rgba(0, 0, 0, 0)');
  assert.equal(await page.locator('.sun').isVisible(),true);assert.equal(await page.locator('.moon').isVisible(),false);
  const canvas=page.locator('#habitat');assert.equal(await page.locator('#zoom,#zoom-out,#follow-ant').count(),0);assert.equal(await canvas.evaluate(el=>getComputedStyle(el).touchAction),'auto');
  for(const ctrlKey of [false,true])assert.equal(await canvas.evaluate((el,ctrlKey)=>{const event=new WheelEvent('wheel',{deltaY:-100,ctrlKey,cancelable:true});el.dispatchEvent(event);return event.defaultPrevented;},ctrlKey),false);
  await page.getByRole('button',{name:'Add food',exact:true}).click();assert.equal(await page.locator('#feed').evaluate(el=>el.classList.contains('is-activated')),true);assert.match(await page.locator('#scene-note').innerText(),/Food added/);
  await page.locator('#trails').click();assert.equal(await page.locator('#trails').getAttribute('aria-pressed'),'true');
  await page.locator('#observe').click();await page.locator('#ant-select').selectOption('queen');assert.match(await page.locator('#ant-detail').innerText(),/does not direct/);await page.locator('#close-observations').click();
  const saved=await page.evaluate(()=>localStorage.getItem('wake-ant-colony@2'));assert.equal(JSON.parse(saved).seed,9876);
  await page.locator('#farm-choice').selectOption('bob');await page.waitForTimeout(80);assert.equal(await page.evaluate(()=>localStorage.getItem('wake-ant-colony@2')),saved,'Shared playback never overwrites personal save');
  await page.locator('#farm-choice').selectOption('mine');await page.getByRole('button',{name:'Pause simulation',exact:true}).click();assert.equal(await page.evaluate(()=>JSON.parse(localStorage.getItem('wake-ant-colony@2')).seed),9876);
  await page.getByRole('button',{name:'Enter full screen',exact:true}).click();await page.waitForTimeout(80);const full=await canvas.boundingBox();assert.ok(full.width>=1190&&full.height>=890);assert.ok(Math.abs(full.y+full.height-900)<2,'Fullscreen sand reaches viewport bottom');
  await page.getByRole('button',{name:'Exit full screen',exact:true}).click();assert.equal(await page.locator('#farm').evaluate(el=>el.classList.contains('is-fullscreen')),false);
  if(process.env.ANT_FARM_SCREENSHOT)await page.screenshot({path:process.env.ANT_FARM_SCREENSHOT});
  await page.clock.setFixedTime(new Date('2026-10-27T02:00:00Z'));await page.reload();await canvas.waitFor({state:'visible'});assert.equal(await page.locator('.sun').isVisible(),false);assert.equal(await page.locator('.moon').isVisible(),true);assert.equal(await page.locator('#trails').getAttribute('aria-pressed'),'false');
  // A missing shared packet must not invent a substitute or consume the personal save.
  const failed=await context.newPage();await failed.addInitScript(()=>{window.__failBob=true;});await failed.goto(base);await failed.waitForFunction(()=>document.querySelector('#scene-note').textContent.includes('unavailable'));assert.equal(await failed.locator('#habitat').isVisible(),false);await failed.locator('#farm-choice').selectOption('mine');await failed.locator('#habitat').waitFor({state:'visible'});await failed.close();
  const phone=await browser.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true}),mobile=await phone.newPage();mobile.on('pageerror',e=>errors.push(e.message));await mobile.goto(base+'?farm=mine');await mobile.getByRole('button',{name:'Pause simulation',exact:true}).click();
  assert(await mobile.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));const initial=await mobile.locator('#habitat').boundingBox();assert(initial.height>844*.65,'Phone habitat uses the available vertical space');
  await mobile.locator('#fullscreen').click();await mobile.waitForTimeout(100);const mobileFull=await mobile.locator('#habitat').boundingBox();assert.ok(Math.abs(mobileFull.y+mobileFull.height-844)<2);assert.ok(mobileFull.height>=840);await mobile.locator('#fullscreen').click();
  await mobile.setViewportSize({width:390,height:700});await mobile.waitForTimeout(100);const shorter=await mobile.locator('#habitat').boundingBox();assert(shorter.height<initial.height-100,'Changing available height resizes the habitat');await mobile.setViewportSize({width:390,height:844});await mobile.waitForTimeout(100);
  const session=await phone.newCDPSession(mobile),habitat=await mobile.locator('#habitat').boundingBox();
  const snapshot=()=>mobile.evaluate(()=>{const c=document.querySelector('#habitat'),b=c.getBoundingClientRect(),f=document.querySelector('.habitat-case').getBoundingClientRect();return{scale:visualViewport.scale,header:document.querySelector('.farm-header').getBoundingClientRect().width,pixels:c.width,pixelHeight:c.height,box:{x:b.x,y:b.y,width:b.width,height:b.height},frame:{x:f.x,y:f.y,width:f.width,height:f.height}};});
  const before=await snapshot();await session.send('Input.synthesizePinchGesture',{x:habitat.x+habitat.width/2,y:habitat.y+habitat.height/2,scaleFactor:1.7,relativeSpeed:800,gestureSourceType:'touch'});await mobile.waitForTimeout(250);const after=await snapshot();
  assert(after.scale>before.scale*1.3);assert.equal(after.header,before.header);assert.deepEqual(after.box,before.box);assert.deepEqual(after.frame,before.frame);assert(after.pixels>before.pixels*1.3);assert(after.pixels*after.pixelHeight<4100000);
  await session.send('Input.synthesizePinchGesture',{x:100,y:180,scaleFactor:.5,relativeSpeed:800,gestureSourceType:'touch'});await mobile.waitForTimeout(250);const out=await snapshot();assert(out.scale<after.scale);assert(out.pixels<after.pixels);
  await mobile.screenshot({path:'/tmp/wake-ant-living-phone.png'});await phone.close();assert.deepEqual(errors,[]);
  console.log(JSON.stringify({result:'PASS',checks:'trails off, automatic Bob readonly replay, personal save preservation, unavailable shared state, visible action feedback, SVG play/pause/fullscreen, queen inspector, taller responsive phone habitat, fullscreen bottom coverage, native page pinch, bounded rendering, transparent glass and day/night'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
