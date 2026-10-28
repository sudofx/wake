/* Public Actions observations never enter the research transport or live canvases. */
(() => {
  const config=window.WAKE_DEPLOYMENT?.hosted_status, light=document.querySelector('.actions-light');
  if(!light || !config || !/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(config.repository || '') || config.workflow!=='research-worker.yml' || config.branch!=='master')return;
  const base=`https://api.github.com/repos/${config.repository}/actions/workflows/${config.workflow}`;
  const link=`https://github.com/${config.repository}/actions/workflows/${config.workflow}`;
  const interval=180000, key=`wake-hosted-status@1:${config.repository}`, stale=240000;
  let timer, pending=false, quotaObservation=null;
  // Installation snapshots contain dated node observations, not live provider calls.
  // Use them only while recent, and only if all twelve independently report standby.
  function confirmedQuota(){
    const data=quotaObservation;
    if(!data || data.live!==false || !Array.isArray(data.nodes) || data.nodes.length!==12)return null;
    const times=data.nodes.map(n=>Date.parse(n.recorded_runtime?.observed_at));
    if(times.some(t=>!Number.isFinite(t)||t>Date.now()+60000||Date.now()-t>30*60000))return null;
    if(!data.nodes.every(n=>n.recorded_runtime?.state==='standby' && /quota/i.test(n.research?.status?.latest?.reason||'')))return null;
    return Math.min(...times);
  }
  window.addEventListener('wake-installation-snapshot',event=>{
    quotaObservation=event.detail;
    const checked=confirmedQuota();
    if(checked)show('standby','All 12 nodes: confirmed provider quota standby (published observation)',checked);
  });
  light.hidden=false;light.href=link;
  function show(state,label,checked){
    if(state)light.dataset.state=state;else light.removeAttribute('data-state');
    const age=checked?` Checked ${new Date(checked).toLocaleTimeString()}.`:'';
    const text=`GitHub research · ${label}.${age} Batch status includes restoration, quota waits and publication; it does not report a live provider call or accepted progress.`;
    light.title=text;light.setAttribute('aria-label',text);
  }
  function apply(value){
    if(!value || !Number.isFinite(value.checked) || Date.now()-value.checked>stale || value.checked>Date.now()+5000)return false;
    const observed=confirmedQuota();
    if(observed)show('standby','All 12 nodes: confirmed provider quota standby (published observation)',observed);
    else show(value.state,value.label,value.checked);
    return true;
  }
  function cached(){try{return JSON.parse(localStorage.getItem(key));}catch{return null;}}
  async function read(url){
    const controller=new AbortController(), timeout=setTimeout(()=>controller.abort(),8000);
    try{
      const response=await fetch(url,{signal:controller.signal,credentials:'omit',referrerPolicy:'no-referrer',headers:{Accept:'application/vnd.github+json'}});
      if(!response.ok)throw new Error('Status unavailable');
      return await response.json();
    }finally{clearTimeout(timeout);}
  }
  async function refresh(){
    clearTimeout(timer);
    if(document.hidden || pending)return;
    if(navigator.onLine===false){show(null,'Offline; status unavailable');timer=setTimeout(refresh,interval);return;}
    const previous=cached();
    if(previous && Date.now()-previous.checked<interval && apply(previous)){
      timer=setTimeout(refresh,Math.max(1000,interval-(Date.now()-previous.checked)));return;
    }
    pending=true;
    // Never leave a green observation on screen while a new read is unresolved.
    show(null,'Checking hosted execution');
    try{
      const [workflow,result]=await Promise.all([read(base),read(`${base}/runs?branch=master&per_page=5`)]);
      if(!['active','disabled_manually','disabled_inactivity','disabled_fork'].includes(workflow.state) || !Array.isArray(result.workflow_runs))throw new Error('Invalid status');
      const runs=result.workflow_runs.filter(run=>run.head_branch==='master' && run.path==='.github/workflows/research-worker.yml');
      const active=runs.find(run=>run.status==='in_progress'), queued=runs.find(run=>['queued','waiting','requested','pending'].includes(run.status));
      let state='idle',label='Between hosted batches';
      if(workflow.state!=='active'){state='stopped';label=active?'Stopping; current batch is draining':'Stopped';}
      else if(active){state=null;label='Hosted batch active; research state unconfirmed';}
      else if(queued){state='waiting';label='Hosted batch queued';}
      else if(!runs.length){state='waiting';label='Waiting for the first hosted batch';}
      else if(runs[0].conclusion==='action_required'){state='blocked';label='GitHub requires attention';}
      else if(runs[0].conclusion!=='success'){
        const finished=Date.parse(runs[0].updated_at);
        if(Number.isFinite(finished) && Date.now()-finished>15*60*1000){state='blocked';label='Hosted research stalled; recovery needs attention';}
        else{state='waiting';label='Waiting for automatic recovery after the last batch';}
      }
      const value={state,label,checked:Date.now()};
      try{localStorage.setItem(key,JSON.stringify(value));}catch{}
      if(!document.hidden)apply(value);
    }catch{
      const value={state:null,label:'Status unavailable; open GitHub for details',checked:Date.now()};
      try{localStorage.setItem(key,JSON.stringify(value));}catch{}
      show(null,value.label,value.checked);
    }
    finally{pending=false;if(!document.hidden)timer=setTimeout(refresh,interval);}
  }
  window.addEventListener('offline',()=>show(null,'Offline; status unavailable'));
  document.addEventListener('visibilitychange',()=>{clearTimeout(timer);if(document.hidden)show(null,'Status not checked while this page is hidden');else refresh();});
  refresh();
})();
