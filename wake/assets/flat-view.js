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
    root.innerHTML=events.map(event=>{
      const payload=event.payload||{},id=payload.id||'system';
      return '<details class="entry record-panel"><summary class="record-panel-head"><div class="record-panel-meta"><span class="record-type">'+esc(event.kind)+'</span><time>'+esc(event.time)+'</time></div><h3>'+esc(id)+'</h3></summary><div class="record-panel-body"><pre>'+esc(JSON.stringify(payload,null,2))+'</pre><p class="subtle">Hash '+esc(event.hash)+'</p></div></details>';
    }).join('')||'<p class="empty">No recorded events.</p>';
    const closeEventDetails=()=>root.querySelectorAll('details.entry').forEach(item=>{item.open=false});
    closeEventDetails();
    window.addEventListener('pageshow',closeEventDetails);
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
