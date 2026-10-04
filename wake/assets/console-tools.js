/* Complete record/map renderers are components of Console, loaded on demand. */
window.WakeConsoleTools = () => {
  const panel=document.getElementById('console-tools'),frame=document.getElementById('console-tool-frame');
  const files={projects:'console-records.html',lab:'console-records.html',evidence:'console-records.html',history:'console-records.html',metrics:'console-records.html',journal:'console-records.html',blog:'console-records.html',records:'console-records.html',map:'console-map.html',map3d:'console-map3d.html',events:'console-events.html',state:'console-state.html',rejected:'console-rejected.html'};
  let active='',route='',workspaceWindow=null;
  const workspaceMode=new URL(location.href).searchParams.get('workspace');
  const syncTheme=()=>{try{frame.contentDocument.documentElement.dataset.theme=document.documentElement.dataset.theme||'dark';}catch{}};
  const popWorkspace=(tool,hash='')=>{
    const url=new URL('console.html',location.href);
    url.searchParams.set('workspace','tool');
    url.searchParams.set('tool',tool);
    if(hash)url.searchParams.set('tool_route',hash);
    const width=Math.max(900,Math.min(1480,(screen.availWidth||1400)-110));
    const height=Math.max(680,Math.min(1040,(screen.availHeight||900)-110));
    const left=Math.max(0,Math.round(((screen.availWidth||width)-width)/2)+24);
    const top=Math.max(0,Math.round(((screen.availHeight||height)-height)/2)+24);
    workspaceWindow=window.open(url.href,'wake-console-workspace',`popup=yes,width=${width},height=${height},left=${left},top=${top},resizable=yes,scrollbars=yes`);
    if(workspaceWindow)workspaceWindow.focus();
    else location.href=url.href;
  };
  function open(tool,hash='',push=true){
    if(!(tool in files))return;
    const resolved=hash||(['map','map3d','events','state','rejected'].includes(tool)?'':`#${tool==='records'?'projects':tool}`);
    if(workspaceMode!=='tool'){popWorkspace(tool,resolved);return;}
    active=tool;route=resolved;panel.hidden=false;document.getElementById('console-tool-title').textContent=({map:'Recorded relationship map',map3d:'Full 3D record map',events:'Exact event history',state:'Durable state',rejected:'Rejected & withheld drafts'})[tool]||`${tool[0].toUpperCase()+tool.slice(1)} / full record`;
    document.querySelectorAll('[data-tool]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.tool===tool)));
    let currentFile='';try{currentFile=frame.contentWindow.location.pathname.split('/').at(-1);}catch{}if(currentFile===files[tool])frame.contentWindow.location.hash=route;else frame.src=files[tool]+route;
    const page=new URL(location.href);page.searchParams.set('tool',tool);if(route)page.searchParams.set('tool_route',route);else page.searchParams.delete('tool_route');if(page.href!==location.href)history[push?'pushState':'replaceState'](null,'',page);syncTheme();
  }
  function close(push=true){
    if(workspaceMode==='tool'){window.close();return;}
    panel.hidden=true;active='';frame.src='about:blank';const url=new URL(location.href);url.searchParams.delete('tool');url.searchParams.delete('tool_route');if(url.href!==location.href)history[push?'pushState':'replaceState'](null,'',url);
  }
  document.addEventListener('click',e=>{const b=e.target.closest('[data-tool]');if(b){e.preventDefault();open(b.dataset.tool,b.dataset.toolRoute||'');}});
  document.getElementById('close-console-tools').onclick=()=>close();frame.addEventListener('load',syncTheme);
  window.addEventListener('message',e=>{if(e.origin!==location.origin||e.source!==frame.contentWindow||e.data?.type!=='wake-console-route')return;if(e.data.tool==='overview')close();else open(e.data.tool,e.data.route||'',false);});
  new MutationObserver(syncTheme).observe(document.documentElement,{attributes:true,attributeFilter:['data-theme']});
  window.addEventListener('popstate',()=>{const p=new URL(location.href).searchParams;if(p.get('tool'))open(p.get('tool'),p.get('tool_route')||'',false);else close(false);});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!panel.hidden)close();});
  const initial=new URL(location.href).searchParams;if(initial.get('tool'))open(initial.get('tool'),initial.get('tool_route')||'',false);
  return {open,close};
};
