/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Main browser controller. It turns exported state into navigation/readable views and must not invent facts absent from the published record.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

(async () => {
  'use strict';
  const data = await window.WakeData;
  // Compatibility bridge for an experiment chain pinned before newer
  // presentation projections reached wake-live. Prefer live fields when present;
  // borrow only missing derived/public-safe fields from the current Pages snapshot.
  const hasField=key=>Object.prototype.hasOwnProperty.call(data,key);
  let fallbackNeeded=false;
  if(!data.metrics)fallbackNeeded=true;
  if(!hasField('matrix_progress')||!hasField('application_observability')||!hasField('application_access')||!data.source)fallbackNeeded=true;
  if(fallbackNeeded){
    try{
      const response=await fetch('wake-data.json?wake_metrics='+Date.now(),{cache:'no-store'});
      if(response.ok){
        const fallback=await response.json();
        if(!data.metrics&&fallback.metrics)data.metrics=fallback.metrics;
        if(!hasField('matrix_progress')&&Object.prototype.hasOwnProperty.call(fallback,'matrix_progress'))data.matrix_progress=fallback.matrix_progress;
        if(!hasField('application_observability')&&Object.prototype.hasOwnProperty.call(fallback,'application_observability'))data.application_observability=fallback.application_observability;
        if(!hasField('application_access')&&Object.prototype.hasOwnProperty.call(fallback,'application_access'))data.application_access=fallback.application_access;
        if(!data.source&&fallback.source)data.source=fallback.source;
      }
    }catch{}
  }
  if (window.WakePetReady) await window.WakePetReady;
  const s = data.state;
  const $ = id => document.getElementById(id);
  const themeToggle = $('theme-toggle');
  function savedTheme() { try { return localStorage.getItem('wake-theme'); } catch { return null; } }
  function setTheme(theme, remember=false) {
    const dark=theme==='dark';
    if(dark) document.documentElement.dataset.theme='dark';else delete document.documentElement.dataset.theme;
    const manual=remember||Boolean(savedTheme());
    document.documentElement.dataset.themeMode=manual?'manual':'system';
    themeToggle.setAttribute('aria-label',dark?'Use light theme':'Use dark theme');
    themeToggle.checked=dark;
    if(remember)try{localStorage.setItem('wake-theme',dark?'dark':'light')}catch{}
    themeToggle.closest('.theme-switch')?.setAttribute('title',manual?`Manual ${dark?'dark':'light'} theme`:`Following system ${dark?'dark':'light'} theme`);
  }
  const storedTheme=savedTheme();
  setTheme(storedTheme==='dark'||(!storedTheme&&document.documentElement.dataset.theme==='dark')?'dark':'light');
  themeToggle.addEventListener('change',()=>setTheme(themeToggle.checked?'dark':'light',true));
  try {
    const systemTheme=matchMedia('(prefers-color-scheme:dark)');
    systemTheme.addEventListener('change',event=>{
      if(localStorage.getItem('wake-theme')) return;
      setTheme(event.matches?'dark':'light');
    });
  } catch {}
  const help = key => window.WakeHelp.button(key);
  const WAKE_TEXT='WAKE\u2733\uFE0E';
  const display = value => String(value ?? '').replaceAll('WAKE✳️','WAKE✳').replaceAll('WAKE✳︎','WAKE✳').replaceAll('WAKE✳','WAKE✳︎');
  const esc = value => display(value).replace(/[&<>"']/g, x => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
  const INLINE_BLOG_SOURCE_LINKS_FROM_VERSION=203;
  const blogText=(value,post)=>{
    let rendered=esc(value);
    if(Number(post?.created_version||0)<INLINE_BLOG_SOURCE_LINKS_FROM_VERSION)return rendered;
    const evidence=new Set(post?.evidence||[]);
    [...evidence].sort((a,b)=>String(b).length-String(a).length).forEach(id=>{
      const source=s.evidence?.[id]?.source;
      if(!source)return;
      const token=esc('['+id+']');
      rendered=rendered.split(token).join('<a class="inline-source-citation" href="'+esc(source)+'">'+token+'</a>');
    });
    return rendered;
  };
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
  let invocations, posts, accepted, decisions, live, fixtures, rejected, inherited, open;
  function refreshDerived() {
    invocations = Object.values(s.invocations || {});
    posts = Object.values(s.posts || {}).sort((a,b)=>b.created_version-a.created_version);
    accepted = (data.events || []).filter(e => e.kind === 'accepted');
    decisions = Object.fromEntries(accepted.map(e => [e.payload.id, e]));
    live = invocations.filter(i => i.provider === 'gemini' && i.status === 'accepted').length;
    fixtures = invocations.filter(i => i.provider === 'fixture' && i.status === 'accepted').length;
    rejected = invocations.filter(i => i.status === 'rejected').length;
    inherited = Object.values(s.commitments || {}).filter(c => c.status === 'fulfilled' && c.created_by !== c.resolved_by).length;
    open = Object.values(s.commitments || {}).filter(c => c.status === 'open');
  }
  refreshDerived();
  let journalLimit = 8, historyLimit = 35;
  const refs = ids => (ids || []).map(id => `<a href="#evidence/${encodeURIComponent(id)}">${esc(id)} →</a>`).join(' ');
  const badge = (value, label) => `<span class="badge ${esc(value)}">${esc(label || value)}</span>`;
  // Preserve immutable legacy event bytes in storage, but never expose the old
  // development nickname as current public terminology.
  const displayEventKind = kind => kind === 'squirrel_assessed' ? 'attention_assessed' : kind;
  const displayEvent = event => event?.kind === 'squirrel_assessed' ? {...event, kind:'attention_assessed'} : event;
  const raw = value => `<pre>${esc(JSON.stringify(value,null,2))}</pre>`;
  function expandRecordDetails(root=document) {
    root.querySelectorAll('details.record-panel').forEach(disclosure=>{
      const panel=document.createElement('section');
      for(const attribute of [...disclosure.attributes]) panel.setAttribute(attribute.name,attribute.value);
      panel.classList.add('expanded-record');
      const summary=disclosure.querySelector(':scope > summary');
      if(summary){
        const heading=document.createElement('div'); heading.className='record-panel-head'; heading.innerHTML=summary.innerHTML;
        panel.append(heading);
      }
      for(const child of [...disclosure.children]) if(child!==summary) panel.append(child);
      disclosure.replaceWith(panel);
    });
  }
  const topicNames=Object.fromEntries((s.research_topics||[]).map(t=>[t.id,t.label]));
  const topicColors=s.topic_colors||{};
  const topicLabel=id=>topicNames[id]||String(id||'').replaceAll('_',' ');
  const topicTag=(id,page,label=topicLabel(id))=>`<a class="topic-tag" href="#${page}/topic:${encodeURIComponent(id)}" data-topic="${esc(id)}" style="--topic-color:${esc(topicColors[id]||'var(--cyan)')}">${esc(String(label).toLowerCase())}</a>`;
  const journalTopics=j=>{
    const event=decisions[j.invocation],actions=event?.payload?.proposal?.actions||[],ids=[];
    actions.forEach(a=>{
      if(a.project&&s.projects?.[a.project]?.domain)ids.push(s.projects[a.project].domain);
      else if(a.domain)ids.push(a.domain);
    });
    return [...new Set(ids.filter(Boolean))];
  };
  // Every tenth accepted cycle is a governed Bob reflection, regardless of
  // whether an older model happened to include the word in its raw title.
  const postResearchTopic=post=>s.projects?.[post.project]?.domain;
  const postTopic=post=>Number(post.created_version)%10===0?'reflection':postResearchTopic(post);
  const postMeta=(post,invocation)=>{const reflection=postTopic(post)==='reflection',topic=postResearchTopic(post),status=String(post.status||'published');return `<div class="record-panel-meta blog-meta"><span class="record-type">${reflection?'REFLECTION':'BLOG'}</span><span class="record-status">${badge(status,status.toUpperCase())}</span><span class="record-topics">${topic?topicTag(topic,'blog'):''}</span><time datetime="${esc(invocation.time)}">${esc(fmt(invocation.time))}</time></div>`;};
  const postTitle=post=>{
    const title=String(post.title||'').trim();
    if(!(Number(post.created_version)%10===0))return title;
    const remainder=title.replace(/^\s*(?:cycle\s*\d+\s*[:—–-]?\s*)?(?:reflection\s*[:—–-]?\s*)?/i,'').replace(/\b(?:first|inaugural)\s+reflection\b/ig,'Reflection').trim();
    return `Cycle ${post.created_version} Reflection: ${remainder||title}`;
  };
  const proofNames = {
    fresh_sessions:'Fresh-session continuity', causal_state:'Causal state intervention',
    commitment_handoff:'Commitments across providers', invalid_transition:'Invalid actions rejected',
    evidence_lifecycle:'Evidence revision and retraction', recovery:'Crash and projection recovery',
    audit_reconstruction:'Independent audit reconstruction', longitudinal:'100+ fresh invocation cycles'
  };
  function renderMetricStrip() {
    $('metrics').innerHTML = [
      [s.version,'Recorded cycles',`${fixtures} simulated · ${live} live Gemini`,'#history'],
      [inherited,'Obligations inherited','Across fresh invocations','#history/filter:inherited'],
      [rejected,'Proposals rejected','Read the drafts and recorded reasons','#history/filter:rejected'],
      [invocations.filter(i=>i.status==='recovered').length,'Calls recovered','Last valid state retained','#history/filter:recovered']
    ].map(([value,label,note,href])=>`<a class="metric" href="${href}"><strong>${value}</strong><span>${label}<small>${note}</small></span></a>`).join('');
  }
  renderMetricStrip();
  const providerSelect = $('provider-filter');
  [...new Set(invocations.map(i=>i.provider))].sort().forEach(provider => {
    const option = document.createElement('option'); option.value=provider; option.textContent=provider; providerSelect.append(option);
  });
  // Event kinds evolve with the durable record. Build this selector from the
  // exported history so a newly introduced receipt never becomes invisible.
  const eventSelect = $('event-filter');
  [...new Set(data.events.map(event=>displayEventKind(event.kind)))].sort().forEach(kind => {
    const option = document.createElement('option'); option.value=kind; option.textContent=kind; eventSelect.append(option);
  });
  function journal() {
    const query=$('search').value.toLowerCase(), provider=providerSelect.value;
    const routeMatch=location.hash.match(/^#journal\/(topic:|cycle:)([^/]+)/);
    const selectedKind=routeMatch?.[1]||'', selected=decodeURIComponent(routeMatch?.[2]||'');
    const entries=[...s.journal].reverse().filter(j =>
      (provider==='all'||s.invocations[j.invocation].provider===provider) &&
      (!selected||(selectedKind==='topic:'?journalTopics(j).includes(selected):String(j.cycle)===selected)) &&
      `${j.title} ${j.summary} ${j.invocation} ${j.cycle} ${journalTopics(j).map(topicLabel).join(' ')}`.toLowerCase().includes(query));
    $('entries').innerHTML=entries.slice(0,journalLimit).map(j => {
      const i=s.invocations[j.invocation], event=decisions[j.invocation], actions=event.payload.proposal.actions;
      return `<article class="entry record-panel" id="cycle-${j.cycle}"><div class="record-panel-head"><div class="record-panel-meta journal-meta"><span class="record-type">JOURNAL · WAKE✳︎ ${String(j.cycle).padStart(3,'0')}</span><span class="record-status">${badge(i.provider==='fixture'?'simulated':'accepted',i.provider==='fixture'?'SIMULATED':'ACCEPTED')}</span><span class="record-topics journal-topics">${journalTopics(j).map(id=>topicTag(id,'journal')).join('')}</span><time datetime="${esc(i.time)}">${esc(fmt(i.time))}</time></div><h3><a href="#journal/cycle:${j.cycle}">${esc(j.title)}</a></h3></div><div class="record-panel-body"><p>${esc(j.summary)}</p><div class="entry-bottom"><span>${esc(i.provider)} / ${esc(i.model)}</span><span>${actions.length} recorded change${actions.length===1?'':'s'}</span></div><details class="lab-notes"><summary>LAB NOTES / ${actions.length} RECORDED CHANGE${actions.length===1?'':'S'}</summary><div class="lab-notes-body">${actions.map(a=>`<div class="decision"><strong>${esc(a.type)} / ${esc(a.id)}</strong><p>${esc(a.statement||a.task||a.status)}</p><p>${esc(a.reason)}</p>${refs(a.evidence)}</div>`).join('') || '<p>No state changes proposed.</p>'}</div></details><a class="subtle" href="#history/${encodeURIComponent(j.invocation)}">Full invocation & decision →</a></div></article>`;
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
    const evidenceRecords=Object.values(s.evidence||{});
    const evidenceCount=evidenceRecords.length, projects=Object.values(s.projects||{}), notebooks=Object.values(s.notebooks||{});
    const evidenceTelemetry=evidenceRecords.map(item=>{
      let payload={};
      try{payload=JSON.parse(item?.content||'{}')}catch{}
      return {
        id:item?.id||'',
        actor:item?.actor||'unknown',
        role:payload?.evidence_role||'unspecified',
        tier:payload?.host_tier||'unspecified',
        topic:payload?.topic_domain||'unattributed',
        source:item?.source||'',
        persistent:Array.isArray(payload?.persistent_identifiers)?payload.persistent_identifiers:[]
      };
    });
    const evidenceRoles=evidenceTelemetry.reduce((acc,item)=>(acc[item.role]=(acc[item.role]||0)+1,acc),{});
    const evidenceTiers=evidenceTelemetry.reduce((acc,item)=>(acc[item.tier]=(acc[item.tier]||0)+1,acc),{});
    const qualifyingEvidence=evidenceTelemetry.filter(item=>item.role==='source'&&item.tier!=='verification-metadata').length;
    const discoveryEvidence=Number(evidenceRoles.discovery||0);
    const metadataEvidence=Number(evidenceRoles.metadata||0);
    const evidenceTierRows=Object.entries(evidenceTiers).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]));
    const evidenceTierMax=Math.max(1,...evidenceTierRows.map(([,count])=>count));
    const evidenceTierBars=evidenceTierRows.slice(0,7).map(([tier,count])=>`<div class="ops-provenance-row"><span>${esc(String(tier).replaceAll('-',' '))}</span><div><i style="width:${Math.max(4,100*count/evidenceTierMax)}%"></i></div><strong>${count}</strong></div>`).join('')||'<p class="empty">No evidence provenance recorded.</p>';
    const opsDriveScored=invocations.filter(item=>item?.inquiry_drive_shadow&&item.status==='accepted');
    const opsDrive=opsDriveScored.at(-1)?.inquiry_drive_shadow||null;
    const opsDriveGate=opsDrive?.activation||null;
    const opsDriveProjects=Array.isArray(opsDrive?.projects)?opsDrive.projects:[];
    const opsDriveStatus=!opsDrive?'WAITING':opsDriveGate?.active?'ACTIVE / ADVISORY':opsDriveGate?.operator_enabled?'LOCKED / OBSERVING':'SHADOW ONLY';
    const opsDriveRows=opsDriveProjects.map((project,index)=>{
      const components=project.components||{};
      const dims=[
        ['C','continuity'],['N','novelty'],['H','coherence'],['G','generativity'],['S','self_correction']
      ].map(([short,key])=>{
        const value=Math.max(0,Math.min(1,Number(components[key])||0));
        return `<span title="${esc(key.replaceAll('_',' '))}: ${Math.round(value*100)}%"><b>${short}</b><i style="--drive-component:${(value*100).toFixed(0)}%"></i></span>`;
      }).join('');
      const score=Math.max(0,Math.min(1,Number(project.score)||0));
      return `<div class="ops-drive-row"><em>${index+1}</em><div class="ops-drive-copy"><strong>${esc(project.title||project.id||'Untitled project')}</strong><small>${esc(project.id||'')}</small></div><div class="ops-drive-components">${components?dims:''}</div><div class="ops-drive-score" style="--drive-score:${(score*100).toFixed(0)}%"><b>${Math.round(score*100)}</b><span>%</span></div></div>`;
    }).join('')||'<p class="empty">No active research projects were scored in the latest accepted wake.</p>';
    const opsDriveTraceSource=opsDriveScored.slice(-40);
    const opsDriveTrace=opsDriveTraceSource.map(item=>{
      const shadow=item.inquiry_drive_shadow||{};
      const projects=Array.isArray(shadow.projects)?shadow.projects:[];
      const leader=projects.reduce((best,current)=>!best||Number(current.score)>Number(best.score)?current:best,null);
      const score=Math.max(0,Math.min(1,Number(leader?.score)||0));
      const active=shadow.activation?.active===true;
      return `<a class="ops-drive-tick ${active?'advisory':'shadow'}" href="#history/${encodeURIComponent(item.id)}" style="--drive-height:${Math.max(5,score*100).toFixed(0)}%" title="${esc(item.id)} · leader ${esc(leader?.title||'none')} · ${Math.round(score*100)}% · ${active?'advisory':'shadow'}"></a>`;
    }).join('');
    const opsResearch=Object.values(s.research||{});
    const opsNotebooks=Object.values(s.notebooks||{});
    const opsPosts=Object.values(s.posts||{});
    const opsProjectTrajectories=projects
      .slice()
      .sort((a,b)=>String(a.status||'active').localeCompare(String(b.status||'active'))||Number(b.updated_version||b.created_version||0)-Number(a.updated_version||a.created_version||0))
      .map(project=>{
        const research=opsResearch.filter(item=>item?.project===project.id);
        const collected=research.filter(item=>item?.status==='collected').length;
        const failed=research.filter(item=>item?.status==='failed').length;
        const notebooksForProject=opsNotebooks.filter(item=>item?.project===project.id);
        const postsForProject=opsPosts.filter(item=>item?.project===project.id&&item?.status!=='superseded');
        const stageValues=[
          ['QUESTION',1],
          ['SOURCES',collected],
          ['NOTEBOOK',notebooksForProject.length],
          ['PUBLISHED',postsForProject.length]
        ];
        const stages=stageValues.map(([label,value],index)=>`<span class="ops-trajectory-stage ${value?'lit':''}" title="${label}: ${value}"><i></i><b>${label}</b><small>${index===0?'recorded':value}</small></span>`).join('');
        return `<a class="ops-trajectory-row" data-project-status="${esc(project.status||'active')}" href="#projects/${encodeURIComponent(project.id)}"><div class="ops-trajectory-copy"><strong>${esc(project.title||project.id)}</strong><span>${esc(String(project.status||'active').toUpperCase())} · ${research.length} research receipts · ${failed} failed</span></div><div class="ops-trajectory-stages">${stages}</div></a>`;
      }).join('')||'<p class="empty">No research projects in the current durable state.</p>';
    const opsBeliefs=Object.values(s.beliefs||{});
    const opsActiveBeliefs=opsBeliefs.filter(item=>item?.status==='active');
    const opsRetractedBeliefs=opsBeliefs.filter(item=>item?.status==='retracted');
    const activeConfidences=opsActiveBeliefs.map(item=>Number(item.confidence)).filter(Number.isFinite).sort((a,b)=>a-b);
    const medianConfidence=activeConfidences.length?activeConfidences[Math.floor((activeConfidences.length-1)/2)]:null;
    const falsifierCount=opsActiveBeliefs.filter(item=>String(item?.falsifier||'').trim()).length;
    const beliefEvidenceRoots=opsActiveBeliefs.reduce((sum,item)=>sum+(Array.isArray(item?.evidence)?item.evidence.length:0),0);
    const confidenceBands=[
      ['0–.2',0,.2],['.2–.4',.2,.4],['.4–.6',.4,.6],['.6–.8',.6,.8],['.8–1',.8,1.000001]
    ].map(([label,low,high])=>[label,activeConfidences.filter(value=>value>=low&&value<high).length]);
    const confidenceBandMax=Math.max(1,...confidenceBands.map(([,count])=>count));
    const confidenceBars=confidenceBands.map(([label,count])=>`<div class="ops-belief-band"><span>${label}</span><div><i style="width:${Math.max(count?5:0,100*count/confidenceBandMax)}%"></i></div><strong>${count}</strong></div>`).join('');
    const providerRequests=completed.reduce((n,i)=>n+(i.provider_requests_sent||0),0);
    const requestsPerAccepted=acceptedCount?(providerRequests/acceptedCount).toFixed(2):'—';
    const wakeStatus=data.wake_status||{};
    const applicationAccess=data.application_access||null;
    const accessEnabled=typeof applicationAccess?.enabled==='boolean'?applicationAccess.enabled:null;
    const sourceMeta=data.source||{};
    const recordIntegrity=data.record_integrity||null;
    const recordReplayOk=recordIntegrity?.semantic_replay_verified===true;
    const sqliteQuickOk=recordIntegrity?.sqlite_quick_check==='ok';
    const shortHead=String(data.head||sourceMeta.head||'').slice(0,12)||'—';
    const runtimeRef=String(sourceMeta.runtime_ref||'').slice(0,12)||'—';
    const sourceAuthority=sourceMeta.authority||'derived projection';
    const matrixProgress=data.matrix_progress||null;
    const matrixEnabled=matrixProgress?.enabled===true;
    const experimental=s.experimental||null;
    const timeControl=experimental?.controls?.time_dilation||null;
    const temporalState=s.temporal||null;
    const temporalInvocations=invocations
      .filter(item=>item?.temporal&&Number.isFinite(Number(item.temporal.wall_elapsed_seconds)))
      .sort((a,b)=>new Date(a.temporal.observed_at||a.time||0)-new Date(b.temporal.observed_at||b.time||0));
    const latestTemporal=temporalInvocations.at(-1)?.temporal||null;
    const formatDuration=value=>{
      const seconds=Number(value);
      if(!Number.isFinite(seconds))return '—';
      if(seconds<60)return seconds.toFixed(seconds<10?1:0)+'s';
      if(seconds<3600)return (seconds/60).toFixed(seconds<600?1:0)+'m';
      if(seconds<86400)return (seconds/3600).toFixed(seconds<36000?1:0)+'h';
      return (seconds/86400).toFixed(seconds<864000?1:0)+'d';
    };
    const temporalTraceSource=temporalInvocations.slice(-48);
    const temporalWallMax=Math.max(1,...temporalTraceSource.map(item=>Number(item.temporal.wall_elapsed_seconds)||0));
    const temporalTrace=temporalTraceSource.map((item,index)=>{
      const temporal=item.temporal;
      const wall=Number(temporal.wall_elapsed_seconds)||0;
      const effective=Number(temporal.effective_elapsed_seconds)||0;
      const height=Math.max(5,Math.min(100,100*Math.sqrt(wall/temporalWallMax)));
      const ratio=wall>0?effective/wall:0;
      const tone=ratio===0?'frozen':ratio>1.001?'scaled':'real';
      return `<a class="ops-time-tick ${tone}" href="#history/${encodeURIComponent(item.id)}" style="--tick-height:${height.toFixed(1)}%" title="${esc(item.id)} · wall ${formatDuration(wall)} · effective ${formatDuration(effective)} · ${Number(temporal.cycle_distance||0)} cycles · ${Number(temporal.intervening_events?.total||0)} events" aria-label="Temporal receipt ${index+1}: wall ${formatDuration(wall)}, effective ${formatDuration(effective)}"></a>`;
    }).join('');
    const appObservability=data.application_observability||null;
    const wakeApp=(appObservability?.applications||[]).find(app=>app?.id==='wake')||null;
    const appActions=wakeApp?.actions||{};
    const appInvocations=wakeApp?.invocations||{};
    const lifecycleRecent=Array.isArray(appInvocations.recent)?appInvocations.recent.slice(-8):[];
    const lifecycleTraces=lifecycleRecent.map(item=>{
      const stages=Array.isArray(item.stages)?item.stages:[];
      const dots=stages.map(stage=>`<i class="trace-stage" data-stage="${esc(stage||'unknown')}" title="${esc(stage||'unknown')}"></i>`).join('');
      const outcome=item.outcome||item.latest_stage||'unknown';
      return `<a class="ops-trace-row" href="#history/${encodeURIComponent(item.invocation_id||'')}" title="${esc(item.invocation_id||'invocation')} · ${esc(outcome)}"><span>${esc(String(item.invocation_id||'').slice(-10)||'—')}</span><div>${dots}</div><strong>${esc(String(outcome).replaceAll('_',' '))}</strong></a>`;
    }).join('')||'<p class="empty">No recent invocation lifecycle receipts.</p>';
    const matrixCompleted=Number(matrixProgress?.completed_count||0);
    const matrixTotal=Number(matrixProgress?.cell_count||343);
    const matrixPct=matrixTotal?Math.round(100*matrixCompleted/matrixTotal):0;
    const matrixStatusCounts=matrixProgress?.status_counts||{};
    const matrixFailed=Number(matrixStatusCounts.failed||0);
    const matrixDeferred=Number(matrixStatusCounts.deferred||0);
    const currentStatus=accessEnabled===false?'STOPPED':wakeStatus.pending?'PENDING':wakeStatus.next_eligible?'WAITING':'IDLE';
    const latestAttempt=wakeStatus.latest_attempt||null;
    const latestAttemptStatus=latestAttempt?.status||'none';
    const latestModel=latestAttempt?.successful_model||latestAttempt?.provider_attempts?.at?.(-1)?.model||'—';
    const attempts=[...completed].sort((a,b)=>new Date(a.time)-new Date(b.time)).slice(-100);
    const contextInvocations=invocations
      .filter(item=>item?.context_delivery&&Number.isFinite(Number(item.context_delivery.rich_context_chars)))
      .sort((a,b)=>new Date(a.time||0)-new Date(b.time||0));
    const latestContext=contextInvocations.at(-1)||null;
    const contextDelivery=latestContext?.context_delivery||null;
    const contextMetrics=latestContext?.working_set_metrics||{};
    const contextTraceSource=contextInvocations.slice(-48);
    const contextRichMax=Math.max(1,...contextTraceSource.map(item=>Number(item.context_delivery.rich_context_chars)||0));
    const contextTrace=contextTraceSource.map(item=>{
      const delivery=item.context_delivery||{};
      const rich=Number(delivery.rich_context_chars)||0;
      const delivered=Number(delivery.delivered_request_chars||delivery.delivered_context_chars)||0;
      const outer=Math.max(5,Math.min(100,100*Math.sqrt(rich/contextRichMax)));
      const inner=rich>0?Math.max(2,Math.min(100,100*delivered/rich)):0;
      const bounded=delivery.mode==='bounded';
      return `<a class="ops-context-tick ${bounded?'bounded':'rich'}" href="#history/${encodeURIComponent(item.id)}" style="--context-height:${outer.toFixed(1)}%;--context-fill:${inner.toFixed(1)}%" title="${esc(item.id)} · ${esc(delivery.mode||'rich')} · rich ${rich.toLocaleString()} chars · delivered ${delivered.toLocaleString()} chars" aria-label="${esc(item.id)} context: ${esc(delivery.mode||'rich')}, ${Math.round(inner)} percent delivered"></a>`;
    }).join('');
    const timeline=attempts.map((i,index)=>`<a class="wake-cell ${esc(i.status||'unknown')}" href="#history/${encodeURIComponent(i.id)}" title="${esc(i.id)} · ${esc((i.status||'unknown').toUpperCase())} · ${esc(i.successful_model||i.model||i.provider||'')}" aria-label="Attempt ${index+1}: ${esc(i.status||'unknown')}"></a>`).join('');
    const statuses=[['accepted',acceptedCount],['rejected',rejectedCount],['deferred',deferredCount],['failed',failedCount],['recovered',recoveredCount]], maxStatus=Math.max(1,...statuses.map(x=>x[1]));
    const outcomeBars=statuses.map(([name,value])=>`<div class="metric-bar-row"><span>${esc(name)}</span><div><i class="metric-bar ${esc(name)}" style="width:${Math.max(value?3:0,100*value/maxStatus)}%"></i></div><strong>${value}</strong></div>`).join('');
    const models={}; completed.forEach(i=>{const key=i.successful_model||i.model||i.provider||'unknown';models[key]??={attempts:0,accepted:0,requests:0};models[key].attempts++;models[key].accepted+=i.status==='accepted'?1:0;models[key].requests+=i.provider_requests_sent||0;});
    const modelRows=Object.entries(models).sort((a,b)=>b[1].attempts-a[1].attempts).map(([name,m])=>`<div class="model-metric-row"><strong>${esc(name)}</strong><span>${m.attempts} wakes</span><span>${m.accepted} accepted</span><span>${m.requests} HTTP requests</span></div>`).join('');
    const fullMetrics=data.metrics||{};
    const storageMetrics=fullMetrics.storage||{};
    const sqliteBytes=Number(storageMetrics.sqlite_bytes);
    const durableEventCount=Number(storageMetrics.event_count);
    const formatBytes=value=>{
      if(!Number.isFinite(value))return '—';
      if(value<1024)return value+' B';
      const units=['KB','MB','GB','TB'];
      let size=value/1024,index=0;
      while(size>=1024&&index<units.length-1){size/=1024;index++;}
      return (size>=100?size.toFixed(0):size>=10?size.toFixed(1):size.toFixed(2))+' '+units[index];
    };
    const sqliteSize=formatBytes(sqliteBytes);
    const eventRecordCount=Number.isFinite(durableEventCount)?durableEventCount:'—';
    const reasonCounts={...(fullMetrics.rejection_reasons||{})};
    if(!Object.keys(reasonCounts).length){
      data.events.filter(e=>e.kind==='rejected').forEach(e=>{
        const key=String(e.payload.reason||'Unspecified rejection').split(':')[0].slice(0,90);
        reasonCounts[key]=(reasonCounts[key]||0)+1;
      });
    }
    const sortedReasons=Object.entries(reasonCounts).sort((a,b)=>b[1]-a[1]);
    const reasons=sortedReasons.slice(0,8).map(([reason,n])=>`<div class="reason-row"><strong>${n}</strong><span>${esc(reason)}</span></div>`).join()||'<p class="empty">No rejected proposals in this record.</p>';
    const pressureMax=Math.max(1,...sortedReasons.slice(0,5).map(([,n])=>n));
    const pressureBars=sortedReasons.slice(0,5).map(([reason,n])=>`<div class="ops-pressure-row"><span>${esc(reason)}</span><div><i style="width:${Math.max(4,100*n/pressureMax)}%"></i></div><strong>${n}</strong></div>`).join('')||'<p class="empty">No rejection pressure recorded.</p>';
    const dailyLimit=Number(wakeStatus.daily_call_limit);
    const requestSlots=Number(wakeStatus.provider_request_slots_today||0);
    const quotaPct=Number.isFinite(dailyLimit)&&dailyLimit>0?Math.max(0,Math.min(100,100*requestSlots/dailyLimit)):0;

    const fullActions=fullMetrics.accepted_actions;
    const actionEvents=accepted.map(e=>({cycle:e.payload.proposal?.base_version+1||0,actions:e.payload.proposal?.actions||[]}));
    const acceptedActions=actionEvents.flatMap(row=>row.actions.map(action=>({cycle:row.cycle,action})));
    const actionCounts=fullActions?.by_type?{...fullActions.by_type}:{};
    if(!fullActions) acceptedActions.forEach(({action})=>actionCounts[action.type]=(actionCounts[action.type]||0)+1);
    const sortedActionCounts=Object.entries(actionCounts).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]));
    const actionTypes=sortedActionCounts.map(([type])=>type);
    const actionTotal=fullActions?.total??acceptedActions.length;

    // One canonical population powers this entire matrix: accepted proposal actions.
    // Topic attribution remains conservative. A topic is used only when the action
    // carries a domain or references a durable project with a recorded domain.
    const actionTopic=action=>{
      if(action.domain)return action.domain;
      const projectId=action.project || (action.type==='project'?action.id:null);
      if(projectId&&s.projects?.[projectId]?.domain)return s.projects[projectId].domain;
      return null;
    };
    const topicStats=Object.fromEntries((s.research_topics||[]).map(t=>[t.id,{label:t.label,actions:{},total:0}]));
    const systemActions={actions:{},total:0};
    if(fullActions){
      Object.entries(fullActions.by_topic||{}).forEach(([topicId,row])=>{
        if(topicStats[topicId]){
          topicStats[topicId].actions={...(row.by_type||{})};
          topicStats[topicId].total=row.total||0;
        }
      });
      systemActions.actions={...(fullActions.unattributed?.by_type||{})};
      systemActions.total=fullActions.unattributed?.total||0;
    }else{
      acceptedActions.forEach(({action})=>{
        const topicId=actionTopic(action);
        const target=topicId&&topicStats[topicId]?topicStats[topicId]:systemActions;
        target.actions[action.type]=(target.actions[action.type]||0)+1;
        target.total++;
      });
    }
    const topicRows=Object.entries(topicStats)
      .map(([id,t])=>({id,...t}))
      .filter(t=>t.total>0)
      .sort((a,b)=>b.total-a.total||a.label.localeCompare(b.label));
    const configuredTopicCount=(s.research_topics||[]).length;
    const topicAttributedTotal=topicRows.reduce((n,t)=>n+t.total,0);
    const matrixCell=(count,total)=>count
      ? `<span class="matrix-value" style="--cell-fill:${Math.max(8,100*count/Math.max(1,total))}%"><b>${count}</b></span>`
      : '<span class="matrix-value zero">0</span>';
    const matrixHeader=actionTypes.map((type,index)=>`<button type="button" class="matrix-sort" data-matrix-sort-index="${index+1}" data-matrix-sort-label="${esc(type)}" aria-label="Sort by ${esc(type)} count">${esc(type)}<span aria-hidden="true">↕</span></button>`).join('');
    const matrixRows=topicRows.map(t=>`<div class="matrix-row"><a class="matrix-topic" data-topic="${esc(t.id)}" style="--topic-color:${esc(topicColors[t.id]||'var(--cyan)')}" href="#projects/topic:${encodeURIComponent(t.id)}">${esc(t.label)}</a>${actionTypes.map(type=>matrixCell(t.actions[type]||0,t.total)).join('')}<strong class="matrix-total">${t.total}</strong></div>`).join('');
    const matrixTotals=actionTypes.map(type=>`<strong>${actionCounts[type]||0}</strong>`).join('');
    const systemMatrix=systemActions.total
      ? `<div class="matrix-system-row"><span>UNATTRIBUTED / SYSTEM</span>${actionTypes.map(type=>`<b>${systemActions.actions[type]||0}</b>`).join('')}<strong>${systemActions.total}</strong></div>`
      : '';
    const mobileMatrix=topicRows.map(t=>`<details class="matrix-topic-card"><summary><span>${esc(t.label)}</span><strong>${t.total}</strong></summary><div>${actionTypes.filter(type=>t.actions[type]).map(type=>`<p><span>${esc(type)}</span><b>${t.actions[type]}</b></p>`).join('')}</div></details>`).join('')
      + (systemActions.total?`<details class="matrix-topic-card matrix-system-card"><summary><span>Unattributed / system</span><strong>${systemActions.total}</strong></summary><div>${actionTypes.filter(type=>systemActions.actions[type]).map(type=>`<p><span>${esc(type)}</span><b>${systemActions.actions[type]}</b></p>`).join('')}</div></details>`:'');
    const windows=[]; for(let i=0;i<completed.length;i+=10){const group=completed.slice(i,i+10),a=group.filter(x=>x.status==='accepted').length,r=group.filter(x=>x.status==='rejected').length,d=group.filter(x=>x.status==='deferred').length;windows.push({label:`${i+1}–${i+group.length}`,a,r,d,total:group.length});}
    const trend=windows.map(w=>`<div class="trend-col" title="Wakes ${w.label}: ${w.a} accepted, ${w.r} rejected, ${w.d} deferred"><div class="trend-stack"><i class="accepted" style="height:${100*w.a/w.total}%"></i><i class="rejected" style="height:${100*w.r/w.total}%"></i><i class="deferred" style="height:${100*w.d/w.total}%"></i></div><span>${w.label}</span></div>`).join('');

    const beliefs=Object.values(s.beliefs||{}), activeBeliefs=beliefs.filter(b=>b.status==='active'), retractedBeliefs=beliefs.filter(b=>b.status==='retracted');
    const revisedBeliefs=fullActions?.belief_actions??actionEvents.flatMap(x=>x.actions).filter(a=>a.type==='belief').length;
    const overdue=obligations.filter(c=>c.status==='open'&&s.version>=c.due_cycle).length;
    const fallbackWakes=completed.filter(i=>(i.provider_attempts||[]).length>1).length;
    const knownAttempts=completed.flatMap(i=>(i.provider_attempts||[]).map((attempt,index)=>({...attempt,_wake:i.id,_attempt:index+1}))).filter(a=>a.result!=='unknown');
    const latency=knownAttempts.map(a=>a.elapsed_ms).filter(Number.isFinite).sort((a,b)=>a-b);
    const providerTraceSource=knownAttempts.slice(-64);
    const providerLatencyMax=Math.max(1,...providerTraceSource.map(a=>Number(a.elapsed_ms)||0));
    const providerTrace=providerTraceSource.map(attempt=>{
      const ms=Number(attempt.elapsed_ms)||0;
      const height=Math.max(6,Math.min(100,100*Math.sqrt(ms/providerLatencyMax)));
      const result=String(attempt.result||'unknown').toLowerCase().replace(/[^a-z0-9_-]+/g,'-');
      const model=attempt.model||attempt.provider||'provider';
      return `<a class="ops-provider-tick" data-result="${esc(result)}" href="#history/${encodeURIComponent(attempt._wake||'')}" style="--provider-height:${height.toFixed(1)}%" title="${esc(model)} · ${esc(attempt.result||'unknown')} · ${ms.toLocaleString()} ms · attempt ${attempt._attempt}" aria-label="${esc(model)}, ${esc(attempt.result||'unknown')}, ${ms} milliseconds"></a>`;
    }).join('');
    const trueMedian=values=>{if(!values.length)return null;const m=Math.floor(values.length/2);return values.length%2?values[m]:(values[m-1]+values[m])/2;};
    const medianLatency=latency.length?Math.round(trueMedian(latency)):null;
    const sortedCompleted=[...completed].sort((a,b)=>new Date(a.time)-new Date(b.time));
    const firstTime=sortedCompleted[0]?.time, lastTime=sortedCompleted.at(-1)?.time;
    const recordHours=firstTime&&lastTime?Math.max(0,(new Date(lastTime)-new Date(firstTime))/36e5):0;
    const wakesPerHour=recordHours?completed.length/recordHours:0;
    const acceptedPerHour=recordHours?acceptedCount/recordHours:0;
    const actionPerAccepted=acceptedCount?(actionTotal/acceptedCount):0;
    const evidencePerAccepted=acceptedCount?(evidenceCount/acceptedCount):0;
    const openCommitments=obligations.filter(c=>c.status==='open');
    const openObligations=openCommitments.length;
    const obligationBuckets=[
      ['OVERDUE',openCommitments.filter(item=>Number(item.due_cycle)<Number(s.version)).length,'danger'],
      ['DUE NOW',openCommitments.filter(item=>Number(item.due_cycle)===Number(s.version)).length,'warning'],
      ['NEXT 1–3',openCommitments.filter(item=>Number(item.due_cycle)>Number(s.version)&&Number(item.due_cycle)<=Number(s.version)+3).length,'info'],
      ['NEXT 4–10',openCommitments.filter(item=>Number(item.due_cycle)>Number(s.version)+3&&Number(item.due_cycle)<=Number(s.version)+10).length,'info'],
      ['LATER',openCommitments.filter(item=>Number(item.due_cycle)>Number(s.version)+10).length,'neutral']
    ];
    const obligationHorizon=obligationBuckets.map(([label,count,tone])=>`<div class="ops-horizon-bucket ${tone}"><span>${label}</span><strong>${count}</strong><div>${Array.from({length:Math.min(count,18)},()=>'<i></i>').join('')}</div></div>`).join('');
    const providerSuccesses=knownAttempts.filter(a=>['success','accepted','ok'].includes(String(a.result||'').toLowerCase())).length;
    const fallbackRate=completed.length?100*fallbackWakes/completed.length:0;
    const rejectionRate=completed.length?100*rejectedCount/completed.length:0;
    const topicActive=topicRows.length;
    // Recovery telemetry is derived from durable receipts and frame records;
    // it describes interventions without treating them as research success.
    const frames=Object.values(s.representations||{}).flat();
    const capabilityBlocks=Object.values(s.acquisition||{}).filter(x=>x.capability_blocked).length;
    const parkedTopics=Object.keys(s.attention?.deferred||{}).length;
    const telemetry=[
      ['Wall-clock span',recordHours>=24?(recordHours/24).toFixed(1)+'d':recordHours.toFixed(1)+'h','first → latest completed wake · idle included','neutral'],
      ['Completed / wall h',wakesPerHour.toFixed(2)+'/h',completed.length+' completed wakes across elapsed wall time','neutral'],
      ['Accepted / wall h',acceptedPerHour.toFixed(2)+'/h',acceptedCount+' accepted wakes across elapsed wall time','success'],
      ['Rejection pressure',rejectionRate.toFixed(1)+'%',rejectedCount+' rejected','danger'],
      ['Fallback rate',fallbackRate.toFixed(1)+'%',fallbackWakes+' multi-attempt wakes','warning'],
      ['Actions / accepted',actionPerAccepted.toFixed(2),actionTotal+' durable actions','neutral'],
      ['Evidence density',evidencePerAccepted.toFixed(2),evidenceCount+' current evidence records ÷ '+acceptedCount+' accepted wakes','info'],
      ['Topic coverage',topicActive+'/'+configuredTopicCount,'configured topics with accepted-action activity','info'],
      ['Open obligations',openObligations,String(overdue)+' overdue',openObligations?'warning':'success'],
      ['Capability blocks',capabilityBlocks,'equivalent retrieval routes paused',capabilityBlocks?'warning':'neutral'],
      ['Problem frames',frames.length,'strategy hypotheses; not findings','neutral'],
      ['Attention parking',parkedTopics,'topics preserved while attention moves','neutral'],
      ['Known provider attempts',knownAttempts.length,providerSuccesses+' success-labelled','neutral'],
      ['SQLite database',sqliteSize,Number.isFinite(sqliteBytes)?sqliteBytes.toLocaleString()+' bytes on wake-state':'Waiting for promoted runtime metric','info'],
      ['Durable events',eventRecordCount,Number.isFinite(durableEventCount)?'append-only event rows in SQLite':'Waiting for promoted runtime metric','info']
    ];
    const telemetryHtml=telemetry.map(([label,value,note,tone])=>`<article class="telemetry-cell ${tone||'neutral'}"><span>${label}</span><strong>${value}</strong><small>${note}</small></article>`).join('');
    const card=(value,label,note)=>`<article class="metric-card"><strong>${value}</strong><span>${label}</span><small>${note}</small></article>`;

    const hypotheses=[];
    if(completed.length>=20){const recent=completed.slice(-20),prior=completed.slice(-40,-20);if(prior.length>=10){const rr=recent.filter(i=>i.status==='accepted').length/recent.length,pr=prior.filter(i=>i.status==='accepted').length/prior.length;if(Math.abs(rr-pr)>=.1)hypotheses.push({title:'Outcome regime may be shifting',text:`Acceptance moved from ${Math.round(pr*100)}% in the prior window to ${Math.round(rr*100)}% in the latest 20 wakes. This is an observed association, not a causal explanation.`});}}
    if(topicRows.length>=2&&topicRows[0].total>Math.max(2,topicRows.at(-1).total*2))hypotheses.push({title:'Research attention is uneven',text:`${topicRows[0].label} currently has ${topicRows[0].total} accepted actions versus ${topicRows.at(-1).total} for ${topicRows.at(-1).label}. The record supports an attention-skew hypothesis; it does not establish topic value.`});
    if(fallbackWakes)hypotheses.push({title:'Provider fallback is part of observed continuity',text:`${fallbackWakes} completed wakes required more than one model attempt. Compare their outcomes with single-attempt wakes before attributing any quality effect to fallback.`});
    if(rejectedCount)hypotheses.push({title:'Rejection is measurable governance work',text:`${rejectedCount} completed wakes were rejected while durable state advanced ${s.version} cycles. Rejections are observable resistance in the process, not automatically failure or success.`});
    if(!hypotheses.length)hypotheses.push({title:'Not enough separation yet',text:'The current record does not show a strong simple pattern worth elevating. Keep collecting data rather than manufacturing a story.'});
    const outcomeTotal=Math.max(1,acceptedCount+rejectedCount+deferredCount+failedCount+recoveredCount);
    const outcomePie=[
      ['accepted',acceptedCount,'var(--success)'],['rejected',rejectedCount,'var(--danger)'],['deferred',deferredCount,'var(--warning)'],['failed',failedCount,'var(--failure)'],['recovered',recoveredCount,'var(--info)']
    ].filter(x=>x[1]>0);
    let pieCursor=0;
    const pieStops=outcomePie.map(([name,value,color])=>{const start=pieCursor,end=pieCursor+=100*value/outcomeTotal;return `${color} ${start.toFixed(2)}% ${end.toFixed(2)}%`;}).join(',');
    const outcomePieHtml=`<div class="visual-summary"><div class="outcome-pie" style="background:conic-gradient(${pieStops||'var(--line) 0 100%'})" role="img" aria-label="Outcome composition: ${outcomePie.map(([n,v])=>n+' '+v).join(', ')}"><span><strong>${completed.length}</strong><small>completed</small></span></div><div class="visual-legend">${outcomePie.map(([name,value])=>`<span class="${esc(name)}"><i></i><b>${value}</b> ${esc(name)}</span>`).join('')}</div></div>`;
    const topicMax=Math.max(1,...topicRows.map(t=>t.total));
    const topicBars=topicRows.map(t=>`<a class="topic-bar-row" href="#projects/topic:${encodeURIComponent(t.id)}" style="--topic-color:${esc(topicColors[t.id]||'var(--cyan)')}"><span>${esc(t.label)}</span><div><i style="width:${100*t.total/topicMax}%"></i></div><strong>${t.total}</strong></a>`).join('');
    const hypothesisHtml=hypotheses.map(h=>`<article class="hypothesis-card"><p class="eyebrow">DATA-DERIVED HYPOTHESIS</p><h3>${esc(h.title)}</h3><p>${esc(h.text)}</p></article>`).join('');

    const matrixAxes=matrixProgress?.axes||[];
    const semanticAxis=matrixAxes[0]?.values||[];
    const exposureAxis=matrixAxes[1]?.values||[];
    const pressureAxis=matrixAxes[2]?.values||[];
    const matrixStatuses=Array.isArray(matrixProgress?.cells)?matrixProgress.cells:[];
    const matrixPlanes=semanticAxis.map((semantic,semanticIndex)=>{
      const offset=semanticIndex*49;
      const cells=matrixStatuses.slice(offset,offset+49);
      const cellHtml=cells.map((status,localIndex)=>{
        const exposure=exposureAxis[Math.floor(localIndex/7)]?.label||'Exposure';
        const pressure=pressureAxis[localIndex%7]?.label||'Pressure';
        const ordinal=offset+localIndex+1;
        const isNext=ordinal===Number(matrixProgress?.next_ordinal||0);
        return `<i class="continuity-cell ${esc(status||'open')} ${isNext?'next':''}" title="${esc(semantic.label)} · ${esc(exposure)} · ${esc(pressure)}" aria-label="${esc(semantic.label)}, ${esc(exposure)}, ${esc(pressure)}: ${esc(status||'open')}${isNext?', next coordinate':''}"></i>`;
      }).join('');
      return `<section class="matrix-plane"><header><span>${esc(semantic.label)}</span><b>${cells.filter(status=>status==='completed').length}/49</b></header><div class="matrix-plane-grid" role="group" aria-label="${esc(semantic.label)} continuity plane">${cellHtml}</div></section>`;
    }).join('');
    const recordTail=(data.events||[]).slice(-64);
    const recordSpine=recordTail.map(event=>{
      const tone=event.kind==='accepted'?'accepted':event.kind==='rejected'?'rejected':event.kind==='deferred'?'deferred':'other';
      const label=`#${event.seq??'—'} · ${displayEventKind(event.kind||'event')} · ${String(event.hash||'').slice(0,12)}`;
      return `<a class="ops-record-node ${tone}" href="#history/${encodeURIComponent(event.seq??'')}" title="${esc(label)}" aria-label="${esc(label)}"></a>`;
    }).join('');
    const databaseMB=recordIntegrity?.database_bytes?Number(recordIntegrity.database_bytes)/(1024*1024):null;
    const freePct=recordIntegrity?.database_bytes?100*Number(recordIntegrity.free_bytes||0)/Number(recordIntegrity.database_bytes):null;
    const opsTopicMax=Math.max(1,...topicRows.map(topic=>topic.total));
    const visibleTopics=topicRows.slice(0,10);
    const topicNodes=visibleTopics.map((topic,index)=>{
      const size=Math.max(10,Math.min(32,10+Math.round(24*topic.total/opsTopicMax)));
      const angle=(-Math.PI/2)+(2*Math.PI*index/Math.max(1,visibleTopics.length));
      const x=(50+36*Math.cos(angle)).toFixed(2);
      const y=(50+34*Math.sin(angle)).toFixed(2);
      return `<a class="ops-topic-node" href="#projects/topic:${encodeURIComponent(topic.id)}" style="--node-size:${size}px;--node-color:${esc(topicColors[topic.id]||'var(--ops-cyan)')};--node-x:${x}%;--node-y:${y}%"><span>${esc(topic.label)}</span><b>${topic.total}</b></a>`;
    }).join('');
    $('metrics-dashboard').innerHTML=`
      <nav class="ops-storyline" aria-label="WAKE data story">
        <a href="#metrics" data-story-target="ops-now"><b>01</b><span>NOW</span><strong>cycle ${s.version}</strong></a>
        <a href="#metrics" data-story-target="ops-pressure"><b>02</b><span>PRESSURE</span><strong>${rejectedCount} rejected</strong></a>
        <a href="#metrics" data-story-target="ops-context"><b>03</b><span>MEMORY</span><strong>${contextDelivery?esc(String(contextDelivery.mode||'rich').toUpperCase()):'no receipt'}</strong></a>
        <a href="#metrics" data-story-target="ops-evidence"><b>04</b><span>EVIDENCE</span><strong>${qualifyingEvidence} substantive</strong></a>
        <a href="#metrics" data-story-target="ops-beliefs"><b>05</b><span>BELIEF</span><strong>${opsActiveBeliefs.length} active</strong></a>
        <a href="#metrics" data-story-target="ops-horizon"><b>06</b><span>FRONTIER</span><strong>${openObligations} open</strong></a>
        <a href="#metrics" data-story-target="ops-matrix"><b>07</b><span>SPACE</span><strong>${matrixPct}% mapped</strong></a>
      </nav>
      <div class="ops-story-lede" aria-label="Current record summary">
        <span>WHAT THE RECORD SAYS NOW</span>
        <p>Cycle <strong>${s.version}</strong> · <strong>${completed.length}</strong> completed wakes · <strong>${acceptedCount}</strong> accepted · <strong>${rejectedCount}</strong> rejected · <strong>${openObligations}</strong> open commitments · <strong>${qualifyingEvidence}</strong> substantive source observations · <strong>${opsActiveBeliefs.length}</strong> active beliefs · <strong>${matrixPct}%</strong> of continuity@1 covered.</p>
        <small>Counts are derived from durable receipts and current governed state. They describe WAKE's recorded history; they do not certify the truth of its research claims.</small>
      </div>
      <div class="ops-reading-key" aria-label="How to read this data story">
        <span><b>NOW</b> what happened</span>
        <i>→</i>
        <span><b>PRESSURE</b> what resisted</span>
        <i>→</i>
        <span><b>MEMORY</b> what survived compression</span>
        <i>→</i>
        <span><b>EVIDENCE</b> what was observed</span>
        <i>→</i>
        <span><b>BELIEF</b> what is carried</span>
        <i>→</i>
        <span><b>FRONTIER</b> what remains</span>
        <i>→</i>
        <span><b>SPACE</b> where continuity has been tested</span>
      </div>
      <section class="ops-console" id="ops-now" aria-label="WAKE operational research console">
        <header class="ops-console-head">
          <div><p class="eyebrow">WAKE✳︎ / RESEARCH OPERATIONS</p><h2>Live governed research field.</h2></div>
          <div class="ops-console-actions">
            <a href="map3d.html">3D RECORD MAP ↗</a>
            <a href="#history">EXACT HISTORY →</a>
            <div class="ops-state" data-status="${currentStatus.toLowerCase()}"><i></i><span>${currentStatus}</span><strong>CYCLE ${s.version}</strong></div>
          </div>
        </header>

        <div class="ops-source-rail" aria-label="Projection provenance">
          <div><span>AUTHORITY</span><strong>${esc(sourceAuthority)}</strong></div>
          <div><span>RECORD HEAD</span><strong>${esc(shortHead)}</strong></div>
          <div><span>RUNTIME</span><strong>${esc(runtimeRef)}</strong></div>
          <div class="ops-access ${accessEnabled===true?'enabled':accessEnabled===false?'disabled':'unknown'}"><span>GLOBAL ACCESS</span><strong>${accessEnabled===true?'ENABLED':accessEnabled===false?'DISABLED':'UNKNOWN'}</strong><small>DERIVED / LIVE · ${applicationAccess?'generation '+applicationAccess.generation:'state unavailable'}</small></div>
        </div>
        <div class="ops-record-spine" aria-label="Durable record integrity evidence">
          <div class="ops-record-summary">
            <span>DURABLE RECORD</span>
            <strong class="${recordReplayOk&&sqliteQuickOk?'ok':'warning'}">${recordReplayOk&&sqliteQuickOk?'REPLAY + SQLITE OK':'CHECK EVIDENCE'}</strong>
            <small>local integrity evidence · not authorship or external notarization</small>
          </div>
          <div class="ops-record-track" role="group" aria-label="Recent WAKE generation events">${recordSpine||'<span class="empty">No recent generation events.</span>'}</div>
          <div class="ops-record-meta">
            <span>REV <b>${recordIntegrity?.sudofx_revision??'—'}</b></span>
            <span>EVENTS <b>${recordIntegrity?.sudofx_event_count??'—'}</b></span>
            <span>REPLAY <b>${recordIntegrity?.replay_ms??'—'} ms</b></span>
            <span>DB <b>${databaseMB===null?'—':databaseMB.toFixed(1)+' MB'}</b></span>
            <span>FREE <b>${freePct===null?'—':freePct.toFixed(1)+'%'}</b></span>
          </div>
        </div>
        <div class="ops-console-grid" id="ops-field">
          <article class="ops-viewport">
            <div class="ops-grid-lines" aria-hidden="true"></div>
            <div class="ops-topic-field">${topicNodes||'<span class="empty">No topic activity yet.</span>'}<div class="ops-field-core"><strong>${s.version}</strong><span>WAKE CYCLE</span><small>${topicActive}/${configuredTopicCount} active topics</small></div></div>
            <div class="ops-viewport-caption"><span>ACCEPTED RESEARCH ACTIVITY · NODE SIZE = ACCEPTED ACTION COUNT</span><b>${topicAttributedTotal} topic-attributed actions</b></div>
          </article>
          <aside class="ops-inspector">
            <div class="ops-readout"><span>LAST ATTEMPT</span><strong>${esc(latestAttemptStatus.toUpperCase())}</strong><small>${esc(latestModel)}</small></div>
            <div class="ops-readout"><span>REQUESTS TODAY</span><strong>${wakeStatus.provider_requests_today??0}</strong><small>limit ${wakeStatus.daily_call_limit??'—'}</small></div>
            <div class="ops-readout"><span>OPEN WORK</span><strong>${openObligations}</strong><small>${overdue} overdue</small></div>
            <div class="ops-readout"><span>PROVIDER FALLBACK</span><strong>${fallbackWakes}</strong><small>${fallbackRate.toFixed(1)}% of completed wakes</small></div>
          </aside>
        </div>
        <div class="ops-pulse-ribbon" aria-label="Recent wake pulse">
          <div class="ops-pulse-copy"><span>RECENT WAKE PULSE</span><strong>LAST ${attempts.length}</strong><small>one cell per completed wake · tap for receipt</small></div>
          <div class="ops-pulse-cells" role="group" aria-label="Recent completed wake outcomes">${timeline||'<span class="empty">No completed wakes yet.</span>'}</div>
          <div class="ops-pulse-legend">${statuses.map(([name,value])=>`<span class="${esc(name)}"><i></i><b>${value}</b>${esc(name)}</span>`).join('')}</div>
        </div>
        <div class="ops-secondary-grid" id="ops-pressure">
        <div class="ops-provider-trace" aria-label="Recent provider attempt trace">
          <div class="ops-provider-head"><div><span>PROVIDER ATTEMPT TRACE</span><strong>LAST ${providerTraceSource.length} KNOWN ATTEMPTS</strong></div><small>height = latency · color = recorded outcome</small></div>
          <div class="ops-provider-track" role="group" aria-label="Recent provider attempt outcomes">${providerTrace||'<span class="empty">No known provider attempts yet.</span>'}</div>
          <div class="ops-provider-meta"><span>median ${medianLatency===null?'—':medianLatency+' ms'}</span><span>${providerSuccesses} success-labelled</span><span>${fallbackWakes} fallback wakes</span></div>
        </div>
        <div class="ops-pressure-board" aria-label="Operational pressure">
          <section>
            <header><span>GOVERNANCE PRESSURE</span><strong>${sortedReasons.length} rejection families</strong></header>
            <div class="ops-pressure-list">${pressureBars}</div>
          </section>
          <section class="ops-quota">
            <header><span>PROVIDER QUOTA PRESSURE</span><strong>${Number.isFinite(dailyLimit)?requestSlots+'/'+dailyLimit:'limit unavailable'}</strong></header>
            <div class="ops-quota-gauge" aria-label="Provider quota usage ${quotaPct.toFixed(0)} percent"><i style="width:${quotaPct}%"></i></div>
            <div class="ops-quota-meta"><span>${wakeStatus.attempts_today??0} charged attempts</span><span>${wakeStatus.provider_requests_today??0} HTTP requests</span><span>${wakeStatus.provider_request_counts_incomplete?'counts incomplete':'counts complete'}</span></div>
          </section>
        </div>
        <div class="ops-time" aria-label="Time Dilation telemetry">
          <div class="ops-time-head">
            <div><p class="eyebrow">TIME DILATION / EXPERIMENTAL REGIME</p><h3>${timeControl?esc(String(timeControl.mode||'real').toUpperCase()):'NOT INITIALIZED'}</h3></div>
            <div class="ops-time-scale"><strong>${timeControl?Number(timeControl.mode==='frozen'?0:timeControl.mode==='scaled'?timeControl.scale||1:1).toFixed(timeControl.mode==='scaled'?1:0):'—'}×</strong><span>EFFECTIVE SCALE</span></div>
          </div>
          <div class="ops-time-grid">
            <div><span>WALL / LAST INTERVAL</span><strong>${formatDuration(latestTemporal?.wall_elapsed_seconds)}</strong><small>raw UTC elapsed time</small></div>
            <div><span>EFFECTIVE / LAST INTERVAL</span><strong>${formatDuration(latestTemporal?.effective_elapsed_seconds)}</strong><small>under active mapping</small></div>
            <div><span>EFFECTIVE / TOTAL</span><strong>${formatDuration(latestTemporal?.effective_seconds_total??temporalState?.effective_seconds)}</strong><small>durable accumulated experimental time</small></div>
            <div><span>CYCLE DISTANCE</span><strong>${latestTemporal?.cycle_distance??'—'}</strong><small>accepted-cycle distance in last receipt</small></div>
            <div><span>INTERVENING EVENTS</span><strong>${latestTemporal?.intervening_events?.total??'—'}</strong><small>between temporal anchors</small></div>
            <div><span>REGIME</span><strong>${esc(String(latestTemporal?.regime_id||experimental?.id||'—').replace(/^reg-/,''))}</strong><small>${timeControl?.enabled===false?'disabled':timeControl?'operator-recorded':'unavailable'}</small></div>
          </div>
          <div class="ops-time-trace">
            <div class="ops-time-trace-head"><span>TEMPORAL RECEIPTS / LAST ${temporalTraceSource.length}</span><small>height = wall interval · color = effective mapping · tap for receipt</small></div>
            <div class="ops-time-track" role="group" aria-label="Recent temporal receipts">${temporalTrace||'<span class="empty">No temporal receipts yet.</span>'}</div>
            <div class="ops-time-legend"><span class="real"><i></i>real</span><span class="scaled"><i></i>scaled</span><span class="frozen"><i></i>frozen</span></div>
          </div>
        </div>
        </div>
        <div class="ops-signal-band" aria-label="Derived operating signals">
          <div class="ops-signal" style="--signal:${acceptanceRate}%"><span>ACCEPTANCE</span><strong>${acceptanceRate}%</strong><i></i></div>
          <div class="ops-signal danger" style="--signal:${Math.min(100,rejectionRate)}%"><span>GOVERNANCE PRESSURE</span><strong>${rejectionRate.toFixed(1)}%</strong><i></i></div>
          <div class="ops-signal" style="--signal:${Math.min(100,handoffRate)}%"><span>HANDOFF CONTINUITY</span><strong>${handoffRate}%</strong><i></i></div>
          <div class="ops-signal warning" style="--signal:${Math.min(100,fallbackRate)}%"><span>FALLBACK LOAD</span><strong>${fallbackRate.toFixed(1)}%</strong><i></i></div>
          <div class="ops-signal info" style="--signal:${Math.min(100,configuredTopicCount?100*topicActive/configuredTopicCount:0)}%"><span>TOPIC COVERAGE</span><strong>${topicActive}/${configuredTopicCount}</strong><i></i></div>
          <div class="ops-signal info" style="--signal:${Math.min(100,matrixPct)}%"><span>MATRIX COVERAGE</span><strong>${matrixPct}%</strong><i></i></div>
        </div>
        <div class="ops-tertiary-grid">
        <div class="ops-context" id="ops-context" aria-label="Context delivery telemetry">
          <div class="ops-context-head">
            <div><p class="eyebrow">CONTEXT DELIVERY / RECOVERABLE COMPRESSION</p><h3>${contextDelivery?esc(String(contextDelivery.mode||'rich').toUpperCase()):'NO RECEIPT'}</h3></div>
            <div class="ops-context-ratio"><strong>${contextDelivery&&Number.isFinite(Number(contextDelivery.request_compression_ratio))?(100*Number(contextDelivery.request_compression_ratio)).toFixed(1)+'%':'—'}</strong><span>REQUEST COMPRESSION</span></div>
          </div>
          <div class="ops-context-grid">
            <div><span>RICH REQUEST</span><strong>${contextDelivery?Number(contextDelivery.rich_context_chars||0).toLocaleString():'—'}</strong><small>characters before delivery fallback</small></div>
            <div><span>DELIVERED REQUEST</span><strong>${contextDelivery?Number(contextDelivery.delivered_request_chars||0).toLocaleString():'—'}</strong><small>characters crossing model boundary</small></div>
            <div><span>OMITTED CATEGORIES</span><strong>${Array.isArray(contextDelivery?.omitted_categories)?contextDelivery.omitted_categories.length:'—'}</strong><small>explicitly receipt-tracked omissions</small></div>
            <div><span>REHYDRATED EVIDENCE</span><strong>${Number.isFinite(Number(contextMetrics.retrieval_rehydrated_evidence_count))?Number(contextMetrics.retrieval_rehydrated_evidence_count):'—'}</strong><small>exact evidence restored from retrieval plan</small></div>
            <div><span>RETRIEVAL EVIDENCE</span><strong>${Number.isFinite(Number(contextMetrics.retrieval_evidence_count))?Number(contextMetrics.retrieval_evidence_count):'—'}</strong><small>evidence roots selected for recovery</small></div>
            <div><span>TRUST ROOTS</span><strong>${Number.isFinite(Number(contextMetrics.trust_compact_evidence_root_count))?Number(contextMetrics.trust_compact_evidence_root_count):'—'}</strong><small>receipt-side compact provenance roots</small></div>
          </div>
          <div class="ops-context-trace">
            <div class="ops-context-trace-head"><span>CONTEXT PRESSURE / LAST ${contextTraceSource.length}</span><small>height = rich request · inner fill = delivered share · orange = bounded mode</small></div>
            <div class="ops-context-track" role="group" aria-label="Recent context delivery receipts">${contextTrace||'<span class="empty">No context receipts yet.</span>'}</div>
          </div>
        </div>
        <div class="ops-provenance" id="ops-evidence" aria-label="Evidence provenance telemetry">
          <div class="ops-provenance-head">
            <div><p class="eyebrow">EVIDENCE PROVENANCE / COLLECTION DEPTH</p><h3>${qualifyingEvidence} substantive source observations</h3></div>
            <small>provenance labels describe retrieval depth; they are not truth scores</small>
          </div>
          <div class="ops-provenance-grid">
            <div class="ops-provenance-kpis">
              <div><span>ALL EVIDENCE</span><strong>${evidenceCount}</strong><small>current evidence records</small></div>
              <div><span>QUALIFYING SOURCES</span><strong>${qualifyingEvidence}</strong><small>source role excluding metadata-only tiers</small></div>
              <div><span>DISCOVERY LEADS</span><strong>${discoveryEvidence}</strong><small>routing material, not substantive evidence</small></div>
              <div><span>METADATA ROUTES</span><strong>${metadataEvidence}</strong><small>bibliographic routing receipts</small></div>
            </div>
            <div class="ops-provenance-tiers"><header><span>HOST / RETRIEVAL TIERS</span><strong>${evidenceTierRows.length} observed classes</strong></header><div>${evidenceTierBars}</div></div>
          </div>
        </div>
        <div class="ops-beliefs" id="ops-beliefs" aria-label="Governed belief telemetry">
          <div class="ops-beliefs-head">
            <div><p class="eyebrow">EPISTEMIC FIELD / GOVERNED BELIEF STATE</p><h3>${opsActiveBeliefs.length} active · ${opsRetractedBeliefs.length} retracted</h3></div>
            <small>confidence is recorded model state, not an empirical probability of truth</small>
          </div>
          <div class="ops-beliefs-grid">
            <div class="ops-belief-kpis">
              <div><span>ACTIVE</span><strong>${opsActiveBeliefs.length}</strong><small>currently carried beliefs</small></div>
              <div><span>RETRACTED</span><strong>${opsRetractedBeliefs.length}</strong><small>kept visible in history</small></div>
              <div><span>MEDIAN CONFIDENCE</span><strong>${medianConfidence===null?'—':medianConfidence.toFixed(2)}</strong><small>active beliefs only</small></div>
              <div><span>FALSIFIERS</span><strong>${falsifierCount}/${opsActiveBeliefs.length}</strong><small>active beliefs with explicit reopen condition</small></div>
              <div><span>EVIDENCE ROOTS</span><strong>${beliefEvidenceRoots}</strong><small>citations carried by active beliefs</small></div>
            </div>
            <div class="ops-belief-distribution"><header><span>ACTIVE CONFIDENCE DISTRIBUTION</span><strong>${activeConfidences.length} measured</strong></header><div>${confidenceBars}</div></div>
          </div>
        </div>
        <div class="ops-lifecycle" aria-label="Application lifecycle observability">
          <div class="ops-lifecycle-head"><p class="eyebrow">APPLICATION LIFECYCLE / GENERIC SUDOFX EVIDENCE</p><span>${appObservability?`record revision ${esc(appObservability.record_revision)}`:`not available`}</span></div>
          <div class="ops-lifecycle-grid">
            <div><span>GOVERNED ACTIONS</span><strong>${Number(appActions.accepted||0)}</strong><small>${Number(appActions.rejected||0)} rejected</small></div>
            <div><span>INVOCATIONS</span><strong>${Number(appInvocations.total||0)}</strong><small>${Number(appInvocations.attempts||0)} provider attempts</small></div>
            <div><span>COMPLETED</span><strong>${Number(appInvocations.completed||0)}</strong><small>${Number(appInvocations.failed||0)} failed</small></div>
            <div><span>QUOTA</span><strong>${Number(appInvocations.quota_exhausted||0)}</strong><small>exhaustion outcomes</small></div>
            <div><span>TEMPORARY</span><strong>${Number(appInvocations.temporary_failures||0)}</strong><small>provider waits</small></div>
            <div><span>EFFECT BARRIER</span><strong>${Number(appInvocations.effect_barrier_failures||0)}</strong><small>blocked before effect</small></div>
          </div>
          <div class="ops-trace">
            <div class="ops-trace-head"><span>RECENT INVOCATION TRACE</span><small>bounded sudofx lifecycle receipts · newest at bottom</small></div>
            <div class="ops-trace-list">${lifecycleTraces}</div>
          </div>
        </div>
        </div>
        <div class="ops-horizon" id="ops-horizon" aria-label="Open commitment horizon">
          <div class="ops-horizon-head"><div><p class="eyebrow">OPEN COMMITMENT HORIZON</p><h3>${openObligations} obligations carried forward</h3></div><small>bucketed by due cycle relative to cycle ${s.version}</small></div>
          <div class="ops-horizon-grid">${obligationHorizon}</div>
        </div>
        <div class="ops-drive" id="ops-drive" aria-label="Inquiry drive shadow telemetry">
          <div class="ops-drive-head">
            <div><p class="eyebrow">INQUIRY-DRIVE SHADOW / WHAT WORK WOULD PERSIST?</p><h3>${opsDriveStatus}</h3></div>
            <div class="ops-drive-gate"><strong>${opsDriveGate?Number(opsDriveGate.completed_scored_cycles||0):0}</strong><span>/ ${opsDriveGate?Number(opsDriveGate.minimum_completed_scored_cycles||0):0} SCORED CYCLES</span><small>deterministic observation · no decision authority</small></div>
          </div>
          <div class="ops-drive-grid">
            <div class="ops-drive-ranking">${opsDriveRows}</div>
            <div class="ops-drive-history">
              <header><span>LEADING PROJECT SCORE / LAST ${opsDriveTraceSource.length}</span><strong>${opsDriveProjects.length} ranked now</strong></header>
              <div class="ops-drive-track" role="group" aria-label="Recent inquiry-drive shadow scores">${opsDriveTrace||'<span class="empty">No inquiry-drive receipts yet.</span>'}</div>
              <p>C continuity · N novelty · H coherence · G generativity · S self-correction</p>
            </div>
          </div>
        </div>
        <div class="ops-trajectory" id="ops-trajectory" aria-label="Research project trajectories">
          <div class="ops-trajectory-head">
            <div><p class="eyebrow">RESEARCH TRAJECTORY / FROM QUESTION TO PUBLICATION</p><h3>${projects.length} durable project paths</h3></div>
            <small>stages show recorded artifacts only · absence is visible, not inferred</small>
          </div>
          <div class="ops-trajectory-list">${opsProjectTrajectories}</div>
        </div>
        <div class="ops-matrix-block" id="ops-matrix">
          <div class="ops-matrix-copy"><p class="eyebrow">CONTINUITY@1 / 7×7×7</p><h3>${matrixEnabled?'Coverage of the governed continuity space.':'Canonical continuity space · not yet enabled for this WAKE generation.'}</h3><p>${matrixEnabled?matrixCompleted+' of '+matrixTotal+' coordinates completed · next '+(matrixProgress.next_ordinal?'#'+matrixProgress.next_ordinal:'complete'):'343 deterministic coordinates are visible as definition geometry only.'}</p><small>Seven semantic planes. Within each plane, columns follow pressure order and rows follow exposure order from the shared continuity@1 definition.</small></div>
          <div class="continuity-matrix-view" aria-label="Continuity matrix coverage: ${matrixCompleted} of ${matrixTotal} coordinates completed">
            <div class="matrix-axis-note"><span>columns / pressure: ${esc(pressureAxis.map(v=>v.label).join(' · '))}</span><span>rows / exposure: ${esc(exposureAxis.map(v=>v.label).join(' · '))}</span></div>
            <div class="matrix-plane-stack">${matrixPlanes}</div>
          </div>
          <div class="ops-matrix-stat"><strong>${matrixPct}%</strong><span>covered</span><small>${matrixFailed} failed · ${matrixDeferred} deferred</small></div>
        </div>
      </section>
      <section class="metrics-row-one">
        <section class="dashboard-grid">
        <article class="dashboard-panel panel-action-matrix"><div class="panel-heading"><div><p class="eyebrow">ACCEPTED ACTION MATRIX</p><h2>Where accepted work goes — and what kind it is.</h2></div><div class="landscape-status"><span>ACCEPTED ACTIONS</span><strong>${actionTotal}</strong></div></div><p class="small">One population, two dimensions: rows are configured research topics; columns are accepted action types. Row totals and column totals reconcile to the same accepted-action record. Actions without a durable topic stay separate below the research matrix.</p><div class="action-matrix-desktop"><div class="action-matrix-scroll"><div class="action-matrix" style="--action-cols:${Math.max(1,actionTypes.length)}"><div class="matrix-header"><button type="button" class="matrix-sort" data-matrix-sort-index="0" data-matrix-sort-label="topic" aria-label="Sort by topic">TOPIC<span aria-hidden="true">↕</span></button>${matrixHeader}<button type="button" class="matrix-sort is-sorted" data-matrix-sort-index="${actionTypes.length+1}" data-matrix-sort-label="total" data-matrix-sort-direction="desc" aria-label="Sort by total, currently descending">TOTAL<span aria-hidden="true">↓</span></button></div>${matrixRows||'<p class="empty">No topic-attributed accepted actions yet.</p>'}${systemMatrix}<div class="matrix-total-row"><span>ALL ACCEPTED</span>${matrixTotals}<strong>${actionTotal}</strong></div></div></div><p class="small matrix-note">${topicAttributedTotal} topic-attributed · ${systemActions.total} unattributed/system · ${actionTotal} total accepted actions.</p></div><div class="action-matrix-mobile">${mobileMatrix||'<p class="empty">No accepted actions yet.</p>'}<p class="small matrix-note">${topicAttributedTotal} topic-attributed · ${systemActions.total} unattributed/system · ${actionTotal} total.</p></div></article>
        <article class="dashboard-panel panel-correctability"><p class="eyebrow">EXPERIMENT / OUTCOME COMPOSITION</p><h2>What happened to completed wakes?</h2>${outcomePieHtml}<p class="metric-definition">Population: all completed wakes in the published durable record. Outcome is governance state, not research quality.</p><div class="metric-bars">${outcomeBars}</div><h3>Most common rejection families</h3><div class="reason-list">${reasons}</div><a class="text-link" href="#history/filter:rejected">Inspect rejected work →</a></article>
        <article class="dashboard-panel panel-continuity"><p class="eyebrow">EXPERIMENT / CONTINUITY</p><h2>Does work cross fresh sessions?</h2><div class="dashboard-stat"><strong>${inheritedFulfilled.length}</strong><span>obligations fulfilled by a later invocation</span></div><div class="dashboard-stat"><strong>${obligations.filter(c=>c.status==='open').length}</strong><span>open obligations still carried forward</span></div><div class="dashboard-stat"><strong>${recoveredCount}</strong><span>recovered calls with durable state retained</span></div><div class="dashboard-stat"><strong>${overdue}</strong><span>open obligations at or past due cycle</span></div></article>
        <article class="dashboard-panel panel-yield"><p class="eyebrow">EXPERIMENT / RESEARCH YIELD</p><h2>What survives as usable work?</h2><div class="dashboard-stat"><strong>${evidenceCount}</strong><span>evidence records</span></div><div class="dashboard-stat"><strong>${projects.length}</strong><span>research projects</span></div><div class="dashboard-stat"><strong>${notebooks.length}</strong><span>notebooks</span></div><div class="dashboard-stat"><strong>${Object.keys(s.posts||{}).length}</strong><span>published posts</span></div></article>
        <article class="dashboard-panel panel-provider"><p class="eyebrow">APPARATUS / PROVIDER PRESSURE</p><h2>What it costs to get a wake.</h2><div class="dashboard-stat"><strong>${providerRequests}</strong><span>recorded HTTP requests</span></div><div class="dashboard-stat"><strong>${fallbackWakes}</strong><span>wakes using provider fallback</span></div><div class="dashboard-stat"><strong>${deferredCount}</strong><span>deferred wakes</span></div><div class="model-metrics">${modelRows||'<p class="empty">No provider data yet.</p>'}</div></article>
      <article class="dashboard-panel panel-topic-shape"><p class="eyebrow">EXPERIMENT / RESEARCH ATTENTION</p><h2>Where accepted work is accumulating.</h2><div class="topic-bar-chart">${topicBars||'<p class="empty">No topic-attributed actions yet.</p>'}</div><p class="metric-definition">Counts are accepted proposal actions attributed to configured topics; they measure attention, not importance or expertise.</p></article></section>
        <article class="dashboard-panel dashboard-hypothesis-summary"><p class="eyebrow">OBSERVATION → HYPOTHESIS</p><h2>From patterns to possibilities.</h2><div class="dashboard-stat"><strong>${hypotheses.length}</strong><span>active hypotheses</span></div><p class="small">Generated only from recorded counts and comparisons. Prompts for investigation, not conclusions.</p></article>
      </section>
        <section class="hypothesis-section"><div class="dashboard-heading"><div><p class="eyebrow">OBSERVATION → HYPOTHESIS</p><h2>Patterns worth testing next.</h2></div><p>Generated only from recorded counts and comparisons.</p></div><div class="hypothesis-grid">${hypothesisHtml}</div></section>
      </section>
      <section class="metrics-row-two">
        <div class="metrics-row-two-left"><article class="dashboard-section dashboard-feature"><div class="dashboard-heading"><div><p class="eyebrow">OUTCOME TREND / 10-WAKE WINDOWS</p><h2>Are the conditions changing?</h2></div><p>Each column is a consecutive ten-wake window. Height is share of outcomes.</p></div><div class="trend-chart">${trend||'<span class="empty">No completed wakes yet.</span>'}</div></article><article class="dashboard-section dashboard-feature"><div class="dashboard-heading"><div><p class="eyebrow">LAST ${attempts.length} COMPLETED WAKES</p><h2>The pulse of the experiment.</h2></div><p>One cell per wake. Color is outcome—not quality. Tap any cell for its receipt.</p></div><div class="wake-timeline" role="group" aria-label="Recent wake outcomes">${timeline||'<span class="empty">No completed wakes yet.</span>'}</div><div class="timeline-legend">${statuses.map(([name])=>`<span><i class="${name}"></i>${name}</span>`).join('')}</div></article></div>
        <div class="metrics-row-two-right"><section class="command-strip"><div><p class="eyebrow">LIVE RECORD TELEMETRY</p><strong>CYCLE ${s.version}</strong></div><div><span>COMPLETED</span><b>${completed.length}</b></div><div class="status-accepted"><span>ACCEPTED</span><b>${acceptedCount}</b></div><div class="status-rejected"><span>REJECTED</span><b>${rejectedCount}</b></div><div class="status-deferred"><span>DEFERRED</span><b>${deferredCount}</b></div><div class="status-fallback"><span>FALLBACK</span><b>${fallbackWakes}</b></div><div><span>OPEN WORK</span><b>${openObligations}</b></div><div><span>TOPICS ACTIVE</span><b>${topicActive}/${configuredTopicCount}</b></div></section>
<section class="telemetry-grid">${telemetryHtml}</section>
<section class="dashboard-kpis">${card(s.version,'Durable cycles','Accepted state advances')}${card(acceptanceRate+'%','Acceptance rate',acceptedCount+' of '+completed.length+' completed wakes')}${card(handoffRate+'%','Obligation handoff',inheritedFulfilled.length+' cross-invocation fulfillments')}${card(requestsPerAccepted,'Requests / accepted','Recorded HTTP attempts ÷ accepted wakes')}${card(fallbackWakes,'Fallback wakes','More than one provider attempt')}${card(medianLatency===null?'—':medianLatency+'ms','Median provider latency','Known completed model attempts')}${card(revisedBeliefs,'Belief actions',activeBeliefs.length+' active · '+retractedBeliefs.length+' retracted')}${card(overdue,'Overdue obligations','Open commitments at or past due cycle')}${card(sqliteSize,'SQLite database','Durable record file size')}${card(eventRecordCount,'Durable events','Append-only event rows')}</section></div>
      </section>
      <p class="dashboard-footnote">Derived view only. The durable state and event log remain authoritative. Derived action counts and hypotheses are explicitly descriptive; they never write back to the record.</p>`;

    const matrix=$('metrics-dashboard').querySelector('.action-matrix');
    if(matrix){
      const sortButtons=[...matrix.querySelectorAll('.matrix-sort')];
      const rows=[...matrix.querySelectorAll('.matrix-row')];
      const anchor=matrix.querySelector('.matrix-system-row,.matrix-total-row');
      const setSortState=(active,direction)=>{
        sortButtons.forEach(button=>{
          const indicator=button.querySelector('span');
          const isActive=button===active;
          button.classList.toggle('is-sorted',isActive);
          button.dataset.matrixSortDirection=isActive?direction:'';
          button.setAttribute('aria-label',isActive
            ? `Sort by ${button.dataset.matrixSortLabel}, currently ${direction==='asc'?'ascending':'descending'}`
            : `Sort by ${button.dataset.matrixSortLabel}`);
          if(indicator)indicator.textContent=isActive?(direction==='asc'?'↑':'↓'):'↕';
        });
      };
      sortButtons.forEach(button=>button.addEventListener('click',()=>{
        const index=Number(button.dataset.matrixSortIndex);
        const prior=button.dataset.matrixSortDirection;
        const direction=prior==='desc'?'asc':prior==='asc'?'desc':(index===0?'asc':'desc');
        const multiplier=direction==='asc'?1:-1;
        rows.sort((a,b)=>{
          if(index===0){
            return multiplier*a.children[0].textContent.trim().localeCompare(b.children[0].textContent.trim(),undefined,{sensitivity:'base'});
          }
          const av=Number(a.children[index]?.textContent.trim()||0);
          const bv=Number(b.children[index]?.textContent.trim()||0);
          return multiplier*(av-bv)||a.children[0].textContent.trim().localeCompare(b.children[0].textContent.trim(),undefined,{sensitivity:'base'});
        });
        rows.forEach(row=>matrix.insertBefore(row,anchor));
        setSortState(button,direction);
      }));
    }
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
    $('lab-content').innerHTML=`<div class="panel"><p class="eyebrow">THE DURABLE OBJECTIVE ${help('durable_objective')}</p><h2>${esc(s.objective)}</h2><p>Current focus: <strong>${esc(s.focus)}</strong></p><div class="flow"><span>Durable state</span>→<span>Fresh invocation</span>→<span>Untrusted proposal</span>→<span>Mechanical rules</span>→<span>Atomic event</span></div><p>Models may review beliefs, create obligations, and propose evidence-backed completion. External actions and rule changes are outside their authority.</p></div>${drivePanel}<div class="lab-grid"><div class="panel"><p class="eyebrow">REPEATABLE HARNESS EXPERIMENT ${help('repeatable_harness')}</p><h2>The test, not the hype.</h2>${coverage}<p>${exp?`Executed ${esc(exp.generated)}. ${exp.cycles} accepted cycles, ${exp.fresh_processes} fresh wake processes. <a href="experiment.json">Download results →</a>`:'Run the offline experiment to populate this checklist.'}</p><p>These results exercise deterministic simulated providers. They do not establish real-model comprehension or general intelligence. Live Gemini accepted cycles here: <strong>${live}</strong>. Human-pasted replies have human-attested model identity.</p></div><div class="panel"><p class="eyebrow">LAST ${Math.min(accepted.length,100)} ACCEPTED CYCLES ${help('accepted_cycles')}</p><h2>Small steps. Long record.</h2><div class="spark" role="group" aria-label="Number of accepted changes per cycle">${bars}</div><div class="chart-labels"><span>OLDER →</span><span>ACCEPTED CHANGES / CYCLE</span><span>NOW</span></div><h3>What the system enforces</h3><p>Atomic proposals. Existing evidence references. New evidence for belief reviews. Persistent obligations. No model cancellation. An auditable decision for each completed invocation.</p><h3>What still needs judgment</h3><p>Whether evidence is true, whether it supports a claim, and whether an obligation was meaningfully fulfilled. Hashes detect edits relative to the recorded head; they do not stop an administrator rewriting the entire history.</p><p>Verified export head:<br><code>${esc(data.head)}</code></p></div></div>${modelPerformance()}<div class="panel"><p class="eyebrow">CURRENT BELIEFS ${help('beliefs')}</p><h2>Allowed to change our minds.</h2>${Object.values(s.beliefs).sort((a,b)=>b.confidence-a.confidence||String(a.id).localeCompare(String(b.id))).map(b=>`<div class="data-card"><div class="entry-meta">${badge(b.status==='active'?'accepted':'rejected',b.status)}<span>${Math.round(b.confidence*100)}% CONFIDENCE</span><span>${esc(b.id)}</span></div><p>${esc(b.statement)}</p><p>${esc(b.reason)}</p>${b.falsifier?'<p><strong>What would change this:</strong> '+esc(b.falsifier)+'</p>':''}${refs(b.evidence)}<details><summary>Full belief record</summary>${raw(b)}</details></div>`).join('')||'<p>No beliefs recorded yet.</p>'}</div><div class="panel"><p class="eyebrow">COMMITMENT REGISTER ${help('commitments')}</p><h2>Still on the hook.</h2>${committed.map(c=>`<details class="data-card"><summary>${esc(c.id)} · ${esc(c.status)} · due cycle ${c.due_cycle}${c.status==='open'&&s.version>=c.due_cycle?' · OVERDUE':''}</summary><p>${esc(c.task)}</p><p>${esc(c.resolution_reason||c.reason)}</p>${refs(c.evidence)}${raw(c)}</details>`).join('')||'<p>No commitments yet.</p>'}</div>`;
  }
  function blog(selected='') {
    if(selected.startsWith('topic:')){
      const topic=decodeURIComponent(selected.slice(6));
      const filtered=posts.filter(post=>postTopic(post)===topic);
      $('blog-content').innerHTML='<p class="topic-filter-note">Showing <strong>'+esc(topic==='reflection'?'reflection':topicLabel(topic).toLowerCase())+'</strong> · <a href="#blog">show all</a></p>'+(filtered.length?'<div class="blog-grid">'+filtered.map(post=>{const invocation=s.invocations[post.created_by];const reflection=postTopic(post)==='reflection';return '<article class="blog-card record-panel'+(reflection?' blog-card-reflection':'')+'"><div class="record-panel-head">'+postMeta(post,invocation)+'<h2><a href="#blog/'+encodeURIComponent(post.id)+'">'+esc(postTitle(post))+'</a></h2></div><div class="record-panel-body"><p>'+esc(post.lede)+'</p>'+(post.lens?'<blockquote>'+esc(post.lens)+'</blockquote>':'')+'<a class="text-link" href="#blog/'+encodeURIComponent(post.id)+'">Read Bob’s note →</a></div></article>';}).join('')+'</div>':'<p class="empty">No posts match this topic.</p>');
      return;
    }
    if(selected){
      const post=posts.find(item=>item.id===selected);
      if(!post){$('blog-content').innerHTML='<p class="empty">That post is not in this record.</p>';return;}
      const invocation=s.invocations[post.created_by];
      const body=String(post.body).split(/\n\s*\n/).map(part=>'<p>'+blogText(part,post)+'</p>').join('');
      const notebooks=(post.notebooks||[]).map(id=>s.notebooks?.[id]?'<a class="text-link" href="#projects/notebook:'+encodeURIComponent(id)+'">'+esc(s.notebooks[id].title)+' →</a>':'').join('');
      const sources=(post.evidence||[]).map(id=>'<a href="#evidence/'+encodeURIComponent(id)+'">'+esc(id)+' →</a>').join(' ');
      const project=post.project?s.projects?.[post.project]:null;
      const projectReceipt=project?'<p>Related project: <a href="#projects/'+encodeURIComponent(post.project)+'">'+esc(project.title)+' →</a></p>':'<p>Scope: system-wide reflection.</p>';
      const correction=post.status==='superseded'?'<div class="research-note">A later post corrected or superseded this one. <a href="#blog/'+encodeURIComponent(post.superseded_by)+'">Read the follow-up →</a></div>':post.supersedes?'<div class="research-note">This note corrects an earlier post. <a href="#blog/'+encodeURIComponent(post.supersedes)+'">Read the original →</a></div>':'';
      $('blog-content').innerHTML='<article class="blog-reading'+(postTopic(post)==='reflection'?' blog-reading-reflection':'')+'"><a class="subtle" href="#blog">← All posts</a>'+postMeta(post,invocation)+'<h2>'+esc(postTitle(post))+'</h2><p class="blog-lede">'+esc(post.lede)+'</p>'+correction+body+(post.lens?'<blockquote><span>BOB’S LENS / PHILOSOPHICAL REFLECTION</span>'+esc(post.lens)+'</blockquote>':'')+'<div class="blog-receipts"><p class="eyebrow">FOLLOW THE RECEIPTS</p>'+projectReceipt+'<div>'+notebooks+'</div><p>'+sources+'</p><a class="subtle" href="#history/'+encodeURIComponent(post.created_by)+'">Exact wake and decision →</a> · <a class="subtle" href="blog/'+encodeURIComponent(post.id)+'.md">Markdown ↓</a></div><p class="blog-disclosure">Bob is WAKE✳︎’s human-facing translation layer, not its mind or identity. This AI-authored note compresses the durable research record for conversation; research claims link back to evidence and philosophical reflections remain reflections.</p></article>';
      return;
    }
    $('blog-content').innerHTML=posts.length?'<div class="blog-grid">'+posts.map(post=>{const invocation=s.invocations[post.created_by];const reflection=postTopic(post)==='reflection';return '<article class="blog-card record-panel'+(reflection?' blog-card-reflection':'')+'"><div class="record-panel-head">'+postMeta(post,invocation)+'<h2><a href="#blog/'+encodeURIComponent(post.id)+'">'+esc(postTitle(post))+'</a></h2></div><div class="record-panel-body"><p>'+esc(post.lede)+'</p>'+(post.lens?'<blockquote>'+esc(post.lens)+'</blockquote>':'')+'<a class="text-link" href="#blog/'+encodeURIComponent(post.id)+'">Read Bob’s note →</a></div></article>';}).join('')+'</div><p class="blog-disclosure">Bob is the public translation layer. Underneath, WAKE✳︎ is a sequence of fresh model calls working from a durable, auditable record—not a persistent person or experiencing self.</p>':'<div class="empty blog-empty"><strong>Bob has nothing worth posting yet.</strong><br>The journal still records every wake. The blog waits for something genuinely interesting.</div>';
  }
  function evidence(selected='') {
    const query=$('evidence-search').value.toLowerCase();
    const rows=Object.values(s.evidence).reverse().filter(e=>(!selected||e.id===selected)&&JSON.stringify(e).toLowerCase().includes(query));
    const valueText=value=>Array.isArray(value)?value.map(valueText).join(' · '):value&&typeof value==='object'?JSON.stringify(value):String(value??'');
    const readable=e=>{
      let content=e.content;
      if(typeof content==='string')try{content=JSON.parse(content)}catch{}
      if(!content||typeof content!=='object'||Array.isArray(content))return `<p class="evidence-plain">${esc(content)}</p>`;
      const priority=['scope','summary','statement','question','reason','process_id','invocation','base_version','previous_head','inherited_commitments'];
      const fields=Object.entries(content).filter(([key,value])=>key!=='excerpt'&&key!=='excerpt_truncated'&&value!==null&&value!==undefined&&value!=='').sort(([a],[b])=>{const ai=priority.indexOf(a),bi=priority.indexOf(b);return(ai<0?999:ai)-(bi<0?999:bi)||a.localeCompare(b)}).slice(0,10);
      const excerpt=content.excerpt?`<details class="evidence-excerpt"><summary>Excerpt${content.excerpt_truncated?' / TRUNCATED':''}</summary><p>${esc(valueText(content.excerpt))}</p></details>`:'';
      return `<dl class="evidence-summary">${fields.map(([key,value])=>`<div><dt>${esc(key.replaceAll('_',' '))}</dt><dd>${esc(valueText(value))}</dd></div>`).join('')}</dl>${excerpt}`;
    };
    $('evidence-content').innerHTML=(selected?'<p><a class="text-link" href="#evidence">← All evidence</a></p>':'')+rows.map(e=>`<article class="data-card evidence-card"><h3>${esc(e.id)}</h3><span class="source">${esc(e.source)} / ${esc(e.actor)} / ${esc(fmt(e.time))}</span>${readable(e)}<details><summary>Raw observation</summary>${raw(displayEvent(e))}</details></article>`).join('')+(rows.length?'':'<p class="empty">No observations match.</p>');
  }
  function history(selected='') {
    const query=$('history-search').value.toLowerCase(), filter=selected.startsWith('filter:')?selected.slice(7):'', kind=filter==='rejected'?'rejected':$('event-filter').value;
    if(filter==='rejected')$('event-filter').value='rejected';
    const inheritedIds=new Set(Object.values(s.commitments).filter(x=>x.status==='fulfilled'&&x.created_by!==x.resolved_by).flatMap(x=>[x.created_by,x.resolved_by]).filter(Boolean));
    const recoveredIds=new Set(invocations.filter(i=>i.status==='recovered').map(i=>i.id));
    const matchesFilter=e=>!filter||(filter==='rejected'?e.kind==='rejected':filter==='recovered'?recoveredIds.has(e.payload.id):filter==='inherited'?inheritedIds.has(e.payload.id):true);
    const exact=selected&&!filter?selected:'';
    const events=[...data.events].reverse().filter(e=>(!exact||e.payload.id===exact)&&matchesFilter(e)&&(kind==='all'||displayEventKind(e.kind)===kind)&&JSON.stringify(displayEvent(e)).toLowerCase().includes(query));
    $('history-content').innerHTML=((selected)?'<p><a class="text-link" href="#history">← All events</a></p>':'')+events.slice(0,historyLimit).map(e=>`<details class="audit-row"><summary><span>#${String(e.seq).padStart(4,'0')}</span>${badge(displayEventKind(e.kind))}<time datetime="${esc(e.time)}">${esc(fmt(e.time))}</time><span class="event-id">${esc(e.payload.id||'system')}</span></summary>${e.payload.reason?`<p>${esc(e.payload.reason)}</p>`:''}${(e.kind==='rejected'||e.payload.editorial)?`<p><a class="text-link" href="rejected.html#${encodeURIComponent(e.payload.id)}">Read the draft and explanation →</a></p>`:''}${raw(e)}</details>`).join('')+(events.length?'':'<p class="empty">No events match.</p>');
    $('history-more').hidden=events.length<=historyLimit;
  }
  function route() {
    const [part,id]=location.hash.slice(1).split('/');
    // Explore is the public entry point even before the record has a charter.
    // Journal remains a depth layer, never the default landing view.
    const page=['home','discoveries','topics','blog','projects','journal','lab','metrics','evidence','history','about'].includes(part)?part:'home';
    document.querySelectorAll('.view').forEach(el=>el.hidden=el.id!==page);
    document.body.classList.toggle('metrics-ops-active',page==='metrics');
    document.querySelectorAll('[data-nav]').forEach(el=>{if(el.dataset.nav===page||(el.dataset.navSection==='research'&&['projects','lab','metrics','evidence','history'].includes(page)))el.setAttribute('aria-current','page');else el.removeAttribute('aria-current');});
    let selected='';try{selected=decodeURIComponent(id||'');}catch{}
    if(page==='blog')blog(selected);
    if(page==='journal')journal();
    if(page==='lab')lab();
    if(page==='metrics')metricsDashboard();
    if(page==='evidence')evidence(selected);
    if(page==='history')history(selected);
    if(['home','discoveries','topics','projects'].includes(page))window.WakePet.render(page,selected);
    expandRecordDetails();
    emphasizeWake(document);
    document.title=`${WAKE_TEXT} / ${page==='home'?'Explore':page==='journal'?'Read':page[0].toUpperCase()+page.slice(1)}`;
  }
  $('evidence-search').addEventListener('input',route);
  $('history-search').addEventListener('input',()=>{historyLimit=35;route();});
  $('event-filter').addEventListener('change',()=>{historyLimit=35;route();});
  $('history-more').addEventListener('click',()=>{historyLimit+=35;route();});
  const resetPageScroll=()=>requestAnimationFrame(()=>requestAnimationFrame(()=>window.scrollTo(0,0)));
  document.addEventListener('click',event=>{
    const storyLink=event.target.closest('[data-story-target]');
    if(!storyLink)return;
    event.preventDefault();
    const target=document.getElementById(storyLink.dataset.storyTarget);
    if(target)target.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'});
  });
  window.addEventListener('hashchange',()=>{historyLimit=35;$('evidence-search').value='';$('history-search').value='';$('event-filter').value='all';route();resetPageScroll();});
  $('generated').textContent=`Live projection ${fmt(data.generated)}.`;

  window.WakeApplyLive = next => {
    if(!next || !next.state || next.authoritative === true) return;
    const nextState=next.state;
    for(const key of Object.keys(s)) delete s[key];
    Object.assign(s,nextState);
    data.events=Array.isArray(next.events)?next.events:[];
    data.head=next.head||data.head;
    data.source=next.source||data.source||{};
    data.generated=next.generated||data.generated;
    data.operation=next.operation||null;
    data.wake_status=next.wake_status||{};
    data.matrix_progress=next.matrix_progress||null;
    data.application_observability=next.application_observability||null;
    data.application_access=next.application_access||null;
    data.record_integrity=next.record_integrity||null;
    // Live telemetry evolves independently of the static Pages shell. Keep the
    // metrics block synchronized with the same projection as state/events so
    // newly published storage counters appear without a Pages redeploy.
    data.metrics=next.metrics||data.metrics||{};
    refreshDerived();
    renderMetricStrip();
    document.querySelectorAll('.cycle-count').forEach(node=>node.textContent=String(s.version??'—'));
    for(const provider of [...new Set(invocations.map(i=>i.provider).filter(Boolean))].sort()){
      if(![...providerSelect.options].some(option=>option.value===provider)){
        const option=document.createElement('option');option.value=provider;option.textContent=provider;providerSelect.append(option);
      }
    }
    for(const kind of [...new Set(data.events.map(event=>displayEventKind(event.kind)))].sort()){
      if(![...eventSelect.options].some(option=>option.value===kind)){
        const option=document.createElement('option');option.value=kind;option.textContent=kind;eventSelect.append(option);
      }
    }
    $('generated').textContent=`Live projection ${fmt(data.generated)}.`;
    journalLimit=8;historyLimit=35;
    route();
  };

  document.querySelectorAll('.cycle-count').forEach(node=>node.textContent=String(s.version??'—'));
  route();
})();
