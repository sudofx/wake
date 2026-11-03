/* Perspective is a view transform of the native 7×7×7 matrix coordinates. */
// Numeric labels follow the frozen row-major grammar, never draw depth or
// selection order. Position fallback keeps older live snapshots readable.
window.WakeMatrixCellLabel = (cell,matrix) => {
  if(!cell)return '';
  const ordinal=Number.isInteger(cell.ordinal)?cell.ordinal:
    cell.position.reduce((value,index,axis)=>value*matrix.axes[axis].values.length+index,0)+1;
  return `#${String(ordinal).padStart(3,'0')}`;
};
window.WakeResearchCube = canvas => {
  const context=canvas.getContext('2d');
  let matrix=null,selected='',previous='',yaw=.65,pitch=-.45,zoom=.6,hovered='',moving=false,timer=0,last=0,heldUntil=0,drag=null,points=[],visible=false,pointerFrame=0,pendingPointer=null;
  const corners=[[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]];
  const edges=[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
  // Fixed scale: the same recorded score keeps the same color across snapshots.
  const scoreStops=[[0,[190,60,55]],[.5,[205,135,55]],[.75,[48,176,185]],[1,[75,200,245]]];
  const scoreColor=score=>{
    if(typeof score!=='number'||!Number.isFinite(score)||score<0||score>1)return null;
    const right=scoreStops.findIndex(([stop])=>stop>=score),[high,b]=scoreStops[right], [low,a]=scoreStops[Math.max(0,right-1)];
    const t=high===low?0:(score-low)/(high-low);
    return `rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*t)).join(',')})`;
  };
  const legend=document.getElementById('cube-heatmap-legend');
  if(legend){
    legend.innerHTML='<strong>Recorded continuity score · higher is better</strong><div class="cube-score-scale" aria-hidden="true"></div><div class="cube-score-ticks"><span>0% · Low</span><span>50% · Middle</span><span>100% · High</span></div><p><span class="cube-unscored" aria-hidden="true">□</span> Unfilled = no recorded score. More results reveal more of the pattern.</p>';
    legend.querySelector('.cube-score-scale').style.background=`linear-gradient(to right,${scoreStops.map(([stop])=>`${scoreColor(stop)} ${stop*100}%`).join(',')})`;
  }
  const faces=[{normal:[0,0,-1],vertices:[0,1,2,3]},{normal:[0,0,1],vertices:[4,5,6,7]},{normal:[-1,0,0],vertices:[0,3,7,4]},{normal:[1,0,0],vertices:[1,2,6,5]},{normal:[0,-1,0],vertices:[0,1,5,4]},{normal:[0,1,0],vertices:[3,2,6,7]}];
  const turn=([x,y,z])=>{const a=x*Math.cos(yaw)+z*Math.sin(yaw),b=-x*Math.sin(yaw)+z*Math.cos(yaw);return[a,y*Math.cos(pitch)-b*Math.sin(pitch),y*Math.sin(pitch)+b*Math.cos(pitch)];};
  const project=(point,w,h,scale)=>{const [x,y,z]=turn(point),p=7/(7-z*.32);return{x:w*.5+x*scale*p,y:h*.51+y*scale*p,z};};
  const canvasDpr=()=>Math.min(matchMedia('(max-width:700px)').matches?1.25:2,devicePixelRatio||1);
  const collapsed=()=>canvas.closest('.console-module')?.classList.contains('module-collapsed');
  let liveCoordinate='';
  const reducedMotion=matchMedia('(prefers-reduced-motion: reduce)');
  const shouldAnimate=()=>(moving||(liveCoordinate&&!reducedMotion.matches))&&visible&&!document.hidden&&!collapsed();

  function draw(){
    if(!visible||collapsed())return;
    const w=canvas.clientWidth,h=canvas.clientHeight;if(!w||!h)return;
    const dpr=canvasDpr(),targetW=Math.round(w*dpr),targetH=Math.round(h*dpr);
    if(canvas.width!==targetW||canvas.height!==targetH){canvas.width=targetW;canvas.height=targetH;}
    context.setTransform(dpr,0,0,dpr,0,0);context.clearRect(0,0,w,h);
    if(!matrix)return;
    const style=getComputedStyle(document.body),cyan=style.getPropertyValue('--cyan').trim(),muted=style.getPropertyValue('--muted').trim(),line=style.getPropertyValue('--line').trim(),orange=style.getPropertyValue('--orange').trim(),scale=Math.min(w,h)*.145*zoom,axisColors=[cyan,orange,style.getPropertyValue('--violet').trim()];
    [[0,1,2],[1,0,2],[2,0,1]].forEach(([axis,a,b],i)=>{
      const face=[[-1,-1],[1,-1],[1,1],[-1,1]].map(([u,v])=>{const p=[0,0,0];p[axis]=3.26;p[a]=u*3.26;p[b]=v*3.26;return project(p,w,h,scale);});
      context.beginPath();face.forEach((p,j)=>j?context.lineTo(p.x,p.y):context.moveTo(p.x,p.y));context.closePath();context.fillStyle=axisColors[i];context.globalAlpha=.035;context.fill();context.strokeStyle=axisColors[i];context.globalAlpha=.9;context.lineWidth=1.6;context.stroke();context.globalAlpha=1;
    });
    canvas.dataset.axisTargets='positive-outer-faces';
    points=matrix.cells.map(cell=>({...cell,screen:project(cell.position.map(x=>x-3),w,h,scale)})).sort((a,b)=>a.screen.z-b.screen.z);
    const visibleFaces=faces.filter(face=>turn(face.normal)[2]>0);
    points.forEach(cell=>{
      const color=scoreColor(cell.score);
      const v=corners.map(c=>project(cell.position.map((x,i)=>x-3+c[i]*.34),w,h,scale));
      if(color){
        context.fillStyle=color;context.globalAlpha=.38;
        visibleFaces.forEach(face=>{
          context.beginPath();face.vertices.forEach((n,i)=>i?context.lineTo(v[n].x,v[n].y):context.moveTo(v[n].x,v[n].y));context.closePath();context.fill();
        });
      }
      context.strokeStyle=color||muted;context.globalAlpha=color?.85:.18;context.lineWidth=color?1:.65;
      context.beginPath();edges.forEach(([a,b])=>{context.moveTo(v[a].x,v[a].y);context.lineTo(v[b].x,v[b].y);});context.stroke();
    });
    // Live marks are a separate overlay: they never replace recorded score fill.
    canvas.dataset.liveCoordinate=liveCoordinate;
    const inFlight=points.find(cell=>cell.id===liveCoordinate);
    if(inFlight){
      const pulse=reducedMotion.matches?0:(1+Math.sin(performance.now()*.005))/2;
      context.strokeStyle=style.getPropertyValue('--green').trim()||'#4bd59a';
      context.globalAlpha=.65+pulse*.35;context.lineWidth=2;
      context.beginPath();context.arc(inFlight.screen.x,inFlight.screen.y,13+pulse*5,0,Math.PI*2);context.stroke();
      context.globalAlpha=1;
    }
    // Draw inspection marks last; never replace the score fill with a selection color.
    points.filter(cell=>[selected,previous,hovered].includes(cell.id)).forEach(cell=>{
      const isSelected=cell.id===selected,isPrevious=cell.id===previous&&!isSelected;
      context.globalAlpha=1;context.strokeStyle=style.getPropertyValue('--ink').trim();context.lineWidth=isSelected?2:1.5;
      context.setLineDash(isPrevious?[3,3]:[]);
      context.beginPath();
      if(isPrevious)context.arc(cell.screen.x,cell.screen.y,10,0,Math.PI*2);
      else context.rect(cell.screen.x-9,cell.screen.y-9,18,18);
      context.stroke();context.setLineDash([]);
    });
    context.globalAlpha=1;context.font='11px ui-monospace, monospace';context.fillStyle=muted;context.textAlign='center';
    [[3.26,0,0],[0,3.26,0],[0,0,3.26]].forEach((v,i)=>{
      const anchor=project(v,w,h,scale),labels=[[w*.76,26],[w*.26,h-20],[w*.24,26]],[x,y]=labels[i];
      context.strokeStyle=axisColors[i];context.lineWidth=1;context.globalAlpha=.9;context.beginPath();context.moveTo(anchor.x,anchor.y);context.lineTo(x,y+7);context.lineTo(x+25,y+7);context.stroke();context.beginPath();context.arc(anchor.x,anchor.y,2.3,0,Math.PI*2);context.fillStyle=axisColors[i];context.fill();context.fillText(['Question','View','Obstacles'][i],x,y);context.globalAlpha=1;
    });
    canvas.dataset.zoom=String(zoom);canvas.dataset.selected=selected;canvas.dataset.previous=previous;canvas.dataset.hovered=hovered;
  }

  function tick(){
    timer=0;
    if(!shouldAnimate())return;
    const now=performance.now(),dt=last?Math.min(100,now-last):50;last=now;
    if(moving&&!drag&&now>heldUntil)yaw+=dt*.000075;draw();
    timer=setTimeout(tick,50);
  }
  function start(){if(!timer&&shouldAnimate()){last=0;timer=setTimeout(tick,50);}}
  function stop(redraw=false){if(timer)clearTimeout(timer);timer=0;last=0;if(redraw)draw();}
  const select=(id,previousId=previous)=>{selected=id;previous=previousId;draw();};

  canvas.tabIndex=0;
  canvas.addEventListener('pointerdown',event=>{drag={x:event.clientX,y:event.clientY,startX:event.clientX,startY:event.clientY};heldUntil=performance.now()+5000;canvas.setPointerCapture(event.pointerId);});
  canvas.addEventListener('pointermove',event=>{
    pendingPointer={clientX:event.clientX,clientY:event.clientY};
    if(pointerFrame)return;
    pointerFrame=requestAnimationFrame(()=>{
      pointerFrame=0;const e=pendingPointer;pendingPointer=null;if(!e)return;
      if(!drag){const rect=canvas.getBoundingClientRect(),x=e.clientX-rect.left,y=e.clientY-rect.top;const hits=points.filter(c=>Math.hypot(c.screen.x-x,c.screen.y-y)<9).sort((a,b)=>b.screen.z-a.screen.z);hovered=hits[0]?.id||'';canvas.title=hovered?`${window.WakeMatrixCellLabel(hits[0],matrix)} · ${hovered} · ${hits[0].status.replaceAll('_',' ')} · ${scoreColor(hits[0].score)?`score ${Number((hits[0].score*100).toFixed(1))}%`:'score unavailable'}`:'Drag to rotate; hover a coordinate to inspect its definition.';draw();return;}
      yaw+=(e.clientX-drag.x)*.008;pitch=Math.max(-1.35,Math.min(1.35,pitch+(e.clientY-drag.y)*.008));drag.x=e.clientX;drag.y=e.clientY;draw();
    });
  });
  canvas.addEventListener('pointerup',event=>{if(drag&&Math.hypot(event.clientX-drag.startX,event.clientY-drag.startY)<6){const rect=canvas.getBoundingClientRect(),x=event.clientX-rect.left,y=event.clientY-rect.top;const hits=points.filter(c=>Math.hypot(c.screen.x-x,c.screen.y-y)<12).sort((a,b)=>b.screen.z-a.screen.z);if(hits[0]){select(hits[0].id);canvas.dispatchEvent(new CustomEvent('wake-cube-select',{detail:hits[0].id}));}}drag=null;heldUntil=performance.now()+5000;});
  canvas.addEventListener('pointerleave',()=>{hovered='';draw();});
  canvas.addEventListener('pointercancel',()=>{drag=null;});
  canvas.addEventListener('keydown',event=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(event.key)){event.preventDefault();if(event.key==='ArrowLeft')yaw-=.15;if(event.key==='ArrowRight')yaw+=.15;if(event.key==='ArrowUp')pitch-=.15;if(event.key==='ArrowDown')pitch+=.15;heldUntil=performance.now()+5000;draw();}});

  new ResizeObserver(()=>draw()).observe(canvas);
  new MutationObserver(()=>{if(visible)draw();}).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  new IntersectionObserver(entries=>{visible=entries[0]?.isIntersecting===true;if(visible){draw();start();}else stop();},{rootMargin:'120px 0px',threshold:.01}).observe(canvas);
  const panel=canvas.closest('.console-module');if(panel)new MutationObserver(()=>{if(collapsed())stop();else{draw();start();}}).observe(panel,{attributes:true,attributeFilter:['class']});
  document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();else{draw();start();}});

  return {
    update:value=>{matrix=value;selected=matrix.cells.some(c=>c.id===selected)?selected:matrix.cells.find(c=>c.position.every(x=>x===3))?.id||matrix.cells[0]?.id;draw();start();return selected;},
    select,
    rotate:amount=>{yaw+=amount;heldUntil=performance.now()+5000;draw();},
    reset:()=>{yaw=.65;pitch=-.45;zoom=.6;draw();},
    setMotion:value=>{moving=Boolean(value);stop(true);start();},
    setActivity:id=>{liveCoordinate=matrix?.cells.some(c=>c.id===id)?id:'';stop(true);start();},
    getRotation:()=>({yaw,pitch,zoom})
  };
};
