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
  const topicTag=(id,page,label=topicLabel(id))=>`<a class="topic-tag" href="#${page}/topic:${encodeURIComponent(id)}" data-topic="${esc(id)}">[${esc(String(label).toLowerCase())}]</a>`;
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
    [s.version,'Recorded cycles',`${fixtures} simulated · ${live} live Gemini`],
    [inherited,'Obligations inherited','Across fresh invocations'],
    [rejected,'Proposals rejected','Read the drafts and recorded reasons'],
    [invocations.filter(i=>i.status==='recovered').length,'Calls recovered','Last valid state retained']
  ].map(([value,label,note])=>`<div class="metric"><strong>${value}</strong><span>${label}<small>${note}</small></span></div>`).join('');
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
    const query=$('history-search').value.toLowerCase(), kind=$('event-filter').value;
    const events=[...data.events].reverse().filter(e=>(!selected||e.payload.id===selected)&&(kind==='all'||e.kind===kind)&&JSON.stringify(e).toLowerCase().includes(query));
    $('history-content').innerHTML=(selected?'<p><a class="text-link" href="#history">← All events</a></p>':'')+events.slice(0,historyLimit).map(e=>`<details class="audit-row"><summary><span>#${String(e.seq).padStart(4,'0')}</span>${badge(e.kind)}<time datetime="${esc(e.time)}">${esc(fmt(e.time))}</time><span class="event-id">${esc(e.payload.id||'system')}</span></summary>${e.payload.reason?`<p>${esc(e.payload.reason)}</p>`:''}${(e.kind==='rejected'||e.payload.editorial)?`<p><a class="text-link" href="rejected.html#${encodeURIComponent(e.payload.id)}">Read the draft and explanation →</a></p>`:''}${raw(e)}</details>`).join('')+(events.length?'':'<p class="empty">No events match.</p>');
    $('history-more').hidden=events.length<=historyLimit;
  }
  function route() {
    const [part,id]=location.hash.slice(1).split('/');
    const page=['home','blog','projects','journal','lab','evidence','history','about'].includes(part)?part:(s.charter?'home':'journal');
    document.querySelectorAll('.view').forEach(el=>el.hidden=el.id!==page);
    document.querySelectorAll('[data-nav]').forEach(el=>{if(el.dataset.nav===page||(el.dataset.navSection==='research'&&['projects','lab','evidence','history'].includes(page)))el.setAttribute('aria-current','page');else el.removeAttribute('aria-current');});
    let selected='';try{selected=decodeURIComponent(id||'');}catch{}
    if(page==='blog')blog(selected);
    if(page==='journal')journal();
    if(page==='lab')lab();
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
