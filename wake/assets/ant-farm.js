/* Canvas owns the habitat; HTML owns controls, observations and conversation. */
(() => {
  'use strict';
  const drawAnt=window.WakeDrawAnt;
  const {Colony,WIDTH:W,HEIGHT:H,SURFACE:S}=window.WakeAntColony;
  const get=id=>document.getElementById(id),canvas=get('habitat'),ctx=canvas.getContext('2d');
  if(!ctx){get('scene-note').textContent='This browser cannot draw the habitat. Try a browser with Canvas support.';return;}
  const KEY='wake-ant-colony@2',reduced=matchMedia('(prefers-reduced-motion: reduce)');
  let colony,storageReady=true,storageConflict=false,unreadableSave=false;
  try{const saved=localStorage.getItem(KEY);colony=saved?Colony.restore(JSON.parse(saved)):null;}catch{storageReady=false;unreadableSave=true;}
  colony ||= new Colony(crypto.getRandomValues(new Uint32Array(1))[0]);
  let paused=false,speed=1,showTrails=true,previous=0,accumulator=0,lastDraw=0,lastSave=0,lastUI=0,zoom=1,cameraX=.5,cameraY=.5,selectedId=null,following=false,antSignature='';
  let width=0,height=0,dpr=1,cw=0,ch=0,terrainDirty=true,needsDraw=true,frameInterval=1000/24,terrain=document.createElement('canvas'),soil=document.createElement('canvas');
  window.addEventListener('wake-ant-art-ready',()=>{needsDraw=true;});
  const soilCtx=soil.getContext('2d'),ground=terrain.getContext('2d');
  function save(){if(storageConflict||unreadableSave)return;try{localStorage.setItem(KEY,JSON.stringify(colony.save()));storageReady=true;}catch{storageReady=false;}updateStorage();}
  function updateStorage(){get('save-status').textContent=unreadableSave?'Your saved colony could not be read and has been kept untouched. This temporary colony will not replace it.':storageConflict?'Another tab updated this colony. Reload to pick up its progress.':storageReady?'Progress stays in this browser. The colony rests when this page is hidden.':'Saving is unavailable. You can watch now; this colony may not survive a reload.';}
  function resize(){
    const box=canvas.getBoundingClientRect();width=box.width;height=box.height;const mobile=matchMedia('(pointer: coarse)').matches||width<=600;dpr=Math.min(devicePixelRatio||1,mobile?1.25:1.5,Math.sqrt(1500000/(width*height)));frameInterval=1000/(reduced.matches?10:mobile?20:24);cw=width/W;ch=height/H;
    for(const layer of [canvas,terrain,soil]){layer.width=Math.round(width*dpr);layer.height=Math.round(height*dpr);layer.getContext('2d').setTransform(dpr,0,0,dpr,0,0);}
    // Drawn colour fields stay quiet at every zoom; no enlarged photographic grains.
    const sky=soilCtx.createLinearGradient(0,0,0,S*ch);sky.addColorStop(0,'#20342a');sky.addColorStop(1,'#526446');soilCtx.fillStyle=sky;soilCtx.fillRect(0,0,width,S*ch);
    const earth=soilCtx.createLinearGradient(0,S*ch,0,height);earth.addColorStop(0,'#eadbb9');earth.addColorStop(1,'#d8c8a7');soilCtx.fillStyle=earth;soilCtx.fillRect(0,S*ch,width,height-S*ch);
    terrainDirty=true;draw();
  }
  function updateTerrain(){
    ground.clearRect(0,0,width,height);ground.drawImage(soil,0,0,width,height);
    ground.strokeStyle='#c9b68f';ground.lineCap='round';ground.lineJoin='round';
    for(const node of colony.nodes){
      if(node.parent===null||node.kind==='surface')continue;const parent=colony.nodes[node.parent];
      ground.lineWidth=Math.min(cw,ch)*1.45;ground.beginPath();ground.moveTo(parent.x*cw,parent.y*ch);ground.lineTo(node.x*cw,node.y*ch);ground.stroke();
    }
    ground.fillStyle='#c9b68f';ground.beginPath();const home=colony.nodes[colony.nest];ground.ellipse(home.x*cw,home.y*ch,2.2*cw,1.3*ch,0,0,Math.PI*2);ground.fill();
    // A warm nest chamber makes the homeward traffic legible.
    const nest=ground.createRadialGradient(home.x*cw,home.y*ch,0,home.x*cw,home.y*ch,8*Math.max(cw,ch));nest.addColorStop(0,'#c7a36d18');nest.addColorStop(1,'#c7a36d00');ground.fillStyle=nest;ground.fillRect((home.x-4)*cw,(home.y-3)*ch,8*cw,6*ch);terrainDirty=false;
  }
  const facings=new Map(),strides=new Map();
  function draw(){
    if(!width||!height)return;needsDraw=false;if(terrainDirty)updateTerrain();ctx.clearRect(0,0,width,height);
    // Sample only the visible terrain into the fixed viewport before transforming ants.
    ctx.drawImage(terrain,(cameraX-.5/zoom)*width*dpr,(cameraY-.5/zoom)*height*dpr,width*dpr/zoom,height*dpr/zoom,0,0,width,height);
    ctx.save();ctx.translate(width/2,height/2);ctx.scale(zoom,zoom);ctx.translate(-cameraX*width,-cameraY*height);
    if(showTrails){ctx.lineCap='round';ctx.lineWidth=Math.min(cw,ch)*.65;for(let i=0;i<colony.trail.length;i++)if(colony.trail[i]>.15){const n=colony.nodes[i],p=colony.nodes[n.parent];if(!p)continue;ctx.strokeStyle=`rgba(117,44,190,${Math.min(.85,.2+colony.trail[i]/15)})`;ctx.beginPath();ctx.moveTo(n.x*cw,n.y*ch);ctx.lineTo(p.x*cw,p.y*ch);ctx.stroke();}}
    for(const f of colony.food){if(!f.left)continue;const x=f.x*cw,y=f.y*ch;ctx.fillStyle='#b3bb68';for(let j=0;j<Math.min(10,Math.ceil(f.left/24));j++){const angle=j*2.4,r=2+Math.sqrt(j)*1.3;ctx.beginPath();ctx.ellipse(x+Math.cos(angle)*r,y+Math.sin(angle)*r,1.2,.8,j,0,7);ctx.fill();}}
    // Deposited grains accumulate at the entrance; excavation requires a return trip.
    ctx.fillStyle='#a7895c';for(let k=0;k<Math.min(70,colony.soilDelivered);k++){const x=(colony.nodes[colony.exit].x-1+(k%2?1:-1)*(1+Math.sqrt(k)*.4))*cw,y=(S-.4-Math.floor(k/15)*.1)*ch;ctx.beginPath();ctx.ellipse(x,y,.7,.5,k,0,7);ctx.fill();}
    const r=Math.max(1.3,Math.min(3.7,Math.min(cw,ch)*.4));
    for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],length=Math.hypot(b.x-a.x,b.y-a.y)||1,t=Math.min(1,ant.phase+(!paused&&ant.wait<=0&&ant.phase<1?accumulator*ant.pace/length*(ant.carrying?.75:1):0));
      const lane=((ant.id%3)-1)*.13,spread=ant.id*2.39996,rad=.5+(ant.id%8)/8,offsetA=ant.from===colony.nest?1-t:0,offsetB=ant.cell===colony.nest?t:0,spreadWeight=offsetA+offsetB;
      const x=(a.x+(b.x-a.x)*t+Math.cos(spread)*rad*1.5*spreadWeight)*cw+Math.sin(ant.dir)*lane*cw,y=(a.y+(b.y-a.y)*t+Math.sin(spread)*rad*.65*spreadWeight)*ch-Math.cos(ant.dir)*lane*ch;
      const moving=ant.phase<1&&ant.wait<=0,scanning=!moving&&ant.work<0&&ant.wait>.8?[0,.35,0,-.3][Math.floor(colony.time*.7+ant.id*1.61)%4]:0;
      const target=(a===b?ant.dir:Math.atan2((b.y-a.y)*ch,(b.x-a.x)*cw))+scanning,old=facings.get(ant.id)??target,turn=Math.atan2(Math.sin(target-old),Math.cos(target-old)),angle=old+Math.max(-.23,Math.min(.23,turn));facings.set(ant.id,angle);
      let pose=strides.get(ant.id);if(!pose)pose={x,y,gait:ant.id*2.39996};
      const distance=Math.hypot(x-pose.x,y-pose.y);if(moving&&distance<Math.max(cw,ch)*2)pose.gait+=distance/r*Math.PI*.55;pose.x=x;pose.y=y;strides.set(ant.id,pose);
      const margin=r*5;
      if(x<(cameraX-.5/zoom)*width-margin||x>(cameraX+.5/zoom)*width+margin||y<(cameraY-.5/zoom)*height-margin||y>(cameraY+.5/zoom)*height+margin)continue;
      ctx.save();ctx.translate(x,y);ctx.rotate(angle+(moving?Math.sin(pose.gait*2)*.018:0));drawAnt(ctx,r,{...ant,moving,turn},pose.gait,colony.time+(!paused?accumulator:0));ctx.restore();
      if(ant.id===selectedId){ctx.strokeStyle='#6925ac';ctx.lineWidth=1/zoom;ctx.beginPath();ctx.arc(x,y,r*5,0,Math.PI*2);ctx.stroke();ctx.fillStyle='#351448';ctx.font=`${11/zoom}px system-ui`;ctx.fillText('#'+ant.id,x+r*6,y-r*3);}
    }
    ctx.restore();
    const vignette=ctx.createRadialGradient(width*.5,height*.45,width*.12,width*.5,height*.5,Math.max(width,height)*.75);vignette.addColorStop(0,'#0000');vignette.addColorStop(1,'#5d492018');ctx.fillStyle=vignette;ctx.fillRect(0,0,width,height);
  }
  const elapsed=seconds=>`${Math.floor(seconds/60).toString().padStart(2,'0')}:${(seconds%60).toString().padStart(2,'0')}`;
  function updateUI(){
    const m=colony.metrics();get('colony-clock').textContent=elapsed(m.seconds);get('seed-label').textContent=`Colony ${colony.seed.toString(16).toUpperCase()} · saved on this device`;
    const values=[['Living ants',m.ants],['Brood developing',m.brood],['Born',m.born],['Died naturally',m.deaths],['Entrances',m.entrances],['Active digging sites',m.tunnel_tips],['Tunnel segments dug',m.dug],['Food brought home',m.delivered],['Food in nest',m.food_reserve],['Soil pellets carried out',m.soil_pellets]];
    const nodes=values.map(([label,value])=>{const block=document.createElement('div'),dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=label;dd.textContent=value.toLocaleString();block.append(dt,dd);return block;});get('metrics').replaceChildren(...nodes);
    const old=colony.samples.find(s=>s.seconds>=m.seconds-120)||colony.samples[0],span=m.seconds-old.seconds;
    get('pattern').textContent=span>=10?`Over the last ${span} simulation seconds: ${m.dug-old.dug} new tunnel segments and ${m.delivered-old.delivered} food deliveries. ${m.carrying_soil} ants are carrying soil to the entrance. Turn on Trails to see where returning foragers leave signals.`:'The colony is settling in. Let it explore for a little while, then look for repeated routes and new branches.';
    if(!get('observations').hidden)get('accessible-status').textContent=`${m.ants} ants; ${m.dug} tunnel segments dug; ${m.delivered} food deliveries; ${elapsed(m.seconds)} elapsed.`;
    const signature=colony.ants.map(a=>a.id).join(',');
    if(signature!==antSignature){antSignature=signature;const live=new Set(colony.ants.map(a=>a.id));for(const id of facings.keys())if(!live.has(id)){facings.delete(id);strides.delete(id);}const options=colony.ants.map(a=>{const o=document.createElement('option');o.value=a.id;o.textContent='#'+a.id;return o;});const empty=document.createElement('option');empty.value='';empty.textContent='Choose an ant';get('ant-select').replaceChildren(empty,...options);get('ant-select').value=selectedId===null?'':String(selectedId);}
    const ant=colony.ants.find(a=>a.id===selectedId),dead=colony.recentDeaths.find(a=>a.id===selectedId);
    get('ant-detail').textContent=ant?`Ant ${colony.seed.toString(16).toUpperCase()}:#${ant.id} · ${ant.role==='dig'?'digger':ant.role==='forage'?'forager':'resting worker'} · age ${elapsed(Math.floor(colony.time-ant.bornAt))} · ${ant.work>=0?'excavating':ant.carrying===2?'carrying soil':ant.carrying===1?'carrying food':ant.wait>0?'resting':'walking'}.`:dead?`Ant #${dead.id} died of ${dead.reason} at age ${elapsed(dead.age)}.`:selectedId!==null?`Ant #${selectedId} is no longer alive.`:'Choose an ant or tap one in the habitat. Its number stays with it for life.';
    get('follow-ant').disabled=!ant;get('follow-ant').setAttribute('aria-pressed',String(following&&!!ant));if(!ant)following=false;
  }
  function animate(now){
    requestAnimationFrame(animate);if(document.hidden){previous=0;return;}if(!previous)previous=now;const delta=Math.min(.25,(now-previous)/1000);previous=now;
    if(!paused){accumulator=Math.min(2,accumulator+delta*speed*4);let steps=0;while(accumulator>=.1&&steps++<20){const before=colony.dug;colony.step();terrainDirty ||= before!==colony.dug;accumulator-=.1;}}
    if(following){const a=colony.ants.find(a=>a.id===selectedId);if(a){const from=colony.nodes[a.from],to=colony.nodes[a.cell];cameraX=(from.x+(to.x-from.x)*a.phase)/W;cameraY=(from.y+(to.y-from.y)*a.phase)/H;cameraClamp();}}
    if(now-lastDraw>=frameInterval&&(!paused||needsDraw)){draw();lastDraw=now;}if(now-lastUI>2000){updateUI();lastUI=now;}if(now-lastSave>10000){save();lastSave=now;}
  }
  function pause(value){paused=value;get('pause').textContent=paused?'Resume':'Pause';get('pause').setAttribute('aria-pressed',String(paused));get('scene-note').textContent=paused?'The colony is resting. Resume whenever you’re ready.':'Small steps. New tunnels. No master plan.';}
  get('pause').onclick=()=>pause(!paused);get('speed').onclick=()=>{speed=speed===1?2:speed===2?4:1;get('speed').textContent=speed+'×';get('speed').setAttribute('aria-label',`Simulation speed, currently ${speed} times`);};
  get('ant-select').onchange=()=>{selectedId=get('ant-select').value===''?null:Number(get('ant-select').value);following=false;updateUI();needsDraw=true;};
  get('follow-ant').onclick=()=>{following=!following;if(following&&zoom<2)setZoom(2);updateUI();needsDraw=true;};
  function cameraClamp(){cameraX=Math.max(.5/zoom,Math.min(1-.5/zoom,cameraX));cameraY=Math.max(.5/zoom,Math.min(1-.5/zoom,cameraY));}
  function setZoom(value,point){const next=Math.max(1,Math.min(4,value));if(point){cameraX+=(point.x/width-.5)*(1/zoom-1/next);cameraY+=(point.y/height-.5)*(1/zoom-1/next);}else if(zoom===1&&next>1){const home=colony.nodes[colony.nest];cameraX=home.x/W;cameraY=Math.max(.2,home.y/H-.06);}zoom=next;cameraClamp();get('zoom').textContent='Closer +';get('zoom').disabled=zoom>=4;get('zoom-out').disabled=zoom<=1;get('zoom-view').textContent=zoom.toFixed(zoom%1?1:0)+'× view';get('scene-note').textContent=zoom>1?'Drag to explore · pinch or scroll to zoom · Fit returns to the whole colony.':'Small steps. New tunnels. No master plan.';needsDraw=true;}
  get('zoom').onclick=()=>setZoom(zoom*2);get('zoom-out').onclick=()=>setZoom(zoom/2);get('zoom-fit').onclick=()=>{cameraX=.5;cameraY=.5;setZoom(1);};
  const pointers=new Map();let gesture=null;
  canvas.addEventListener('pointerdown',event=>{canvas.setPointerCapture(event.pointerId);pointers.set(event.pointerId,{x:event.clientX,y:event.clientY,startX:event.clientX,startY:event.clientY});gesture=null;});
  canvas.addEventListener('pointermove',event=>{if(!pointers.has(event.pointerId))return;const previous=pointers.get(event.pointerId);pointers.set(event.pointerId,{...previous,x:event.clientX,y:event.clientY});if(pointers.size===1){if(Math.hypot(event.clientX-previous.startX,event.clientY-previous.startY)>6)following=false;cameraX-=(event.clientX-previous.x)/width/zoom;cameraY-=(event.clientY-previous.y)/height/zoom;cameraClamp();needsDraw=true;}else{const [a,b]=[...pointers.values()],distance=Math.hypot(a.x-b.x,a.y-b.y),box=canvas.getBoundingClientRect();if(gesture)setZoom(zoom*distance/gesture,{x:(a.x+b.x)/2-box.left,y:(a.y+b.y)/2-box.top});gesture=distance;}});
  for(const name of ['pointerup','pointercancel','lostpointercapture'])canvas.addEventListener(name,event=>{
    const down=pointers.get(event.pointerId);
    if(name==='pointerup'&&pointers.size===1&&down&&Math.hypot(event.clientX-down.startX,event.clientY-down.startY)<6){
      const box=canvas.getBoundingClientRect(),x=(cameraX+(event.clientX-box.left-width/2)/width/zoom)*W,y=(cameraY+(event.clientY-box.top-height/2)/height/zoom)*H;
      let nearest=null,distance=14;
      for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],d=Math.hypot((a.x+(b.x-a.x)*ant.phase-x)*cw*zoom,(a.y+(b.y-a.y)*ant.phase-y)*ch*zoom);if(d<distance){nearest=ant;distance=d;}}
      if(nearest){selectedId=nearest.id;get('ant-select').value=String(selectedId);updateUI();needsDraw=true;}
    }
    pointers.delete(event.pointerId);gesture=null;
  });
  canvas.addEventListener('wheel',event=>{event.preventDefault();const box=canvas.getBoundingClientRect();setZoom(zoom*Math.exp(-event.deltaY*.002),{x:event.clientX-box.left,y:event.clientY-box.top});},{passive:false});
  canvas.addEventListener('keydown',event=>{if(['+','=','-','Home'].includes(event.key)){event.preventDefault();if(event.key==='Home'){cameraX=.5;cameraY=.5;setZoom(1);}else setZoom(zoom*(event.key==='-'?.5:2));}else if(event.key.startsWith('Arrow')){event.preventDefault();cameraX+=(event.key==='ArrowLeft'?-.08:event.key==='ArrowRight'?.08:0)/zoom;cameraY+=(event.key==='ArrowUp'?-.08:event.key==='ArrowDown'?.08:0)/zoom;cameraClamp();needsDraw=true;}});
  get('trails').onclick=()=>{showTrails=!showTrails;get('trails').setAttribute('aria-pressed',String(showTrails));get('scene-note').textContent=showTrails?'Purple trails show returning foragers’ food signals.':'Food trails hidden.';needsDraw=true;};
  get('feed').onclick=()=>{const added=colony.addFood();save();updateUI();get('scene-note').textContent=added?'A few crumbs on the surface. Who will find them first?':'There are plenty of crumbs already. Give the foragers time to find them.';needsDraw=true;};
  function observe(open){get('observations').hidden=!open;get('observe').setAttribute('aria-expanded',String(open));updateUI();if(open)get('close-observations').focus();else get('observe').focus();}
  get('observe').onclick=()=>observe(get('observations').hidden);get('close-observations').onclick=()=>observe(false);document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!get('observations').hidden)observe(false);});
  get('fullscreen').hidden=!document.fullscreenEnabled;get('fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await get('farm').requestFullscreen();}catch{get('scene-note').textContent='Full screen is unavailable in this browser.';}};
  get('new-colony').onclick=()=>{get('reset-confirm').hidden=false;get('confirm-reset').focus();get('options-status').textContent='Choose Start fresh to replace this colony, or Keep it to cancel.';};get('cancel-reset').onclick=()=>{get('reset-confirm').hidden=true;get('options-status').textContent='Your colony is unchanged.';};
  get('confirm-reset').onclick=()=>{if(storageConflict||unreadableSave){get('options-status').textContent='Reload or recover the saved colony before replacing it.';return;}active?.abort();history=[];get('bob-log').replaceChildren();colony=new Colony(crypto.getRandomValues(new Uint32Array(1))[0]);selectedId=null;following=false;accumulator=0;get('reset-confirm').hidden=true;pause(false);save();resize();updateUI();get('options-status').textContent='New colony started.';};
  get('download').onclick=()=>{const text=JSON.stringify(colony.observation(),null,2),url=URL.createObjectURL(new Blob([text],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download='ant-colony-observation.json';document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);get('observation-export').value=text;get('export-preview').hidden=false;get('options-status').textContent='Observation prepared. If no download appears, copy the text below.';};
  let active=null,history=[];
  function message(who,text){const box=document.createElement('article'),label=document.createElement('strong'),p=document.createElement(who==='You'?'p':'div');label.textContent=who;p.textContent=text;if(who==='Bob')p.className='bob-markdown';box.append(label,p);get('bob-log').append(box);while(get('bob-log').children.length>12)get('bob-log').firstChild.remove();return p;}
  get('stop-bob').onclick=()=>active?.abort();
  get('bob-form').onsubmit=async event=>{
    event.preventDefault();if(active)return;const question=get('bob-question').value.trim();if(!question)return;
    const endpoint=window.WAKE_DEPLOYMENT?.ask_bob?.url||(location.hostname==='sudofx.github.io'?'https://wake-ask-bob.coolgrove68.chatgpt.site':null);
    if(!endpoint){get('bob-status').textContent='Bob connects on the published WAKE site. You can save this observation to review or share.';return;}
    const controller=new AbortController();active=controller;get('ask-bob').disabled=true;get('stop-bob').hidden=false;get('bob-status').textContent='Sharing a snapshot with Bob…';
    const sample=colony.observation(),asked=message('You',question),answer=message('Bob','');let output='',complete=false;
    let timedOut=false;const waiting=setTimeout(()=>{get('bob-status').textContent='Bob is still preparing a reply…';},10000),timer=setTimeout(()=>{timedOut=true;controller.abort();},60000);
    try{
      const response=await fetch(endpoint+'/v1/chat',{method:'POST',credentials:'omit',headers:{'Content-Type':'application/json'},body:JSON.stringify({mode:'ant-farm',observation:sample,question,history:history.slice(-4)}),signal:controller.signal});
      if(!response.ok){const detail=await response.json().catch(()=>({}));if(response.status===429)throw Error('Bob’s shared allowance is temporarily unavailable. Try later; your question is kept here.');if(detail.error==='invalid_request')throw Error('The answer service needs the ant farm update before Bob can read this sample.');throw Error('Bob is unavailable right now. Your question is kept here.');}
      const reader=response.body.getReader(),decoder=new TextDecoder();let buffer='';
      try{for(;;){const {value,done}=await reader.read();buffer+=decoder.decode(value||new Uint8Array(),{stream:!done});if(buffer.length>65536)throw Error('The reply was too large.');const lines=buffer.split('\n');buffer=lines.pop();for(const line of lines){if(!line.trim())continue;const packet=JSON.parse(line);if(packet.type==='delta'){output+=packet.text;WakeBobMarkdown.render(answer,output.slice(0,6000));}if(packet.type==='done'){complete=true;}if(packet.type==='error')throw Error('Bob’s reply was interrupted. Try again.');}if(done)break;}}finally{await reader.cancel().catch(()=>{});}
      if(!complete||!output)throw Error('Bob’s reply was interrupted. Try again.');history.push({question:question.slice(0,1000),answer:output.slice(0,2000)});history=history.slice(-4);get('bob-status').textContent=`Snapshot at ${elapsed(sample.metrics.seconds)} · ${sample.metrics.dug} tunnel segments dug. Bob does not see later changes until you ask again.`;
    }catch(error){get('bob-status').textContent=controller.signal.aborted?(timedOut?'Bob did not finish in time. Your question is kept here; try again.':'Stopped. Your question is kept here.'):error.message;if(!output)answer.parentElement.remove();asked.parentElement.dataset.incomplete='true';}
    finally{clearTimeout(waiting);clearTimeout(timer);if(active===controller)active=null;get('ask-bob').disabled=false;get('stop-bob').hidden=true;}
  };
  document.addEventListener('visibilitychange',()=>{previous=0;accumulator=0;if(document.hidden)save();});window.addEventListener('pagehide',save);window.addEventListener('resize',resize);
  reduced.addEventListener('change',()=>{resize();});
  // Multiple tabs must not silently overwrite the same colony.
  window.addEventListener('storage',event=>{if(event.key===KEY){pause(true);storageConflict=true;get('save-status').textContent='Another tab updated this colony. Reload to pick up its progress.';}});
  pause(paused);updateStorage();resize();updateUI();requestAnimationFrame(animate);
})();
