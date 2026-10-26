/* Device-local conversation window over exact published source versions. */
import * as gpu from './ask-bob-gpu.js';
import {prepareContext,readJSON,recordPath,citedSources} from './ask-bob-context.js';
import {answer as searchAnswer} from './ask-bob-guide.js';
const $ = id => document.getElementById(id), params = new URLSearchParams(location.search);
const selection = params.has('article') ? {article:params.get('article'),hash:params.get('hash')} : {collection:params.get('collection') || 'overview',record:params.get('record') || 'home',head:params.get('head'),node:params.get('node') || ''};
const identity = selection.article || [selection.node,selection.collection,selection.record].join('/');
const version = selection.hash || selection.head;
let contextReady = false, mode = 'model', active, history = [], storageKey, allChats = {}, epoch = 0;
const modelPreference = 'wake-bob-device-model';
let cacheCheck = 0;
async function modelSetup() {
  const check = ++cacheCheck, choice = $('model').value;
  $('download').textContent = 'Checking saved Bob…';$('download').disabled = true;
  const saved = await gpu.cached(choice);
  if(check !== cacheCheck) return;
  $('download').textContent = saved ? 'Use saved Bob' : saved === false ? 'Download Bob' : 'Open Bob';
  $('setup-note').textContent = saved ? 'Saved model files found. Open Bob to load them into your graphics processor. Any missing files are fetched again.' : saved === false ? 'Download once, then reuse saved files in this browser. Browser storage can be cleared or evicted; speed and memory needs depend on your device.' : 'Browser storage could not be checked. Bob will reuse available files and download any missing ones.';
  $('download').disabled = Boolean(active);
  status(saved ? 'Bob’s model is saved on this device.' : 'Choose a model to start.');
}
const state = () => { $('send').disabled = !contextReady || Boolean(active); $('download').disabled = Boolean(active); $('model').disabled = Boolean(active); $('search-mode').disabled = Boolean(active); $('change-model').disabled = Boolean(active); $('stop').hidden = !active; $('chat').setAttribute('aria-busy',String(Boolean(active))); };
const status = value => { $('status').textContent = value; };
const nearBottom = () => $('chat').scrollHeight - $('chat').scrollTop - $('chat').clientHeight < 100;
const bottom = () => {$('chat').scrollTop = $('chat').scrollHeight;};
function bubble(who,text = '') {
  $('welcome')?.remove();
  const row = document.createElement('article'); row.className = who === 'You' ? 'you' : 'bob';
  const name = document.createElement('span');name.className = 'speaker';name.textContent = who;
  const prose = document.createElement('div'); prose.className = 'prose';
  row.append(name,prose);$('chat').append(row); render(prose,text);bottom();return row;
}
function render(node,text) {if(window.WakeBobMarkdown)window.WakeBobMarkdown.render(node,text);else node.textContent = text;}
function sources(row,values,label = 'Sources') {
  if (!values.length) return;
  const details = document.createElement('details'), summary = document.createElement('summary');summary.textContent = label;details.append(summary);
  for (const source of values) {
    let url;try {url = new URL(source.url,location.href);} catch {continue;}
    if (url.origin !== location.origin || !['http:','https:'].includes(url.protocol)) continue;
    const p = document.createElement('p'), a = document.createElement('a'); a.textContent = source.id + ' · ' + source.label;a.href = url.href;a.target = '_blank';a.rel = 'noopener';p.append(a);details.append(p);
  }
  row.append(details);
}
function normalizedChats(value) {
  if(!value || typeof value !== 'object' || Array.isArray(value)) return {};
  const rows=[];
  for(const [key,row] of Object.entries(value).slice(-100)) {
    if(key.length>500 || !row || typeof row!=='object' || Array.isArray(row) || typeof row.version!=='string' || !/^(?:snapshot:)?[a-f0-9]{64}$/.test(row.version) || !Number.isSafeInteger(row.time) || row.time<0 || !Array.isArray(row.turns)) continue;
    const turns=row.turns.slice(-10).flatMap(turn=>{
      if(!turn || typeof turn!=='object' || typeof turn.question!=='string' || !turn.question || turn.question.length>2000 || typeof turn.answer!=='string' || !turn.answer || turn.answer.length>10000) return [];
      const references=(Array.isArray(turn.sources)?turn.sources:[]).slice(0,20).flatMap(source=>{
        if(!source || typeof source!=='object' || typeof source.id!=='string' || !/^S\d{1,3}$/.test(source.id) || typeof source.label!=='string' || source.label.length>240 || typeof source.url!=='string' || source.url.length>2000) return [];
        let url;try{url=new URL(source.url,location.href);}catch{return [];}
        if(url.origin!==location.origin || !['http:','https:'].includes(url.protocol))return [];
        return [{id:source.id,label:source.label,url:url.href}];
      });
      return [{question:turn.question,answer:turn.answer,sources:references,mode:turn.mode==='search'?'search':'model',sourceLabel:turn.sourceLabel==='Sources Bob read'?'Sources Bob read':'Sources'}];
    });
    rows.push([key,{version:row.version,turns,time:row.time}]);
  }
  return Object.fromEntries(rows.sort((a,b)=>a[1].time-b[1].time).slice(-20));
}
function save() {
  if (!storageKey) return;
  allChats[identity] = {version,turns:history.slice(-10),time:Date.now()};
  allChats = normalizedChats(allChats);
  const ordered = Object.entries(allChats).sort((a,b) => a[1].time - b[1].time);
  while (ordered.length > 20 || new TextEncoder().encode(JSON.stringify(Object.fromEntries(ordered))).length > 32768) {
    const oldest = ordered[0]; if (!oldest) break;
    if (oldest[1].turns.length > 1) oldest[1].turns.shift(); else ordered.shift();
  }
  allChats = Object.fromEntries(ordered);
  try {localStorage.setItem(storageKey,JSON.stringify(allChats));} catch {$('storage-note').textContent = 'Browser storage is unavailable. This conversation stays in memory until you close it.';}
}
async function restore() {
  try {
    const installation = await readJSON('installation.json',AbortSignal.timeout(8000),524288);
    if (typeof installation.installation_id !== 'string' || !installation.installation_id) return;
    storageKey = 'wake-bob-device-chat:' + installation.installation_id;
    const stored = localStorage.getItem(storageKey);if(stored && new TextEncoder().encode(stored).length <= 32768)allChats = normalizedChats(JSON.parse(stored));
    const saved = allChats[identity];
    if (saved?.version === version && Array.isArray(saved.turns)) history = saved.turns.slice(-10).filter(t => typeof t.question === 'string' && t.question.length <= 2000 && typeof t.answer === 'string' && t.answer.length <= 10000);
    for (const turn of history) {bubble('You',turn.question); const row = bubble('Bob',turn.answer);sources(row,Array.isArray(turn.sources) ? turn.sources : [],turn.sourceLabel);}
  } catch {$('storage-note').textContent = 'Saved chat is unavailable. This conversation works in memory; unreadable history is not reconstructed.';}
}
function fitKeyboard() {
  const view = window.visualViewport;
  if (!view) return;
  const anchored = nearBottom();document.querySelector('main').style.height = Math.round(view.height) + 'px';
  document.querySelector('main').style.transform = 'translateY(' + Math.max(0,view.offsetTop) + 'px)';
  if(anchored)bottom();
}
window.visualViewport?.addEventListener('resize',fitKeyboard);window.visualViewport?.addEventListener('scroll',fitKeyboard);fitKeyboard();
if (['dark','light'].includes(params.get('theme'))) document.documentElement.dataset.theme = params.get('theme');
window.addEventListener('message',event => {if(event.origin === location.origin && event.source === window.opener && event.data?.type === 'wake-theme' && ['dark','light'].includes(event.data.theme))document.documentElement.dataset.theme = event.data.theme;});
$('theme').onclick = () => {const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';document.documentElement.dataset.theme = next;try {localStorage.setItem('wake-site-theme',next);}catch{}};
$('question').oninput = () => {$('question').style.height = 'auto';$('question').style.height = Math.min(128,$('question').scrollHeight) + 'px';};
$('question').onkeydown = event => {if(event.key === 'Enter' && !event.shiftKey && !event.isComposing && matchMedia('(pointer:fine)').matches){event.preventDefault();$('form').requestSubmit();}};
$('stop').onclick = () => active?.abort();
$('clear').onclick = () => {epoch++;active?.abort();history = [];if(storageKey){delete allChats[identity];try{localStorage.setItem(storageKey,JSON.stringify(allChats));}catch{}}$('chat').replaceChildren();status('Chat cleared.');};
$('change-model').onclick = () => {gpu.stop();mode = 'model';$('setup').hidden = false;$('model-setup').hidden = false;$('presence').textContent = 'On your device · WAKE✳︎';void modelSetup();};
$('model').onchange = () => {try{localStorage.setItem(modelPreference,$('model').value);}catch{}void modelSetup();};
$('search-mode').onclick = () => {
  if(!selection.article){status('Source search is available from a blog article. Open Bob’s Blog to choose one.');return;}
  mode = 'search';$('setup').hidden = true;$('presence').textContent = 'Source search · no model';status('Source search quotes published passages.');$('question').focus();
};
async function download() {
  cacheCheck++;
  try{localStorage.setItem(modelPreference,$('model').value);}catch{}
  // Ask for persistence from the user's click. Denial must not block use.
  try{navigator.storage?.persist?.().catch(() => {});}catch{}
  const controller = new AbortController(); active = controller;state();$('progress').hidden = false;$('progress').removeAttribute('value');
  try {
    await gpu.load($('model').value,(message,report) => {status(message);if(Number.isFinite(report.progress))$('progress').value = report.progress;},controller.signal);
    mode = 'model';$('setup').hidden = true;$('presence').textContent = 'On device · ready';status('Bob is ready. Ask away.');$('question').focus();
  } catch(error) {status(error.name === 'AbortError' ? 'Stopped. Downloaded files are kept for retry.' : error.message);}
  finally {if(active === controller)active = undefined;$('progress').hidden = true;state();}
}
$('download').onclick = download;
$('form').onsubmit = async event => {
  event.preventDefault();if(active || !contextReady) return;
  const question = $('question').value.trim();if(!question)return;
  if(mode === 'model' && !gpu.ready()){$('setup').hidden = false;await modelSetup();status('Open Bob using the setup button, or use source search.');return;}
  const controller = new AbortController(), revision = epoch;active = controller;state();
  bubble('You',question);const row = bubble('Bob','…');$('question').value = '';$('question').style.height = '44px';status(mode === 'search' ? 'Finding published passages…' : 'Reading the sources…');
  try {
    let answer,refs,metrics,complete = true,sourceLabel = 'Sources';
    if(mode === 'search') {
      const result = await searchAnswer({article_id:selection.article,expected_article_hash:selection.hash,question,history},controller.signal);
      answer = result.answer;refs = result.citations;
    } else {
      const prepared = await prepareContext(selection,question,history,controller.signal);
      const result = await gpu.generate(prepared.messages,{signal:controller.signal,onText:value => {if(revision !== epoch || controller.signal.aborted)return;const pinned = nearBottom();render(row.querySelector('.prose'),value);if(pinned)bottom();status('Bob is writing…');}});
      answer = result.answer;refs = citedSources(answer,prepared.sources);if(!refs.length){refs=prepared.sources;sourceLabel='Sources Bob read';}metrics = result.metrics;complete = result.complete;
    }
    if (revision !== epoch || controller.signal.aborted) return;
    render(row.querySelector('.prose'),answer);sources(row,refs,sourceLabel);
    if(complete) {history.push({question,answer,sources:refs,mode,sourceLabel});save();status(metrics ? 'On device · ' + (metrics.latency_ms/1000).toFixed(1) + 's' : 'Published source passages');}
    else {row.classList.add('incomplete');status('Reply reached its length limit. Ask Bob to focus on one part.');}
    bottom();
  } catch(error) {
    if(revision === epoch){row.classList.add('incomplete');if(row.querySelector('.prose').textContent === '…')row.remove();status(error.name === 'AbortError' ? 'Stopped. Your earlier replies are kept.' : error.message);if(!$('question').value)$('question').value = question;}
  } finally {if(active === controller)active = undefined;state();}
};
try {
  const prepared = await prepareContext(selection,'What is this about?',[],AbortSignal.timeout(15000));
  $('context-title').textContent = prepared.title;
  const link = prepared.sources[0]?.url;if(link)$('source-page').href = link;
  await restore();contextReady = true;state();status('Choose a model to start.');
  if(!await gpu.supported()){$('model-setup').hidden = true;status('GPU Bob is unavailable in this browser. Source search is still available for articles.');}
  else {
    let preferred;try{preferred=localStorage.getItem(modelPreference);}catch{}
    if(Object.hasOwn(gpu.MODELS,preferred))$('model').value=preferred;
    else if(!await gpu.cached('best') && await gpu.cached('capable'))$('model').value='capable';
    await modelSetup();
  }
} catch(error) {status(error.message);$('setup').hidden = true;}
