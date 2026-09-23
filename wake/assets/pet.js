/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Interface personality/experimental behavior kept separate from durable research mechanics. UI personality is not persistence or agency.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

(() => {
  'use strict';
  const d=JSON.parse(document.getElementById('wake-data').textContent),s=d.state;
  if(s.charter){document.querySelector('.footer-mark').href='#home';}
  const help=key=>window.WakeHelp.button(key);
  const blogNav=document.querySelector('[data-nav="blog"]');if(blogNav)blogNav.hidden=!Object.keys(s.posts||{}).length;
  const WAKE_TEXT='WAKE\u2733\uFE0E';
  const normalizeWake=v=>String(v??'').replaceAll('WAKE\u2733\uFE0F','WAKE\u2733').replaceAll('WAKE\u2733\uFE0E','WAKE\u2733').replaceAll('WAKE\u2733',WAKE_TEXT);
  const esc=v=>normalizeWake(v).replace(/[&<>"']/g,x=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
  const displayName=normalizeWake(s.pet_name||WAKE_TEXT);
  const names=Object.fromEntries((s.research_topics||[]).map(topic=>[topic.id,topic.label]));
  const topicColors=s.topic_colors||{};
  const topicName=id=>names[id]||String(id||'Unconfigured topic').replaceAll('_',' ');
  const topicTag=(id)=>`<a class="topic-tag" data-topic="${esc(id)}" style="--topic-color:${esc(topicColors[id]||'var(--cyan)')}" href="#projects/topic:${encodeURIComponent(id)}">${esc(topicName(id).toLowerCase())}</a>`;
  const projects=Object.values(s.projects||{}),books=Object.values(s.notebooks||{}).sort((a,b)=>b.updated_version-a.updated_version);
  const active=projects.filter(p=>p.status==='active');
  const invocations=Object.values(s.invocations),last=invocations.at(-1);
  const format=t=>new Date(t).toLocaleString('en-US',{timeZone:'America/Los_Angeles',month:'short',day:'numeric',hour:'numeric',minute:'2-digit',timeZoneName:'short'});
  const key='wake-visit-'+(d.events[0]?.hash||'new');
  let previous=null;try{previous=JSON.parse(localStorage.getItem(key));localStorage.setItem(key,JSON.stringify({cycle:s.version,time:Date.now()}));}catch{}
  const old=previous?.cycle??s.version;
  const progress=d.wake_status||{},attempt=progress.latest_attempt||last,accepted=progress.last_accepted;
  const paused=attempt&&attempt.status!=='accepted';
  const labels={accepted:'Accepted',deferred:'Deferred',rejected:'Rejected',failed:'Failed',pending:'In progress',recovered:'Interrupted'};
  const status=attempt?(labels[attempt.status]||attempt.status):'Waiting for the first wake';
  const diagnostics=attempt?.provider_error||{};
  const problem=attempt?.reason||'';
  const summarizeProblem=reason=>{
    if(diagnostics.category==='server')return `Gemini returned HTTP ${diagnostics.http_status}. The attempt was deferred after ${diagnostics.provider_requests_sent??diagnostics.attempts?.length??1} requests; the saved research is intact.`;
    if(diagnostics.category==='timeout')return 'Gemini timed out before this wake could complete. The saved research is intact.';
    if(diagnostics.category==='connection')return 'WAKE could not connect to Gemini. The saved research is intact.';
    if(/quota|daily call ceiling|HTTP 429/i.test(reason))return 'The API quota or daily attempt limit paused new research. The saved research is intact.';
    if(attempt?.status==='rejected')return 'The proposal did not pass validation. No research or blog changes from that attempt were accepted.';
    if(attempt?.status==='pending')return 'This attempt has not finished. Its request is saved.';
    if(/temporarily unavailable/i.test(reason))return 'Gemini could not complete this attempt after retries. This older receipt does not distinguish server errors, connection failures, and timeouts.';
    return reason||'The latest attempt did not finish. Its record is preserved.';
  };
  const explanation=summarizeProblem(problem);
  const nextEligible=progress.pending?'Waiting for the current attempt':progress.next_eligible?format(progress.next_eligible):'At the next scheduled check';
  const progressPanel=`<section class="wake-progress" aria-label="Research progress"><div><p class="eyebrow">LAST ACCEPTED WAKE</p><p>${accepted?`<a href="#history/${encodeURIComponent(accepted.id)}">${esc(format(accepted.finished||accepted.time))}</a>`:'None yet'}</p><span class="small">${s.version} accepted cycles</span></div><div><p class="eyebrow">LATEST ATTEMPT</p><p>${attempt?`<a href="#history/${encodeURIComponent(attempt.id)}">${esc(labels[attempt.status]||attempt.status)} · ${esc(format(attempt.time))}</a>`:'Not started'}</p>${attempt?.editorial?'<span class="small">Research accepted; proposed blog post withheld.</span>':''}</div><div><p class="eyebrow">NEXT ELIGIBLE RETRY</p><p>${esc(nextEligible)}</p><span class="small">Eligibility is not a promised start time. GitHub scheduling and provider availability determine when work resumes.</span></div></section>`;
  const paragraph=t=>String(t).split(/\n\s*\n/).map(p=>`<p>${esc(p).replace(/\n/g,'<br>')}</p>`).join('');
  const panelTime=item=>{const iid=item.updated_by||item.created_by,inv=iid&&s.invocations?.[iid];return inv?.time?format(inv.time):'';};
  function projectCard(p){const stamp=panelTime(p);return `<article class="project-card record-panel"><div class="record-panel-head"><div class="record-panel-meta project-meta"><span class="record-type">PROJECT</span><span class="record-status"><span class="badge ${esc(p.status)}">${esc(p.status.toUpperCase())}</span></span><span class="record-topics">${topicTag(p.domain)}</span>${stamp?`<time>${esc(stamp)}</time>`:''}</div><h3><a href="#projects/${encodeURIComponent(p.id)}">${esc(p.title)}</a></h3></div><div class="record-panel-body"><p>${esc(p.question)}</p><div class="next-step"><span>NEXT STEP</span>${esc(p.next_step)}</div><a class="text-link" href="#projects/${encodeURIComponent(p.id)}">Follow this question →</a></div></article>`;}
  function bookCard(n){const stamp=panelTime(n);return `<article class="notebook-card record-panel"><div class="record-panel-head"><div class="record-panel-meta notebook-meta"><span class="record-type">NOTEBOOK</span><span class="record-status"><span class="badge revision">REVISION ${n.revision}</span></span><span class="record-topics">${topicTag(n.domain)}</span>${stamp?`<time>${esc(stamp)}</time>`:''}</div><h3><a href="#projects/notebook:${encodeURIComponent(n.id)}">${esc(n.title)}</a></h3></div><div class="record-panel-body"><p>${esc(n.summary)}</p><a class="text-link" href="#projects/notebook:${encodeURIComponent(n.id)}">Read the notebook →</a></div></article>`;}
  function notebook(n){
    if(!n)return '<p class="empty">That notebook is not in this record.</p>';
    const sourceHtml=n.evidence.map(id=>{const e=s.evidence[id];let source={};try{source=JSON.parse(e.content);}catch{}return `<details class="data-card notebook-source"><summary>${esc(id)} / SOURCE RECEIPT</summary><div><a class="text-link" href="${esc(e.source)}" target="_blank" rel="noopener noreferrer">Open source →</a><p>${esc(source.scope||'Collected source')} ${source.excerpt_truncated?'· excerpt truncated':''}</p><a class="subtle" href="#evidence/${encodeURIComponent(id)}">Inspect the saved evidence →</a></div></details>`;}).join('');
    const stamp=panelTime(n);return `<article class="notebook-reading"><a class="subtle" href="#projects">← All projects</a><div class="record-panel-meta notebook-reading-meta"><span class="record-type">NOTEBOOK</span><span class="record-status"><span class="badge revision">REVISION ${n.revision}</span></span><span class="record-topics">${topicTag(n.domain)}</span>${stamp?`<time>${esc(stamp)}</time>`:''}</div><h2>${esc(n.title)}</h2><p class="notebook-lede">${esc(n.summary)}</p><div class="research-note">AI-authored research synthesis. Sources may include abstracts or incomplete excerpts. Read the limitations alongside the findings.</div><h3>Findings & interpretations</h3>${paragraph(n.findings)}<h3>Limitations & competing views</h3>${paragraph(n.limitations)}<h3>Questions worth following</h3>${paragraph(n.next_questions)}<h3>The source trail</h3>${sourceHtml}<p><a class="text-link" href="notebooks/${encodeURIComponent(n.id)}.md">Read as Markdown ↓</a></p><a class="subtle" href="#history/${encodeURIComponent(n.updated_by)}">How this revision was made →</a></article>`;
  }
  function discoveryCard(n){
    const project=projects.find(p=>p.id===n.project);
    const stamp=panelTime(n);
    return `<article class="discovery-card" style="--topic-color:${esc(topicColors[n.domain]||'var(--cyan)')}"><div class="discovery-meta"><span>FINDING</span>${topicTag(n.domain)}${stamp?`<time>${esc(stamp)}</time>`:''}</div><h2>${esc(n.title)}</h2><p class="discovery-summary">${esc(n.summary)}</p><div class="discovery-why"><strong>WHY IT MATTERS</strong><p>${esc(project?.question||'This finding contributes to an active research question in the durable record.')}</p></div><details><summary>Research depth</summary><div class="discovery-depth"><section><strong>FINDINGS</strong>${paragraph(n.findings)}</section><section><strong>LIMITATIONS / COMPETING VIEWS</strong>${paragraph(n.limitations)}</section><section><strong>EVIDENCE DEPTH</strong><p>${n.evidence.length} recorded evidence item${n.evidence.length===1?'':'s'} support this notebook revision.</p></section></div></details><div class="discovery-actions"><a class="text-link" href="#projects/notebook:${encodeURIComponent(n.id)}">Read the notebook →</a><a class="subtle" href="#evidence">Inspect evidence →</a><a class="subtle" href="#history/${encodeURIComponent(n.updated_by||n.created_by)}">Exact receipt →</a></div></article>`;
  }
  function discoveries(){
    const published=books.filter(n=>n.findings&&n.summary);
    document.getElementById('discoveries-content').innerHTML=published.length?`<div class="discovery-intro"><p><strong>${published.length}</strong> published notebook${published.length===1?'':'s'} currently form the discovery layer. A discovery here means a recorded research finding—not settled truth.</p></div><div class="discovery-list">${published.map(discoveryCard).join('')}</div>`:'<p class="empty">No research finding has reached the notebook layer yet.</p>';
  }
  function topics(){
    const cards=(s.research_topics||[]).map(topic=>{
      const ps=projects.filter(p=>p.domain===topic.id), ns=books.filter(n=>n.domain===topic.id), open=ps.filter(p=>p.status==='active');
      const latest=ns[0];
      return `<article class="topic-hub" style="--topic-color:${esc(topicColors[topic.id]||'var(--cyan)')}"><div class="topic-hub-head"><span>RESEARCH TOPIC</span><h2>${esc(topic.label)}</h2><p>${open.length} active project${open.length===1?'':'s'} · ${ns.length} published notebook${ns.length===1?'':'s'}</p></div>${open[0]?`<div><strong>QUESTION IN MOTION</strong><p>${esc(open[0].question)}</p></div>`:''}${latest?`<div><strong>LATEST FINDING</strong><p>${esc(latest.summary)}</p></div>`:''}<div class="topic-hub-actions"><a class="text-link" href="#projects/topic:${encodeURIComponent(topic.id)}">Explore this topic →</a><a class="subtle" href="#topics">Journal activity →</a></div></article>`;
    }).join('');
    document.getElementById('topics-content').innerHTML=`<div class="topic-hubs">${cards||'<p class="empty">No research topics are configured.</p>'}</div>`;
  }
  function render(page,selected){
    if(page==='discoveries'){discoveries();return;}
    if(page==='topics'){topics();return;}
    if(page==='projects'){
      let output='';
      if(selected.startsWith('notebook:'))output=notebook(books.find(n=>n.id===selected.slice(9)));
      else if(selected.startsWith('topic:')){const topic=decodeURIComponent(selected.slice(6)),topicProjects=projects.filter(p=>p.domain===topic),topicBooks=books.filter(n=>n.domain===topic);output=`<p class="topic-filter-note">Showing <strong>${esc(topicName(topic).toLowerCase())}</strong> · <a href="#projects">show all</a></p><div class="project-grid">${topicProjects.map((p,i)=>projectCard(p,i<2)).join('')||'<p class="empty">No projects match this topic.</p>'}</div><h2 class="shelf-title">Published notebooks</h2><div class="project-grid">${topicBooks.map((n,i)=>bookCard(n,i<2)).join('')||'<p class="empty">No published notebooks match this topic.</p>'}</div>`;}
      else if(selected){const p=projects.find(p=>p.id===selected);output=p?projectCard(p,true)+`<h2 class="shelf-title">The work so far</h2><div class="project-grid">${books.filter(n=>n.project===p.id).map((n,i)=>bookCard(n,i<2)).join('')||'<p class="empty">Still investigating. No notebook has been published for this question yet.</p>'}</div>`:'<p class="empty">Project not found.</p>';}
      else output=`<div class="project-grid">${[...projects].sort((a,b)=>(b.status==='active')-(a.status==='active')||b.updated_version-a.updated_version) .map((p,i)=>projectCard(p,i<2)).join('')||'<p class="empty">The first research question will appear after an autonomous wake.</p>'}</div><h2 class="shelf-title">The notebook shelf ${help('notebook_shelf')}</h2><div class="project-grid">${books.map((n,i)=>bookCard(n,i<2)).join('')||'<p class="empty">No research has been published yet. Finished work will appear here with its evidence and limitations.</p>'}</div>`;
      document.getElementById('pet-projects').innerHTML=output;return;
    }
    const journal=s.journal.at(-1);
    const noteLink=journal?'#journal':'#about';
    const latestBook=books[0], leadProject=latestBook?projects.find(p=>p.id===latestBook.project):active[0];
    const completed=invocations.filter(i=>['accepted','rejected','deferred','failed','recovered'].includes(i.status));
    const recentWakes=completed.slice(-60);
    const wakeCells=recentWakes.map(i=>`<a class="home-wake-cell ${esc(i.status||'unknown')}" href="#history/${encodeURIComponent(i.id)}" title="${esc(i.status||'unknown')} · ${esc(i.id)}"></a>`).join('');
    const outcomeCounts={};recentWakes.forEach(i=>outcomeCounts[i.status]=(outcomeCounts[i.status]||0)+1);
    const acceptedRecent=outcomeCounts.accepted||0,rejectedRecent=outcomeCounts.rejected||0,deferredRecent=outcomeCounts.deferred||0;
    const topicActivity=(s.research_topics||[]).map(topic=>{const ps=projects.filter(p=>p.domain===topic.id),ns=books.filter(n=>n.domain===topic.id),activeCount=ps.filter(p=>p.status==='active').length;return {topic,ps,ns,activeCount,score:ps.length+ns.length};});
    const maxTopic=Math.max(1,...topicActivity.map(x=>x.score));
    const topicObservatory=topicActivity.map(({topic,ps,ns,activeCount,score})=>{const latest=ns[0],question=ps.find(p=>p.status==='active')?.question||ps[0]?.question||'No active project has been recorded for this topic yet.';return `<a class="observatory-topic" style="--topic-color:${esc(topicColors[topic.id]||'var(--cyan)')};--activity:${Math.max(4,100*score/maxTopic)}%" href="#projects/topic:${encodeURIComponent(topic.id)}"><div><span>${activeCount?'ACTIVE':'TOPIC'}</span><h3>${esc(topic.label)}</h3></div><p>${esc(question)}</p><div class="topic-signal"><i></i><b>${ns.length}</b><small>notebooks</small></div>${latest?`<small class="topic-latest">LATEST / ${esc(latest.title)}</small>`:''}</a>`;}).join('');
    const leadTitle=latestBook?.title||journal?.title||'The record is still building its first research finding.';
    const leadSummary=latestBook?.summary||journal?.summary||'WAKE✳︎ will not manufacture a discovery before the durable record contains one.';
    const leadTopic=latestBook?.domain;
    const evidenceDepth=latestBook?.evidence?.length||0;
    document.getElementById('pet-home').innerHTML=`
      <section class="observatory-hero">
        <div class="observatory-question"><p class="eyebrow">AN OPEN EXPERIMENT IN AI CONTINUITY</p><h1>Can the work continue when every session starts over?</h1><p>The model forgets. The public record carries evidence, commitments, corrections, and unfinished work into the next fresh session.</p><div class="observatory-actions"><a class="primary-link" href="#discoveries">See what it has found <span>→</span></a><a class="subtle" href="#about">Understand the experiment →</a></div></div>
        <aside class="observatory-now"><p class="eyebrow">RIGHT NOW / CYCLE ${s.version}</p><strong>${esc(status)}</strong><p>${active[0]?esc(active[0].question):'Waiting for the next recorded research question.'}</p><div class="now-stats"><span><b>${active.length}</b> active questions</span><span><b>${books.length}</b> notebooks</span><span><b>${Object.keys(s.evidence||{}).length}</b> evidence records</span></div></aside>
      </section>
      <section class="home-lead-story" style="--topic-color:${esc(topicColors[leadTopic]||'var(--cyan)')}">
        <div class="lead-story-label"><p class="eyebrow">LATEST RESEARCH SIGNAL</p>${leadTopic?topicTag(leadTopic):''}</div>
        <div class="lead-story-copy"><h2>${esc(leadTitle)}</h2><p>${esc(leadSummary)}</p>${leadProject?`<div class="lead-question"><span>QUESTION BEHIND IT</span><p>${esc(leadProject.question)}</p></div>`:''}</div>
        <div class="lead-story-depth"><div><strong>${evidenceDepth}</strong><span>evidence records in this notebook</span></div><a class="text-link" href="${latestBook?`#projects/notebook:${encodeURIComponent(latestBook.id)}`:noteLink}">Understand it →</a><a class="subtle" href="#evidence">See the evidence →</a>${latestBook?.updated_by?`<a class="subtle" href="#history/${encodeURIComponent(latestBook.updated_by)}">Inspect the receipt →</a>`:''}</div>
      </section>
      <section class="home-motion">
        <div class="section-top"><div><p class="eyebrow">THE EXPERIMENT IS MOVING</p><h2>The shape of the last ${recentWakes.length} completed wakes.</h2></div><a class="subtle" href="#metrics">Open the instrument panel →</a></div>
        <div class="motion-grid"><div class="motion-pulse"><div class="home-wake-timeline">${wakeCells||'<span class="empty">No completed wakes yet.</span>'}</div><p>Each cell is a completed wake. Outcome is governance state—not a quality score.</p></div><div class="motion-numbers"><div><strong>${acceptedRecent}</strong><span>accepted</span></div><div><strong>${rejectedRecent}</strong><span>rejected</span></div><div><strong>${deferredRecent}</strong><span>deferred</span></div></div></div>
      </section>
      <section class="home-landscape"><div class="section-top"><div><p class="eyebrow">WHAT IS <span class="wake-mark">WAKE✳︎</span> THINKING ABOUT?</p><h2>Enter through a question you care about.</h2></div><a class="subtle" href="#topics">Full research landscape →</a></div><div class="observatory-topics">${topicObservatory}</div></section>
      <section class="home-depth"><div><p class="eyebrow">HOW DEEP DO YOU WANT TO GO?</p><h2>Same record. Different depth.</h2><p>Start with the story, inspect the research, or reconstruct the exact durable event.</p></div><nav aria-label="Research depth"><a href="#discoveries"><span>01 / STORY</span><strong>What did it find?</strong><small>Plain-language findings and why they matter.</small></a><a href="#projects"><span>02 / RESEARCH</span><strong>How does it know?</strong><small>Questions, notebooks, limitations, and evidence.</small></a><a href="#history"><span>03 / RECORD</span><strong>What exactly happened?</strong><small>Proposals, outcomes, identifiers, and provenance.</small></a></nav></section>
    `;
  }
  window.WakePet={render};
})();
