/*
 * WAKE✳︎ shared operator controls.
 * Presentation/auth only: this file never receives provider credentials and never
 * mutates durable state directly. It talks only to the confidential control Worker.
 */
(() => {
  const controlUrl=window.WakeControlUrl||'';
  const ownerAccess=document.querySelector('[data-owner-access]');
  const ownerLogin=document.querySelector('[data-owner-login]');
  const ownerControls=document.querySelector('[data-owner-controls]');
  const ownerStatus=document.querySelector('[data-owner-control-status]');
  const ownerMenuToggle=document.querySelector('[data-owner-menu-toggle]');
  const ownerMenuLabel=document.querySelector('[data-owner-menu-label]');
  const ownerIdentity=document.querySelector('[data-owner-identity]');
  const ownerStart=document.querySelector('[data-owner-start]');
  const ownerStop=document.querySelector('[data-owner-stop]');
  const ownerReset=document.querySelector('[data-owner-reset]');
  const ownerSignout=document.querySelector('[data-owner-signout]');
  if(!ownerAccess||!ownerLogin)return;

  const sessionKey='wake-owner-session';
  const fragment='#wake-control=';
  let publicCycle=Number(document.querySelector('.cycle-count')?.textContent)||0;
  try{
    if(!localStorage.getItem(sessionKey)){
      const legacy=sessionStorage.getItem(sessionKey);
      if(legacy)localStorage.setItem(sessionKey,legacy);
    }
    sessionStorage.removeItem(sessionKey);
  }catch{}

  if(controlUrl && location.hash.startsWith(fragment)){
    try{
      localStorage.setItem(sessionKey,decodeURIComponent(location.hash.slice(fragment.length)));
      history.replaceState(null,'',location.pathname+location.search);
    }catch{}
  }

  const session=()=>{try{return localStorage.getItem(sessionKey)||''}catch{return ''}};
  const setOwnerLight=state=>{ownerAccess.dataset.lightState=state};
  const syncPublic=data=>{
    publicCycle=Number(data?.public_cycle??data?.state?.version??data?.meta?.version??0);
    if(!session())setOwnerLight(publicCycle>0?'running':'idle');
  };
  window.WakeOperatorSyncPublic=syncPublic;

  const setOwnerMenu=open=>{
    if(ownerControls)ownerControls.hidden=!open;
    ownerMenuToggle?.setAttribute('aria-expanded',String(open));
  };
  const showSignedOut=(message='')=>{
    setOwnerMenu(false);
    if(ownerMenuToggle)ownerMenuToggle.hidden=true;
    ownerLogin.hidden=false;
    ownerLogin.setAttribute('aria-label',message?`Open Settings. Last error: ${message}`:'Open Settings');
    ownerLogin.setAttribute('title','Settings');
    if(ownerIdentity)ownerIdentity.textContent='Signed out';
    setOwnerLight(publicCycle>0?'running':'idle');
  };
  const request=async(path,method='GET')=>{
    const response=await fetch(controlUrl+path,{
      method,cache:'no-store',headers:{Authorization:'Bearer '+session()}
    });
    const body=await response.json().catch(()=>({}));
    if(!response.ok)throw new Error(body.error||'Operator control request failed');
    return body;
  };
  const refreshControls=async()=>{
    if(!controlUrl)return;
    ownerAccess.hidden=false;
    ownerLogin.href=controlUrl+'/auth/login';
    if(!session()){showSignedOut();return}
    try{
      const state=await request('/api/session');
      ownerLogin.hidden=true;
      if(ownerMenuToggle)ownerMenuToggle.hidden=false;
      const active=(state.activeRunnerRuns?.length||0)+(state.activeWakeRuns?.length||0);
      const mode=state.mode||(active>0?(state.enabled===false?'draining':'running'):(state.enabled===false?'disabled':'stopped'));
      const fallbackControls={start:active===0,stop:mode==='running',reset:active===0};
      const controls=state.controls||fallbackControls;
      const labels={running:'Running now',draining:'Stopping…',stopped:'Stopped',disabled:'Disabled'};
      setOwnerLight(mode==='running'?'running':labels[mode]?'stopped':'unknown');
      if(ownerStatus)ownerStatus.textContent=labels[mode]||'Checking controls…';
      if(ownerIdentity)ownerIdentity.textContent=state.login?`Signed in as ${state.login}`:'Signed in';
      if(ownerMenuLabel)ownerMenuLabel.textContent='Settings';
      if(ownerStart)ownerStart.disabled=controls.start!==true;
      if(ownerStop)ownerStop.disabled=controls.stop!==true;
      if(ownerReset)ownerReset.disabled=controls.reset!==true;
    }catch(error){
      try{localStorage.removeItem(sessionKey)}catch{}
      showSignedOut(error instanceof Error?error.message:'Session check failed');
    }
  };
  const operate=async path=>{
    if(ownerStart)ownerStart.disabled=true;
    if(ownerStop)ownerStop.disabled=true;
    if(ownerReset)ownerReset.disabled=true;
    if(ownerStatus)ownerStatus.textContent='Updating…';
    try{
      const result=await request(path,'POST');
      if(ownerStatus)ownerStatus.textContent=result.message||'Updated';
      await refreshControls();
    }catch(error){
      if(ownerStatus)ownerStatus.textContent=error.message;
      await refreshControls();
    }
  };
  ownerMenuToggle?.addEventListener('click',event=>{event.stopPropagation();setOwnerMenu(ownerControls?.hidden!==false)});
  ownerControls?.addEventListener('click',event=>event.stopPropagation());
  document.addEventListener('click',()=>setOwnerMenu(false));
  document.addEventListener('keydown',event=>{if(event.key==='Escape')setOwnerMenu(false)});
  ownerStart?.addEventListener('click',()=>operate('/api/start'));
  ownerStop?.addEventListener('click',()=>operate('/api/stop'));
  ownerReset?.addEventListener('click',()=>{
    if(confirm('Reset WAKE✳︎ durable research/history to cycle 0? Continuous operation will remain stopped.'))operate('/api/reset');
  });
  ownerSignout?.addEventListener('click',()=>{
    try{localStorage.removeItem(sessionKey)}catch{}
    showSignedOut();
  });
  refreshControls();
  setInterval(refreshControls,15000);
})();
