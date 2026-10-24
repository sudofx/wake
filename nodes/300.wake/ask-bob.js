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
    mode:value?.mode==='published-passages'?'published-passages':'generated',
    citations:(Array.isArray(value?.citations)?value.citations:[]).slice(0,4).map(source=>({id:text(source.id,20),label:text(source.label||source.title,240),url:text(source.url||source.path,2000)})),
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
  let guideRuntime;
  const guide=async()=>guideRuntime||(guideRuntime=await import(new URL('ask-bob-guide.js?build=passages-2',document.baseURI).href));
  let browserRuntime;
  // Replace the broken startup module without invalidating the large model cache.
  const browser=async()=>browserRuntime||(browserRuntime=await import(new URL('ask-bob-browser.js?build=focused-3',document.baseURI).href));
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
    let epoch=0,active,failedTurn;
    const panel=element('section',undefined,'ask-bob');
    panel.setAttribute('aria-label','Ask Bob');
    panel.append(element('h2','Ask Bob'));
    panel.append(element('p',cap.browser?
      'Find answers in this article and its linked sources. Published passages appear without a model download.':
      'Talk about this article. Bob uses the article and your recent conversation.','ask-bob-note'));
    const conversation=element('div',undefined,'ask-bob-conversation');
    conversation.setAttribute('role','log');conversation.setAttribute('aria-label','Conversation with Bob');
    conversation.setAttribute('aria-live','polite');conversation.tabIndex=0;panel.append(conversation);
    const activity=element('div',undefined,'ask-bob-activity');activity.hidden=true;
    const stages=element('ol',undefined,'ask-bob-stages');stages.setAttribute('aria-label','Bob progress');
    const steps=['Download','Prepare','Reply'].map(title=>{const step=element('li',title);stages.append(step);return step;});
    const progressBar=element('progress');progressBar.max=1;progressBar.setAttribute('aria-label','Bob download progress');
    const spinner=element('span',undefined,'ask-bob-spinner');spinner.setAttribute('aria-hidden','true');
    const progressText=element('span'),elapsed=element('span',undefined,'ask-bob-elapsed');elapsed.setAttribute('aria-hidden','true');
    const progressLine=element('div',undefined,'ask-bob-progress-line');progressLine.setAttribute('role','status');progressLine.append(spinner,progressText,elapsed);
    activity.append(stages,progressBar,progressLine);panel.append(activity);
    const status=element('p','','ask-bob-status');status.setAttribute('role','status');panel.append(status);
    const form=element('form',undefined,'ask-bob-composer'),question=element('textarea');
    question.required=true;question.maxLength=2000;question.rows=2;
    question.placeholder='Ask about this article…';question.setAttribute('aria-label','Message Bob');
    const submit=element('button','Send');submit.type='submit';submit.disabled=!displayedHash;
    const cancel=element('button','Stop');cancel.type='button';cancel.hidden=true;cancel.addEventListener('click',()=>active?.abort());
    form.append(question,submit,cancel);panel.append(form);
    const retry=element('button','Retry');retry.type='button';retry.hidden=true;panel.append(retry);
    retry.addEventListener('click',()=>form.requestSubmit());
    const useModel=element('input');useModel.type='checkbox';
    const modelLabel=element('label');modelLabel.append(useModel,document.createTextNode(' Experimental AI answer on this device (491 MB download; slower and may be inaccurate)'));
    const privacy=element('details',undefined,'ask-bob-privacy');privacy.append(element('summary','About this chat'));
    privacy.append(element('p',cap.browser?
      'The site prepares a small searchable guide when it publishes each article. Your browser finds and quotes relevant passages; it does not generate new facts. Questions and saved replies stay here and never enter the research record. The optional AI answer downloads a model from Hugging Face and runs on this device.':
      'History stays in this browser. Questions and recent context go to the local answer service and its configured model, and are excluded from public exports. Bob can make mistakes; check the sources.'));
    if(cap.browser)privacy.append(modelLabel);
    const storageNote=element('p');privacy.append(storageNote);
    const clear=element('button','Clear chat');clear.type='button';privacy.append(clear);panel.append(privacy);
    if(cap.browser){const prompts=element('div',undefined,'ask-bob-prompts');for(const label of ['What is the main point?','What evidence is cited?','What are the limitations?']){const button=element('button',label);button.type='button';button.addEventListener('click',()=>{if(!active){question.value=label;form.requestSubmit();}});prompts.append(button);}form.before(prompts);}
    container.append(panel);
    function persist(){store.save();current=store.value.articles.find(row=>row.id===post.id)||current;}
    function refresh(){
      storageNote.textContent=!store.available?'Browser storage is unavailable. This chat works in memory and may be lost when you leave.':
        store.damaged?'Saved chat could not be read. Starting a new chat; missing messages have not been reconstructed.':
        'Chat is saved only in this browser. Clearing chat keeps any optional model download.';
    }
    function bottom(){conversation.scrollTop=conversation.scrollHeight;}
    function display(value){
      const item=element('div',undefined,'ask-bob-turn');
      const user=element('div',undefined,'ask-bob-message ask-bob-user');user.append(element('strong','You'),element('p',value.question));item.append(user);
      if(value.answer){
        const reply=element('div',undefined,'ask-bob-message ask-bob-reply');reply.append(element('strong',value.mode==='published-passages'?'Bob · source passages':'Bob · AI answer (unverified)'),element('p',value.answer,'ask-bob-answer'));item.append(reply);
        const links=element('ul',undefined,'ask-bob-sources');for(const source of value.citations||[]){const href=safeURL(source.url);if(!href)continue;const row=element('li'),link=element('a',source.id+' · '+source.label);link.href=href;link.rel='noopener noreferrer';row.append(link);links.append(row);}if(links.children.length)reply.append(links);
      }
      conversation.append(item);bottom();return item;
    }
    current.turns.forEach(display);refresh();
    if(!displayedHash)status.textContent='This article has no verified display version. Reload a newly exported snapshot before asking a question.';
    clear.addEventListener('click',()=>{
      epoch++;active?.abort();previous=null;priorHash='';store.clear();current={id:text(post.id,240),hash:displayedHash,head:text(descriptor?.head||head,100),opened:true,encountered_at:new Date().toISOString(),self_report:null,turns:[],versions:[]};
      conversation.replaceChildren();failedTurn=null;retry.hidden=true;status.textContent='Chat cleared.';refresh();
    });
    form.addEventListener('submit',async event=>{
      event.preventDefault();if(submit.disabled||active)return;
      if(!valid()){status.textContent='This article changed while the chat was open. Reload the article and send again. Your message is kept.';return;}
      const asked=question.value.trim();if(!asked)return;
      const requestEpoch=epoch,requestValid=()=>valid()&&requestEpoch===epoch;
      // Conversation policy is automatic. Prior answers stay untrusted and
      // bounded; no opening/typing event asserts reader comprehension.
      const modelMode=cap.browser&&useModel.checked;
      steps.forEach((step,index)=>{step.textContent=(modelMode?['Download','Prepare','Reply']:['Sources','Find','Reply'])[index];});
      const body={article_id:post.id,question:asked,condition:'C',expected_article_hash:displayedHash,
        history:current.turns.slice(-MAX_TURNS).map(({mode,citations,...value})=>value),
        previous_article:priorHash?previous:{id:current.id,hash:current.hash||undefined,head:current.head,exposure:{opened:true},self_report:current.self_report}};
      if(priorHash)body.prior_article_hash=priorHash;
      failedTurn?.remove();failedTurn=null;const pending=display({question:asked});question.value='';
      retry.hidden=true;submit.disabled=true;cancel.hidden=false;activity.hidden=false;status.textContent='';
      conversation.setAttribute('aria-busy','true');
      const controller=new AbortController();active=controller;
      let phase='prepare',started=Date.now(),deadlineAt=started+(modelMode?600000:120000),deadline,ticker;
      let rejectStopped;
      const stopped=new Promise((_,reject)=>{rejectStopped=reject;});
      const showProgress=(message,detail={})=>{
        if(!requestValid()||controller.signal.aborted)return;
        const stage=detail.stage==='download'?0:detail.stage==='answer'||detail.stage==='ready'?2:1;
        steps.forEach((step,index)=>{step.className=index<stage?'complete':index===stage?'current':'';if(index===stage)step.setAttribute('aria-current','step');else step.removeAttribute('aria-current');});
        progressBar.hidden=stage!==0;
        if(stage===0&&typeof detail.fraction==='number'){progressBar.value=detail.fraction;progressBar.setAttribute('aria-valuetext',Math.floor(detail.fraction*100)+'% downloaded');}
        else{progressBar.removeAttribute('value');progressBar.removeAttribute('aria-valuetext');}
        progressText.textContent=stage===0?(typeof detail.fraction==='number'?'Downloading Bob: '+Math.floor(detail.fraction*100)+'%':'Checking Bob’s saved download…'):
          stage===1?'Preparing Bob on your device…':detail.characters?'Bob is writing… '+detail.characters+' characters generated':modelMode?'Bob is reading and thinking…':'Finding relevant published passages…';
      };
      const checkDeadline=()=>{if(Date.now()>=deadlineAt)controller.abort(new DOMException(phase==='prepare'?'Bob took too long to prepare.':'Bob took too long to answer.','TimeoutError'));};
      const setDeadline=ms=>{clearTimeout(deadline);deadlineAt=Date.now()+ms;deadline=setTimeout(checkDeadline,ms);};
      const stop=()=>{if(phase==='prepare')browserRuntime?.cancelLoad?.();rejectStopped(controller.signal.reason||new DOMException('Stopped','AbortError'));};
      controller.signal.addEventListener('abort',stop,{once:true});
      const leave=()=>controller.abort();window.addEventListener('hashchange',leave,{once:true});
      document.addEventListener('visibilitychange',checkDeadline);window.addEventListener('pageshow',checkDeadline);
      ticker=setInterval(()=>{checkDeadline();if(requestValid())elapsed.textContent=Math.floor((Date.now()-started)/1000)+'s elapsed';},1000);
      elapsed.textContent='0s elapsed';showProgress('',{stage:modelMode?'download':'answer'});setDeadline(modelMode?600000:120000);
      try{
        const work=(async()=>{
          let result,responseOK=true;
          if(cap.browser){
            if(!modelMode){phase='answer';setDeadline(15000);const runtime=await guide();return {result:await runtime.answer(body,controller.signal,showProgress),responseOK:true};}
            const runtime=await browser();
            if(controller.signal.aborted)throw controller.signal.reason;
            await runtime.load(showProgress,controller.signal);
            if(controller.signal.aborted)throw controller.signal.reason;
            phase='answer';setDeadline(300000);showProgress('',{stage:'answer'});
            result=await runtime.answer(body,controller.signal,showProgress);
          }else{
            phase='answer';
            const response=await fetch('/ask-bob',{method:'POST',credentials:'same-origin',cache:'no-store',
              headers:{'Content-Type':'application/json','X-Wake-Reader-Token':cap.token},body:JSON.stringify(body),signal:controller.signal});
            responseOK=response.ok;result=await response.json();
          }
          checkDeadline();if(controller.signal.aborted)throw controller.signal.reason;
          return {result,responseOK};
        })();
        const {result,responseOK}=await Promise.race([work,stopped]);
        if(!requestValid())return;
        if(!responseOK||result.ok===false){
          const unavailable={busy:'Bob is busy. Try again shortly.',busy_or_unavailable:'Bob is busy or unavailable. Try again shortly.',paused:'Reader questions are paused.',session_limit:'This local preview has reached its question limit.',provider_deferred_or_failed:'Bob could not complete this answer. Try again later.',invalid_or_unavailable_article:'This article is unavailable or has changed. Reload it before asking again.'};
          throw Error(unavailable[result.error]||'Bob could not complete this question. Try again later.');
        }
        if(typeof result.answer!=='string'||result.article?.id!==post.id||result.article?.hash!==displayedHash)throw Error('The answer did not identify this article version.');
        current.hash=result.article.hash;current.head=text(result.article.head,100);
        const value=turn({id:crypto.randomUUID(),article_id:post.id,article_hash:current.hash,head:current.head,question:asked,answer:result.answer,mode:result.metrics?.mode,citations:result.citations,self_report:current.self_report,time:new Date().toISOString()});
        if(!store.value.articles.includes(current))store.value.articles.push(current);
        current.turns.push(value);persist();pending.remove();const completed=display(value);priorHash='';previous=null;
        const notices=[...(Array.isArray(result.missing)?result.missing:[]),...(Array.isArray(result.warnings)?result.warnings:[])];
        const note=notices.map(value=>typeof value==='string'?text(value,500):[text(value?.collection,50),text(value?.id,240),text(value?.reason,300)].filter(Boolean).join(': ')).filter(Boolean).join(' ');
        if(note){const notes=element('details');notes.append(element('summary','Source notes'),element('p',note));completed.querySelector('.ask-bob-reply').append(notes);}
        status.textContent='';bottom();refresh();
      }catch(error){if(requestValid()){
        failedTurn=pending;pending.classList.add('ask-bob-failed');
        const reason=controller.signal.reason?.name==='TimeoutError'?controller.signal.reason.message:error.name==='AbortError'?'Stopped.':text(error.message,500)||'Bob could not answer.';
        status.textContent=reason+' You can send again to retry. Your earlier replies are kept.';
        if(!question.value)question.value=asked;retry.hidden=false;
      }}finally{
        clearTimeout(deadline);clearInterval(ticker);controller.signal.removeEventListener('abort',stop);
        window.removeEventListener('hashchange',leave);document.removeEventListener('visibilitychange',checkDeadline);window.removeEventListener('pageshow',checkDeadline);
        if(active===controller){active=null;if(valid()){activity.hidden=true;cancel.hidden=true;submit.disabled=!displayedHash;conversation.setAttribute('aria-busy','false');}}
      }
    });
  }
  window.WakeAskBob={mount};
})();
