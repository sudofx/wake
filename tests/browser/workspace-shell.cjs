/* Generated local fixture only. No provider calls or authority mutations. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),assert=require('node:assert/strict');
const base=process.argv[2];
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});try{
 for(const theme of ['dark','light']){
  const context=await browser.newContext({viewport:{width:2560,height:1200},colorScheme:theme}),page=await context.newPage();
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  for(const path of ['index.html','console.html','map.html','map3d.html','state.html','events.html','rejected.html','notebooks/chrome-test.html']){
   await page.goto(new URL(path,base).href);await page.waitForLoadState('networkidle');
   const head=await page.locator('.masthead').boundingBox();assert.equal(head.x,0,path);assert.equal(head.y,0,path);assert.equal(head.width,await page.evaluate(()=>document.documentElement.clientWidth),path);
  }
  await page.goto(new URL('console.html',base).href);await page.waitForLoadState('networkidle');
  for(const width of [1920,2560,3440,390]){
   await page.setViewportSize({width,height:1200});await page.waitForTimeout(200);
   const available=await page.evaluate(()=>document.documentElement.clientWidth),main=await page.locator('#main').boundingBox();assert.equal(main.x,0);assert.equal(main.width,available);
   const grid=await page.locator('#console-module-grid').boundingBox(),overview=await page.locator('[data-console-panel-id="001"]').boundingBox();assert.equal(overview.width,grid.width);assert.equal(grid.x,20);assert.equal(grid.x+grid.width,available-20);
   assert.equal(await page.locator('#console-module-grid').evaluate(e=>Number(getComputedStyle(e).getPropertyValue('--console-cols'))),width<768?1:Math.max(1,Math.floor((grid.width+16)/316)));
  }
  await page.setViewportSize({width:1920,height:1000});await page.waitForTimeout(200);
  if(theme==='dark'){
   const border=await page.locator('.console-story-panel').first().evaluate(e=>getComputedStyle(e).borderTopColor);assert.notEqual(border,'rgb(255, 177, 92)');
   const tint=await page.locator('.console-story-panel').first().evaluate(e=>getComputedStyle(e).backgroundImage),normal=await page.locator('.matrix-panel').evaluate(e=>getComputedStyle(e).backgroundImage);assert.notEqual(tint,normal);
  }
  await page.evaluate(()=>window.scrollTo(0,600));await page.locator('.masthead-scroll-hidden').waitFor();await page.waitForTimeout(220);
  assert((await page.locator('.masthead').boundingBox()).y<0);
  await page.evaluate(()=>window.scrollTo(0,480));await page.waitForFunction(()=>!document.querySelector('.masthead').classList.contains('masthead-scroll-hidden'));await page.waitForTimeout(220);
  assert.equal((await page.locator('.masthead').boundingBox()).y,0);
  assert(await page.locator('.masthead').evaluate(e=>{const r=e.getBoundingClientRect();return e.contains(document.elementFromPoint(r.width/2,12))}));
  await page.locator('.theme-switch').click();
  await page.evaluate(()=>window.scrollTo(0,800));await page.locator('.masthead-scroll-hidden').waitFor();await page.locator('.console-link').focus();await page.waitForFunction(()=>!document.querySelector('.masthead').classList.contains('masthead-scroll-hidden'));
  if(await page.locator('html').getAttribute('data-theme')!==theme)await page.locator('.theme-switch').click();
  await page.screenshot({path:`/tmp/wake-workspace-${theme}.png`});assert.deepEqual(errors,[]);await context.close();
 }
 const quiet=await browser.newContext({reducedMotion:'reduce'}),page=await quiet.newPage();await page.goto(new URL('console.html',base).href);assert.equal(await page.locator('.masthead').evaluate(e=>getComputedStyle(e).transitionDuration),'0s');await quiet.close();
 console.log('PASS: viewport-wide workspace at four sizes; eight full-width mastheads in both themes; subdued dark story panels; down/up scroll, keyboard reveal, top stacking and reduced motion.');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
