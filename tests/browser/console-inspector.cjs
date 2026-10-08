/* Read-only generated fixture. A synthetic record exercises selection without
   editing an installation's authority or contacting a model. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),assert=require('node:assert/strict');
const base=process.argv[2];
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});try{
 const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'light'}),page=await context.newPage();
 const source=await context.request.get(new URL('research-data.json',base).href).then(r=>r.json());
 source.graph.nodes=[{id:'project:inspector-fixture',kind:'project',title:'Inspector fixture',detail:{id:'inspector-fixture',status:'active',question:'A readable test record'}}];source.graph.edges=[];
 await context.route('**/research-data.json',r=>r.fulfill({json:source}));
 await page.goto(new URL('console.html',base).href);await page.waitForLoadState('networkidle');
 const main=page.locator('#main'),inspector=page.locator('[data-console-panel-id="014"]');const full=(await main.boundingBox()).width;assert.equal(full,await page.evaluate(()=>document.documentElement.clientWidth));
 await page.goto(new URL('console.html?record=project%3Ainspector-fixture',base).href);await page.locator('html.console-inspector-docked').waitFor();
 assert((await main.boundingBox()).width<full-200);
 // Measure usable content, not just the outer box: legacy padding once reserved
 // the inspector twice while the outer-width check still passed.
 const usable=await page.locator('#console-module-grid').evaluate(e=>{const m=e.closest('#main'),r=m.getBoundingClientRect(),g=e.getBoundingClientRect(),s=getComputedStyle(m);return {gap:r.right-g.right,padding:parseFloat(s.paddingRight)}});assert(usable.padding<=24);assert(usable.gap<=25);
 const desktopGap=await page.locator('.console-overview .panel-heading').evaluate(e=>e.getBoundingClientRect().bottom-e.querySelector('.panel-actions').getBoundingClientRect().bottom);assert(desktopGap>=19);
 assert.equal(await inspector.locator('.inspector-height-handle').count(),1);
 const rect=await inspector.boundingBox(),handle=await inspector.locator('.inspector-height-handle').boundingBox();await page.mouse.move(handle.x+handle.width/2,handle.y+handle.height/2);await page.mouse.down();await page.mouse.move(handle.x+handle.width/2,handle.y+handle.height/2-120,{steps:8});await page.mouse.up();assert((await inspector.boundingBox()).height<rect.height-50);
 const popupPromise=page.waitForEvent('popup');await inspector.locator('.panel-popout').click();const popup=await popupPromise;await popup.waitForLoadState('networkidle');
 await page.waitForFunction(()=>!document.documentElement.classList.contains('console-inspector-docked'));
 assert.equal((await main.boundingBox()).width,full);
 const frame=await popup.locator('.panel-popout-target').boundingBox(),viewport=await popup.evaluate(()=>({width:innerWidth,height:innerHeight}));assert(frame.y>=19);assert(frame.y+frame.height<=viewport.height-19);assert(frame.x+frame.width<=viewport.width-19);
 assert.equal(await popup.locator('.masthead').isVisible(),false);assert.equal(await popup.locator('.panel-popout-target .module-drag').isVisible(),false);
 const closing=popup.waitForEvent('close');await popup.locator('.panel-popout-target .panel-popout').click();await closing;await page.locator('html.console-inspector-docked').waitFor();assert((await main.boundingBox()).width<full-200);
 // Closing the native popup also returns its reserved space to the source.
 const secondPromise=page.waitForEvent('popup');await inspector.locator('.panel-popout').click();const second=await secondPromise;await second.waitForLoadState('networkidle');await page.waitForFunction(()=>!document.documentElement.classList.contains('console-inspector-docked'));await second.close();await page.locator('html.console-inspector-docked').waitFor();
 await page.locator('#close-inspector').click();await page.waitForFunction(()=>!document.documentElement.classList.contains('console-inspector-docked'));
 assert.equal(await page.locator('.map-key').evaluate(e=>Boolean(e.closest('.panel-actions'))),true);
 const borders=await page.locator('.console-story-panel').evaluateAll(nodes=>nodes.map(e=>getComputedStyle(e).borderTopColor));assert.equal(borders.length,7);
 const washes=await page.locator('.console-story-panel').evaluateAll(nodes=>nodes.map(e=>getComputedStyle(e).backgroundImage));assert(washes.every(c=>c.includes('166, 83, 9')));assert(borders.every(c=>c==='rgb(255, 177, 92)'));
 const cube=page.locator('#matrix-cube');await cube.scrollIntoViewIfNeeded();const zoom=await cube.getAttribute('data-zoom');await cube.hover();await page.mouse.wheel(0,-150);assert.equal(await cube.getAttribute('data-zoom'),zoom);
 await page.setViewportSize({width:390,height:844});await page.waitForTimeout(300);await page.locator('.map-node').first().scrollIntoViewIfNeeded();await page.locator('.map-node').first().click();await page.locator('html.console-inspector-docked').waitFor();
 const sheet=await inspector.boundingBox(),origin=await page.locator('.map-node').first().boundingBox();assert(sheet.y>400);assert(origin.y+origin.height<=sheet.y);
 const gap=await page.locator('.console-overview .panel-heading').evaluate(e=>e.getBoundingClientRect().bottom-e.querySelector('.panel-actions').getBoundingClientRect().bottom);assert(gap>=19);
 await context.close();
 // Real mobile viewport semantics and iPhone controls need their own context;
 // resizing a desktop context misses sticky overflow and inspector precedence.
 const phone=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,userAgent:'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 Version/18.0 Mobile Safari/604.1'}),mobile=await phone.newPage();
 await phone.route('**/research-data.json',r=>r.fulfill({json:source}));
 await mobile.goto(new URL('console.html?record=project%3Ainspector-fixture',base).href);await mobile.locator('html.console-inspector-docked').waitFor();
 const visibleSheet=await mobile.locator('.detail-panel').evaluate(e=>{const r=e.getBoundingClientRect();return {height:r.height,top:r.top,visible:e.contains(document.elementFromPoint(r.left+30,r.top+40))}});assert(visibleSheet.height<=844*.47);assert(visibleSheet.top>400);assert(visibleSheet.visible);
 await mobile.evaluate(()=>window.scrollTo({top:1100,behavior:'instant'}));await mobile.locator('.masthead-scroll-hidden').waitFor();await mobile.evaluate(()=>window.scrollTo({top:1000,behavior:'instant'}));await mobile.waitForFunction(()=>!document.querySelector('.masthead').classList.contains('masthead-scroll-hidden'));await mobile.waitForTimeout(220);assert.equal((await mobile.locator('.masthead').boundingBox()).y,0);
 assert(await mobile.locator('.masthead').evaluate(e=>e.contains(document.elementFromPoint(30,20))));await phone.close();
 const light=await browser.newContext({colorScheme:'light'}),reading=await light.newPage();
 for(const path of ['index.html','map.html','map3d.html','state.html','events.html','rejected.html']){await reading.goto(new URL(path,base).href);await reading.waitForLoadState('networkidle');assert.equal(await reading.locator('html').getAttribute('data-theme'),'light');const dark=await reading.locator('.panel,.topic-hub,.discovery-card,.home-lead-story,.motion-pulse,.motion-numbers,.metric-strip,.about-contract').evaluateAll(nodes=>nodes.filter(e=>getComputedStyle(e).backgroundImage!=='none').map(e=>e.className));assert.deepEqual(dark,[],path);}
 await light.close();console.log('PASS: inspector dock/resize/pop-out/restore, mobile origin visibility, category row, seven amber sections, fixed cube scale and light reading surfaces.');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
