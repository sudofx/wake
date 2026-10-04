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
  const refreshActionsLight=()=>{
    const bust='?_='+Date.now();
    const latchUrl='https://api.github.com/repos/sudofx/wake/actions/workflows/wake-runner.yml'+bust;
    const runsUrl='https://api.github.com/repos/sudofx/wake/actions/workflows/wake.yml/runs?branch=wake-runtime&per_page=10&_='+Date.now();
    Promise.all([
      fetch(latchUrl,{cache:'no-store'}).then(response=>response.ok?response.json():Promise.reject()),
      fetch(runsUrl,{cache:'no-store'}).then(response=>response.ok?response.json():Promise.reject()),
    ])
      .then(([latch,runs])=>{
        const enabled=latch.state==='active';
        const activeCycle=(runs.workflow_runs||[]).some(run=>run.status!=='completed');
        actionsLight.dataset.state=enabled?'running':'stopped';
        actionsLight.title=enabled?(activeCycle?'Running':'Running · between cycles'):'Stopped';
      })
      .catch(()=>{
        actionsLight.removeAttribute('data-state');
        actionsLight.title='GitHub Actions';
      });
  };
  refreshActionsLight();
  setInterval(refreshActionsLight,15000);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refreshActionsLight();});
}
