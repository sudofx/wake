/* A disposable, paired instrument using the farm's actual colony rules. No storage or authority. */
(function(root){
  'use strict';
  const colony=typeof module!=='undefined'&&module.exports?require('./ant-colony.js'):root.WakeAntColony;
  const PROTOCOL=Object.freeze({schema:'wake-ant-distance@1',seconds:180,ticks:1800,food:100,threshold:2,model:colony.MODEL});
  const predictions=Object.freeze({near:'The closer patch will deliver at least two more food units.',far:'The farther patch will deliver at least two more food units.',similar:'The two deliveries will differ by fewer than two food units.'});
  function setup(seed){
    if(!Number.isSafeInteger(seed)||seed<1||seed>4294967295)throw Error('Choose a whole-number seed from 1 to 4294967295.');
    const initial=new colony.Colony(seed),save=initial.save();
    const near=initial.nodes[initial.exit].x,far=near<60?116:4;
    const arms=[near,far].map(x=>{
      const c=colony.Colony.restore(save);
      // Remove the two starter patches in BOTH arms before placing equal food.
      // Nest reserves, workers, tunnels and RNG begin identically.
      c.food=[];
      if(!c.addFood(x))throw Error('The food intervention could not be applied.');
      return c;
    });
    return {seed,arms,positions:[near,far],tick:0};
  }
  function advance(run,count=30){
    if(!Number.isSafeInteger(count)||count<1||count>PROTOCOL.ticks)throw Error('Invalid simulation step count.');
    const end=Math.min(PROTOCOL.ticks,run.tick+count);
    while(run.tick<end){for(const arm of run.arms)arm.step();run.tick++;}
    return run.tick===PROTOCOL.ticks;
  }
  function measure(run){
    if(run.tick!==PROTOCOL.ticks)throw Error('The experiment has not completed.');
    const rows=run.arms.map(c=>({ticks:c.ticks,delivered:c.delivered,remaining:c.food.reduce((sum,f)=>sum+f.left,0),carried:c.ants.filter(a=>a.carrying===1).length}));
    if(rows.some(r=>r.ticks!==PROTOCOL.ticks||!Number.isSafeInteger(r.delivered)||r.delivered<0||r.delivered>PROTOCOL.food||r.delivered+r.remaining+r.carried!==PROTOCOL.food))throw Error('The food measurements are unavailable or inconsistent.');
    const difference=rows[0].delivered-rows[1].delivered;
    return {schema:PROTOCOL.schema,model:PROTOCOL.model,seed:run.seed,protocol:{...PROTOCOL},positions:{near:run.positions[0],far:run.positions[1]},measurements:{near:rows[0],far:rows[1],difference},outcome:Math.abs(difference)<PROTOCOL.threshold?'inconclusive':difference>0?'near':'far'};
  }
  function evaluate(result,prediction){
    if(!Object.hasOwn(predictions,prediction))throw Error('Choose a prediction first.');
    // A tiny difference cannot settle a directional explanation. A "similar"
    // prediction can match this observation without establishing equivalence.
    if(result.outcome==='inconclusive')return prediction==='similar'?'matched-small-difference':'inconclusive';
    return prediction===result.outcome?'supported':'contradicted';
  }
  const api={PROTOCOL,predictions,setup,advance,measure,evaluate};
  if(typeof module!=='undefined'&&module.exports){module.exports=api;return;}
  root.WakeAntExperiment=api;
  const $=id=>document.getElementById(id),form=$('prediction-form');
  if(!form)return;
  let active=null,generation=0,last=null;
  const sourceRevision=/^[a-f0-9]{40}$/.test(root.WAKE_DEPLOYMENT?.presentation_revision||'')?root.WAKE_DEPLOYMENT.presentation_revision:null;
  if(sourceRevision)document.querySelectorAll('a[data-experiment-source]').forEach(link=>{link.href=link.href.replace('/blob/master/','/blob/'+sourceRevision+'/');});
  function status(text){$('experiment-status').textContent=text;}
  function unlock(){form.querySelectorAll('input,button').forEach(el=>{el.disabled=false;});$('stop-test').hidden=true;$('stop-test').disabled=true;}
  function stop(){generation++;active=null;unlock();status('Stopped. No conclusion was recorded. You can run the comparison again.');}
  function complete(run,prediction){
    const result=measure(run),verdict=evaluate(result,prediction);
    last={...result,prediction:predictions[prediction],verdict,presentation_revision:sourceRevision};
    const m=result.measurements;
    $('near-result').textContent=String(m.near.delivered);$('far-result').textContent=String(m.far.delivered);
    $('frozen-prediction').textContent=predictions[prediction];
    const labels={supported:'Your prediction was supported in this run.',contradicted:'Your prediction was contradicted in this run.',inconclusive:'This run cannot settle your prediction.','matched-small-difference':'You predicted a small difference, and this run matched it.'};
    $('result-title').textContent=labels[verdict];
    $('result-detail').textContent=`Closer minus farther: ${m.difference} food units. ${Math.abs(m.difference)<PROTOCOL.threshold?'The gap is below the preset two-unit threshold. This does not establish that distance has no effect.':'The gap reached the preset two-unit threshold. This does not show that the same outcome holds for other seeds or real ants.'}`;
    $('method-result').textContent=`Both colonies ran for three simulation minutes with the same starting conditions and 100 food units each. We counted food delivered to the nest. Food still outside or being carried is counted separately, so none is missing.`;
    $('technical-result').textContent=JSON.stringify(last,null,2);
    $('save-result').disabled=false;$('result').hidden=false;$('result-title').focus({preventScroll:true});$('result-title').scrollIntoView({block:'start'});active=null;unlock();status('Comparison complete. There is no next step you have to take.');
  }
  function frame(run,prediction,token){
    if(token!==generation)return;
    try{
      const done=advance(run);$('experiment-progress').value=run.tick;
      $('progress-label').textContent=`${Math.floor(run.tick/10)} of ${PROTOCOL.seconds} simulation seconds`;
      if(done){complete(run,prediction);return;}
      setTimeout(()=>frame(run,prediction,token),0);
    }catch(error){active=null;last=null;unlock();status(`No result: ${error.message} Try the comparison again.`);}
  }
  form.addEventListener('submit',event=>{
    event.preventDefault();if(active)return;
    const prediction=form.querySelector('input[name="prediction"]:checked')?.value;
    try{
      if(!prediction)throw Error('Choose what you expect to happen.');
      active=setup(Number($('experiment-seed').value));
      $('result').hidden=true;last=null;
      form.querySelectorAll('input,button').forEach(el=>{el.disabled=true;});$('stop-test').hidden=false;$('stop-test').disabled=false;
      $('result-copy').hidden=true;$('result-text').textContent='';
      $('experiment-progress').value=0;status('Running two separate colonies. Your prediction and the method are fixed for this run.');
      const token=++generation;setTimeout(()=>frame(active,prediction,token),0);
    }catch(error){status(error.message);(prediction?$('experiment-seed'):form.querySelector('input[name="prediction"]')).focus();}
  });
  $('stop-test').addEventListener('click',stop);
  // Navigating away cancels all work; no catch-up, save, telemetry or return requirement.
  root.addEventListener('pagehide',()=>{generation++;active=null;});
  $('save-result').addEventListener('click',()=>{
    if(!last)return;
    $('result-text').textContent=`A shorter trip?\n\nMy prediction: ${last.prediction}\n\nWhat happened: ${last.measurements.near.delivered} food units reached the nest from the closer patch, and ${last.measurements.far.delivered} from the farther patch.\n\n${$('result-title').textContent}\n\nThe colonies started alike, apart from food location, and ran for three simulation minutes. This is one simulation run. It does not establish how real ants behave or what happens in every layout.\n\nTo repeat this starting layout, use ${last.seed}.`;$('result-copy').hidden=false;
    status('Your short summary is below. Copy it if you want to keep it. Nothing has been uploaded.');
  });
  unlock();status('Ready. Your prediction stays on this page and is never sent anywhere.');
})(typeof globalThis!=='undefined'?globalThis:this);
