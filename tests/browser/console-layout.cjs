/* Generated offline fixture only; optional live phases are simulated at the
   read-only HTTP boundary, with no authority writes or provider calls. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),assert=require('node:assert/strict');
const base=process.argv[2];
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const context=await browser.newContext({viewport:{width:1440,height:3200}}),page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message));await page.goto(new URL('console.html',base).href);await page.waitForLoadState('networkidle');
  const all=page.locator('#console-module-grid>.console-module');assert.equal(await all.count(),18);
  const initial=await all.evaluateAll(nodes=>nodes.map(e=>e.dataset.moduleKey));
  assert(await all.evaluateAll(nodes=>nodes.every(e=>e.dataset.consolePanelId==='001'?e.getBoundingClientRect().width===e.parentElement.getBoundingClientRect().width:e.style.getPropertyValue('--panel-slots')==='1')));
  const process=page.locator('[data-console-panel-id="002"]');await process.locator('.module-size').click();assert.notEqual(await process.evaluate(e=>e.style.getPropertyValue('--panel-slots')),'1');
  const from=await process.locator('.module-drag').boundingBox(),target=await all.nth(3).boundingBox();
  await page.mouse.move(from.x+from.width/2,from.y+from.height/2);await page.mouse.down();await page.mouse.move(target.x+target.width/2,target.y+target.height*.7,{steps:12});await page.mouse.up();
  const saved=await all.evaluateAll(nodes=>nodes.map(e=>e.dataset.moduleKey));assert.notDeepEqual(saved,initial);assert(saved.indexOf(await process.getAttribute('data-module-key'))>1);
  const width=await process.getAttribute('data-span');await page.reload();await page.waitForLoadState('networkidle');assert.deepEqual(await all.evaluateAll(nodes=>nodes.map(e=>e.dataset.moduleKey)),saved);assert.equal(await process.getAttribute('data-span'),width);
  const before=await page.evaluate(()=>performance.timeOrigin);await page.locator('#reset-console-layout').click();assert.equal(await page.evaluate(()=>performance.timeOrigin),before);
  assert.deepEqual(await all.evaluateAll(nodes=>nodes.map(e=>e.dataset.moduleKey)),initial);assert(await all.evaluateAll(nodes=>nodes.every(e=>e.dataset.consolePanelId==='001'?e.getBoundingClientRect().width===e.parentElement.getBoundingClientRect().width:e.style.getPropertyValue('--panel-slots')==='1')));
  for(const screen of [{width:1440,height:1800},{width:900,height:1200},{width:390,height:844}]){
   await page.setViewportSize(screen);
   await page.waitForTimeout(100);
   assert.equal(await page.locator('[data-console-panel-id="001"]').evaluate(e=>e.getBoundingClientRect().width),await page.locator('#console-module-grid').evaluate(e=>e.getBoundingClientRect().width));
   assert(await page.locator('.console-overview').evaluate(e=>{const outer=e.getBoundingClientRect();return [...e.children].every(child=>{const r=child.getBoundingClientRect();return r.left>=outer.left&&r.right<=outer.right+1})&&e.querySelector('.status-band').getBoundingClientRect().top>=e.querySelector('.panel-heading').getBoundingClientRect().bottom}));
   const misplaced=await page.locator('.console-panel-heading').evaluateAll(headings=>headings.filter(e=>{const title=e.querySelector('h1,h2,h3').getBoundingClientRect(),actions=e.querySelector('.panel-actions').getBoundingClientRect();return actions.top<title.bottom-1||Math.abs(actions.left-title.left)>2}).map(e=>e.innerText));assert.deepEqual(misplaced,[]);
  }
  let stage='context';
  await context.route('**/runtime.json',r=>r.fulfill({json:{mode:'standalone',state:'running',activity_schema:1,runtime_id:'offline-ui-fixture',capabilities:{live_activity:true},observed_at:new Date().toISOString(),activity:{active:true,stage,invocation_id:'fixture-request',coordinate_id:null,started_at:new Date().toISOString()}}}));
  await page.goto(new URL('console.html?panel=002',base).href);const canvas=page.locator('#process-field-canvas');await page.locator('canvas[data-provider-phase=context]').waitFor();
  stage='provider';await page.locator('canvas[data-provider-phase=request]').waitFor();assert.match(await page.locator('#process-field-trace').innerText(),/awaiting proposal/);
  const a=await canvas.evaluate(e=>e.toDataURL());await page.waitForTimeout(200);assert.notEqual(await canvas.evaluate(e=>e.toDataURL()),a);
  stage='governance';await page.locator('canvas[data-provider-phase=proposal]').waitFor();assert.match(await page.locator('#process-field-trace').innerText(),/proposal received/);
  stage='idle';await page.locator('canvas[data-provider-phase=idle]').waitFor();
  await page.screenshot({path:'/tmp/wake-process-controls.png'});assert.deepEqual(errors,[]);
  await context.close();
  const quiet=await browser.newContext({viewport:{width:1100,height:800},reducedMotion:'reduce'});
  await quiet.route('**/runtime.json',r=>r.fulfill({json:{mode:'standalone',state:'running',activity_schema:1,runtime_id:'quiet-fixture',capabilities:{live_activity:true},observed_at:new Date().toISOString(),activity:{active:true,stage:'provider',coordinate_id:null}}}));
  const q=await quiet.newPage();await q.goto(new URL('console.html?panel=002',base).href);await q.locator('canvas[data-provider-phase=request]').waitFor();
  const still=await q.locator('#process-field-canvas').evaluate(e=>e.toDataURL());await q.waitForTimeout(3300);
  assert.equal(await q.locator('#process-field-canvas').evaluate(e=>e.toDataURL()),still);
  await quiet.unroute('**/runtime.json');await quiet.route('**/runtime.json',r=>r.abort());await q.locator('canvas[data-provider-phase=idle]').waitFor();
  await quiet.close();console.log('PASS: #001 full-row and 17 panels minimum-width; saved #002 drag order/width; reset without navigation; controls below headings across widths; distinct live provider request/proposal/idle overlays.');
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
