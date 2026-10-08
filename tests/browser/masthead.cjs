/* Run against a generated standalone fixture, never raw templates or authority.
   PLAYWRIGHT_MODULE and optional CHROME_EXECUTABLE select an installed browser. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict');
const base=process.argv[2];if(!base)throw Error('Usage: node tests/browser/masthead.cjs <fixture URL>');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
 const selectors=['.masthead','.wordmark','.compact-nav','.header-tools','.theme-switch','.console-link','.actions-light'];
 const pages=['index.html','console.html','map.html','map3d.html','state.html','events.html','rejected.html','notebooks/chrome-test.html'];
 const errors=[];
 for(const width of [1440,900,390,320]){
  let baseline;
  for(const theme of ['dark','light']){
   const context=await browser.newContext({viewport:{width,height:1000},colorScheme:theme,reducedMotion:'reduce'});
   const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));page.on('requestfailed',r=>errors.push(r.url()+': '+r.failure()?.errorText));
   for(const path of pages){
    await page.goto(new URL(path,base).href);await page.waitForLoadState('networkidle');await page.locator('.actions-light[data-state=stopped]').waitFor();
    const geometry=await page.evaluate(selectors=>selectors.map(s=>{const e=document.querySelector(s),r=e.getBoundingClientRect(),c=getComputedStyle(e);return [s,...[r.x,r.y,r.width,r.height].map(n=>Math.round(n*100)/100),c.fontSize,c.fontFamily]}),selectors);
    if(!baseline)baseline=geometry;else assert.deepEqual(geometry,baseline,`${width} ${theme} ${path}`);
    if(!(await page.locator('html').getAttribute('data-theme')))console.error('theme missing',path,await page.evaluate(()=>({url:location.href,owner:typeof window.WakeTheme,scripts:[...document.scripts].map(s=>s.src),root:document.documentElement.outerHTML.slice(0,100)})));
    assert.equal(await page.locator('html').getAttribute('data-theme'),theme,`${width} ${theme} ${path}: ${errors.join('; ')}`);
    assert.equal(await page.locator('.actions-light-label').count(),0);
    assert.match(await page.locator('.wordmark small').innerText(),/ACCEPTED WAKES$/);
    const glass=await page.locator('.masthead').evaluate(e=>{const s=getComputedStyle(e);return {background:s.backgroundColor,blur:s.backdropFilter,webkit:s.getPropertyValue("-webkit-backdrop-filter")||s.backdropFilter}});
    assert.match(glass.blur,/blur\(24px\)/);const alpha=Number(glass.background.match(/\/\s*([\d.]+)\)/)?.[1]);assert(alpha>0&&alpha<=.53,glass.background);
    assert.match(glass.webkit,/blur\(24px\)/);
    assert.equal(await page.locator('.header-tools>*').first().getAttribute('class'),'theme-switch');
    const consoleStyle=await page.locator('.console-link').evaluate(e=>{const c=getComputedStyle(e);return [c.backgroundColor,c.borderWidth,c.boxShadow]});
    assert.deepEqual(consoleStyle,['rgba(0, 0, 0, 0)','0px','none']);
    await page.locator('.console-link').hover({timeout:3000}).catch(async error=>{console.error(width,theme,path,await page.locator('#details').evaluate(e=>({rect:e.getBoundingClientRect().toJSON(),position:getComputedStyle(e).position,z:getComputedStyle(e).zIndex})).catch(()=>null));throw error});
    assert.equal(await page.locator('.console-link').evaluate(e=>getComputedStyle(e).textDecorationLine),'none');
    assert.equal(await page.locator('.actions-light i').evaluate(e=>getComputedStyle(e).backgroundColor),'rgb(231, 195, 90)');
   }
   await context.close();
  }
 }
 const context=await browser.newContext({viewport:{width:390,height:844},hasTouch:true,colorScheme:'light'});
 const page=await context.newPage();await page.goto(new URL('console.html',base).href);
 await page.locator('.actions-light[data-state=stopped]').waitFor();
 await page.locator('.actions-light').tap();
 await page.locator('#site-tooltip:not([hidden])').waitFor();assert.match(await page.locator('#site-tooltip').innerText(),/Paused/);
 assert.match(await page.locator('.actions-light').getAttribute('aria-describedby'),/site-tooltip/);
 await page.locator('.theme-switch').tap();assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
 await page.goto(new URL('index.html',base).href);assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
 await page.goto(new URL('console.html',base).href);
 assert.equal(await page.locator('#matrix-cube').evaluate(e=>getComputedStyle(e).userSelect),'none');
 assert.notEqual(await page.locator('#wake-detail').evaluate(e=>getComputedStyle(e).userSelect),'none');
 await page.locator('#theme-toggle').focus();await page.keyboard.press('Space');assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
 await page.screenshot({path:'/tmp/wake-shared-masthead-mobile.png'});
 await context.route('**/runtime.json',route=>route.fulfill({json:{state:'running'}}));
 await page.reload();await page.locator('.actions-light[data-state=running]').waitFor();
 assert.equal(await page.locator('.actions-light i').evaluate(e=>getComputedStyle(e).backgroundColor),'rgb(63, 185, 80)');
 assert.match(await page.locator('.actions-light').getAttribute('aria-label'),/Running/);
 await context.close();assert.deepEqual(errors,[]);
 console.log('PASS: identical masthead across eight exported pages, four widths and both themes; unboxed active glyph, compact lamp, touch description, keyboard/theme persistence and selective selection.');
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1});
