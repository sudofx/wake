/* Disposable Research✳︎ view. No database, provider, or operator mutation APIs. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const safeUrl = value => { try { const u = new URL(value); return ['https:','http:'].includes(u.protocol) ? u.href : ''; } catch { return ''; } };
  const count = value => Number(value || 0).toLocaleString('en-US');
  const bytes = value => {
    const n=Number(value);
    if(!Number.isFinite(n)||n<0)return 'Not reported';
    if(n<1024)return `${count(n)} B`;
    if(n<1024*1024)return `${(n/1024).toFixed(1)} KB`;
    if(n<1024*1024*1024)return `${(n/1024/1024).toFixed(1)} MB`;
    return `${(n/1024/1024/1024).toFixed(2)} GB`;
  };
  const stamp = (value, full=false) => { if (!value || Number.isNaN(Date.parse(value))) return 'Unknown'; return new Intl.DateTimeFormat('en-US', {timeZone:'America/Los_Angeles', ...(full ? {month:'short',day:'numeric'} : {}), hour:'numeric',minute:'2-digit'}).format(new Date(value)); };
  const badge = status => `<span class="badge ${esc(status)}">${esc(String(status || 'recorded').replaceAll('_',' '))}</span>`;
  const local = ['localhost','127.0.0.1',''].includes(location.hostname);
  const raw = 'https://raw.githubusercontent.com/sudofx/wake/';
  let data, loading=false, fallback=false, loadedCommit='', selected='', topic='all', query='', mode=matchMedia('(max-width:700px)').matches?'list':'graph';
  let nodeById=new Map(), selectedWake='', wakeTab='summary', followLatest=true, focusedKinds=[];
  let motion=!matchMedia('(prefers-reduced-motion:reduce)').matches;
  const tools=window.WakeConsoleTools();
  const cube=window.WakeResearchCube($('matrix-cube'));
  const contextMap=window.WakeContextMap($('context-map-canvas'));
  let frontierState='active';
  let matrixCell='';
  const label = id => data?.topics.find(t=>t.id===id)?.label || 'Unattributed';
  const nodeFor = (kind, id) => data?.graph.nodes.find(n=>n.kind===kind && (n.detail.id===id || n.id===`${kind}:${id}`));
  const pickButton = (kind, item, text) => { const n=nodeFor(kind,item.id); return n?`<button type="button" data-record="${esc(n.id)}">${esc(text)}</button>`:`<button type="button" data-tool="projects">${esc(text)}</button>`; };
  function readUrl() {
    const p=new URL(location.href).searchParams;
    topic=p.get('topic') || 'all'; selected=p.get('record') || ''; query=p.get('q') || '';selectedWake=p.get('wake')||'';followLatest=!selectedWake;wakeTab=['summary','context','response','provider','receipt'].includes(p.get('tab'))?p.get('tab'):'summary';
    if(['list','graph'].includes(p.get('view'))) mode=p.get('view');
  }
  function writeUrl(push=true) {
    const u=new URL(location.href); for(const key of ['topic','record','q','view','wake','tab'])u.searchParams.delete(key);
    if(selectedWake&&!followLatest){u.searchParams.set('wake',selectedWake);u.searchParams.set('tab',wakeTab);}
    if(topic!=='all')u.searchParams.set('topic',topic); if(selected)u.searchParams.set('record',selected); if(query)u.searchParams.set('q',query);u.searchParams.set('view',mode);
    if(u.href!==location.href)history[push?'pushState':'replaceState'](null,'',u);
  }
  function notice(message) { $('notice').hidden=!message; $('notice').textContent=message || ''; }
  async function json(url) { const r=await fetch(url,{cache:'no-store',signal:AbortSignal.timeout(12000)});if(!r.ok)throw new Error(`HTTP ${r.status}`);return r.json(); }
  function validate(d) {
    if(d?.projection_schema!==1 || d?.projection_kind!=='disposable-research-view' || d.authoritative!==false || !d.head || !Array.isArray(d.graph?.nodes) || !Array.isArray(d.graph?.edges) || !d.records || !Array.isArray(d.activity) || !Array.isArray(d.topics) || !d.metrics || !d.evidence || !d.status)throw new Error('Unsupported research projection');
    const ids=new Set(d.graph.nodes.map(n=>n.id));
    if(d.graph.nodes.some(n=>!n.detail) || d.graph.edges.some(e=>!ids.has(e.source)||!ids.has(e.target)))throw new Error('Incomplete graph projection');
    return d;
  }
  function freshness() {
    if(!data)return;
    const age=Math.max(0,Math.round((Date.now()-Date.parse(data.generated))/60000));
    $('freshness').textContent=`${fallback?'Published snapshot':'Record snapshot'} · ${stamp(data.generated,true)} PT${age>15?` · ${age} min old`:''}`;
  }
  async function refresh() {
    if(loading)return;loading=true;$('refresh').disabled=true;$('refresh').textContent='Refreshing…';
    try {
      let next,commit=''; fallback=false;
      if(local) next=await json('research-data.json');
      else {
        try { next=await json(`${raw}wake-live/research-data.json`); }
        catch { fallback=true;next=await json('research-data.json'); }
      }
      validate(next);
      if(data && data.head===next.head && data.generated===next.generated){freshness();notice(next.preview_transport_error?'Public snapshot refresh failed. The last dated snapshot remains visible.':fallback?'Live data is unavailable. Showing the published snapshot; its date is shown above.':'');return;}
      const old=nodeById.get(selected);
      data=next;loadedCommit=commit;nodeById=new Map(data.graph.nodes.map(n=>[n.id,n]));
      if(old && !nodeById.has(selected))selected=nodeFor(old.kind,old.detail.id)?.id || '';
      if(topic!=='all'&&!data.topics.some(t=>t.id===topic))topic='all';
      notice(next.preview_transport_error?'Public snapshot refresh failed. The last dated snapshot remains visible.':fallback?'Live data is unavailable. Showing the published snapshot; its date is shown above.':'');
      render();writeUrl(false);freshness();
    } catch(error) {
      if(data) { fallback=true;notice('Refresh failed. The previous snapshot remains visible.');freshness(); }
      else { notice('The research record could not be loaded. Retry, or inspect the complete record tools.');$('status-band').innerHTML='<p class="empty">Record unavailable · <button type="button" data-tool="lab">Open the Lab →</button></p>'; }
    } finally {loading=false;$('refresh').disabled=false;$('refresh').textContent='Refresh record ↻';}
  }
  function visibleRecord(x) {return topic==='all'||x.domain===topic||data.records.projects.find(p=>p.id===x.project)?.domain===topic;}
  function render() {
    const s=data.status,latest=s.latest || {};
    const cells=[['Accepted cycles',count(s.accepted_cycles),'Accepted transitions, not a quality score',''],['Latest outcome',latest.status || 'No attempts',latest.model || 'No recorded model',latest.status],['Active projects',count(s.active_projects),`${count(data.record_totals.projects)} projects in the record`,''],['Open commitments',count(s.open_commitments),'Outstanding recorded obligations',''],['Research focus',s.attention_topic?label(s.attention_topic):'Unassigned',s.regime?.enabled?`Time Dilation: ${s.regime.mode} · ×${s.regime.scale}`:'No recorded Time Dilation regime','']];
    $('status-band').innerHTML=cells.map(([name,value,note,status],i)=>`<div class="status-cell"><span class="label">${esc(name)}</span><button type="button" class="status-value ${i===1||i===4?'latest-label ':''}${esc(status)}" data-metric="${['accepted','latest','projects','commitments','attention'][i]}">${esc(value)}</button><small>${esc(note)}</small></div>`).join('');
    $('topic').innerHTML='<option value="all">All topics</option>'+data.topics.map(t=>`<option value="${esc(t.id)}">${esc(t.label)}</option>`).join('');$('topic').value=topic;$('search').value=query;
    renderFrontier();renderMap();renderDetail();renderMetrics();renderSynthesis();renderCube();renderWake();renderInstruments();
    $('provenance').innerHTML=`<p>Snapshot: ${esc(stamp(data.generated,true))} PT · accepted state ${count(data.version)}</p><p>Authority: ${esc(data.source.authority || 'Verified export')} / ${esc(data.source.database || 'record')}</p><p>Record head: <code>${esc(data.head)}</code></p>${loadedCommit?`<p>Projection commit: <code>${esc(loadedCommit)}</code></p>`:''}<p><a href="research-data.json">Published JSON snapshot</a> · <a href="https://github.com/sudofx/wake/tree/wake-state">Authority checkpoint ↗</a></p>`;
  }
  function renderFrontier() {
    const projects=data.records.projects.filter(visibleRecord);
    projects.sort((a,b)=>({active:0,parked:1,completed:2}[a.status]??3)-({active:0,parked:1,completed:2}[b.status]??3));
    $('frontier').innerHTML=projects.map(p=>{
      const block=data.frontier.acquisition.find(x=>x.project===p.id)?.capability_blocked;
      return `<article class="project-row">${badge(p.status)}${pickButton('project',p,p.title)}<p class="question">${esc(p.question)}</p><span class="topic-label">${esc(label(p.domain))}</span>${block?'<p class="caption">Capability blocked · inspect acquisition history.</p>':''}</article>`;
    }).join('')||'<p class="empty">No projects in this topic.</p>';
    const commitments=data.records.commitments.filter(x=>x.status==='open');
    $('commitments').innerHTML=commitments.map(c=>`<div class="obligation">${badge(c.status)}${pickButton('commitment',c,c.task)}<p class="caption">Due accepted cycle ${count(c.due_cycle)}${data.version>=c.due_cycle?' · at or past due':''}</p></div>`).join('')||'<p class="empty">No open commitments.</p>';
  }
  function scopedNodes() {
    let nodes=data.graph.nodes;
    if(topic!=='all'){
      const seeds=new Set(nodes.filter(n=>visibleRecord(n.detail)).map(n=>n.id));
      const linked=new Set(seeds);
      data.graph.edges.forEach(e=>{if(seeds.has(e.source)&&e.relation==='evidence')linked.add(e.target);});
      nodes=nodes.filter(n=>linked.has(n.id));
    }
    if(query){const q=query.toLowerCase();nodes=nodes.filter(n=>`${n.title} ${n.id} ${JSON.stringify(n.detail)}`.toLowerCase().includes(q));}
    return nodes;
  }
  function renderMap() {
    const scoped=scopedNodes();
    $('graph-mode').setAttribute('aria-pressed',String(mode==='graph'));$('list-mode').setAttribute('aria-pressed',String(mode==='list'));
    $('research-map').toggleAttribute('hidden',mode!=='graph');$('map-list').hidden=mode!=='list';
    $('map-list').innerHTML=scoped.map(n=>`<div class="map-list-row"><span class="badge">${esc(n.kind)}</span><button type="button" aria-pressed="${n.id===selected}" data-record="${esc(n.id)}">${esc(n.title)}<small>${esc(n.detail.status || n.detail.evidence_class || 'recorded')}</small></button></div>`).join('')||'<p class="empty">No records match. Try another topic or clear the search.</p>';
    document.querySelectorAll('[data-kind]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.kind.split(',').some(k=>focusedKinds.includes(k)))));
    const kinds=['project','research','notebook','evidence','belief','commitment'];
    const neighbors=new Set([selected]);data.graph.edges.forEach(e=>{if(e.source===selected)neighbors.add(e.target);if(e.target===selected)neighbors.add(e.source);});
    const shown=[];
    kinds.forEach(kind=>{
      const list=scoped.filter(n=>n.kind===kind);list.sort((a,b)=>Number(neighbors.has(b.id))-Number(neighbors.has(a.id))||Number(b.detail.status==='active')-Number(a.detail.status==='active'));
      shown.push(...list.slice(0,8));
    });
    const usedKinds=kinds.filter(kind=>shown.some(n=>n.kind===kind));
    const width=Math.max(640,$('map-stage').clientWidth),step=width/Math.max(usedKinds.length,1),pos=new Map();
    $('research-map').setAttribute('viewBox',`0 0 ${width} 520`);
    usedKinds.forEach((kind,col)=>{
      const rows=shown.filter(n=>n.kind===kind);
      rows.forEach((n,i)=>pos.set(n.id,{x:step*(col+.5),y:65+i*(440/Math.max(rows.length,1))}));
    });
    let svg='<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#75e6e3"/></marker></defs>';
    for(let x=0;x<=width;x+=50)svg+=`<path class="map-grid" d="M${x} 40V510"/>`;for(let y=60;y<=510;y+=50)svg+=`<path class="map-grid" d="M0 ${y}H${width}"/>`;
    usedKinds.forEach((kind,i)=>{svg+=`<text class="map-lane" x="${step*(i+.5)}" y="28" text-anchor="middle">${esc(kind==='research'?'SOURCE SEARCH':kind.toUpperCase())}</text>`;});
    const edges=data.graph.edges.filter(e=>pos.has(e.source)&&pos.has(e.target));
    edges.forEach(e=>{const a=pos.get(e.source),b=pos.get(e.target),focused=e.source===selected||e.target===selected;svg+=`<path class="map-edge${focused?' focused':''}" ${focused?'marker-end="url(#arrow)"':''} d="M${a.x} ${a.y} C${(a.x+b.x)/2} ${a.y},${(a.x+b.x)/2} ${b.y},${b.x} ${b.y}"><title>${esc(nodeById.get(e.source)?.title)} → ${esc(e.relation)} → ${esc(nodeById.get(e.target)?.title)}</title></path>`;});
    const marks={project:'□',research:'◇',notebook:'▤',evidence:'●',belief:'△',commitment:'△'};
    shown.forEach(n=>{const p=pos.get(n.id),connected=neighbors.has(n.id),nodeWidth=Math.min(180,step-14),chars=Math.max(9,Math.floor((nodeWidth-24)/7)),short=n.title.length>chars?n.title.slice(0,chars-1)+'…':n.title;svg+=`<g class="map-node ${esc(n.detail.status || '')}${n.id===selected?' selected':''}${focusedKinds.includes(n.kind)?' category-focus':''}${selected&&!connected?' dimmed':''}" data-record="${esc(n.id)}" tabindex="0" role="button" aria-label="${esc(n.kind+': '+n.title)}" aria-pressed="${n.id===selected}" transform="translate(${p.x},${p.y})"><title>${esc(n.title)}</title><rect x="${-nodeWidth/2}" y="-26" width="${nodeWidth}" height="53"/><text class="node-mark" x="${-nodeWidth/2+10}" y="-5">${marks[n.kind]}</text><text class="node-type" x="${-nodeWidth/2+33}" y="-7">${esc((n.detail.status || n.detail.evidence_class || n.kind).slice(0,Math.max(6,chars-4)))}</text><svg class="node-label-window" x="${-nodeWidth/2+10}" y="1" width="${nodeWidth-20}" height="23"><text class="node-long-label" style="--label-shift:${-Math.max(0,n.title.length*7-nodeWidth+25)}px;--label-duration:${Math.max(4,n.title.length*.14)}s" x="0" y="14">${esc(n.title)}</text></svg></g>`;});
    if(!shown.length)svg+=`<text x="${width/2}" y="300" text-anchor="middle" fill="#9fb7bf">No matching records</text>`;
    $('research-map').innerHTML=svg;
    $('map-count').textContent=mode==='list'?`${count(scoped.length)} records in this view`:`${count(shown.length)} of ${count(scoped.length)} scoped records · ${count(edges.length)} visible relationships${data.graph.truncated?' · overview capped':''}`;
    const scopeIds=new Set(scoped.map(n=>n.id)),scopeEdges=data.graph.edges.filter(e=>scopeIds.has(e.source)&&scopeIds.has(e.target));
    contextMap.update({nodes:scoped,edges:scopeEdges},selected);
    const attributed=new Set(scoped.map(n=>n.detail.domain||data.records.projects.find(p=>p.id===n.detail.project)?.domain).filter(Boolean));
    $('context-map-stats').innerHTML=[['Records',scoped.length],['Links',scopeEdges.length],['Attributed topics',attributed.size],['Active projects',scoped.filter(n=>n.kind==='project'&&n.detail.status==='active').length]].map(([k,v])=>`<p>${esc(k)}<strong>${count(v)}</strong></p>`).join('');
    $('scope-note').textContent=`Current state ${count(data.version)} · ${data.graph.nodes.length} overview records`;
  }
  function renderDetail() {
    const n=nodeById.get(selected);
    document.querySelector('.detail-panel').classList.toggle('has-selection',Boolean(n));
    if(!n){$('record-detail').innerHTML=selected?'<p class="empty">This record is outside the current overview. Clear the search or refresh the record.</p>':'<p class="empty">Select a project or map node. Follow its recorded relationships into notebooks and source material.</p><p class="caption">The map shows a bounded current-state overview. Full history remains one layer deeper.</p>';return;}
    const d=n.detail,source=safeUrl(d.source),invocation=d.updated_by || d.created_by || d.resolved_by;
    const description=d.question || d.summary || d.statement || d.task || d.reason || '';
    const fields=['findings','limitations','next_questions','next_step','revision','confidence','due_cycle'];
    const relations=data.graph.edges.filter(e=>e.source===n.id||e.target===n.id);
    $('record-detail').innerHTML=`${badge(d.status || d.evidence_class || n.kind)}<h3 class="detail-title">${esc(n.title)}</h3><p class="detail-text">${esc(description)}</p>${d.domain?`<p class="caption">${esc(label(d.domain))}</p>`:''}${fields.filter(k=>d[k]!==undefined).map(k=>`<dl class="detail-field"><dt>${esc(k.replaceAll('_',' '))}${k==='confidence'?' · recorded belief assessment':''}</dt><dd>${esc(d[k])}</dd></dl>`).join('')}<div class="detail-links">${source?`<a href="${esc(source)}" target="_blank" rel="noopener noreferrer">Open source ↗</a>`:''}<button type="button" data-tool="map3d" data-tool-route="#record=${esc(encodeURIComponent(n.id))}">Open complete record map →</button>${invocation?`<button type="button" data-wake="${esc(invocation)}" data-inspect-wake="true">Origin / latest recorded change →</button>`:''}</div><p class="record-id">${esc(n.id)}<br>As of accepted state ${count(data.version)}</p><h3 style="margin-top:22px">Recorded relationships</h3>${relations.map(e=>{const target=e.source===n.id?e.target:e.source,other=nodeById.get(target);return `<div class="relation-row"><small>${e.source===n.id?'→':'←'} ${esc(e.relation)}</small><button type="button" data-record="${esc(target)}">${esc(other?.title || target)}</button><small>${esc(e.record)}</small></div>`;}).join('')||'<p class="caption">No relationships in this bounded overview.</p>'}`;
  }
  function meter(name,value,total,cls='') {return `<div class="meter-row"><button type="button" ${cls?`data-outcome="${esc(cls)}"`:`data-evidence-class="${esc(name)}"`}>${esc(name)}</button><strong>${count(value)}</strong><div class="meter-track"><i class="${cls}" style="width:${total?Math.min(100,100*value/total):0}%"></i></div></div>`;}
  function renderMetrics() {
    const m=data.metrics,maximum=Math.max(1,...m.hourly.map(b=>['accepted','rejected','deferred','failed'].reduce((n,k)=>n+(b[k]||0),0)));
    $('activity-chart').innerHTML=m.hourly.map(b=>{
      const total=['accepted','rejected','deferred','failed'].reduce((n,k)=>n+(b[k]||0),0),note=`${stamp(b.time,true)} PT: ${b.accepted||0} accepted, ${b.rejected||0} rejected, ${b.deferred||0} deferred, ${b.failed||0} failed`;
      return `<button type="button" class="hour-bin" data-hour="${esc(b.time)}" aria-label="${esc(note)}" title="${esc(note)}"><div class="hour-stack" style="height:${100*total/maximum}%">${['accepted','rejected','deferred','failed'].map(k=>`<i class="${k}" style="height:${total?100*(b[k]||0)/total:0}%"></i>`).join('')}</div></button>`;
    }).join('');
    $('activity-caption').textContent=m.hourly.length?`Completed invocations per hour · ${stamp(m.hourly[0].time,true)}–${stamp(m.hourly.at(-1).time,true)} PT · peak ${maximum}/hour. All topics; zero-hour gaps retained.`:'No completed invocation timestamps recorded.';
    $('activity').innerHTML=data.activity.slice(0,6).map(a=>`<div class="activity-row"><time datetime="${esc(a.time)}">${esc(stamp(a.time))}</time><span class="${esc(a.status)}">${esc(a.status)}</span><button type="button" data-wake="${esc(a.id)}" title="${esc(a.reason || a.model)}">${esc(a.reason || a.model || a.id)}</button></div>`).join('');
    const e=data.evidence,classes=[['source','Source-ready records'],['discovery','Discovery leads'],['metadata','Metadata records'],['receipt','Runtime receipts'],['unreadable','Unreadable material'],['unclassified','Unclassified records']];
    $('evidence-summary').innerHTML=evidenceRing(e)+`<div class="source-total">${e.classification_complete?'':'≥ '}${count(e.source_works)}<small>${e.classification_complete?'Distinct':'Known distinct'} source-ready works · ${count(e.total)} evidence records overall</small></div>`+classes.map(([key,name])=>meter(name,e.by_class[key]||0,e.total)).join('')+(!e.classification_complete?'<p class="caption">Classification is incomplete in this snapshot. Unclassified records are not counted as source-ready.</p>':'');
    $('evidence-recent').innerHTML=e.recent.map(x=>{const u=safeUrl(x.source);return `<div class="source-row">${badge(x.class)}<p>${u?`<a href="${esc(u)}" target="_blank" rel="noopener noreferrer">${esc(new URL(u).hostname)} ↗</a>`:esc(x.source)}</p><small>${esc(x.id)} · ${esc(stamp(x.time,true))} PT</small></div>`;}).join('')+`<p class="caption">Top source hosts · counts are records, not independent works.</p>`+e.hosts.map(x=>`<div class="rejection-row"><span>${esc(x.host)}</span><b>${count(x.count)}</b></div>`).join('');
    $('outcomes').innerHTML=ring(m.outcomes,m.completed,'Completed invocations')+['accepted','rejected','deferred','failed'].map(k=>meter(k[0].toUpperCase()+k.slice(1),m.outcomes[k]||0,m.completed,k)).join('')+`<p class="caption">${count(m.completed)} completed invocations across the record. ${count(Object.values(m.research_actions).reduce((sum,n)=>sum+n,0))} accepted non-editorial actions; ${count(m.editorial_actions)} editorial actions shown separately.</p><p class="caption">${count(m.provider_requests)} recorded provider requests${m.provider_requests_complete?'':' · historical request accounting incomplete'}.</p>`;
    $('rejections').innerHTML=m.rejection_reasons.map(x=>`<div class="rejection-row"><span>${esc(x.reason)}</span><b>${count(x.count)}</b></div>`).join('')||'<p class="empty">No recorded rejections.</p>';
  }
  function renderSynthesis() {
    const notebooks=data.records.notebooks.filter(visibleRecord).slice(0,6),beliefs=data.records.beliefs.filter(x=>x.status==='active');
    $('synthesis').innerHTML=notebooks.map(n=>`<article class="synthesis-item"><p class="eyebrow">NOTEBOOK · REVISION ${count(n.revision||1)}</p>${pickButton('notebook',n,n.title)}<p>${esc(n.summary)}</p><p>${count(n.evidence.length)} cited records · ${esc(label(n.domain || data.records.projects.find(p=>p.id===n.project)?.domain))}</p></article>`).join('')+beliefs.slice(0,2).map(b=>`<article class="synthesis-item"><p class="eyebrow">WORKING BELIEF</p>${pickButton('belief',b,b.statement)}<p>${count(b.evidence.length)} cited records · recorded assessment ${esc(b.confidence??'unknown')}</p></article>`).join('')||'<p class="empty">No notebooks or beliefs in this view.</p>';
  }

  function ring(values,total,title) {
    let offset=0;
    const colors={accepted:'var(--green)',rejected:'var(--red)',deferred:'var(--orange)',failed:'var(--muted)'};
    const segments=Object.entries(values).filter(([k])=>k in colors).map(([k,v])=>{const size=total?100*v/total:0;const mark=`<circle tabindex="0" role="button" data-outcome="${esc(k)}" aria-label="Inspect ${esc(k)} invocations: ${count(v)}" r="44" cx="60" cy="60" pathLength="100" fill="none" stroke="${colors[k]}" stroke-width="10" stroke-dasharray="${size} ${100-size}" stroke-dashoffset="${-offset}"/>`;offset+=size;return mark;}).join('');
    return `<div class="ring-readout"><svg viewBox="0 0 120 120" role="img" aria-label="${esc(title)}: ${count(total)}; ${esc(Object.entries(values).map(([k,v])=>`${k} ${v}`).join(', '))}"><circle r="53" cx="60" cy="60" class="ring-orbit" fill="none"/><circle r="44" cx="60" cy="60" fill="none" stroke="var(--line)" stroke-width="10"/><g transform="rotate(-90 60 60)">${segments}</g><text x="60" y="61" text-anchor="middle">${count(total)}</text><text class="ring-label" x="60" y="77" text-anchor="middle">INVOCATIONS</text></svg><div><strong>${total?Math.round(100*(values.accepted||0)/total):0}%</strong><p>accepted of completed</p><p class="caption">${count(values.accepted)} accepted / ${count(total)} completed</p></div></div>`;
  }

  function evidenceRing(e) {
    const groups=[['Source-ready',e.by_class.source||0,'var(--cyan)','Source-ready records'],['Leads / metadata',(e.by_class.discovery||0)+(e.by_class.metadata||0),'var(--orange)','Discovery leads'],['Other / unknown',e.total-(e.by_class.source||0)-(e.by_class.discovery||0)-(e.by_class.metadata||0),'var(--muted)','Unclassified records']];
    let offset=0;
    const arcs=groups.map(([name,value,color,link])=>{const size=e.total?100*value/e.total:0;const arc=`<circle r="44" cx="60" cy="60" pathLength="100" fill="none" stroke="${color}" stroke-width="10" stroke-dasharray="${size} ${100-size}" stroke-dashoffset="${-offset}"><title>${esc(name)}: ${count(value)} records</title></circle>`;offset+=size;return arc;}).join('');
    return `<div class="ring-readout evidence-ring"><svg viewBox="0 0 120 120" role="img" aria-label="Evidence retrieval depth: ${esc(groups.map(([name,value])=>`${name} ${value}`).join(', '))}"><circle r="53" cx="60" cy="60" class="ring-orbit" fill="none"/><g transform="rotate(-90 60 60)">${arcs}</g><text x="60" y="61" text-anchor="middle">${count(e.total)}</text><text class="ring-label" x="60" y="77" text-anchor="middle">RECORDS</text></svg><div>${groups.map(([name,value,color])=>`<p><span style="color:${color}">■</span> ${esc(name)} <b>${count(value)}</b></p>`).join('')}</div></div>`;
  }

  function renderCube() {
    const m=data.matrix;
    if(!m){$('matrix-state').textContent='Matrix progress is not reported in this snapshot.';const enable=$('matrix-enable');if(enable)enable.hidden=true;return;}
    matrixCell=cube.update(m) || m.cells[0]?.id;
    $('matrix-state').textContent=m.reported?(m.enabled?'Continuity campaign recorded':'Campaign not enabled'):'Campaign progress not reported';
    $('matrix-coverage').textContent=m.reported?`${count(m.completed)} / ${count(m.cells.length)}`:`— / ${count(m.cells.length)}`;
    const enable=$('matrix-enable');
    if(enable)enable.hidden=!(m.reported && m.enabled===false);
    $('cube-selectors').innerHTML=m.axes.map((a,i)=>`<label>${esc(a.label)}<select data-cube-axis="${i}" aria-label="${esc(a.label)}">${a.values.map((v,j)=>`<option value="${j}">${esc(v.label)}</option>`).join('')}</select></label>`).join('');
    renderCell();
  }
  function renderCell() {
    const m=data?.matrix,c=m?.cells.find(c=>c.id===matrixCell);if(!c)return;
    document.querySelectorAll('[data-cube-axis]').forEach(el=>el.value=c.position[Number(el.dataset.cubeAxis)]);
    $('cube-cell').innerHTML=`${esc(c.id)}<br><strong style="color:var(--orange)">${esc(c.status.replaceAll('_',' '))}</strong>${c.score!==null&&c.score!==undefined?` · recorded score ${esc(c.score)}`:''}<br>${m.axes.map((a,i)=>esc(a.values[c.position[i]].description)).join('<br>')}<br>${c.status==='not_recorded'?'Coordinate definition only; no result is recorded for this cell.':'Recorded campaign result for this coordinate.'}`;
  }
  function chooseWake(id, floating=false) {selectedWake=id;followLatest=false;writeUrl();renderWake();$('wake-detail').classList.toggle('floating',floating);if(floating)$('wake-inspector-title')?.focus({preventScroll:true});}
  function renderWake() {
    const wakes=data.wakes || [], w=followLatest?wakes[0]:wakes.find(w=>w.id===selectedWake);
    document.querySelectorAll('[data-wake-tab]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.wakeTab===wakeTab)));
    if(!w){$('wake-flow').innerHTML='';$('wake-detail').innerHTML=`<button class="close-wake" type="button">× Close</button><p class="empty">This wake’s trace is outside the current bounded snapshot.</p><button type="button" data-tool="history" data-tool-route="#history/${esc(selectedWake)}">Inspect the full recorded history →</button>`;return;}
    selectedWake=w.id;$('wake-story-title').textContent=followLatest?'The latest recorded wake':'Inspecting a recorded wake';
    const terminal=['accepted','rejected','failed','deferred','recovered'].includes(w.status), accepted=w.status==='accepted';
    const phases=[['Context',w.context.available?'Recorded':'Not in event tail',w.context.available],['Provider',w.attempts.length?`${w.attempts.length} attempts`:w.provider||'Not reported',Boolean(w.attempts.length)],['Proposal',w.proposal.title|| (w.proposal.actions.length?'Recorded':'Not reported'),Boolean(w.proposal.title||w.proposal.actions.length)],['Governance',terminal?w.status:'Pending',terminal],['Transition',accepted?'Accepted':terminal?'No accepted transition':'Awaiting outcome',accepted],['Receipt',w.receipt.available?`Event ${w.receipt.seq}`:'Not in event tail',w.receipt.available]];
    $('wake-flow').innerHTML=phases.map(([name,note,observed],i)=>`<button type="button" data-wake-tab="${['context','provider','summary','summary','receipt','receipt'][i]}" class="wake-phase ${observed?'observed':'unobserved'}"><span>0${i+1} / ${name}</span><strong>${esc(note)}</strong></button>`).join('');
    const story=`<div class="wake-narrative"><p><strong>${w.topic?esc(label(w.topic)):'The recorded research question'}</strong> was the focus. ${w.context.available?'WAKE received a bounded record of earlier work.':'The delivered context is outside this snapshot.'}</p><p>${w.attempts.length?`The provider made ${count(w.attempts.length)} recorded attempt${w.attempts.length===1?'':'s'}.`:'Provider attempt details are not reported.'} ${accepted?'The proposal passed governance and changed the durable record.':terminal?`The wake ended ${esc(w.status)}; it did not advance accepted research.`:'The wake has not reached a terminal outcome.'}</p>${w.reason?`<p class="story-reason">${esc(w.reason)}</p>`:''}<p class="caption">Inspect the received material, proposal summary, provider receipts and decision below.</p></div>`;
    let body='';
    if(wakeTab==='summary')body=`${badge(w.status)}<h3>${esc(w.proposal.title||'Recorded outcome')}</h3><p>${esc(w.proposal.summary||w.reason||'No summary in this event tail.')}</p><div class="action-chips">${w.proposal.actions.map(a=>`<span class="badge">${esc(a.type)}</span>`).join('')}</div><p class="caption">${accepted?'Actions passed governance and were accepted into the durable research record.':'This outcome does not count as an accepted research transition.'} Bob editorial actions remain separate.</p>`;
    if(wakeTab==='context')body=`<h3>Bounded context delivered</h3>${w.context.available?`<p>${esc(w.context.objective||'No objective field reported.')}</p><p class="caption">${count(w.context.characters)} context characters · fields: ${esc(w.context.fields.join(', '))}</p><button type="button" id="expand-context">Expand context reader ↗</button><h3>Full system text</h3><pre>${esc(w.context.system||'No system field reported.')}</pre><h3>Full recorded request</h3><pre>${esc(JSON.stringify(w.context.request,null,2)||'Full request is not reported in this older snapshot.')}</pre>`:'<p class="empty">The start event is outside this event tail. Delivered context cannot be reconstructed from this snapshot.</p>'}`;
    if(wakeTab==='response')body=`<h3>Recorded provider response</h3><p class="caption">${accepted?'Accepted proposal; the receipt records its governed transition.':'Unaccepted output. Its presence does not mean its actions were applied.'} The response is the exact text retained in this event; rejected output may have been bounded when recorded.</p>${w.response===null||w.response===undefined?'<p class="empty">Response text is outside this event tail.</p>':`<button type="button" id="expand-context">Expand response reader ↗</button><pre>${esc(w.response)}</pre>`}`;
    if(wakeTab==='provider')body=`<h3>${esc(w.provider||'Provider not reported')} / ${esc(w.model||'Model not reported')}</h3>${w.attempts.map((a,i)=>`<div class="attempt-row"><strong>Attempt ${i+1} · ${esc(a.model||'unknown')}</strong><p>${esc(a.result||'result not reported')} · ${a.elapsed_ms!==undefined?`${count(a.elapsed_ms)} ms`:'duration not reported'}</p><p class="caption">${a.request_payload_bytes!==undefined?`${count(a.request_payload_bytes)} request bytes`:'request size not reported'}${a.http_status?` · HTTP ${esc(a.http_status)}`:''}</p>${a.usage?`<pre>${esc(JSON.stringify(a.usage,null,2))}</pre>`:''}</div>`).join('')||'<p class="empty">Attempt details are not reported in this snapshot.</p>'}`;
    if(wakeTab==='receipt')body=`<h3>Durable event trace</h3><p class="record-id">Request ${esc(w.request_hash||'not reported')}<br>Terminal ${esc(w.receipt.hash||'not in event tail')}<br>Result ${esc(w.receipt.result_hash||'not reported')}</p>${w.events.map(e=>`<div class="trace-row"><span>${esc(e.kind)}</span><time>${esc(stamp(e.time))}</time><code>${esc(e.hash)}</code>${e.reason?`<p>${esc(e.reason)}</p>`:''}</div>`).join('')||'<p class="empty">Events are outside the bounded tail.</p>'}`;
    $('wake-detail').innerHTML=`<div class="wake-reader-toolbar"><button class="close-wake" type="button">× Close</button><div class="wake-tabs inspector-tabs">${["summary","context","response","provider","receipt"].map(t=>`<button type="button" data-wake-tab="${t}" aria-pressed="${t===wakeTab}">${t}</button>`).join("")}</div><h3 id="wake-inspector-title" tabindex="-1">${esc(w.id)}</h3></div>${story}<p class="caption">${esc(stamp(w.time,true))} PT → ${esc(stamp(w.finished))} · base state ${w.base_version==null?'not reported':count(w.base_version)}</p>${body}`;
    $('live-story').textContent=`Snapshot state ${count(data.version)}. Completed wakes are historical receipts; the status light separately reports execution now. Refresh checks every minute.`;
  }
  function controls() {
    document.documentElement.dataset.theme='dark';
    try{localStorage.setItem('wake-theme','dark')}catch{}
    const setMotion=()=>{cube.setMotion(motion);contextMap.setMotion(motion);document.body.dataset.motion=motion?'on':'off';$('motion-toggle').setAttribute('aria-pressed',String(motion));$('motion-toggle').textContent=motion?'Pause motion':'Resume motion';};setMotion();$('motion-toggle').onclick=()=>{motion=!motion;setMotion();};
    $('cube-left').onclick=()=>cube.rotate(-.3);$('cube-right').onclick=()=>cube.rotate(.3);$('cube-reset').onclick=()=>cube.reset();
    $('matrix-cube').addEventListener('wake-cube-select',e=>{matrixCell=e.detail;renderCell();});
    $('cube-selectors').addEventListener('change',()=>{const pos=[...document.querySelectorAll('[data-cube-axis]')].map(el=>Number(el.value));const c=data.matrix.cells.find(c=>c.position.every((v,i)=>v===pos[i]));if(c){matrixCell=c.id;cube.select(c.id);renderCell();}});
    $('context-map-canvas').addEventListener('wake-graph-select',e=>choose(e.detail,true));
    document.querySelectorAll('[data-context-view]').forEach(b=>b.onclick=()=>{contextMap.view(b.dataset.contextView);document.querySelectorAll('[data-context-view]').forEach(o=>o.setAttribute('aria-pressed',String(o===b)));});
    $('context-map-list').onclick=()=>inspectRecords('Context map records',scopedNodes(),'Select a record to inspect the relationships shown in this map.');
    document.querySelectorAll('[data-frontier-state]').forEach(b=>b.onclick=()=>{frontierState=b.dataset.frontierState;renderFrontierTable();});
    document.addEventListener('click',e=>{const t=e.target.closest('[data-story-topic]');if(t){topic=t.dataset.storyTopic;selected='';query='';writeUrl();render();inspectRecords(label(topic),scopedNodes(),'Recorded research in this topic.');}});
    $('close-data-inspector').onclick=()=>{$('data-inspector').hidden=true;};
    $('close-inspector').onclick=()=>{document.querySelector('.detail-panel').classList.remove('reader-floating');selected='';writeUrl();renderMap();renderDetail();};
    $('latest-wake').onclick=()=>{followLatest=true;selectedWake='';wakeTab='summary';writeUrl();renderWake();};
    $('show-latest-receipt').onclick=()=>{wakeTab='receipt';chooseWake(data?.wakes?.[0]?.id||'',true);};
    $('show-projects').onclick=()=>inspectRecords('Research projects',data.graph.nodes.filter(n=>n.kind==='project'),'Current projects in the bounded overview. Select one to inspect its contents and relationships.');
    document.addEventListener('click',e=>{const outcome=e.target.closest('[data-outcome]'),evidence=e.target.closest('[data-evidence-class]');if(outcome)inspectWakes(`${outcome.dataset.outcome} invocations`,(data.wakes||[]).filter(w=>w.status===outcome.dataset.outcome),`${count(data.metrics.outcomes[outcome.dataset.outcome])} across the durable record; traces are limited to the latest ${count(data.wakes?.length)} invocations.`);if(evidence){const classes={'Source-ready records':'source','Discovery leads':'discovery','Metadata records':'metadata','Runtime receipts':'receipt','Unreadable material':'unreadable','Unclassified records':'unclassified'};inspectRecords(evidence.dataset.evidenceClass,data.graph.nodes.filter(n=>n.kind==='evidence'&&n.detail.evidence_class===classes[evidence.dataset.evidenceClass]),'These are cited records in the bounded research graph; the count includes the full evidence population.');}const metric=e.target.closest('[data-metric]'),kind=e.target.closest('[data-kind]'),hour=e.target.closest('[data-hour]');if(metric)inspectMetric(metric.dataset.metric);if(kind){focusedKinds=kind.dataset.kind.split(',');const list=scopedNodes().filter(n=>focusedKinds.includes(n.kind));const i=list.findIndex(n=>n.id===selected);if(list.length)choose(list[(i+1)%list.length].id);else{renderMap();inspectRecords('No records in this category',[]);}}if(hour)inspectHour(hour.dataset.hour,true);const w=e.target.closest('[data-wake]'),tab=e.target.closest('[data-wake-tab]');if(w&&w.dataset.wake&&!w.hasAttribute('data-hour')){$('data-inspector').hidden=true;wakeTab='summary';chooseWake(w.dataset.wake,true);}if(tab){wakeTab=tab.dataset.wakeTab;writeUrl(false);renderWake();}if(e.target.closest('#expand-context')){$('wake-detail').classList.add('floating');$('wake-inspector-title')?.focus({preventScroll:true});}if(e.target.closest('.close-wake'))$('wake-detail').classList.remove('floating');});
  }


  function inspectRecords(title, nodes, note='') {
    $('data-inspector').hidden=false;
    $('data-inspector-body').innerHTML=`<h2 tabindex="-1" id="referenced-title">${esc(title)}</h2><p class="caption">${esc(note)}</p>${nodes.map(n=>`<div class="relation-row"><small>${esc(n.kind)}</small><button type="button" data-record="${esc(n.id)}">${esc(n.title)}</button></div>`).join('')||'<p class="empty">No matching records in this bounded overview.</p>'}`;
    $('referenced-title').focus({preventScroll:true});
  }
  function inspectWakes(title,wakes,note='') {
    $('data-inspector').hidden=false;
    $('data-inspector-body').innerHTML=`<h2 tabindex="-1" id="referenced-title">${esc(title)}</h2><p class="caption">${esc(note)}</p>${wakes.map(w=>`<div class="relation-row">${badge(w.status)}<button type="button" data-wake="${esc(w.id)}">${esc(w.proposal?.title||w.reason||w.id)}</button><small>${esc(stamp(w.finished||w.time,true))} PT · ${esc(w.id)}</small></div>`).join('')||'<p class="empty">No wake traces for this selection in the bounded snapshot.</p>'}`;
    $('referenced-title').focus({preventScroll:true});
  }
  function inspectMetric(metric) {
    if(metric==='latest'){chooseWake(data.status.latest?.id||'',true);return;}
    if(metric==='accepted'){inspectWakes('Accepted cycles',(data.wakes||[]).filter(w=>w.status==='accepted'),`${count(data.status.accepted_cycles)} accepted transitions across the durable record. The list shows accepted wake traces within the latest ${count(data.wakes?.length)} invocations; earlier cycles lie outside this bounded view.`);return;}
    const filter=metric==='projects'?n=>n.kind==='project'&&n.detail.status==='active':metric==='commitments'?n=>n.kind==='commitment'&&n.detail.status==='open':n=>n.detail.domain===data.status.attention_topic;
    inspectRecords(metric==='projects'?'Active projects':metric==='commitments'?'Open commitments':'Current research focus',data.graph.nodes.filter(filter),'Select a record to follow its relationships and wake receipt.');
  }
  function inspectHour(time,open=false) {
    const b=data.metrics.hourly.find(b=>b.time===time);if(!b)return;
    const note=`${stamp(time,true)} PT · ${['accepted','rejected','deferred','failed'].map(k=>`${count(b[k]||0)} ${k}`).join(' · ')}`;
    $('hour-detail').textContent=note;
    if(open){const start=Date.parse(time),end=start+3600000;inspectWakes('Completed wakes in this hour',(data.wakes||[]).filter(w=>{const t=Date.parse(w.finished||w.time);return t>=start&&t<end;}),`${note}. Wake detail is limited to the latest ${count(data.wakes?.length)} invocations.`);}
  }
  $('activity-chart').addEventListener('pointerover',e=>{const b=e.target.closest('[data-hour]');if(b)inspectHour(b.dataset.hour);});
  $('activity-chart').addEventListener('focusin',e=>{const b=e.target.closest('[data-hour]');if(b)inspectHour(b.dataset.hour);});


  function lineChart(series,names,unit='count',scrollable=false) {
    const palette={accepted:'var(--cyan)',rejected:'var(--red)',deferred:'var(--orange)',failed:'var(--red)',objectives:'var(--cyan)',constraints:'var(--green)',frontier:'var(--orange)',results:'var(--red)'};
    const colors=names.map(k=>palette[k]||'var(--cyan)');
    if(!series.length)return '<p class="empty">No recorded measurements in this snapshot.</p>';
    const chartWidth=scrollable?Math.max(960,series.length*52+60):570;
    const max=Math.max(1,...series.flatMap(p=>names.map(k=>Number(p[k]||0)))),x=i=>40+i*(chartWidth-60)/Math.max(1,series.length-1),y=v=>145-120*v/max;
    const legend=names.map((k,i)=>`<span style="color:${colors[i]}">■ ${esc(k.replaceAll('_',' '))}</span>`).join(' ');
    let svg=`<svg class="instrument-chart" viewBox="0 0 ${chartWidth} 185" ${scrollable?`style="--timeline-width:${chartWidth}px"`:""} role="img" aria-label="Recorded ${esc(names.join(', '))} in ${esc(unit)}. ${series.length} observations; maximum ${max.toFixed(1)}.">`;
    [0,.5,1].forEach(v=>{svg+=`<path class="chart-grid" d="M40 ${y(v*max)}H${chartWidth-20}"/><text x="32" y="${y(v*max)+4}" text-anchor="end">${Number((v*max).toFixed(1))}</text>`;});
    names.forEach((k,i)=>{svg+=`<path fill="none" stroke="${colors[i]}" stroke-width="1.7" ${k==='failed'?'stroke-dasharray="4 3"':''} d="${series.map((p,j)=>`${j?'L':'M'}${x(j)} ${y(p[k]||0)}`).join(' ')}"/>`;series.forEach((p,j)=>{svg+=`<circle tabindex="0" role="button" data-wake="${esc(p.id||'')}" ${p.hour?`data-hour="${esc(p.hour)}"`:''} cx="${x(j)}" cy="${y(p[k]||0)}" r="3" fill="${colors[i]}"><title>${esc(p.time)} · ${esc(k)}: ${esc(p[k]||0)} ${esc(unit)}</title></circle>`;});});
    [0,Math.floor((series.length-1)/2),series.length-1].forEach(i=>svg+=`<text x="${x(i)}" y="172" text-anchor="middle">${esc(stamp(series[i].time))}</text>`);
    return (scrollable?'<p class="timeline-scroll-hint">Scroll or swipe horizontally to inspect each hour →</p><div class="timeline-scroll" tabindex="0" role="region" aria-label="Hourly wake timeline; scroll horizontally">':'')+svg+'</svg>'+(scrollable?'</div>':'')+'<div class="instrument-key">'+legend+`</div><p class="caption">${esc(unit)} · ${esc(stamp(series[0].time,true))}–${esc(stamp(series.at(-1).time,true))} PT</p>`;
  }
  function renderFrontierTable() {
    document.querySelectorAll('[data-frontier-state]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.frontierState===frontierState)));
    if(frontierState==='rejected'){$('frontier-table').innerHTML=`<p class="caption">Recent rejected wakes; these are outcomes, not project states.</p>`+(data.wakes||[]).filter(w=>w.status==='rejected').slice(0,8).map(w=>`<div class="frontier-table-row"><button data-wake="${esc(w.id)}" type="button">${esc(w.id)}</button><span>${esc(w.reason)}</span>${badge(w.status)}<time>${esc(stamp(w.finished))}</time></div>`).join('');return;}
    const rows=data.records.projects.filter(p=>p.status===frontierState);
    $('frontier-table').innerHTML=`<div class="frontier-table-row table-label"><span>Record</span><span>Question</span><span>Status</span><span>State</span></div>`+rows.map(p=>`<div class="frontier-table-row">${pickButton('project',p,p.id)}<span>${esc(p.question||p.title)}</span>${badge(p.status)}<span>${p.updated_version==null&&p.created_version==null?'—':count(p.updated_version??p.created_version)}</span></div>`).join('')+(rows.length?'':'<p class="empty">No projects in this state. Choose another tab to follow earlier work.</p>');
  }
  function renderInstruments() {
    const wakes=[...(data.wakes||[])].reverse();
    const context=wakes.filter(w=>Object.keys(w.context_delivery||{}).length).map(w=>({id:w.id,time:w.time,delivered_request:w.context_delivery.delivered_request_chars,rich_request:w.context_delivery.rich_context_chars,ratio:w.context_delivery.request_compression_ratio}));
    const latest=context.at(-1),current=data.wakes?.[0];
    const compressionSeries=context.filter(w=>w.ratio!==undefined).map(w=>({...w,compression_pct:(1-Number(w.ratio))*100}));
    const latestCompression=latest?.ratio===undefined?null:(1-Number(latest.ratio))*100;
    const sqliteBytes=data.metrics?.storage?.sqlite_bytes;
    $('compression').innerHTML=lineChart(compressionSeries,['compression_pct'],'request reduction %')+(latest?`<div class="telemetry-values"><button type="button" data-wake="${esc(latest.id)}">Compression reduction <strong>${latestCompression===null?'Not reported':latestCompression.toFixed(1)+'%'}</strong></button><button type="button" data-wake="${esc(latest.id)}">Delivered request <strong>${count(latest.delivered_request)} chars</strong></button><button type="button" data-wake="${esc(latest.id)}">Rich request <strong>${count(latest.rich_request)} chars</strong></button><button type="button" data-wake="${esc(latest.id)}">Retained ratio <strong>${latest.ratio===undefined?'Not reported':Number(latest.ratio).toFixed(4)}</strong></button><span>SQLite database <strong>${bytes(sqliteBytes)}</strong></span></div><p class="caption">Compression reduction is the recorded size reduction from rich request to delivered request. SQLite database is the measured authoritative database file size. Size reduction alone does not establish that meaning was preserved.</p>`:`<div class="telemetry-values"><span>SQLite database <strong>${bytes(sqliteBytes)}</strong></span></div><p class="caption">No recorded compression denominator. No ratio is inferred.</p>`);
    const attempts=wakes.flatMap(w=>w.attempts.filter(a=>typeof a.elapsed_ms==='number').map(a=>({id:w.id,time:w.finished||w.time,seconds:a.elapsed_ms/1000,result:a.result,usage:a.usage||{}})));
    $('latency').innerHTML=lineChart(attempts,['seconds'],'seconds per measured provider attempt')+`<p class="caption">${count(attempts.length)} measured attempts in the latest ${count(wakes.length)} wakes. Missing duration is omitted; provider latency excludes checkpoint and governance time.</p>`;
    $('wake-timeline').innerHTML=lineChart(data.metrics.hourly.map(b=>({...b,hour:b.time})),['accepted','rejected','deferred','failed'],'completed wakes per hour',true);
    const successes=attempts.filter(a=>a.result==='success').length,avg=attempts.length?attempts.reduce((s,a)=>s+a.seconds,0)/attempts.length:null,inputs=attempts.filter(a=>typeof a.usage.promptTokenCount==='number'),outputs=attempts.filter(a=>typeof a.usage.candidatesTokenCount==='number');
    $('provider-readout').innerHTML=`<span>Measured attempts <b>${count(attempts.length)}</b></span><span>Provider success <b>${attempts.length?Math.round(100*successes/attempts.length)+'%':'Not reported'}</b></span><span>Mean latency <b>${avg===null?'Not reported':avg.toFixed(1)+'s'}</b></span><span>Reported prompt / candidate tokens <b>${inputs.length?count(inputs.reduce((s,a)=>s+a.usage.promptTokenCount,0)):'—'} / ${outputs.length?count(outputs.reduce((s,a)=>s+a.usage.candidatesTokenCount,0)):'—'}</b></span><p class="caption">Bounded measured-attempt population; token totals cover ${inputs.length} prompt / ${outputs.length} candidate usage receipts. Provider success remains separate from research acceptance.</p>`;
    const groups={objectives:['objective','mission'],constraints:['bounded_context'],frontier:['projects','research','working_notebook'],results:['notebooks','beliefs','evidence','project_evidence']};
    const evolution=wakes.filter(w=>w.context.request?.context).map(w=>{const c=w.context.request.context;return {id:w.id,time:w.time,...Object.fromEntries(Object.entries(groups).map(([name,keys])=>[name,keys.reduce((s,k)=>s+(c[k]===undefined?0:JSON.stringify(c[k]).length),0)]))};});
    $('context-evolution').innerHTML=lineChart(evolution,Object.keys(groups),'serialized characters in delivered fields')+'<p class="caption">Size of selected delivered fields, grouped by role. This shows context allocation, not importance, reasoning, or quality. Other request fields are excluded.</p>';
    const topics=data.topics.map(t=>{const types=data.metrics.by_topic[t.id]?.by_type||{},total=Object.entries(types).filter(([k])=>k!=='blog').reduce((s,[k,n])=>s+n,0);const values=data.metrics.hourly.map(bin=>wakes.filter(w=>w.topic===t.id&&w.status==='accepted'&&Date.parse(w.finished||w.time)>=Date.parse(bin.time)&&Date.parse(w.finished||w.time)<Date.parse(bin.time)+3600000).length);return {...t,total,values};}).sort((a,b)=>b.total-a.total);
    const max=Math.max(1,...topics.map(t=>t.total));
    $('top-topics').innerHTML=topics.map((t,i)=>{const peak=Math.max(1,...t.values),path=t.values.map((v,j)=>`${j?'L':'M'}${j*100/Math.max(1,t.values.length-1)} ${28-25*v/peak}`).join(' ');return `<div class="topic-ranking"><span>${i+1}</span><button data-story-topic="${esc(t.id)}" type="button">${esc(t.label)}</button><b>${count(t.total)}</b><div class="topic-bar"><i style="width:${100*t.total/max}%"></i></div><svg viewBox="0 0 100 32" role="img" aria-label="${esc(t.label)}: ${t.values.reduce((a,b)=>a+b,0)} attributed accepted wakes in trace"><path d="${path}" fill="none" stroke="var(--orange)" stroke-width="1.5"/></svg></div>`;}).join('');
    renderFrontierTable();
  }

  function choose(id,floating=false) {document.querySelector('.detail-panel').classList.toggle('reader-floating',floating);$('data-inspector').hidden=true;selected=id;writeUrl();renderMap();renderDetail();$('detail-title').focus({preventScroll:true});}
  document.addEventListener('click',event=>{const target=event.target.closest('[data-record]');if(target)choose(target.dataset.record,Boolean(target.closest('#data-inspector')));});
  document.querySelector('#outcomes').addEventListener('keydown',e=>{if(['Enter',' '].includes(e.key)&&e.target.matches('[data-outcome]')){e.preventDefault();e.target.dispatchEvent(new MouseEvent('click',{bubbles:true}));}});
  $('research-map').addEventListener('keydown',event=>{if(['Enter',' '].includes(event.key)){const target=event.target.closest('[data-record]');if(target){event.preventDefault();choose(target.dataset.record);}}});
  $('topic').addEventListener('change',()=>{topic=$('topic').value;selected='';writeUrl();renderFrontier();renderMap();renderDetail();renderSynthesis();});
  $('search').addEventListener('input',()=>{query=$('search').value;writeUrl(false);renderMap();});
  $('graph-mode').addEventListener('click',()=>{mode='graph';writeUrl();renderMap();});$('list-mode').addEventListener('click',()=>{mode='list';writeUrl();renderMap();});
  $('refresh').addEventListener('click',refresh);
  window.addEventListener('popstate',()=>{readUrl();if(data)render();});
  document.addEventListener('keydown',event=>{if(['Enter',' '].includes(event.key)&&event.target.tagName.toLowerCase()==='circle'&&event.target.matches('[data-wake],[data-hour]')){event.preventDefault();event.target.dispatchEvent(new MouseEvent('click',{bubbles:true}));}if(event.key==='Escape'){$('data-inspector').hidden=true;selected='';renderDetail();writeUrl(false);$('wake-detail').classList.remove('floating');document.querySelectorAll('.research-header details[open]').forEach(d=>{d.open=false;d.querySelector('summary').focus();});}});
  document.querySelectorAll('.research-header details').forEach(d=>d.addEventListener('toggle',()=>{if(d.open)document.querySelectorAll('.research-header details').forEach(other=>{if(other!==d)other.open=false;});}));
  document.addEventListener('click',event=>{if(!event.target.closest('.research-header details'))document.querySelectorAll('.research-header details').forEach(d=>d.open=false);});
  let resizeFrame;window.addEventListener('resize',()=>{cancelAnimationFrame(resizeFrame);resizeFrame=requestAnimationFrame(()=>{if(data)renderMap();});});
  controls();readUrl();refresh();
  setInterval(()=>{if(!document.hidden)refresh();},60000);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refresh();});
})();
