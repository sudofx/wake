/*
 * WAKE✳︎ modular in-page Console workspace.
 * Presentation state only: layout preferences live in localStorage and never touch the durable record.
 */
(() => {
  'use strict';
  const params=new URL(location.href).searchParams;
  const detached=params.get('workspace')==='detached';
  const toolWindow=params.get('workspace')==='tool';
  const panelWindow=params.get('panel');
  if(/iPhone/i.test(navigator.userAgent))document.documentElement.classList.add('console-iphone');
  const poppedPanels=new Map();
  const setPanelPoppedOut=(panel,popped)=>{
    panel.classList.toggle('panel-popped-out',popped);
    const button=panel.querySelector('.panel-popout');
    if(button){
      button.textContent=popped?'↙':'↗';
      button.setAttribute('aria-label',popped?button.dataset.restoreLabel:button.dataset.popoutLabel);
      button.title=button.getAttribute('aria-label');
    }
    if(panel.dataset.consolePanelId==='014')document.documentElement.classList.toggle('console-inspector-popped-out',popped);
  };
  const restorePanel=id=>{
    const panel=document.querySelector(`[data-console-panel-id="${id}"]`);
    if(panel)setPanelPoppedOut(panel,false);
    poppedPanels.delete(id);
  };
  const announcePanel=(target=window.opener)=>{
    if(panelWindow&&target)try{target.postMessage({type:'wake-console-panel-open',id:panelWindow},location.origin);}catch{}
  };
  window.addEventListener('message',event=>{
    if(event.origin!==location.origin||!event.source)return;
    if(panelWindow){
      if(event.data?.type==='wake-console-panel-ping'&&event.data.id===panelWindow)announcePanel(event.source);
      return;
    }
    const id=event.data?.id;
    if(!['wake-console-panel-open','wake-console-panel-close'].includes(event.data?.type)||!/^\d{3}$/.test(id))return;
    const panel=document.querySelector(`[data-console-panel-id="${id}"]`);
    if(!panel)return;
    const tracked=poppedPanels.get(id);
    try{if(tracked?.window!==event.source&&event.source.opener!==window)return;}catch{return;}
    if(event.data.type==='wake-console-panel-close'){restorePanel(id);return;}
    poppedPanels.set(id,{window:event.source,ready:true});
    setPanelPoppedOut(panel,true);
  });
  if(!panelWindow)setInterval(()=>{
    poppedPanels.forEach((entry,id)=>{
      if(!entry.ready&&Date.now()>entry.expires){poppedPanels.delete(id);return;}
      let closed=false;
      try{closed=entry.window.closed;}catch{closed=true;}
      if(closed){
        restorePanel(id);
      }else try{entry.window.postMessage({type:'wake-console-panel-ping',id},location.origin);}catch{}
    });
  },500);
  if(toolWindow)return;

  if(detached){
    window.name='wake-console';
    document.documentElement.classList.add('console-detached');
  }

  const STORAGE='wake-console-workspace-v3';
  const PREVIOUS_STORAGE='wake-console-workspace-v2';
  const main=document.getElementById('main');
  const status=document.getElementById('status-band');
  const toolbar=document.querySelector('.workspace-toolbar');
  if(!main||!status)return;

  const sourceSelectors=[
    '#main > .console-overview',
    '#main > .process-field-panel',
    '.story-grid > .panel',
    '.instruments-grid > .panel',
    '.research-workspace > .panel',
    '.telemetry-grid > .panel',
    '#main > .notebook-panel'
  ];
  const panels=[...document.querySelectorAll(sourceSelectors.join(','))];
  if(!panels.length)return;

  const grid=document.createElement('section');
  grid.id='console-module-grid';
  grid.className='console-module-grid';
  grid.setAttribute('aria-label','Rearrangeable Console workspace');
  const overview=document.querySelector('.console-overview');
  if(toolbar)overview.append(toolbar);
  overview.after(grid);
  const overviewHeading=document.createElement('div');overviewHeading.className='panel-heading';
  overviewHeading.append(overview.querySelector('.eyebrow'),overview.querySelector('h1'));
  overview.prepend(overviewHeading);


  const originalParents=new Set();
  const defaultOrder=[...panels];
  const slug=text=>String(text||'panel').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,50)||'panel';
  const titleFor=panel=>panel.querySelector('h1,h2,h3')?.textContent?.trim()||panel.getAttribute('aria-label')||'Console panel';
  const brandWakeMarks=root=>{
    root.querySelectorAll('.panel-heading h1,.panel-heading h2,.panel-heading h3,.panel-heading .eyebrow').forEach(el=>{
      if(el.querySelector('.wake-inline-mark')||!el.textContent.includes('WAKE✳︎'))return;
      [...el.childNodes].forEach(node=>{
        if(node.nodeType!==Node.TEXT_NODE||!node.nodeValue.includes('WAKE✳︎'))return;
        const frag=document.createDocumentFragment(),parts=node.nodeValue.split('WAKE✳︎');
        parts.forEach((part,i)=>{if(i){const mark=document.createElement('span');mark.className='wake-inline-mark';mark.innerHTML='<span>WAKE</span><b>✳︎</b>';frag.append(mark);}frag.append(document.createTextNode(part));});
        node.replaceWith(frag);
      });
    });
  };
  brandWakeMarks(document);

  panels.forEach((panel,index)=>{
    originalParents.add(panel.parentElement);
    panel.dataset.moduleKey=panel.id||slug(titleFor(panel))||`panel-${index}`;
    panel.classList.add('console-module');
    // One slot is the minimum at every workspace width. Saved sizes override it.
    panel.dataset.span=panel===overview?'12':'1';

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
  // Give every header the same title stack and shared action row, regardless
  // of whether the original markup wrapped its label and title in a div.
  document.querySelectorAll('.panel > .panel-heading,.page-intro > .panel-heading').forEach(heading=>{
    const title=document.createElement('div');
    title.className='panel-title';
    const label=heading.querySelector('.eyebrow');
    const name=heading.querySelector('h1,h2,h3');
    if(label)title.append(label);
    if(name)title.append(name);
    [...heading.children].forEach(child=>{if(!child.childNodes.length)child.remove();});
    const actions=document.createElement('div');
    actions.className='panel-actions';
    while(heading.firstChild)actions.append(heading.firstChild);
    heading.append(title,actions);
    heading.classList.add('console-panel-heading');
  });
  const categories=document.querySelector('.map-key');
  if(categories)document.querySelector('.map-panel .panel-actions').append(categories);
  // Each numbered panel opens the same data-bound Console in an isolated view.
  document.querySelectorAll('.panel-id').forEach(label=>{
    const panel=label.closest('.panel,.page-intro');
    const id=label.textContent.match(/#(\d{3})/)?.[1];
    if(!panel||!id)return;
    panel.dataset.consolePanelId=id;
    panel.classList.toggle('console-story-panel',Number(id)>=12&&Number(id)<=18);
    const button=document.createElement('button');
    button.type='button';button.className='panel-popout';button.textContent='↗';
    button.dataset.popoutLabel=`Pop out ${titleFor(panel)} · #${id}`;
    button.dataset.restoreLabel=`Restore ${titleFor(panel)} to Console · #${id}`;
    button.setAttribute('aria-label',button.dataset.popoutLabel);
    button.title=button.dataset.popoutLabel;
    (panel.querySelector('.module-controls,.panel-actions,.snapshot')||panel).append(button);
    button.addEventListener('click',()=>{
      if(panelWindow===id){
        if(window.opener&&!window.opener.closed){
          window.opener.postMessage({type:'wake-console-panel-close',id},location.origin);
          window.opener.focus();
          window.close();
        }else{
          const url=new URL(location.href);url.searchParams.delete('panel');location.assign(url.href);
        }
        return;
      }
      const tracked=poppedPanels.get(id);
      if(tracked&&!tracked.window.closed){tracked.window.close();restorePanel(id);return;}
      const url=new URL(location.href);
      url.searchParams.delete('workspace');url.searchParams.set('panel',id);
      const opened=window.open(url.href,`wake-console-panel-${id}`,'popup=yes,width=1000,height=800');
      if(opened){
        if(!panelWindow)poppedPanels.set(id,{window:opened,ready:false,expires:Date.now()+15000});
        opened.focus();
      }else location.assign(url.href);
    });
  });
  if(panelWindow){
    const target=document.querySelector(`[data-console-panel-id="${CSS.escape(panelWindow)}"]`);
    if(target){
      if(target.matches('.detail-panel'))main.append(target);
      document.documentElement.classList.add('console-panel-window');
      target.classList.add('panel-popout-target');
      const button=target.querySelector('.panel-popout');
      if(button){button.textContent='↙';button.setAttribute('aria-label',button.dataset.restoreLabel);button.title=button.dataset.restoreLabel;}
      document.title=`${titleFor(target)} · #${panelWindow} / WAKE✳︎`;
    }
  }
  originalParents.forEach(parent=>{if(parent&&parent!==main)parent.classList.add('console-layout-source-empty');});

  const readState=()=>{
    try{
      const current=localStorage.getItem(STORAGE);
      if(current)return JSON.parse(current)||{};
      const previous=JSON.parse(localStorage.getItem(PREVIOUS_STORAGE)||'{}')||{};
      if(previous.panels){
        localStorage.setItem(STORAGE,JSON.stringify(previous));
      }
      return previous;
    }catch{return {};}
  };
  const writeState=()=>{
    if(panelWindow)return;
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
  if(!panelWindow){
    applyState();
  }

  // Count columns in the actual workspace, including every numbered panel.
  // CSS auto-placement owns rows; no stale row/column coordinates survive a resize.
  const columnCount=()=>innerWidth<768?1:Math.max(1,Math.floor((grid.clientWidth+16)/316));
  const spanToSlots=(span,cols)=>Math.max(1,Math.min(cols,Math.round(Number(span||6)*cols/12)));
  const pack=()=>{
    const cols=panelWindow?1:columnCount();
    grid.style.setProperty('--console-cols',String(cols));
    [...grid.children].forEach(panel=>{
      // The overview always fills its row, including when an older save has a narrow span.
      if(panel===overview)panel.dataset.span='12';
      panel.style.setProperty('--panel-slots',String(panel===overview?cols:spanToSlots(panel.dataset.span,cols)));
      const button=panel.querySelector('.module-size');
      if(button){
        button.disabled=cols===1||panel===overview;
        button.title=panel===overview?'Overview always fills the available row':cols===1?'Full width in this workspace':'Change panel width';
      }
    });
  };
  pack();
  new ResizeObserver(pack).observe(grid);

  grid.addEventListener('click',event=>{
    const panel=event.target.closest('.console-module');
    if(!panel)return;
    const size=event.target.closest('.module-size');
    const collapse=event.target.closest('.module-collapse');
    if(size){
      const cols=columnCount();
      if(cols===1||panel===overview)return;
      const slots=spanToSlots(panel.dataset.span,cols)%cols+1;
      panel.dataset.span=String(slots*12/cols);
      writeState();pack();
    }
    if(collapse){
      const collapsed=panel.classList.toggle('module-collapsed');
      collapse.setAttribute('aria-expanded',String(!collapsed));
      collapse.textContent=collapsed?'+':'−';
      writeState();pack();
    }
  });

  let dragging=null,placeholder=null,pointerId=null;
  const nearest=(x,y)=>{
    const candidates=[...grid.querySelectorAll('.console-module')].filter(panel=>panel!==dragging&&!panel.classList.contains('panel-popped-out'));
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
    placeholder.style.setProperty('--panel-slots',panel.style.getPropertyValue('--panel-slots'));
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
    writeState();pack();
  };
  grid.addEventListener('pointerup',finish);
  grid.addEventListener('pointercancel',finish);

  document.getElementById('reset-console-layout').addEventListener('click',()=>{
    try{localStorage.removeItem(STORAGE);localStorage.removeItem(PREVIOUS_STORAGE);localStorage.removeItem('wake-console-workspace-v1');}catch{}
    defaultOrder.forEach(panel=>{
      grid.append(panel);panel.dataset.span=panel===overview?'12':'1';panel.classList.remove('module-collapsed');
      const collapse=panel.querySelector('.module-collapse');
      if(collapse){collapse.setAttribute('aria-expanded','true');collapse.textContent='−';}
    });
    pack();writeState();
  });
  overview.querySelectorAll('.snapshot button').forEach(button=>overview.querySelector('.panel-actions').append(button));
  // Dock only a populated inspector. Pop-out releases the reservation immediately;
  // closing it restores docking without changing the saved grid order.
  const inspector=document.querySelector('.detail-panel');
  // Navigation owns visibility; the inspector only consumes that state. Never
  // reserve a fixed header gap once the shared masthead has left the viewport.
  const masthead=document.querySelector('.masthead');
  const sizeInspector=()=>{
    const edge=parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--console-edge'))||20;
    const header=masthead&&!masthead.classList.contains('masthead-scroll-hidden')?masthead.getBoundingClientRect().height:0;
    document.documentElement.style.setProperty('--inspector-top',`${header+edge}px`);
  };
  if(masthead){
    new MutationObserver(sizeInspector).observe(masthead,{attributes:true,attributeFilter:['class']});
    new ResizeObserver(sizeInspector).observe(masthead);
  }
  window.addEventListener('resize',sizeInspector);
  sizeInspector();
  const dockInspector=()=>{
    const docked=!panelWindow&&inspector.classList.contains('has-selection')&&!inspector.classList.contains('panel-popped-out');
    document.documentElement.classList.toggle('console-inspector-docked',docked);
    pack();
  };
  new MutationObserver(dockInspector).observe(inspector,{attributes:true,attributeFilter:['class']});
  dockInspector();
  if(panelWindow){announcePanel();setInterval(()=>announcePanel(),2000);}
})();
