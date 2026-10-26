/* Canvas owns the habitat; HTML owns controls and observations. */
(() => {
  'use strict';
  class ColonyPersistence{
    constructor(storage,key){this.storage=storage;this.key=key;this.value=storage.getItem(key);this.conflict=false;}
    save(colony){
      if(this.conflict)return false;
      if(this.storage.getItem(this.key)!==this.value){this.conflict=true;return false;}
      const previous=this.value;this.value=JSON.stringify(colony);
      try{this.storage.setItem(this.key,this.value);}catch(error){this.value=previous;throw error;}
      return true;
    }
    observe(event){
      if((event.key!==this.key&&event.key!==null)||event.newValue===this.value)return false;
      // A delayed event from the pre-reload document is not a competing writer.
      if(this.storage.getItem(this.key)!==event.newValue)return false;
      this.conflict=true;return true;
    }
  }
  if(typeof module!=='undefined'&&module.exports){module.exports={ColonyPersistence};return;}
  const drawAnt=window.WakeDrawAnt;
  const {Colony,WIDTH:W,HEIGHT:H,SURFACE:S}=window.WakeAntColony;
  const get=id=>document.getElementById(id),canvas=get('habitat'),ctx=canvas.getContext('2d');
  if(!ctx){get('scene-note').textContent='This browser cannot draw the habitat. Try a browser with Canvas support.';return;}
  const KEY='wake-ant-colony@2',reduced=matchMedia('(prefers-reduced-motion: reduce)');
  let colony,persistence,storageReady=true,storageConflict=false,unreadableSave=false;
  try{persistence=new ColonyPersistence(localStorage,KEY);const saved=persistence.value;colony=saved?Colony.restore(JSON.parse(saved)):null;}catch{storageReady=false;unreadableSave=true;}
  colony ||= new Colony(crypto.getRandomValues(new Uint32Array(1))[0]);
  let paused=false,speed=1,showTrails=true,previous=0,accumulator=0,lastDraw=0,lastSave=0,lastUI=0,selectedId=null,antSignature='';
  let width=0,height=0,dpr=1,cw=0,ch=0,terrainDirty=true,needsDraw=true,frameInterval=1000/24,terrain=document.createElement('canvas'),soil=document.createElement('canvas');
  window.addEventListener('wake-ant-art-ready',()=>{needsDraw=true;});
  const soilCtx=soil.getContext('2d'),ground=terrain.getContext('2d');
  function save(){if(storageConflict||unreadableSave)return;try{if(!persistence.save(colony.save())){storageConflict=true;pause(true);}else storageReady=true;}catch{storageReady=false;}updateStorage();}
  function updateStorage(){get('save-status').textContent=unreadableSave?'Your saved colony could not be read and has been kept untouched. This temporary colony will not replace it.':storageConflict?'Another tab updated this colony. Reload to pick up its progress.':storageReady?'Progress stays in this browser. The colony rests when this page is hidden.':'Saving is unavailable. You can watch now; this colony may not survive a reload.';}
  function resize(){
    const box=canvas.getBoundingClientRect();width=box.width;height=box.height;const mobile=matchMedia('(pointer: coarse)').matches||width<=600;
    // Increase backing detail for browser page zoom without changing scene coordinates.
    const pageScale=Math.max(1,window.visualViewport?.scale||1);
    dpr=Math.min((devicePixelRatio||1)*pageScale,8,Math.sqrt(4000000/(width*height)));frameInterval=1000/(reduced.matches?10:mobile?20:24);cw=width/W;ch=height/H;
    for(const layer of [canvas,terrain,soil]){layer.width=Math.round(width*dpr);layer.height=Math.round(height*dpr);layer.getContext('2d').setTransform(dpr,0,0,dpr,0,0);}
    // Drawn colour fields stay quiet at every zoom; no enlarged photographic grains.
    soilCtx.clearRect(0,0,width,height);
    const earth=soilCtx.createLinearGradient(0,0,0,height);earth.addColorStop(0,'#eee2c8');earth.addColorStop(1,'#d9c8a8');soilCtx.fillStyle=earth;
    soilCtx.beginPath();soilCtx.moveTo(0,(colony.surfaceAt(2)+1)*ch);
    for(const n of colony.nodes){if(n.kind==='surface')soilCtx.lineTo(n.x*cw,(n.y+1)*ch);}
    soilCtx.lineTo(width,(colony.surfaceAt(W-2)+1)*ch);soilCtx.lineTo(width,height);soilCtx.lineTo(0,height);soilCtx.closePath();soilCtx.fill();
    terrainDirty=true;draw();
  }
  function updateTerrain(){
    ground.clearRect(0,0,width,height);ground.drawImage(soil,0,0,width,height);
    ground.strokeStyle='#c9b68f';ground.lineCap='round';ground.lineJoin='round';
    for(const node of colony.nodes){
      if(node.parent===null||node.kind==='surface')continue;const parent=colony.nodes[node.parent];
      ground.lineWidth=Math.min(cw,ch)*1.45;ground.beginPath();ground.moveTo(parent.x*cw,parent.y*ch);ground.lineTo(node.x*cw,node.y*ch);ground.stroke();
    }
    ground.fillStyle='#c9b68f';for(let i=0;i<colony.nodes.length;i++){const n=colony.nodes[i];if(n.kind==='chamber'&&i!==colony.nest){ground.beginPath();ground.ellipse(n.x*cw,n.y*ch,1.8*cw,1.1*ch,0,0,Math.PI*2);ground.fill();}}
    ground.fillStyle='#c9b68f';ground.beginPath();const home=colony.nodes[colony.nest];ground.ellipse(home.x*cw,home.y*ch,2.2*cw,1.3*ch,0,0,Math.PI*2);ground.fill();
    // A warm nest chamber makes the homeward traffic legible.
    const nest=ground.createRadialGradient(home.x*cw,home.y*ch,0,home.x*cw,home.y*ch,8*Math.max(cw,ch));nest.addColorStop(0,'#c7a36d18');nest.addColorStop(1,'#c7a36d00');ground.fillStyle=nest;ground.fillRect((home.x-4)*cw,(home.y-3)*ch,8*cw,6*ch);terrainDirty=false;
  }
  const facings=new Map(),strides=new Map();
  function draw(){
    if(!width||!height)return;needsDraw=false;if(terrainDirty)updateTerrain();ctx.clearRect(0,0,width,height);
    ctx.drawImage(terrain,0,0,width,height);
    if(showTrails){ctx.lineCap='round';ctx.lineWidth=Math.min(cw,ch)*.325;for(let i=0;i<colony.trail.length;i++)if(colony.trail[i]>.15){const n=colony.nodes[i],p=colony.nodes[n.parent];if(!p)continue;ctx.strokeStyle=`rgba(185,57,255,${Math.min(1,.55+colony.trail[i]/12)})`;ctx.beginPath();ctx.moveTo(n.x*cw,n.y*ch);ctx.lineTo(p.x*cw,p.y*ch);ctx.stroke();}}
    for(const f of colony.food){if(!f.left)continue;const x=f.x*cw,y=f.y*ch;ctx.fillStyle='#b3bb68';for(let j=0;j<Math.min(10,Math.ceil(f.left/24));j++){const angle=j*2.4,r=2+Math.sqrt(j)*1.3;ctx.beginPath();ctx.ellipse(x+Math.cos(angle)*r,y+Math.sin(angle)*r,1.2,.8,j,0,7);ctx.fill();}}
    // Deposited grains accumulate at the entrance; excavation requires a return trip.
    ctx.fillStyle='#a7895c';for(let k=0;k<Math.min(70,colony.soilDelivered);k++){const x=(colony.nodes[colony.exit].x-1+(k%2?1:-1)*(1+Math.sqrt(k)*.4))*cw,y=(colony.nodes[colony.exit].y+.5-Math.floor(k/15)*.1)*ch;ctx.beginPath();ctx.ellipse(x,y,.7,.5,k,0,7);ctx.fill();}
    const r=Math.max(1.3,Math.min(3.7,Math.min(cw,ch)*.4));
    for(const dead of colony.recentDeaths){if(!Number.isFinite(dead.x)||colony.time-dead.at>120)continue;ctx.save();ctx.translate(dead.x*cw,dead.y*ch);ctx.rotate(dead.dir);ctx.globalAlpha=.65*(1-(colony.time-dead.at)/120);drawAnt(ctx,r,{id:dead.id,dead:true,moving:false,work:-1,carrying:0},0,colony.time);ctx.restore();}
    for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],length=Math.hypot(b.x-a.x,b.y-a.y)||1,t=Math.min(1,ant.phase+(!paused&&ant.wait<=0&&ant.phase<1?accumulator*ant.pace/length*(ant.carrying?.75:1)*(colony.starvationSeconds>600?.65:1):0));
      const lane=((ant.id%3)-1)*.13,spread=ant.id*2.39996,rad=.5+(ant.id%8)/8,offsetA=ant.from===colony.nest?1-t:0,offsetB=ant.cell===colony.nest?t:0,spreadWeight=offsetA+offsetB;
      const x=(a.x+(b.x-a.x)*t+Math.cos(spread)*rad*1.5*spreadWeight)*cw+Math.sin(ant.dir)*lane*cw,y=(a.y+(b.y-a.y)*t+Math.sin(spread)*rad*.65*spreadWeight)*ch-Math.cos(ant.dir)*lane*ch;
      const moving=ant.phase<1&&ant.wait<=0,scanning=!moving&&ant.work<0&&ant.wait>.8?[0,.35,0,-.3][Math.floor(colony.time*.7+ant.id*1.61)%4]:0;
      const target=(a===b?ant.dir:Math.atan2((b.y-a.y)*ch,(b.x-a.x)*cw))+scanning,old=facings.get(ant.id)??target,turn=Math.atan2(Math.sin(target-old),Math.cos(target-old)),angle=old+Math.max(-.23,Math.min(.23,turn));facings.set(ant.id,angle);
      let pose=strides.get(ant.id);if(!pose)pose={x,y,gait:ant.id*2.39996};
      const distance=Math.hypot(x-pose.x,y-pose.y);if(moving&&distance<Math.max(cw,ch)*2)pose.gait+=distance/r*Math.PI*.55;pose.x=x;pose.y=y;strides.set(ant.id,pose);
      ctx.save();ctx.translate(x,y);ctx.rotate(angle+(moving?Math.sin(pose.gait*2)*.018:0));drawAnt(ctx,r,{...ant,moving,turn},pose.gait,colony.time+(!paused?accumulator:0));ctx.restore();
      if(ant.id===selectedId){ctx.strokeStyle='#6925ac';ctx.lineWidth=1;ctx.beginPath();ctx.arc(x,y,r*5,0,Math.PI*2);ctx.stroke();ctx.fillStyle='#351448';ctx.font='11px system-ui';ctx.fillText('#'+ant.id,x+r*6,y-r*3);}
    }
    const vignette=ctx.createRadialGradient(width*.5,height*.45,width*.12,width*.5,height*.5,Math.max(width,height)*.75);vignette.addColorStop(0,'#0000');vignette.addColorStop(1,'#5d492018');ctx.fillStyle=vignette;ctx.fillRect(0,0,width,height);
  }
  const elapsed=seconds=>`${Math.floor(seconds/60).toString().padStart(2,'0')}:${(seconds%60).toString().padStart(2,'0')}`;
  function updateUI(){
    const m=colony.metrics();get('colony-clock').textContent=elapsed(m.seconds);get('seed-label').textContent=`Colony ${colony.seed.toString(16).toUpperCase()} · saved on this device`;
    const values=[['Living ants',m.ants],['Brood developing',m.brood],['Born',m.born],['Deaths',m.deaths],['Lost to starvation',m.starved],['Entrances',m.entrances],['Tunnel connections',m.connections],['Active digging sites',m.tunnel_tips],['Tunnel segments dug',m.dug],['Food brought home',m.delivered],['Food in nest',m.food_reserve],['Soil pellets carried out',m.soil_pellets]];
    const nodes=values.map(([label,value])=>{const block=document.createElement('div'),dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=label;dd.textContent=value.toLocaleString();block.append(dt,dd);return block;});get('metrics').replaceChildren(...nodes);
    const old=colony.samples.find(s=>s.seconds>=m.seconds-120)||colony.samples[0],span=m.seconds-old.seconds;
    get('pattern').textContent=span>=10?`Over the last ${span} simulation seconds: ${m.dug-old.dug} new tunnel segments and ${m.delivered-old.delivered} food deliveries. ${m.carrying_soil} ants are carrying soil to the entrance. Turn on Trails to see where returning foragers leave signals.`:'The colony is settling in. Let it explore for a little while, then look for repeated routes and new branches.';
    if(m.hungry)get('pattern').textContent='The nest has run out of food. Workers are searching for crumbs; prolonged hunger slows them and eventually causes starvation. Add food to help the colony recover.';
    if(!get('observations').hidden)get('accessible-status').textContent=`${m.ants} ants; ${m.dug} tunnel segments dug; ${m.delivered} food deliveries; ${elapsed(m.seconds)} elapsed.`;
    const signature=colony.ants.map(a=>a.id).join(',');
    if(signature!==antSignature){antSignature=signature;const live=new Set(colony.ants.map(a=>a.id));for(const id of facings.keys())if(!live.has(id)){facings.delete(id);strides.delete(id);}const options=colony.ants.map(a=>{const o=document.createElement('option');o.value=a.id;o.textContent='#'+a.id;return o;});const empty=document.createElement('option');empty.value='';empty.textContent='Choose an ant';get('ant-select').replaceChildren(empty,...options);get('ant-select').value=selectedId===null?'':String(selectedId);}
    const ant=colony.ants.find(a=>a.id===selectedId),dead=colony.recentDeaths.find(a=>a.id===selectedId);
    get('ant-detail').textContent=ant?`Ant ${colony.seed.toString(16).toUpperCase()}:#${ant.id} · ${ant.role==='dig'?'digger':ant.role==='forage'?'forager':'resting worker'} · age ${elapsed(Math.floor(colony.time-ant.bornAt))} · ${ant.work>=0?'excavating':ant.carrying===2?'carrying soil':ant.carrying===1?'carrying food':ant.wait>0?'resting':'walking'}.`:dead?`Ant #${dead.id} died of ${dead.reason} at age ${elapsed(dead.age)}.`:selectedId!==null?`Ant #${selectedId} is no longer alive.`:'Choose an ant or tap one in the habitat. Its number stays with it for life.';
  }
  let sceneryOffset=0,lastScenery=0;
  function updateScenery(){
    const now=new Date(Date.now()+sceneryOffset),hour=now.getHours()+now.getMinutes()/60;
    const daylight=Math.max(0,Math.min(1,(Math.sin((hour-6)*Math.PI/12)+.16)/.65));
    const dusk=Math.max(0,1-Math.abs(daylight-.35)*3);
    get('farm').style.setProperty('--daylight',daylight.toFixed(3));
    get('farm').style.setProperty('--dusk',dusk.toFixed(3));
    get('farm').style.setProperty('--sun-x',`${8+((hour+18)%24)/24*84}%`);
    get('farm').dataset.timeOfDay=hour>=6&&hour<18?'day':'night';
  }
  function animate(now){
    requestAnimationFrame(animate);if(document.hidden){previous=0;return;}if(!previous)previous=now;const delta=Math.min(.25,(now-previous)/1000);previous=now;
    sceneryOffset+=delta*1000*(speed-1);if(now-lastScenery>15000){updateScenery();lastScenery=now;}
    if(!paused){accumulator=Math.min(2,accumulator+delta*speed*4);let steps=0;while(accumulator>=.1&&steps++<20){const before=colony.dug;colony.step();terrainDirty ||= before!==colony.dug;accumulator-=.1;}}
    if(now-lastDraw>=frameInterval&&(!paused||needsDraw)){draw();lastDraw=now;}if(now-lastUI>2000){updateUI();lastUI=now;}if(now-lastSave>10000){save();lastSave=now;}
  }
  function pause(value){paused=value;get('pause').textContent=paused?'Resume':'Pause';get('pause').setAttribute('aria-pressed',String(paused));get('scene-note').textContent=paused?'The colony is resting. Resume whenever you’re ready.':'Small steps. New tunnels. No master plan.';}
  get('pause').onclick=()=>pause(!paused);get('speed').onclick=()=>{speed=speed===1?2:speed===2?4:1;get('speed').textContent=speed+'×';get('speed').setAttribute('aria-label',`Simulation speed, currently ${speed} times`);};
  get('ant-select').onchange=()=>{selectedId=get('ant-select').value===''?null:Number(get('ant-select').value);updateUI();needsDraw=true;};
  function fullscreenState(active){get('farm').classList.toggle('is-fullscreen',active);get('fullscreen').setAttribute('aria-pressed',String(active));get('fullscreen').setAttribute('aria-label',active?'Exit full screen':'Enter full screen');get('fullscreen').textContent=active?'Exit full screen':'Full screen';resize();}
  get('fullscreen').onclick=async()=>{
    const farm=get('farm'),active=farm.classList.contains('is-fullscreen');
    if(active){if(document.fullscreenElement)await document.exitFullscreen();fullscreenState(false);}
    else{fullscreenState(true);try{if(farm.requestFullscreen)await farm.requestFullscreen();}catch{/* Embedded and iPhone browsers still get the full-viewport layout. */}}
  };
  document.addEventListener('fullscreenchange',()=>fullscreenState(!!document.fullscreenElement));
  // The browser owns all page zoom and panning. A tap only selects an ant.
  canvas.addEventListener('click',event=>{
    const box=canvas.getBoundingClientRect(),x=(event.clientX-box.left)/width*W,y=(event.clientY-box.top)/height*H;
    let nearest=null,distance=14;
    for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],d=Math.hypot((a.x+(b.x-a.x)*ant.phase-x)*cw,(a.y+(b.y-a.y)*ant.phase-y)*ch);if(d<distance){nearest=ant;distance=d;}}
    if(nearest){selectedId=nearest.id;get('ant-select').value=String(selectedId);updateUI();needsDraw=true;}
  });
  get('trails').onclick=()=>{showTrails=!showTrails;get('trails').setAttribute('aria-pressed',String(showTrails));get('scene-note').textContent=showTrails?'Purple trails show returning foragers’ food signals.':'Food trails hidden.';needsDraw=true;};
  get('feed').onclick=()=>{const added=colony.addFood();save();updateUI();get('scene-note').textContent=added?'A few crumbs on the surface. Who will find them first?':'There are plenty of crumbs already. Give the foragers time to find them.';needsDraw=true;};
  function observe(open){get('observations').hidden=!open;get('observe').setAttribute('aria-expanded',String(open));updateUI();if(open)get('close-observations').focus();else get('observe').focus();}
  get('observe').onclick=()=>observe(get('observations').hidden);get('close-observations').onclick=()=>observe(false);document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!get('observations').hidden)observe(false);});
  get('new-colony').onclick=()=>{get('reset-confirm').hidden=false;get('confirm-reset').focus();get('options-status').textContent='Choose Start fresh to replace this colony, or Keep it to cancel.';};get('cancel-reset').onclick=()=>{get('reset-confirm').hidden=true;get('options-status').textContent='Your colony is unchanged.';};
  get('confirm-reset').onclick=()=>{if(storageConflict||unreadableSave){get('options-status').textContent='Reload or recover the saved colony before replacing it.';return;}colony=new Colony(crypto.getRandomValues(new Uint32Array(1))[0]);selectedId=null;accumulator=0;get('reset-confirm').hidden=true;pause(false);save();resize();updateUI();get('options-status').textContent='New colony started.';};
  get('download').onclick=()=>{const text=JSON.stringify(colony.observation(),null,2),url=URL.createObjectURL(new Blob([text],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download='ant-colony-observation.json';document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);get('observation-export').value=text;get('export-preview').hidden=false;get('options-status').textContent='Observation prepared. If no download appears, copy the text below.';};
  document.addEventListener('visibilitychange',()=>{previous=0;accumulator=0;if(document.hidden)save();});window.addEventListener('pagehide',save);window.addEventListener('resize',scheduleResize);
  let resizeFrame;
  function scheduleResize(){if(!resizeFrame)resizeFrame=requestAnimationFrame(()=>{resizeFrame=0;resize();});}
  window.visualViewport?.addEventListener('resize',scheduleResize);
  reduced.addEventListener('change',()=>{resize();});
  // Multiple tabs must not silently overwrite the same colony.
  window.addEventListener('storage',event=>{try{if(persistence?.observe(event)){pause(true);storageConflict=true;updateStorage();}}catch{storageReady=false;updateStorage();}});
  updateScenery();pause(paused);updateStorage();resize();updateUI();requestAnimationFrame(animate);
})();
