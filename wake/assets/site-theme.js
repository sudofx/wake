/* One preference owner across pages. Default follows the device; a deliberate
   switch is origin-local presentation only, never part of the durable record. */
(()=>{
 if(window.WakeTheme)return;
 if(document.querySelector('link[href*="console-component.css"]'))document.documentElement.dataset.consoleTheme='shared';
 const root=document.documentElement,media=matchMedia('(prefers-color-scheme: dark)'),key='wake-site-theme';
 let choice;try{choice=localStorage.getItem(key)}catch{}
 if(!['dark','light'].includes(choice))choice=null;
 const sync=()=>{
  const dark=(choice|| (media.matches?'dark':'light'))==='dark';
  root.dataset.theme=dark?'dark':'light';root.style.colorScheme=root.dataset.theme;
  document.querySelectorAll('meta[name="theme-color"]').forEach(meta=>meta.content=dark?'#000000':'#f3f6fb');
  const toggle=document.getElementById('theme-toggle');
  if(toggle){toggle.checked=dark;toggle.setAttribute('aria-label',dark?'Use light theme':'Use dark theme');toggle.closest('label').dataset.uiTooltip=`${choice?'Manual':'Following system'} ${root.dataset.theme} theme · switch to ${dark?'light':'dark'}`;}
  window.dispatchEvent(new CustomEvent('wake-theme-change',{detail:{theme:root.dataset.theme}}));
 };
 const bind=()=>{sync();document.getElementById('theme-toggle')?.addEventListener('change',event=>{choice=event.target.checked?'dark':'light';try{localStorage.setItem(key,choice)}catch{}sync();});};
 window.WakeTheme={sync};sync();
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',bind,{once:true});else bind();
 media.addEventListener('change',()=>{if(!choice)sync()});
 window.addEventListener('storage',event=>{if(event.key===key){choice=['dark','light'].includes(event.newValue)?event.newValue:null;sync();}});
})();
