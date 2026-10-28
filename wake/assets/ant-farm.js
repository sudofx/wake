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
  let following=false,lastPoseTime=0,excavationCache=null;
  const positions=new Map();
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
  function useColony(value){colony=value;selectedId=null;antSignature='';excavationCache=null;facings.clear();strides.clear();positions.clear();following=false;accumulator=0;terrainDirty=true;needsDraw=true;resize();updateUI();}
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
    ground.setTransform(dpr,0,0,dpr,0,0);ground.clearRect(0,0,width,height);
    ground.save();ground.translate(camera.x,camera.y);ground.scale(camera.zoom,camera.zoom);ground.drawImage(soil,0,0,width,height);
    drawSoilDetail(ground);
    ground.save();soilOutline(ground);ground.clip();ground.lineCap='round';ground.lineJoin='round';
    // Filled, overlapping contours form one excavation: no outlined segment caps
    // or chamber rims across a connected passage. Width follows stable soil relief.
    const geometryKey=[colony.seed,colony.nodes.length,colony.links.length,colony.junctions.length,cw,ch].join(':');
    if(excavationCache?.key!==geometryKey)excavationCache={key:geometryKey,walls:excavationShape(1),shoulder:excavationShape(.93),interior:excavationShape(.84)};
    const {walls,shoulder,interior}=excavationCache;
    ground.fillStyle='#907653';ground.fill(walls);ground.fillStyle='#ad9067';ground.fill(shoulder);
    ground.save();ground.clip(walls);
    const cavity=ground.createLinearGradient(0,0,0,height);
    cavity.addColorStop(0,'#c5ae86');cavity.addColorStop(.5,'#b49a70');cavity.addColorStop(1,'#a48b64');
    ground.fillStyle=cavity;ground.save();ground.translate(0,.10*ch);ground.fill(interior);ground.restore();
    // Fine grains remain on the back wall; cavity grain contrast is lower than
    // packed soil, with scattered fallen particles on the lower edges.
    ground.globalAlpha=.17;ground.fillStyle=sandPattern;ground.fill(walls);ground.globalAlpha=1;
    for(let id=117;id<colony.nodes.length;id++){
      const n=colony.nodes[id],p=colony.nodes[n.parent];if(!p)continue;
      for(let i=0;i<5;i++){const t=(i+.3)/5,point=passagePoint(p,n,t),angle=Math.atan2((n.y-p.y)*ch,(n.x-p.x)*cw),radius=passageRadius(p,n,t),side=i%2?1:-1;
        const x=point.x*cw-Math.sin(angle)*radius*cw*side*.93,y=point.y*ch+Math.cos(angle)*radius*ch*side*.93;
        ground.fillStyle=i%2?'#eed6a96b':'#614c365e';ground.beginPath();ground.ellipse(x,y,cw*(.027+(id%3)*.009),ch*.024,id+i,0,Math.PI*2);ground.fill();
      }
    }
    ground.restore();
    // A warm nest chamber makes the homeward traffic legible.
    const home=colony.nodes[colony.nest],nest=ground.createRadialGradient(home.x*cw,home.y*ch,0,home.x*cw,home.y*ch,8*Math.max(cw,ch));nest.addColorStop(0,'#c7a36d18');nest.addColorStop(1,'#c7a36d00');ground.fillStyle=nest;ground.fillRect((home.x-4)*cw,(home.y-3)*ch,8*cw,6*ch);for(const id of colony.exits){const n=colony.nodes[id],y=surfaceY(n.x)*ch;
      ground.strokeStyle='#b59b70';ground.lineWidth=.65*Math.min(cw,ch);ground.beginPath();ground.moveTo(n.x*cw,y);ground.lineTo(n.x*cw,n.y*ch);ground.stroke();
      ground.fillStyle='#5e4a2e';ground.beginPath();ground.ellipse(n.x*cw,y,.58*cw,.23*ch,0,0,Math.PI*2);ground.fill();
      ground.strokeStyle='#b69a6d';ground.lineWidth=Math.max(.65,cw*.08);ground.beginPath();ground.ellipse(n.x*cw,y+.04*ch,.66*cw,.27*ch,0,0,Math.PI);ground.stroke();
      ground.fillStyle='#b99d70';for(let k=0;k<26;k++){const dx=(k%2?1:-1)*(.9+(k%13)*.18),x=n.x+dx;ground.beginPath();ground.ellipse(x*cw,(surfaceY(x)+.15+(k%3)*.13)*ch,.09*cw,.06*ch,k,0,7);ground.fill();}
    }
    ground.restore();ground.restore();terrainDirty=false;
  }
  function passagePoint(a,b,t){
    const dx=b.x-a.x,dy=b.y-a.y,bend=a.kind==='surface'&&b.kind==='surface'?0:Math.sin((a.x+b.x)*3.65+(a.y+b.y)*1.55)*.07*(a.x<b.x||a.x===b.x&&a.y<b.y?1:-1);
    return{x:a.x+dx*t-dy*bend*2*t*(1-t),y:a.y+dy*t+dx*bend*2*t*(1-t)};
  }
  function passageRadius(a,b,t){
    const point=passagePoint(a,b,t);
    return .64+.09*Math.sin(point.x*.83+point.y*.57)+.035*Math.sin(point.x*4.7-point.y*3.2);
  }
  function excavationShape(inset){
    const path=new Path2D();
    const segment=(a,b)=>{
      const dx=b.x-a.x,dy=b.y-a.y,length=Math.hypot(dx,dy)||1,steps=Math.max(6,Math.ceil(length*7));
      for(const side of [-1,1])for(let k=0;k<=steps;k++){
        const t=side<0?k/steps:1-k/steps,point=passagePoint(a,b,t),r=passageRadius(a,b,t)*inset;
        const x=(point.x-dy/length*r*side)*cw,y=(point.y+dx/length*r*side)*ch;
        if(side===-1&&k===0)path.moveTo(x,y);else path.lineTo(x,y);
      }
      path.closePath();
    };
    for(const n of colony.nodes){const p=colony.nodes[n.parent];if(p&&n.kind!=='surface')segment(p,n);}
    for(const [a,b]of [...colony.links,...colony.junctions])segment(colony.nodes[a],colony.nodes[b]);
    for(let id=117;id<colony.nodes.length;id++){
      const n=colony.nodes[id],r=passageRadius(n,n,0)*inset;
      path.moveTo((n.x+r)*cw,n.y*ch);path.ellipse(n.x*cw,n.y*ch,r*cw,r*ch,0,0,Math.PI*2);
      if(n.kind!=='chamber'&&id!==colony.nest)continue;
      const home=id===colony.nest,rx=(home?4.9:1.8)-(1-inset)*.8,ry=(home?2.7:1.1)-(1-inset)*.8;
      // Broad lobes, small excavated notches and an uneven floor replace ovals.
      for(let k=0;k<=64;k++){const angle=k*Math.PI/32,wave=1+.085*Math.sin(angle*3+id)+.045*Math.sin(angle*7-id*.7)+.018*Math.sin(angle*17+id),x=(n.x+Math.cos(angle)*rx*wave)*cw,y=(n.y+Math.sin(angle)*ry*wave)*ch;if(!k)path.moveTo(x,y);else path.lineTo(x,y);}path.closePath();
    }
    return path;
  }
  function antPosition(ant){
    const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],length=Math.hypot(b.x-a.x,b.y-a.y)||1;
    const tempo=.88+.12*Math.sin((colony.time+.1)*3.1+ant.id*2.4);
    const t=Math.min(1,ant.phase+(!paused&&ant.wait<=0&&ant.phase<1?accumulator*ant.pace*tempo/length*(ant.carrying?.75:1)*(colony.starvationSeconds>600?.65:1):0));
    const surface=a.kind==='surface'&&b.kind==='surface',lane=surface?0:((ant.id%3)-1)*.11*Math.sin(Math.PI*t),spread=ant.id*2.39996,rad=.5+(ant.id%8)/8,weight=(ant.from===colony.nest?1-t:0)+(ant.cell===colony.nest?t:0);
    const center=passagePoint(a,b,t),tangent=passagePoint(a,b,Math.min(1,t+.01)),behind=passagePoint(a,b,Math.max(0,t-.01));
    let worldX=center.x+Math.cos(spread)*rad*1.5*weight;
    let worldY=(surface?surfaceY(worldX):center.y+(a.kind==='surface'?(surfaceY(a.x)-a.y)*(1-t):0)+(b.kind==='surface'?(surfaceY(b.x)-b.y)*t:0)+Math.sin(spread)*rad*.65*weight);
    if(ant.role==='nurse'&&ant.cell===colony.nest&&ant.phase>=1){
      // Small tending paths stay beside the brood, clear of the queen's body.
      const home=colony.nodes[colony.nest],time=colony.time+(!paused?accumulator:0),motion=reduced.matches?0:Math.sin(time*.18+ant.id)*.15;
      worldX=home.x+1.65+Math.cos(spread)*1.25+motion;worldY=home.y+Math.sin(spread)*1.1+motion*.5;
    }
    return {x:worldX*cw+Math.sin(ant.dir)*lane*cw,y:worldY*ch-Math.cos(ant.dir)*lane*ch,worldX,surface,heading:Math.atan2((tangent.y-behind.y)*ch,(tangent.x-behind.x)*cw)};
  }
  let soilGrains=null,soilSeed=null,sandPattern=null;
  function drawSoilDetail(layer){
    if(soilSeed!==colony.seed){
      soilSeed=colony.seed;let seed=colony.seed||1;const random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;};
      const tile=document.createElement('canvas');tile.width=tile.height=768;const material=tile.getContext('2d');
      material.fillStyle='#d0bd97';material.fillRect(0,0,768,768);
      // Close-packed, differently sized mineral grains, with a consistent light
      // direction. The texture is fixed in world space, so zoom reveals grains.
      const colors=['#a38b65','#b59b72','#c5ad84','#d5c29d','#e4d3b1','#ecdfc1','#f4e8cc'];
      for(let i=0;i<85000;i++){
        const x=random()*768,y=random()*768,r=.65+Math.pow(random(),2)*2.15,angle=random()*Math.PI,shade=Math.floor(random()*colors.length);
        material.fillStyle=colors[shade];material.beginPath();
        for(let k=0;k<6;k++){const a=angle+k*Math.PI/3,rr=r*(.72+random()*.28);if(!k)material.moveTo(x+Math.cos(a)*rr,y+Math.sin(a)*rr*.8);else material.lineTo(x+Math.cos(a)*rr,y+Math.sin(a)*rr*.8);}material.closePath();material.fill();
        if(r>1.7){material.strokeStyle='#6e543329';material.lineWidth=.3;material.stroke();material.fillStyle='#fff5db55';material.fillRect(x-r*.35,y-r*.4,r*.55,.35);}
      }
      sandPattern=layer.createPattern(tile,'repeat');
      soilGrains=Array.from({length:480},()=>[]);for(let i=0;i<96000;i++){const grain={x:random()*W,y:random()*H,r:.008+Math.pow(random(),6)*.065,shade:random(),angle:random()*Math.PI};soilGrains[Math.min(19,Math.floor(grain.y/H*20))*24+Math.min(23,Math.floor(grain.x/W*24))].push(grain);}
    }
    layer.save();soilOutline(layer);layer.clip();
    sandPattern.setTransform(new DOMMatrix().scale(cw*24/768,ch*24/768));layer.fillStyle=sandPattern;layer.fillRect(0,0,width,height);
    for(let i=0;i<8;i++){const y=(29+i*9)*ch;layer.fillStyle=i%2?'#96774907':'#fff8df0b';layer.beginPath();layer.moveTo(0,y);layer.bezierCurveTo(width*.25,y-2*ch,width*.65,y+2*ch,width,y-ch);layer.lineTo(width,y+2*ch);layer.bezierCurveTo(width*.65,y+5*ch,width*.25,y,width,y+ch);layer.lineTo(0,y+3*ch);layer.fill();}
    const scale=camera.zoom,left=-camera.x/scale,right=(width-camera.x)/scale,top=-camera.y/scale,bottom=(height-camera.y)/scale;
    const firstCol=Math.max(0,Math.floor(left/width*24)),lastCol=Math.min(23,Math.floor(right/width*24)),firstRow=Math.max(0,Math.floor(top/height*20)),lastRow=Math.min(19,Math.floor(bottom/height*20));
    for(let row=firstRow;row<=lastRow;row++)for(let col=firstCol;col<=lastCol;col++)for(const grain of soilGrains[row*24+col]){const x=grain.x*cw,y=grain.y*ch,r=grain.r*Math.min(cw,ch);if(x<left-r||x>right+r||y<top-r||y>bottom+r||r*scale*dpr<.3)continue;
      layer.fillStyle=grain.shade<.18?'#76634355':grain.shade<.48?'#b4a17e88':grain.shade<.85?'#f7edd699':'#fff9e7bb';layer.beginPath();for(let i=0;i<5;i++){const angle=grain.angle+i*Math.PI*2/5,rx=r*(.7+.25*Math.sin(i*2.3+grain.angle));if(i===0)layer.moveTo(x+Math.cos(angle)*rx,y+Math.sin(angle)*rx*.72);else layer.lineTo(x+Math.cos(angle)*rx,y+Math.sin(angle)*rx*.72);}layer.closePath();layer.fill();
      if(r*scale>1.4){layer.strokeStyle='#8d795733';layer.lineWidth=.025*Math.min(cw,ch);layer.stroke();}
    }
    layer.restore();
  }
  function zoomTo(value,x=width/2,y=height/2){
    const next=Math.max(1,Math.min(16,value)),ratio=next/camera.zoom;
    camera.x=x-(x-camera.x)*ratio;camera.y=y-(y-camera.y)*ratio;camera.zoom=next;clampCamera();terrainDirty=true;needsDraw=true;
    canvas.style.touchAction=next>1?'pinch-zoom':'auto';get('magnification').value=next;get('zoom-label').textContent=next.toFixed(1)+'×';get('zoom-reset').hidden=next===1;get('zoom-out').disabled=next<=1;get('zoom-in').disabled=next>=16;
  }
  get('magnification').oninput=event=>{following=false;zoomTo(Number(event.target.value));};
  get('zoom-in').onclick=()=>{following=false;zoomTo(camera.zoom*2);};
  get('zoom-out').onclick=()=>{following=false;zoomTo(camera.zoom/2);};
  get('zoom-reset').onclick=()=>{following=false;zoomTo(1);};
  get('view-ant').onclick=()=>{if(!positions.has(selectedId))return;following=true;zoomTo(12);observe(false);};
  let drag=null,dragMoved=false;
  canvas.addEventListener('pointerdown',event=>{dragMoved=false;if(camera.zoom<=1)return;drag={id:event.pointerId,x:event.clientX,y:event.clientY,startX:camera.x,startY:camera.y};canvas.setPointerCapture(event.pointerId);});
  canvas.addEventListener('pointermove',event=>{if(!drag||drag.id!==event.pointerId)return;const dx=event.clientX-drag.x,dy=event.clientY-drag.y;if(Math.hypot(dx,dy)<5&&!dragMoved)return;dragMoved=true;following=false;camera.x=drag.startX+dx;camera.y=drag.startY+dy;clampCamera();terrainDirty=true;needsDraw=true;});
  canvas.addEventListener('pointerup',()=>{drag=null;});canvas.addEventListener('pointercancel',()=>{drag=null;});
  const facings=new Map(),strides=new Map();
  function draw(){
    if(!width||!height)return;needsDraw=false;
    const poseTime=colony.time+(!paused?accumulator:0),poseDelta=Math.min(.15,Math.max(0,(performance.now()-lastPoseTime)/1000));lastPoseTime=performance.now();
    for(const ant of colony.ants){const point=antPosition(ant),old=positions.get(ant.id);if(old&&!paused&&Math.hypot(point.x-old.x,point.y-old.y)<Math.max(cw,ch)*2){const blend=1-Math.exp(-poseDelta*32);point.x=old.x+(point.x-old.x)*blend;point.y=old.y+(point.y-old.y)*blend;}positions.set(ant.id,point);}const aliveIds=new Set(colony.ants.map(a=>a.id));for(const id of positions.keys())if(id!=='queen'&&!aliveIds.has(id))positions.delete(id);
    const homePosition=colony.nodes[colony.nest];positions.set('queen',{x:(homePosition.x-1.7)*cw,y:homePosition.y*ch});
    if(following&&positions.has(selectedId)){const point=positions.get(selectedId);const oldX=camera.x,oldY=camera.y;camera.x=width/2-point.x*camera.zoom;camera.y=height/2-point.y*camera.zoom;clampCamera();terrainDirty ||= oldX!==camera.x||oldY!==camera.y;}
    if(terrainDirty)updateTerrain();ctx.clearRect(0,0,width,height);ctx.drawImage(terrain,0,0,width,height);
    ctx.save();ctx.translate(camera.x,camera.y);ctx.scale(camera.zoom,camera.zoom);
    if(showTrails){
      const strongest=Math.max(0,...colony.trail);ctx.save();ctx.lineCap='round';ctx.lineJoin='round';
      const route=(n,p)=>{const y=point=>point.kind==='surface'?surfaceY(point.x):point.y;ctx.beginPath();ctx.moveTo(n.x*cw,y(n)*ch);ctx.lineTo(p.x*cw,y(p)*ch);};
      // Visits and food signals are different observations. Show the former as
      // dashes even when pheromones have faded, without inventing food signals.
      ctx.strokeStyle='#8136b4b8';ctx.lineWidth=Math.max(1.4/camera.zoom,Math.min(cw,ch)*.18);ctx.setLineDash([Math.max(3/camera.zoom,Math.min(cw,ch)*.5),Math.max(2.5/camera.zoom,Math.min(cw,ch)*.3)]);
      for(let i=0;i<colony.nodes.length;i++){const n=colony.nodes[i],p=colony.nodes[n.parent];if(!p||!colony.visits[i]||!colony.visits[n.parent])continue;route(n,p);ctx.stroke();}
      ctx.setLineDash([]);ctx.lineWidth=Math.max(2/camera.zoom,Math.min(cw,ch)*.325);
      if(strongest>0)for(let i=0;i<colony.trail.length;i++){const strength=colony.trail[i];if(strength<=0)continue;const n=colony.nodes[i],p=colony.nodes[n.parent];if(!p)continue;ctx.strokeStyle=`rgba(185,57,255,${.45+.5*Math.sqrt(strength/strongest)})`;route(n,p);ctx.stroke();}
      ctx.restore();
    }
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
    for(const ant of colony.ants){const a=colony.nodes[ant.from],b=colony.nodes[ant.cell],{x,y,worldX,surface,heading}=positions.get(ant.id);
      const moving=ant.phase<1&&ant.wait<=0||ant.role==='nurse'&&ant.cell===colony.nest&&!reduced.matches,scanning=!moving&&ant.work<0&&ant.wait>.8?[0,.35,0,-.3][Math.floor(colony.time*.7+ant.id*1.61)%4]:0;
      const direction=Math.sign(b.x-a.x)||1,target=(a===b?ant.dir:surface?Math.atan2((surfaceY(worldX+.08*direction)-surfaceY(worldX-.08*direction))*ch,.16*direction*cw):heading),old=facings.get(ant.id)??target,turn=Math.atan2(Math.sin(target-old),Math.cos(target-old)),angle=old+turn*(1-Math.exp(-poseDelta*9));facings.set(ant.id,angle);
      let pose=strides.get(ant.id);if(!pose)pose={x,y,gait:ant.id*2.39996};
      const distance=Math.hypot(x-pose.x,y-pose.y);if(!paused&&moving&&distance<Math.max(cw,ch)*2)pose.gait+=distance/r*Math.PI*.55;pose.x=x;pose.y=y;strides.set(ant.id,pose);
      ctx.save();ctx.translate(x,y);ctx.rotate(angle+(moving?Math.sin(pose.gait*2)*.018:0));drawAnt(ctx,r,{...ant,moving,turn,detail:r*camera.zoom,callow:colony.time-ant.bornAt<180,headYaw:Math.max(-.22,Math.min(.22,turn*.32))+(!moving&&ant.work<0?Math.sin(poseTime*1.2+ant.id)*.065+scanning*.45:0)},pose.gait,colony.time+(!paused?accumulator:0));ctx.restore();
      if(ant.id===selectedId){ctx.strokeStyle='#876838aa';ctx.lineWidth=1/camera.zoom;ctx.beginPath();ctx.arc(x,y,r*3.5,0,Math.PI*2);ctx.stroke();ctx.fillStyle='#3e3020';ctx.font=(12/camera.zoom)+'px system-ui';ctx.fillText('#'+ant.id,x+r*6,y-r*3);}
    }
    if(colony.queen){
      const time=colony.time+(!paused?accumulator:0),alive=colony.queen.alive,motion=alive&&!reduced.matches?1:0,x=(home.x-1.7)*cw+Math.sin(time*.38)*r*.23*motion,y=home.y*ch+Math.sin(time*.51)*r*.14*motion;
      ctx.save();ctx.translate(x,y);ctx.rotate(Math.sin(time*.32)*.055*motion);ctx.scale(1+Math.sin(time*1.1)*.012*motion,1);drawAnt(ctx,r*1.85,{id:-1,queen:true,dead:!alive,restingMotion:motion,detail:r*camera.zoom*1.85,moving:false,work:-1,carrying:0},0,time);ctx.restore();
      if(selectedId==='queen'){ctx.strokeStyle='#9b672599';ctx.lineWidth=1.5/camera.zoom;ctx.beginPath();ctx.ellipse(x,y,r*6.4,r*4,0,0,Math.PI*2);ctx.stroke();}
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
    const signature=(colony.queen?'queen,':'')+colony.ants.map(a=>a.id+':'+a.role).join(',');
    if(signature!==antSignature){antSignature=signature;const live=new Set(colony.ants.map(a=>a.id));for(const id of facings.keys())if(!live.has(id)){facings.delete(id);strides.delete(id);}const options=[];if(colony.queen){const queen=document.createElement('option');queen.value='queen';queen.textContent='Queen';options.push(queen);}for(const [role,label] of [['nurse','Nurses'],['forage','Foragers'],['dig','Diggers'],['rest','Resting workers']]){const ants=colony.ants.filter(a=>a.role===role);if(!ants.length)continue;const group=document.createElement('optgroup');group.label=label+' ('+ants.length+')';for(const ant of ants){const o=document.createElement('option');o.value=ant.id;o.textContent='#'+ant.id+' · '+(role==='nurse'?'nurse':role==='forage'?'forager':role==='dig'?'digger':'resting');group.append(o);}options.push(group);}const empty=document.createElement('option');empty.value='';empty.textContent='Choose an ant';get('ant-select').replaceChildren(empty,...options);get('ant-select').value=selectedId===null?'':String(selectedId);}
    get('view-ant').disabled=selectedId===null||!positions.has(selectedId);
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
    else{fullscreenState(true);try{
      // Touch browsers reserve downward swipes to leave native fullscreen.
      // Keep touch exploration in our viewport layout so those swipes can pan.
      if(!navigator.maxTouchPoints&&!matchMedia('(pointer: coarse)').matches&&farm.requestFullscreen)await farm.requestFullscreen();
    }catch{/* Embedded browsers still get the full-viewport layout. */}}
  };
  document.addEventListener('fullscreenchange',()=>fullscreenState(!!document.fullscreenElement));
  // Desktop wheel zoom stays anchored to the pointer. Touch and Ctrl-wheel
  // retain the browser's native page zoom.
  canvas.addEventListener('wheel',event=>{
    if(event.ctrlKey||!matchMedia('(pointer: fine)').matches)return;
    event.preventDefault();const box=canvas.getBoundingClientRect(),x=event.clientX-box.left,y=event.clientY-box.top;
    const delta=event.deltaY*(event.deltaMode===1?16:event.deltaMode===2?height:1);following=false;zoomTo(camera.zoom*Math.exp(-delta*.0015),x,y);
  },{passive:false});
  canvas.addEventListener('click',event=>{
    const box=canvas.getBoundingClientRect(),x=(event.clientX-box.left-camera.x)/camera.zoom/cw,y=(event.clientY-box.top-camera.y)/camera.zoom/ch;
    if(dragMoved)return;let nearest=null,distance=Infinity;
    for(const [id,point] of positions){const radius=id==='queen'?6:2.5,d=Math.hypot(x*cw-point.x,y*ch-point.y);if(d<Math.max(14/camera.zoom,radius*Math.min(cw,ch)*.4)&&d<distance){nearest=id;distance=d;}}
    if(nearest!==null){selectedId=nearest;get('ant-select').value=String(selectedId);updateUI();needsDraw=true;}
  });
  get('trails').onclick=()=>{showTrails=!showTrails;get('trails').setAttribute('aria-pressed',String(showTrails));feedback(get('trails'),showTrails?(colony.trail.some(n=>n>0)||colony.visits.some(n=>n>0)?'Dashed purple marks show visited routes. Brighter lines show relative food signals.':'No trails yet. Let the ants explore and carry food home.'):'Trails hidden.');needsDraw=true;};
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
