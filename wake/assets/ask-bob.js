/* Private browser conversation views; never research authority or exported state. */
(() => {
  'use strict';
  const MAX_BYTES=32768,MAX_ARTICLES=20,MAX_TURNS=10;
  const bytes=value=>new TextEncoder().encode(JSON.stringify(value)).length;
  const text=(value,limit)=>typeof value==='string'?Array.from(value).slice(0,limit).join(''):'';
  const hash=value=>typeof value==='string'&&/^[a-f0-9]{64}$/.test(value)?value:'';
  const report=value=>['understood','unsure'].includes(value)?value:null;
  const turn=value=>({id:text(value?.id,100),article_id:text(value?.article_id,240),
    article_hash:hash(value?.article_hash),head:text(value?.head,100),
    question:text(value?.question,2000),answer:text(value?.answer,6000),
    self_report:report(value?.self_report),understanding:report(value?.self_report)?'self_reported':'unknown',time:text(value?.time,100)});
  function bounded(value){
    const entries=Array.isArray(value?.articles)?value.articles:[];
    const seen=new Set();
    const articles=entries.slice(-MAX_ARTICLES).filter(row=>{
      if(!row||!text(row.id,240)||seen.has(row.id))return false;
      seen.add(row.id);return true;
    }).map(row=>({id:text(row.id,240),hash:hash(row.hash),head:text(row.head,100),
      opened:true,encountered_at:text(row.encountered_at,100),self_report:report(row.self_report),
      versions:(Array.isArray(row.versions)?row.versions:[]).slice(-3).map(version=>({hash:hash(version?.hash),head:text(version?.head,100),encountered_at:text(version?.encountered_at,100)})).filter(version=>version.hash),
      turns:(Array.isArray(row.turns)?row.turns:[]).slice(-MAX_TURNS).map(turn).filter(value=>value.article_id&&value.article_hash)}));
    const result={schema:1,articles};
    // Evict whole oldest turns, then oldest articles. Never silently rewrite an answer.
    while(bytes(result)>MAX_BYTES&&articles.length){
      const oldest=articles.find(row=>row.turns.length);
      if(oldest)oldest.turns.shift();else articles.shift();
    }
    return result;
  }
  function storage(installation){
    const key='wake-ask-bob:'+encodeURIComponent(location.origin)+':'+encodeURIComponent(installation);
    let value={schema:1,articles:[]},available=true,damaged=false;
    try{value=bounded(JSON.parse(localStorage.getItem(key)||'null'));}catch(error){if(error instanceof SyntaxError)damaged=true;else available=false;}
    const save=()=>{
      value=bounded(value);
      try{localStorage.setItem(key,JSON.stringify(value));}catch{available=false;}
    };
    return {get value(){return value;},get available(){return available;},get damaged(){return damaged;},key,save,
      clear(){value={schema:1,articles:[]};damaged=false;try{localStorage.removeItem(key);}catch{available=false;}}};
  }
  let capability;
  const capabilities=()=>capability||(capability=window.WAKE_DEPLOYMENT?.snapshot_only===true?
    fetch('installation.json',{cache:'no-cache',credentials:'omit',signal:AbortSignal.timeout(5000)})
      .then(async response=>{
        const value=response.ok?await response.json():null;
        return typeof value?.installation_id==='string'&&value.installation_id?
          {enabled:true,token:'browser-only',installation_id:value.installation_id,browser:true}:null;
      }).catch(()=>null):fetch('/ask-bob/capabilities',{
    cache:'no-store',credentials:'same-origin',signal:AbortSignal.timeout(5000)
  }).then(async response=>response.ok?response.json():null).catch(()=>null));
  let browserRuntime;
  // Replace the broken startup module without invalidating the large model cache.
  const browser=async()=>browserRuntime||(browserRuntime=await import(new URL('ask-bob-browser.js?build=reply-validation-1',document.baseURI).href));
  function element(tag,content,className){
    const node=document.createElement(tag);if(content!==undefined)node.textContent=content;
    if(className)node.className=className;return node;
  }
  function safeURL(value){
    if(typeof value!=='string')return null;
    try{const url=new URL(value,location.href);return ['http:','https:'].includes(url.protocol)?url.href:null;}catch{return null;}
  }
  async function mount(container,{post,head=''}){
    // The unified blog owns cross-node source IDs; individual node pages do not.
    if(!container||!post?.id||/\/nodes(?:\/|$)/.test(location.pathname))return;
    const route=location.href,valid=()=>container.isConnected&&location.href===route;
    const cap=await capabilities();
    if(!valid()||!cap?.enabled||typeof cap.token!=='string'||!cap.token||typeof cap.installation_id!=='string'||!cap.installation_id)return;
    if(container.querySelector('.ask-bob'))return;
    const store=storage(cap.installation_id);
    const descriptor=post._reader_article,displayedHash=hash(descriptor?.hash);
    let current=store.value.articles.find(row=>row.id===post.id);
    let previous=current?{id:current.id,hash:current.hash,head:current.head,exposure:{opened:true},self_report:current.self_report}:null;
    let priorHash=previous?.hash&&displayedHash&&previous.hash!==displayedHash?previous.hash:'';
    if(!current){current={id:text(post.id,240),hash:displayedHash,head:text(descriptor?.head||head,100),opened:true,self_report:null,turns:[],versions:[]};store.value.articles.push(current);}
    else{store.value.articles.splice(store.value.articles.indexOf(current),1);store.value.articles.push(current);}
    if(displayedHash){
      if(current.hash!==displayedHash){
        if(current.hash)(current.versions||=[]).push({hash:current.hash,head:current.head,encountered_at:current.encountered_at});
        current.self_report=null;
      }
      current.hash=displayedHash;current.head=text(descriptor?.head||head,100);
    }
    current.encountered_at=new Date().toISOString();
    persist();
    let epoch=0,active;
    const panel=element('details',undefined,'ask-bob');
    panel.append(element('summary','Ask Bob about this article'));
    panel.append(element('p','Questions and replies are private conversation aids, not accepted research. Opening an article records exposure, not comprehension.'));
    const privacy=element('p',cap.browser?
      'No sign-in or API key. Bob runs on your device using a small model, with answers that may be less accurate than cloud models. Loading it downloads about 491 MB from Hugging Face; your browser may cache it. Questions and saved replies stay in this browser and never enter the research record.':
      'History stays in this browser. Your question and selected context go to the local answer service and its configured model; they are excluded from public exports.','ask-bob-note');panel.append(privacy);
    let modelReady=!cap.browser,modelLoadCancelled=false;
    const loadModel=cap.browser?element('button','Load Bob on this device (491 MB)'):null;
    const cancelModel=cap.browser?element('button','Cancel loading'):null;
    if(loadModel){loadModel.type='button';cancelModel.type='button';cancelModel.hidden=true;panel.append(loadModel,cancelModel);}
    const form=element('form'),label=element('label','Your question'),question=element('textarea');
    question.required=true;question.maxLength=2000;question.rows=3;question.setAttribute('aria-label','Your question');label.append(question);form.append(label);
    const contextLabel=element('label','Conversation context'),condition=element('select');condition.setAttribute('aria-label','Conversation context');
    for(const [value,title] of [['A','No prior conversation (A)'],['B','Full prior conversation (B)'],['C','Compact prior conversation (C)']]){const option=element('option',title);option.value=value;condition.append(option);}condition.value='C';contextLabel.append(condition);form.append(contextLabel);
    const submit=element('button','Ask Bob');submit.type='submit';submit.disabled=!displayedHash||!modelReady;form.append(submit);panel.append(form);
    const status=element('p','', 'ask-bob-status');status.setAttribute('role','status');panel.append(status);
    const conversation=element('div',undefined,'ask-bob-conversation');conversation.setAttribute('aria-live','polite');panel.append(conversation);
    const understandingLabel=element('label','Your understanding of this exact article version (optional)'),understanding=element('select');understanding.setAttribute('aria-label','Your understanding of this article version');
    for(const [value,title] of [['','Not reported'],['understood','I understand it'],['unsure','I am unsure']]){const option=element('option',title);option.value=value;understanding.append(option);}understanding.value=current.self_report||'';understanding.disabled=!current.hash;understandingLabel.append(understanding);panel.append(understandingLabel);
    const inspect=element('details'),summary=element('summary','Inspect private browser history'),historyView=element('pre');inspect.append(summary,historyView);panel.append(inspect);
    const clear=element('button','Clear private browser history');clear.type='button';panel.append(clear);
    container.append(panel);
    function persist(){store.save();current=store.value.articles.find(row=>row.id===post.id)||current;}
    function refresh(){
      historyView.textContent=JSON.stringify(store.value,null,2);
      if(!store.available)status.textContent='Browser storage is unavailable. This conversation can continue in memory; it may be lost when you leave.';
      else if(store.damaged)status.textContent='Stored browser history could not be read. Starting a new local history; missing entries have not been reconstructed.';
    }
    function display(value){
      const item=element('div',undefined,'ask-bob-turn');item.append(element('p','You: '+value.question));item.append(element('p',value.answer,'ask-bob-answer'));conversation.append(item);
    }
    current.turns.forEach(display);refresh();
    if(loadModel){
      cancelModel.addEventListener('click',()=>{modelLoadCancelled=true;browserRuntime?.cancelLoad?.();});
      loadModel.addEventListener('click',async()=>{
        modelLoadCancelled=false;loadModel.disabled=true;cancelModel.hidden=false;
        try{
          const runtime=await browser();
          if(modelLoadCancelled)throw new DOMException('Bob loading cancelled.','AbortError');
          await runtime.load(message=>{if(valid())status.textContent=message;});
          modelReady=true;
          if(valid()){loadModel.hidden=true;submit.disabled=!displayedHash;}
        }catch(error){if(valid())status.textContent=text(error.message,500)||'Bob could not load on this device.';}
        finally{if(valid()){loadModel.disabled=false;cancelModel.hidden=true;}}
      });
      status.textContent='Load Bob once before asking. It can take time and needs available device memory. Reading the article does not load the model.';
    }
    if(!displayedHash)status.textContent='This article has no verified display version. Reload a newly exported snapshot before asking a question.';
    understanding.addEventListener('change',()=>{
      // No reading-duration or navigation inference can set a self-report.
      if(!current.hash)return;if(!store.value.articles.includes(current))store.value.articles.push(current);current.self_report=report(understanding.value);
      // Earlier turns retain their original metadata for compressed-context hashes.
      // The current report applies now and is captured by subsequent interactions.
      persist();refresh();
    });
    clear.addEventListener('click',()=>{
      epoch++;active?.abort();previous=null;priorHash='';store.clear();current={id:text(post.id,240),hash:displayedHash,head:text(descriptor?.head||head,100),opened:true,encountered_at:new Date().toISOString(),self_report:null,turns:[],versions:[]};
      conversation.replaceChildren();historyView.textContent=JSON.stringify(store.value,null,2);
      understanding.value='';understanding.disabled=!displayedHash;submit.disabled=!displayedHash||!modelReady;status.textContent='Private browser history cleared.';
    });
    form.addEventListener('submit',async event=>{
      event.preventDefault();if(submit.disabled||!valid())return;
      const asked=question.value.trim();if(!asked)return;
      const mode=condition.value,requestEpoch=epoch;
      const requestValid=()=>valid()&&requestEpoch===epoch;
      const body={article_id:post.id,question:asked,condition:mode,expected_article_hash:displayedHash,
        history:mode==='A'?[]:store.value.articles.flatMap(row=>row.turns).sort((a,b)=>a.time.localeCompare(b.time)||a.id.localeCompare(b.id)).slice(-MAX_TURNS),
        previous_article:mode==='A'?null:(priorHash?previous:{id:current.id,hash:current.hash||undefined,head:current.head,exposure:{opened:true},self_report:current.self_report})};
      if(mode!=='A'&&priorHash)body.prior_article_hash=priorHash;
      submit.disabled=true;status.textContent=cap.browser?'Bob is answering on your device. Keep this tab open; slower devices can take a few minutes…':'Preparing an answer from this article and its recorded sources…';
      const controller=new AbortController();active=controller;const timeout=setTimeout(()=>controller.abort(),cap.browser?300000:120000);
      const leave=()=>controller.abort();window.addEventListener('hashchange',leave,{once:true});
      try{
        let result,responseOK=true;
        if(cap.browser){result=await (await browser()).answer(body,controller.signal);}
        else{
          const response=await fetch('/ask-bob',{method:'POST',credentials:'same-origin',cache:'no-store',
            headers:{'Content-Type':'application/json','X-Wake-Reader-Token':cap.token},body:JSON.stringify(body),signal:controller.signal});
          responseOK=response.ok;result=await response.json();
        }
        if(!requestValid())return;
        if(!responseOK||result.ok===false){
          const unavailable={busy:'The answer service is busy. Try again shortly.',busy_or_unavailable:'The answer service is busy or unavailable. Try again shortly.',paused:'Reader questions are paused.',session_limit:'This local preview has reached its question limit.',provider_deferred_or_failed:'The configured model deferred or could not complete this answer. Try again later.',invalid_or_unavailable_article:'This article is unavailable or has changed. Reload it before asking again.'};
          throw Error(unavailable[result.error]||'The answer service could not complete this question. Try again later.');
        }
        if(typeof result.answer!=='string'||result.article?.id!==post.id||result.article?.hash!==displayedHash)throw Error('The answer did not identify this article version.');
        if(current.hash&&current.hash!==result.article.hash){current.self_report=null;understanding.value='';}
        current.hash=result.article.hash;current.head=text(result.article.head,100);understanding.disabled=false;
        const value=turn({id:crypto.randomUUID(),article_id:post.id,article_hash:current.hash,head:current.head,question:asked,answer:result.answer,self_report:current.self_report,time:new Date().toISOString()});
        if(!store.value.articles.includes(current))store.value.articles.push(current);
        current.turns.push(value);persist();display(value);question.value='';priorHash='';previous=null;
        const links=element('ul');
        for(const source of Array.isArray(result.citations)?result.citations:[]){const href=safeURL(source.url||source.path);if(!href)continue;const item=element('li'),link=element('a',text((source.id?source.id+' · ':'')+(source.title||source.label||'Source'),300));link.href=href;link.rel='noopener noreferrer';if(new URL(href).origin!==location.origin)link.target='_blank';item.append(link);links.append(item);}if(links.children.length)conversation.append(links);
        const metrics=element('details'),metricsTitle=element('summary','Response details'),metricsList=element('dl');
        const fields={condition:'Context condition',source_records:'Source records',context_bytes:'Input bytes',source_bytes_read:'Source bytes read',output_bytes:'Output bytes',latency_ms:'Response time (ms)',history_input_turns:'History turns supplied',history_selected_turns:'History turns selected',history_omitted_turns:'History turns omitted'};
        for(const [key,label] of Object.entries(fields)){
          const metric=result.metrics?.[key];if(typeof metric==='number'&&Number.isFinite(metric)||key==='condition'&&['A','B','C'].includes(metric)){metricsList.append(element('dt',label),element('dd',String(metric)));}
        }
        for(const key of ['promptTokenCount','candidatesTokenCount','totalTokenCount','thoughtsTokenCount']){
          const count=result.metrics?.provider_tokens?.[key];if(Number.isInteger(count)&&count>=0)metricsList.append(element('dt',key),element('dd',String(count)));
        }
        if(metricsList.children.length){metrics.append(metricsTitle,metricsList);conversation.append(metrics);}
        const notices=[...(Array.isArray(result.missing)?result.missing:[]),...(Array.isArray(result.warnings)?result.warnings:[])];
        status.textContent=notices.map(value=>typeof value==='string'?text(value,500):[text(value?.collection,50),text(value?.id,240),text(value?.reason,300)].filter(Boolean).join(': ')).filter(Boolean).join(' ')||'Answer ready. Check the linked sources; this reply does not change the research record.';
        refresh();
      }catch(error){if(requestValid())status.textContent=error.name==='AbortError'?'The answer timed out or navigation interrupted it. You can retry.':text(error.message,500)||'Answer unavailable. You can retry.';}
      finally{clearTimeout(timeout);window.removeEventListener('hashchange',leave);if(valid())submit.disabled=!displayedHash||!modelReady;}
    });
  }
  window.WakeAskBob={mount};
})();
