const $=s=>document.querySelector(s); let report;
const esc=s=>String(s??'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
function card(label,value){return `<article><small>${esc(label)}</small><strong>${esc(value)}</strong></article>`}
function render(r){
  report=r;
  const x=r.latest;
  if(!x){$('#brief').innerHTML='<p>No cycles found.</p>';return}
  const p=x.proposal||{};
  $('#brief').innerHTML=`<section class="grid">${card('RECORD CYCLE',r.record.version)}${card('LATEST OUTCOME',x.status)}${card('MODEL',x.model)}${card('REPEATED REASON',r.pattern.same_reason_count+' / 12')}</section><section class="feature"><small>LATEST WAKE · ${esc(x.id)}</small><h2>${esc(p.title||'No accepted proposal')}</h2><p>${esc(x.reason||p.summary||'No decision reason recorded.')}</p><p class="rec">${esc(r.recommendation)}</p></section><section class="split"><article><h2>Proposal actions</h2>${(p.actions||[]).map(a=>`<p><b>${esc(a.type)}</b> · ${esc(a.id)}<br><small>${esc((a.evidence||[]).join(', '))}</small></p>`).join('')||'<p>No proposal payload available.</p>'}</article><article><h2>Attention signals</h2><p>Trust Compacts: ${esc(x.trust_compacts?.settled_count||0)} settled / ${esc(x.trust_compacts?.candidate_count||0)} candidates</p><p>Retrieval candidates: ${esc(x.retrieval?.candidate_count||0)}</p><p>Open commitments: ${esc(r.open_commitments.length)}</p></article></section>`;
}
async function refresh(){
  $('#status').textContent='Refreshing wake-state…';
  try{
    const r=await fetch('/api/report');
    const data=await r.json();
    if(!r.ok)throw Error(data.error);
    $('#setup').hidden=true;
    render(data);
    $('#status').textContent=`Read ${data.record.event_count} events · ${data.record.integrity}`;
  }catch(e){
    $('#status').textContent='Connection needed before the record can be read.';
    $('#setup').hidden=false;
    $('#setup p').textContent=e.message;
  }
}
$('#save-path').onclick=async()=>{
  try{
    const mode=document.querySelector('input[name=source]:checked').value;
    const source=mode==='github'?{mode,repository:$('#github-repo').value,branch:$('#github-branch').value}:{mode,wake_root:$('#wake-path').value};
    const r=await fetch('/api/config',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(source)}),d=await r.json();
    if(!r.ok)throw Error(d.error);
    refresh();
  }catch(e){$('#setup p').textContent=e.message}
};
$('#refresh').onclick=refresh;
$('#opinion').onclick=async()=>{
  try{
    $('#opinion-text').textContent='Asking Gemini…';
    const r=await fetch('/api/opinion',{method:'POST'}),d=await r.json();
    if(!r.ok)throw Error(d.error);
    $('#opinion-text').textContent=d.opinion;
  }catch(e){$('#opinion-text').textContent=e.message}
};
const themeToggle=$('#theme-toggle');
if(themeToggle){
  themeToggle.checked=document.documentElement.dataset.theme==='dark';
  themeToggle.onchange=()=>{
    const dark=themeToggle.checked;
    document.documentElement.dataset.theme=dark?'dark':'';
    try{localStorage.setItem('wake-theme',dark?'dark':'light')}catch{}
  };
}
refresh();
