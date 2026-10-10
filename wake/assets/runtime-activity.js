/* Optional same-origin inspection channel. It cannot authorize work or import
 * hosted data. A missing capability stays hidden; a lost connection clears all
 * live marks. Published pending invocations are historical evidence, not a pulse.
 */
window.WakeRuntimeActivityView = status => {
  const states=new Set(['running','idle','paused','waiting','standby','blocked']);
  const stages=new Set(['idle','record','context','collecting','provider','governance','continuity','receipt']);
  if(status?.mode!=='standalone'||status.activity_schema!==1||status.capabilities?.live_activity!==true||
     typeof status.runtime_id!=='string'||!status.runtime_id||!states.has(status.state)||
     typeof status.observed_at!=='string'||!Number.isFinite(Date.parse(status.observed_at))||!stages.has(status.activity?.stage))return null;
  const active=status.state==='running'&&status.activity.active===true&&status.activity.stage!=='idle';
  return {...status,activity:{...status.activity,active,
    coordinate_id:active&&['provider','governance','continuity'].includes(status.activity.stage)&&
      typeof status.activity.coordinate_id==='string'?status.activity.coordinate_id:null}};
};
(() => {
  if(window.WAKE_DEPLOYMENT?.schema!==1||window.WAKE_DEPLOYMENT.mode!=='standalone')return;
  let receivedAt=0,busy=false;
  const publish=value=>{window.WakeRuntimeActivity=value;window.dispatchEvent(new CustomEvent('wake-runtime-activity',{detail:value}));};
  async function poll(){
    if(busy||document.hidden)return;
    busy=true;
    const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),2500);
    try{
      const response=await fetch('/runtime.json',{cache:'no-store',signal:controller.signal});
      if(!response.ok)throw new Error('Runtime unavailable');
      const view=window.WakeRuntimeActivityView(await response.json());
      receivedAt=performance.now();publish(view);
    }catch{
      publish(null);
    }finally{clearTimeout(timeout);busy=false;}
  }
  poll();setInterval(poll,3000);
  setInterval(()=>{if(window.WakeRuntimeActivity&&performance.now()-receivedAt>9000)publish(null);},1000);
  document.addEventListener('visibilitychange',()=>{publish(null);if(!document.hidden)poll();});
})();
