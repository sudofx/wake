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
  let mine=colony,mode='bob',bobPacket=null,bobError='',modeRequest=0,bobRefreshAt=0,bobRefreshing=false;
  let paused=false,speed=1,showTrails=false,previous=0,accumulator=0,lastDraw=0,lastSave=0,lastUI=0,selectedId=null,antSignature='';
  const foodFlashes=[];
  const camera={zoom:1,x:0,y:0};
  let width=0,height=0,dpr=1,cw=0,ch=0,terrainDirty=true,needsDraw=true,frameInterval=1000/24,terrain=document.createElement('canvas'),soil=document.createElement('canvas');
  window.addEventListener('wake-ant-art-ready',()=>{needsDraw=true;});
  const soilCtx=soil.getContext('2d'),ground=terrain.getContext('2d');
  function save(){if(mode!=='mine'||storageConflict||unreadableSave)return;try{if(!persistence.save(colony.save())){storageConflict=true;pause(true);}else storageReady=true;}catch{storageReady=false;}updateStorage();}
  function updateStorage(){
    if(mode==='bob'){
      const date=bobPacket?new Date(bobPacket.updated_at):null,stale=date&&Date.now()-date.getTime()>10800000;
      get('save-status').textContent=bobError||(!date?'Opening Bob’s shared colony…':`Recorded ${date.toLocaleString()}. You are watching its latest recorded interval. Bob’s caretaker feeds and maintains the shared colony.${stale?' A newer care visit has not been published yet.':''}`);
      return;
    }
    get('save-status').textContent=unreadableSave?'Your saved colony could not be read and has been kept untouched. This temporary colony will not replace it.':storageConflict?'Another tab updated this colony. Reload to pick up its progress.':storageReady?'Progress stays in this browser. The colony rests when this page is hidden.':'Saving is unavailable. You can watch now; this colony may not survive a reload.';
  }
  function feedback(button,message){
    button.classList.remove('is-activated');void button.offsetWidth;button.classList.add('is-activated');
    clearTimeout(button.feedbackTimer);button.feedbackTimer=setTimeout(()=>button.classList.remove('is-activated'),750);
    if(message){get('scene-note').textContent=message;get('accessible-status').textContent=message;}
  }
  function useColony(value){colony=value;selectedId=null;antSignature='';facings.clear();strides.clear();accumulator=0;terrainDirty=true;needsDraw=true;resize();updateUI();}
  function resetReplay(){useColony(Colony.restore(bobPacket.replay.start));}
  function stepColony(){
    if(mode==='bob'){
      if(!bobPacket||!bobPacket.replay.ticks)return;
      if(colony.ticks>=bobPacket.replay.start.ticks+bobPacket.replay.ticks)resetReplay();
      for(const event of bobPacket.replay.care)if(event.tick===colony.ticks)colony.addFood(event.x);
    }
    colony.step();
  }
  async function switchMode(next){
    const request=++modeRequest;
    if(mode==='mine'){save();mine=colony;}
    mode=next;get('farm-choice').value=mode;get('farm').dataset.colony=mode;
    for(const id of ['feed','new-colony','reset-confirm'])get(id).hidden=mode==='bob';
    get('feed').disabled=mode==='bob';get('reset-confirm').hidden=true;
    get('download').disabled=mode==='bob'&&!bobPacket;
    get('speed').setAttribute('aria-label',`${mode==='bob'?'Playback':'Simulation'} speed, currently ${speed} times`);
    bobError='';pause(mode==='mine'&&storageConflict);
    if(mode==='mine'){canvas.hidden=false;useColony(mine);updateStorage();return;}
    canvas.hidden=true;get('scene-note').textContent='Opening Bob’s shared farm…';updateStorage();
    try{
      const packet=bobPacket||await window.WakeBobFarm.read();
      if(request!==modeRequest||mode!=='bob')return;
      bobPacket=packet;bobRefreshAt=performance.now();canvas.hidden=false;get('download').disabled=false;resetReplay();pause(false);updateStorage();
    }catch{
      if(request!==modeRequest||mode!=='bob')return;
      bobError='Bob’s shared farm is unavailable right now. Your personal farm is unchanged; choose My farm to watch it.';
      get('scene-note').textContent='Bob’s farm is unavailable. My farm is still yours to explore.';updateStorage();
    }
  }
  async function refreshBob(now){
    if(mode!=='bob'||!bobPacket||paused||bobRefreshing||now-bobRefreshAt<300000)return;
    bobRefreshing=true;bobRefreshAt=now;
    try{const next=await window.WakeBobFarm.read();if(mode==='bob'&&!paused&&next.updated_at!==bobPacket.updated_at){bobPacket=next;resetReplay();updateStorage();}}
    catch{/* Keep the last valid dated recording; never replace it with a random colony. */}
    finally{bobRefreshing=false;}
  }
  function resize(){
    const box=canvas.getBoundingClientRect();width=box.width;height=box.height;const mobile=matchMedia('(pointer: coarse)').matches||width<=600;
    // Increase backing detail for browser page zoom without changing scene coordinates.
    const pageScale=Math.max(1,window.visualViewport?.scale||1);
    dpr=Math.min((devicePixelRatio||1)*pageScale,8,Math.sqrt(4000000/(width*height)));frameInterval=1000/(reduced.matches?10:mobile?20:24);cw=width/W;ch=height/H;
    for(const layer of [canvas,terrain,soil]){layer.width=Math.round(width*dpr);layer.height=Math.round(height*dpr);layer.getContext('2d').setTransform(dpr,0,0,dpr,0,0);}
    // Drawn colour fields stay quiet at every zoom; no enlarged photographic grains.
    soilCtx.clearRect(0,0,width,height);
    const earth=soilCtx.createLinearGradient(0,0,0,height);earth.addColorStop(0,'#eee2c8');earth.addColorStop(1,'#d9c8a8');soilCtx.fillStyle=earth;
    soilOutline(soilCtx);soilCtx.fill();clampCamera();
    terrainDirty=true;draw();
  }
  function surfaceBase(x){
    const i=Math.max(0,Math.min(115,Math.floor(x)-2)),a=colony.nodes[i],b=colony.nodes[i+1];
    return a.y+(b.y-a.y)*Math.max(0,Math.min(1,x-a.x));
  }
  function surfaceY(x){
    let rise=0;
    for(const id of colony.exits){const d=Math.abs(x-colony.nodes[id].x);
      // Raised shoulders and a shallow central crater share the ants' contour.
      const mound=d<.55?1.12:d<.9?1.12+(d-.55)/.35*.55:d<3.4?1.67*(1-(d-.9)/2.5):0;
      rise=Math.max(rise,mound);
    }
    return surfaceBase(x)-rise;
  }
  function soilOutline(layer){
    layer.beginPath();layer.moveTo(0,surfaceY(0)*ch);
    for(let x=0;x<=W;x+=.2)layer.lineTo(x*cw,surfaceY(x)*ch);
    layer.lineTo(width,height);layer.lineTo(0,height);layer.closePath();
  }
  function clampCamera(){camera.x=Math.max(width*(1-camera.zoom),Math.min(0,camera.x));camera.y=Math.max(height*(1-camera.zoom),Math.min(0,camera.y));}
  function updateTerrain(){
    // Excavation may open another entrance; rebuild the same visible contour.
    soilCtx.clearRect(0,0,width,height);const earth=soilCtx.createLinearGradient(0,0,0,height);earth.addColorStop(0,'#eee2c8');earth.addColorStop(1,'#d9c8a8');soilCtx.fillStyle=earth;soilOutline(soilCtx);soilCtx.fill();
    ground.clearRect(0,0,width,height);ground.drawImage(soil,0,0,width,height);
    ground.save();soilOutline(ground);ground.clip();
    ground.strokeStyle='#c9b68f';ground.lineCap='round';ground.lineJoin='round';
    for(const node of colony.nodes){
      if(node.parent===null||node.kind==='surface')continue;const parent=colony.nodes[node.parent];
      ground.lineWidth=Math.min(cw,ch)*1.45;ground.beginPath();ground.moveTo(parent.x*cw,parent.y*ch);ground.lineTo(node.x*cw,node.y*ch);ground.stroke();
    }
    ground.fillStyle='#c9b68f';for(let i=0;i<colony.nodes.length;i++){const n=colony.nodes[i];if(n.kind==='chamber'&&i!==colony.nest){ground.beginPath();ground.ellipse(n.x*cw,n.y*ch,1.8*cw,1.1*ch,0,0,Math.PI*2);ground.fill();}}
    ground.fillStyle='#c9b68f';ground.beginPath();const home=colony.nodes[colony.nest];ground.ellipse(home.x*cw,home.y*ch,4.9*cw,2.7*ch,0,0,Math.PI*2);ground.fill();
    // A warm nest chamber makes the homeward traffic legible.
    const nest=ground.createRadialGradient(home.x*cw,home.y*ch,0,home.x*cw,home.y*ch,8*Math.max(cw,ch));nest.addColorStop(0,'#c7a36d18');nest.addColorStop(1,'#c7a36d00');ground.fillStyle=nest;ground.fillRect((home.x-4)*cw,(home.y-3)*ch,8*cw,6*ch);for(const id of colony.exits){const n=colony.nodes[id],y=surfaceY(n.x)*ch;
      ground.strokeStyle='#b59b70';ground.lineWidth=.65*Math.min(cw,ch);ground.beginPath();ground.moveTo(n.x*cw,y);ground.lineTo(n.x*cw,n.y*ch);ground.stroke();
      ground.fillStyle='#5e4a2e';ground.beginPath();ground.ellipse(n.x*cw,y,.58*cw,.23*ch,0,0,Math.PI*2);ground.fill();
      ground.strokeStyle='#b69a6d';ground.lineWidth=Math.max(.65,cw*.08);ground.beginPath();ground.ellipse(n.x*cw,y+.04*ch,.66*cw,.27*ch,0,0,Math.PI);ground.stroke();
      ground.fillStyle='#b99d70';for(let k=0;k<26;k++){const dx=(k%2?1:-1)*(.9+(k%13)*.18),x=n.x+dx;ground.beginPath();ground.ellipse(x*cw,(surfaceY(x)+.15+(k%3)*.13)*ch,.09*cw,.06*ch,k,0,7);ground.fill();}
    }
    ground.restore();terrainDirty=false;
  }
  const facings=new Map(),strides=new Map();
  function draw(){
    if(!width||!height)return;needsDraw=false;if(terrainDirty)updateTerrain();ctx.clearRect(0,0,width,height);
    ctx.save();ctx.translate(camera.x,camera.y);ctx.scale(camera.zoom,camera.zoom);ctx.drawImage(terrain,0,0,width,height);
    if(showTrails){ctx.lineCap='round';ctx.lineWidth=Math.min(cw,ch)*.325;for(let i=0;i<colony.trail.length;i++)if(colony.trail[i]>.15){const n=colony.nodes[i],p=colony.nodes[n.parent];if(!p)continue;ctx.strokeStyle=`rgba(185,57,255,${Math.min(1,.55+colony.trail[i]/12)})`;ctx.beginPath();ctx.moveTo(n.x*cw,n.y*ch);ctx.lineTo(p.x*cw,p.y*ch);ctx.stroke();}}
    for(const f of colony.food){if(!f.left)continue;const x=f.x*cw,y=surfaceY(f.x)*ch;ctx.fillStyle=f.kind==='protein'?'#a76b47':'#9ca74c';for(let j=0;j<Math.min(10,Math.ceil(f.left/24));j++){const angle=j*2.4,r=2+Math.sqrt(j)*1.3;ctx.beginPath();ctx.ellipse(x+Math.cos(angle)*r,y+Math.sin(angle)*r,1.5,1,j,0,7);ctx.fill();}}
    const flashNow=performance.now();
    for(let i=foodFlashes.length-1;i>=0;i--){const flash=foodFlashes[i],age=(flashNow-flash.at)/1600;if(age>=1){foodFlashes.splice(i,1);continue;}ctx.save();ctx.globalAlpha=1-age;ctx.strokeStyle='#f7f4a4';ctx.lineWidth=2;ctx.beginPath();ctx.arc(flash.x*cw,flash.y*ch,reduced.matches?12:8+age*24,0,Math.PI*2);ctx.stroke();ctx.fillStyle='#fff7ba';ctx.beginPath();ctx.arc(flash.x*cw,flash.y*ch,3,0,Math.PI*2);ctx.fill();ctx.restore();needsDraw=true;}
    // Deposited grains accumulate at the entrance; excavation requires a return trip.
    ctx.fillStyle='#a7895c';for(let k=0;k<Math.min(70,colony.soilDelivered);k++){const x=colony.nodes[colony.exit].x+(k%2?1:-1)*(1+Math.sqrt(k)*.4),y=surfaceY(x)+.15+(k%3)*.12;ctx.beginPath();ctx.ellipse(x*cw,y*ch,.7,.5,k,0,7);ctx.fill();}
    const r=Math.max(1.3,Math.min(3.7,Math.min(cw,ch)*.4));
    const home=colony.nodes[colony.nest];
    for(const [i,brood] of colony.brood.slice(0,32).entries()){
      const x=(home.x+1.1+(i%6)*.52)*cw,y=(home.y-.9+Math.floor(i/6)*.42)*ch;
      ctx.save();ctx.translate(x,y);ctx.rotate((i%3-1)*.35);ctx.fillStyle=brood.stage==='pupa'?'#bca780':'#f7efd8';ctx.strokeStyle='#f7efd8';ctx.lineWidth=r*.7;
      if(brood.stage==='larva'){ctx.beginPath();ctx.arc(0,0,r*.6,.3,Math.PI*1.7);ctx.stroke();}
      else{ctx.beginPath();ctx.ellipse(0,0,r*(brood.stage==='pupa'?.95:.5),r*.4,0,0,Math.PI*2);ctx.fill();}
      ctx.restore();
    }
    for(const dead of colony.recentDeaths){if(!Number.isFinite(dead.x)||colony.time-dead.at>120)continue;ctx.save();ctx.translate(dead.x*cw,dead.y*ch);ctx.rotate(dead.dir);ctx.globalAlpha=.65*(1-(colony.time-dead.at)/120);drawAnt(ctx,r,{id:dead.id,dead:true,moving:false,work:-1,carrying:0},0,colony.time);ctx.restore();}
    for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],length=Math.hypot(b.x-a.x,b.y-a.y)||1,t=Math.min(1,ant.phase+(!paused&&ant.wait<=0&&ant.phase<1?accumulator*ant.pace/length*(ant.carrying?.75:1)*(colony.starvationSeconds>600?.65:1):0));
      const surface=a.kind==='surface'&&b.kind==='surface',lane=surface?0:((ant.id%3)-1)*.13,spread=ant.id*2.39996,rad=.5+(ant.id%8)/8,offsetA=ant.from===colony.nest?1-t:0,offsetB=ant.cell===colony.nest?t:0,spreadWeight=offsetA+offsetB;
      const worldX=a.x+(b.x-a.x)*t+Math.cos(spread)*rad*1.5*spreadWeight;
      const x=worldX*cw+Math.sin(ant.dir)*lane*cw,y=(surface?surfaceY(worldX):(a.kind==='surface'?surfaceY(a.x):a.y)*(1-t)+(b.kind==='surface'?surfaceY(b.x):b.y)*t+Math.sin(spread)*rad*.65*spreadWeight)*ch-Math.cos(ant.dir)*lane*ch;
      const moving=ant.phase<1&&ant.wait<=0,scanning=!moving&&ant.work<0&&ant.wait>.8?[0,.35,0,-.3][Math.floor(colony.time*.7+ant.id*1.61)%4]:0;
      const direction=Math.sign(b.x-a.x)||1,target=(a===b?ant.dir:surface?Math.atan2((surfaceY(worldX+.08*direction)-surfaceY(worldX-.08*direction))*ch,.16*direction*cw):Math.atan2(((b.kind==='surface'?surfaceY(b.x):b.y)-(a.kind==='surface'?surfaceY(a.x):a.y))*ch,(b.x-a.x)*cw))+scanning,old=facings.get(ant.id)??target,turn=Math.atan2(Math.sin(target-old),Math.cos(target-old)),angle=old+Math.max(-.23,Math.min(.23,turn));facings.set(ant.id,angle);
      let pose=strides.get(ant.id);if(!pose)pose={x,y,gait:ant.id*2.39996};
      const distance=Math.hypot(x-pose.x,y-pose.y);if(moving&&distance<Math.max(cw,ch)*2)pose.gait+=distance/r*Math.PI*.55;pose.x=x;pose.y=y;strides.set(ant.id,pose);
      ctx.save();ctx.translate(x,y);ctx.rotate(angle+(moving?Math.sin(pose.gait*2)*.018:0));drawAnt(ctx,r,{...ant,moving,turn,callow:colony.time-ant.bornAt<180},pose.gait,colony.time+(!paused?accumulator:0));ctx.restore();
      if(ant.id===selectedId){ctx.strokeStyle='#6925ac';ctx.lineWidth=1;ctx.beginPath();ctx.arc(x,y,r*5,0,Math.PI*2);ctx.stroke();ctx.fillStyle='#351448';ctx.font='11px system-ui';ctx.fillText('#'+ant.id,x+r*6,y-r*3);}
    }
    if(colony.queen){
      const time=colony.time+(!paused?accumulator:0),alive=colony.queen.alive,motion=alive&&!reduced.matches?1:0,x=(home.x-1.7)*cw+Math.sin(time*.38)*r*.23*motion,y=home.y*ch+Math.sin(time*.51)*r*.14*motion;
      ctx.save();ctx.translate(x,y);ctx.rotate(Math.sin(time*.32)*.055*motion);ctx.scale(1+Math.sin(time*1.1)*.012*motion,1);drawAnt(ctx,r*1.85,{id:-1,queen:true,dead:!alive,restingMotion:motion,moving:false,work:-1,carrying:0},0,time);ctx.restore();
      if(selectedId==='queen'){ctx.strokeStyle='#9b6725';ctx.lineWidth=1.5;ctx.beginPath();ctx.ellipse(x,y,r*6.4,r*4,0,0,Math.PI*2);ctx.stroke();}
    }
    ctx.restore();
    const vignette=ctx.createRadialGradient(width*.5,height*.45,width*.12,width*.5,height*.5,Math.max(width,height)*.75);vignette.addColorStop(0,'#0000');vignette.addColorStop(1,'#5d492018');ctx.fillStyle=vignette;ctx.fillRect(0,0,width,height);
  }
  const elapsed=seconds=>`${Math.floor(seconds/60).toString().padStart(2,'0')}:${(seconds%60).toString().padStart(2,'0')}`;
  function updateUI(){
    if(mode==='bob'&&!bobPacket){get('metrics').replaceChildren();get('seed-label').textContent='Bob’s shared colony';get('pattern').textContent=bobError||'Loading the latest recorded interval.';get('ant-select').disabled=true;return;}
    get('ant-select').disabled=false;
    const m=colony.metrics();get('colony-clock').textContent=(mode==='bob'?'REPLAY ':'')+elapsed(m.seconds);get('seed-label').textContent=`Colony ${colony.seed.toString(16).toUpperCase()} · ${mode==='bob'?'Bob’s shared recorded farm':'saved on this device'}`;
    const values=[['Workers',m.ants],['Queen',m.queen_alive===false?'Died':'Alive'],['Eggs',m.eggs??0],['Larvae',m.larvae??0],['Pupae',m.pupae??0],['Nurses',m.nurses??0],['Born',m.born],['Deaths',m.deaths],['Lost to starvation',m.starved],['Entrances',m.entrances],['Tunnel segments dug',m.dug],['Food brought home',m.delivered],['Energy in nest',m.food_reserve],['Brood nutrition',m.protein_reserve??0],['Soil pellets carried out',m.soil_pellets]];
    const nodes=values.map(([label,value])=>{const block=document.createElement('div'),dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=label;dd.textContent=value.toLocaleString();block.append(dt,dd);return block;});get('metrics').replaceChildren(...nodes);
    const old=colony.samples.find(s=>s.seconds>=m.seconds-120)||colony.samples[0],span=m.seconds-old.seconds;
    get('pattern').textContent=span>=10?`Over the last ${span} simulation seconds: ${m.dug-old.dug} new tunnel segments and ${m.delivered-old.delivered} food deliveries. ${m.carrying_soil} ants are carrying soil to the entrance. Turn on Trails to see where returning foragers leave signals.`:'The colony is settling in. Let it explore for a little while, then look for repeated routes and new branches.';
    if(m.hungry)get('pattern').textContent=mode==='bob'?'This recorded interval includes a food shortage. Bob’s care visits and feedings are recorded with the shared farm.':'The nest has run out of food. Workers are searching for crumbs; prolonged hunger slows them and eventually causes starvation. Add food to help the colony recover.';
    if(!get('observations').hidden)get('accessible-status').textContent=`${m.ants} ants; ${m.dug} tunnel segments dug; ${m.delivered} food deliveries; ${elapsed(m.seconds)} elapsed.`;
    const signature=(colony.queen?'queen,':'')+colony.ants.map(a=>a.id).join(',');
    if(signature!==antSignature){antSignature=signature;const live=new Set(colony.ants.map(a=>a.id));for(const id of facings.keys())if(!live.has(id)){facings.delete(id);strides.delete(id);}const options=colony.ants.map(a=>{const o=document.createElement('option');o.value=a.id;o.textContent='#'+a.id;return o;});if(colony.queen){const queen=document.createElement('option');queen.value='queen';queen.textContent='Queen';options.unshift(queen);}const empty=document.createElement('option');empty.value='';empty.textContent='Choose an ant';get('ant-select').replaceChildren(empty,...options);get('ant-select').value=selectedId===null?'':String(selectedId);}
    const ant=colony.ants.find(a=>a.id===selectedId),dead=colony.recentDeaths.find(a=>a.id===selectedId);
    get('ant-detail').textContent=selectedId==='queen'?`The queen stays near the nursery and lays eggs; workers tend her and the brood. She does not direct the colony’s jobs. ${colony.queen?.alive?'':'This colony’s queen has died.'}`:ant?`Ant ${colony.seed.toString(16).toUpperCase()}:#${ant.id} · ${ant.role==='dig'?'digger':ant.role==='forage'?'forager':ant.role==='nurse'?'nurse':'resting worker'} · age ${elapsed(Math.floor(colony.time-ant.bornAt))} · ${ant.work>=0?'excavating':ant.carrying===2?'carrying soil':ant.carrying===1?'carrying food':ant.role==='nurse'?'tending the nursery':ant.wait>0?'resting':'walking'}.`:dead?`Ant #${dead.id} died of ${dead.reason} at age ${elapsed(dead.age)}.`:selectedId!==null?`Ant #${selectedId} is no longer alive.`:'Choose an ant or tap one in the habitat. Its number stays with it for life.';
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
    if(!paused&&(mode==='mine'||bobPacket)){accumulator=Math.min(2,accumulator+delta*speed*4);let steps=0;while(accumulator>=.1&&steps++<20){const before=colony.dug;stepColony();terrainDirty ||= before!==colony.dug;accumulator-=.1;}}
    if(now-lastDraw>=frameInterval&&(!paused||needsDraw)){draw();lastDraw=now;}if(now-lastUI>2000){updateUI();lastUI=now;}if(now-lastSave>10000){save();lastSave=now;}
    void refreshBob(now);
  }
  function pause(value){
    paused=value;needsDraw=true;const label=(paused?'Play ':'Pause ')+(mode==='bob'?'playback':'simulation');get('pause').setAttribute('aria-label',label);get('pause').title=label;
    get('pause').innerHTML=paused?'<svg viewBox="0 0 24 24" aria-hidden="true"><path class="play-mark" d="m8 4 12 8-12 8Z"/></svg>':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14M16 5v14"/></svg>';
    get('pause').setAttribute('aria-pressed',String(paused));get('scene-note').textContent=mode==='bob'?(paused?'Recorded playback paused. Bob’s caretaker continues independently.':'Bob’s shared farm · replaying its latest recorded interval.'):(paused?'The colony is resting. Play whenever you’re ready.':'Small steps. New tunnels. No master plan.');
  }
  get('pause').onclick=()=>{pause(!paused);feedback(get('pause'));};get('speed').onclick=()=>{speed=speed===1?2:speed===2?4:1;get('speed').textContent=speed+'×';get('speed').setAttribute('aria-label',`${mode==='bob'?'Playback':'Simulation'} speed, currently ${speed} times`);feedback(get('speed'),`${mode==='bob'?'Playback':'Simulation'} speed: ${speed}×.`);};
  get('ant-select').onchange=()=>{const value=get('ant-select').value;selectedId=value===''?null:value==='queen'?'queen':Number(value);updateUI();needsDraw=true;};
  function fullscreenState(active){get('farm').classList.toggle('is-fullscreen',active);get('fullscreen').setAttribute('aria-pressed',String(active));get('fullscreen').setAttribute('aria-label',active?'Exit full screen':'Enter full screen');get('fullscreen').title=active?'Exit full screen':'Enter full screen';get('fullscreen').innerHTML=active?'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9h5V4m6 0v5h5M9 20v-5H4m16 0h-5v5"/></svg>':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4H4v5m11-5h5v5M4 15v5h5m11-5v5h-5"/></svg>';resize();}
  get('fullscreen').onclick=async()=>{
    const farm=get('farm'),active=farm.classList.contains('is-fullscreen');
    feedback(get('fullscreen'));
    if(active){if(document.fullscreenElement)await document.exitFullscreen();fullscreenState(false);}
    else{fullscreenState(true);try{if(farm.requestFullscreen)await farm.requestFullscreen();}catch{/* Embedded and iPhone browsers still get the full-viewport layout. */}}
  };
  document.addEventListener('fullscreenchange',()=>fullscreenState(!!document.fullscreenElement));
  // Desktop wheel zoom stays anchored to the pointer. Touch and Ctrl-wheel
  // retain the browser's native page zoom.
  canvas.addEventListener('wheel',event=>{
    if(event.ctrlKey||!matchMedia('(pointer: fine)').matches)return;
    event.preventDefault();const box=canvas.getBoundingClientRect(),x=event.clientX-box.left,y=event.clientY-box.top;
    const delta=event.deltaY*(event.deltaMode===1?16:event.deltaMode===2?height:1),next=Math.max(1,Math.min(6,camera.zoom*Math.exp(-delta*.0015))),ratio=next/camera.zoom;
    camera.x=x-(x-camera.x)*ratio;camera.y=y-(y-camera.y)*ratio;camera.zoom=next;clampCamera();needsDraw=true;
  },{passive:false});
  canvas.addEventListener('click',event=>{
    const box=canvas.getBoundingClientRect(),x=(event.clientX-box.left-camera.x)/camera.zoom/cw,y=(event.clientY-box.top-camera.y)/camera.zoom/ch;
    let nearest=null,distance=14;
    const home=colony.nodes[colony.nest];if(colony.queen&&Math.hypot((home.x-1.7-x)*cw,(home.y-y)*ch)<18){selectedId='queen';get('ant-select').value='queen';updateUI();needsDraw=true;return;}
    for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],d=Math.hypot((a.x+(b.x-a.x)*ant.phase-x)*cw,(a.y+(b.y-a.y)*ant.phase-y)*ch);if(d<distance){nearest=ant;distance=d;}}
    if(nearest){selectedId=nearest.id;get('ant-select').value=String(selectedId);updateUI();needsDraw=true;}
  });
  get('trails').onclick=()=>{showTrails=!showTrails;get('trails').setAttribute('aria-pressed',String(showTrails));feedback(get('trails'),showTrails?'Purple trails show returning foragers’ food signals.':'Food trails hidden.');needsDraw=true;};
  get('feed').onclick=()=>{if(mode!=='mine')return;const before=colony.food.length,added=colony.addFood();if(added){const fresh=colony.food.slice(before);for(const food of fresh)foodFlashes.push({x:food.x,y:food.y,at:performance.now()});}save();updateUI();feedback(get('feed'),added?'Food added — watch the glowing crumbs on the surface.':'There are plenty of crumbs already. Give the foragers time to find them.');needsDraw=true;};
  get('farm-choice').onchange=()=>{void switchMode(get('farm-choice').value==='mine'?'mine':'bob');};
  function observe(open){get('observations').hidden=!open;get('observe').setAttribute('aria-expanded',String(open));updateUI();if(open)get('close-observations').focus();else get('observe').focus();}
  get('observe').onclick=()=>observe(get('observations').hidden);get('close-observations').onclick=()=>observe(false);document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!get('observations').hidden)observe(false);});
  get('new-colony').onclick=()=>{if(mode!=='mine')return;get('reset-confirm').hidden=false;get('confirm-reset').focus();get('options-status').textContent='Choose Start fresh to replace this colony, or Keep it to cancel.';};get('cancel-reset').onclick=()=>{get('reset-confirm').hidden=true;get('options-status').textContent='Your colony is unchanged.';};
  get('confirm-reset').onclick=()=>{if(mode!=='mine')return;if(storageConflict||unreadableSave){get('options-status').textContent='Reload or recover the saved colony before replacing it.';return;}mine=new Colony(crypto.getRandomValues(new Uint32Array(1))[0]);useColony(mine);get('reset-confirm').hidden=true;pause(false);save();updateUI();get('options-status').textContent='New colony started.';feedback(get('new-colony'));};
  get('download').onclick=()=>{if(mode==='bob'&&!bobPacket)return;const observation=mode==='bob'?{schema:'wake-bob-ant-observation@1',colony_id:bobPacket.colony_id,model:bobPacket.model,updated_at:bobPacket.updated_at,recorded_tick:bobPacket.checkpoint.ticks,observation:bobPacket.observation,scope:'Published simulation checkpoint. Browser playback is not new colony history.'}:colony.observation();const text=JSON.stringify(observation,null,2),url=URL.createObjectURL(new Blob([text],{type:'application/json'})),link=document.createElement('a');link.href=url;link.download='ant-colony-observation.json';document.body.append(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);get('observation-export').value=text;get('export-preview').hidden=false;get('options-status').textContent='Observation prepared. If no download appears, copy the text below.';};
  document.addEventListener('visibilitychange',()=>{previous=0;accumulator=0;if(document.hidden)save();});window.addEventListener('pagehide',save);window.addEventListener('resize',scheduleResize);
  let resizeFrame;
  function scheduleResize(){if(!resizeFrame)resizeFrame=requestAnimationFrame(()=>{resizeFrame=0;resize();});}
  window.visualViewport?.addEventListener('resize',scheduleResize);
  reduced.addEventListener('change',()=>{resize();});
  // Multiple tabs must not silently overwrite the same colony.
  window.addEventListener('storage',event=>{try{if(persistence?.observe(event)){if(mode==='mine')pause(true);storageConflict=true;updateStorage();}}catch{storageReady=false;updateStorage();}});
  updateScenery();pause(paused);updateStorage();resize();updateUI();requestAnimationFrame(animate);
  void switchMode(new URLSearchParams(location.search).get('farm')==='mine'?'mine':'bob');
})();
