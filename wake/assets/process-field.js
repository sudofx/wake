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
  const reset=document.getElementById('process-field-reset');
  const selectionEl=document.getElementById('process-field-selection');
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
  let projection=null,latest=null,frame=null,start=performance.now(),motion=false,visible=true;
  let nodePositions=[],recordEdges=[],recordNodes=[],lastVersion=null,flashUntil=0;
  let viewAngle=0,viewTilt=0,selectedNode=null,selectedStage=null,stagePoints=[];
  let pointer=null,dragged=false;
  let runtime=window.WakeRuntimeActivity||null,lastLiveDraw=0,lastStageHTML='';
  const liveIndex=()=>runtime?.activity?.active?({record:0,context:1,collecting:1,provider:2,governance:3,continuity:3,receipt:5}[runtime.activity.stage]??-1):-1;


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
    const stageHTML=STAGES.map(([key,label],i)=>`<div class="process-stage ${active[i]?'observed':'quiet'} ${liveIndex()===i?'live-current':''}" data-stage="${key}" data-stage-index="${i}" role="button" tabindex="0"><span>0${i+1}</span><strong>${label}</strong><small>${escapeHtml(stateLabel(latest,i))}</small></div>`).join('');
    if(stageHTML!==lastStageHTML){stageList.innerHTML=stageHTML;lastStageHTML=stageHTML;}
    const setText=(element,text)=>{if(element.textContent!==text)element.textContent=text;};
    if(runtime){
      const labels={record:'reading the record',context:'preparing context',collecting:'collecting evidence',provider:'waiting for model response',governance:'checking the proposal',continuity:'evaluating the matrix response',receipt:'finishing the receipt',idle:({paused:'research paused',waiting:'waiting for the next eligible wake',blocked:'operator review required',running:'preparing work',idle:'between wakes'})[runtime.state]};
      setText(statusEl,runtime.activity.active?'LIVE ACTIVITY':'RUNTIME '+runtime.state.toUpperCase());
      statusEl.dataset.state=runtime.activity.active?'running':runtime.state;
      setText(traceEl,`Now · ${labels[runtime.activity.stage]}`);
      traceEl.title=`Sampled ${new Date(runtime.observed_at).toLocaleTimeString()}`;
      setText(detailEl,'Live indicators report this installation’s current work. The orange trace and background remain a replay of recorded history; activity does not imply accepted progress.');
      return;
    }
    const runner=actions?.dataset.state||'unknown';
    const running=runner==='running'||runner==='campaign';
    setText(statusEl,running?'EXECUTION ACTIVE':'EXECUTION '+(runner==='stopped'?'STOPPED':'STATUS UNKNOWN'));
    statusEl.dataset.state=running?'running':runner;
    setText(traceEl,latest?`Latest recorded wake · ${latest.status||'unknown'}`:'Waiting for a recorded wake');
    traceEl.removeAttribute('title');
    setText(detailEl,running
      ?'The runner is active. Exact in-flight activity is unavailable here; the orange trace replays the latest recorded wake.'
      :'The field replays observable WAKE activity from the durable projection. Motion is presentation; nodes and relationships come from recorded data.');
  }
  function buildRecordField(){
    const graph=projection?.graph;
    if(!graph?.nodes?.length){recordNodes=[];recordEdges=[];return;}
    const limit=110;
    const nodes=graph.nodes.slice(-limit);
    const ids=new Set(nodes.map(n=>n.id));
    recordNodes=nodes.map((n,i)=>{
      const h=hash(n.id),a=(h%6283)/1000,r=.15+((h>>>8)%1000)/1000*.36;
      return {id:n.id,kind:n.kind,label:n.label||n.title||n.name||n.id,a,r,phase:((h>>>16)%1000)/1000*Math.PI*2,index:i};
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
    if(!visible){frame=null;return;}
    // Keep live inspection lightweight on phones without changing view rotation.
    if(!motion&&liveIndex()>=0&&!reduced&&performance.now()-lastLiveDraw<50){frame=requestAnimationFrame(draw);return;}
    lastLiveDraw=performance.now();
    const {w,h}=resize();if(!w||!h){frame=null;return;}
    const p=palette(),now=performance.now(),t=(now-start)/1000;
    ctx.clearRect(0,0,w,h);
    const cx=w*.5,cy=h*.49,small=w<700,scale=Math.min(w,h);
    const drift=motion ? .015 : 0;
    nodePositions=recordNodes.map(n=>{
      const angle=n.a+viewAngle+t*drift*((n.index%3)-1);
      const rr=n.r*scale*(.88+.08*Math.sin(t*.18+n.phase));
      const depth=Math.sin(angle);
      const tiltShift=viewTilt*scale*.18*depth;
      return {id:n.id,kind:n.kind,label:n.label,x:cx+Math.cos(angle)*rr*1.55,y:cy+Math.sin(angle)*rr*.82+tiltShift,depth};
    });
    const byId=new Map(nodePositions.map(n=>[n.id,n]));

    ctx.lineWidth=.55;
    recordEdges.forEach(e=>{
      const a=byId.get(e.source),b=byId.get(e.target);if(!a||!b)return;
      ctx.strokeStyle=p.line;ctx.globalAlpha=.22;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();
    });
    nodePositions.forEach((pt,i)=>{
      const chosen=selectedNode===pt.id;
      ctx.fillStyle=chosen?p.orange:(i%9===0?p.violet:p.cyan);ctx.globalAlpha=chosen?.98:(i%9===0?.45:.24);
      ctx.shadowColor=chosen?p.orange:'transparent';ctx.shadowBlur=chosen?14:0;
      ctx.beginPath();ctx.arc(pt.x,pt.y,chosen?5:(i%11===0?2.4:1.35),0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
    });

    const active=stageState(latest);
    const margin=small?28:54;
    const y=cy;
    const points=STAGES.map((_,i)=>({x:margin+(w-margin*2)*(i/(STAGES.length-1)),y:y+Math.sin(i*1.7)*scale*.035}));
    stagePoints=points;
    ctx.globalAlpha=.42;ctx.strokeStyle=p.cyan;ctx.lineWidth=1;
    ctx.beginPath();points.forEach((pt,i)=>i?ctx.lineTo(pt.x,pt.y):ctx.moveTo(pt.x,pt.y));ctx.stroke();

    const runtimeX=(points[1].x+points[2].x)/2,runtimeY=y-scale*.16;
    ctx.globalAlpha=.22+.08*Math.sin(t*1.3);ctx.strokeStyle=p.violet;ctx.lineWidth=1;
    ctx.beginPath();ctx.arc(runtimeX,runtimeY,small?24:32,0,Math.PI*2);ctx.stroke();
    ctx.globalAlpha=.75;ctx.fillStyle=p.muted;ctx.font=`${small?8:9}px ui-monospace,monospace`;ctx.textAlign='center';ctx.fillText('MODEL / RUNTIME',runtimeX,runtimeY+3);
    ctx.globalAlpha=.28;ctx.beginPath();ctx.moveTo(points[1].x,points[1].y);ctx.lineTo(runtimeX,runtimeY);ctx.lineTo(points[2].x,points[2].y);ctx.stroke();

    points.forEach((pt,i)=>{
      const observed=active[i],accepted=latest?.status==='accepted',chosen=selectedStage===i;
      const terminal=i===3&&latest&&['rejected','failed','deferred'].includes(latest.status);
      const color=chosen?p.orange:(terminal?p.red:(i===4&&observed&&accepted?p.green:(observed?p.cyan:p.muted)));
      const live=liveIndex()===i;
      const pulse=(!reduced&&(live||(motion&&observed)))?1+Math.sin(t*3+i)*.12:1;
      if(live){ctx.strokeStyle=p.green;ctx.globalAlpha=.8;ctx.lineWidth=2;ctx.beginPath();ctx.arc(pt.x,pt.y,(small?11:15)*pulse,0,Math.PI*2);ctx.stroke();}
      ctx.globalAlpha=observed?.92:.3;ctx.fillStyle=color;ctx.shadowColor=color;ctx.shadowBlur=observed?10:0;
      ctx.beginPath();ctx.arc(pt.x,pt.y,(chosen?1.35:1)*(small?6:8)*pulse,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;
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
    if(runtime?runtime.activity.active:(runner==='running'||runner==='campaign')){
      ctx.globalAlpha=.35+.2*Math.sin(t*2);ctx.strokeStyle=p.green;ctx.lineWidth=1.2;
      ctx.beginPath();ctx.ellipse(cx,cy,scale*.69,scale*.35,0,0,Math.PI*2);ctx.stroke();
      ctx.globalAlpha=.9;ctx.fillStyle=p.green;ctx.font='9px ui-monospace,monospace';ctx.textAlign='right';ctx.fillText('EXECUTION ACTIVE',w-18,22);
    }

    if(now<flashUntil){
      const f=(flashUntil-now)/900;ctx.globalAlpha=f*.35;ctx.strokeStyle=p.orange;ctx.lineWidth=2;
      ctx.beginPath();ctx.ellipse(cx,cy,scale*.62,scale*.31,0,0,Math.PI*2);ctx.stroke();
    }
    ctx.globalAlpha=1;
    if(motion||(liveIndex()>=0&&!reduced&&!document.hidden))frame=requestAnimationFrame(draw);
    else frame=null;
  }
  function scheduleDraw(){if(frame)return;frame=requestAnimationFrame(draw);}
  function inspectNode(id){
    const node=recordNodes.find(n=>n.id===id);if(!node)return;
    selectedNode=id;selectedStage=null;
    selectionEl.textContent=`Recorded object · ${node.kind||'record'} · ${node.label||node.id}`;
    stageList.querySelectorAll('.process-stage').forEach(el=>el.classList.remove('selected'));scheduleDraw();
  }
  function inspectStage(index){
    selectedStage=index;selectedNode=null;
    const descriptions=['Durable record · governed history available to later work.','Context · bounded material assembled for an invocation.','Proposal · model/runtime output before WAKE grants it authority.','Governance · deterministic checks decide what may transition.','Transition · accepted change enters durable state.','Receipt · auditable trace of what happened and why.'];
    selectionEl.textContent=`${STAGES[index][1]} · ${descriptions[index]}`;
    stageList.querySelectorAll('.process-stage').forEach((el,i)=>el.classList.toggle('selected',i===index));scheduleDraw();
  }
  function resetView(){viewAngle=0;viewTilt=0;selectedNode=null;selectedStage=null;selectionEl.textContent='Drag the field to rotate · tap a node or stage to inspect';stageList.querySelectorAll('.process-stage').forEach(el=>el.classList.remove('selected'));scheduleDraw();}
  function hitTest(x,y){let best=null,bestD=18;for(const pt of nodePositions){const d=Math.hypot(pt.x-x,pt.y-y);if(d<bestD){best=pt;bestD=d;}}if(best){inspectNode(best.id);window.dispatchEvent(new CustomEvent('wake-process-record-select',{detail:best.id}));return true;}let si=-1,sd=24;stagePoints.forEach((pt,i)=>{const d=Math.hypot(pt.x-x,pt.y-y);if(d<sd){si=i;sd=d;}});if(si>=0){inspectStage(si);return true;}return false;}
  function receive(d){
    if(!d||d.projection_kind!=='disposable-research-view')return;
    projection=d;latest=(d.wakes||[])[0]||null;
    if(lastVersion!==null&&d.version!==lastVersion)flashUntil=performance.now()+900;
    lastVersion=d.version;
    buildRecordField();setStageReadout();scheduleDraw();
  }
  window.addEventListener('wake-process-data',event=>receive(event.detail));
  window.addEventListener('wake-console-selection',event=>{
    const recordId=event.detail?.recordId||'',wakeId=event.detail?.wakeId||'',selectedWake=event.detail?.wake||null;
    if(wakeId){
      const wake=selectedWake||(projection?.wakes||[]).find(w=>w.id===wakeId);
      if(wake)latest=wake;
    }else if(projection?.wakes?.length)latest=projection.wakes[0];
    if(recordId && recordNodes.some(n=>n.id===recordId))inspectNode(recordId);
    else if(!recordId){selectedNode=null;selectedStage=null;stageList.querySelectorAll('.process-stage').forEach(el=>el.classList.remove('selected'));scheduleDraw();}
    setStageReadout();scheduleDraw();
  });
  async function loadProjection(){
    try{
      const response=await fetch('research-data.json',{cache:'no-store'});
      if(!response.ok)throw new Error(`HTTP ${response.status}`);
      const next=await response.json();
      if(next?.projection_kind!=='disposable-research-view'||!Array.isArray(next.graph?.nodes)||!Array.isArray(next.graph?.edges))throw new Error('Unsupported projection');
      receive(next);
    }catch(error){
      statusEl.textContent='PROCESS DATA UNAVAILABLE';
      statusEl.dataset.state='error';
      traceEl.textContent='Published projection could not be loaded';
      detailEl.textContent='The process field could not load its published WAKE projection. Other Console panels may still remain usable.';
      scheduleDraw();
    }
  }
  const observer=new MutationObserver(()=>{setStageReadout();scheduleDraw();});
  window.addEventListener('wake-runtime-activity',event=>{runtime=event.detail;setStageReadout();scheduleDraw();});
  window.addEventListener('wake-theme-change',scheduleDraw);
  if(actions)observer.observe(actions,{attributes:true,attributeFilter:['data-state','title']});

  stageList.addEventListener('click',event=>{const el=event.target.closest('.process-stage');if(el)inspectStage(Number(el.dataset.stageIndex));});
  stageList.addEventListener('keydown',event=>{if(event.key!=='Enter'&&event.key!==' ')return;const el=event.target.closest('.process-stage');if(!el)return;event.preventDefault();inspectStage(Number(el.dataset.stageIndex));});
  reset?.addEventListener('click',resetView);
  canvas.addEventListener('pointerdown',event=>{const rect=canvas.getBoundingClientRect();pointer={id:event.pointerId,lastX:event.clientX,lastY:event.clientY,startX:event.clientX,startY:event.clientY,rect};dragged=false;canvas.setPointerCapture?.(event.pointerId);});
  canvas.addEventListener('pointermove',event=>{if(!pointer||pointer.id!==event.pointerId)return;const dx=event.clientX-pointer.lastX,dy=event.clientY-pointer.lastY;if(Math.hypot(event.clientX-pointer.startX,event.clientY-pointer.startY)>5)dragged=true;if(dragged){viewAngle+=dx*.008;viewTilt=Math.max(-1,Math.min(1,viewTilt+dy*.004));canvas.classList.add('is-dragging');scheduleDraw();}pointer.lastX=event.clientX;pointer.lastY=event.clientY;});
  const finishPointer=event=>{if(!pointer||pointer.id!==event.pointerId)return;const rect=canvas.getBoundingClientRect();if(!dragged)hitTest(event.clientX-rect.left,event.clientY-rect.top);canvas.classList.remove('is-dragging');pointer=null;};
  canvas.addEventListener('pointerup',finishPointer);canvas.addEventListener('pointercancel',()=>{canvas.classList.remove('is-dragging');pointer=null;});
  toggle?.addEventListener('click',()=>{});
  window.addEventListener('wake-global-motion',event=>{motion=Boolean(event.detail?.enabled);if(!motion&&frame){cancelAnimationFrame(frame);frame=null;}scheduleDraw();});
  motion=false;
  const io=new IntersectionObserver(entries=>{visible=entries[0]?.isIntersecting??true;if(visible)scheduleDraw();},{threshold:.02});
  io.observe(panel||canvas);
  new ResizeObserver(scheduleDraw).observe(canvas);
  window.addEventListener('resize',scheduleDraw);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)scheduleDraw();});
  setStageReadout();scheduleDraw();loadProjection();
})();
