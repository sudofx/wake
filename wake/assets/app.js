/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Main browser controller. It turns exported state into navigation/readable views and must not invent facts absent from the published record.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('wake-data').textContent);
  const s = data.state;
  const $ = id => document.getElementById(id);
  const themeToggle = $('theme-toggle');
  function setTheme(theme, remember=false) {
    const dark=theme==='dark';
    if(dark) document.documentElement.dataset.theme='dark';else delete document.documentElement.dataset.theme;
    themeToggle.setAttribute('aria-pressed',String(dark));
    themeToggle.setAttribute('aria-label',dark?'Use light theme':'Use dark theme');
    themeToggle.innerHTML='<span aria-hidden="true">◐</span> '+(dark?'LIGHT':'DARK');
    if(remember)try{localStorage.setItem('wake-theme',dark?'dark':'light')}catch{}
  }
  setTheme(document.documentElement.dataset.theme==='dark'?'dark':'light');
  themeToggle.addEventListener('click',()=>setTheme(document.documentElement.dataset.theme==='dark'?'light':'dark',true));
  const help = key => window.WakeHelp.button(key);
  const WAKE_TEXT='WAKE\u2733\uFE0E';
  const display = value => String(value ?? '').replaceAll('WAKE✳️','WAKE✳').replaceAll('WAKE✳︎','WAKE✳').replaceAll('WAKE✳','WAKE✳︎');
  const esc = value => display(value).replace(/[&<>"']/g, x => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
  function emphasizeWake(root=document) {
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
    const targets=[];
    while(walker.nextNode()){
      const node=walker.currentNode, parent=node.parentElement;
      if(!parent || !node.nodeValue.includes(WAKE_TEXT)) continue;
      if(parent.closest('script,style,pre,code,textarea,.wake-mark')) continue;
      targets.push(node);
    }
    targets.forEach(node=>{
      const parts=node.nodeValue.split(WAKE_TEXT);
      const fragment=document.createDocumentFragment();
      parts.forEach((part,index)=>{
        if(part) fragment.append(document.createTextNode(part));
        if(index<parts.length-1){
          const strong=document.createElement('strong');
          strong.className='wake-mark';
          strong.textContent=WAKE_TEXT;
          fragment.append(strong);
        }
      });
      node.replaceWith(fragment);
    });
  }
  const fmt = time => new Date(time).toLocaleString('en-US', {timeZone:data.timezone,month:'short',day:'numeric',hour:'numeric',minute:'2-digit',timeZoneName:'short'});
  const invocations = Object.values(s.invocations);
  const posts = Object.values(s.posts || {}).sort((a,b)=>b.created_version-a.created_version);
  const accepted = data.events.filter(e => e.kind === 'accepted');
  const decisions = Object.fromEntries(accepted.map(e => [e.payload.id, e]));
  const live = invocations.filter(i => i.provider === 'gemini' && i.status === 'accepted').length;
  const fixtures = invocations.filter(i => i.provider === 'fixture' && i.status === 'accepted').length;
  const rejected = invocations.filter(i => i.status === 'rejected').length;
  const inherited = Object.values(s.commitments).filter(c => c.status === 'fulfilled' && c.created_by !== c.resolved_by).length;
  const open = Object.values(s.commitments).filter(c => c.status === 'open');
  let journalLimit = 8, historyLimit = 35;
  const refs = ids => (ids || []).map(id => `<a href="#evidence/${encodeURIComponent(id)}">${esc(id)} →</a>`).join(' ');
  const badge = (value, label) => `<span class="badge ${esc(value)}">${esc(label || value)}</span>`;
  const raw = value => `<pre>${esc(JSON.stringify(value,null,2))}</pre>`;
  const topicNames=Object.fromEntries((s.research_topics||[]).map(t=>[t.id,t.label]));
  const topicLabel=id=>topicNames[id]||String(id||'').replaceAll('_',' ');
  const topicTag=(id,page,label=topicLabel(id))=>`<a class="topic-tag" href="#${page}/topic:${encodeURIComponent(id)}" data-topic="${esc(id)}">${esc(String(label).toLowerCase())}</a>`;
  const journalTopics=j=>{
    const event=decisions[j.invocation],actions=event?.payload?.proposal?.actions||[],ids=[];
    actions.forEach(a=>{
      if(a.project&&s.projects?.[a.project]?.domain)ids.push(s.projects[a.project].domain);
      else if(a.domain)ids.push(a.domain);
    });
    return [...new Set(ids.filter(Boolean))];
  };
  const postTopic=post=>((Number(post.created_version)%10===0)&&(/reflection/i.test(String(post.id))||/reflection/i.test(String(post.title))))?'reflection':s.projects?.[post.project]?.domain;
  const proofNames = {
    fresh_sessions:'Fresh-session continuity', causal_state:'Causal state intervention',
    commitment_handoff:'Commitments across providers', invalid_transition:'Invalid actions rejected',
    evidence_lifecycle:'Evidence revision and retraction', recovery:'Crash and projection recovery',
    audit_reconstruction:'Independent audit reconstruction', longitudinal:'100+ fresh invocation cycles'
  };
  $('metrics').innerHTML = [
    [s.version,'Recorded cycles',`${fixtures} simulated · ${live} live Gemini`,'#history'],
    [inherited,'Obligations inherited','Across fresh invocations','#history/filter:inherited'],
    [rejected,'Proposals rejected','Read the drafts and recorded reasons','#history/filter:rejected'],
    [invocations.filter(i=>i.status==='recovered').length,'Calls recovered','Last valid state retained','#history/filter:recovered']
  ].map(([value,label,note,href])=>`<a class="metric" href="${href}"><strong>${value}</strong><span>${label}<small>${note}</small></span></a>`).join('');
  const providerSelect = $('provider-filter');
  [...new Set(invocations.map(i=>i.provider))].sort().forEach(provider => {
    const option = document.createElement('option'); option.value=provider; option.textContent=provider; providerSelect.append(option);
  });
  function journal() {
    const query=$('search').value.toLowerCase(), provider=providerSelect.value;
    const selected=decodeURIComponent((location.hash.match(/^#journal\/topic:([^/]+)/)||[])[1]||'');
    const entries=[...s.journal].reverse().filter(j =>
      (provider==='all'||s.invocations[j.invocation].provider===provider) &&
      (!selected||journalTopics(j).includes(selected)) &&
      `${j.title} ${j.summary} ${j.invocation} ${j.cycle} ${journalTopics(j).map(topicLabel).join(' ')}`.toLowerCase().includes(query));
    $('entries').innerHTML=entries.slice(0,journalLimit).map(j => {
      const i=s.invocations[j.invocation], event=decisions[j.invocation], actions=event.payload.proposal.actions;
      return `<article class="entry" id="cycle-${j.cycle}"><div class="entry-meta"><span class="cycle">WAKE✳︎ ${String(j.cycle).padStart(3,'0')}</span><span>/</span><time datetime="${esc(i.time)}">${esc(fmt(i.time))}</time>${badge(i.provider==='fixture'?'simulated':'accepted',i.provider==='fixture'?'SIMULATED':'ACCEPTED')}${journalTopics(j).map(id=>topicTag(id,'journal')).join('')}</div><h3>${esc(j.title)}</h3><p>${esc(j.summary)}</p><div class="entry-bottom"><span>${esc(i.provider)} / ${esc(i.model)}</span><span>${actions.length} recorded change${actions.length===1?'':'s'}</span></div><details><summary>Open the lab notes →</summary>${actions.map(a=>`<div class="decision"><strong>${esc(a.type)} / ${esc(a.id)}</strong><p>${esc(a.statement||a.task||a.status)}</p><p>${esc(a.reason)}</p>${refs(a.evidence)}</div>`).join('') || '<p>No state changes proposed.</p>'}<a class="subtle" href="#history/${encodeURIComponent(j.invocation)}">Full invocation & decision →</a></details></article>`;
    }).join('') || '<p class="empty">No matching entries. The tape is blank here.</p>';
    $('more').hidden=entries.length<=journalLimit;
  }
  $('search').addEventListener('input',()=>{journalLimit=8;journal();});
  providerSelect.addEventListener('change',()=>{journalLimit=8;journal();});
  $('more').addEventListener('click',()=>{journalLimit+=8;journal();});
  $('open-commitments').innerHTML=open.slice(0,3).map(c=>`<div class="obligation"><span class="dot"></span><div>${esc(c.task)}<small>DUE / CYCLE ${c.due_cycle}${s.version>=c.due_cycle?' · OVERDUE':''}</small></div></div>`).join('')||'<p class="small">No open obligations. Nothing quietly dropped.</p>';
  function modelPerformance() {
    const attempts=[];
    invocations.forEach(invocation=>(invocation.provider_attempts||[]).forEach(attempt=>attempts.push({
      day:invocation.quota_day||new Date(invocation.time).toLocaleDateString('en-CA',{timeZone:data.timezone}),
      model:attempt.model||invocation.model,
      status:attempt.http_status,
      result:attempt.result||'unknown'
    })));
    if(!attempts.length)return `<div class="panel model-panel"><p class="eyebrow">GEMINI MODEL RESPONSES</p><h2>Waiting for the first request.</h2><p>Every model attempt will appear here by Pacific day, including fallbacks and non-200 responses.</p></div>`;
    const days=[...new Set(attempts.map(a=>a.day))].sort();
    const models=[...new Set(attempts.map(a=>a.model))];
    const bucket=(model,day)=>attempts.filter(a=>a.model===model&&a.day===day);
    const cell=(model,day)=>{
      const group=bucket(model,day);if(!group.length)return `<span class="model-cell empty-cell" aria-label="${esc(model)} on ${esc(day)}: no requests">—</span>`;
      const known=group.filter(a=>a.result!=='unknown'),unknown=group.length-known.length;
      if(!known.length)return `<span class="model-cell empty-cell" aria-label="${esc(model)} on ${esc(day)}: ${unknown} request outcomes unknown">?</span>`;
      const ok=known.filter(a=>a.status===200).length,rate=ok/known.length;
      const tone=rate===1?'good':rate===0?'bad':'mixed';
      const statuses=group.map(a=>a.status??a.result).join(', ');
      return `<span class="model-cell ${tone}" title="Recorded outcomes: ${esc(statuses)}" aria-label="${esc(model)} on ${esc(day)}: ${ok} of ${known.length} completed attempts returned HTTP 200${unknown?`; ${unknown} unknown`:''}"><b>${ok}/${known.length}</b><small>200${unknown?' · '+unknown+'?':''}</small></span>`;
    };
    const rows=models.map(model=>{
      const all=attempts.filter(a=>a.model===model),known=all.filter(a=>a.result!=='unknown'),unknown=all.length-known.length;
      const ok=known.filter(a=>a.status===200).length;
      return `<div class="model-row"><strong>${esc(model)}</strong>${days.map(day=>cell(model,day)).join('')}<span class="model-total"><b>${ok}/${known.length}</b><small>${known.length?Math.round(100*ok/known.length):0}%${unknown?' · '+unknown+'?':''}</small></span></div>`;
    }).join('');
    return `<div class="panel model-panel"><p class="eyebrow">GEMINI MODEL RESPONSES / PACIFIC TIME</p><h2>Which version answers?</h2><p>Each cell is HTTP 200 responses divided by completed attempts for that model and day. A 200 measures availability, not research quality. “?” marks a reserved request whose outcome was never durably recorded.</p><div class="model-scroll"><div class="model-matrix" style="--model-days:${days.length}"><div class="model-row model-head"><strong>MODEL</strong>${days.map(day=>`<span>${esc(day.slice(5))}</span>`).join('')}<span>ALL</span></div>${rows}</div></div><div class="model-legend"><span><i class="good"></i>all 200</span><span><i class="mixed"></i>mixed</span><span><i class="bad"></i>no 200</span></div></div>`;
  }
  function metricsDashboard() {
    const completed=invocations.filter(i=>['accepted','rejected','deferred','failed','recovered'].includes(i.status));
    const count=status=>completed.filter(i=>i.status===status).length;
    const acceptedCount=count('accepted'), rejectedCount=count('rejected'), deferredCount=count('deferred'), failedCount=count('failed'), recoveredCount=count('recovered');
    const acceptanceRate=completed.length?Math.round(100*acceptedCount/completed.length):0;
    const obligations=Object.values(s.commitments||{}), fulfilled=obligations.filter(c=>c.status==='fulfilled');
    const inheritedFulfilled=fulfilled.filter(c=>c.created_by&&c.resolved_by&&c.created_by!==c.resolved_by);
    const handoffRate=fulfilled.length?Math.round(100*inheritedFulfilled.length/fulfilled.length):0;
    const evidenceCount=Object.keys(s.evidence||{}).length, projects=Object.values(s.projects||{}), notebooks=Object.values(s.notebooks||{});
    const providerRequests=completed.reduce((n,i)=>n+(i.provider_requests_sent||0),0);
    const requestsPerAccepted=acceptedCount?(providerRequests/acceptedCount).toFixed(2):'—';
    const attempts=[...completed].sort((a,b)=>new Date(a.time)-new Date(b.time)).slice(-100);
    const timeline=attempts.map((i,index)=>`<a class="wake-cell ${esc(i.status||'unknown')}" href="#history/${encodeURIComponent(i.id)}" title="${esc(i.id)} · ${esc((i.status||'unknown').toUpperCase())} · ${esc(i.successful_model||i.model||i.provider||'')}" aria-label="Attempt ${index+1}: ${esc(i.status||'unknown')}"></a>`).join('');
    const statuses=[['accepted',acceptedCount],['rejected',rejectedCount],['deferred',deferredCount],['failed',failedCount],['recovered',recoveredCount]], maxStatus=Math.max(1,...statuses.map(x=>x[1]));
    const outcomeBars=statuses.map(([name,value])=>`<div class="metric-bar-row"><span>${esc(name)}</span><div><i class="metric-bar ${esc(name)}" style="width:${Math.max(value?3:0,100*value/maxStatus)}%"></i></div><strong>${value}</strong></div>`).join('');
    const models={}; completed.forEach(i=>{const key=i.successful_model||i.model||i.provider||'unknown';models[key]??={attempts:0,accepted:0,requests:0};models[key].attempts++;models[key].accepted+=i.status==='accepted'?1:0;models[key].requests+=i.provider_requests_sent||0;});
    const modelRows=Object.entries(models).sort((a,b)=>b[1].attempts-a[1].attempts).map(([name,m])=>`<div class="model-metric-row"><strong>${esc(name)}</strong><span>${m.attempts} wakes</span><span>${m.accepted} accepted</span><span>${m.requests} HTTP requests</span></div>`).join('');
    const rejectionReasons=data.events.filter(e=>e.kind==='rejected').map(e=>String(e.payload.reason||'Unspecified rejection')), reasonCounts={};
    rejectionReasons.forEach(reason=>{const key=reason.split(':')[0].slice(0,90);reasonCounts[key]=(reasonCounts[key]||0)+1;});
    const reasons=Object.entries(reasonCounts).sort((a,b)=>b[1]-a[1]).slice(0,8).map(([reason,n])=>`<div class="reason-row"><strong>${n}</strong><span>${esc(reason)}</span></div>`).join()||'<p class="empty">No rejected proposals in this record.</p>';

    const actionEvents=accepted.map(e=>({cycle:e.payload.proposal?.base_version+1||0,actions:e.payload.proposal?.actions||[]}));
    const actionCounts={}; actionEvents.forEach(row=>row.actions.forEach(a=>actionCounts[a.type]=(actionCounts[a.type]||0)+1));
    const actionTotal=Object.values(actionCounts).reduce((a,b)=>a+b,0);
    const actionPie=Object.entries(actionCounts).sort((a,b)=>b[1]-a[1]).map(([name,n])=>`<div class="pie-key"><i style="--slice:${n/actionTotal*360}deg"></i><span>${esc(name)}</span><strong>${n}</strong></div>`).join('');
    let angle=0; const pieStops=Object.entries(actionCounts).sort((a,b)=>b[1]-a[1]).map(([name,n],idx)=>{const from=angle;angle+=actionTotal?n/actionTotal*360:0;return `var(--chart-${idx%6}) ${from}deg ${angle}deg`;}).join(',');

    const topicStats=Object.fromEntries((s.research_topics||[]).map(t=>[t.id,{label:t.label,projects:0,research:0,evidence:0,notebooks:0,accepted:0}]));
    const ensureTopic=id=>{if(!id)return null;if(!topicStats[id])topicStats[id]={label:topicLabel(id),projects:0,research:0,evidence:0,notebooks:0,accepted:0};return topicStats[id];};
    projects.forEach(p=>{const t=ensureTopic(p.domain);if(t)t.projects++;});
    Object.values(s.research||{}).forEach(r=>{const t=ensureTopic(r.domain);if(t)t.research++;});
    Object.values(s.evidence||{}).forEach(e=>{let domain=e.topic_domain;try{if(!domain&&typeof e.content==='string')domain=JSON.parse(e.content).topic_domain;}catch{}const t=ensureTopic(domain);if(t)t.evidence++;});
    notebooks.forEach(n=>{const domain=s.projects?.[n.project]?.domain||n.domain;const t=ensureTopic(domain);if(t)t.notebooks++;});
    actionEvents.forEach(row=>{const ids=new Set();row.actions.forEach(a=>{const domain=a.domain||s.projects?.[a.project]?.domain;if(domain)ids.add(domain);});ids.forEach(id=>{const t=ensureTopic(id);if(t)t.accepted++;});});
    const topicRows=Object.entries(topicStats).map(([id,t])=>({id,...t,activity:t.projects+t.research+t.evidence+t.notebooks+t.accepted})).sort((a,b)=>b.activity-a.activity||a.label.localeCompare(b.label));
    const maxTopic=Math.max(1,...topicRows.map(t=>t.activity));
    const topicChart=topicRows.map(t=>`<div class="topic-metric-row"><a href="#projects/topic:${encodeURIComponent(t.id)}">${esc(t.label)}</a><div class="topic-stack" title="${t.projects} projects · ${t.research} research · ${t.evidence} evidence · ${t.notebooks} notebooks · ${t.accepted} accepted wakes"><i class="topic-projects" style="width:${100*t.projects/maxTopic}%"></i><i class="topic-research" style="width:${100*t.research/maxTopic}%"></i><i class="topic-evidence" style="width:${100*t.evidence/maxTopic}%"></i><i class="topic-notebooks" style="width:${100*t.notebooks/maxTopic}%"></i><i class="topic-wakes" style="width:${100*t.accepted/maxTopic}%"></i></div><strong>${t.activity}</strong></div>`).join('');

    const windows=[]; for(let i=0;i<completed.length;i+=10){const group=completed.slice(i,i+10),a=group.filter(x=>x.status==='accepted').length,r=group.filter(x=>x.status==='rejected').length,d=group.filter(x=>x.status==='deferred').length;windows.push({label:`${i+1}–${i+group.length}`,a,r,d,total:group.length});}
    const trend=windows.map(w=>`<div class="trend-col" title="Wakes ${w.label}: ${w.a} accepted, ${w.r} rejected, ${w.d} deferred"><div class="trend-stack"><i class="accepted" style="height:${100*w.a/w.total}%"></i><i class="rejected" style="height:${100*w.r/w.total}%"></i><i class="deferred" style="height:${100*w.d/w.total}%"></i></div><span>${w.label}</span></div>`).join('');

    const beliefs=Object.values(s.beliefs||{}), activeBeliefs=beliefs.filter(b=>b.status==='active'), retractedBeliefs=beliefs.filter(b=>b.status==='retracted');
    const revisedBeliefs=actionEvents.flatMap(x=>x.actions).filter(a=>a.type==='belief').length;
    const overdue=obligations.filter(c=>c.status==='open'&&s.version>=c.due_cycle).length;
    const fallbackWakes=completed.filter(i=>(i.provider_attempts||[]).length>1).length;
    const knownAttempts=completed.flatMap(i=>i.provider_attempts||[]).filter(a=>a.result!=='unknown');
    const latency=knownAttempts.map(a=>a.elapsed_ms).filter(Number.isFinite).sort((a,b)=>a-b);
    const trueMedian=values=>{if(!values.length)return null;const m=Math.floor(values.length/2);return values.length%2?values[m]:(values[m-1]+values[m])/2;};
    const medianLatency=latency.length?Math.round(trueMedian(latency)):null;
    const sortedCompleted=[...completed].sort((a,b)=>new Date(a.time)-new Date(b.time));
    const firstTime=sortedCompleted[0]?.time, lastTime=sortedCompleted.at(-1)?.time;
    const recordHours=firstTime&&lastTime?Math.max(0,(new Date(lastTime)-new Date(firstTime))/36e5):0;
    const wakesPerHour=recordHours?completed.length/recordHours:0;
    const acceptedPerHour=recordHours?acceptedCount/recordHours:0;
    const actionPerAccepted=acceptedCount?(actionTotal/acceptedCount):0;
    const evidencePerAccepted=acceptedCount?(evidenceCount/acceptedCount):0;
    const openObligations=obligations.filter(c=>c.status==='open').length;
    const providerSuccesses=knownAttempts.filter(a=>['success','accepted','ok'].includes(String(a.result||'').toLowerCase())).length;
    const fallbackRate=completed.length?100*fallbackWakes/completed.length:0;
    const rejectionRate=completed.length?100*rejectedCount/completed.length:0;
    const topicActive=topicRows.filter(t=>t.activity>0).length;
    const telemetry=[
      ['Record span',recordHours>=24?(recordHours/24).toFixed(1)+'d':recordHours.toFixed(1)+'h','first → latest completed wake'],
      ['Wake velocity',wakesPerHour.toFixed(2)+'/h',completed.length+' completed'],
      ['Accepted velocity',acceptedPerHour.toFixed(2)+'/h',acceptedCount+' accepted'],
      ['Rejection pressure',rejectionRate.toFixed(1)+'%',rejectedCount+' rejected'],
      ['Fallback rate',fallbackRate.toFixed(1)+'%',fallbackWakes+' multi-attempt wakes'],
      ['Actions / accepted',actionPerAccepted.toFixed(2),actionTotal+' durable actions'],
      ['Evidence / accepted',evidencePerAccepted.toFixed(2),evidenceCount+' evidence records'],
      ['Topic coverage',topicActive+'/'+topicRows.length,'topics with recorded activity'],
      ['Open obligations',openObligations,String(overdue)+' overdue'],
      ['Known attempts',knownAttempts.length,providerSuccesses+' success-labelled']
    ];
    const telemetryHtml=telemetry.map(([label,value,note])=>`<article class="telemetry-cell"><span>${label}</span><strong>${value}</strong><small>${note}</small></article>`).join('');
    const card=(value,label,note)=>`<article class="metric-card"><strong>${value}</strong><span>${label}</span><small>${note}</small></article>`;

    const hypotheses=[];
    if(completed.length>=20){const recent=completed.slice(-20),prior=completed.slice(-40,-20);if(prior.length>=10){const rr=recent.filter(i=>i.status==='accepted').length/recent.length,pr=prior.filter(i=>i.status==='accepted').length/prior.length;if(Math.abs(rr-pr)>=.1)hypotheses.push({title:'Outcome regime may be shifting',text:`Acceptance moved from ${Math.round(pr*100)}% in the prior window to ${Math.round(rr*100)}% in the latest 20 wakes. This is an observed association, not a causal explanation.`});}}
    if(topicRows.length>=2&&topicRows[0].activity>Math.max(2,topicRows.at(-1).activity*2))hypotheses.push({title:'Research attention is uneven',text:`${topicRows[0].label} currently has ${topicRows[0].activity} recorded activity units versus ${topicRows.at(-1).activity} for ${topicRows.at(-1).label}. The record supports an attention-skew hypothesis; it does not establish topic value.`});
    if(fallbackWakes)hypotheses.push({title:'Provider fallback is part of observed continuity',text:`${fallbackWakes} completed wakes required more than one model attempt. Compare their outcomes with single-attempt wakes before attributing any quality effect to fallback.`});
    if(rejectedCount)hypotheses.push({title:'Rejection is measurable governance work',text:`${rejectedCount} completed wakes were rejected while durable state advanced ${s.version} cycles. Rejections are observable resistance in the process, not automatically failure or success.`});
    if(!hypotheses.length)hypotheses.push({title:'Not enough separation yet',text:'The current record does not show a strong simple pattern worth elevating. Keep collecting data rather than manufacturing a story.'});
    const hypothesisHtml=hypotheses.map(h=>`<article class="hypothesis-card"><p class="eyebrow">DATA-DERIVED HYPOTHESIS</p><h3>${esc(h.title)}</h3><p>${esc(h.text)}</p></article>`).join('');

    $('metrics-dashboard').innerHTML=`
      <section class="metrics-row-one">
        <div class="metrics-landscape-heading"><div><p class="eyebrow">TOPIC LANDSCAPE</p><h2>Where the work explores.</h2></div><div class="landscape-status"><span>CURRENT TOPICS</span><strong>${topicRows.length}</strong></div></div>
        <section class="dashboard-grid">
        <article class="dashboard-panel"><p class="eyebrow">TOPIC DISTRIBUTION</p><h2>Where work accumulates.</h2><p class="small">Composite activity is a descriptive count of projects, research records, evidence, notebooks, and accepted wakes touching each configured topic. It is not a quality score.</p><div class="topic-metrics">${topicChart||'<p class="empty">No topic activity yet.</p>'}</div><div class="topic-legend"><span>projects</span><span>research</span><span>evidence</span><span>notebooks</span><span>wakes</span></div></article>
        <article class="dashboard-panel"><p class="eyebrow">ACCEPTED ACTION MIX</p><h2>What kind of work survives governance?</h2><div class="pie-layout"><div class="css-pie" style="background:conic-gradient(${pieStops||'var(--line) 0deg 360deg'})" role="img" aria-label="Accepted action type composition"></div><div class="pie-keys">${actionPie||'<p class="empty">No accepted actions yet.</p>'}</div></div></article>
        <article class="dashboard-panel"><p class="eyebrow">CORRECTABILITY</p><h2>What governance stopped.</h2><div class="metric-bars">${outcomeBars}</div><h3>Most common rejection families</h3><div class="reason-list">${reasons}</div><a class="text-link" href="#history/filter:rejected">Inspect rejected work →</a></article>
        <article class="dashboard-panel"><p class="eyebrow">CONTINUITY</p><h2>Does work cross fresh sessions?</h2><div class="dashboard-stat"><strong>${inheritedFulfilled.length}</strong><span>obligations fulfilled by a later invocation</span></div><div class="dashboard-stat"><strong>${obligations.filter(c=>c.status==='open').length}</strong><span>open obligations still carried forward</span></div><div class="dashboard-stat"><strong>${recoveredCount}</strong><span>recovered calls with durable state retained</span></div><div class="dashboard-stat"><strong>${overdue}</strong><span>open obligations at or past due cycle</span></div></article>
        <article class="dashboard-panel"><p class="eyebrow">RESEARCH YIELD</p><h2>What survives as usable work?</h2><div class="dashboard-stat"><strong>${evidenceCount}</strong><span>evidence records</span></div><div class="dashboard-stat"><strong>${projects.length}</strong><span>research projects</span></div><div class="dashboard-stat"><strong>${notebooks.length}</strong><span>notebooks</span></div><div class="dashboard-stat"><strong>${Object.keys(s.posts||{}).length}</strong><span>published posts</span></div></article>
        <article class="dashboard-panel"><p class="eyebrow">PROVIDER PRESSURE</p><h2>What it costs to get a wake.</h2><div class="dashboard-stat"><strong>${providerRequests}</strong><span>recorded HTTP requests</span></div><div class="dashboard-stat"><strong>${fallbackWakes}</strong><span>wakes using provider fallback</span></div><div class="dashboard-stat"><strong>${deferredCount}</strong><span>deferred wakes</span></div><div class="model-metrics">${modelRows||'<p class="empty">No provider data yet.</p>'}</div></article>
      </section>
        <article class="dashboard-panel dashboard-hypothesis-summary"><p class="eyebrow">OBSERVATION → HYPOTHESIS</p><h2>From patterns to possibilities.</h2><div class="dashboard-stat"><strong>${hypotheses.length}</strong><span>active hypotheses</span></div><p class="small">Generated only from recorded counts and comparisons. Prompts for investigation, not conclusions.</p></article>
      </section>
        <section class="hypothesis-section"><div class="dashboard-heading"><div><p class="eyebrow">OBSERVATION → HYPOTHESIS</p><h2>Patterns worth testing next.</h2></div><p>Generated only from recorded counts and comparisons.</p></div><div class="hypothesis-grid">${hypothesisHtml}</div></section>
      </section>
      <section class="metrics-row-two">
        <div class="metrics-row-two-left"><article class="dashboard-section dashboard-feature"><div class="dashboard-heading"><div><p class="eyebrow">OUTCOME TREND / 10-WAKE WINDOWS</p><h2>Are the conditions changing?</h2></div><p>Each column is a consecutive ten-wake window. Height is share of outcomes.</p></div><div class="trend-chart">${trend||'<span class="empty">No completed wakes yet.</span>'}</div></article><article class="dashboard-section dashboard-feature"><div class="dashboard-heading"><div><p class="eyebrow">LAST ${attempts.length} COMPLETED WAKES</p><h2>The pulse of the experiment.</h2></div><p>One cell per wake. Color is outcome—not quality. Tap any cell for its receipt.</p></div><div class="wake-timeline" role="group" aria-label="Recent wake outcomes">${timeline||'<span class="empty">No completed wakes yet.</span>'}</div><div class="timeline-legend">${statuses.map(([name])=>`<span><i class="${name}"></i>${name}</span>`).join('')}</div></article></div>
        <div class="metrics-row-two-right"><section class="command-strip"><div><p class="eyebrow">LIVE RECORD TELEMETRY</p><strong>CYCLE ${s.version}</strong></div><div><span>COMPLETED</span><b>${completed.length}</b></div><div><span>ACCEPTED</span><b>${acceptedCount}</b></div><div><span>REJECTED</span><b>${rejectedCount}</b></div><div><span>DEFERRED</span><b>${deferredCount}</b></div><div><span>FALLBACK</span><b>${fallbackWakes}</b></div><div><span>OPEN WORK</span><b>${openObligations}</b></div><div><span>TOPICS ACTIVE</span><b>${topicActive}/${topicRows.length}</b></div></section>
<section class="telemetry-grid">${telemetryHtml}</section>
<section class="dashboard-kpis">${card(s.version,'Durable cycles','Accepted state advances')}${card(acceptanceRate+'%','Acceptance rate',acceptedCount+' of '+completed.length+' completed wakes')}${card(handoffRate+'%','Obligation handoff',inheritedFulfilled.length+' cross-invocation fulfillments')}${card(requestsPerAccepted,'Requests / accepted','Recorded HTTP attempts ÷ accepted wakes')}${card(fallbackWakes,'Fallback wakes','More than one provider attempt')}${card(medianLatency===null?'—':medianLatency+'ms','Median provider latency','Known completed model attempts')}${card(revisedBeliefs,'Belief actions',activeBeliefs.length+' active · '+retractedBeliefs.length+' retracted')}${card(overdue,'Overdue obligations','Open commitments at or past due cycle')}</section></div>
      </section>
      <p class="dashboard-footnote">Derived view only. The durable state and event log remain authoritative. Composite counts and hypotheses are explicitly descriptive; they never write back to the record.</p>`;
  }
  function lab() {
    const exp=data.experiment;
    const coverage=Object.entries(proofNames).map(([key,label])=>`<div class="check"><span>${label}</span><b class="${exp?.checks[key]?.passed?'':'pending'}">${exp?.checks[key]?.passed?'PASS · FIXTURE':'NOT RUN'}</b></div>`).join('');
    const committed=Object.values(s.commitments).sort((a,b)=> (a.status==='open'?-1:1)-(b.status==='open'?-1:1)||b.created_version-a.created_version);
    const bars=accepted.slice(-100).map(e=>`<a href="#history/${encodeURIComponent(e.payload.id)}" style="height:${Math.max(8,Math.min(100,15+e.payload.proposal.actions.length*12))}%" title="${esc(e.payload.id)}: ${e.payload.proposal.actions.length} accepted changes" aria-label="${esc(e.payload.id)}: ${e.payload.proposal.actions.length} accepted changes"></a>`).join('');
    const scored=invocations.filter(item=>item.inquiry_drive_shadow&&item.status==='accepted');
    const drive=scored.at(-1)?.inquiry_drive_shadow, gate=drive?.activation;
    const driveStatus=!drive?'WAITING FOR A CHARTERED WAKE':gate?.active?'ACTIVE / ADVISORY':gate?.operator_enabled?`LOCKED / ${gate.completed_scored_cycles} OF ${gate.minimum_completed_scored_cycles} SCORED CYCLES`:'SHADOW ONLY / OPERATOR DISABLED';
    const driveRows=(drive?.projects||[]).map((project,index)=>`<div class="drive-row"><b>${index+1}</b><span>${esc(project.title)}</span><strong>${Math.round(project.score*100)}%</strong><small>C ${Math.round(project.components.continuity*100)} · N ${Math.round(project.components.novelty*100)} · H ${Math.round(project.components.coherence*100)} · G ${Math.round(project.components.generativity*100)} · S ${Math.round(project.components.self_correction*100)}</small></div>`).join('')||'<p>No active research projects were scored in the latest wake.</p>';
    const drivePanel=`<div class="panel drive-panel"><p class="eyebrow">INQUIRY-DRIVE SHADOW</p><h2>What work would persist?</h2><p class="drive-status">${esc(driveStatus)}</p><p>The rank is a deterministic record-based signal, not an inner motive. C = continuity, N = novelty, H = coherence, G = generativity, S = self-correction.</p>${driveRows}<p class="small">It cannot preserve WAKE, alter rules, or select work unless an operator enables it after the required scored history. <a href="#history">Inspect the receipts →</a></p></div>`;
    $('lab-content').innerHTML=`<div class="panel"><p class="eyebrow">THE DURABLE OBJECTIVE ${help('durable_objective')}</p><h2>${esc(s.objective)}</h2><p>Current focus: <strong>${esc(s.focus)}</strong></p><div class="flow"><span>Durable state</span>→<span>Fresh invocation</span>→<span>Untrusted proposal</span>→<span>Mechanical rules</span>→<span>Atomic event</span></div><p>Models may review beliefs, create obligations, and propose evidence-backed completion. External actions and rule changes are outside their authority.</p></div>${drivePanel}<div class="lab-grid"><div class="panel"><p class="eyebrow">REPEATABLE HARNESS EXPERIMENT ${help('repeatable_harness')}</p><h2>The test, not the hype.</h2>${coverage}<p>${exp?`Executed ${esc(exp.generated)}. ${exp.cycles} accepted cycles, ${exp.fresh_processes} fresh wake processes. <a href="experiment.json">Download results →</a>`:'Run the offline experiment to populate this checklist.'}</p><p>These results exercise deterministic simulated providers. They do not establish real-model comprehension or general intelligence. Live Gemini accepted cycles here: <strong>${live}</strong>. Human-pasted replies have human-attested model identity.</p></div><div class="panel"><p class="eyebrow">LAST ${Math.min(accepted.length,100)} ACCEPTED CYCLES ${help('accepted_cycles')}</p><h2>Small steps. Long record.</h2><div class="spark" role="group" aria-label="Number of accepted changes per cycle">${bars}</div><div class="chart-labels"><span>OLDER →</span><span>ACCEPTED CHANGES / CYCLE</span><span>NOW</span></div><h3>What the system enforces</h3><p>Atomic proposals. Existing evidence references. New evidence for belief reviews. Persistent obligations. No model cancellation. An auditable decision for each completed invocation.</p><h3>What still needs judgment</h3><p>Whether evidence is true, whether it supports a claim, and whether an obligation was meaningfully fulfilled. Hashes detect edits relative to the recorded head; they do not stop an administrator rewriting the entire history.</p><p>Verified export head:<br><code>${esc(data.head)}</code></p></div></div>${modelPerformance()}<div class="panel"><p class="eyebrow">CURRENT BELIEFS ${help('beliefs')}</p><h2>Allowed to change our minds.</h2>${Object.values(s.beliefs).sort((a,b)=>b.confidence-a.confidence||String(a.id).localeCompare(String(b.id))).map(b=>`<div class="data-card"><div class="entry-meta">${badge(b.status==='active'?'accepted':'rejected',b.status)}<span>${Math.round(b.confidence*100)}% CONFIDENCE</span><span>${esc(b.id)}</span></div><p>${esc(b.statement)}</p><p>${esc(b.reason)}</p>${refs(b.evidence)}<details><summary>Full belief record</summary>${raw(b)}</details></div>`).join('')||'<p>No beliefs recorded yet.</p>'}</div><div class="panel"><p class="eyebrow">COMMITMENT REGISTER ${help('commitments')}</p><h2>Still on the hook.</h2>${committed.map(c=>`<details class="data-card"><summary>${esc(c.id)} · ${esc(c.status)} · due cycle ${c.due_cycle}${c.status==='open'&&s.version>=c.due_cycle?' · OVERDUE':''}</summary><p>${esc(c.task)}</p><p>${esc(c.resolution_reason||c.reason)}</p>${refs(c.evidence)}${raw(c)}</details>`).join('')||'<p>No commitments yet.</p>'}</div>`;
  }
  function blog(selected='') {
    if(selected.startsWith('topic:')){
      const topic=decodeURIComponent(selected.slice(6));
      const filtered=posts.filter(post=>postTopic(post)===topic);
      $('blog-content').innerHTML='<p class="topic-filter-note">Showing <strong>'+esc(topic==='reflection'?'reflection':topicLabel(topic).toLowerCase())+'</strong> · <a href="#blog">show all</a></p>'+(filtered.length?'<div class="blog-grid">'+filtered.map(post=>{const invocation=s.invocations[post.created_by];const reflection=postTopic(post)==='reflection';return '<article class="blog-card'+(reflection?' blog-card-reflection':'')+'"><p class="eyebrow">BOB / '+esc(fmt(invocation.time))+' '+topicTag(postTopic(post),'blog',postTopic(post)==='reflection'?'reflection':topicLabel(postTopic(post)))+'</p><h2><a href="#blog/'+encodeURIComponent(post.id)+'">'+esc(post.title)+'</a></h2><p>'+esc(post.lede)+'</p>'+(post.lens?'<blockquote>'+esc(post.lens)+'</blockquote>':'')+'<a class="text-link" href="#blog/'+encodeURIComponent(post.id)+'">Read Bob’s note →</a></article>';}).join('')+'</div>':'<p class="empty">No posts match this topic.</p>');
      return;
    }
    if(selected){
      const post=posts.find(item=>item.id===selected);
      if(!post){$('blog-content').innerHTML='<p class="empty">That post is not in this record.</p>';return;}
      const invocation=s.invocations[post.created_by];
      const body=String(post.body).split(/\n\s*\n/).map(part=>'<p>'+esc(part)+'</p>').join('');
      const notebooks=post.notebooks.map(id=>'<a class="text-link" href="#projects/notebook:'+encodeURIComponent(id)+'">'+esc(s.notebooks[id].title)+' →</a>').join('');
      const sources=post.evidence.map(id=>'<a href="#evidence/'+encodeURIComponent(id)+'">'+esc(id)+' →</a>').join(' ');
      const correction=post.status==='superseded'?'<div class="research-note">A later post corrected or superseded this one. <a href="#blog/'+encodeURIComponent(post.superseded_by)+'">Read the follow-up →</a></div>':post.supersedes?'<div class="research-note">This note corrects an earlier post. <a href="#blog/'+encodeURIComponent(post.supersedes)+'">Read the original →</a></div>':'';
      $('blog-content').innerHTML='<article class="blog-reading"><a class="subtle" href="#blog">← All posts</a><p class="eyebrow">BY BOB / WAKE '+String(post.created_version).padStart(3,'0')+' / '+esc(fmt(invocation.time))+' '+topicTag(postTopic(post),'blog',postTopic(post)==='reflection'?'reflection':topicLabel(postTopic(post)))+'</p><h2>'+esc(post.title)+'</h2><p class="blog-lede">'+esc(post.lede)+'</p>'+correction+body+(post.lens?'<blockquote><span>BOB’S LENS / PHILOSOPHICAL REFLECTION</span>'+esc(post.lens)+'</blockquote>':'')+'<div class="blog-receipts"><p class="eyebrow">FOLLOW THE RECEIPTS</p><p>Related project: <a href="#projects/'+encodeURIComponent(post.project)+'">'+esc(s.projects[post.project].title)+' →</a></p><div>'+notebooks+'</div><p>'+sources+'</p><a class="subtle" href="#history/'+encodeURIComponent(post.created_by)+'">Exact wake and decision →</a> · <a class="subtle" href="blog/'+encodeURIComponent(post.id)+'.md">Markdown ↓</a></div><p class="blog-disclosure">Bob is WAKE✳︎’s human-facing translation layer, not its mind or identity. This AI-authored note compresses the durable research record for conversation; research claims link back to evidence and philosophical reflections remain reflections.</p></article>';
      return;
    }
    $('blog-content').innerHTML=posts.length?'<div class="blog-grid">'+posts.map(post=>{const invocation=s.invocations[post.created_by];const reflection=(Number(post.created_version)%10===0)&&(/reflection/i.test(String(post.id))||/reflection/i.test(String(post.title)));return '<article class="blog-card'+(reflection?' blog-card-reflection':'')+'"><p class="eyebrow">BOB / '+esc(fmt(invocation.time))+' '+topicTag(postTopic(post),'blog',postTopic(post)==='reflection'?'reflection':topicLabel(postTopic(post)))+'</p><h2><a href="#blog/'+encodeURIComponent(post.id)+'">'+esc(post.title)+'</a></h2><p>'+esc(post.lede)+'</p>'+(post.lens?'<blockquote>'+esc(post.lens)+'</blockquote>':'')+'<a class="text-link" href="#blog/'+encodeURIComponent(post.id)+'">Read Bob’s note →</a></article>';}).join('')+'</div><p class="blog-disclosure">Bob is the public translation layer. Underneath, WAKE✳︎ is a sequence of fresh model calls working from a durable, auditable record—not a persistent person or experiencing self.</p>':'<div class="empty blog-empty"><strong>Bob has nothing worth posting yet.</strong><br>The journal still records every wake. The blog waits for something genuinely interesting.</div>';
  }
  function evidence(selected='') {
    const query=$('evidence-search').value.toLowerCase();
    const rows=Object.values(s.evidence).reverse().filter(e=>(!selected||e.id===selected)&&JSON.stringify(e).toLowerCase().includes(query));
    $('evidence-content').innerHTML=(selected?'<p><a class="text-link" href="#evidence">← All evidence</a></p>':'')+rows.map(e=>`<article class="data-card"><h3>${esc(e.id)}</h3><span class="source">${esc(e.source)} / ${esc(e.actor)} / ${esc(fmt(e.time))}</span><p>${esc(e.content)}</p><details><summary>Raw observation</summary>${raw(e)}</details></article>`).join('')+(rows.length?'':'<p class="empty">No observations match.</p>');
  }
  function history(selected='') {
    const query=$('history-search').value.toLowerCase(), filter=selected.startsWith('filter:')?selected.slice(7):'', kind=filter==='rejected'?'rejected':$('event-filter').value;
    if(filter==='rejected')$('event-filter').value='rejected';
    const inheritedIds=new Set(Object.values(s.commitments).filter(x=>x.status==='fulfilled'&&x.created_by!==x.resolved_by).flatMap(x=>[x.created_by,x.resolved_by]).filter(Boolean));
    const recoveredIds=new Set(invocations.filter(i=>i.status==='recovered').map(i=>i.id));
    const matchesFilter=e=>!filter||(filter==='rejected'?e.kind==='rejected':filter==='recovered'?recoveredIds.has(e.payload.id):filter==='inherited'?inheritedIds.has(e.payload.id):true);
    const exact=selected&&!filter?selected:'';
    const events=[...data.events].reverse().filter(e=>(!exact||e.payload.id===exact)&&matchesFilter(e)&&(kind==='all'||e.kind===kind)&&JSON.stringify(e).toLowerCase().includes(query));
    $('history-content').innerHTML=((selected)?'<p><a class="text-link" href="#history">← All events</a></p>':'')+events.slice(0,historyLimit).map(e=>`<details class="audit-row"><summary><span>#${String(e.seq).padStart(4,'0')}</span>${badge(e.kind)}<time datetime="${esc(e.time)}">${esc(fmt(e.time))}</time><span class="event-id">${esc(e.payload.id||'system')}</span></summary>${e.payload.reason?`<p>${esc(e.payload.reason)}</p>`:''}${(e.kind==='rejected'||e.payload.editorial)?`<p><a class="text-link" href="rejected.html#${encodeURIComponent(e.payload.id)}">Read the draft and explanation →</a></p>`:''}${raw(e)}</details>`).join('')+(events.length?'':'<p class="empty">No events match.</p>');
    $('history-more').hidden=events.length<=historyLimit;
  }
  function route() {
    const [part,id]=location.hash.slice(1).split('/');
    const page=['home','blog','projects','journal','lab','metrics','evidence','history','about'].includes(part)?part:(s.charter?'home':'journal');
    document.querySelectorAll('.view').forEach(el=>el.hidden=el.id!==page);
    document.querySelectorAll('[data-nav]').forEach(el=>{if(el.dataset.nav===page||(el.dataset.navSection==='research'&&['projects','lab','metrics','evidence','history'].includes(page)))el.setAttribute('aria-current','page');else el.removeAttribute('aria-current');});
    let selected='';try{selected=decodeURIComponent(id||'');}catch{}
    if(page==='blog')blog(selected);
    if(page==='journal')journal();
    if(page==='lab')lab();
    if(page==='metrics')metricsDashboard();
    if(page==='evidence')evidence(selected);
    if(page==='history')history(selected);
    if(page==='home'||page==='projects')window.WakePet.render(page,selected);
    emphasizeWake(document);
    document.title=`${WAKE_TEXT} / ${page==='home'?'Explore':page==='journal'?'Read':page[0].toUpperCase()+page.slice(1)}`;
  }
  $('evidence-search').addEventListener('input',route);
  $('history-search').addEventListener('input',()=>{historyLimit=35;route();});
  $('event-filter').addEventListener('change',()=>{historyLimit=35;route();});
  $('history-more').addEventListener('click',()=>{historyLimit+=35;route();});
  window.addEventListener('hashchange',()=>{historyLimit=35;$('evidence-search').value='';$('history-search').value='';$('event-filter').value='all';route();window.scrollTo(0,0);});
  $('generated').textContent=`Exported ${fmt(data.generated)}.`;
  journal();route();
})();
