/* Research instruments consume the same disposable snapshot, never authority. */
window.WakeContextMap = canvas => {
  const ctx=canvas.getContext('2d');let graph={nodes:[],edges:[]},mode='sphere',yaw=.3,pitch=-.2,selected='',hover='',drag=null,motion=false,frame=0,points=[];
  function draw(){const w=canvas.clientWidth,h=canvas.clientHeight;if(!w||!h)return;const d=Math.min(2,devicePixelRatio||1);canvas.width=w*d;canvas.height=h*d;ctx.setTransform(d,0,0,d,0,0);const css=getComputedStyle(document.body),color=k=>css.getPropertyValue(k).trim(),cyan=color('--cyan'),orange=color('--orange');
    const kinds=['project','research','notebook','evidence','belief','commitment'];
    points=graph.nodes.map((n,i)=>{const t=i/Math.max(1,graph.nodes.length-1),a=i*2.399963,y=1-2*t,r=Math.sqrt(Math.max(0,1-y*y));let x=Math.cos(a)*r,z=Math.sin(a)*r,v=y;
      if(mode==='3d'){x=(kinds.indexOf(n.kind)-2.5)/2.8;v=((i%7)-3)/3;z=((Math.floor(i/7)%7)-3)/4;}
      if(mode==='2d'){x=Math.cos(a)*Math.sqrt(t);v=Math.sin(a)*Math.sqrt(t);z=0;}
      const X=x*Math.cos(yaw)+z*Math.sin(yaw),Z=-x*Math.sin(yaw)+z*Math.cos(yaw),Y=v*Math.cos(pitch)-Z*Math.sin(pitch),depth=v*Math.sin(pitch)+Z*Math.cos(pitch),scale=Math.min(w*.37,h*.37),p=mode==='2d'?1:4/(4-depth*.3);
      return {...n,x:w/2+X*scale*p,y:h/2+Y*scale*p,z:depth};});
    const byId=new Map(points.map(n=>[n.id,n]));ctx.strokeStyle=cyan;ctx.lineWidth=.6;
    graph.edges.forEach(e=>{const a=byId.get(e.source),b=byId.get(e.target);if(!a||!b)return;const hot=e.source===selected||e.target===selected;ctx.globalAlpha=hot?.9:.13;ctx.strokeStyle=hot?orange:cyan;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();});
    if(mode==='sphere'){ctx.strokeStyle=cyan;ctx.globalAlpha=.18;for(let k=0;k<3;k++){ctx.beginPath();ctx.ellipse(w/2,h/2,Math.min(w*.37,h*.37)+10+k*6,(Math.min(w*.37,h*.37)+10+k*6)*.3,-.15,0,Math.PI*2);ctx.stroke();}}
    points.sort((a,b)=>a.z-b.z).forEach(n=>{const hot=n.id===selected||n.id===hover;ctx.globalAlpha=hot?1:.5+(n.z+1)*.2;ctx.fillStyle=hot?orange:n.detail.status==='completed'?color('--green'):['parked','open'].includes(n.detail.status)?orange:n.detail.status==='failed'?color('--red'):cyan;ctx.beginPath();ctx.arc(n.x,n.y,hot?6:n.kind==='project'?4:2,0,Math.PI*2);ctx.fill();if(mode==='3d'){const r=hot?8:n.kind==='project'?6:3;ctx.strokeStyle=ctx.fillStyle;ctx.lineWidth=hot?1.5:.7;ctx.beginPath();ctx.moveTo(n.x-r,n.y-r*.5);ctx.lineTo(n.x,n.y-r);ctx.lineTo(n.x+r,n.y-r*.5);ctx.lineTo(n.x+r,n.y+r*.5);ctx.lineTo(n.x,n.y+r);ctx.lineTo(n.x-r,n.y+r*.5);ctx.closePath();ctx.moveTo(n.x,n.y);ctx.lineTo(n.x,n.y+r);ctx.moveTo(n.x-r,n.y-r*.5);ctx.lineTo(n.x,n.y);ctx.lineTo(n.x+r,n.y-r*.5);ctx.stroke();}});ctx.globalAlpha=1;canvas.dataset.selected=selected;canvas.dataset.hovered=hover;
  }
  function animate(){if(motion&&!document.hidden&&!drag){yaw+=.0015;draw();}frame=requestAnimationFrame(animate);}
  const hit=e=>{const r=canvas.getBoundingClientRect();return points.filter(n=>Math.hypot(n.x-e.clientX+r.left,n.y-e.clientY+r.top)<9).sort((a,b)=>b.z-a.z)[0];};
  canvas.tabIndex=0;canvas.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,sx:e.clientX,sy:e.clientY};canvas.setPointerCapture(e.pointerId);});
  canvas.addEventListener('pointermove',e=>{if(drag){yaw+=(e.clientX-drag.x)*.008;pitch+=(e.clientY-drag.y)*.008;drag.x=e.clientX;drag.y=e.clientY;}else{const n=hit(e);hover=n?.id||'';canvas.title=n?`${n.kind}: ${n.title}`:'Drag to turn the recorded graph';}draw();});
  canvas.addEventListener('pointerup',e=>{if(drag&&Math.hypot(e.clientX-drag.sx,e.clientY-drag.sy)<6){const n=hit(e);if(n){selected=n.id;canvas.dispatchEvent(new CustomEvent('wake-graph-select',{detail:n.id}));}}drag=null;draw();});canvas.addEventListener('pointercancel',()=>drag=null);canvas.addEventListener('pointerleave',()=>{hover='';draw();});canvas.addEventListener('keydown',e=>{if(e.key.startsWith('Arrow')){e.preventDefault();yaw+=e.key==='ArrowLeft'?-.15:e.key==='ArrowRight'?.15:0;pitch+=e.key==='ArrowUp'?-.15:e.key==='ArrowDown'?.15:0;draw();}});
  new ResizeObserver(draw).observe(canvas);new MutationObserver(draw).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  return {update:(g,id)=>{graph=g;selected=id;draw();},view:v=>{mode=v;if(v==='2d'){yaw=0;pitch=0;}draw();},setMotion:v=>{motion=v;cancelAnimationFrame(frame);if(v)frame=requestAnimationFrame(animate);else draw();}};
};
