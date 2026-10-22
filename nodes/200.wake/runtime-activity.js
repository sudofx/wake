/* Optional same-origin inspection channel. It cannot authorize work or import
 * hosted data. A missing capability stays hidden; a lost connection clears all
 * live marks. Published pending invocations are historical evidence, not a pulse.
 */
window.WakeRuntimeActivityView = status => {
  const states=new Set(['running','idle','paused','stopped','waiting','standby','blocked']);
  const stages=new Set(['idle','record','context','collecting','provider_wait','provider','provider_uncoordinated','provider_response','governance','continuity','receipt']);
  if(status?.mode!=='standalone'||status.activity_schema!==1||status.capabilities?.live_activity!==true||
     typeof status.runtime_id!=='string'||!status.runtime_id||!states.has(status.state)||
     typeof status.observed_at!=='string'||!Number.isFinite(Date.parse(status.observed_at))||!stages.has(status.activity?.stage))return null;
  const active=['running','standby'].includes(status.state)&&status.activity.active===true&&status.activity.stage!=='idle';
  return {...status,activity:{...status.activity,active,
    coordinate_id:active&&['provider','provider_uncoordinated','provider_response','governance','continuity'].includes(status.activity.stage)&&
      typeof status.activity.coordinate_id==='string'?status.activity.coordinate_id:null}};
};
// Shared, disposable research data: one request and object for this document.
window.WakeViewData=(()=>{
  let current=null,pending=null,legacy=false;
  const details=new Map();
  const get=async (url,json=true)=>{const response=await fetch(url,{cache:'no-store',signal:AbortSignal.timeout(12000)});if(!response.ok){const error=Error(`HTTP ${response.status}`);error.status=response.status;throw error;}return json?response.json():response.text();};
  const overview=async()=>{
    if(legacy)return get('research-data.json');
    try{return await get('research-overview.json');}
    catch(error){if(![404,410].includes(error.status))throw error;legacy=true;return get('research-data.json');}
  };
  return {research:async (refresh=false)=>{
    if(pending)return pending;if(current&&!refresh)return current;
    pending=(async()=>{if(current){try{const head=(await get('head.txt',false)).trim();if(head===current.head)return current;}catch{}}const next=await overview();if(next?.projection_kind!=='disposable-research-view'||!next.head)throw Error('Unsupported research projection');current=next;return current;})();
    try{return await pending;}finally{pending=null;}
  },wake:async (projection,wake)=>{
    if(!wake.detail_url)return wake;
    if(!/^research-details\/[a-f0-9]{64}\.json$/.test(wake.detail_url))throw Error('Unsafe wake detail path');
    const key=wake.detail_url;
    const attach=detail=>{if(detail?.id!==wake.id||detail.request_hash!==wake.request_hash)throw Error('Wake detail does not match this snapshot');return wake.origin?{...detail,origin:wake.origin}:detail;};
    if(details.has(key))return attach(await details.get(key));
    const pendingDetail=(async()=>{
      const detail=await get(key);
      if(detail?.schema!==1||detail.wake?.id!==wake.id||detail.wake?.request_hash!==wake.request_hash)throw Error('Wake detail does not match this snapshot');
      return detail.wake;
    })();
    details.set(key,pendingDetail);
    // Long reading sessions must not retain every multi-megabyte context opened.
    if(details.size>8)details.delete(details.keys().next().value);
    try{return attach(await pendingDetail);}catch(error){details.delete(key);throw error;}
  }};
})();

// Expensive view objects are created only near the viewport or on interaction.
window.WakeLazyCanvas=(canvas,factory)=>{
  let view=null,near=false,selected='';const pending=new Map();
  const panel=canvas.closest('.panel');
  const create=()=>{if(!view){view=factory(canvas);canvas.dataset.wakeInitialized='true';}for(const [name,args] of pending)view[name]?.(...args);pending.clear();return view;};
  const initialize=()=>{if(near&&!document.hidden&&!panel?.classList.contains('module-collapsed'))create();};
  new IntersectionObserver(entries=>{near=entries[0]?.isIntersecting===true;initialize();},{rootMargin:'150px'}).observe(canvas);
  if(panel)new MutationObserver(initialize).observe(panel,{attributes:true,attributeFilter:['class']});
  document.addEventListener('visibilitychange',initialize);
  const call=(name,args,interaction=false)=>{if(interaction)create();if(view&&!document.hidden&&!panel?.classList.contains('module-collapsed'))return view[name]?.(...args);pending.set(name,args);};
  return {update:(...args)=>{const cells=args[0]?.cells;if(cells&&!cells.some(c=>c.id===selected))selected=cells.find(c=>c.position.every(v=>v===3))?.id||cells[0]?.id||'';call('update',args);return selected||undefined;},select:(...args)=>{selected=args[0];return call('select',args);},rotate:(...args)=>call('rotate',args,true),reset:(...args)=>call('reset',args,true),view:(...args)=>call('view',args,true),setMotion:(...args)=>call('setMotion',args),setActivity:(...args)=>call('setActivity',args),getRotation:()=>create().getRotation()};
};

