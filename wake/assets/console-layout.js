/*
 * WAKE✳︎ modular in-page Console workspace.
 * Presentation state only: layout preferences live in localStorage and never touch the durable record.
 */
(() => {
  'use strict';
  const params=new URL(location.href).searchParams;
  const detached=params.get('workspace')==='detached';
  const toolWindow=params.get('workspace')==='tool';
  if(toolWindow)return;

  if(detached){
    window.name='wake-console';
    document.documentElement.classList.add('console-detached');
  }

  const STORAGE='wake-console-workspace-v1';
  const main=document.getElementById('main');
  const status=document.getElementById('status-band');
  const toolbar=document.querySelector('.workspace-toolbar');
  if(!main||!status)return;

  const sourceSelectors=[
    '.story-grid > .panel',
    '.instruments-grid > .panel',
    '.research-workspace > .panel:not(.detail-panel)',
    '.telemetry-grid > .panel',
    '#main > .notebook-panel'
  ];
  const panels=[...document.querySelectorAll(sourceSelectors.join(','))];
  if(!panels.length)return;

  const grid=document.createElement('section');
  grid.id='console-module-grid';
  grid.className='console-module-grid';
  grid.setAttribute('aria-label','Rearrangeable Console workspace');
  (toolbar||status).after(grid);

  const originalParents=new Set();
  const slug=text=>String(text||'panel').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,50)||'panel';
  const titleFor=panel=>panel.querySelector('h2,h3')?.textContent?.trim()||panel.getAttribute('aria-label')||'Console panel';
  panels.forEach((panel,index)=>{
    originalParents.add(panel.parentElement);
    panel.dataset.moduleKey=panel.id||slug(titleFor(panel))||`panel-${index}`;
    panel.classList.add('console-module');
    const defaults=panel.matches('.map-panel,.notebook-panel,.process-field-panel')?12:
      panel.matches('.frontier-panel,.detail-panel,.evidence-panel,.outcomes-panel')?4:
      6;
    panel.dataset.span=String(defaults);

    let heading=panel.querySelector(':scope > .panel-heading');
    if(!heading){
      heading=document.createElement('div');
      heading.className='panel-heading console-generated-heading';
      heading.innerHTML=`<div><p class="eyebrow">WORKSPACE / MODULE</p><h2>${titleFor(panel)}</h2></div>`;
      panel.prepend(heading);
    }
    const controls=document.createElement('div');
    controls.className='module-controls';
    controls.innerHTML=`
      <button class="module-drag" type="button" aria-label="Drag ${titleFor(panel)}" title="Drag to rearrange">⠿</button>
      <button class="module-size" type="button" aria-label="Resize ${titleFor(panel)}" title="Change panel width">↔</button>
      <button class="module-collapse" type="button" aria-expanded="true" aria-label="Collapse ${titleFor(panel)}" title="Collapse panel">−</button>`;
    heading.append(controls);
    grid.append(panel);
  });
  originalParents.forEach(parent=>{if(parent&&parent!==main)parent.classList.add('console-layout-source-empty');});

  const readState=()=>{
    try{return JSON.parse(localStorage.getItem(STORAGE)||'{}')||{};}catch{return {};}
  };
  const writeState=()=>{
    const state={
      order:[...grid.children].map(panel=>panel.dataset.moduleKey),
      panels:Object.fromEntries([...grid.children].map(panel=>[
        panel.dataset.moduleKey,
        {span:Number(panel.dataset.span||6),collapsed:panel.classList.contains('module-collapsed')}
      ]))
    };
    try{localStorage.setItem(STORAGE,JSON.stringify(state));}catch{}
  };
  const applyState=()=>{
    const state=readState();
    const byKey=new Map([...grid.children].map(panel=>[panel.dataset.moduleKey,panel]));
    (state.order||[]).forEach(key=>{const panel=byKey.get(key);if(panel)grid.append(panel);});
    [...grid.children].forEach(panel=>{
      const saved=state.panels?.[panel.dataset.moduleKey];
      if(saved?.span)panel.dataset.span=String(saved.span);
      if(saved?.collapsed){
        panel.classList.add('module-collapsed');
        const button=panel.querySelector('.module-collapse');
        if(button){button.setAttribute('aria-expanded','false');button.textContent='+';}
      }
    });
  };
  applyState();

  const spanCycle=[4,6,8,12];
  grid.addEventListener('click',event=>{
    const panel=event.target.closest('.console-module');
    if(!panel)return;
    const size=event.target.closest('.module-size');
    const collapse=event.target.closest('.module-collapse');
    if(size){
      const current=Number(panel.dataset.span||6),idx=spanCycle.indexOf(current);
      panel.dataset.span=String(spanCycle[(idx+1)%spanCycle.length]);
      writeState();
    }
    if(collapse){
      const collapsed=panel.classList.toggle('module-collapsed');
      collapse.setAttribute('aria-expanded',String(!collapsed));
      collapse.textContent=collapsed?'+':'−';
      writeState();
    }
  });

  let dragging=null,placeholder=null,pointerId=null;
  const nearest=(x,y)=>{
    const candidates=[...grid.querySelectorAll('.console-module')].filter(panel=>panel!==dragging);
    if(!candidates.length)return null;
    return candidates.reduce((best,panel)=>{
      const r=panel.getBoundingClientRect(),cx=r.left+r.width/2,cy=r.top+r.height/2;
      const d=(cx-x)**2+(cy-y)**2;
      return !best||d<best.d?{panel,d,r}:best;
    },null);
  };
  grid.addEventListener('pointerdown',event=>{
    const handle=event.target.closest('.module-drag');
    if(!handle)return;
    const panel=handle.closest('.console-module');
    if(!panel)return;
    event.preventDefault();
    pointerId=event.pointerId;
    handle.setPointerCapture(pointerId);
    dragging=panel;
    placeholder=document.createElement('div');
    placeholder.className='console-module-placeholder';
    placeholder.dataset.span=panel.dataset.span||'6';
    panel.after(placeholder);
    panel.classList.add('module-dragging');
    document.body.classList.add('console-is-dragging');
  });
  grid.addEventListener('pointermove',event=>{
    if(!dragging||event.pointerId!==pointerId)return;
    event.preventDefault();
    const hit=nearest(event.clientX,event.clientY);
    if(!hit)return;
    const before=event.clientY<hit.r.top+hit.r.height/2 ||
      (Math.abs(event.clientY-(hit.r.top+hit.r.height/2))<hit.r.height*.25 && event.clientX<hit.r.left+hit.r.width/2);
    grid.insertBefore(placeholder,before?hit.panel:hit.panel.nextSibling);
  });
  const finish=event=>{
    if(!dragging||event.pointerId!==pointerId)return;
    placeholder.replaceWith(dragging);
    dragging.classList.remove('module-dragging');
    document.body.classList.remove('console-is-dragging');
    dragging=null;placeholder=null;pointerId=null;
    writeState();
  };
  grid.addEventListener('pointerup',finish);
  grid.addEventListener('pointercancel',finish);

  const toolbarRow=document.createElement('div');
  toolbarRow.className='console-workspace-controls';
  toolbarRow.innerHTML=`<span>${detached?'DETACHED WORKSPACE':'CONSOLE WORKSPACE'}</span><div class="console-workspace-actions"><button id="reset-console-layout" type="button">Reset layout</button></div>`;
  status.before(toolbarRow);
  toolbarRow.querySelector('#reset-console-layout').addEventListener('click',()=>{
    try{localStorage.removeItem(STORAGE);}catch{}
    location.reload();
  });
})();
;(()=>{
  const button=document.getElementById('global-motion-toggle');
  if(!button)return;
  let enabled=false;
  const apply=()=>{
    button.setAttribute('aria-pressed',String(enabled));
    button.textContent='Motion';
    button.title=enabled?'Disable presentation motion':'Enable presentation motion';
    document.documentElement.dataset.motion=enabled?'on':'off';
    window.dispatchEvent(new CustomEvent('wake-global-motion',{detail:{enabled}}));
  };
  button.addEventListener('click',()=>{enabled=!enabled;apply();});
  apply();
})();
