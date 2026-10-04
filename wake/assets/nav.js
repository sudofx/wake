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
  const applyActionsState=(state,title)=>{
    if(state==='running'||state==='stopped')actionsLight.dataset.state=state;
    else actionsLight.removeAttribute('data-state');
    actionsLight.title=title||'GitHub Actions';
  };
  try{
    const cached=JSON.parse(localStorage.getItem(CACHE_KEY)||'null');
    if(cached&&['running','stopped'].includes(cached.state))applyActionsState(cached.state,cached.state==='running'?'Running · last verified':'Stopped · last verified');
  }catch{}
  const refreshActionsLight=()=>{
    const latchUrl='https://api.github.com/repos/sudofx/wake/actions/workflows/wake-runner.yml?_='+Date.now();
    fetch(latchUrl,{cache:'no-store'})
      .then(response=>response.ok?response.json():Promise.reject(new Error('GitHub status unavailable')))
      .then(latch=>{
        const state=latch.state==='active'?'running':'stopped';
        applyActionsState(state,state==='running'?'Running':'Stopped');
        try{localStorage.setItem(CACHE_KEY,JSON.stringify({state,verified_at:Date.now()}));}catch{}
      })
      .catch(()=>{
        if(!actionsLight.dataset.state)applyActionsState(null,'GitHub Actions status unavailable');
      });
  };
  refreshActionsLight();
  setInterval(refreshActionsLight,120000);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refreshActionsLight();});
}
