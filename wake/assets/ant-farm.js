/* Canvas owns the habitat; HTML owns controls, observations and conversation. */
(() => {
  'use strict';
  const drawAnt=window.WakeDrawAnt;
  const {Colony,WIDTH:W,HEIGHT:H,SURFACE:S}=window.WakeAntColony;
  const get=id=>document.getElementById(id),canvas=get('habitat'),ctx=canvas.getContext('2d');
  if(!ctx){get('scene-note').textContent='This browser cannot draw the habitat. Try a browser with Canvas support.';return;}
  const KEY='wake-ant-colony@2',reduced=matchMedia('(prefers-reduced-motion: reduce)');
  let colony,storageReady=true,storageConflict=false;
  try{const saved=localStorage.getItem(KEY);colony=saved?Colony.restore(JSON.parse(saved)):null;}catch{storageReady=false;}
  colony ||= new Colony(crypto.getRandomValues(new Uint32Array(1))[0]);
  let paused=reduced.matches,speed=1,showTrails=false,previous=0,accumulator=0,lastDraw=0,lastSave=0,lastUI=0,zoom=1;
  let width=0,height=0,dpr=1,cw=0,ch=0,terrainDirty=true,terrain=document.createElement('canvas'),soil=document.createElement('canvas');
  const soilPhoto=new Image();soilPhoto.onload=()=>resize();soilPhoto.src='backgrounds/ant-soil-v1.png';
  window.addEventListener('wake-ant-art-ready',()=>draw());
  const soilCtx=soil.getContext('2d'),ground=terrain.getContext('2d');
  function save(){if(storageConflict)return;try{localStorage.setItem(KEY,JSON.stringify(colony.save()));storageReady=true;}catch{storageReady=false;}updateStorage();}
  function updateStorage(){get('save-status').textContent=storageReady?'Progress stays in this browser. The colony rests when this page is hidden.':'Saving is unavailable. You can watch now; this colony may not survive a reload.';}
  function resize(){
    const box=canvas.getBoundingClientRect();width=box.width;height=box.height;dpr=Math.min(devicePixelRatio||1,2);cw=width/W;ch=height/H;
    for(const layer of [canvas,terrain,soil]){layer.width=Math.round(width*dpr);layer.height=Math.round(height*dpr);layer.getContext('2d').setTransform(dpr,0,0,dpr,0,0);}
    // Stable texture is a cached substrate, independent of the simulation RNG.
    const sky=soilCtx.createLinearGradient(0,0,0,height);sky.addColorStop(0,'#1b2c23');sky.addColorStop(S/H-.008,'#354b33');sky.addColorStop(S/H,'#74664a');sky.addColorStop(.28,'#756048');sky.addColorStop(.67,'#564431');sky.addColorStop(1,'#382f25');soilCtx.fillStyle=sky;soilCtx.fillRect(0,0,width,height);
    if(soilPhoto.complete&&soilPhoto.naturalWidth){soilCtx.drawImage(soilPhoto,0,S*ch,width,height-S*ch);const depth=soilCtx.createLinearGradient(0,S*ch,0,height);depth.addColorStop(0,'#20170a12');depth.addColorStop(1,'#090e10a0');soilCtx.fillStyle=depth;soilCtx.fillRect(0,S*ch,width,height-S*ch);}
    let textureSeed=colony.seed;const noise=()=>{textureSeed=(Math.imul(textureSeed,1664525)+1013904223)>>>0;return textureSeed/4294967296;};
    for(let i=0;i<width*height/120;i++){const x=noise()*width,y=S*ch+noise()*(height-S*ch),r=.3+noise()*1.4;soilCtx.fillStyle=noise()>.5?'#e0bf811a':'#1e1c2430';soilCtx.beginPath();soilCtx.ellipse(x,y,r*2,r,noise()*3,0,Math.PI*2);soilCtx.fill();}
    soilCtx.strokeStyle='#83945a';soilCtx.lineWidth=1;for(let x=0;x<width;x+=4+noise()*9){const y=(S-.3)*ch;soilCtx.beginPath();soilCtx.moveTo(x,y);soilCtx.lineTo(x-2+noise()*4,y-2-noise()*7);soilCtx.stroke();}
    terrainDirty=true;draw();
  }
  function updateTerrain(){
    ground.clearRect(0,0,width,height);ground.drawImage(soil,0,0,width,height);
    ground.strokeStyle='#29241d';ground.lineCap='round';ground.lineJoin='round';
    for(const node of colony.nodes){
      if(node.parent===null||node.kind==='surface')continue;const parent=colony.nodes[node.parent];
      ground.lineWidth=Math.min(cw,ch)*1.45;ground.beginPath();ground.moveTo(parent.x*cw,parent.y*ch);ground.lineTo(node.x*cw,node.y*ch);ground.stroke();
    }
    ground.fillStyle='#29241d';ground.beginPath();const home=colony.nodes[colony.nest];ground.ellipse(home.x*cw,home.y*ch,2.2*cw,1.3*ch,0,0,Math.PI*2);ground.fill();
    // A warm nest chamber makes the homeward traffic legible.
    const nest=ground.createRadialGradient(60*cw,25*ch,0,60*cw,25*ch,8*Math.max(cw,ch));nest.addColorStop(0,'#c7a36d18');nest.addColorStop(1,'#c7a36d00');ground.fillStyle=nest;ground.fillRect(56*cw,22*ch,8*cw,6*ch);terrainDirty=false;
  }
  const facings=new Map();
  function draw(){
    if(!width||!height)return;if(terrainDirty)updateTerrain();ctx.clearRect(0,0,width,height);ctx.drawImage(terrain,0,0,width,height);
    ctx.save();ctx.translate(width/2,height*.12);ctx.scale(zoom,zoom);ctx.translate(-width/2,-height*.12);
    // Draw the substrate inside the same camera transform as ants and trails.
    if(zoom!==1){ctx.clearRect(-width,-height,width*3,height*3);ctx.drawImage(terrain,0,0,width,height);}
    if(showTrails){ctx.lineCap='round';ctx.lineWidth=Math.min(cw,ch)*.65;for(let i=0;i<colony.trail.length;i++)if(colony.trail[i]>.15){const n=colony.nodes[i],p=colony.nodes[n.parent];if(!p)continue;ctx.strokeStyle=`rgba(168,207,144,${Math.min(.62,colony.trail[i]/17)})`;ctx.beginPath();ctx.moveTo(n.x*cw,n.y*ch);ctx.lineTo(p.x*cw,p.y*ch);ctx.stroke();}}
    for(const f of colony.food){if(!f.left)continue;const x=f.x*cw,y=f.y*ch;ctx.fillStyle='#b3bb68';for(let j=0;j<Math.min(10,Math.ceil(f.left/24));j++){const angle=j*2.4,r=2+Math.sqrt(j)*1.3;ctx.beginPath();ctx.ellipse(x+Math.cos(angle)*r,y+Math.sin(angle)*r,1.2,.8,j,0,7);ctx.fill();}}
    // Deposited grains accumulate at the entrance; excavation requires a return trip.
    ctx.fillStyle='#a7895c';for(let k=0;k<Math.min(70,colony.soilDelivered);k++){const x=(59+(k%2?1:-1)*(1+Math.sqrt(k)*.4))*cw,y=(S-.4-Math.floor(k/15)*.1)*ch;ctx.beginPath();ctx.ellipse(x,y,.7,.5,k,0,7);ctx.fill();}
    const r=Math.max(1.3,Math.min(3.7,Math.min(cw,ch)*.4));
    for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],length=Math.hypot(b.x-a.x,b.y-a.y)||1,t=Math.min(1,ant.phase+(!paused&&ant.phase<1?accumulator*ant.pace/length*(ant.carrying?.75:1):0));
      const lane=((ant.id%3)-1)*.13,spread=ant.id*2.39996,rad=.5+(ant.id%8)/8,offsetA=ant.from===colony.nest?1-t:0,offsetB=ant.cell===colony.nest?t:0,spreadWeight=offsetA+offsetB;
      const x=(a.x+(b.x-a.x)*t+Math.cos(spread)*rad*1.5*spreadWeight)*cw+Math.sin(ant.dir)*lane*cw,y=(a.y+(b.y-a.y)*t+Math.sin(spread)*rad*.65*spreadWeight)*ch-Math.cos(ant.dir)*lane*ch;
      const target=a===b?ant.dir:Math.atan2((b.y-a.y)*ch,(b.x-a.x)*cw),old=facings.get(ant.id)??target,turn=Math.atan2(Math.sin(target-old),Math.cos(target-old)),angle=old+Math.max(-.14,Math.min(.14,turn));facings.set(ant.id,angle);
      ctx.save();ctx.translate(x,y);ctx.rotate(angle);const moving=ant.phase<1,gait=moving?(ant.steps+t)*Math.PI*3:0;drawAnt(ctx,r,ant,gait,colony.time);ctx.restore();
    }
    ctx.restore();
    const vignette=ctx.createRadialGradient(width*.5,height*.45,width*.12,width*.5,height*.5,Math.max(width,height)*.75);vignette.addColorStop(0,'#0000');vignette.addColorStop(1,'#0a100e65');ctx.fillStyle=vignette;ctx.fillRect(0,0,width,height);
  }
  const elapsed=seconds=>`${Math.floor(seconds/60).toString().padStart(2,'0')}:${(seconds%60).toString().padStart(2,'0')}`;
  function updateUI(){
    const m=colony.metrics();get('colony-clock').textContent=elapsed(m.seconds);get('seed-label').textContent=`Colony ${colony.seed.toString(16).toUpperCase()} · saved on this device`;
    const values=[['Ants',m.ants],['Tunnel segments dug',m.dug],['Food brought home',m.delivered],['Depth in model units',m.depth],['Carrying food',m.carrying_food],['Soil pellets carried out',m.soil_pellets]];
    const nodes=values.map(([label,value])=>{const block=document.createElement('div'),dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=label;dd.textContent=value.toLocaleString();block.append(dt,dd);return block;});get('metrics').replaceChildren(...nodes);
    const old=colony.samples.find(s=>s.seconds>=m.seconds-120)||colony.samples[0],span=m.seconds-old.seconds;
    get('pattern').textContent=span>=10?`Over the last ${span} simulation seconds: ${m.dug-old.dug} new tunnel segments and ${m.delivered-old.delivered} food deliveries. ${m.carrying_soil} ants are carrying soil to the entrance. Turn on Trails to see where returning foragers leave signals.`:'The colony is settling in. Let it explore for a little while, then look for repeated routes and new branches.';
    if(!get('observations').hidden)get('accessible-status').textContent=`${m.ants} ants; ${m.dug} tunnel segments dug; ${m.delivered} food deliveries; ${elapsed(m.seconds)} elapsed.`;
  }
  function animate(now){
    requestAnimationFrame(animate);if(document.hidden){previous=0;return;}if(!previous)previous=now;const delta=Math.min(.25,(now-previous)/1000);previous=now;
    if(!paused){accumulator+=delta*speed;let steps=0;while(accumulator>=.1&&steps++<20){const before=colony.dug;colony.step();terrainDirty ||= before!==colony.dug;accumulator-=.1;}}
    if(now-lastDraw>=1000/30){draw();lastDraw=now;}if(now-lastUI>2000){updateUI();lastUI=now;}if(now-lastSave>10000){save();lastSave=now;}
  }
  function pause(value){paused=value;get('pause').textContent=paused?'Resume':'Pause';get('pause').setAttribute('aria-pressed',String(paused));get('scene-note').textContent=paused?'The colony is resting. Resume whenever you’re ready.':'Small steps. New tunnels. No master plan.';}
  get('pause').onclick=()=>pause(!paused);get('speed').onclick=()=>{speed=speed===1?2:speed===2?4:1;get('speed').textContent=speed+'×';get('speed').setAttribute('aria-label',`Simulation speed, currently ${speed} times`);};
  get('zoom').onclick=()=>{zoom=zoom===1?2:1;get('zoom').textContent=zoom===1?'Closer':'Wide view';draw();};
  get('trails').onclick=()=>{showTrails=!showTrails;get('trails').setAttribute('aria-pressed',String(showTrails));draw();};
  get('feed').onclick=()=>{const added=colony.addFood();save();updateUI();get('scene-note').textContent=added?'A few crumbs on the surface. Who will find them first?':'There are plenty of crumbs already. Give the foragers time to find them.';draw();};
  function observe(open){get('observations').hidden=!open;get('observe').setAttribute('aria-expanded',String(open));updateUI();if(open)get('close-observations').focus();else get('observe').focus();}
  get('observe').onclick=()=>observe(get('observations').hidden);get('close-observations').onclick=()=>observe(false);document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!get('observations').hidden)observe(false);});
  get('fullscreen').hidden=!document.fullscreenEnabled;get('fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await get('farm').requestFullscreen();}catch{get('scene-note').textContent='Full screen is unavailable in this browser.';}};
  get('new-colony').onclick=()=>{get('reset-confirm').hidden=false;};get('cancel-reset').onclick=()=>{get('reset-confirm').hidden=true;};
  get('confirm-reset').onclick=()=>{active?.abort();history=[];get('bob-log').replaceChildren();colony=new Colony(crypto.getRandomValues(new Uint32Array(1))[0]);accumulator=0;get('reset-confirm').hidden=true;save();resize();updateUI();};
  get('download').onclick=()=>{const url=URL.createObjectURL(new Blob([JSON.stringify(colony.observation(),null,2)],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download='ant-colony-observation.json';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
  let active=null,history=[];
  function message(who,text){const box=document.createElement('article'),label=document.createElement('strong'),p=document.createElement(who==='You'?'p':'div');label.textContent=who;p.textContent=text;if(who==='Bob')p.className='bob-markdown';box.append(label,p);get('bob-log').append(box);while(get('bob-log').children.length>12)get('bob-log').firstChild.remove();return p;}
  get('stop-bob').onclick=()=>active?.abort();
  get('bob-form').onsubmit=async event=>{
    event.preventDefault();if(active)return;const question=get('bob-question').value.trim();if(!question)return;
    const endpoint=window.WAKE_DEPLOYMENT?.ask_bob?.url||(location.hostname==='sudofx.github.io'?'https://wake-ask-bob.coolgrove68.chatgpt.site':null);
    if(!endpoint){get('bob-status').textContent='Bob connects on the published WAKE site. You can save this observation to review or share.';return;}
    const controller=new AbortController();active=controller;get('ask-bob').disabled=true;get('stop-bob').hidden=false;get('bob-status').textContent='Sharing a snapshot with Bob…';
    const sample=colony.observation(),asked=message('You',question),answer=message('Bob','');let output='',complete=false;
    const timer=setTimeout(()=>controller.abort(),60000);
    try{
      const response=await fetch(endpoint+'/v1/chat',{method:'POST',credentials:'omit',headers:{'Content-Type':'application/json'},body:JSON.stringify({mode:'ant-farm',observation:sample,question,history:history.slice(-4)}),signal:controller.signal});
      if(!response.ok){const detail=await response.json().catch(()=>({}));if(response.status===429)throw Error('Bob’s shared allowance is temporarily unavailable. Try later; your question is kept here.');if(detail.error==='invalid_request')throw Error('The answer service needs the ant farm update before Bob can read this sample.');throw Error('Bob is unavailable right now. Your question is kept here.');}
      const reader=response.body.getReader(),decoder=new TextDecoder();let buffer='';
      try{for(;;){const {value,done}=await reader.read();buffer+=decoder.decode(value||new Uint8Array(),{stream:!done});if(buffer.length>65536)throw Error('The reply was too large.');const lines=buffer.split('\n');buffer=lines.pop();for(const line of lines){if(!line.trim())continue;const packet=JSON.parse(line);if(packet.type==='delta'){output+=packet.text;WakeBobMarkdown.render(answer,output.slice(0,6000));}if(packet.type==='done'){complete=true;}if(packet.type==='error')throw Error('Bob’s reply was interrupted. Try again.');}if(done)break;}}finally{await reader.cancel().catch(()=>{});}
      if(!complete||!output)throw Error('Bob’s reply was interrupted. Try again.');history.push({question:question.slice(0,1000),answer:output.slice(0,2000)});history=history.slice(-4);get('bob-status').textContent=`Snapshot at ${elapsed(sample.metrics.seconds)} · ${sample.metrics.dug} tunnel segments dug. Bob does not see later changes until you ask again.`;
    }catch(error){get('bob-status').textContent=controller.signal.aborted?'Stopped. Your question is kept here.':error.message;if(!output)answer.parentElement.remove();asked.parentElement.dataset.incomplete='true';}
    finally{clearTimeout(timer);if(active===controller)active=null;get('ask-bob').disabled=false;get('stop-bob').hidden=true;}
  };
  document.addEventListener('visibilitychange',()=>{previous=0;accumulator=0;if(document.hidden)save();});window.addEventListener('pagehide',save);window.addEventListener('resize',resize);
  reduced.addEventListener('change',event=>{if(event.matches)pause(true);});
  // Multiple tabs must not silently overwrite the same colony.
  window.addEventListener('storage',event=>{if(event.key===KEY){pause(true);storageConflict=true;get('save-status').textContent='Another tab updated this colony. Reload to pick up its progress.';}});
  pause(paused);updateStorage();resize();updateUI();requestAnimationFrame(animate);
})();
