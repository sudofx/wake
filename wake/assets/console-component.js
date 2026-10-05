/* Internal research links stay in the parent Console's record workspace. */
(() => {
  const routes={'console-records.html':'records','console-map.html':'map','console-map3d.html':'map3d','console-events.html':'events','console-state.html':'state','console-rejected.html':'rejected','console.html':'overview'};
  const send=(tool,route='')=>{if(parent!==window)parent.postMessage({type:'wake-console-route',tool,route},location.origin);};
  document.addEventListener('click',event=>{if(parent===window)return;const link=event.target.closest('a[href]');if(!link)return;let url;try{url=new URL(link.href,location.href);}catch{return;}if(url.origin!==location.origin)return;const file=url.pathname.split('/').at(-1),tool=file==='console.html'&&url.searchParams.has('tool')?url.searchParams.get('tool'):routes[file];if(!tool)return;
    // Same-component hash navigation retains the original record renderer.
    if(file===location.pathname.split('/').at(-1)&&url.hash&&tool==='records')return;
    event.preventDefault();const part=url.hash.slice(1).split('/')[0];send(tool==='records'&&['projects','lab','evidence','history','metrics','journal','blog'].includes(part)?part:tool,url.hash);
  },true);
  const announce=()=>{const file=location.pathname.split('/').at(-1),kind=routes[file],part=location.hash.slice(1).split('/')[0];if(kind==='map'||kind==='map3d')send(kind,location.hash);else if(kind==='records'&&['projects','lab','evidence','history','metrics','journal','blog'].includes(part))send(part,location.hash);};
  for(const method of ['pushState','replaceState']){const original=history[method].bind(history);history[method]=(...args)=>{original(...args);announce();};}
  window.addEventListener('hashchange',()=>{const part=location.hash.slice(1).split('/')[0];if(routes[location.pathname.split('/').at(-1)]==='records'&&['projects','lab','evidence','history','metrics','journal','blog'].includes(part))send(part,location.hash);});
})();
