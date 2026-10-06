/*
 * WAKE✳︎ PROCESS FIELD
 * A presentation of observable record/process activity.
 * It is explicitly not a visualization of model cognition or consciousness.
 */
(() => {
  'use strict';
  const canvas=document.getElementById('process-field-canvas');
  if(!canvas)return;
  const ctx=canvas.getContext('2d');
  const panel=canvas.closest('.process-field-panel');
  const stageList=document.getElementById('process-field-stages');
  const statusEl=document.getElementById('process-field-status');
  const traceEl=document.getElementById('process-field-trace');
  const detailEl=document.getElementById('process-field-detail');
  const toggle=document.getElementById('process-field-motion');
  const actions=document.getElementById('execution-state');
  const reduced=matchMedia?.('(prefers-reduced-motion: reduce)').matches;

  const STAGES=[
    ['record','RECORD'],
    ['context','CONTEXT'],
    ['proposal','PROPOSAL'],
    ['governance','GOVERNANCE'],
    ['transition','TRANSITION'],
    ['receipt','RECEIPT']
  ];
  let projection=null,latest=null,frame=null,start=performance.now(),motion=!reduced,visible=true;
  let nodePositions=[],recordEdges=[],recordNodes=[],lastVersion=null,flashUntil=0;

  const hash=value=>{let h=2166136261;for(const ch of String(value||''))h=Math.imul(h^ch.charCodeAt(0),16777619);return h>>>0;};
  const stageState=w=>{
    if(!w)return [true,false,false,false,false,false];
    const terminal=['accepted','rejected','failed','deferred','recovered'].includes(w.status);
    const proposal=Boolean(w.proposal?.title||(w.proposal?.actions||[]).length);
    return [
      true,
      Boolean(w.context?.available),
      proposal,
      terminal,
      w.status==='accepted',
      Boolean(w.receipt?.available)
    ];
  };
  const stateLabel=(w,index)=>{
    if(index===0)return projection?`state ${Number(projection.version||0).toLocaleString('en-US')}`:'loading';
    if(!w)return 'not recorded';
    if(index===1)return w.context?.available?`${Number(w.context.characters||0).toLocaleString('en-US')} chars`:'outside tail';
    if(index===2)return w.proposal?.title||((w.proposal?.actions||[]).length?`${w.proposal.actions.length} action${w.proposal.actions.length===1?'':'s'}`:'not recorded');
    if(index===3)return ['accepted','rejected','failed','deferred','recovered'].includes(w.status)?w.status:'pending';
    if(index===4)return w.status==='accepted'?'committed':'no accepted transition';
    if(index===5)return w.receipt?.available?`event ${w.receipt.seq}`:'outside tail';
    return '';
  };
  function escapeHtml(value){return String(value??'').replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));}
  function setStageReadout(){
    const active=stageState(latest);
    stageList.innerHTML=STAGES.map(([key,label],i)=>`<div class="process-stage ${active[i]?'observed':'quiet'}" data-stage="${key}"><span>0${i+1}</span><strong>${label}</strong><small>${escapeHtml(stateLabel(latest,i))}</small></div>`).join('');
    const runner=actions?.dataset.state||'unknown';
    const running=runner==='running'||runner==='campaign';
    statusEl.textContent=running?'EXECUTION ACTIVE':'EXECUTION '+(runner==='stopped'?'STOPPED':'STATUS UNKNOWN');
    statusEl.dataset.state=running?'running':runner;
    traceEl.textContent=latest?`Latest recorded wake · ${latest.status||'unknown'}`:'Waiting for a recorded wake';
    detailEl.textContent=running
      ?'The runner is active. WAKE does not currently expose the exact in-flight kernel step, so the moving trace below replays the latest recorded wake rather than pretending to show hidden model thought.'
      :'The field replays observable WAKE activity from the durable projection. Motion is presentation; nodes and relationships come from recorded data.';
  }
  function buildRecordField(){
    const graph=projection?.graph;
    if(!graph?.nodes?.length){recordNodes=[];recordEdges=[];return;}
    const limit=110;
    const nodes=graph.nodes.slice(-limit);
    const ids=new Set(nodes.map(n=>n.id));
    recordNodes=nodes.map((n,i)=>{
      const h=hash(n.id),a=(h%6283)/1000,r=.15+((h>>>8)%1000)/1000*.36;
      return {id:n.id,kind:n.kind,a,r,phase:((h>>>16)%1000)/1000*Math.PI*2,index:i};
    });
    recordEdges=(graph.edges||[]).filter(e=>ids.has(e.source)&&ids.has(e.target)).slice(-180);
  }

  function resize(){
    const w=canvas.clientWidth,h=canvas.clientHeight,dpr=Math.min(devicePixelRatio||1,2);
    const tw=Math.round(w*dpr),th=Math.round(h*dpr);
    if(canvas.width!==tw||canvas.height!==th){canvas.width=tw;canvas.height=th;}
    ctx.setTransform(dpr,0,0,dpr,0,0);
    return {w,h};
  }
  function palette(){
    const s=getComputedStyle(document.body);
    return {
      cyan:s.getPropertyValue('--cyan').trim()||'#00d9ee',
      orange:s.getPropertyValue('--orange').trim()||'#ff9d38',
      green:s.getPropertyValue('--green').trim()||'#55db9a',
      red:s.getPropertyValue('--red').trim()||'#ff655c',
      violet:s.getPropertyValue('--violet').trim()||'#b69bff',
      ink:s.getPropertyValue('--ink').trim()||'#caeaf5',
      muted:s.getPropertyValue('--muted').trim()||'#85adbf',
      line:s.getPropertyValue('--line').trim()||'#125064'
    };
  }
  function draw(){
    if(!visible)return;
    const {w,h}=resize();if(!w||!h)return;
    const p=palette(),now=performance.now(),t=(now-start)/1000;
    ctx.clearRect(0,0,w,h);
    const cx=w*.5,cy=h*.49,small=w<700,scale=Math.min(w,h);
    const drift=motion ? .015 : 0;
    nodePositions=recordNodes.map(n=>{
      const angle=n.a+t*drift*((n.index%3)-1);
      const rr=n.r*scale*(.88+.08*Math.sin(t*.18+n.phase));
      return {id:n.id,x:cx+Math.cos(angle)*rr*1.55,y:cy+Math.sin(angle)*rr*.82};
    });
    const byId=new Map(nodePositions.map(n=>[n.id,n]));

    ctx.lineWidth=.55;
    recordEdges.forEach(e=>{
      const a=byId.get(e.source),b=byId.get(e.target);if(!a||!b)return;
      ctx.strokeStyle=p.line;ctx.globalAlpha=.22;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();
    });
    nodePositions.forEach((pt,i)=>{
      ctx.fillStyle=i%9===0?p.violet:p.cyan;ctx.globalAlpha=i%9===0?.45:.24;
      ctx.beginPath();ctx.arc(pt.x,pt.y,i%11===0?2.4:1.35,0,Math.PI*2);ctx.fill();
    });

    const active=stageState(latest);
    const margin=small?28:54;
    const y=cy;
    const points=STAGES.map((_,i)=>({x:margin+(w-margin*2)*(i/(STAGES.length-1)),y:y+Math.sin(i*1.7)*scale*.035}));
    ctx.globalAlpha=.42;ctx.strokeStyle=p.cyan;ctx.lineWidth=1;
    ctx.beginPath();points.forEach((pt,i)=>i?ctx.lineTo(pt.x,pt.y):ctx.moveTo(pt.x,pt.y));ctx.stroke();

    const runtimeX=(points[1].x+points[2].x)/2,runtimeY=y-scale*.16;
    ctx.globalAlpha=.22+.08*Math.sin(t*1.3);ctx.strokeStyle=p.violet;ctx.lineWidth=1;
    ctx.beginPath();ctx.arc(runtimeX,runtimeY,small?24:32,0,Math.PI*2);ctx.stroke();
    ctx.globalAlpha=.75;ctx.fillStyle=p.muted;ctx.font=`${small?8:9}px ui-monospace,monospace`;ctx.textAlign='center';ctx.fillText('MODEL / RUNTIME',runtimeX,runtimeY+3);
    ctx.globalAlpha=.28;ctx.beginPath();ctx.moveTo(points[1].x,points[1].y);ctx.lineTo(runtimeX,runtimeY);ctx.lineTo(points[2].x,points[2].y);ctx.stroke();

    points.forEach((pt,i)=>{
      const observed=active[i],accepted=latest?.status==='accepted';
      const terminal=i===3&&latest&&['rejected','failed','deferred'].includes(latest.status);
      const color=terminal?p.red:(i===4&&observed&&accepted?p.green:(observed?p.cyan:p.muted));
      const pulse=(motion&&observed)?1+Math.sin(t*1.5+i)*.08:1;
      ctx.globalAlpha=observed?.92:.3;ctx.fillStyle=color;ctx.shadowColor=color;ctx.shadowBlur=observed?10:0;
      ctx.beginPath();ctx.arc(pt.x,pt.y,(small?6:8)*pulse,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
      ctx.globalAlpha=.9;ctx.fillStyle=p.ink;ctx.font=`${small?8:10}px ui-monospace,monospace`;ctx.textAlign='center';
      ctx.fillText(STAGES[i][1],pt.x,pt.y+(small?20:25));
    });

    if(latest&&motion){
      const completion=active.reduce((n,v)=>n+(v?1:0),0);
      const maxSegment=Math.max(0,Math.min(5,completion-1));
      if(maxSegment>0){
        const cycle=((t*.13)%1)*maxSegment;
        const seg=Math.min(maxSegment-1,Math.floor(cycle)),u=cycle-seg;
        const a=points[seg],b=points[seg+1];
        const x=a.x+(b.x-a.x)*u,y2=a.y+(b.y-a.y)*u;
        ctx.globalAlpha=.95;ctx.fillStyle=p.orange;ctx.shadowColor=p.orange;ctx.shadowBlur=16;
        ctx.beginPath();ctx.arc(x,y2,small?3.8:4.8,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
      }
    }

    const runner=actions?.dataset.state;
    if(runner==='running'||runner==='campaign'){
      ctx.globalAlpha=.35+.2*Math.sin(t*2);ctx.strokeStyle=p.green;ctx.lineWidth=1.2;
      ctx.beginPath();ctx.ellipse(cx,cy,scale*.69,scale*.35,0,0,Math.PI*2);ctx.stroke();
      ctx.globalAlpha=.9;ctx.fillStyle=p.green;ctx.font='9px ui-monospace,monospace';ctx.textAlign='right';ctx.fillText('EXECUTION ACTIVE',w-18,22);
    }

    if(now<flashUntil){
      const f=(flashUntil-now)/900;ctx.globalAlpha=f*.35;ctx.strokeStyle=p.orange;ctx.lineWidth=2;
      ctx.beginPath();ctx.ellipse(cx,cy,scale*.62,scale*.31,0,0,Math.PI*2);ctx.stroke();
    }
    ctx.globalAlpha=1;
    if(motion||runner==='running'||runner==='campaign'||now<flashUntil)frame=requestAnimationFrame(draw);
    else frame=null;
  }
  function scheduleDraw(){if(frame)return;frame=requestAnimationFrame(draw);}
  function receive(d){
    if(!d||d.projection_kind!=='disposable-research-view')return;
    projection=d;latest=(d.wakes||[])[0]||null;
    if(lastVersion!==null&&d.version!==lastVersion)flashUntil=performance.now()+900;
    lastVersion=d.version;
    buildRecordField();setStageReadout();scheduleDraw();
  }
  window.addEventListener('wake-process-data',event=>receive(event.detail));
  const observer=new MutationObserver(()=>{setStageReadout();scheduleDraw();});
  if(actions)observer.observe(actions,{attributes:true,attributeFilter:['data-state','title']});

  toggle?.addEventListener('click',()=>{
    motion=!motion;toggle.setAttribute('aria-pressed',String(motion));toggle.textContent=motion?'Pause motion':'Resume motion';scheduleDraw();
  });
  if(reduced&&toggle){toggle.setAttribute('aria-pressed','false');toggle.textContent='Resume motion';}
  const io=new IntersectionObserver(entries=>{visible=entries[0]?.isIntersecting??true;if(visible)scheduleDraw();},{threshold:.02});
  io.observe(panel||canvas);
  window.addEventListener('resize',scheduleDraw);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)scheduleDraw();});
  setStageReadout();scheduleDraw();
})();