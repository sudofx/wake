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
 function pickerIcon(){
  const icon=document.querySelector('.installation-picker-icon');
  if(icon)icon.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="5" r="3"/><circle cx="5" cy="19" r="3"/><circle cx="19" cy="19" r="3"/><path d="M12 8v4M5 16v-4h14v4"/></svg>';
 }
 const stateNames={running:'Running',waiting:'Waiting',idle:'Idle',paused:'Paused',stopped:'Stopped',standby:'Waiting for provider',blocked:'Blocked',unavailable:'Unavailable',unknown:'Unknown',mixed:'Mixed node states'};
 function pickerState(node,data){
  if(data.disconnected)return {state:'unknown',description:'Current status unavailable; connection lost'};
  if(data.live===true){
   const runtime=node.runtime||{},state=stateNames[runtime.state]?runtime.state:'unknown';
   return {state,description:`Current status: ${stateNames[state]}`};
  }
  const runtime=node.recorded_runtime||{},raw=stateNames[runtime.state]?runtime.state:'unknown';
  const latest=node.research?.status?.latest, observed=Date.parse(runtime.observed_at), attempted=Date.parse(latest?.time);
  // Hosted disposable workers can exit after a quota deferral. Do not equate
  // worker exit with operator-stop when the captured start was acknowledged.
  const quota=data.hosted_execution?.research_start?.ok===true && raw==='stopped' &&
    latest?.status==='deferred' && /quota/i.test(latest.reason||'') &&
    Number.isFinite(observed) && observed<=Date.now()+60000 && Date.now()-observed<30*60000 &&
    Number.isFinite(attempted) && attempted<=Date.now()+60000 && Date.now()-attempted<30*60000;
  const state=quota?'standby':raw;
  return {state,description:quota?`Last uploaded research: Provider quota standby; worker stopped · observed ${stamp(runtime.observed_at)}`:
    state==='unknown'?'No uploaded status available':`Last uploaded status: ${stateNames[state]} · observed ${stamp(runtime.observed_at)}`};
 }
 function aggregateStatus(data){
  const nodes=(data?.nodes||[]).filter(validNode),states=nodes.map(node=>pickerState(node,data));
  // Idle workers do not cancel active work elsewhere in the installation.
  // Gray is reserved for unavailable observations, not differing known states.
  const priority=['blocked','running','waiting','standby','paused','stopped','idle'];
  const state=data?.disconnected?'unknown':priority.find(value=>states.some(item=>item.state===value))||'unknown';
  const counts=priority.map(value=>{const count=states.filter(item=>item.state===value).length;return count?`${count} ${stateNames[value].toLowerCase()}`:null;}).filter(Boolean);
  const times=nodes.map(node=>Date.parse((data.live===true?node.runtime:node.recorded_runtime)?.observed_at)).filter(Number.isFinite);
  return{state,description:`${data.live===true?'Current node states':'Last uploaded node states'}: ${counts.join(', ')||'unavailable'}`,checked:times.length?Math.min(...times):null};
 }
 window.WakeInstallationAggregate=aggregateStatus;
 function buildPicker(nodes,data){
  const label=get('instance-name');if(label)label.textContent=nodeMatch?nodeMatch[2]:'wake';
  const domain=document.querySelector('body>.masthead .node-domain');if(domain)domain.textContent=nodeMatch?nodeMatch[2]:'wake';
  if(currentPage!=='console.html')return;
  document.querySelectorAll('#installation-selector,.console-overview .installation-node-picker').forEach(item=>item.remove());
  const masthead=document.querySelector('body>.masthead'),host=masthead?.querySelector('.header-tools')||masthead?.querySelector('.brand-lockup');if(!host)return;
  if(!picker){
   const menu=el('details',undefined,'nav-group installation-node-picker');
   const summary=el('summary');summary.setAttribute('aria-label','Choose installation or node');
   summary.append(el('span','Choose installation or node','installation-picker-label'),el('span',undefined,'installation-picker-icon'));
   picker=el('div',undefined,'nav-dropdown installation-node-menu');menu.append(summary,picker);
   host.insertBefore(menu,host.querySelector('.mobile-nav-menu'));
   picker.addEventListener('click',event=>{const choice=event.target.closest('a[data-node]');if(choice)choice.href=viewURL(choice.dataset.node||null).href;});
  }
  const states=nodes.map(node=>pickerState(node,data));
  const whole=aggregateStatus(data);
  const rows=[{id:'',text:'wake',status:whole||{state:'unknown',description:'Status unavailable'}},...nodes.map((node,index)=>({id:node.id,text:`${node.role==='child'?'↳ ':''}${node.id}${node.available===false?' · unavailable':''}`,status:states[index]}))];
  const current=[...picker.children];
  // Steady polling updates lights without replacing focused menu links.
  const same=current.length===rows.length&&current.every((a,index)=>a.dataset.node===rows[index].id);
  if(!same)picker.replaceChildren(...rows.map(row=>{const a=el('a');a.dataset.node=row.id;const light=el('span',undefined,'installation-node-status');light.setAttribute('aria-hidden','true');a.append(light,el('span',row.text,'installation-node-name'));return a;}));
  rows.forEach((row,index)=>{const a=picker.children[index],name=a.querySelector('.installation-node-name');if(name.textContent!==row.text)name.textContent=row.text;a.href=viewURL(row.id||null).href;a.querySelector('.installation-node-status').dataset.state=row.status.state;a.setAttribute('aria-label',`${row.text} · ${row.status.description}`);a.dataset.uiTooltip=`${row.text} · ${row.status.description}`;if((nodeMatch?.[2]||'')===row.id)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
  pickerIcon(nodeMatch?nodes.find(node=>node.id===nodeMatch[2]):null);
  document.documentElement.style.setProperty('--wake-masthead-height',`${masthead.getBoundingClientRect().height}px`);
 }
 function listItem(list,node,text,detail){const item=el('li');if(node)item.dataset.node=node.id;if(node)item.append(link(node,node.id),' · ');item.append(document.createTextNode(text));if(detail)item.append(el('small',detail));list.append(item);}
 function render(data){
  const nodes=data.nodes.filter(validNode).slice(0,100);buildPicker(nodes,data);if(!dashboard)return;
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
 let timer,refreshTimer,loading=false,statusConnected=false,lastStatusShape='',lastExportHead='';
 const connectStatus=()=>{
  if(statusConnected||!window.WakeStatusChannel)return;statusConnected=true;
  window.WakeStatusChannel.subscribe(packet=>{
   if(!manifest||manifest.live!==true)return;
   if(!packet){lastStatusShape='';render({...manifest,live:false,disconnected:true});return;}
   if(!Array.isArray(packet.members)||(packet.installation_id&&packet.installation_id!==manifest.installation_id))return;
   clearTimeout(timer);
   const fresh=new Map(packet.members.map(member=>[member.id,member]));
   const data={...manifest,live:true,coordinator:packet.coordinator,disconnected:false,nodes:manifest.nodes.map(node=>({...node,runtime:fresh.get(node.id)?.runtime||{state:'unavailable'}}))};
   const shape=data.nodes.map(node=>`${node.id}:${node.runtime.runtime_id||''}:${node.runtime.state}:${node.runtime.activity?.stage||''}:${node.runtime.activity?.active}`).join('|')+JSON.stringify(packet.coordinator||{});
   manifest=data;window.WakeInstallationSnapshot=data;
   if(shape!==lastStatusShape){lastStatusShape=shape;render(data);}else{buildPicker(data.nodes,data);if(dashboard)for(const node of data.nodes){const note=get('installation-live').querySelector(`li[data-node="${node.id}"] small`),observed=node.runtime.observed_at;if(note)note.textContent=stale(observed)?`Observation ${age(observed)}; no live activity inferred.`:`Sampled ${stamp(observed)} · ${age(observed)}. This is an observation, not a receipt.`;}}
   if(lastExportHead&&packet.head&&packet.head!==lastExportHead&&!refreshTimer){const refresh=()=>{if(loading){refreshTimer=setTimeout(refresh,3000);return;}refreshTimer=null;load();};refreshTimer=setTimeout(refresh,3000);}if(packet.head)lastExportHead=packet.head;
  });
 };
 async function load(){
  if(loading)return;loading=true;
  clearTimeout(timer);
  try{const response=await (window.WakePublicData?.fetch || fetch)(new URL('installation.json',asset),{cache:'no-store',credentials:'same-origin'});if(!response.ok)throw Error(`HTTP ${response.status}`);const data=await response.json();if(data.schema!==1||!Array.isArray(data.nodes))throw Error('Unsupported installation snapshot');if(window.WAKE_DEPLOYMENT?.snapshot_only===true)data.live=false;manifest=data;window.WakeInstallationSnapshot=data;window.dispatchEvent(new CustomEvent('wake-installation-snapshot',{detail:data}));render(data);if(dashboard)get('installation-notice').hidden=true;}
  catch(error){
   if(manifest)render({...manifest,live:false,disconnected:true});
   if(dashboard){const notice=get('installation-notice');notice.hidden=false;notice.textContent=manifest?'Connection unavailable. Showing the last received snapshot; current activity is unknown.':'Installation snapshot unavailable. No node activity or counts inferred.';if(manifest)get('installation-freshness').textContent=`Disconnected · last snapshot ${stamp(manifest.generated)} · ${age(manifest.generated)}`;}
  }
  loading=false;
  const shared=window.WakeStatusSnapshot?.members;
  if(window.WAKE_DEPLOYMENT?.snapshot_only!==true&&(!manifest||manifest.live===true)&&!Array.isArray(shared))timer=setTimeout(load,5000);
 }
 window.addEventListener('wake-status-ready',connectStatus);connectStatus();
 load();
})();
