/* Pixel connectivity of the real cached terrain, including Safari's Canvas renderer. */
const {chromium,webkit}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const assets=path.resolve(__dirname,'../../wake/assets'),caretaker=require('../../scripts/bob_ant_farm.cjs');
const revision='a'.repeat(40),first=caretaker.advancePacket(caretaker.bootstrap({sourceRevision:revision,at:'2026-10-26T18:00:00Z'}),{sourceRevision:revision,at:'2026-10-26T19:00:00Z',ticks:6000});
const packet=process.argv[2]?JSON.parse(fs.readFileSync(process.argv[2],'utf8')):caretaker.advancePacket(first,{sourceRevision:revision,at:'2026-10-26T20:00:00Z',ticks:6000});
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');
 if(url.pathname==='/bob-ant-farm.json'){res.setHeader('Content-Type','application/json');return res.end(JSON.stringify(packet));}
 const file=path.join(assets,url.pathname);if(!file.startsWith(assets+path.sep)){res.writeHead(404);return res.end();}
 fs.readFile(file,(error,data)=>{if(error){res.writeHead(404);return res.end();}
  if(url.pathname==='/ant-farm.html')data=data.toString().replace('<head>','<head><script>window.WAKE_DEPLOYMENT={bob_ant_farm:{preview_path:"bob-ant-farm.json"}};</script>');
  res.setHeader('Content-Type',file.endsWith('.js')?'text/javascript':file.endsWith('.css')?'text/css':file.endsWith('.html')?'text/html':'application/octet-stream');res.end(data);
 });
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 try{for(const [name,engine] of [['chromium',chromium],['webkit',webkit]]){
  const browser=await engine.launch({headless:true,...(name==='chromium'&&process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});
  try{for(const [width,height,ratio] of [[1200,900,1],[390,844,3],[390,844,8]]){
   const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:ratio,isMobile:width<600,hasTouch:width<600});
   const errors=[];page.on('pageerror',error=>errors.push(error.message));
   await page.addInitScript(()=>{
    // Observe actual offscreen pixels, before ants can obscure a broken join.
    window.__terrainBuffers=[];const create=document.createElement.bind(document);
    document.createElement=function(tag,...args){const element=create(tag,...args);if(tag==='canvas')__terrainBuffers.push(element);return element;};
   });
   if(process.env.ANT_FARM_URL)await page.route('**/bob-ant-farm/farm.json',route=>route.fulfill({json:packet}));
   await page.goto(process.env.ANT_FARM_URL||`http://127.0.0.1:${server.address().port}/ant-farm.html`);
   await page.locator('#habitat').waitFor({state:'visible'});await page.locator('#pause').click();
   const result=await page.evaluate(state=>{
    const canvas=__terrainBuffers[0],ctx=canvas.getContext('2d'),w=canvas.width,h=canvas.height;
    const pixels=ctx.getImageData(0,0,w,h).data,cw=w/120,ch=h/96,home=state.nodes[state.nest];
    const visited=new Uint8Array(w*h),queue=new Int32Array(w*h);let head=0,tail=0;
    const pass=i=>i>=0&&i<w*h&&pixels[i*4+3]>240&&pixels[i*4]<220&&pixels[i*4+1]<205&&pixels[i*4+2]<174;
    const start=Math.floor(home.y*ch)*w+Math.floor(home.x*cw);visited[start]=1;queue[tail++]=start;
    while(head<tail){const i=queue[head++];for(const next of [i-w,i+w,...(i%w?[i-1]:[]),...(i%w<w-1?[i+1]:[])]){
     if(!visited[next]&&pass(next)){visited[next]=1;queue[tail++]=next;}
    }}
    const disconnected=[];let checked=0;
    for(let id=117;id<state.nodes.length;id++){
     const node=state.nodes[id];if(node.y<26)continue;checked++;
     if(!visited[Math.floor(node.y*ch)*w+Math.floor(node.x*cw)])disconnected.push(id);
    }
    return{checked,disconnected,pixels:w*h};
   },packet.replay.start);
   assert(result.checked>5,'Fixture includes multiple underground bends and branches');
   assert.deepEqual(result.disconnected,[],`${name} ${width}px at ${ratio}×: every underground passage must connect to the nest`);
   assert(result.pixels<4100000,'Pinch-scale detail keeps the rendering budget');assert.deepEqual(errors,[]);
   if(process.env.TUNNEL_SCREENSHOT&&name==='webkit'&&ratio===3)await page.screenshot({path:process.env.TUNNEL_SCREENSHOT});
   console.log(JSON.stringify({browser:name,viewport:width,pixelRatio:ratio,connectedNodes:result.checked}));await page.close();
  }}finally{await browser.close();}
 }}finally{server.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
