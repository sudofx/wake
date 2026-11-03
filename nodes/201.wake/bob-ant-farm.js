/* Read-only shared colony and derived farm notebook. Never research evidence. */
((root)=>{
  'use strict';
  const SCHEMA='wake-bob-ant-farm@1',MODEL='pellet-tunnels@9',COLONY_ID='bobs-ant-farm',SEED=0x0b0b5a17,MAX_BYTES=2097152;
  const metricKeys=['seconds','ants','born','deaths','starved','food_reserve','protein_reserve','food_remaining','dug','delivered','eggs','larvae','pupae','nurses','queen_alive'];
  const integer=(value,min=0,max=1e10)=>Number.isSafeInteger(value)&&value>=min&&value<=max;
  const plain=value=>value&&typeof value==='object'&&!Array.isArray(value)&&[Object.prototype,null].includes(Object.getPrototypeOf(value));
  const keys=(value,allowed)=>plain(value)&&Object.keys(value).every(key=>allowed.includes(key));
  const validDate=value=>typeof value==='string'&&value.length<=30&&/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3})?Z$/.test(value)&&Number.isFinite(Date.parse(value))&&new Date(value).toISOString()===(value.includes('.')?value:value.replace('Z','.000Z'));
  function metric(value,strict=true){
    if((strict&&!keys(value,metricKeys))||metricKeys.some(key=>key==='queen_alive'?typeof value[key]!=='boolean':!Number.isFinite(value[key])||value[key]<0||value[key]>1e10))throw Error('Invalid shared-colony observations.');
    return Object.fromEntries(metricKeys.map(key=>[key,value[key]]));
  }
  function careEvent(value,start,end){
    if(!keys(value,['tick','action','x','units'])||!integer(value.tick,start,end)||value.action!=='feed'||!integer(value.x,4,116)||value.units!==100)throw Error('Invalid shared-colony care event.');
    return {tick:value.tick,action:'feed',x:value.x,units:100};
  }
  function note(value,end){
    const fields=['id','at','from_tick','to_tick','workers','worker_change','deliveries','new_tunnels','eggs','larvae','pupae','feedings','food_added','queen_alive'];
    if(!keys(value,fields)||typeof value.id!=='string'||!/^farm-\d+-\d+$/.test(value.id)||value.id.length>60||!validDate(value.at)||!integer(value.from_tick,0,end)||!integer(value.to_tick,value.from_tick,end)||!integer(value.workers,0,128)||!integer(value.worker_change,-128,128)||value.to_tick-value.from_tick>6000||!integer(value.feedings,0,120)||!integer(value.new_tunnels,0,3000)||!['eggs','larvae','pupae'].every(key=>integer(value[key],0,128))||!['deliveries','new_tunnels','eggs','larvae','pupae','feedings','food_added'].every(key=>integer(value[key]))||value.food_added!==value.feedings*100||typeof value.queen_alive!=='boolean')throw Error('Invalid shared-colony notebook entry.');
    return Object.fromEntries(fields.map(key=>[key,value[key]]));
  }
  function validate(value,{ColonyClass=root.WakeAntColony?.Colony}={}){
    if(!keys(value,['schema','colony_id','seed','model','source_revision','updated_at','sequence','checkpoint','replay','observation','care_receipts','notes'])||value.schema!==SCHEMA||value.colony_id!==COLONY_ID||value.seed!==SEED||value.model!==MODEL||!/^[a-f0-9]{40}$/.test(value.source_revision||'')||!validDate(value.updated_at)||!integer(value.sequence)||!ColonyClass)throw Error('Bob’s shared farm has an unsupported identity or model.');
    if(!plain(value.checkpoint)||!plain(value.replay?.start)||value.checkpoint.schema!=='wake-ant-colony@4'||value.replay.start.schema!=='wake-ant-colony@4'||!keys(value.replay,['start','ticks','care'])||!integer(value.replay.ticks,0,6000)||!Array.isArray(value.replay.care)||value.replay.care.length>120)throw Error('Invalid shared-colony replay.');
    const endColony=ColonyClass.restore(value.checkpoint),startColony=ColonyClass.restore(value.replay.start);
    if(endColony.observation().model!==MODEL||startColony.observation().model!==MODEL)throw Error('The shared-colony player has a different model.');
    const checkpoint=endColony.save(),start=startColony.save();
    if(checkpoint.seed!==SEED||start.seed!==SEED||start.ticks+value.replay.ticks!==checkpoint.ticks)throw Error('Shared-colony checkpoint does not match replay.');
    const care=value.replay.care.map(row=>careEvent(row,start.ticks,Math.max(start.ticks,checkpoint.ticks-1)));
    if((value.replay.ticks===0&&care.length)||care.some((row,i)=>i>0&&row.tick<care[i-1].tick))throw Error('Shared-colony interventions are out of order.');
    const observation=value.observation;
    if(!keys(observation,['from_tick','to_tick','before','after','feedings','food_added','care_failures','scope'])||observation.from_tick!==start.ticks||observation.to_tick!==checkpoint.ticks||observation.scope!=='simulation-only'||observation.feedings!==care.length||observation.food_added!==care.length*100||checkpoint.addedFood-start.addedFood!==observation.food_added||!integer(observation.care_failures,0,120))throw Error('Shared-colony observation does not match care.');
    const before=metric(observation.before),after=metric(observation.after),actualBefore=metric(ColonyClass.restore(start).metrics(),false),actualAfter=metric(ColonyClass.restore(checkpoint).metrics(),false);
    if(metricKeys.some(key=>before[key]!==actualBefore[key]||after[key]!==actualAfter[key]))throw Error('Shared-colony observations do not match the checkpoint.');
    if(!Array.isArray(value.care_receipts)||value.care_receipts.length>120||!Array.isArray(value.notes)||value.notes.length>48)throw Error('Shared-colony notebook exceeds its bounds.');
    const receipts=value.care_receipts.map(row=>careEvent(row,0,Math.max(0,checkpoint.ticks-1))),notes=value.notes.map(row=>note(row,checkpoint.ticks));
    if(receipts.some((row,i)=>i>0&&row.tick<receipts[i-1].tick)||notes.some((row,i)=>i>0&&row.to_tick<notes[i-1].to_tick)||new Set(notes.map(row=>row.id)).size!==notes.length||(value.sequence===0&&notes.length)||(value.sequence>0&&(!notes.length||notes.at(-1).to_tick!==checkpoint.ticks||notes.at(-1).at!==value.updated_at||notes.at(-1).workers!==after.ants||notes.at(-1).deliveries!==after.delivered-before.delivered||notes.at(-1).new_tunnels!==after.dug-before.dug||notes.at(-1).feedings!==care.length)))throw Error('Shared-colony history is out of order.');
    return {schema:SCHEMA,colony_id:COLONY_ID,seed:SEED,model:MODEL,source_revision:value.source_revision,updated_at:value.updated_at,sequence:value.sequence,checkpoint,replay:{start,ticks:value.replay.ticks,care},observation:{from_tick:start.ticks,to_tick:checkpoint.ticks,before,after,feedings:care.length,food_added:care.length*100,care_failures:observation.care_failures,scope:'simulation-only'},care_receipts:receipts,notes};
  }
  function applyReplayStep(colony,packet,cursor=0){
    if(colony.ticks>=packet.checkpoint.ticks)return cursor;
    while(cursor<packet.replay.care.length&&packet.replay.care[cursor].tick===colony.ticks){const event=packet.replay.care[cursor++];if(!colony.addFood(event.x))throw Error('Shared-colony replay cannot apply recorded feeding.');}
    colony.step();return cursor;
  }
  function createReplay(packet){const safe=validate(packet);return {colony:root.WakeAntColony.Colony.restore(safe.replay.start),packet:safe,cursor:0};}
  function sourceURL(){
    const binding=root.WAKE_DEPLOYMENT?.bob_ant_farm||{};
    if(binding.preview_path!==undefined){
      const own=new URL(root.document?.baseURI||root.location?.href),target=new URL(binding.preview_path,own);
      if(target.origin!==own.origin||target.search||target.hash||!/^\/[A-Za-z0-9_/-]*bob-ant-farm\.json$/.test(target.pathname))throw Error('Invalid local shared-farm binding.');
      return target.href;
    }
    const repository=binding.repository||root.WAKE_DEPLOYMENT?.public_data?.repository||root.WAKE_DEPLOYMENT?.hosted_status?.repository||'sudofx/wake';
    if(!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository))throw Error('Invalid shared-farm repository binding.');
    return 'https://raw.githubusercontent.com/'+repository+'/bob-ant-farm/farm.json';
  }
  let cached,checkedAt=0;
  async function read(){
    if(cached&&Date.now()-checkedAt<60000)return cached;
    checkedAt=Date.now();
    cached=(async()=>{
      const response=await root.fetch(sourceURL(),{credentials:'omit',referrerPolicy:'no-referrer',cache:'no-cache',signal:AbortSignal.timeout(8000)});
      if(!response.ok||!response.body)throw Error('Bob’s shared farm is unavailable. Your own colony has not changed.');
      const reader=response.body.getReader(),chunks=[];let size=0;
      try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>MAX_BYTES)throw Error('Bob’s shared farm exceeds its reading limit.');chunks.push(value);}}finally{await reader.cancel();}
      const bytes=new Uint8Array(size);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
      const packet=validate(JSON.parse(new TextDecoder().decode(bytes)));
      const freeze=value=>{if(value&&typeof value==='object'){Object.freeze(value);for(const child of Object.values(value))freeze(child);}return value;};return freeze(packet);
    })();
    try{return await cached;}catch(error){cached=undefined;throw error;}
  }
  function notebookText(value){
    return `${value.deliveries} food deliveries · ${value.new_tunnels} new tunnel segments · ${value.workers} workers · ${value.eggs+value.larvae+value.pupae} developing young · ${value.feedings} recorded feedings (${value.food_added} simulation units).`;
  }

  async function mountNotebook(container){
    if(!container||container.querySelector('[data-bob-farm-notebook]'))return;
    const document=container.ownerDocument,section=document.createElement('details');section.dataset.bobFarmNotebook='';section.className='bob-farm-notebook';
    const heading=document.createElement('summary');heading.textContent='Farm observation record';
    const description=document.createElement('p');description.textContent='Dated simulation observations and care receipts. Bob’s interpretation belongs in the article, when these observations support a useful connection.';
    section.append(heading,description);container.append(section);
    try{
      const packet=await read(),latest=packet.notes.slice(-3).reverse();
      if(!latest.length){const pending=document.createElement('p');pending.textContent='Bob’s farm is settling in. Its first recorded interval will appear here.';section.append(pending);}
      for(const entry of latest){const article=document.createElement('article'),time=document.createElement('time'),text=document.createElement('p');time.dateTime=entry.at;time.textContent=new Date(entry.at).toLocaleString();text.textContent=notebookText(entry);article.append(time,text);section.append(article);}
      const status=document.createElement('p');status.className='small';const age=Date.now()-Date.parse(packet.updated_at);status.textContent=(age>7200000?'Upkeep is delayed; the saved simulation is resting. ':'')+'This is an observation record, not Bob’s writing or independent biological research.';section.append(status);
      const link=document.createElement('a');link.textContent='Observe Bob’s ant farm →';link.href=new URL('ant-farm.html?farm=bob',document.baseURI).href;section.append(link);
    }catch{const unavailable=document.createElement('p');unavailable.textContent='Bob’s shared farm notes are temporarily unavailable. The research articles are unchanged.';section.append(unavailable);}
    return section;
  }
  const api={read,validate,createReplay,applyReplayStep,mountNotebook,notebookText,sourceURL,validDate,MAX_BYTES,SCHEMA,MODEL,COLONY_ID,SEED};
  if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.WakeBobFarm=api;
})(typeof globalThis!=='undefined'?globalThis:this);
