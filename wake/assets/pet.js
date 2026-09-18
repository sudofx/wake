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
  const topicName=id=>names[id]||String(id||'Unconfigured topic').replaceAll('_',' ');
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
  function projectCard(p){return `<article class="project-card"><div class="entry-meta"><span class="badge">${esc(topicName(p.domain))}</span><span>${esc(p.status.toUpperCase())}</span></div><h3>${esc(p.title)}</h3><p>${esc(p.question)}</p><div class="next-step"><span>NEXT STEP</span>${esc(p.next_step)}</div><a class="text-link" href="#projects/${encodeURIComponent(p.id)}">Follow this question →</a></article>`;}
  function bookCard(n){return `<a class="notebook-card" href="#projects/notebook:${encodeURIComponent(n.id)}"><span class="eyebrow">${esc(topicName(n.domain))} / REVISION ${n.revision}</span><h3>${esc(n.title)}</h3><p>${esc(n.summary)}</p><span class="text-link">Read the notebook →</span></a>`;}
  function notebook(n){
    if(!n)return '<p class="empty">That notebook is not in this record.</p>';
    const sourceHtml=n.evidence.map(id=>{const e=s.evidence[id];let source={};try{source=JSON.parse(e.content);}catch{}return `<div class="data-card"><a class="text-link" href="${esc(e.source)}" target="_blank" rel="noopener noreferrer">${esc(id)} →</a><p>${esc(source.scope||'Collected source')} ${source.excerpt_truncated?'· excerpt truncated':''}</p><a class="subtle" href="#evidence/${encodeURIComponent(id)}">Inspect the saved evidence →</a></div>`;}).join('');
    return `<article class="notebook-reading"><a class="subtle" href="#projects">← All projects</a><p class="eyebrow">${esc(topicName(n.domain))} / REVISION ${n.revision}</p><h2>${esc(n.title)}</h2><p class="notebook-lede">${esc(n.summary)}</p><div class="research-note">AI-authored research synthesis. Sources may include abstracts or incomplete excerpts. Read the limitations alongside the findings.</div><h3>Findings & interpretations</h3>${paragraph(n.findings)}<h3>Limitations & competing views</h3>${paragraph(n.limitations)}<h3>Questions worth following</h3>${paragraph(n.next_questions)}<h3>The source trail</h3>${sourceHtml}<p><a class="text-link" href="notebooks/${encodeURIComponent(n.id)}.md">Read as Markdown ↓</a></p><a class="subtle" href="#history/${encodeURIComponent(n.updated_by)}">How this revision was made →</a></article>`;
  }
  function render(page,selected){
    if(page==='projects'){
      let output='';
      if(selected.startsWith('notebook:'))output=notebook(books.find(n=>n.id===selected.slice(9)));
      else if(selected){const p=projects.find(p=>p.id===selected);output=p?projectCard(p)+`<h2 class="shelf-title">The work so far</h2><div class="project-grid">${books.filter(n=>n.project===p.id).map(bookCard).join('')||'<p class="empty">Still investigating. No notebook has been published for this question yet.</p>'}</div>`:'<p class="empty">Project not found.</p>';}
      else output=`<div class="project-grid">${[...projects].sort((a,b)=>(b.status==='active')-(a.status==='active')||b.updated_version-a.updated_version).map(projectCard).join('')||'<p class="empty">The first research question will appear after an autonomous wake.</p>'}</div><h2 class="shelf-title">The notebook shelf ${help('notebook_shelf')}</h2><div class="project-grid">${books.map(bookCard).join('')||'<p class="empty">No research has been published yet. Finished work will appear here with its evidence and limitations.</p>'}</div>`;
      document.getElementById('pet-projects').innerHTML=output;return;
    }
    const domains=Object.entries(names).map(([id,label])=>({label,count:books.filter(n=>n.domain===id).length})).sort((a,b)=>b.count-a.count);
    const recent=books.filter(n=>n.updated_version>old);
    const journal=s.journal.at(-1);
    const event=d.events.find(item=>item.payload?.id===journal?.invocation);
    const evidence=[...new Set((event?.payload?.proposal?.actions||[]).flatMap(action=>action.evidence||[]))];
    const observation=journal?`<section class="observation-hero"><p class="eyebrow">EXPLORE / A RECORDED OBSERVATION</p><h1>${esc(journal.title)}</h1><p>${esc(journal.summary)}</p><div><a class="text-link" href="#journal">See what happened →</a><a class="subtle" href="#history/${encodeURIComponent(journal.invocation)}">Exact recorded wake →</a>${evidence.map(id=>`<a class="subtle" href="#evidence/${encodeURIComponent(id)}">Evidence: ${esc(id)} →</a>`).join('')}</div><small>This is the latest accepted journal entry, not a claim beyond the recorded run.</small></section>`:`<section class="observation-hero"><p class="eyebrow">EXPLORE</p><h1>Something unexpected happened.<br><em>Here it is.</em></h1><p>The first recorded observation will appear after an accepted wake.</p></section>`;
    document.getElementById('pet-home').innerHTML=`${observation}<div class="pet-intro"><div class="crt-pet" aria-label="Bob's small retro computer avatar"><div class="crt-screen"><span class="pixel-eye"></span><span class="pixel-eye"></span><span class="pixel-mouth"></span></div><div class="crt-label">BOB / CURIOUS BY DEFAULT <i></i></div><div class="crt-feet"></div></div><div><p class="eyebrow">WHAT ARE YOU LOOKING AT?</p><h1>Fresh sessions.<br><em>One durable record.</em></h1><p class="pet-description">Each model begins without hidden memory. The record carries forward only what can be checked: commitments, evidence, rules, and history.</p><a class="text-link" href="#about">How WAKE works →</a></div></div>${progressPanel}<div class="visit-card"><div><p class="eyebrow">READ / THE ONGOING ACCOUNT</p><h2>${previous?`${Math.max(0,s.version-old)} fresh wakes since your last visit.`:'A project that begins again, without starting over.'}</h2><p>Read the journal for the narrative, then inspect the laboratory when you want the underlying method and records.</p></div><a class="text-link" href="#journal">Read the journal →</a></div><div class="pet-layout"><section><div class="section-top"><div><p class="eyebrow">WHAT IT IS EXPLORING ${help('workbench')}</p><h2>Questions still in motion</h2></div><a class="subtle" href="#projects">All projects →</a></div><div class="project-grid">${active.map(projectCard).join('')||'<p class="empty">Choosing the next question. Its project and first steps will appear here.</p>'}</div><div class="section-top shelf-top"><div><p class="eyebrow">READ / RESEARCH NOTES ${help('latest_work')}</p><h2>Useful work, with limits</h2></div></div><div class="project-grid">${books.slice(0,4).map(bookCard).join('')||'<p class="empty">Still gathering evidence. Nothing is labeled finished just to fill the shelf.</p>'}</div></section><aside><div class="note-card"><p class="eyebrow">THE CONTRACT</p><h3>Don’t trust us.<br>Check us.</h3><p>Interesting observations point to the record. The record can still be incomplete, wrong, or open to another interpretation.</p><a class="text-link" href="#evidence">Inspect evidence →</a></div><div class="sidebar-block"><p class="eyebrow">RESEARCH, NOT THEATER</p><p class="small">Every decision, source, rejected proposal, and change of mind stays available to inspect.</p><a class="text-link" href="#lab">Open the laboratory →</a></div></aside></div>`;
  }
  window.WakePet={render};
})();
