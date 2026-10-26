/* Real browser checks: transparent glass, one sky light, mouse pan, native page pinch and fullscreen. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),fs=require('node:fs'),http=require('node:http'),path=require('node:path');
const assets=path.resolve(__dirname,'../../wake/assets');
const server=http.createServer((req,res)=>{
 const file=path.join(assets,new URL(req.url,'http://localhost').pathname);
 if(!file.startsWith(assets+path.sep)){res.writeHead(404);res.end();return;}
 fs.readFile(file,(error,data)=>{if(error){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':file.endsWith('.png')?'image/png':'text/html');res.end(data);});
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const context=await browser.newContext({viewport:{width:1200,height:900},timezoneId:'America/Los_Angeles',hasTouch:true}),page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.clock.install({time:new Date('2026-10-26T19:00:00Z')});
  const base=`http://127.0.0.1:${server.address().port}/ant-farm.html`;
  await page.goto(base);await page.getByRole('button',{name:'Pause',exact:true}).click();
  const alpha=await page.locator('#habitat').evaluate(canvas=>canvas.getContext('2d').getImageData(20,5,1,1).data[3]);
  assert.ok(alpha<60,'Glass above the soil must reveal the scenery behind it');
  assert.equal(await page.locator('.habitat-case').evaluate(el=>getComputedStyle(el).backgroundColor),'rgba(0, 0, 0, 0)');
  assert.equal(await page.locator('.sun').isVisible(),true);assert.equal(await page.locator('.moon').isVisible(),false);
  const canvas=page.locator('#habitat');
  assert.equal(await page.locator('#zoom,#zoom-out,#follow-ant').count(),0,'No separate colony zoom controls or follow camera');
  assert.equal(await canvas.evaluate(el=>getComputedStyle(el).touchAction),'auto');
  for(const ctrlKey of [false,true])assert.equal(await canvas.evaluate((el,ctrlKey)=>{const event=new WheelEvent('wheel',{deltaY:-100,ctrlKey,cancelable:true});el.dispatchEvent(event);return event.defaultPrevented;},ctrlKey),false,'Wheel gestures belong to the browser');
  await page.getByRole('button',{name:'Enter full screen',exact:true}).click();await page.waitForTimeout(100);
  assert.equal(await page.locator('#farm').evaluate(el=>el.classList.contains('is-fullscreen')),true);
  const full=await canvas.boundingBox();assert.ok(full.width>=1190&&full.height>=890);
  await page.getByRole('button',{name:'Exit full screen',exact:true}).click();assert.equal(await page.locator('#farm').evaluate(el=>el.classList.contains('is-fullscreen')),false);

  if(process.env.ANT_FARM_SCREENSHOT)await page.screenshot({path:process.env.ANT_FARM_SCREENSHOT});
  await page.clock.setFixedTime(new Date('2026-10-27T02:00:00Z'));await page.reload();
  assert.equal(await page.locator('.sun').isVisible(),false);assert.equal(await page.locator('.moon').isVisible(),true);
  await page.setViewportSize({width:390,height:844});await page.waitForTimeout(100);
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Phone controls must fit without document overflow');
  const phone=await browser.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true}),mobile=await phone.newPage();
  mobile.on('pageerror',e=>errors.push(e.message));
  await mobile.goto(base);await mobile.getByRole('button',{name:'Pause',exact:true}).click();
  const session=await phone.newCDPSession(mobile),habitat=await mobile.locator('#habitat').boundingBox();
  const snapshot=()=>mobile.evaluate(()=>{
    const canvas=document.querySelector('#habitat'),box=canvas.getBoundingClientRect(),frame=document.querySelector('.habitat-case').getBoundingClientRect();
    return {scale:visualViewport.scale,header:document.querySelector('.farm-header').getBoundingClientRect().width,farm:document.querySelector('#farm').className,pixels:canvas.width,pixelHeight:canvas.height,box:{x:box.x,y:box.y,width:box.width,height:box.height},frame:{x:frame.x,y:frame.y,width:frame.width,height:frame.height}};
  });
  const before=await snapshot();
  await session.send('Input.synthesizePinchGesture',{x:habitat.x+habitat.width/2,y:habitat.y+habitat.height/2,scaleFactor:1.7,relativeSpeed:800,gestureSourceType:'touch'});
  await mobile.waitForTimeout(250);
  const after=await snapshot();
  assert.ok(after.scale>before.scale*1.3,'Native pinch must enlarge the whole visual viewport');
  assert.equal(after.header,before.header,'Page zoom must preserve the layout of all elements');
  assert.equal(after.farm,before.farm,'Native pinch must not engage the internal zoom layout');
  assert.deepEqual(after.box,before.box,'Page zoom must not move the sand within the frame');
  assert.deepEqual(after.frame,before.frame,'The frame shares the same page zoom as the canvas');
  assert.ok(after.pixels>before.pixels*1.3,'Pinching in must rerender ants at greater pixel detail, even when paused');
  assert.ok(after.pixels*after.pixelHeight<4100000,'Backing buffers stay within their pixel budget');
  await session.send('Input.synthesizePinchGesture',{x:195,y:400,scaleFactor:.6,relativeSpeed:800,gestureSourceType:'touch'});await mobile.waitForTimeout(250);
  const out=await snapshot();assert.ok(out.scale<after.scale);assert.ok(out.pixels<after.pixels,'Zooming out releases the larger backing buffers');
  await mobile.screenshot({path:'/tmp/wake-ant-native-zoom-phone.png'});
  await phone.close();
  assert.deepEqual(errors,[]);console.log(JSON.stringify({result:'PASS',checks:'transparent glass, single day/night light, no internal camera or zoom buttons, native whole-page pinch, higher detail at zoom, bounded buffers, browser wheel zoom, fullscreen enter/exit, phone width'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
