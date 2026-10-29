/* Public observation only. No credentials, dispatches, or operational writes. */
(() => {
  'use strict';
  const REPOSITORY='sudofx/wake';
  const API=`https://api.github.com/repos/${REPOSITORY}`;
  const OBSERVATION_INTERVAL=10*60*1000;
  const $=id=>document.getElementById(id);
  const element=(tag,text,className)=>{const value=document.createElement(tag);if(text!==undefined)value.textContent=String(text);if(className)value.className=className;return value;};
  const stamp=value=>Number.isFinite(Date.parse(value))?new Date(value).toLocaleString():'time unavailable';
  const count=value=>Number.isSafeInteger(value)&&value>=0?String(value):'unknown';
  const short=value=>typeof value==='string'&&/^[0-9a-f]{40,64}$/.test(value)?value.slice(0,12):'unknown';
  const githubLink=(url,label,kind)=>{const a=element('a',label);if(typeof url==='string'&&new RegExp(`^https://github\\.com/${REPOSITORY}/${kind}/[0-9]+$`).test(url))a.href=url;return a;};
  async function json(url,maximum=4*1024*1024,read=globalThis.fetch.bind(globalThis)){
    const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),15000);
    try{
      const response=await read(url,{cache:'no-store',credentials:'omit',signal:controller.signal,headers:{Accept:'application/json'}});
      if(!response.ok){const error=new Error('Unavailable');error.status=response.status;throw error;}
      const length=Number(response.headers.get('content-length'));if(length>maximum)throw new Error('Response exceeds limit');
      // Stream bounds apply even when Content-Length is absent or compressed.
      if(!response.body?.getReader){const text=await response.text();if(new TextEncoder().encode(text).length>maximum)throw new Error('Response exceeds limit');return JSON.parse(text);}
      const reader=response.body.getReader(),chunks=[];let bytes=0;
      for(;;){const {done,value}=await reader.read();if(done)break;bytes+=value.byteLength;if(bytes>maximum){await reader.cancel();throw new Error('Response exceeds limit');}chunks.push(value);}
      const all=new Uint8Array(bytes);let at=0;for(const chunk of chunks){all.set(chunk,at);at+=chunk.byteLength;}return JSON.parse(new TextDecoder().decode(all));
    }finally{clearTimeout(timer);}
  }
  // Share anonymous metadata reads across navigation. The snapshot transport is
  // reserved for exported evidence; GitHub API observations use ordinary fetch.
  async function metadata(url,slot,maximum){
    const key=`wake-correction-observation@1:${REPOSITORY}:${slot}`;
    try{
      const raw=localStorage.getItem(key);
      if(raw && raw.length<maximum*2){
        const cached=JSON.parse(raw);
        if(cached.url===url && cached.checked<=Date.now() && Date.now()-cached.checked<OBSERVATION_INTERVAL){
          if(cached.failed){const error=new Error('Unavailable');error.status=cached.status;throw error;}
          return cached;
        }
      }
    }catch(error){if(error.message==='Unavailable')throw error;}
    let result;
    try{result={url,data:await json(url,maximum),checked:Date.now()};}
    catch(error){
      try{localStorage.setItem(key,JSON.stringify({url,checked:Date.now(),failed:true,status:error.status}));}catch{}
      throw error;
    }
    try{localStorage.setItem(key,JSON.stringify(result));}catch{}
    return result;
  }
  const outcomes={healthy:'healthy — no repair needed',repaired:'repair applied',republished:'website republished',
    review_required:'proposal needs review',provider_wait:'waiting for provider',outside_scope:'outside repair scope',
    budget_wait:'waiting for budget',failed:'check failed'};
  async function workflow(){
    try{
      const observation=await metadata(`${API}/actions/workflows/self-correction.yml/runs?per_page=6`,'runs',256*1024),data=observation.data;
      if(!Array.isArray(data.workflow_runs))throw new Error('Invalid runs');
      const rows=data.workflow_runs.filter(run=>Number.isSafeInteger(run.id)).slice(0,6);
      let outcome=null;
      if(rows.length)try{
        const jobs=await metadata(`${API}/actions/runs/${rows[0].id}/jobs?per_page=50`,'latest-jobs',256*1024);
        if(Array.isArray(jobs.data.jobs)){
          const matches=jobs.data.jobs.slice(0,50).filter(job=>job.status==='completed'&&job.conclusion==='success'&&/^Outcome: [a-z_]+$/.test(job.name));
          const named=matches.map(job=>job.name.slice('Outcome: '.length)).filter(name=>Object.hasOwn(outcomes,name));
          if(named.length===1)outcome=named[0];
        }
      }catch{} // A workflow conclusion alone cannot establish a repair outcome.
      $('correction-runs').replaceChildren();
      for(const [index,run] of rows.entries()){
        const row=element('li'),body=element('div'),state=run.status==='completed'?(run.conclusion||'unknown'):run.status;
        body.append(githubLink(run.html_url,run.display_title||`Correction run ${run.run_number||run.id}`,'actions/runs'));
        body.append(element('small',`Started ${stamp(run.created_at)} · updated ${stamp(run.updated_at)} · source ${short(run.head_sha)}`));
        const badge=element('span',index===0&&outcome?outcomes[outcome]:String(state||'unknown').replaceAll('_',' '),'run-state');badge.dataset.state=index===0&&outcome?outcome:state||'unknown';row.append(body,badge);$('correction-runs').append(row);
      }
      $('workflow-status').textContent=rows.length?'Recent GitHub checks. The latest run’s named outcome distinguishes a healthy check, an automatic repair, republishing and a review proposal.':'The correction workflow is installed. No runs have been recorded yet.';
      $('workflow-observed').textContent=`Runs checked ${new Date(observation.checked).toLocaleString()}. ${outcome?'Open the latest run for its evidence.':'The latest repair outcome is not reported; workflow success alone does not establish a repair or publication.'}`;
    }catch(error){
      $('workflow-status').textContent=error.status===404?'The source-correction workflow is not available on GitHub yet. Publish its source before starting a run.':'Current correction runs are unavailable. Open GitHub directly; no activity or success is inferred.';
      $('workflow-observed').textContent=`Last check ${new Date().toLocaleString()}. ${error.status===403||error.status===429?'GitHub may be limiting anonymous requests.':''}`;
      // Do not leave old successful runs looking current after observation fails.
      $('correction-runs').replaceChildren();
    }
  }
  async function reviews(){
    try{
      const {data}=await metadata(`${API}/pulls?state=all&sort=updated&direction=desc&per_page=30`,'reviews',1024*1024);
      if(!Array.isArray(data))throw new Error('Invalid reviews');
      const rows=data.filter(pr=>Number.isSafeInteger(pr.number)&&pr.head?.ref?.startsWith('wake-correction/')).slice(0,5);
      $('correction-reviews').replaceChildren();
      for(const pr of rows){
        const row=element('li'),body=element('div'),state=pr.merged_at?'merged':pr.state==='closed'?'closed':pr.draft?'draft review':'open review';
        body.append(githubLink(pr.html_url,`#${pr.number} · ${pr.title||'Source correction'}`,'pull'));
        body.append(element('small',`Updated ${stamp(pr.updated_at)} · proposed source ${short(pr.head?.sha)}`));
        row.append(body,element('span',state,'run-state'));$('correction-reviews').append(row);
      }
      $('review-status').textContent=rows.length?'Recent correction pull requests. Merged source still needs its normal publication or runtime release.':'No correction pull requests among the 30 most recently updated requests.';
    }catch{
      $('correction-reviews').replaceChildren();$('review-status').textContent='Current review state is unavailable. Open the pull-request list directly.';
    }
  }
  async function snapshot(){
    try{
      const transport=window.WakePublicData;
      const data=await json(new URL('../installation.json',location.href),4*1024*1024,
        transport?transport.fetch.bind(transport):globalThis.fetch.bind(globalThis));
      if(!Array.isArray(data.nodes)||typeof data.installation_id!=='string'||data.nodes.length>100)throw new Error('Invalid installation');
      $('adaptation-nodes').replaceChildren();
      for(const node of data.nodes){
        if(!node||typeof node.id!=='string'||!/^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$/.test(node.id))continue;
        const status=node.research?.status?.autonomous_context,row=element('tr'),name=element('td');
        const link=element('a',node.id),url=new URL(`../nodes/${encodeURIComponent(node.id)}/console.html`,location.href);
        link.href=(transport?transport.pin(url):url).href;name.append(link);row.append(name);
        const reported=node.available!==false&&status&&status.schema==='autonomous-context@1';
        for(const value of [reported?(status.enabled===true?'Enabled':status.enabled===false?'Disabled':'Unknown'):'Not reported',reported?(status.policy?.selector||'Unknown'):'Unknown',reported?`${count(status.trials)} / ${count(status.adoptions)} / ${count(status.rollbacks)}`:'Unknown'])row.append(element('td',value));
        const evidence=element('td');evidence.append(element('div',`v${count(node.snapshot?.version??node.research?.version)} · ${short(node.snapshot?.head||node.research?.head)}`));
        evidence.append(element('small',stamp(node.snapshot?.generated||node.research?.generated)));
        if(status?.quarantined===true)evidence.append(element('div','Adaptation quarantined'));
        row.append(evidence);$('adaptation-nodes').append(row);
      }
      const captured=data.hosted_execution?.captured_at||data.generated;
      $('snapshot-status').textContent=`Published record snapshot · captured ${stamp(captured)}. This is dated evidence, not a live runtime connection.`;
      $('snapshot-identity').textContent=`Installation ${data.installation_id} · executing revision at capture ${short(data.hosted_execution?.source_revision)}${transport?.revision?' · public snapshot '+short(transport.revision):''}. “Not reported” does not mean zero trials or an enabled grant.`;
    }catch{
      $('adaptation-nodes').replaceChildren();$('snapshot-status').textContent='The current installation snapshot is unavailable. No adoption, grant or live runtime status is inferred.';$('snapshot-identity').textContent='';
    }
  }
  let busy=false;
  async function observations(){if(busy)return;busy=true;await Promise.allSettled([workflow(),reviews()]);busy=false;}
  $('refresh').addEventListener('click',()=>{
    $('refresh').disabled=true;
    const config=window.WAKE_DEPLOYMENT?.public_data;
    if(config&&!new URL(location.href).searchParams.has('public_revision'))try{
      const key=`wake-public-snapshot:${config.repository}:${config.installation_id}`,cached=JSON.parse(localStorage.getItem(key));
      // Expire discovery, retaining the verified revision for offline recovery.
      if(cached&&/^[a-f0-9]{40}$/.test(cached.revision))localStorage.setItem(key,JSON.stringify({...cached,time:0,failedAt:0}));
    }catch{}
    location.reload();
  });
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)observations();});
  setInterval(()=>{if(!document.hidden)observations();},OBSERVATION_INTERVAL);
  observations();snapshot();
})();
