/* Disposable same-origin reader views. No worker, record, or provider access. */
(() => {
  'use strict';
  const timeout=()=>AbortSignal.timeout(8000);
  const read=async(path,signal=timeout())=>{
    const response=await (window.WakePublicData?.fetch || fetch)(path,{cache:'no-cache',signal});
    if(!response.ok){const error=Error('Published view unavailable ('+response.status+')');error.status=response.status;throw error;}
    return response.json();
  };
  const recordPath=(collection,id)=>{
    const hex=Array.from(new TextEncoder().encode(id),byte=>byte.toString(16).padStart(2,'0')).join('');
    return 'reader-records/'+collection+'/'+hex.match(/.{1,64}/g).join('/')+'.json';
  };
  async function recentJournal(data){
    if(!data.reader_transport || window.WAKE_DEPLOYMENT?.unified!==true || window.WAKE_DEPLOYMENT?.snapshot_only!==true)return data;
    const signal=AbortSignal.timeout(5000);
    try{
      // Older unified exporters sorted timestamp-free journal rows by node.
      // Recover a bounded recent window from those same snapshot's node records.
      const manifest=await read('installation.json',signal),candidates=new Map();
      if(manifest.schema!==1 || manifest.live!==false || !Array.isArray(manifest.nodes) || manifest.nodes.length!==12 ||
         manifest.installation_id!==window.WAKE_DEPLOYMENT.public_data?.installation_id)return data;
      for(const node of manifest.nodes){
        if(!/^(?:10[0-3]|20[0-3]|30[0-3])\.wake$/.test(node.id) || !/^[a-f0-9]{64}$/.test(manifest.record_heads?.[node.id]?.head||''))continue;
        const status=node.research?.status;
        for(const row of [status?.last_accepted,...(node.research?.activity||[]).filter(row=>row.status==='accepted')]){
          if(!row || !/^[A-Za-z0-9._-]{1,160}$/.test(row.id||''))continue;
          const stamp=Date.parse(row.time);if(!Number.isFinite(stamp)||stamp>Date.now()+60000)continue;
          candidates.set(node.id+'::'+row.id,{node:node.id,id:row.id,stamp});
        }
      }
      const known=new Set(data.state.journal.map(row=>row.invocation));
      const queue=[...candidates.values()].sort((a,b)=>b.stamp-a.stamp).slice(0,8).filter(row=>!known.has(row.node+'::'+row.id));
      async function worker(){
        while(queue.length){
          const row=queue.shift(),qualified=row.node+'::'+row.id;
          try{
            const packet=await read('nodes/'+row.node+'/'+recordPath('journal',row.id),signal);
            const receipt=packet.related?.invocations?.[row.id];
            if(packet.head!==manifest.record_heads[row.node].head || packet.collection!=='journal' ||
               packet.item?.invocation!==row.id || receipt?.status!=='accepted')continue;
            const origin={node:row.node,...manifest.record_heads[row.node]};
            data.state.journal.push({...packet.item,invocation:qualified,origin});
            data.state.invocations[qualified]={...Object.fromEntries(Object.entries(receipt).filter(([key])=>
              ['time','finished','status','provider','model','phase'].includes(key))),id:qualified,origin};
          }catch{}
        }
      }
      await Promise.all(Array.from({length:Math.min(3,queue.length)},worker));
      const stamp=row=>Date.parse(data.state.invocations[row.invocation]?.finished||data.state.invocations[row.invocation]?.time||row.time)||0;
      data.state.journal.sort((a,b)=>stamp(a)-stamp(b));
    }catch{}
    return data;
  }
  window.WakeLiveUrl='reader-data.json';
  window.WakeData=read(window.WakeLiveUrl).catch(error=>{
    // Older completed exports have no bootstrap. A broken new export must be
    // visible rather than silently downloading the complete archive instead.
    if(![404,410].includes(error.status))throw error;
    window.WakeLiveUrl='wake-data.json';return read(window.WakeLiveUrl);
  }).then(recentJournal).then(data=>{data.public_cycle=Number(data.state?.version||0);return data;});
  const loaded=new Set(),pages=new Map();
  const merge=(data,packet)=>{
    if(packet.head!==data.head)throw Error('The published snapshot changed. Reload to read its current details.');
    if(packet.item){
      if(packet.collection==='journal'){
        if(!data.state.journal.some(row=>row.invocation===packet.item.invocation))data.state.journal.push(packet.item);
      }else data.state[packet.collection][packet.item.id]=packet.item;
    }
    for(const [name,items] of Object.entries(packet.related||{}))Object.assign(data.state[name]||={},items);
    const known=new Set(data.events.map(event=>event.projection_id||event.hash));
    for(const event of packet.events||[])if(!known.has(event.projection_id||event.hash))data.events.push(event);
  };
  window.WakeReader={
    reset(){loaded.clear();pages.clear();},
    async ensure(page,id){
      const data=await window.WakeData;if(!data.reader_transport)return;
      const listing=({journal:'journal',history:'events',evidence:'evidence'})[page];
      if(listing && window.WakePublicData?.mode==='bundled' && window.WakePublicData.limited && (!id||id.startsWith('filter:')||id.startsWith('topic:')))return;
      if(listing && (!id||id.startsWith('filter:')||id.startsWith('topic:'))){if(!pages.has(listing))await this.more(listing);return;}
      let collection=({blog:'posts',evidence:'evidence',history:'invocations',projects:'projects',journal:'journal'})[page];
      if(!collection||!id||id.startsWith('topic:')||id.startsWith('filter:'))return;
      if(page==='projects'&&id.startsWith('notebook:')){collection='notebooks';id=id.slice(9);}
      const path=recordPath(collection,id),key=data.head+':'+path;if(loaded.has(key))return;
      const packet=await read(path);
      if(packet.collection!==collection||!packet.item||
        (collection==='journal'?'cycle:'+packet.item.cycle:packet.item.id)!==id)throw Error('The exported detail does not match the selected record.');
      if(packet.head!==data.head){
        // Pages may serve a cached overview beside a newly published detail.
        // Adopt only a matching bounded overview; never combine generations.
        const next=await read('reader-data.json?head='+encodeURIComponent(packet.head));
        if(!next?.state||next.authoritative===true||next.head!==packet.head||!next.reader_transport)
          throw Error('The site is updating. Please retry opening this article.');
        merge(next,packet);loaded.clear();pages.clear();loaded.add(next.head+':'+path);
        if(typeof window.WakeApplyLive==='function')window.WakeApplyLive(next);
        else{
          const state=data.state;
          for(const name of Object.keys(state))delete state[name];
          Object.assign(state,next.state);Object.assign(data,next,{state});
        }
        return;
      }
      merge(data,packet);loaded.add(key);
    },
    hasMore(collection){return pages.get(collection)!==null;},
    async more(collection){
      const data=await window.WakeData;if(!data.reader_transport)return false;
      const index=pages.get(collection)??0;if(index===null)return false;
      const packet=await read('reader-records/pages/'+collection+'/'+index+'.json');
      if(packet.collection!==collection||!Array.isArray(packet.rows))throw Error('The exported page does not match this list.');
      merge(data,packet);
      if(collection==='events'){
        const known=new Set(data.events.map(event=>event.projection_id||event.hash));
        data.events.push(...packet.rows.filter(event=>!known.has(event.projection_id||event.hash)));
        data.events.sort((a,b)=>String(a.time).localeCompare(String(b.time)));
      }else if(collection==='journal'){
        const known=new Set(data.state.journal.map(row=>row.invocation));
        data.state.journal.unshift(...packet.rows.filter(row=>!known.has(row.invocation)).reverse());
      }else for(const item of packet.rows)data.state[collection][item.id]=item;
      pages.set(collection,packet.next);return packet.next!==null;
    }
  };
  window.WakeData.then(()=>{
    if(window.WAKE_DEPLOYMENT?.snapshot_only===true)return;
    let marker;
    const poll=async()=>{
      try{
        if(!document.hidden){
          // The full browser archive is never a live polling channel.
          const response=await (window.WakePublicData?.fetch || fetch)('head.txt',{cache:'no-cache',signal:timeout()});
          if(response.ok){const head=(await response.text()).trim();
            if(marker&&head!==marker){const next=await read(window.WakeLiveUrl);window.WakeReader.reset();window.WakeApplyLive?.(next);}
            marker=head;
          }
        }
      }catch{}
      setTimeout(poll,10000);
    };
    window.WakeData.then(data=>{marker=data.head;setTimeout(poll,10000);});
  }).catch(()=>{});
})();
