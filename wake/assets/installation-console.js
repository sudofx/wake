/* One disposable installation manifest; record authority remains with its nodes. */
(()=>{
 'use strict';
 const dashboard=document.body.classList.contains('installation-page');
 // The asset URL identifies the export root even on nested record pages.
 const asset=new URL(document.currentScript?.src||'installation-console.js',location.href);
 const assetNode=asset.pathname.match(/^(.*\/)nodes\/([^/]+)\//);
 const nodeMatch=location.pathname.match(/^(.*\/)nodes\/([^/]+)\/(.*)$/);
 const root=new URL(assetNode?assetNode[1]:'./',asset);
 const pagePath=nodeMatch?nodeMatch[3]:location.pathname.slice(root.pathname.length);
 const currentPage=pagePath||'index.html';
 const nodeURL=id=>new URL(`nodes/${encodeURIComponent(id)}/console.html`,root);
 const viewURL=id=>{
  let page=currentPage,hash=location.hash;
  const deep=page.match(/^([^/]+)\/([^/]+)$/);
  if(deep){
   let file;try{file=decodeURIComponent(deep[2]);}catch{file=deep[2];}
   const qualified=file.match(/^([A-Za-z0-9][A-Za-z0-9._-]{0,99})::(.+)$/);
   const owner=nodeMatch?.[2]||qualified?.[1],localFile=nodeMatch?file:qualified?.[2];
   if(!id&&nodeMatch){page=`${deep[1]}/${encodeURIComponent(owner+'::'+file)}`;}
   else if(id&&owner===id&&localFile){page=`${deep[1]}/${encodeURIComponent(localFile)}`;}
   else if(id&&owner!==id){
    // A record from another node cannot be assumed to exist in this record.
    const section={notebooks:'projects',projects:'projects',questions:'projects',blog:'blog',journal:'journal',evidence:'evidence',receipts:'history'}[deep[1]];
    page=section?'index.html':'console.html';hash=section?'#'+section:'';
   }
  }
  // Reader routes use node-qualified IDs in the unified view and local IDs
  // in node views. Preserve the section when another node has no such record.
  const route=hash.match(/^#(blog|history)\/([^/]+)$/);
  if(route){
   let record;try{record=decodeURIComponent(route[2]);}catch{record=route[2];}
   const qualified=record.match(/^([A-Za-z0-9][A-Za-z0-9._-]{0,99})::(.+)$/);
   const owner=nodeMatch?.[2]||qualified?.[1],local=nodeMatch?record:qualified?.[2];
   if(id&&id===owner&&local)hash=`#${route[1]}/${encodeURIComponent(local)}`;
   else if(id&&owner&&id!==owner)hash=`#${route[1]}`;
   else if(!id&&nodeMatch)hash=record.startsWith('group-')?`#${route[1]}`:`#${route[1]}/${encodeURIComponent(owner+'::'+record)}`;
  }
  const url=new URL((id?`nodes/${encodeURIComponent(id)}/`:'')+page,root);url.search=location.search;url.hash=hash;return url;
 };
 const el=(tag,text,className)=>{const item=document.createElement(tag);if(text!==undefined)item.textContent=String(text);if(className)item.className=className;return item;};
 const get=id=>document.getElementById(id);
 const number=value=>typeof value==='number'&&Number.isFinite(value)&&value>=0?value:null;
 const count=value=>number(value)===null?'—':value.toLocaleString();
 const age=value=>{const time=Date.parse(value);if(!Number.isFinite(time))return 'age unknown';const seconds=Math.max(0,Math.floor((Date.now()-time)/1000));return seconds<60?`${seconds}s old`:seconds<3600?`${Math.floor(seconds/60)}m old`:`${Math.floor(seconds/3600)}h old`;};
 const stale=value=>!Number.isFinite(Date.parse(value))||Date.now()-Date.parse(value)>120000;
 const stamp=value=>Number.isFinite(Date.parse(value))?new Date(value).toLocaleString():'time unknown';
 const validNode=node=>node&&typeof node.id==='string'&&/^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$/.test(node.id);
 function link(node,text,invocation){const a=el('a',text);const url=nodeURL(node.id);if(invocation)url.searchParams.set('wake',invocation);a.href=url.href;return a;}
 let picker,manifest;
 function pickerIcon(node){
  const computer=!node&&Boolean(window.WAKE_DEPLOYMENT?.codespace_name);
  const path=computer?'<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>':node?'<circle cx="12" cy="5" r="3"/><circle cx="5" cy="19" r="3"/><circle cx="19" cy="19" r="3"/><path d="M12 8v4M5 16v-4h14v4"/>':'<path d="m12 3 9 5-9 5-9-5 9-5ZM3 8v9l9 5 9-5V8M12 13v9"/>';
  const icon=document.querySelector('.installation-picker-icon');if(icon)icon.innerHTML=`<svg viewBox="0 0 24 24" aria-hidden="true">${path}</svg>`;
 }
 function buildPicker(nodes){
  document.querySelectorAll('#installation-selector,.console-overview .installation-node-picker').forEach(item=>item.remove());
  const masthead=document.querySelector('body>.masthead'),host=masthead?.querySelector('.header-tools')||masthead?.querySelector('.brand-lockup');if(!host)return;
  if(!picker){const label=el('label',undefined,'installation-node-picker');label.append(el('span','Choose installation or node','installation-picker-label'),el('span',undefined,'installation-picker-icon'));picker=el('select');picker.setAttribute('aria-label','Choose installation or node');label.append(picker);host.insertBefore(label,host.querySelector('.mobile-nav-menu'));picker.addEventListener('change',()=>{location.href=viewURL(picker.value||null).href;});}
  picker.replaceChildren();
  const whole=el('option','wake');whole.value='';picker.append(whole);
  nodes.forEach(node=>{const option=el('option',`${node.role==='child'?'↳ ':''}${node.id}${node.available===false?' · unavailable':''}`);option.value=node.id;option.selected=nodeMatch?.[2]===node.id;picker.append(option);});
  if(!nodeMatch)whole.selected=true;
  pickerIcon(nodeMatch?nodes.find(node=>node.id===nodeMatch[2]):null);
  const label=get('instance-name');if(label)label.textContent=nodeMatch?nodeMatch[2]:'wake';
  const domain=masthead.querySelector('.node-domain');if(domain)domain.textContent=nodeMatch?nodeMatch[2]:'wake';
  document.documentElement.style.setProperty('--wake-masthead-height',`${masthead.getBoundingClientRect().height}px`);
 }
 function listItem(list,node,text,detail){const item=el('li');if(node)item.append(link(node,node.id),' · ');item.append(document.createTextNode(text));if(detail)item.append(el('small',detail));list.append(item);}
 function render(data){
  const nodes=data.nodes.filter(validNode).slice(0,100);buildPicker(nodes);if(!dashboard)return;
  get('installation-name').textContent='wake';
  get('installation-freshness').textContent=`${data.live===true?'Local installation snapshot':'Last uploaded data · dated snapshot'} · ${stamp(data.generated)} · ${age(data.generated)}`;
  const available=nodes.filter(n=>n.available===true&&n.research);
  const values=available.map(n=>number(n.research.status?.accepted_cycles??n.snapshot?.version));
  const total=values.every(v=>v!==null)?values.reduce((a,b)=>a+b,0):null;
  const pending=available.map(n=>n.research.status?.pending);
  const summary=get('installation-summary');summary.replaceChildren();
  [[`${available.length} / ${nodes.length}`,'Nodes with snapshots'],[count(total),`Accepted wakes · ${available.length===nodes.length?'all nodes':'available nodes only'}`],[pending.every(v=>typeof v==='boolean')?String(pending.filter(Boolean).length):'—','Nodes with pending attempts'],[data.live===true?'Local':'Mirror','Observation mode']].forEach(([value,label])=>{const cell=el('div');cell.append(el('strong',value),el('span',label));summary.append(cell);});
  const rows=get('installation-nodes'),watch=get('installation-watch'),live=get('installation-live'),receipts=get('installation-receipts');[rows,watch,live,receipts].forEach(item=>item.replaceChildren());
  if(data.live===true&&data.coordinator){const coordinator=data.coordinator,active=coordinator.active;listItem(live,null,active?`API request in flight · ${active.member||'node unknown'} · ${active.model||'model unknown'}`:'No API request in flight.',`Shared queue: ${count(coordinator.queued)} waiting. Local response processing can continue separately.`);Object.entries(coordinator.models||{}).slice(0,20).forEach(([model,state])=>{if(state.daily)listItem(watch,null,`${model} · daily quota exhausted.`,state.probe_at?`Next shared eligibility check: ${stamp(new Date(state.probe_at*1000).toISOString())}.`:'Recovery check time unavailable.');else if(state.blocked)listItem(watch,null,`${model} · access blocked.`, 'Provider access needs attention before this model can receive more calls.');else if(state.retry_at)listItem(watch,null,`${model} · temporary rate limit.`, `Eligible again: ${stamp(new Date(state.retry_at*1000).toISOString())}.`);});}
  const history=[];
  nodes.forEach(node=>{
   const research=node.research||{},snapshot=node.snapshot||{},runtime=node.runtime||{},status=research.status||{},outcomes=research.metrics?.outcomes||{};
   const known=node.available===true&&Boolean(node.research),row=el('tr');row.dataset.role=node.role;row.dataset.unavailable=String(!known);
   const name=el('td');name.append(link(node,node.id),el('small',node.role==='child'?`Child of ${node.parent||'unknown parent'}`:'Parent node'));row.append(name);
   const state=typeof runtime.state==='string'?runtime.state:'unknown';
   const outcomeText=known?['accepted','rejected','deferred','failed'].map(key=>`${key} ${count(outcomes[key])}`).join(' · '):'Unavailable';
   const snapshotCell=el('td');snapshotCell.append(el('span',known?age(snapshot.generated||research.generated):'Unavailable'));
   if(known)snapshotCell.append(el('small',`Version ${count(snapshot.version??research.version)} · head ${snapshot.head||research.head||'unknown'}`));
   [data.live===true?state:'Not live',known?count(status.accepted_cycles??snapshot.version):'—',known?(typeof status.pending==='boolean'?(status.pending?'Yes':'No'):'Unknown'):'—',outcomeText].forEach(text=>row.append(el('td',text)));row.append(snapshotCell);rows.append(row);
   if(!known){listItem(watch,node,'Snapshot unavailable.','No counts inferred; the node’s record may still exist.');return;}
   if(data.live===true&&stale(snapshot.generated||research.generated))listItem(watch,node,'Snapshot is stale or its age is unknown.',`Last export: ${stamp(snapshot.generated||research.generated)}.`);
   if(status.pending===true)listItem(watch,node,'An attempt is pending in the record.','Pending is not accepted progress or proof of an active API call.');
   const recent=Array.isArray(research.activity)?research.activity:[];
   if(recent.slice(0,3).filter(a=>a.status==='failed').length>=2)listItem(watch,node,'Multiple recent recorded failures.','Inspect the receipts to distinguish provider errors from other failures.');
   if(data.live===true){const activity=runtime.activity||{},stage=activity.stage||activity.phase;const observed=runtime.observed_at||activity.observed_at;if(stale(observed))listItem(live,node,'Current stage unavailable.',`Observation ${age(observed)}; no live activity inferred.`);else listItem(live,node,stage||state,`Sampled ${stamp(observed)} · ${age(observed)}. This is an observation, not a receipt.`);}
   const wakes=Array.isArray(research.wakes)?research.wakes:[];
   recent.slice(0,12).forEach(a=>{if(!['accepted','rejected','deferred','failed','recovered','research_planned'].includes(a.status))return;const wake=wakes.find(w=>w.id===a.id);history.push({node,id:a.id,status:a.status,time:a.time,model:a.model,receipt:wake?.receipt});});
  });
  if(!watch.children.length)listItem(watch,null,'No watch conditions in the available snapshot.','This view is bounded; it does not establish scientific support or overall system health.');
  get('installation-live-note').textContent=data.live===true?'Sampled runtime stages may lag or disappear. They do not change accepted counts.':'This public mirror contains no live execution capability. Recorded pending attempts do not imply current activity.';
  if(data.live!==true)listItem(live,null,'Live activity unavailable in a published mirror.');else if(!live.children.length)listItem(live,null,'No current node observations available.');
  history.sort((a,b)=>(Date.parse(b.time)||0)-(Date.parse(a.time)||0)).slice(0,36).forEach(a=>{const item=el('li'),details=el('div');item.append(el('span',a.status.replaceAll('_',' '),'receipt-outcome'));details.append(link(a.node,`${a.node.id} · ${a.id}`,a.id),el('small',`${stamp(a.time)}${a.model?' · '+a.model:''}`));details.append(el('small',a.receipt?.available?`Receipt ${a.receipt.seq??'sequence unknown'} · ${a.receipt.hash||'hash unavailable'}`:'Receipt details available through the node Console.'));item.append(details);receipts.append(item);});
  if(!history.length)listItem(receipts,null,'No terminal outcomes in this snapshot.');
  get('installation-provenance').textContent=`Derived installation view · ${data.installation_id||'identity unavailable'} · each row names its source snapshot. Totals add node work; they do not count independent scientific confirmations.`;
 }
 let timer;
 async function load(){
  clearTimeout(timer);
  try{const response=await fetch(new URL('installation.json',asset),{cache:'no-store',credentials:'same-origin'});if(!response.ok)throw Error(`HTTP ${response.status}`);const data=await response.json();if(data.schema!==1||!Array.isArray(data.nodes))throw Error('Unsupported installation snapshot');if(window.WAKE_DEPLOYMENT?.snapshot_only===true)data.live=false;manifest=data;window.WakeInstallationSnapshot=data;window.dispatchEvent(new CustomEvent('wake-installation-snapshot',{detail:data}));render(data);if(dashboard)get('installation-notice').hidden=true;}
  catch(error){if(dashboard){const notice=get('installation-notice');notice.hidden=false;notice.textContent=manifest?'Connection unavailable. Showing the last received snapshot; current activity is unknown.':'Installation snapshot unavailable. No node activity or counts inferred.';if(manifest){const old={...manifest,live:false};render(old);get('installation-freshness').textContent=`Disconnected · last snapshot ${stamp(manifest.generated)} · ${age(manifest.generated)}`;}}}
  if(dashboard&&window.WAKE_DEPLOYMENT?.snapshot_only!==true&&(!manifest||manifest.live===true))timer=setTimeout(load,5000);
 }
 load();
})();
