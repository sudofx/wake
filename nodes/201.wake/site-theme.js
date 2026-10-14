/* System theme owns presentation when detectable. Manual choice is a fallback
   for browsers that cannot report a light or dark system preference. */
(()=>{
 if(window.WakeTheme)return;
 if(document.querySelector('link[href*="console-component.css"]'))document.documentElement.dataset.consoleTheme='shared';
 const root=document.documentElement,key='wake-site-theme';
 let darkMedia,lightMedia;
 try{if(typeof matchMedia==='function'){darkMedia=matchMedia('(prefers-color-scheme: dark)');lightMedia=matchMedia('(prefers-color-scheme: light)');}}catch{}
 let choice;try{choice=localStorage.getItem(key)}catch{}
 if(!['dark','light'].includes(choice))choice=null;
 const sync=()=>{
  const detected=Boolean(darkMedia?.matches||lightMedia?.matches);
  root.dataset.systemTheme=detected?'detected':'unavailable';
  const dark=detected?Boolean(darkMedia.matches):choice==='dark';
  root.dataset.theme=dark?'dark':'light';root.style.colorScheme=root.dataset.theme;
  document.querySelectorAll('meta[name="theme-color"]').forEach(meta=>meta.content=dark?'#000000':'#f3f6fb');
  const toggle=document.getElementById('theme-toggle');
  if(toggle){toggle.checked=dark;toggle.setAttribute('aria-label',dark?'Use light theme':'Use dark theme');const label=toggle.closest('label');if(label){label.hidden=detected;label.dataset.uiTooltip=`${detected?'Following system':'Manual'} ${root.dataset.theme} theme · switch to ${dark?'light':'dark'}`;}}
  window.dispatchEvent(new CustomEvent('wake-theme-change',{detail:{theme:root.dataset.theme}}));
 };
 const bind=()=>{sync();document.getElementById('theme-toggle')?.addEventListener('change',event=>{choice=event.target.checked?'dark':'light';try{localStorage.setItem(key,choice)}catch{}sync();});};
 window.WakeTheme={sync};sync();
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',bind,{once:true});else bind();
 for(const media of [darkMedia,lightMedia]){if(media?.addEventListener)media.addEventListener('change',sync);else media?.addListener?.(sync);}
 window.addEventListener('storage',event=>{if(event.key===key){choice=['dark','light'].includes(event.newValue)?event.newValue:null;sync();}});
})();
