/* Read-only exported site with populated application data. No provider calls.
   Contrast is sampled from real rendered text, including inherited translucent
   surfaces. Image/gradient text is reviewed visually instead of guessing pixels. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright'),assert=require('node:assert/strict');
const base=process.argv[2];
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});try{
for(const width of [1440,390]){
 const context=await browser.newContext({viewport:{width,height:1000},colorScheme:'light'}),page=await context.newPage(),errors=[];
 if(process.env.WAKE_DAYLIGHT_STYLESHEET)await context.route("**/console-light.css*",r=>r.fulfill({contentType:"text/css",body:require("node:fs").readFileSync(process.env.WAKE_DAYLIGHT_STYLESHEET,"utf8")}));page.on('pageerror',e=>errors.push(e.message));
 for(const route of ['home','journal','discoveries','topics','blog','projects','lab','metrics','evidence','history','about']){
  await page.goto(new URL('index.html#'+route,base).href);await page.waitForLoadState('networkidle');await page.waitForTimeout(100);
  assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
  if(route==='journal'){await page.locator('.help-trigger:visible').first().click();await page.locator('#help-panel').waitFor();}
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true,`${width} ${route}: horizontal overflow`);
  const failures=await page.evaluate(()=>{
   const rgb=value=>{if(value.startsWith('color(srgb'))return value.match(/[\d.]+/g).map(Number).map((n,i)=>i<3?n*255:n);return value.match(/[\d.]+/g)?.map(Number)||[0,0,0,0]},lum=c=>c.slice(0,3).map(n=>n/255).map(n=>n<=.04045?n/12.92:((n+.055)/1.055)**2.4).reduce((s,n,i)=>s+n*[.2126,.7152,.0722][i],0),mix=(fg,bg)=>fg.slice(0,3).map((n,i)=>n*(fg[3]??1)+bg[i]*(1-(fg[3]??1)));
   const result=[];
   for(const el of document.querySelectorAll('main *,footer *,#help-panel *')){
    if(![...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim())||el.closest('svg,[aria-hidden=true]')||!el.getClientRects().length)continue;
    const style=getComputedStyle(el),fg=rgb(style.color);if(style.visibility==='hidden'||Number(style.opacity)===0||(fg[3]??1)===0)continue;
    const chain=[];for(let p=el;p;p=p.parentElement)chain.unshift(p);
    if(chain.some(p=>getComputedStyle(p).backgroundImage.includes('url(')))continue;
    let bg=[255,255,255];for(const p of chain)bg=mix(rgb(getComputedStyle(p).backgroundColor),bg);
    const l=[lum(mix(fg,bg)),lum(bg)].sort((a,b)=>a-b),ratio=(l[1]+.05)/(l[0]+.05),size=parseFloat(style.fontSize),large=size>=24||(size>=18.66&&Number(style.fontWeight)>=700);
    if(ratio<(large?3:4.5)-.05)result.push({tag:el.tagName,class:el.className,text:el.textContent.trim().slice(0,55),color:style.color,bg,ratio:ratio.toFixed(2)});
   }
   return result;
  });
  assert.deepEqual(failures,[],`${width} ${route}: rendered text contrast`);
  if(await page.locator('#help-close').isVisible())await page.locator('#help-close').click();
 }
 await page.goto(new URL('index.html#home',base).href);await page.waitForLoadState('networkidle');
 assert.equal(await page.locator('.nebula-pillars article').count(),3);
 assert.equal(await page.locator('.nebula-explore-card').count(),4);
 assert.equal(await page.locator('.nebula-explore-copy').first().evaluate(e=>getComputedStyle(e).backgroundImage),'none');
 await page.screenshot({path:`/tmp/wake-daylight-home-${width}.png`,fullPage:true});assert.deepEqual(errors,[]);await context.close();
}
console.log('PASS: populated main-page routes in daylight at desktop/phone sizes; rendered text contrast, no horizontal overflow, complete home surfaces and no script errors.');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
