/* One pinned public GitHub export per document. Never operational authority. */
(() => {
  'use strict';
  const config=window.WAKE_DEPLOYMENT?.public_data;
  if(!config || window.WAKE_DEPLOYMENT?.snapshot_only!==true)return;
  const own=new URL('.',document.currentScript.src),prefix=config.prefix||'';
  if(!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(config.repository) || config.branch!=='wake-public' ||
     typeof config.installation_id!=='string' || !config.installation_id ||
     !/^(?:nodes\/(?:10[0-3]|20[0-3]|30[0-3])\.wake\/)?$/.test(prefix))return;
  const site=new URL(prefix?'../../':'./',own),key='wake-public-snapshot:'+config.repository+':'+config.installation_id;
  const requested=new URL(location.href).searchParams.get('public_revision');
  const nativeFetch=globalThis.fetch.bind(globalThis);
  const json=async(url,limit)=>{
    const response=await nativeFetch(url,{credentials:'omit',referrerPolicy:'no-referrer',cache:'no-cache',signal:AbortSignal.timeout(8000)});
    if(!response.ok || !response.body)throw Error('Public snapshot unavailable');
    const reader=response.body.getReader(),chunks=[];let size=0;
    try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>limit)throw Error('Public snapshot metadata exceeds limit');chunks.push(value);}}finally{await reader.cancel();}
    const bytes=new Uint8Array(size);let offset=0;for(const value of chunks){bytes.set(value,offset);offset+=value.length;}
    return JSON.parse(new TextDecoder().decode(bytes));
  };
  const notice=()=>{
    const show=()=>{
      const node=document.createElement('p');node.id='public-data-notice';node.setAttribute('role','status');
      node.textContent='Latest published data is unavailable. Showing the snapshot bundled with this website; current research activity is unknown.';
      node.style.cssText='margin:1rem;padding:.7rem;border:1px solid currentColor;font:inherit';
      document.querySelector('main')?.prepend(node);
    };
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',show,{once:true});else show();
  };
  const transport={revision:null,mode:'loading'};
  transport.ready=(async()=>{
    try{
      if(requested==='bundled'){transport.mode='bundled';notice();return null;}
      if(requested && !/^[a-f0-9]{40}$/.test(requested))throw Error('Invalid snapshot revision');
      let revision=requested,discovered=false;
      if(!revision && window.parent!==window){
        try{
          const parent=window.parent.WakePublicData;
          if(parent){await parent.ready;if(parent.mode==='bundled'){transport.mode='bundled';notice();return null;}revision=parent.revision;}
        }catch{throw Error('Parent snapshot unavailable');}
      }
      if(!revision){
        try{const cached=JSON.parse(localStorage.getItem(key));if(cached?.time<=Date.now() && Date.now()-cached.time<180000 && /^[a-f0-9]{40}$/.test(cached.revision))revision=cached.revision;}catch{}
        if(!revision){
          const head=await json('https://api.github.com/repos/'+config.repository+'/git/ref/heads/'+config.branch,16384);
          if(head.object?.type!=='commit' || !/^[a-f0-9]{40}$/.test(head.object.sha))throw Error('Invalid public revision');revision=head.object.sha;discovered=true;
        }
      }
      const root=new URL('https://raw.githubusercontent.com/'+config.repository+'/'+revision+'/');
      const manifest=await json(new URL('installation.json',root),524288);
      if(manifest.schema!==1 || manifest.installation_id!==config.installation_id || manifest.live!==false ||
         !Array.isArray(manifest.nodes) || manifest.nodes.length!==12 || Object.keys(manifest.record_heads||{}).length!==12)
        throw Error('Public installation changed');
      transport.revision=revision;transport.mode='published';
      // Navigating must not extend discovery's TTL indefinitely.
      if(discovered)try{localStorage.setItem(key,JSON.stringify({revision,time:Date.now()}));}catch{}
      return root;
    }catch(error){
      // A popup must read the source version its opener selected. Falling back
      // here would present a different context under the same conversation.
      if(requested){transport.mode='unavailable';throw Error('The selected published snapshot is unavailable. Reopen Bob from a current page.');}
      transport.mode='bundled';notice();return null;
    }
  })();
  const targetFor=(input,root)=>{
    const url=new URL(input,location.href);
    if(url.origin!==site.origin || !url.pathname.startsWith(site.pathname))throw Error('Public data must belong to this installation');
    const relative=url.pathname.slice(site.pathname.length);
    if(!/^(?:nodes\/(?:10[0-3]|20[0-3]|30[0-3])\.wake\/)?(?:(?:reader-records|research-details|research|map3d|group)\/[A-Za-z0-9_./-]+\.json|inspect\/[A-Za-z0-9_./-]+\.(?:json|md)|(?:installation|reader-data|wake-data|research-overview|research-data|research-expansion|map-data|map3d-data|state|export-format)\.json|head\.txt|events\.jsonl(?:\.gz)?)$/.test(relative))throw Error('Not a published data path');
    return root?new URL(relative,root):url;
  };
  transport.resolve=async input=>targetFor(input,await transport.ready).href;
  transport.fetch=async(input,options={})=>{
    const target=await transport.resolve(input);
    const settings={...options,credentials:'omit',referrerPolicy:'no-referrer',signal:options.signal||AbortSignal.timeout(12000)};
    delete settings.headers;delete settings.body;settings.method='GET';
    return nativeFetch(target,settings);
  };
  // Readers may attach their own error UI after parsing; keep early failures
  // from becoming unhandled promise rejections before those readers attach.
  transport.ready.catch(()=>{});
  transport.pin=url=>{if(transport.revision || transport.mode==='bundled')url.searchParams.set('public_revision',transport.revision||'bundled');return url;};
  window.WakePublicData=transport;
  // Export/download links must identify the same evidence as the displayed UI.
  // This also covers links inserted later by the existing view renderers.
  transport.ready.then(root=>{
    if(!root)return;
    const update=node=>{
      const links=node.matches?.('a[href]')?[node]:node.querySelectorAll?.('a[href]')||[];
      for(const link of links)try{
        // The external inspection entry is a self-contained document. Read its
        // exact packet rather than loading executable HTML from a data branch.
        const input=/\/inspect\/index\.html$/.test(new URL(link.href).pathname)?new URL('packet.md',link.href):link.href;
        const target=targetFor(input,root);if(target.href!==link.href){link.href=target.href;link.target='_blank';link.rel='noopener';}
      }catch{}
    };
    const watch=()=>{
      update(document);
      new MutationObserver(records=>{for(const record of records){if(record.type==='attributes')update(record.target);else for(const node of record.addedNodes)update(node);}})
        .observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['href']});
    };
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',watch,{once:true});else watch();
  }).catch(()=>{});
})();
