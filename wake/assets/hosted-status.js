/* Public Actions observations never enter the research transport or live canvases. */
(() => {
  const config=window.WAKE_DEPLOYMENT?.hosted_status, light=document.querySelector('.actions-light');
  if(!light || !config || !/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(config.repository || '') || config.workflow!=='research-worker.yml' || config.branch!=='master')return;
  const base=`https://api.github.com/repos/${config.repository}/actions/workflows/${config.workflow}`;
  const link=`https://github.com/${config.repository}/actions/workflows/${config.workflow}`;
  const interval=180000, key=`wake-hosted-status@1:${config.repository}`, stale=240000;
  // Safari may finish the cached installation read before this deferred script.
  // Consume the same snapshot as the node picker even when its event has passed.
  let timer, pending=false, quotaObservation=window.WakeInstallationSnapshot||null;
  // Installation snapshots contain dated node observations, not live provider calls.
  // Use them only while recent; temporary workers may stop after quota deferral.
  function confirmedQuota(){
    const data=quotaObservation;
    if(!data || data.live!==false || !Array.isArray(data.nodes) || data.nodes.length!==12)return null;
    const times=data.nodes.map(n=>Date.parse(n.recorded_runtime?.observed_at));
    if(times.some(t=>!Number.isFinite(t)||t>Date.now()+60000||Date.now()-t>30*60000))return null;
    if(!data.nodes.every(n=>{
      const state=n.recorded_runtime?.state, latest=n.research?.status?.latest;
      return (state==='standby'||(state==='stopped' && data.hosted_execution?.research_start?.ok===true)) &&
        latest?.status==='deferred' && /quota/i.test(latest.reason||'') &&
        Number.isFinite(Date.parse(latest.time)) && Date.parse(latest.time)<=Date.now()+60000 &&
        Date.now()-Date.parse(latest.time)<30*60000;
    }))return null;
    return Math.min(...times);
  }
  function confirmedRunning(value){
    const data=quotaObservation;
    // The picker reports dated snapshot states. When all twelve agree, use
    // that same aggregate even across a batch handoff or delayed upload.
    // Partial execution evidence still requires a recent, matching batch.
    if(!value?.activeRun || !data || data.live!==false ||
       !Array.isArray(data.nodes) || data.nodes.length!==12)return null;
    const allRunning=data.nodes.every(node=>node.available!==false &&
      node.recorded_runtime?.state==='running' &&
      Number.isFinite(Date.parse(node.recorded_runtime?.observed_at)) &&
      Date.parse(node.recorded_runtime.observed_at)<=Date.now()+60000);
    if(allRunning)return{count:12,checked:Math.min(...data.nodes.map(node=>Date.parse(node.recorded_runtime.observed_at)))};
    if(String(data.hosted_execution?.run_id)!==String(value.activeRun))return null;
    const running=data.nodes.filter(node=>{
      const at=Date.parse(node.recorded_runtime?.observed_at);
      return node.available!==false && node.recorded_runtime?.state==='running' &&
        Number.isFinite(at) && at<=Date.now()+60000 && Date.now()-at<30*60000;
    });
    return running.length?{count:running.length,checked:Math.min(...running.map(node=>Date.parse(node.recorded_runtime.observed_at)))}:null;
  }
  window.addEventListener('wake-installation-snapshot',event=>{
    quotaObservation=event.detail;
    const checked=confirmedQuota();
    if(checked)show('standby','All 12 nodes: confirmed provider quota standby (published observation)',checked);
    else if(!apply(cached()))show(null,'Research status unconfirmed; node observations unavailable or mixed');
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
    if(value.unavailable || (value.state===null&&!value.activeRun)){showUnavailable(value);return true;}
    const aggregate=window.WakeInstallationAggregate?.(quotaObservation);
    if(value.activeRun && aggregate && aggregate.state!=='unknown'){
      const previous=quotaObservation?.hosted_execution?.run_id &&
        String(quotaObservation.hosted_execution.run_id)!==String(value.activeRun);
      const observed=Number.isFinite(aggregate.checked)?
        '. '+(previous?'Previous batch observation ':'Published observation ')+new Date(aggregate.checked).toLocaleString():'';
      show(aggregate.state,'Hosted batch active; '+aggregate.description+observed,value.checked);return true;
    }
    const observed=confirmedQuota();
    if(observed && value.state!=='stopped' && value.state!=='blocked')show('standby','All 12 nodes: confirmed provider quota standby (published observation)',observed);
    else {
      const running=confirmedRunning(value);
      if(running)show('running',`Hosted batch active; ${running.count} of 12 nodes recorded running in its latest snapshot`,running.checked);
      else show(value.state,value.label,value.checked);
    }
    return true;
  }
  function showUnavailable(value){
    const aggregate=quotaObservation?.live===false?window.WakeInstallationAggregate?.(quotaObservation):null;
    if(aggregate && aggregate.state!=='unknown' && Number.isFinite(aggregate.checked) && aggregate.checked<=Date.now()+60000){
      show('waiting',value.label+'. Current status is unconfirmed; '+aggregate.description+
        '. Published observation '+new Date(aggregate.checked).toLocaleString(),value.checked);
    }else show(null,value.label+'; no published node status is available',value.checked);
  }
  function failureLabel(error){
    if(error?.rateLimited)return 'GitHub public status limit reached';
    if(error?.status)return 'GitHub status request failed (HTTP '+error.status+')';
    if(error?.name==='AbortError'||error?.name==='TimeoutError')return 'GitHub status request timed out';
    if(error?.name==='SyntaxError'||error?.message==='Invalid status')return 'GitHub returned unusable status data';
    return 'Could not reach GitHub to check current status';
  }
  function cached(){try{return JSON.parse(localStorage.getItem(key));}catch{return null;}}
  async function read(url){
    const controller=new AbortController(), timeout=setTimeout(()=>controller.abort(),8000);
    try{
      const response=await fetch(url,{signal:controller.signal,credentials:'omit',referrerPolicy:'no-referrer',headers:{Accept:'application/vnd.github+json'}});
      if(!response.ok){const error=new Error('GitHub status request failed');error.status=response.status;
        error.rateLimited=response.status===429||(response.status===403&&response.headers?.get?.('x-ratelimit-remaining')==='0');throw error;}
      return await response.json();
    }finally{clearTimeout(timeout);}
  }
  async function refresh(){
    clearTimeout(timer);
    if(document.hidden || pending)return;
    if(navigator.onLine===false){showUnavailable({label:'Offline; current status cannot be checked',checked:Date.now()});timer=setTimeout(refresh,interval);return;}
    const previous=cached();
    if(previous && Date.now()-previous.checked<interval && apply(previous)){
      timer=setTimeout(refresh,Math.max(1000,interval-(Date.now()-previous.checked)));return;
    }
    pending=true;
    // Never leave a green observation on screen while a new read is unresolved.
    if(!confirmedQuota())show(null,'Checking hosted execution');
    try{
      const [workflow,result]=await Promise.all([read(base),read(`${base}/runs?branch=master&per_page=5`)]);
      if(!['active','disabled_manually','disabled_inactivity','disabled_fork'].includes(workflow.state) || !Array.isArray(result.workflow_runs))throw new Error('Invalid status');
      const runs=result.workflow_runs.filter(run=>run.head_branch==='master' && run.path==='.github/workflows/research-worker.yml');
      const active=runs.find(run=>run.status==='in_progress'), queued=runs.find(run=>['queued','waiting','requested','pending'].includes(run.status));
      let state='idle',label='Between hosted batches';
      if(workflow.state!=='active'){state='stopped';label=active?'Stopping; current batch is draining':'Stopped';}
      else if(active){state='waiting';label='Hosted batch active; waiting for current node observations';}
      else if(queued){state='waiting';label='Hosted batch queued';}
      else if(!runs.length){state='waiting';label='Waiting for the first hosted batch';}
      else if(runs[0].conclusion==='action_required'){state='blocked';label='GitHub requires attention';}
      else if(runs[0].conclusion!=='success'){
        const finished=Date.parse(runs[0].updated_at);
        if(Number.isFinite(finished) && Date.now()-finished>15*60*1000){state='blocked';label='Hosted research stalled; recovery needs attention';}
        else{state='waiting';label='Waiting for automatic recovery after the last batch';}
      }
      const value={state,label,checked:Date.now(),...(workflow.state==='active' && active?{activeRun:active.id}:{})};
      try{localStorage.setItem(key,JSON.stringify(value));}catch{}
      if(!document.hidden)apply(value);
    }catch(error){
      const value={state:null,unavailable:true,label:failureLabel(error),checked:Date.now()};
      try{localStorage.setItem(key,JSON.stringify(value));}catch{}
      showUnavailable(value);
    }
    finally{pending=false;if(!document.hidden)timer=setTimeout(refresh,interval);}
  }
  window.addEventListener('offline',()=>showUnavailable({label:'Offline; current status cannot be checked',checked:Date.now()}));
  // Safari may restore a frozen page without a visibilitychange transition.
  // Reapply the bounded cache or restart its expired check on that lifecycle.
  window.addEventListener('pageshow',()=>{if(!document.hidden)refresh();});
  document.addEventListener('visibilitychange',()=>{clearTimeout(timer);if(document.hidden)show(null,'Status not checked while this page is hidden');else refresh();});
  refresh();
})();
