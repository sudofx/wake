/* Real browser checks: transparent glass, one sky light, drag/pinch and fullscreen. */
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
  await page.addInitScript(()=>{const draw=CanvasRenderingContext2D.prototype.drawImage;CanvasRenderingContext2D.prototype.drawImage=function(...args){if(this.canvas.id==='habitat'&&args.length===9&&args[0].width===this.canvas.width&&args[0].height===this.canvas.height)window.__view=args.slice(1);return draw.apply(this,args);};});
  await page.clock.install({time:new Date('2026-10-26T19:00:00Z')});
  const base=`http://127.0.0.1:${server.address().port}/ant-farm.html`;
  await page.goto(base);await page.getByRole('button',{name:'Pause',exact:true}).click();
  const alpha=await page.locator('#habitat').evaluate(canvas=>canvas.getContext('2d').getImageData(20,5,1,1).data[3]);
  assert.ok(alpha<60,'Glass above the soil must reveal the scenery behind it');
  assert.equal(await page.locator('.habitat-case').evaluate(el=>getComputedStyle(el).backgroundColor),'rgba(0, 0, 0, 0)');
  assert.equal(await page.locator('.sun').isVisible(),true);assert.equal(await page.locator('.moon').isVisible(),false);
  await page.getByRole('button',{name:'Zoom in',exact:true}).click();await page.waitForTimeout(100);
  const canvas=page.locator('#habitat'),box=await canvas.boundingBox(),start=await page.evaluate(()=>window.__view);
  await page.mouse.move(box.x+box.width*.5,box.y+box.height*.5);await page.mouse.down();await page.mouse.move(box.x+box.width*.65,box.y+box.height*.55,{steps:12});await page.mouse.up();await page.waitForTimeout(100);
  const moved=await page.evaluate(()=>window.__view);assert.ok(Math.abs(start[0]-moved[0])>10,'Mouse drag must pan the zoomed habitat');
  const cdp=await context.newCDPSession(page),x=box.x+box.width*.5,y=box.y+box.height*.5;
  const touches=(a,b)=>[{x:a,y,radiusX:3,radiusY:3,id:1},...(b===undefined?[]:[{x:b,y,radiusX:3,radiusY:3,id:2}])];
  await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:touches(x-70,x+70)});
  await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:touches(x-110,x+110)});
  await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});await page.waitForTimeout(100);
  const pinched=await page.evaluate(()=>window.__view);assert.ok(pinched[2]<moved[2],'Two-finger pinch must magnify the colony');
  await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:touches(x)});
  await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:touches(x-100)});
  await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});await page.waitForTimeout(100);
  const dragged=await page.evaluate(()=>window.__view);assert.ok(Math.abs(dragged[0]-pinched[0])>10,'One-finger drag after pinch must pan');
  await page.getByRole('button',{name:'Enter full screen',exact:true}).click();await page.waitForTimeout(100);
  assert.equal(await page.locator('#farm').evaluate(el=>el.classList.contains('is-fullscreen')),true);
  const full=await canvas.boundingBox();assert.ok(full.width>=1190&&full.height>=890);
  await page.getByRole('button',{name:'Exit full screen',exact:true}).click();assert.equal(await page.locator('#farm').evaluate(el=>el.classList.contains('is-fullscreen')),false);
  await canvas.focus();await page.keyboard.press('Home');await page.waitForTimeout(100);
  if(process.env.ANT_FARM_SCREENSHOT)await page.screenshot({path:process.env.ANT_FARM_SCREENSHOT});
  await page.clock.setFixedTime(new Date('2026-10-27T02:00:00Z'));await page.reload();
  assert.equal(await page.locator('.sun').isVisible(),false);assert.equal(await page.locator('.moon').isVisible(),true);
  await page.setViewportSize({width:390,height:844});await page.waitForTimeout(100);
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Phone controls must fit without document overflow');
  assert.deepEqual(errors,[]);console.log(JSON.stringify({result:'PASS',checks:'transparent glass, single day/night light, mouse pan, pinch, touch pan, fullscreen enter/exit, phone width'}));
 }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
