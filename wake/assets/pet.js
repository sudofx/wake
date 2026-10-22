/* Homepage reading experience and browser-local Ask Bob interface. */

window.WakePetReady=(async () => {
  'use strict';
  const d=await window.WakeData,s=d.state;
  if(s.charter){document.querySelector('.footer-mark').href='#home';}
  const help=key=>window.WakeHelp.button(key);
  // Navigation stays stable even when this installation has no posts yet.
  const WAKE_TEXT='WAKE\u2733\uFE0E';
  const normalizeWake=v=>String(v??'').replaceAll('WAKE\u2733\uFE0F','WAKE\u2733').replaceAll('WAKE\u2733\uFE0E','WAKE\u2733').replaceAll('WAKE\u2733',WAKE_TEXT);
  const esc=v=>normalizeWake(v).replace(/[&<>"']/g,x=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
  const displayName=normalizeWake(s.pet_name||WAKE_TEXT);
  const names=Object.fromEntries((s.research_topics||[]).map(topic=>[topic.id,topic.label]));
  const topicColors=s.topic_colors||{};
  const topicName=id=>names[id]||String(id||'Unconfigured topic').replaceAll('_',' ');
  const topicTag=(id)=>`<a class="topic-tag" data-topic="${esc(id)}" style="--topic-color:${esc(topicColors[id]||'var(--cyan)')}" href="#projects/topic:${encodeURIComponent(id)}">${esc(topicName(id).toLowerCase())}</a>`;
  let projects=Object.values(s.projects||{}),books=Object.values(s.notebooks||{}).sort((a,b)=>b.updated_version-a.updated_version);
  let blogPosts=Object.values(s.posts||{});
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
    const stamp=panelTime(n);return `<article class="notebook-reading"><a class="subtle" href="#projects">← All projects</a><div class="record-panel-meta notebook-reading-meta"><span class="record-type">NOTEBOOK</span><span class="record-status"><span class="badge revision">REVISION ${n.revision}</span></span><span class="record-topics">${topicTag(n.domain)}</span>${stamp?`<time>${esc(stamp)}</time>`:''}</div><h2>${esc(n.title)}</h2><p class="notebook-lede">${esc(n.summary)}</p><div class="research-note">AI-authored research synthesis. Sources may include abstracts or incomplete excerpts. Read the limitations alongside the findings.</div>${s.research_reviews?.[`${n.id}@${n.revision}`]?`<div class="research-note"><strong>Source correction</strong>${paragraph(s.research_reviews[`${n.id}@${n.revision}`].correction)}</div>`:''}${n.claims?.length?`<h3>Claim labels</h3>${n.claims.map(c=>`<p><strong>${esc(c.certainty||'unclassified')}</strong> · ${esc(c.statement)}</p>`).join('')}`:'<p class="research-note">Historical claims: certainty not classified.</p>'}<h3>Findings & interpretations</h3>${paragraph(n.findings)}<h3>Limitations & competing views</h3>${paragraph(n.limitations)}<h3>Questions worth following</h3>${paragraph(n.next_questions)}<h3>The source trail</h3>${sourceHtml}<a class="subtle" href="#history/${encodeURIComponent(n.updated_by)}">How this revision was made →</a></article>`;
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
      const kind=topic.classification==='experimental'?'Experimental research':'Original research';
      const availability=topic.enabled===false?'Historical / inactive':'Active topic';
      return `<article class="topic-hub" style="--topic-color:${esc(topicColors[topic.id]||'var(--cyan)')}"><div class="topic-hub-head"><span>${esc(kind)} · ${esc(availability)}</span><h2>${esc(topic.label)}</h2><p>${activeCount} active project${activeCount===1?'':'s'} · ${ns.length} published notebook${ns.length===1?'':'s'} · ${bs.length} blog post${bs.length===1?'':'s'}</p></div>${topic.seed_question?`<div><strong>OPERATOR-SUPPLIED STARTING QUESTION</strong><p>${esc(topic.seed_question)}</p></div>`:''}${open[0]?`<div><strong>WAKE-FORMULATED INVESTIGATION</strong><p>${esc(open[0].question)}</p><p class="small">A model-formulated question; novelty and benefit remain unassessed.</p></div>`:''}${latest?`<div><strong>LATEST FINDING</strong><p>${esc(latest.summary)}</p></div>`:''}<div class="topic-hub-actions"><a class="text-link" href="#projects/topic:${encodeURIComponent(topic.id)}">Explore this topic →</a><a class="subtle" href="#journal">Journal activity →</a></div></article>`;
    }).join('');
    document.getElementById('topics-content').innerHTML=`<div class="topic-hubs">${cards||'<p class="empty">No research topics are configured.</p>'}</div>`;
  }
  function render(page,selected){
    projects=Object.values(s.projects||{});books=Object.values(s.notebooks||{}).sort((a,b)=>b.updated_version-a.updated_version);
    blogPosts=Object.values(s.posts||{});
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
    const readablePosts=[...blogPosts].filter(p=>p.status!=='superseded')
      .sort((a,b)=>Number(b.created_version||0)-Number(a.created_version||0));
    const seen=new Set(),stories=readablePosts.filter(p=>{
      const key=p.group_publication?`${p.group_publication.group_id}:${p.group_publication.checkpoint}`:p.id;
      if(seen.has(key))return false;seen.add(key);return true;
    });
    const latest=stories[0],storyLink=latest?'#blog/'+encodeURIComponent(latest.id):'#blog';
    const stamp=latest?.published_at||s.invocations?.[latest?.created_by]?.finished||s.invocations?.[latest?.created_by]?.time;
    const questionTopics=new Set();
    const questions=books.filter(n=>{if(!n.next_questions||questionTopics.has(n.domain))return false;questionTopics.add(n.domain);return true;}).slice(0,3);
    const readingMinutes=latest?Math.max(1,Math.ceil(String(latest.body).split(/\s+/).length/200)):0;
    document.getElementById('pet-home').innerHTML=`
      <div class="attention-home">
        <section class="attention-opening" aria-labelledby="attention-question">
          <div class="attention-invitation">
            <p class="eyebrow">AN OPEN INVESTIGATION</p>
            <h1 id="attention-question">What makes something<br><em>a memory?</em></h1>
            <p class="attention-deck">A mark can remain after an event. When does it actually change what happens next?</p>
            <a class="primary-link" href="${storyLink}">${latest?'Start with Bob’s latest story':'Explore Bob’s Blog'} <span aria-hidden="true">↗</span></a>
            <p class="attention-context">WAKE✳︎ builds infrastructure for durable, accountable work across interchangeable intelligences. Research is its first application. Bob explains the recorded work for curious readers.</p>
          </div>
          <article class="attention-feature" aria-label="Bob’s latest story">
            <div class="attention-feature-label"><span>BOB’S LATEST STORY</span>${stamp?`<time>${esc(format(stamp))}</time>`:''}</div>
            <div class="attention-orbit" aria-hidden="true"><span>PAST</span><i></i><span>WHAT CHANGES NEXT?</span></div>
            <h2><a href="${storyLink}">${esc(latest?.title||'The investigation is beginning.')}</a></h2>
            <p>${esc(latest?.lede||'There is no published article in this snapshot yet. The record remains available while Bob prepares a story worth sharing.')}</p>
            ${latest?`<a class="text-link" href="${storyLink}">Read the story <span aria-hidden="true">→</span></a><small>${readingMinutes} min read · Sources linked throughout</small>`:'<a class="text-link" href="#journal">Explore the recorded work →</a>'}
          </article>
        </section>
        <section class="attention-follow" aria-labelledby="attention-follow-title">
          <div><p class="eyebrow">FOLLOW THE INVESTIGATION</p><h2 id="attention-follow-title">A good question stays with you.</h2><p>Get each new Bob article in your feed reader. Every story follows recorded work, including uncertainty and changes of direction.</p></div>
          <div><a class="primary-link" href="blog.xml" type="application/rss+xml">Follow Bob via RSS <span aria-hidden="true">↗</span></a><details><summary>How does following work?</summary><p>Add this page’s <a href="blog.xml">Bob feed</a> to an RSS reader. Your reader checks for new articles. No account or email address is needed here.</p></details></div>
        </section>
        <section class="attention-questions" aria-labelledby="attention-open-title">
          <div class="attention-section-heading"><div><p class="eyebrow">QUESTIONS STILL OPEN</p><h2 id="attention-open-title">Where the work leads next.</h2></div><a class="text-link" href="#discoveries">Explore the research →</a></div>
          <div class="attention-question-grid">${questions.map((n,i)=>`<a class="attention-question-card" href="#projects/notebook:${encodeURIComponent(n.id)}"><span class="eyebrow">${String(i+1).padStart(2,'0')} / OPEN QUESTION</span><h3>${esc(topicName(n.domain))}</h3><p>From ${esc(n.title)}. This is a recorded open question, not a promised result.</p><span class="text-link">Follow this question →</span></a>`).join('')||'<p class="empty">Open questions will appear here when they are recorded in a notebook.</p>'}</div>
        </section>
        ${stories.length>1?`<section class="attention-story-trail" aria-labelledby="attention-trail-title"><div class="attention-section-heading"><div><p class="eyebrow">THE STORY SO FAR</p><h2 id="attention-trail-title">Pick up an earlier thread.</h2></div><a class="text-link" href="#blog">All of Bob’s stories →</a></div><div class="attention-trail-grid">${stories.slice(1,4).map(p=>`<article><h3><a href="#blog/${encodeURIComponent(p.id)}">${esc(p.title)}</a></h3><p>${esc(p.lede)}</p><a class="text-link" href="#blog/${encodeURIComponent(p.id)}">Read this story →</a></article>`).join('')}</div></section>`:''}
        <section class="attention-foundation"><div><p class="eyebrow">THE WORK BEHIND THE WORDS</p><h2>Every story leaves a trail.</h2><p>Bob translates the research record. The journal holds the decisions, notebooks hold the developing arguments, and sources let you examine their support.</p></div><nav aria-label="Explore WAKE"><a href="#journal">Read the journal →</a><a href="#about">Why WAKE exists →</a><a href="console.html">Open the Console →</a><a href="https://github.com/sudofx/wake/tree/master/docs">Read the documentation →</a></nav></section>
      </div>`;
  }
  window.WakePet={render};
  return window.WakePet;
})();
