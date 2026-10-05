/* Console deep tools open as real browser pages, never an in-page mobile workspace. */
window.WakeConsoleTools = () => {
  const files={projects:'console-records.html',lab:'console-records.html',evidence:'console-records.html',history:'console-records.html',metrics:'console-records.html',journal:'console-records.html',blog:'console-records.html',records:'console-records.html',map:'console-map.html',map3d:'console-map3d.html',events:'console-events.html',state:'console-state.html',rejected:'console-rejected.html'};
  const desktopPointer=()=>window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const destination=(tool,hash='')=>{
    if(!(tool in files))return null;
    const route=hash||(['map','map3d','events','state','rejected'].includes(tool)?'':`#${tool==='records'?'projects':tool}`);
    return new URL(files[tool]+route,location.href);
  };
  const open=(tool,hash='')=>{
    const url=destination(tool,hash);
    if(!url)return;
    // iPhone/iPad/touch devices stay in a normal full browser page. No iframe,
    // popup-sized window, or embedded workspace.
    if(!desktopPointer()){location.assign(url.href);return;}
    // The 3D map owns a dedicated viewport-filling desktop pop-out.
    const isMap=tool==='map3d';
    if(isMap)url.searchParams.set('popout','1');
    const opened=isMap
      ?window.open(url.href,'wake-map3d','popup=yes,width='+Math.min(1500,Math.max(320,screen.availWidth-80))+',height='+Math.min(1000,Math.max(320,screen.availHeight-80)))
      :window.open(url.href,'wake-console-workspace');
    if(opened)opened.focus();
    else location.assign(url.href);
  };
  document.addEventListener('click',event=>{
    const control=event.target.closest('[data-tool]');
    if(!control)return;
    event.preventDefault();
    open(control.dataset.tool,control.dataset.toolRoute||'');
  });
  // Old bookmarked Console workspace URLs resolve directly to the real tool page.
  const initial=new URL(location.href).searchParams;
  if(initial.get('tool'))open(initial.get('tool'),initial.get('tool_route')||'');
  return {open};
};
