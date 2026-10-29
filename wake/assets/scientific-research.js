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
  function text(doc,parent,tag,value){
    const element=doc.createElement(tag);element.textContent=value;parent.append(element);return element;
  }
  function paragraph(doc,parent,title,value){
    text(doc,parent,'h3',title);text(doc,parent,'p',typeof value==='string'&&value?value:'Not recorded yet.');
  }
  function list(doc,parent,values){
    const items=Array.isArray(values)?values.filter(v=>typeof v==='string'&&v):[];
    if(!items.length)return;
    const ul=doc.createElement('ul');for(const value of items)text(doc,ul,'li',value);parent.append(ul);
  }
  const metricLabels={A_accuracy:'Correct answers without relevant history',B_accuracy:'Correct answers with relevant history',
    C_accuracy:'Correct answers with compressed history',accuracy:'Correct answers in this test',
    holdout_accuracy:'Correct predictions on unseen cases',probe_accuracy:'Correct predictions on initial tests',
    accuracy_gain_B_over_A:'Improvement with relevant history',accuracy_gain_C_over_B:'Difference with compressed history',
    cases:'Cases tested',errors:'Incorrect predictions'};
  function quantity(key,value){
    if(typeof value!=='number'||!Number.isFinite(value))return 'Not available';
    const number=n=>String(Math.round(n*100)/100);
    if(key.startsWith('accuracy_gain_'))return number(value*100)+' percentage points';
    if(key.includes('accuracy'))return number(value*100)+'%';
    return number(value);
  }
  function predictionText(prediction){
    const name=metricLabels[prediction.metric],comparison={gte:'at least',gt:'more than',lte:'at most',lt:'less than',eq:'equal to',ne:'different from'}[prediction.operator];
    if(!name||!comparison||typeof prediction.value!=='number')return 'The exact prediction is available in the technical record.';
    return name+' should be '+comparison+' '+quantity(prediction.metric,prediction.value)+'.';
  }
  function renderRecord(doc,parent,node,record){
    const article=doc.createElement('article');
    const repeated=['replicated','replication_failed'].includes(record.evaluation?.replication_status);
    text(doc,article,'h2',repeated?'A repeat test':record.question||'An investigation');
    if(repeated&&record.question)text(doc,article,'p',record.question);
    text(doc,article,'p',record.evidence_kind==='synthetic_benchmark'?
      'A controlled synthetic test. Its results do not establish what happens in nature.':'A computational observation. Its limits are described below.');
    const evaluation=record.evaluation;
    const outcome={provisionally_supported:'The prediction was supported in this test.',contradicted:'The prediction was contradicted in this test.',
      inconclusive:'The test was inconclusive.',invalid_measurement:'The measurements could not be validated.',
      observation_only:'An observation is available; the hypothesis has not been validated.'};
    text(doc,article,'h3','An independent check');
    text(doc,article,'p',evaluation?.execution_valid===false?'The test did not execute correctly. It cannot settle the prediction.':
      outcome[evaluation?.outcome]||'This experiment has not produced an evaluated result yet.');
    const definition=record.hypothesis?.revisions?.[(record.protocol?.revision||1)-1]?.definition;
    paragraph(doc,article,'The explanation being tested',definition?.statement);
    text(doc,article,'h3','What was predicted before the test');
    const predictions=Array.isArray(record.frozen_predictions)?record.frozen_predictions:[];
    if(predictions.length)list(doc,article,predictions.map(predictionText));
    else text(doc,article,'p','No prediction has been recorded.');
    text(doc,article,'h3','What happened');
    const metrics=evaluation?.metrics||{},rows=[];
    // Show one unseen-case accuracy value, not both aliases for the same score.
    for(const key of ['A_accuracy','B_accuracy','C_accuracy','accuracy_gain_B_over_A','accuracy_gain_C_over_B',metrics.holdout_accuracy!==undefined?'holdout_accuracy':'accuracy','probe_accuracy','cases','errors']){
      if(typeof metrics[key]==='number'&&Number.isFinite(metrics[key]))rows.push([metricLabels[key],quantity(key,metrics[key])]);
    }
    if(rows.length){const dl=doc.createElement('dl');for(const [label,value] of rows){text(doc,dl,'dt',label);text(doc,dl,'dd',value);}article.append(dl);}
    else text(doc,article,'p','No summary measurements are available yet.');
    if(evaluation?.measurement_validity&&evaluation.measurement_validity!=='validated')
      text(doc,article,'p','These measurements have not passed independent validation.');
    const replication={replicated:'A repeat test reproduced the recorded result.',replication_failed:'A repeat test did not reproduce the recorded result.',
      not_attempted:'This result has not been replicated yet.'};
    text(doc,article,'p',replication[evaluation?.replication_status]||'Replication has not been established.');
    const interpretations=Array.isArray(record.interpretations)?record.interpretations:[];
    paragraph(doc,article,'Model explanation — not an independent finding',interpretations.at(-1)?.interpretation||'No model explanation has been recorded.');
    const decisions=Array.isArray(record.next_steps)?record.next_steps:[],decision=decisions.at(-1);
    paragraph(doc,article,'What remains unknown',decision?.uncertainty||definition?.uncertainty);
    if(decision?.next_experiment)paragraph(doc,article,'A possible next test',decision.next_experiment);
    if(decision?.reason)paragraph(doc,article,decision.decision==='close'?'Why this investigation stopped':'Why this is the next step',decision.reason);
    if(decision?.decision==='close')text(doc,article,'p','Stopping an investigation does not mean its scientific question is settled.');
    if(evaluation?.evaluator==='historical-correction@1')text(doc,article,'p',
      'This small comparison does not establish a general reasoning benefit. In some tasks, history supplied extra facts. Other tasks supplied the same facts in every condition. Those are different tests of what history helps with.');
    section(doc,article,'Technical record for researchers and developers',{node,...record},true);
    parent.append(article);
  }
  function renderReport(doc,parent,node,data){
    const report=doc.createElement('section');
    text(doc,report,'h2','Recorded progress');
    const counts=data.metrics||{},items=[];
    for(const [key,singular,plural] of [['hypotheses_formulated','hypothesis or revision recorded','hypotheses and revisions recorded'],['completed_executions','test run completed','test runs completed'],
      ['valid_measurements','measurement independently validated','measurements independently validated'],['successful_replications','successful repeat test','successful repeat tests']])
      if(Number.isSafeInteger(counts[key]))items.push(counts[key]+' '+(counts[key]===1?singular:plural));
    list(doc,report,items);
    for(const record of data.investigations.slice(-50))renderRecord(doc,report,node,record);
    if(data.investigations.length>50)text(doc,report,'p','Showing the most recent 50 investigations. The technical export retains the full report.');
    paragraph(doc,report,'Limits of these findings','These results apply to the tests we ran. They do not establish a general rule about intelligence, natural systems or people. Unanswered questions remain open even when an investigation stops.');
    section(doc,report,'Report metadata for researchers and developers',{node,source:data.source,metrics:data.metrics,convergence:data.convergence_evidence,limits:data.limits},true);
    parent.append(report);
  }
  function emptyStatus(manifest){
    const nodes=manifest?.nodes||[],states=nodes.map(node=>node.research?.status?.experimental_research?.enabled);
    const enabled=states.filter(value=>value===true).length;
    if(enabled)return 'Experiment execution is recorded as enabled on '+enabled+' '+(enabled===1?'node':'nodes')+', but no experiment results have been published yet. Enabled does not mean a test is currently running.';
    if(states.length&&states.every(value=>value===false))return 'Experiment execution is switched off in this snapshot. No experiment results have been published.';
    return 'No experiment results have been published. This snapshot does not report whether experiment execution is enabled.';
  }
  if(typeof module==='object' && module.exports)module.exports={loadReports,renderRecord,renderReport,emptyStatus};
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
      renderReport(document,parent,node,data);
    }
    status.textContent=reports.length?'Results from '+reports.length+' published research '+(reports.length===1?'report.':'reports.'):
      emptyStatus(manifest);
    if(manifest?.generated){const date=new Date(manifest.generated);if(!Number.isNaN(date.getTime()))status.textContent+=' Updated '+date.toLocaleString()+'.';}
    if(unavailable.length)status.textContent+=' Some reports could not be loaded; this view may be incomplete.';
    else if(reports.length&&absent.length)status.textContent+=' Some reports have not been published yet.';
    section(document,parent,'Snapshot details for researchers and developers',{
      captured_at:manifest?.generated||null,public_commit:window.WakePublicData?.revision||null,absent,unavailable},true);
  }).catch(error=>{
    status.textContent='The experiment results could not be loaded. Try refreshing this page.';
    section(document,parent,'Loading diagnostics for researchers and developers',{error:error.message},true);
  });
})();
