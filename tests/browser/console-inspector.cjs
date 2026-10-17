/* Read-only export: selection fills #014 without changing layout or scroll. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),assert=require('node:assert/strict');
const base=process.argv[2];
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});try{
 for(const viewport of [{width:1440,height:1000},{width:390,height:844}]){
  const context=await browser.newContext({viewport,hasTouch:viewport.width===390}),page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  const source=await context.request.get(new URL('research-data.json',base).href).then(r=>r.json());
  source.graph.nodes=[{id:'project:inspector-fixture',kind:'project',title:'Inspector fixture',detail:{id:'inspector-fixture',status:'active',question:'A readable test record'}}];source.graph.edges=[];
  await context.route(/\/research-(?:data|overview)\.json$/,r=>r.fulfill({json:source}));
  await page.goto(new URL('console.html',base).href);await page.waitForLoadState('networkidle');
  const inspector=page.locator('[data-console-panel-id="014"]');
  assert(await inspector.isVisible());assert(await inspector.locator('.empty').isVisible());
  const order=()=>page.locator('#console-module-grid>.console-module').evaluateAll(nodes=>nodes.map(e=>e.dataset.consolePanelId));
  const initial=await order();assert.equal(initial.indexOf('014'),initial.indexOf('013')+1);assert.equal(initial.indexOf('015'),initial.indexOf('014')+1);
  assert.equal(await inspector.evaluate(e=>getComputedStyle(e).position),'relative');
  assert.equal(await inspector.locator('.module-drag').count(),1);assert.equal(await inspector.locator('.panel-popout').count(),1);
  for(const top of [600,480,800,400]){
   await page.evaluate(top=>window.scrollTo({top,behavior:'instant'}),top);await page.waitForTimeout(200);
   assert.equal((await page.locator('.masthead').boundingBox()).y,0);assert.equal(await page.evaluate(()=>scrollY),top);
  }
  const position=await inspector.boundingBox();
  const before=await page.evaluate(()=>scrollY);
  await page.evaluate(()=>window.dispatchEvent(new CustomEvent('wake-process-record-select',{detail:'project:inspector-fixture'})));
  await inspector.locator('.detail-title').waitFor();
  assert.match(await inspector.innerText(),/Inspector fixture/);assert.equal(await page.evaluate(()=>scrollY),before);
  assert.deepEqual(await order(),initial);assert.equal((await inspector.boundingBox()).x,position.x);assert.equal(await inspector.evaluate(e=>getComputedStyle(e).position),'relative');assert.equal(await page.locator('html.console-inspector-docked').count(),0);
  const [popup]=await Promise.all([page.waitForEvent('popup'),inspector.locator('.panel-popout').click()]);
  await popup.locator('.panel-popout-target').waitFor();assert.equal(await popup.locator('.masthead').isVisible(),false);
  assert(await popup.locator('[data-console-panel-id="014"].panel-popout-target').isVisible());
  await page.waitForFunction(()=>document.querySelector('[data-console-panel-id="014"]').classList.contains('panel-popped-out'));
  assert.equal(await inspector.isVisible(),false);await popup.close();
  await page.waitForFunction(()=>!document.querySelector('[data-console-panel-id="014"]').classList.contains('panel-popped-out'));
  assert(await inspector.isVisible());assert.deepEqual(await order(),initial);
  if(viewport.width===1440){
   await page.evaluate(()=>{const key='wake-console-workspace-v3',state={order:[...document.querySelectorAll('.console-module')].filter(e=>e.dataset.consolePanelId!=='014').map(e=>e.dataset.moduleKey),panels:{}};localStorage.setItem(key,JSON.stringify(state));});
   await page.reload();await page.waitForLoadState('networkidle');assert.deepEqual(await order(),initial);
   await page.evaluate(()=>{const key='wake-console-workspace-v3',state=JSON.parse(localStorage.getItem(key)),panel=document.querySelector('[data-console-panel-id="014"]');state.order=state.order.filter(key=>key!==panel.dataset.moduleKey);state.order.push(panel.dataset.moduleKey);localStorage.setItem(key,JSON.stringify(state));});
   await page.reload();await page.waitForLoadState('networkidle');assert.equal((await order()).at(-1),'014');
   await page.locator('#reset-console-layout').click();assert.deepEqual(await order(),initial);
   // A large preceding card must not let later story cards backfill a grid hole.
   await page.locator('[data-console-panel-id="013"] .module-size').click();
   const visual=await page.locator('#console-module-grid>.console-module').evaluateAll(nodes=>nodes.map(e=>({id:e.dataset.consolePanelId,r:e.getBoundingClientRect()})).sort((a,b)=>a.r.top-b.r.top||a.r.left-b.r.left).map(e=>e.id));
   assert.deepEqual(visual,initial);
   const node=page.locator('#research-map [data-record="project:inspector-fixture"]');
   await node.scrollIntoViewIfNeeded();
   const beforeClick=await inspector.boundingBox(),scroll=await page.evaluate(()=>scrollY);
   await node.dispatchEvent('click');
   assert.deepEqual(await order(),initial);assert.equal((await inspector.boundingBox()).x,beforeClick.x);assert.equal(await inspector.evaluate(e=>getComputedStyle(e).position),'relative');assert.equal(await page.evaluate(()=>scrollY),scroll);
   await page.locator('#reset-console-layout').click();assert.deepEqual(await order(),initial);
  }
  await page.screenshot({path:`/tmp/wake-sunday-console-${viewport.width}.png`});assert.deepEqual(errors,[]);await context.close();
 }
 console.log('PASS: ordinary #014 module on desktop/phone; selection preserves scroll/order; explicit pop-out/restore, saved placement and reset; continuously visible masthead.');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
