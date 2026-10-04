/*
 * WAKE✳︎ flat-view controller.
 * Standalone pages are stable shells; current facts are loaded from flat exports
 * in the browser so publication cost does not grow with the record.
 */
(async()=>{
  'use strict';
  const root=document.getElementById('flat-content');
  const kind=document.body.dataset.flatKind;
  const source=document.body.dataset.flatSource;
  const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const response=await fetch(source,{cache:'no-store'});
  if(!response.ok)throw new Error('Published WAKE data could not be loaded');
  if(kind==='state'){
    const state=await response.json();
    root.innerHTML='<pre>'+esc(JSON.stringify(state,null,2))+'</pre>';
    return;
  }
  if(kind==='events'){
    const text=await response.text();
    const events=text.split(/\n+/).filter(Boolean).map(line=>JSON.parse(line)).reverse();
    const eventKinds=[...new Set(events.map(event=>String(event.kind||'unknown')))].sort();
    const toolsHtml=events.length?'<div class="flat-history-tools" aria-label="Filter append-only history"><label><span>SEARCH RECORD</span><input id="flat-event-search" type="search" inputmode="search" autocomplete="off" placeholder="event, ID, hash, payload…"></label><label><span>EVENT KIND</span><select id="flat-event-kind"><option value="all">ALL KINDS</option>'+eventKinds.map(value=>'<option value="'+esc(value)+'">'+esc(value.toUpperCase())+'</option>').join('')+'</select></label><div><span>VISIBLE RECEIPTS</span><strong id="flat-event-count">'+events.length+' / '+events.length+'</strong></div></div>':'';
    const eventHtml=events.map(event=>{
      const payload=event.payload||{},id=payload.id||'system',seq=String(event.seq??'');
      return '<article class="entry record-panel" id="event-'+esc(seq)+'" data-event-seq="'+esc(seq)+'" data-event-id="'+esc(id)+'" data-event-kind="'+esc(event.kind||'unknown')+'"><div class="record-panel-head"><div class="record-panel-meta"><span class="record-type">'+esc(event.kind)+'</span><span class="record-seq">EVENT '+esc(seq)+'</span><time>'+esc(event.time)+'</time></div><h3>'+esc(id)+'</h3></div><div class="record-panel-body"><pre>'+esc(JSON.stringify(payload,null,2))+'</pre><p class="subtle">Hash '+esc(event.hash)+'</p></div></article>';
    }).join('');
    root.innerHTML=toolsHtml+'<div id="flat-target-status" class="flat-target-status" role="status" hidden></div>'+(eventHtml||'<p class="empty">No recorded events.</p>')+'<p id="flat-event-empty" class="empty" hidden>No receipts match the current history filter.</p>';
    const search=document.getElementById('flat-event-search');
    const kindFilter=document.getElementById('flat-event-kind');
    const count=document.getElementById('flat-event-count');
    const empty=document.getElementById('flat-event-empty');
    const cards=[...root.querySelectorAll('[data-event-seq]')];
    const filterEvents=()=>{
      const query=String(search?.value||'').trim().toLowerCase();
      const selected=String(kindFilter?.value||'all');
      let visible=0;
      cards.forEach(card=>{
        const matchesKind=selected==='all'||card.dataset.eventKind===selected;
        const matchesQuery=!query||card.textContent.toLowerCase().includes(query);
        card.hidden=!(matchesKind&&matchesQuery);
        if(!card.hidden)visible++;
      });
      if(count)count.textContent=visible+' / '+events.length;
      if(empty)empty.hidden=visible!==0||events.length===0;
    };
    search?.addEventListener('input',filterEvents);
    kindFilter?.addEventListener('change',filterEvents);
    const focusTarget=()=>{
      root.querySelectorAll('.flat-target').forEach(node=>node.classList.remove('flat-target'));
      const status=document.getElementById('flat-target-status');
      if(status)status.hidden=true;
      let target=null,label='';
      const seqMatch=location.hash.match(/^#seq=(\d+)$/);
      const eventMatch=location.hash.match(/^#event=(.+)$/);
      if(seqMatch){
        target=root.querySelector('[data-event-seq="'+seqMatch[1]+'"]');
        label='event '+seqMatch[1];
      }else if(eventMatch){
        let wanted='';try{wanted=decodeURIComponent(eventMatch[1])}catch{wanted=eventMatch[1]}
        target=[...root.querySelectorAll('[data-event-id]')].find(node=>node.dataset.eventId===wanted)||null;
        label='record '+wanted;
      }
      if(!seqMatch&&!eventMatch)return;
      if(target?.hidden){
        if(search)search.value='';
        if(kindFilter)kindFilter.value='all';
        filterEvents();
      }
      if(status){
        status.hidden=false;
        if(target){
          const seq=Number(target.dataset.eventSeq||0);
          const ordered=[...events].sort((a,b)=>Number(a.seq||0)-Number(b.seq||0));
          const index=ordered.findIndex(event=>Number(event.seq||0)===seq);
          const previous=index>0?ordered[index-1]:null;
          const next=index>=0&&index<ordered.length-1?ordered[index+1]:null;
          status.innerHTML='<span>Located '+esc(label)+' in the append-only export.</span><nav aria-label="Adjacent receipts">'+
            (previous?'<a href="#seq='+esc(previous.seq)+'">← EVENT '+esc(previous.seq)+'</a>':'<span>← RECORD START</span>')+
            '<strong>EVENT '+esc(seq)+'</strong>'+
            (next?'<a href="#seq='+esc(next.seq)+'">EVENT '+esc(next.seq)+' →</a>':'<span>RECORD HEAD →</span>')+
            '</nav>';
        }else status.textContent='Requested '+label+' was not found in this published export.';
      }
      if(target){
        target.classList.add('flat-target');
        requestAnimationFrame(()=>target.scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'}));
      }
    };
    filterEvents();
    focusTarget();
    window.addEventListener('hashchange',focusTarget);
    return;
  }
  const data=await response.json();
  const events=(data.events||[]).filter(event=>event.kind==='rejected').reverse();
  root.innerHTML=events.map(event=>{
    const payload=event.payload||{};
    return '<article class="entry record-panel"><div class="record-panel-head"><div class="record-panel-meta"><span class="record-type">REJECTED</span><time>'+esc(event.time)+'</time></div><h3>'+esc(payload.id||'Proposal')+'</h3></div><div class="record-panel-body"><p>'+esc(payload.reason||'Rejected by governance')+'</p><pre>'+esc(JSON.stringify(payload.raw_response??payload.proposal??payload,null,2))+'</pre></div></article>';
  }).join('')||'<p class="empty">No rejected proposals in the current record.</p>';
})().catch(error=>{
  console.error(error);
  const root=document.getElementById('flat-content');
  if(root)root.innerHTML='<p class="empty">This published view could not load its flat data file.</p>';
});
