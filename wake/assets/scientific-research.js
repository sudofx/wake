/* Read-only audit of one selected export. Never authority or provider access. */
(() => {
  'use strict';
  const nodeID=/^(?:10[0-3]|20[0-3]|30[0-3])\.wake$/;
  function validate(data){
    if(data.schema!=='wake-scientific-audit@1' || typeof data.source?.head!=='string' || !Array.isArray(data.investigations))
      throw Error('Unsupported scientific report');
    return data;
  }
  async function loadReports(read,{node:scope=null}={}){
    if(scope!==null && !nodeID.test(scope))throw Error('Invalid node scope');
    const prefix=scope?'../../':'';
    const manifest=await read(prefix+'installation.json');
    if(!manifest){
      if(scope)throw Error('Installation snapshot unavailable for this node');
      const data=await read('scientific-research.json');
      return {reports:data?[{node:'Record',data:validate(data)}]:[],unavailable:[],absent:data?[]:['Record']};
    }
    if(manifest.schema!==1 || !Array.isArray(manifest.nodes) || manifest.nodes.length>12 ||
       manifest.nodes.some(n=>!nodeID.test(n.id)) || new Set(manifest.nodes.map(n=>n.id)).size!==manifest.nodes.length)
      throw Error('Invalid installation snapshot');
    const nodes=scope?manifest.nodes.filter(n=>n.id===scope):manifest.nodes;
    if(scope && !nodes.length)throw Error('Node is absent from selected installation');
    const reports=[],unavailable=[],absent=[];
    for(let offset=0;offset<nodes.length;offset+=3){
      await Promise.all(nodes.slice(offset,offset+3).map(async node=>{
        try{
          if(node.available===false)throw Error('Node snapshot unavailable');
          const data=await read(prefix+'nodes/'+node.id+'/scientific-research.json');
          if(!data){absent.push(node.id);return;}
          validate(data);
          const expected=manifest.record_heads?.[node.id]?.head;
          if(typeof expected!=='string' || data.source.head!==expected)throw Error('Record head differs from selected snapshot');
          reports.push({node:node.id,data});
        }catch(error){unavailable.push(node.id+': '+error.message);}
      }));
    }
    reports.sort((a,b)=>a.node.localeCompare(b.node));
    absent.sort();unavailable.sort();
    return {manifest,reports,unavailable,absent};
  }
  function section(doc,parent,title,value,collapsed=false){
    if(collapsed){const details=doc.createElement('details'),summary=doc.createElement('summary');
      summary.textContent=title;details.append(summary);parent.append(details);parent=details;}
    else{
    const heading=doc.createElement('h3');heading.textContent=title;parent.append(heading);
    }
    const pre=doc.createElement('pre');pre.textContent=value==null?'Not recorded':typeof value==='string'?value:JSON.stringify(value,null,2);parent.append(pre);
  }
  function renderRecord(doc,parent,node,record){
    const article=doc.createElement('article'),heading=doc.createElement('h2');
    heading.textContent=node+' · '+record.id;article.append(heading);
    const question=doc.createElement('p');question.textContent=record.question;article.append(question);
    section(doc,article,'Evidence and status',{kind:record.evidence_kind,status:record.status});
    section(doc,article,'Hypothesis and frozen prediction',{
      hypothesis:record.hypothesis?.revisions?.[(record.protocol?.revision||1)-1],predictions:record.frozen_predictions});
    section(doc,article,'Method and frozen code',record.protocol,true);
    section(doc,article,'Proposal provenance',record.proposer,true);
    section(doc,article,'Actual execution and measurements',record.executions,true);
    section(doc,article,'Independent evaluation',record.evaluation||'Not evaluated');
    section(doc,article,'Model interpretation',record.interpretations);
    section(doc,article,'Next step and remaining uncertainty',record.next_steps);
    parent.append(article);
  }
  if(typeof module==='object' && module.exports)module.exports={loadReports,renderRecord};
  if(typeof window==='undefined')return;
  const read=async path=>{
    const response=await (window.WakePublicData?.fetch || fetch)(path,{
      credentials:'omit',referrerPolicy:'no-referrer',cache:'no-cache',signal:AbortSignal.timeout(12000)});
    if(response.status===404)return null;
    if(!response.ok || !response.body)throw Error('Published audit unavailable');
    const reader=response.body.getReader(),chunks=[];let size=0;
    try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;
      if(size>8*1024*1024)throw Error('Audit exceeds reader limit');chunks.push(value);}}
    finally{await reader.cancel();}
    const bytes=new Uint8Array(size);let offset=0;for(const value of chunks){bytes.set(value,offset);offset+=value.length;}
    return JSON.parse(new TextDecoder().decode(bytes));
  };
  const status=document.getElementById('science-status'),parent=document.getElementById('science-reports');
  const node=window.WAKE_DEPLOYMENT?.public_data?.prefix?.match(/^nodes\/([^/]+)\/$/)?.[1] ||
    new URL(location.href).pathname.match(/\/nodes\/(10[0-3]\.wake|20[0-3]\.wake|30[0-3]\.wake)\/scientific-research\.html$/)?.[1] || null;
  loadReports(read,{node}).then(({manifest,reports,unavailable,absent})=>{
    for(const {node,data} of reports){
      if(data.schema!=='wake-scientific-audit@1' || !Array.isArray(data.investigations))throw Error('Unsupported scientific report');
      section(document,parent,node+' · record provenance',data.source,true);
      section(document,parent,'Scientific progress',data.metrics);
      section(document,parent,'Convergence and unresolved questions',data.convergence_evidence);
      for(const record of data.investigations.slice(-50))renderRecord(document,parent,node,record);
      if(data.investigations.length>50)section(document,parent,'Earlier investigations','Showing the most recent 50; the exported JSON retains the complete report.');
      section(document,parent,'Interpretation limits',data.limits);
    }
    status.textContent=(reports.length?'Published reports: '+reports.length+'.':'No experimental report is published in this selected snapshot.')+
      (manifest?.generated?' Snapshot: '+manifest.generated+'.':'')+
      (window.WakePublicData?.revision?' Public commit: '+window.WakePublicData.revision+'.':'')+
      (absent.length?' No scientific report published for: '+absent.join(', ')+'.':'')+
      (unavailable.length?' Unavailable node reports: '+unavailable.join('; '):'');
  }).catch(error=>{status.textContent='Scientific audit unavailable: '+error.message;});
})();
