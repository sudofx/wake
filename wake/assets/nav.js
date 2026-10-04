/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Shared navigation behavior isolated from research/state logic so interaction fixes cannot alter experiment semantics.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

(() => {
  const nav = document.querySelector('.compact-nav');
  if (!nav) return;
  const groups = [...nav.querySelectorAll('.nav-group')];
  function close(except) {
    groups.forEach(group => { if (group !== except) group.open = false; });
  }
  groups.forEach(group => {
    group.addEventListener('toggle', () => { if (group.open) close(group); });
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) close();
  });
  nav.addEventListener('keydown', event => {
    const open = groups.find(group => group.open);
    if (event.key === 'Escape' && open) {
      event.preventDefault();
      event.stopPropagation();
      close();
      open.querySelector('summary').focus();
    }
  });
  document.addEventListener('focusin', event => {
    if (!nav.contains(event.target)) close();
  });
  document.addEventListener('click', event => {
    if (!nav.contains(event.target)) close();
  });
  window.addEventListener('hashchange', () => close());
})();

const actionsLight=document.querySelector('.actions-light');
if(actionsLight){
  const CACHE_KEY='wake-actions-light-state';
  const CACHE_FRESH_MS=90000;
  const REFRESH_MS=180000;
  const CAMPAIGN_ACTIVE=new Set(['queued','in_progress','waiting','requested','pending']);
  const validState=state=>['running','stopped','campaign'].includes(state);
  const stateTitle=(state,suffix='')=>{
    const base=state==='campaign'?'Continuity campaign':state==='running'?'Running':state==='stopped'?'Stopped':'Status unavailable';
    return suffix?`${base} · ${suffix}`:base;
  };
  const applyActionsState=(state,title)=>{
    if(validState(state))actionsLight.dataset.state=state;
    else actionsLight.removeAttribute('data-state');
    const message=title||'Status unavailable';
    actionsLight.title=message;
    actionsLight.setAttribute('aria-label',`Open WAKE GitHub Actions · ${message}`);
    const label=actionsLight.querySelector('.actions-light-label');
    if(label)label.textContent=state==='campaign'?'Campaign':state==='running'?'Running':state==='stopped'?'Stopped':'Status';
  };
  const readCached=()=>{
    try{
      const cached=JSON.parse(localStorage.getItem(CACHE_KEY)||'null');
      return cached&&validState(cached.state)&&Number.isFinite(Number(cached.verified_at))?cached:null;
    }catch{return null;}
  };
  const applyCached=(cached,suffix='last verified')=>{
    if(!cached)return false;
    applyActionsState(cached.state,stateTitle(cached.state,suffix));
    return true;
  };
  const initial=readCached();
  if(initial)applyCached(initial);
  const remember=(state)=>{
    const cached={state,verified_at:Date.now()};
    applyActionsState(state,stateTitle(state));
    try{localStorage.setItem(CACHE_KEY,JSON.stringify(cached));}catch{}
  };
  const fetchJson=url=>fetch(url,{cache:'no-store'}).then(response=>response.ok?response.json():Promise.reject(new Error('GitHub status unavailable')));
  const refreshActionsLight=(force=false)=>{
    if(document.hidden&&!force)return;
    const cached=readCached();
    if(!force&&cached&&Date.now()-Number(cached.verified_at)<CACHE_FRESH_MS){
      applyCached(cached);
      return;
    }
    const stamp=Date.now();
    const latchUrl='https://api.github.com/repos/sudofx/wake/actions/workflows/wake-runner.yml?_='+stamp;
    const campaignUrl='https://api.github.com/repos/sudofx/wake/actions/workflows/operator-enable-continuity.yml/runs?per_page=10&_='+stamp;
    fetchJson(latchUrl)
      .then(latch=>{
        if(latch.state==='active'){
          remember('running');
          return null;
        }
        return fetchJson(campaignUrl).then(campaign=>{
          const active=(campaign.workflow_runs||[]).some(run=>CAMPAIGN_ACTIVE.has(run.status));
          remember(active?'campaign':'stopped');
          return null;
        });
      })
      .catch(()=>{
        // A transport/rate-limit failure must not contradict a state already
        // verified by another WAKE page. Yellow is reserved for "never verified".
        const fallback=readCached();
        if(!applyCached(fallback,'last verified · refresh unavailable')){
          applyActionsState(null,'GitHub Actions status unavailable');
        }
      });
  };
  refreshActionsLight();
  setInterval(refreshActionsLight,REFRESH_MS);
  window.addEventListener('storage',event=>{
    if(event.key!==CACHE_KEY||!event.newValue)return;
    try{
      const cached=JSON.parse(event.newValue);
      if(cached&&validState(cached.state))applyCached(cached);
    }catch{}
  });
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refreshActionsLight();});
}


/* DETACHABLE CONSOLE LINKS — 2026-10-04 */
(() => {
  if (location.pathname.endsWith('/console.html')) return;
  let consoleWindow=null,workspaceWindow=null;
  const openConsole=(href)=>{
    const url=new URL(href,location.href);
    const isWorkspace=url.searchParams.has('tool');
    url.searchParams.set('workspace',isWorkspace?'tool':'detached');
    const width=Math.max(isWorkspace?900:980,Math.min(isWorkspace?1480:1560,(screen.availWidth||1440)-(isWorkspace?110:80)));
    const height=Math.max(isWorkspace?680:720,Math.min(isWorkspace?1040:1100,(screen.availHeight||900)-(isWorkspace?110:80)));
    const left=Math.max(0,Math.round(((screen.availWidth||width)-width)/2)+(isWorkspace?24:0));
    const top=Math.max(0,Math.round(((screen.availHeight||height)-height)/2)+(isWorkspace?24:0));
    const features=`popup=yes,width=${width},height=${height},left=${left},top=${top},resizable=yes,scrollbars=yes`;
    const name=isWorkspace?'wake-console-workspace':'wake-console';
    const opened=window.open(url.href,name,features);
    if(isWorkspace)workspaceWindow=opened;else consoleWindow=opened;
    if(opened)opened.focus();
    else location.href=url.href;
  };
  const desktopPointer=()=>window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  document.addEventListener('click',event=>{
    if(event.defaultPrevented||event.button>0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
    const link=event.target.closest('a[href]');
    if(!link)return;
    let url;try{url=new URL(link.href,location.href);}catch{return;}
    if(url.origin!==location.origin||!url.pathname.endsWith('/console.html'))return;
    // Pop the console out only for a desktop-style mouse/trackpad UI.
    // Touch/coarse-pointer devices follow the normal link in the same window.
    if(!desktopPointer())return;
    event.preventDefault();
    openConsole(url.href);
  },true);
})();
