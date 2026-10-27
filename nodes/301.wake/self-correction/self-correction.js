/* Public observation only. No credentials, dispatches, or operational writes. */
(() => {
  'use strict';
  const REPOSITORY='sudofx/wake';
  const API=`https://api.github.com/repos/${REPOSITORY}`;
  const $=id=>document.getElementById(id);
  const element=(tag,text,className)=>{const value=document.createElement(tag);if(text!==undefined)value.textContent=String(text);if(className)value.className=className;return value;};
  const stamp=value=>Number.isFinite(Date.parse(value))?new Date(value).toLocaleString():'time unavailable';
  const count=value=>Number.isSafeInteger(value)&&value>=0?String(value):'unknown';
  const short=value=>typeof value==='string'&&/^[0-9a-f]{40,64}$/.test(value)?value.slice(0,12):'unknown';
  const githubLink=(url,label,kind)=>{const a=element('a',label);if(typeof url==='string'&&new RegExp(`^https://github\\.com/${REPOSITORY}/${kind}/[0-9]+$`).test(url))a.href=url;return a;};
  async function json(url,maximum=4*1024*1024){
    const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),15000);
    try{
      const response=await fetch(url,{cache:'no-store',credentials:'omit',signal:controller.signal,headers:{Accept:'application/json'}});
      if(!response.ok){const error=new Error('Unavailable');error.status=response.status;throw error;}
      const length=Number(response.headers.get('content-length'));if(length>maximum)throw new Error('Response exceeds limit');
      // Stream bounds apply even when Content-Length is absent or compressed.
      if(!response.body?.getReader){const text=await response.text();if(new TextEncoder().encode(text).length>maximum)throw new Error('Response exceeds limit');return JSON.parse(text);}
      const reader=response.body.getReader(),chunks=[];let bytes=0;
      for(;;){const {done,value}=await reader.read();if(done)break;bytes+=value.byteLength;if(bytes>maximum){await reader.cancel();throw new Error('Response exceeds limit');}chunks.push(value);}
      const all=new Uint8Array(bytes);let at=0;for(const chunk of chunks){all.set(chunk,at);at+=chunk.byteLength;}return JSON.parse(new TextDecoder().decode(all));
    }finally{clearTimeout(timer);}
  }
  async function workflow(){
    try{
      const data=await json(`${API}/actions/workflows/self-correction.yml/runs?per_page=6`,256*1024);
      if(!Array.isArray(data.workflow_runs))throw new Error('Invalid runs');
      const rows=data.workflow_runs.filter(run=>Number.isSafeInteger(run.id)).slice(0,6);
      $('correction-runs').replaceChildren();
      for(const run of rows){
        const row=element('li'),body=element('div'),state=run.status==='completed'?(run.conclusion||'unknown'):run.status;
        body.append(githubLink(run.html_url,run.display_title||`Correction run ${run.run_number||run.id}`,'actions/runs'));
        body.append(element('small',`Started ${stamp(run.created_at)} · updated ${stamp(run.updated_at)} · source ${short(run.head_sha)}`));
        const badge=element('span',String(state||'unknown').replaceAll('_',' '),'run-state');badge.dataset.state=state||'unknown';row.append(body,badge);$('correction-runs').append(row);
      }
      $('workflow-status').textContent=rows.length?'Current GitHub workflow observations. Open a run for its proposal, tests and review step.':'The correction workflow is installed. No runs have been recorded yet.';
      $('workflow-observed').textContent=`GitHub checked ${new Date().toLocaleString()}. A successful run creates a draft only; it does not mean the change was merged or deployed.`;
    }catch(error){
      $('workflow-status').textContent=error.status===404?'The source-correction workflow is not available on GitHub yet. Publish its source before starting a run.':'Current correction runs are unavailable. Open GitHub directly; no activity or success is inferred.';
      $('workflow-observed').textContent=`Last check ${new Date().toLocaleString()}. ${error.status===403||error.status===429?'GitHub may be limiting anonymous requests.':''}`;
      // Do not leave old successful runs looking current after observation fails.
      $('correction-runs').replaceChildren();
    }
  }
  async function reviews(){
    try{
      const data=await json(`${API}/pulls?state=all&sort=updated&direction=desc&per_page=30`,1024*1024);
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
      const data=await json(new URL('../installation.json',location.href));
      if(!Array.isArray(data.nodes)||typeof data.installation_id!=='string'||data.nodes.length>100)throw new Error('Invalid installation');
      $('adaptation-nodes').replaceChildren();
      for(const node of data.nodes){
        if(!node||typeof node.id!=='string'||!/^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$/.test(node.id))continue;
        const status=node.research?.status?.autonomous_context,row=element('tr'),name=element('td');
        const link=element('a',node.id);link.href=new URL(`../nodes/${encodeURIComponent(node.id)}/console.html`,location.href);name.append(link);row.append(name);
        const reported=node.available!==false&&status&&status.schema==='autonomous-context@1';
        for(const value of [reported?(status.enabled===true?'Enabled':status.enabled===false?'Disabled':'Unknown'):'Not reported',reported?(status.policy?.selector||'Unknown'):'Unknown',reported?`${count(status.trials)} / ${count(status.adoptions)} / ${count(status.rollbacks)}`:'Unknown'])row.append(element('td',value));
        const evidence=element('td');evidence.append(element('div',`v${count(node.snapshot?.version??node.research?.version)} · ${short(node.snapshot?.head||node.research?.head)}`));
        evidence.append(element('small',stamp(node.snapshot?.generated||node.research?.generated)));
        if(status?.quarantined===true)evidence.append(element('div','Adaptation quarantined'));
        row.append(evidence);$('adaptation-nodes').append(row);
      }
      const captured=data.hosted_execution?.captured_at||data.generated;
      $('snapshot-status').textContent=`Published record snapshot · captured ${stamp(captured)}. This is dated evidence, not a live runtime connection.`;
      $('snapshot-identity').textContent=`Installation ${data.installation_id} · executing revision at capture ${short(data.hosted_execution?.source_revision)}. “Not reported” does not mean zero trials or an enabled grant.`;
    }catch{
      $('adaptation-nodes').replaceChildren();$('snapshot-status').textContent='The current installation snapshot is unavailable. No adoption, grant or live runtime status is inferred.';$('snapshot-identity').textContent='';
    }
  }
  let busy=false;
  async function refresh(){if(busy)return;busy=true;$('refresh').disabled=true;await Promise.allSettled([workflow(),reviews(),snapshot()]);busy=false;$('refresh').disabled=false;}
  $('refresh').addEventListener('click',refresh);
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)refresh();});
  setInterval(()=>{if(!document.hidden)refresh();},180000);
  refresh();
})();
