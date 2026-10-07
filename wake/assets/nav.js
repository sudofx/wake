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
if(actionsLight && window.WAKE_STANDALONE){
  actionsLight.href='/runtime.json';
  const refreshLocal=()=>fetch('/runtime.json',{cache:'no-store'}).then(r=>{if(!r.ok)throw new Error('Unavailable');return r.json();}).then(status=>{
    const label=status.state==='running'?'Running':status.state==='waiting'?'Waiting':'Paused';
    actionsLight.dataset.state=status.state==='paused'?'stopped':'running';
    actionsLight.title='Local WAKE · '+label;
    actionsLight.setAttribute('aria-label','Inspect local WAKE runtime · '+label);
    const text=actionsLight.querySelector('.actions-light-label');if(text)text.textContent=label;
  }).catch(()=>{actionsLight.removeAttribute('data-state');actionsLight.title='Local runtime unavailable';});
  refreshLocal();setInterval(refreshLocal,30000);
}
if(actionsLight && !window.WAKE_STANDALONE){
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

/* Shared action glyphs and previews. Record names and metric values remain content. */
(() => {
  const icons={
    refresh:['↻','Refresh record'], 'reset-console-layout':['↺','Reset Console view'],
    'process-field-reset':['↺','Reset process field view'],
    'cube-left':['↶','Rotate cube left'], 'cube-right':['↷','Rotate cube right'], 'cube-reset':['↺','Reset cube view'],
    'latest-wake':['◷','Inspect latest wake'], 'close-inspector':['×','Close record inspector'],
    'close-data-inspector':['×','Close referenced records'], 'show-projects':['□','Inspect projects'],
    'show-latest-receipt':['▤','Inspect latest receipt'], 'expand-context':['⤢','Expand reader'],
    clear:['×','Clear selection'], 'clear-detail':['×','Clear selection'], 'back-detail':['↶','Back up'],
    'zoom-in-detail':['+','Zoom in'], 'zoom-out-detail':['−','Zoom out'],
    'open-map-window':['↗','Open map window'], 'history-more':['↓','More events'],
    'help-close':['×','Close explanation']
  };
  const tabs={summary:'≡',context:'▧',response:'↩',provider:'◇',receipt:'▤'};
  const states={active:'▷',completed:'✓',parked:'Ⅱ',rejected:'×'};
  function action(button){
    if(button.id==='global-motion-toggle')return [button.getAttribute('aria-pressed')==='true'?'◉':'▷',button.getAttribute('aria-pressed')==='true'?'Disable presentation motion':'Enable presentation motion'];
    if(icons[button.id])return icons[button.id];
    const panelName=button.closest('.console-module')?.querySelector('h2')?.textContent.trim()||'panel';
    if(button.matches('.module-drag'))return ['⠿',`Move ${panelName}`];
    if(button.matches('.module-size'))return ['↔',`Resize ${panelName}`];
    if(button.matches('.module-collapse'))return [button.closest('.module-collapsed')?'+':'−',`${button.closest('.module-collapsed')?'Expand':'Collapse'} ${panelName}`];
    if(button.matches('.close-wake'))return ['×','Close wake reader'];
    if(button.matches('.panel-popout'))return ['↗',button.getAttribute('aria-label')];
    if(button.matches('.wake-tabs button'))return [tabs[button.dataset.wakeTab]||'≡',`Inspect ${button.dataset.wakeTab}`];
    if(button.dataset.contextView)return [button.dataset.contextView==='sphere'?'◉':'◇',`${button.dataset.contextView==='sphere'?'Sphere':'3D'} context view`];
    if(button.dataset.frontierState)return [states[button.dataset.frontierState],`${button.dataset.frontierState} frontier`];
    if(button.dataset.kind)return [{project:'□',research:'◇',notebook:'▤',evidence:'●','belief,commitment':'△'}[button.dataset.kind],button.dataset.uiLabel||button.textContent.trim()];
    if(button.matches('.help-trigger'))return ['?',button.getAttribute('aria-label')];
    if(button.matches('.detail-links button, #wake-detail button[data-tool]'))return [button.hasAttribute('data-wake')?'◷':'↗',button.dataset.uiLabel||button.textContent.trim()];
    // Existing glyph-only controls retain their symbols and accessible names.
    if(button.getAttribute('aria-label')&&button.childElementCount===0&&button.textContent.trim().length>0&&button.textContent.trim().length<=3)return [button.textContent.trim(),button.getAttribute('aria-label')];
    return null;
  }
  const tooltip=document.createElement('div');
  tooltip.id='site-tooltip';tooltip.setAttribute('role','tooltip');tooltip.hidden=true;
  document.body.append(tooltip);
  let owner=null;
  function decorate(element){
    if(element===tooltip||element.tagName==='IFRAME'||element.closest('#node-popover,.constellation-node'))return;
    const icon=element.tagName==='BUTTON'?action(element):null;
    if(icon){
      const [glyph,label]=icon;
      if(!element.classList.contains('glyph-button'))element.classList.add('glyph-button');
      if(element.dataset.uiLabel!==label)element.dataset.uiLabel=label;
      if(element.getAttribute('aria-label')!==label)element.setAttribute('aria-label',label);
      if(element.dataset.uiTooltip!==label)element.dataset.uiTooltip=label;
      if(element.textContent!==glyph)element.textContent=glyph;
    }
    const title=element.getAttribute('title');
    if(title){element.dataset.uiTooltip=title;element.removeAttribute('title');}
    const svgTitle=element.matches('svg [role="button"]')?element.querySelector('title'):null;
    if(svgTitle){element.dataset.uiTooltip=svgTitle.textContent;svgTitle.remove();}
  }
  function scan(root){
    if(root.nodeType!==1)return;
    decorate(root);
    root.querySelectorAll('button,[title],svg [role="button"]').forEach(decorate);
  }
  scan(document.body);
  function hide(){
    if(owner){const ids=(owner.getAttribute('aria-describedby')||'').split(/\s+/).filter(id=>id&&id!==tooltip.id);if(ids.length)owner.setAttribute('aria-describedby',ids.join(' '));else owner.removeAttribute('aria-describedby');}
    tooltip.hidden=true;owner=null;
  }
  function show(target){
    const element=target.closest('[data-ui-tooltip],button[aria-label],a[aria-label],summary[aria-label]');
    if(!element||element.closest('.constellation-node,#node-popover')||element.disabled)return hide();
    const text=element.dataset.uiTooltip||element.getAttribute('aria-label');
    if(!text)return hide();
    if(owner!==element)hide();
    owner=element;tooltip.textContent=text;tooltip.hidden=false;
    const ids=new Set((element.getAttribute('aria-describedby')||'').split(/\s+/).filter(Boolean));ids.add(tooltip.id);element.setAttribute('aria-describedby',[...ids].join(' '));
    const rect=element.getBoundingClientRect(),box=tooltip.getBoundingClientRect();
    tooltip.style.left=`${Math.max(8,Math.min(innerWidth-box.width-8,rect.left+rect.width/2-box.width/2))}px`;
    tooltip.style.top=`${rect.bottom+8+box.height<innerHeight?rect.bottom+8:Math.max(8,rect.top-box.height-8)}px`;
  }
  document.addEventListener('pointerover',event=>show(event.target));
  document.addEventListener('pointerout',event=>{if(owner&&!owner.contains(event.relatedTarget))hide();});
  document.addEventListener('focusin',event=>show(event.target));
  document.addEventListener('focusout',hide);
  document.addEventListener('click',hide);
  document.addEventListener('keydown',event=>{if(event.key==='Escape')hide();});
  window.addEventListener('scroll',hide,true);window.addEventListener('resize',hide);
  new MutationObserver(changes=>{
    for(const change of changes){
      if(change.type==='attributes')scan(change.target);
      else {if(change.target.matches?.('button'))decorate(change.target);change.addedNodes.forEach(scan);}
    }
    if(owner&&(!owner.isConnected||owner.closest('[hidden]')))hide();
  }).observe(document.body,{subtree:true,childList:true,attributes:true,attributeFilter:['title','aria-label','aria-pressed','class']});
})();
