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
    mode:['published-passages','live-gemini'].includes(value?.mode)?value.mode:'generated',
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
  let popup, popupArticle;
  let capability;
  const capabilities=()=>capability||(capability=window.WAKE_DEPLOYMENT?.snapshot_only===true?
    Promise.resolve({enabled:true,browser:true,token:'device-local',installation_id:'public-reader'}):fetch('/ask-bob/capabilities',{
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
  function markdown(node,value){if(window.WakeBobMarkdown)window.WakeBobMarkdown.render(node,value);else node.textContent=value;}
  function safeURL(value){
    if(typeof value!=='string')return null;
    try{const url=new URL(value,location.href);return ['http:','https:'].includes(url.protocol)?url.href:null;}catch{return null;}
  }
  function browserLauncher(container,selection,title){
    const node=location.pathname.match(/\/nodes\/((?:10[0-3]|20[0-3]|30[0-3])\.wake)\//)?.[1];
    const url=new URL((node?'../../':'')+'bob-chat.html',document.baseURI);
    for(const [key,value] of Object.entries({...selection,...(node?{node}:{})}))if(value)url.searchParams.set(key,value);
    url.searchParams.set('theme',document.documentElement.dataset.theme||'light');
    const link=element('a','Ask Bob','ask-bob-launch'+(selection.collection?' ask-bob-record':''));
    link.href=url.href;link.target='_blank';link.rel='noopener';link.setAttribute('aria-label',title||'Ask Bob · open chat window');
    const identity=url.searchParams.toString();
    link.addEventListener('click',event=>{
      const themed=new URL(link.href);themed.searchParams.set('theme',document.documentElement.dataset.theme||'light');link.href=themed.href;
      if(popup&&!popup.closed&&popupArticle===identity){event.preventDefault();popup.postMessage({type:'wake-theme',theme:document.documentElement.dataset.theme||'light'},location.origin);popup.focus();return;}
      const opened=window.open(link.href,'wake-bob-chat','popup,width=480,height=760,resizable=yes,scrollbars=yes');
      if(opened){event.preventDefault();popup=opened;popupArticle=identity;opened.focus();}
    });
    const heading=container.querySelector(':scope > h1,:scope > h2')||container.querySelector(':scope > .record-panel-head,:scope > .record-panel-meta');
    if(heading)heading.after(link);else container.prepend(link);
  }
  async function mount(container,{post,head=''}){
    // The unified blog owns cross-node source IDs; individual node pages do not.
    if(!container||!post?.id||/\/nodes(?:\/|$)/.test(location.pathname))return;
    const route=location.href,valid=()=>container.isConnected&&location.href===route;
    const cap=await capabilities();
    if(!valid()||!cap?.enabled||typeof cap.token!=='string'||!cap.token||typeof cap.installation_id!=='string'||!cap.installation_id)return;
    if(container.querySelector('.ask-bob')||container.querySelector(':scope > .ask-bob-launch'))return;
    if(cap.browser&&window.WAKE_DEPLOYMENT?.snapshot_only===true){
      const displayedHash=hash(post._reader_article?.hash);
      if(displayedHash)browserLauncher(container,{article:post.id,hash:displayedHash});
      return;
    }
    if(cap.live){
      const launcher=element('a',undefined,'ask-bob-launch');
      launcher.href=cap.url+'/?article='+encodeURIComponent(post.id)+'&hash='+hash(post._reader_article?.hash)+'&theme='+encodeURIComponent(document.documentElement.dataset.theme||'light');launcher.target='_blank';launcher.rel='noopener';
      const icon=element('span');icon.innerHTML='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M20 15a3 3 0 0 1-3 3H9l-5 4V6a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3Z"/><path d="M8 10h8M8 14h5"/></svg>';icon.setAttribute('aria-hidden','true');launcher.append(icon,document.createTextNode('Ask Bob'));
      launcher.setAttribute('aria-label','Ask Bob · open chat window');
      launcher.addEventListener('click',event=>{
        const themed=new URL(launcher.href);themed.searchParams.set('theme',document.documentElement.dataset.theme||'light');launcher.href=themed.href;
        if(popup&&!popup.closed&&popupArticle===post.id){event.preventDefault();popup.postMessage({type:'wake-theme',theme:document.documentElement.dataset.theme||'light'},new URL(cap.url).origin);popup.focus();return;}
        const opened=window.open(launcher.href,'wake-bob-chat','popup,width=480,height=760,resizable=yes,scrollbars=yes');
        if(opened){event.preventDefault();popup=opened;popupArticle=post.id;opened.focus();}
      });
      const title=container.querySelector('h1');if(title)title.after(launcher);else container.prepend(launcher);
      return; // The live conversation opens above; no duplicate footer composer.
    }
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
    panel.append(element('p',cap.live?'Talk with Bob live about this article, WAKE, or your own questions. No sign-in required.':cap.browser?
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
    question.placeholder=cap.live?'Talk to Bob…':'Ask about this article…';question.setAttribute('aria-label','Message Bob');
    const submit=element('button','Send');submit.type='submit';submit.disabled=!displayedHash;
    const cancel=element('button','Stop');cancel.type='button';cancel.hidden=true;cancel.addEventListener('click',()=>active?.abort());
    form.append(question,submit,cancel);panel.append(form);
    const retry=element('button','Retry');retry.type='button';retry.hidden=true;panel.append(retry);
    retry.addEventListener('click',()=>form.requestSubmit());
    const useModel=element('input');useModel.type='checkbox';
    const modelLabel=element('label');modelLabel.append(useModel,document.createTextNode(' Experimental AI answer on this device (491 MB download; slower and may be inaccurate)'));
    const privacy=element('details',undefined,'ask-bob-privacy');privacy.append(element('summary','About this chat'));
    privacy.append(element('p',cap.live?'Your message and recent conversation go to WAKE’s answer service and Google Gemini. Chat history is saved in this browser; our service stores only temporary request counters, not conversations. Do not send sensitive information. Bob can make mistakes and cannot change research records. Anonymous use has shared request limits.':cap.browser?
      'The site prepares a small searchable guide when it publishes each article. Your browser finds and quotes relevant passages; it does not generate new facts. Questions and saved replies stay here and never enter the research record. The optional AI answer downloads a model from Hugging Face and runs on this device.':
      'History stays in this browser. Questions and recent context go to the local answer service and its configured model, and are excluded from public exports. Bob can make mistakes; check the sources.'));
    if(cap.browser)privacy.append(modelLabel);
    const storageNote=element('p');privacy.append(storageNote);
    const clear=element('button','Clear chat');clear.type='button';privacy.append(clear);panel.append(privacy);
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
        const reply=element('div',undefined,'ask-bob-message ask-bob-reply');reply.append(element('strong',value.mode==='published-passages'?'Bob · source passages':value.mode==='live-gemini'?'Bob · live (AI)':'Bob · AI answer (unverified)'),element('div','','ask-bob-answer'));markdown(reply.querySelector('.ask-bob-answer'),value.answer);item.append(reply);
        const links=element('ul',undefined,'ask-bob-sources');for(const source of value.citations||[]){const href=safeURL(source.url);if(!href)continue;const row=element('li'),link=element('a',source.id+' · '+source.label);link.href=href;link.rel='noopener noreferrer';row.append(link);links.append(row);}if(links.children.length)reply.append(links);
      }
      conversation.append(item);bottom();return item;
    }
    current.turns.forEach(display);refresh();
    if(cap.unavailable)status.textContent='Bob is temporarily unavailable. You can try sending again shortly.';
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
      if(cap.live)body.history=current.turns.slice(-6).map(value=>({question:text(value.question,1000),answer:text(value.answer,2000)}));
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
          stage===1?(cap.live?'Connecting to Bob…':'Preparing Bob on your device…'):detail.characters?'Bob is writing… '+detail.characters+' characters generated':modelMode||cap.live?'Bob is reading and thinking…':'Finding relevant published passages…';
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
          if(cap.live){
            phase='answer';setDeadline(60000);
            const response=await fetch(cap.url+'/v1/chat',{method:'POST',credentials:'omit',cache:'no-store',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),signal:controller.signal});
            if(!response.ok){const value=await response.json();throw Error(({daily_limit:'Bob has reached today’s shared question allowance. Please try tomorrow.',rate_limited:'Please wait a minute before sending another message.',busy:'Bob is helping other readers. Try again shortly.',provider_quota:'Gemini’s shared quota is currently exhausted. Please try later.',article_changed:'This article changed. Reload it before sending again.',article_unavailable:'This article is no longer available. Reload the latest blog.'})[value.error]||'Bob is temporarily unavailable. Please try again later.');}
            const reply=element('div',undefined,'ask-bob-message ask-bob-reply'),prose=element('div','','ask-bob-answer');reply.append(element('strong','Bob · live'),prose);pending.append(reply);
            const reader=response.body.getReader(),decoder=new TextDecoder();let buffer='',partial='',done=false;
            try{for(;;){const chunk=await reader.read();buffer+=decoder.decode(chunk.value||new Uint8Array(),{stream:!chunk.done});if(buffer.length>65536)throw Error('Bob sent an oversized reply.');const lines=buffer.split('\n');buffer=lines.pop();for(const line of lines){if(!line.trim())continue;const event=JSON.parse(line);if(event.type==='delta'){partial+=text(event.text,6000);markdown(prose,partial);showProgress('',{stage:'answer',characters:partial.length});bottom();}else if(event.type==='done'){result=event.result;done=true;}else if(event.type==='error')throw Error('Bob could not finish the reply. Please try again.');}if(chunk.done)break;}if(!done)throw Error('The connection ended before Bob finished.');}finally{await reader.cancel();}
          }else if(cap.browser){
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
  async function mountRecord(container,{collection,record_id,head=''}){
    if(!container||!record_id||!head||container.querySelector(':scope > .ask-bob-record'))return;
    const route=location.href,cap=await capabilities();
    if(!container.isConnected||location.href!==route||(!cap?.live&&!cap?.browser)||!cap.enabled)return;
    if(container.querySelector(':scope > .ask-bob-record'))return;
    if(cap.browser&&window.WAKE_DEPLOYMENT?.snapshot_only===true){browserLauncher(container,{collection,record:record_id,head},'Ask Bob about this '+(collection==='overview'?'page':collection==='notebooks'?'notebook':collection==='journal'?'journal entry':'record'));return;}
    const link=element('a','Ask Bob','ask-bob-launch ask-bob-record'),url=new URL('/',cap.url);
    const node=location.pathname.match(/\/nodes\/((?:10[0-3]|20[0-3]|30[0-3])\.wake)\//)?.[1];
    for(const [key,value] of Object.entries({collection,record:record_id,head,...(node?{node}:{})}))url.searchParams.set(key,value);
    url.searchParams.set('theme',document.documentElement.dataset.theme||'light');link.href=url.href;link.target='_blank';link.rel='noopener';link.setAttribute('aria-label','Ask Bob about this '+(collection==='overview'?'page':collection==='notebooks'?'notebook':collection==='journal'?'journal entry':'record'));
    const identity=[node||'',collection,record_id,head].join('|');
    link.addEventListener('click',event=>{
      const themed=new URL(link.href);themed.searchParams.set('theme',document.documentElement.dataset.theme||'light');link.href=themed.href;
      if(popup&&!popup.closed&&popupArticle===identity){event.preventDefault();popup.postMessage({type:'wake-theme',theme:document.documentElement.dataset.theme||'light'},new URL(cap.url).origin);popup.focus();return;}
      const opened=window.open(link.href,'wake-bob-chat','popup,width=480,height=760,resizable=yes,scrollbars=yes');if(opened){event.preventDefault();popup=opened;popupArticle=identity;opened.focus();}
    });
    const heading=container.querySelector(':scope > h1,:scope > h2')||container.querySelector(':scope > .record-panel-head,:scope > .record-panel-meta');if(heading)heading.after(link);else container.prepend(link);
  }
  function attachRecords(view,{page,head,selected=''}){
    if(!view)return;
    view.querySelectorAll('.ask-bob-record').forEach(node=>node.remove());
    for(const card of view.querySelectorAll('[data-bob-collection][data-bob-id]'))mountRecord(card,{collection:card.dataset.bobCollection,record_id:card.dataset.bobId,head});
    if(!(selected&&['projects','journal','evidence'].includes(page)&&!selected.startsWith('topic:'))&&['home','discoveries','topics','projects','journal','evidence','history','lab','metrics','about'].includes(page))mountRecord(view,{collection:'overview',record_id:page,head});
  }

  window.WakeAskBob={mount,mountRecord,attachRecords};
})();
