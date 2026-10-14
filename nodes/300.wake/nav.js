/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Shared navigation behavior isolated from research/state logic so interaction fixes cannot alter experiment semantics.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

(() => {
  const domain=document.querySelector('.node-domain');
  if(domain&&!domain.textContent.trim())domain.textContent=location.hostname;
  const masthead=document.querySelector('body > .masthead');
  if(masthead){
    const tools=masthead.querySelector('.header-tools'),menu=masthead.querySelector('.mobile-nav-menu');
    if(tools){
      ['.actions-light','.theme-switch','.repo-link','.console-link'].forEach(selector=>{const control=masthead.querySelector(selector);if(control)tools.append(control);});
      const nodePicker=masthead.querySelector('.installation-node-picker');if(nodePicker)tools.append(nodePicker);
      if(menu){menu.querySelector('summary').setAttribute('aria-label','Open main menu');tools.append(menu);}
    }
    const reserveHeader=()=>document.documentElement.style.setProperty('--wake-masthead-height',`${masthead.getBoundingClientRect().height}px`);
    reserveHeader();
    new ResizeObserver(reserveHeader).observe(masthead);
  }
  const nav = document.querySelector('.compact-nav');
  if (!nav) return;
  const groups = () => [...(masthead||nav).querySelectorAll('.nav-group')];
  const menuScope=masthead||nav;
  function close(except) {
    groups().forEach(group => { if (group !== except) group.open = false; });
  }
  // Node navigation is added after the installation manifest arrives.
  menuScope.addEventListener('toggle', event => {
    const group=event.target;if(group.matches('.nav-group')&&group.open)close(group);
  }, true);
  menuScope.addEventListener('click', event => {
    if (event.target.closest('a')) close();
  });
  menuScope.addEventListener('keydown', event => {
    const open = groups().find(group => group.open);
    if (event.key === 'Escape' && open) {
      event.preventDefault();
      event.stopPropagation();
      close();
      open.querySelector('summary').focus();
    }
  });
  document.addEventListener('focusin', event => {
    if (!menuScope.contains(event.target)) close();
  });
  document.addEventListener('click', event => {
    if (!menuScope.contains(event.target)) close();
  });
  window.addEventListener('hashchange', () => close());
})();

const actionsLight=document.querySelector('.actions-light');
// Unknown installation identity must not display GitHub's status as local status.
if(actionsLight && window.WAKE_DEPLOYMENT?.snapshot_only===true){
  document.documentElement.dataset.wakeSnapshotOnly='true';
  actionsLight.hidden=true;
}
if(actionsLight && window.WAKE_DEPLOYMENT?.mode!=='hosted' && window.WAKE_DEPLOYMENT?.snapshot_only!==true){
  actionsLight.href='runtime.json';
  const applyLocal=status=>{
    const label=status.state==='standby'?(status.reason||'Provider quota reported; retrying on the regular schedule'):
      ({running:'Running',waiting:'Waiting',idle:'Idle',paused:'Paused',stopped:'Stopped',blocked:'Blocked'})[status.state]||'Unknown';
    actionsLight.dataset.state=status.state==='running'?'running':status.state==='paused'?'stopped':status.state;
    actionsLight.title='Local WAKE · '+label;
    actionsLight.setAttribute('aria-label','Inspect local WAKE runtime · '+label);
  };
  const unavailable=()=>{actionsLight.removeAttribute('data-state');actionsLight.title='Local runtime unavailable';actionsLight.setAttribute('aria-label','Local runtime unavailable');};
  const refreshLocal=()=>fetch(new URL('runtime.json',location.href),{cache:'no-store'}).then(r=>{if(!r.ok)throw new Error('Unavailable');return r.json();}).then(applyLocal).catch(unavailable);
  // Activity is optional. Losing that capability is not proof the runtime is offline.
  window.addEventListener('wake-runtime-activity',event=>{if(event.detail)applyLocal(event.detail);else refreshLocal();});
  refreshLocal();setInterval(refreshLocal,30000);
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
    if(button.matches('.panel-popout'))return [button.closest('.panel-popout-target,.panel-popped-out')?'↙':'↗',button.getAttribute('aria-label')];
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
    if(title){if(element.dataset.uiTooltip!==title)element.dataset.uiTooltip=title;element.removeAttribute('title');}
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
    owner=element;if(tooltip.textContent!==text)tooltip.textContent=text;tooltip.hidden=false;
    const ids=new Set((element.getAttribute('aria-describedby')||'').split(/\s+/).filter(Boolean));ids.add(tooltip.id);element.setAttribute('aria-describedby',[...ids].join(' '));
    const rect=element.getBoundingClientRect(),box=tooltip.getBoundingClientRect();
    tooltip.style.left=`${Math.max(8,Math.min(innerWidth-box.width-8,rect.left+rect.width/2-box.width/2))}px`;
    tooltip.style.top=`${rect.bottom+8+box.height<innerHeight?rect.bottom+8:Math.max(8,rect.top-box.height-8)}px`;
  }
  let touchTimer=null,touchOwner=null,touchShown=false,lastTouch=null;
  const cancelTouch=()=>{clearTimeout(touchTimer);touchTimer=null;touchOwner=null;};
  document.addEventListener('pointerdown',event=>{
    if(event.pointerType!=='touch')return;
    cancelTouch();touchShown=false;touchOwner=event.target;lastTouch=event.target;
    touchTimer=setTimeout(()=>{show(touchOwner);touchShown=Boolean(owner);},450);
  });
  document.addEventListener('pointerup',()=>{cancelTouch();if(touchShown)setTimeout(hide,2500);});
  document.addEventListener('pointercancel',()=>{cancelTouch();hide();});
  document.addEventListener('pointermove',event=>{if(event.pointerType==='touch'&&!touchShown)cancelTouch();});
  document.addEventListener('click',event=>{if(touchShown||(lastTouch===event.target&&event.target.closest('.actions-light'))){event.preventDefault();event.stopPropagation();show(event.target);touchShown=false;setTimeout(hide,2500);}else hide();lastTouch=null;},true);
  document.addEventListener('pointerover',event=>{if(event.pointerType!=='touch')show(event.target);});
  document.addEventListener('pointerout',event=>{if(event.pointerType!=='touch'&&owner&&!owner.contains(event.relatedTarget))hide();});
  document.addEventListener('focusin',event=>show(event.target));
  document.addEventListener('focusout',hide);

  document.addEventListener('keydown',event=>{if(event.key==='Escape')hide();});
  window.addEventListener('scroll',hide,true);window.addEventListener('resize',hide);
  new MutationObserver(changes=>{
    for(const change of changes){
      if(change.type==='attributes')scan(change.target);
      else {if(change.target.matches?.('button'))decorate(change.target);change.addedNodes.forEach(scan);}
    }
    if(owner&&(!owner.isConnected||owner.closest('[hidden]')))hide();
    else if(owner)show(owner);
  }).observe(document.body,{subtree:true,childList:true,attributes:true,attributeFilter:['title','aria-label','aria-pressed','class','data-ui-tooltip']});
})();

// Recorded links stay within this installation on LAN and a Pages subpath.
for(const link of document.querySelectorAll('[data-record-url]')){
  const path=location.pathname,root=path.includes('/nodes/')?path.split('/nodes/')[0]+'/':path.split('/blog/')[0]+'/';
  link.href=root+link.dataset.recordUrl.replace(/^\//,'');
}