(() => {
  const deployment=window.WAKE_DEPLOYMENT;
  const hosted=deployment?.hosted_activity;
  const remote=hosted?.url==='https://wake-live-activity.coolgrove68.chatgpt.site/activity.json'&&typeof hosted.installation_id==='string';
  if(deployment?.schema!==1||deployment.mode!=='standalone'||(deployment.snapshot_only===true&&!remote))return;
  const asset=new URL(document.currentScript?.src||'runtime-activity.js',location.href);
  const node=location.pathname.match(/\/nodes\/([^/]+)\//)?.[1];
  const root=new URL(asset.pathname.includes('/nodes/')?asset.pathname.split('/nodes/')[0]+'/':'./',asset);
  const listeners=new Set();let latest=null,stream=null,timer=null,busy=false,receivedAt=0,streamRetryAt=0;
  const view=packet=>{
    if(packet?.mode!=='installation')return packet;
    if(node)return packet.members?.find(member=>member.id===node)?.runtime||packet.legacy_node||null;
    if(!remote||packet.coordinator?.active?.confirmed!==true)return null;
    const runtime=packet.members?.find(member=>member.id===packet.coordinator.active.member)?.runtime;
    // The unified view may show a confirmed call, but its matrix is not the
    // selected worker's matrix. Only node views may animate that coordinate.
    return runtime?{...runtime,activity:{...runtime.activity,coordinate_id:null}}:null;
  };
  const publish=packet=>{latest=packet;window.WakeStatusSnapshot=packet;for(const listener of listeners)listener(packet);const status=window.WakeRuntimeActivityView(view(packet));window.WakeRuntimeActivity=status;window.dispatchEvent(new CustomEvent('wake-runtime-activity',{detail:status}));};
  window.WakeStatusChannel={root:root.href,get snapshot(){return latest;},subscribe:listener=>{listeners.add(listener);if(latest)listener(latest);return ()=>listeners.delete(listener);},view};
  const accept=packet=>{if(document.hidden){publish(null);return;}receivedAt=performance.now();publish(packet);};
  const close=()=>{stream?.close();stream=null;clearTimeout(timer);timer=null;};
  const startStream=()=>{
    if(!window.EventSource||stream||document.hidden)return;
    stream=new EventSource(new URL('runtime.events',root));
    stream.onmessage=event=>{try{const packet=JSON.parse(event.data);if(packet.mode!=='installation'||!Array.isArray(packet.members))throw Error('Unsupported status stream');accept(packet);}catch{publish(null);}};
    stream.onerror=()=>{close();streamRetryAt=performance.now()+30000;publish(null);timer=setTimeout(poll,3000);};
  };
  const fetchJSON=async url=>{const response=await fetch(url,{cache:'no-store',credentials:remote?'omit':'same-origin',referrerPolicy:'no-referrer',signal:AbortSignal.timeout(2500)});if(!response.ok)throw Error('Runtime unavailable');return response.json();};
  async function poll(){
    if(busy||document.hidden)return;busy=true;
    try{
      const packet=await fetchJSON(remote?hosted.url:new URL('runtime.json',root));
      if(remote&&(packet?.mode!=='installation'||packet.installation_id!==hosted.installation_id||!Array.isArray(packet.members)||packet.members.length!==12||!Number.isFinite(Date.parse(packet.observed_at))||Date.now()-Date.parse(packet.observed_at)>9000||Date.parse(packet.observed_at)>Date.now()+5000))throw Error('Hosted activity unavailable');
      if(packet.mode==='installation'&&node&&!Array.isArray(packet.members))packet.legacy_node=await fetchJSON(new URL('runtime.json',location.href));
      accept(packet);
      if(!remote&&packet.capabilities?.status_stream===true&&window.EventSource&&performance.now()>=streamRetryAt){startStream();return;}
    }catch{publish(null);}finally{busy=false;}
    timer=setTimeout(poll,3000);
  }
  // Same-origin embedded panels subscribe to their parent instead of opening
  // another long-lived HTTP connection. Separate browser windows own a channel.
  try{if(window.parent!==window&&window.parent.WakeStatusChannel?.root===root.href){const parent=window.parent.WakeStatusChannel;const unsubscribe=parent.subscribe(packet=>{if(document.hidden)publish(null);else accept(packet);});document.addEventListener('visibilitychange',()=>{if(document.hidden)publish(null);else if(parent.snapshot)accept(parent.snapshot);});window.addEventListener('pagehide',unsubscribe,{once:true});window.dispatchEvent(new Event('wake-status-ready'));return;}}catch{}
  window.dispatchEvent(new Event('wake-status-ready'));
  poll();
  setInterval(()=>{if(latest&&performance.now()-receivedAt>9000)publish(null);},1000);
  document.addEventListener('visibilitychange',()=>{close();publish(null);if(!document.hidden)poll();});
  window.addEventListener('pagehide',close);
})();
