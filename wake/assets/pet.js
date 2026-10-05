/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Interface personality/experimental behavior kept separate from durable research mechanics. UI personality is not persistence or agency.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

window.WakePetReady=(async () => {
  'use strict';
  const d=await window.WakeData,s=d.state;
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
  const blogPosts=Object.values(s.posts||{});
  const topicActivityRows=()=> (s.research_topics||[]).map(topic=>{
    const ps=projects.filter(p=>p.domain===topic.id);
    const ns=books.filter(n=>n.domain===topic.id);
    const bs=blogPosts.filter(post=>s.projects?.[post.project]?.domain===topic.id);
    const publications=ns.length+bs.length;
    return {
      topic, ps, ns, bs,
      activeCount:ps.filter(p=>p.status==='active').length,
      publications,
      score:ps.length+publications
    };
  }).sort((a,b)=>
    b.score-a.score ||
    b.publications-a.publications ||
    b.ps.length-a.ps.length ||
    a.topic.label.localeCompare(b.topic.label)
  );
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
    const stamp=panelTime(n);return `<article class="notebook-reading"><a class="subtle" href="#projects">← All projects</a><div class="record-panel-meta notebook-reading-meta"><span class="record-type">NOTEBOOK</span><span class="record-status"><span class="badge revision">REVISION ${n.revision}</span></span><span class="record-topics">${topicTag(n.domain)}</span>${stamp?`<time>${esc(stamp)}</time>`:''}</div><h2>${esc(n.title)}</h2><p class="notebook-lede">${esc(n.summary)}</p><div class="research-note">AI-authored research synthesis. Sources may include abstracts or incomplete excerpts. Read the limitations alongside the findings.</div><h3>Findings & interpretations</h3>${paragraph(n.findings)}<h3>Limitations & competing views</h3>${paragraph(n.limitations)}<h3>Questions worth following</h3>${paragraph(n.next_questions)}<h3>The source trail</h3>${sourceHtml}<a class="subtle" href="#history/${encodeURIComponent(n.updated_by)}">How this revision was made →</a></article>`;
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
    const cards=topicActivityRows().map(({topic,ps,ns,bs,activeCount})=>{
      const open=ps.filter(p=>p.status==='active'), latest=ns[0];
      return `<article class="topic-hub" style="--topic-color:${esc(topicColors[topic.id]||'var(--cyan)')}"><div class="topic-hub-head"><span>RESEARCH TOPIC</span><h2>${esc(topic.label)}</h2><p>${activeCount} active project${activeCount===1?'':'s'} · ${ns.length} published notebook${ns.length===1?'':'s'} · ${bs.length} blog post${bs.length===1?'':'s'}</p></div>${open[0]?`<div><strong>QUESTION IN MOTION</strong><p>${esc(open[0].question)}</p></div>`:''}${latest?`<div><strong>LATEST FINDING</strong><p>${esc(latest.summary)}</p></div>`:''}<div class="topic-hub-actions"><a class="text-link" href="#projects/topic:${encodeURIComponent(topic.id)}">Explore this topic →</a><a class="subtle" href="#topics">Journal activity →</a></div></article>`;
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
      else output=`<h2 class="shelf-title">The notebook shelf ${help('notebook_shelf')}</h2><div class="project-grid">${books.map((n,i)=>bookCard(n,i<2)).join('')||'<p class="empty">No research has been published yet. Finished work will appear here with its evidence and limitations.</p>'}</div><h2 class="shelf-title">Research notes</h2><div class="project-grid">${[...projects].sort((a,b)=>(b.status==='active')-(a.status==='active')||b.updated_version-a.updated_version).map((p,i)=>projectCard(p,i<2)).join('')||'<p class="empty">The first research question will appear after an autonomous wake.</p>'}</div>`;
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
    const topicActivity=topicActivityRows();
    const maxTopic=Math.max(1,...topicActivity.map(x=>x.score));
    const topicObservatory=topicActivity.map(({topic,ps,ns,activeCount,score})=>{const latest=ns[0],question=ps.find(p=>p.status==='active')?.question||ps[0]?.question||'No active project has been recorded for this topic yet.';return `<a class="observatory-topic" style="--topic-color:${esc(topicColors[topic.id]||'var(--cyan)')};--activity:${Math.max(4,100*score/maxTopic)}%" href="#projects/topic:${encodeURIComponent(topic.id)}"><div><span>${activeCount?'ACTIVE':'TOPIC'}</span><h3>${esc(topic.label)}</h3></div><p>${esc(question)}</p><div class="topic-signal"><i></i><b>${ns.length}</b><small>notebooks</small></div>${latest?`<small class="topic-latest">LATEST / ${esc(latest.title)}</small>`:''}</a>`;}).join('');
    const leadTitle=latestBook?.title||journal?.title||'The record is still building its first research finding.';
    const leadSummary=latestBook?.summary||journal?.summary||'WAKE✳︎ will not manufacture a discovery before the durable record contains one.';
    const leadTopic=latestBook?.domain;
    const evidenceDepth=latestBook?.evidence?.length||0;
    const latestResearch=books.slice(0,3);
    const latestResearchRows=latestResearch.map(n=>{
      const stamp=panelTime(n);
      return `<a class="nebula-research-row" href="#projects/notebook:${encodeURIComponent(n.id)}"><span class="nebula-thumb" style="--topic-color:${esc(topicColors[n.domain]||'var(--cyan)')}"></span><span><strong>${esc(n.title)}</strong><small>${stamp?esc(stamp):'Recorded notebook'}</small></span><b aria-hidden="true">›</b></a>`;
    }).join('');
    const topTopics=topicActivity.slice(0,4).map(({topic,score})=>`<a class="nebula-topic-row" href="#projects/topic:${encodeURIComponent(topic.id)}"><span>${esc(topic.label)}</span><b>${score}</b></a>`).join('');
    const publishedBlogPosts=[...blogPosts]
      .filter(post=>String(post.status||'current')!=='superseded')
      .sort((a,b)=>Number(b.created_version||0)-Number(a.created_version||0));
    const latestBlog=publishedBlogPosts[0]||[...blogPosts].sort((a,b)=>Number(b.created_version||0)-Number(a.created_version||0))[0];
    const latestPublishedBook=books.find(n=>n.findings&&n.summary)||books[0];
    const latestBlogInvocation=latestBlog?.created_by?s.invocations?.[latestBlog.created_by]:null;
    const latestBlogStamp=latestBlogInvocation?.time?format(latestBlogInvocation.time):'';
    const latestBookStamp=latestPublishedBook?panelTime(latestPublishedBook):'';
    document.getElementById('pet-home').innerHTML=`
      <section class="nebula-home-hero">
        <div class="nebula-hero-copy">
          <h1>A more durable<br><span>intelligence future.</span></h1>
          <p>WAKE✳︎ is infrastructure for accountable work across interchangeable intelligences — preserving how we reach conclusions, not just what they are.</p>
          <div class="nebula-hero-actions">
            <a class="primary-link" href="#discoveries">Explore Research <span>→</span></a>
            <a class="nebula-secondary" href="console.html">Open Console</a>
          </div>
        </div>
      </section>

      <section class="nebula-pillars" aria-label="WAKE principles">
        <article>
          <span class="nebula-icon nebula-record" aria-hidden="true">
            <svg viewBox="0 0 64 64"><ellipse cx="32" cy="14" rx="19" ry="8"/><path d="M13 14v13c0 4.5 8.5 8 19 8s19-3.5 19-8V14"/><path d="M13 27v13c0 4.5 8.5 8 19 8s19-3.5 19-8V27"/><path d="M13 40v9c0 4.5 8.5 8 19 8s19-3.5 19-8v-9"/></svg>
          </span>
          <div><h2>Record</h2><p>Append-only history<br>with verifiable provenance.</p></div>
        </article>
        <article>
          <span class="nebula-icon nebula-govern" aria-hidden="true">
            <svg viewBox="0 0 64 64"><path d="M32 7 49 14v14c0 11-6.5 21-17 28-10.5-7-17-17-17-28V14L32 7Z"/><path class="shield-flame" d="M32 22c3.6 4.5 5.5 7.9 5.5 11a5.5 5.5 0 0 1-11 0c0-3.1 1.9-6.5 5.5-11Z"/></svg>
          </span>
          <div><h2>Govern</h2><p>Deterministic policy<br>and accountability.</p></div>
        </article>
        <article>
          <span class="nebula-icon nebula-explore-glyph" aria-hidden="true">
            <svg viewBox="0 0 64 64">
              <path d="M32 31 32 13M32 31 16 22M32 31 48 22M32 31 20 48M32 31 44 48"/>
              <circle cx="32" cy="31" r="5"/><circle cx="32" cy="11" r="5"/><circle cx="14" cy="21" r="5"/><circle cx="50" cy="21" r="5"/><circle cx="18" cy="50" r="5"/><circle cx="46" cy="50" r="5"/>
            </svg>
          </span>
          <div><h2>Explore</h2><p>Research in<br>the open.</p></div>
        </article>
      </section>

      <section class="nebula-explore" aria-labelledby="nebula-explore-title">
        <div class="nebula-explore-heading">
          <div>
            <h2 id="nebula-explore-title">Explore WAKE✳︎</h2>
            <p>Different views into the same system. From research to documentation.</p>
          </div>
          <a href="#topics">View all topics →</a>
        </div>
        <div class="nebula-explore-grid">
          <article class="nebula-explore-card">
            <a class="nebula-explore-visual nebula-explore-research" href="#discoveries" aria-label="Open research"></a>
            <div class="nebula-explore-copy">
              <h3><a href="#discoveries">Research</a></h3>
              <p>Exploring how intelligence systems can work together accountably.</p>
              <nav class="nebula-explore-tags" aria-label="Research shortcuts">
                <a href="#topics">Topics</a><a href="map.html">Map</a><a href="#metrics">Metrics</a>
              </nav>
            </div>
          </article>
          <article class="nebula-explore-card">
            <a class="nebula-explore-visual nebula-explore-console" href="console.html" aria-label="Open Live Console"><i></i><i></i><i></i><i></i><i></i><i></i></a>
            <div class="nebula-explore-copy">
              <h3><a href="console.html">Live Console</a></h3>
              <p>Interactive tools, visualizations and the current state.</p>
              <nav class="nebula-explore-tags" aria-label="Console shortcuts">
                <a href="console.html?tool=map3d">3D Map</a><a href="console.html?tool=history">Timeline</a><a href="console.html?tool=records">Records</a>
              </nav>
            </div>
          </article>
          <article class="nebula-explore-card">
            <a class="nebula-explore-visual nebula-explore-about" href="#about" aria-label="About WAKE"></a>
            <div class="nebula-explore-copy">
              <h3><a href="#about">About WAKE✳︎</a></h3>
              <p>A long-horizon project for durable, accountable work.</p>
              <nav class="nebula-explore-tags" aria-label="About shortcuts">
                <a href="#about">The vision</a><a href="#lab">How it works</a><a href="https://github.com/sudofx/wake">Contributing</a>
              </nav>
            </div>
          </article>
          <article class="nebula-explore-card">
            <a class="nebula-explore-visual nebula-explore-docs" href="https://github.com/sudofx/wake/tree/master/docs" aria-label="Open documentation"></a>
            <div class="nebula-explore-copy">
              <h3><a href="https://github.com/sudofx/wake/tree/master/docs">Documentation</a></h3>
              <p>Guides, references and architecture details.</p>
              <nav class="nebula-explore-tags" aria-label="Documentation shortcuts">
                <a href="https://github.com/sudofx/wake#start-here--no-account-no-api-calls">Getting started</a>
              </nav>
            </div>
          </article>
        </div>
      </section>

      <section class="home-research-heading-panel" aria-labelledby="home-research-heading-title">
        <div><p class="eyebrow">CURRENT RESEARCH</p><h2 id="home-research-heading-title">Questions in motion.</h2><p>Lightweight progress from the recorded research frontier.</p></div>
        <a href="#topics">View all topics →</a>
      </section>

      <section class="home-latest-grid" aria-label="Latest published work">
        <article class="home-latest-card">
          <div class="home-latest-meta"><span>BOB’S LATEST POST</span>${latestBlogStamp?`<time>${esc(latestBlogStamp)}</time>`:''}</div>
          ${latestBlog?`
            <h2><a href="#blog/${encodeURIComponent(latestBlog.id)}">${esc(latestBlog.title||'Latest post')}</a></h2>
            <p>${esc(latestBlog.lede||String(latestBlog.body||'').split(/\n\s*\n/)[0]||'Read the latest note from Bob.')}</p>
            <div class="home-latest-actions"><a class="text-link" href="#blog/${encodeURIComponent(latestBlog.id)}">Read Bob’s post →</a><a class="subtle" href="#blog">All posts</a></div>
          `:'<p class="empty">Bob has not published a post yet.</p>'}
        </article>
        <article class="home-latest-card">
          <div class="home-latest-meta"><span>LATEST PUBLISHED NOTEBOOK</span>${latestBookStamp?`<time>${esc(latestBookStamp)}</time>`:''}</div>
          ${latestPublishedBook?`
            <h2><a href="#projects/notebook:${encodeURIComponent(latestPublishedBook.id)}">${esc(latestPublishedBook.title)}</a></h2>
            <p>${esc(latestPublishedBook.summary||'Open the latest published research notebook.')}</p>
            <div class="home-latest-stats"><span><b>R${esc(latestPublishedBook.revision??'—')}</b><small>revision</small></span><span><b>${latestPublishedBook.evidence?.length||0}</b><small>evidence</small></span><span><b>${esc(topicName(latestPublishedBook.domain))}</b><small>topic</small></span></div>
            <div class="home-latest-actions"><a class="text-link" href="#projects/notebook:${encodeURIComponent(latestPublishedBook.id)}">Read the notebook →</a><a class="subtle" href="#discoveries">All findings</a></div>
          `:'<p class="empty">No notebook has been published yet.</p>'}
        </article>
      </section>   `;  }
  window.WakePet={render};
  return window.WakePet;
})();
