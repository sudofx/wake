/* Full generated reader + app mount + real loopback backend, with fixture generation. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const assert=require('node:assert/strict'),path=require('node:path');
const base=process.argv[2];if(!base)throw Error('Usage: ask-bob-export.cjs <loopback origin>');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
 try{
  const page=await browser.newPage({viewport:{width:390,height:844}}),errors=[],requests=[];
  page.on('pageerror',error=>errors.push(error.message));page.on('request',request=>requests.push(new URL(request.url()).pathname));
  await page.route('**/*',route=>new URL(route.request().url()).origin===base?route.continue():route.abort());
  await page.goto(base+'/blog.html#blog/offline-integration-post',{waitUntil:'domcontentloaded'});
  await page.locator('.blog-reading h1').waitFor({timeout:10000}).catch(async error=>{throw Error(error.message+'\n'+JSON.stringify({errors,body:await page.locator('body').innerText(),requests}));});assert.equal(await page.locator('.blog-reading h1').innerText(),'Synthetic reader integration');
  await page.locator('.blog-reading .ask-bob > summary').waitFor();assert.equal(await page.locator('.ask-bob').getAttribute('open'),null);
  const displayed=await page.evaluate(async()=>{const data=await window.WakeData;return data.state.posts['offline-integration-post']._reader_article;});
  assert(/^[a-f0-9]{64}$/.test(displayed.hash));
  const opened=await page.evaluate(()=>JSON.parse(localStorage[Object.keys(localStorage).find(key=>key.startsWith('wake-ask-bob:'))]));
  assert.equal(opened.articles[0].hash,displayed.hash);assert(!Number.isNaN(Date.parse(opened.articles[0].encountered_at)));
  await page.locator('.ask-bob > summary').focus();await page.keyboard.press('Enter');
  await page.getByRole('combobox',{name:'Your understanding of this article version'}).selectOption('unsure');
  await page.getByRole('textbox',{name:'Your question'}).fill('OFFLINE-INTEGRATION-QUESTION: what does the synthetic result establish?');
  await page.getByRole('button',{name:'Ask Bob',exact:true}).click();await page.locator('.ask-bob-answer').waitFor();
  assert((await page.locator('.ask-bob-answer').innerText()).includes('OFFLINE-INTEGRATION-ANSWER'));
  assert.equal(await page.locator('.ask-bob-conversation a').count(),1);
  assert((await page.locator('.ask-bob-conversation a').innerText()).includes('S1'));
  await page.getByText('Response details',{exact:true}).click();assert((await page.locator('.ask-bob-conversation').innerText()).includes('Input bytes'));
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Generated reader fits phone width');
  const directory=process.env.WAKE_BROWSER_ARTIFACT_DIR||'/tmp';
  const phone=path.join(directory,'wake-ask-bob-integration-phone.png'),desktop=path.join(directory,'wake-ask-bob-integration-desktop.png');
  await page.locator('.ask-bob').scrollIntoViewIfNeeded();await page.screenshot({path:phone});
  await page.setViewportSize({width:1440,height:1000});await page.locator('.ask-bob').scrollIntoViewIfNeeded();await page.screenshot({path:desktop});
  assert(!requests.some(url=>/^\/(wake-data|research-data)\.json$/.test(url)),'No full archive fetch');
  assert(requests.includes('/reader-data.json'));assert(requests.some(url=>url.startsWith('/reader-records/posts/')),'Selected exact article loaded through reader transport');
  assert(requests.includes('/ask-bob/capabilities'));assert(requests.includes('/ask-bob'));
  assert.deepEqual(errors,[]);
  console.log(JSON.stringify({result:'PASS',checks:'actual exported page, normal app mount, exact detail transport, loopback HTTP, native invocation journal, fixture generation, no archive fetch, phone and desktop',article_hash:displayed.hash,screenshots:{phone,desktop}}));
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
