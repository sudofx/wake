/* Published controlled evaluations are separate from native research records. */
((root)=>{
  'use strict';
  async function mount(container){
    if(!container||container.querySelector('[data-evaluation]'))return;
    const section=document.createElement('section');section.className='panel';section.dataset.evaluation='';
    const title=document.createElement('h2');title.textContent='Controlled evaluation';section.append(title);container.prepend(section);
    try{
      const repository=root.WAKE_DEPLOYMENT?.public_data?.repository;
      if(repository&&!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository))throw Error('Invalid repository');
      const url=repository?'https://raw.githubusercontent.com/'+repository+'/wake-evaluations/latest.json':new URL('evaluation.json',document.baseURI).href;
      const response=await fetch(url,{credentials:'omit',cache:'no-cache',signal:AbortSignal.timeout(8000)});
      if(!response.ok)throw Error('No published evaluation');
      const reader=response.body.getReader(),chunks=[];let size=0;
      try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>2097152)throw Error('Evaluation exceeds reading limit');chunks.push(value);}}finally{await reader.cancel();}
      const bytes=new Uint8Array(size);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
      const report=JSON.parse(new TextDecoder().decode(bytes));
      if(report.schema!=='wake-evaluation@1'||typeof report.result_id!=='string'||typeof report.title!=='string'||!Array.isArray(report.metrics)||report.metrics.length>32||!Array.isArray(report.limitations))throw Error('Unsupported evaluation');
      title.textContent=report.title;
      const stamp=document.createElement('p');stamp.textContent=report.generated_at+' · '+report.result_id;section.append(stamp);
      const summary=document.createElement('p');summary.textContent=report.summary;section.append(summary);
      const table=document.createElement('table');
      for(const metric of report.metrics){const row=document.createElement('tr');for(const value of [metric.name,metric.value]){const cell=document.createElement('td');cell.textContent=String(value);row.append(cell);}table.append(row);}section.append(table);
      for(const text of report.limitations){const p=document.createElement('p');p.className='small';p.textContent=text;section.append(p);}
      section.dataset.resultId=report.result_id;
    }catch{section.remove();}
  }
  root.WakeEvaluation={mount};
})(window);
