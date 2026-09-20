/*
 * WAKE✳︎ MAINTAINER NOTE
 *
 * Interactive provenance map. Visual relationships must correspond to graph data emitted by provenance.py rather than browser-side inference.
 *
 * Comments should preserve the boundary between presentation and the canonical durable record.
 */

(()=>{'use strict';
const data=JSON.parse(document.getElementById('map-data').textContent), nodes=new Map(data.nodes.map(n=>[n.id,n])), topicColors=data.meta?.topic_colors||{};
const timeline=document.getElementById('timeline'), constellation=document.getElementById('constellation'), details=document.getElementById('details'), clearButton=document.getElementById('clear');
const emptyConstellation=constellation.innerHTML, emptyDetails=details.innerHTML;
const adjacency=new Map(); for(const edge of data.edges){for(const id of [edge.source,edge.target]){if(!adjacency.has(id))adjacency.set(id,[]);adjacency.get(id).push(edge)}}
let context=null, selected=null, lastFocus=null;
const labels={journal:'Journal',blog:'Blog',belief:'Belief',notebook:'Notebook',evidence:'Source / receipt',project:'Project',commitment:'Commitment',research:'Research request',invocation:'Invocation',editorial:'Editorial decision'};
function el(tag,cls,text){const e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)mark(e,String(text));return e}
function mark(e,text){text=text.replace(/^\[([^\[\]\n]+)\]$/,'$1');const parts=text.split(/(WAKE✳︎?)/g);for(const part of parts){if(/^WAKE✳︎?$/.test(part)){const b=document.createElement('strong');b.className='wake-mark';b.textContent='WAKE✳︎';e.append(b)}else e.append(document.createTextNode(part))}}
function related(id){return new Set([id,...(adjacency.get(id)||[]).map(e=>e.source===id?e.target:e.source)])}
function topicFor(n){const domainOf=id=>{const a=nodes.get(id);if(a?.detail?.domain)return a.detail.domain;for(const edge of adjacency.get(id)||[]){const other=nodes.get(edge.source===id?edge.target:edge.source);if(other?.detail?.domain)return other.detail.domain}return ''};if(n.kind==='journal'){for(const edge of adjacency.get(n.id)||[]){const otherId=edge.source===n.id?edge.target:edge.source;const domain=domainOf(otherId);if(domain)return domain}for(const change of n.detail.changes||[]){const match=String(change).match(/(?:project|notebook):\s*([^\s]+)/i);if(!match)continue;const prefix=/project/i.test(change)?'project:':'notebook:';const artifact=[...nodes.values()].find(x=>x.id.startsWith(prefix+match[1]));if(artifact?.detail?.domain)return artifact.detail.domain}return ''}if(n.kind==='blog'){if(n.detail.domain)return n.detail.domain;const project=n.detail.project;if(project){const artifact=[...nodes.values()].find(x=>x.id.startsWith('project:'+project));if(artifact?.detail?.domain)return artifact.detail.domain}for(const edge of adjacency.get(n.id)||[]){const other=nodes.get(edge.source===n.id?edge.target:edge.source);if(other?.kind==='journal'){const domain=topicFor(other);if(domain)return domain}}return ''}return ''}
function timeFor(n){if(n.detail?.time)return n.detail.time;for(const field of ['updated_by','created_by']){const iid=n.detail?.[field];const invocation=iid&&nodes.get('invocation:'+iid);if(invocation?.detail?.time)return invocation.detail.time}return ''}
function timeLabel(value){if(!value||Number.isNaN(Date.parse(value)))return '';return new Intl.DateTimeFormat('en-US',{month:'short',day:'numeric',hour:'numeric',minute:'2-digit',timeZone:'America/Los_Angeles'}).format(new Date(value))}
function button(id,showTopic=false){const n=nodes.get(id), b=el('button','node '+n.kind);b.type='button';b.dataset.node=id;b.setAttribute('aria-label',labels[n.kind]+': '+n.title);const kind=el('span','kind',labels[n.kind]);if(showTopic){const topic=topicFor(n);if(topic){const tag=el('small','topic-tag',topic.replaceAll('_',' ').toLowerCase());tag.dataset.topic=topic;tag.style.setProperty('--topic-color',topicColors[topic]||'var(--cyan)');kind.append(tag)}}const stamp=timeLabel(timeFor(n));if(stamp&&(showTopic||n.kind==='project'))kind.append(el('small','node-time',stamp));b.append(kind);b.append(el('span','node-title',n.title));if(n.kind==='blog'&&n.detail.status)b.append(el('small','',n.detail.status));b.addEventListener('click',()=>select(id));b.addEventListener('pointerenter',()=>emphasis(id));b.addEventListener('pointerleave',()=>emphasis());return b}
function emphasis(hover){
// An artifact click locks its neighborhood. Pointer movement while scrolling
// must not replace that selection with a different hover preview.
const pinned=selected&&!['journal','blog'].includes(nodes.get(selected)?.kind)?selected:null;
const active=pinned||hover;
const ids=active?related(active):new Set([selected,context,...(nodes.get(context)?.expands||[]),...(context?[...related(context)]:[])]);
for(const b of document.querySelectorAll('[data-node]')){
  b.classList.toggle('selected',b.dataset.node===selected);
  b.classList.toggle('related',ids.has(b.dataset.node));
  b.classList.toggle('dim',Boolean(active||selected)&&!ids.has(b.dataset.node));
  b.setAttribute('aria-pressed',String(b.dataset.node===selected));
}
for(const path of constellation.querySelectorAll('svg path')){
  const connected=path.dataset.source===active||path.dataset.target===active;
  path.classList.toggle('edge-hot',Boolean(active)&&connected);
  path.classList.toggle('edge-dim',Boolean(active)&&!connected);
}
}
const origin=new Map();for(const edge of data.edges)if(edge.relation==='originating wake'){if(!origin.has(edge.source))origin.set(edge.source,[]);origin.get(edge.source).push(edge.target)}
for(const jid of data.journals){const row=el('div','timeline-row');row.append(button(jid,true));for(const bid of data.blogs.filter(b=>(origin.get(b)||[]).includes(jid))){const branch=el('div','blog-link');branch.append(button(bid,true));row.append(branch)}timeline.append(row)}
const unlinked=data.blogs.filter(b=>!origin.has(b));if(unlinked.length){timeline.append(el('p','eyebrow','Blog posts / no recorded wake link'));for(const id of unlinked)timeline.append(button(id,true))}
if(!data.journals.length&&!data.blogs.length)timeline.append(el('p','empty','No accepted wakes or blog posts in this export yet.'));
document.getElementById('counts').textContent=`${data.journals.length} wakes · ${data.blogs.length} ${data.blogs.length===1?'post':'posts'} · version ${data.meta.version}`;
function bloom(){constellation.replaceChildren();if(!context){constellation.innerHTML=emptyConstellation;return}const j=nodes.get(context);constellation.append(el('div','bloom-context','○ Cycle '+j.detail.cycle));const visible=j.expands||[];
for(const kind of ['belief','notebook','evidence','project','commitment','research','invocation','editorial']){const ids=visible.filter(id=>nodes.get(id)?.kind===kind);if(!ids.length)continue;const group=el('section','artifact-group');group.append(el('h3','',labels[kind]+' · '+ids.length));for(const id of ids)group.append(button(id));constellation.append(group)}requestAnimationFrame(drawEdges)}
function drawEdges(){
const old=constellation.querySelector('svg');if(old)old.remove();if(!context)return;
const positions=new Map();const bounds=constellation.getBoundingClientRect();
for(const b of constellation.querySelectorAll('[data-node]')){const r=b.getBoundingClientRect();positions.set(b.dataset.node,{x:r.left-bounds.left+constellation.scrollLeft,y:r.top-bounds.top+constellation.scrollTop+r.height/2})}
const anchor=constellation.querySelector('.bloom-context');if(anchor){const r=anchor.getBoundingClientRect();positions.set(context,{x:r.left-bounds.left,y:r.top-bounds.top+constellation.scrollTop+r.height/2})}
const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.classList.add('provenance-lines');svg.setAttribute('aria-hidden','true');svg.setAttribute('width',String(constellation.scrollWidth));svg.setAttribute('height',String(constellation.scrollHeight));
for(const e of data.edges){const a=positions.get(e.source),b=positions.get(e.target);if(!a||!b)continue;const path=document.createElementNS(svg.namespaceURI,'path');path.setAttribute('d',`M ${a.x} ${a.y} C 3 ${a.y}, 3 ${b.y}, ${b.x} ${b.y}`);path.dataset.source=e.source;path.dataset.target=e.target;const title=document.createElementNS(svg.namespaceURI,'title');title.textContent=e.relation+' · '+e.record;path.append(title);svg.append(path)}constellation.prepend(svg);emphasis()
}
window.addEventListener('resize',()=>requestAnimationFrame(drawEdges));
function label(key){return ({working_set_chars:'Working-set characters',delivered_context_chars:'Delivered-context characters',working_to_delivered_ratio:'Working / delivered character ratio',as_of_cycle:'Values at selected cycle',collected_content:'Collected source content',provider_requests_sent:'Provider requests sent',exact_record:'Exact accepted event'})[key]||key.replaceAll('_',' ')}
function value(parent,v,key){if(v===null||v===undefined){parent.append(el('span','','Not recorded'));return}if(Array.isArray(v)){const ul=el('ul');for(const item of v){const li=el('li');value(li,item,key);ul.append(li)}parent.append(ul);return}if(typeof v==='object'){for(const [k,item] of Object.entries(v))field(parent,k,item);return}let text=String(v);if(key==='confidence'&&typeof v==='number')text=Math.round(v*100)+'%';if(['time','finished','collected_at'].includes(key)&&!Number.isNaN(Date.parse(text)))text=new Intl.DateTimeFormat('en-US',{dateStyle:'medium',timeStyle:'long',timeZone:'America/Los_Angeles'}).format(new Date(text));if(/^https?:\/\//i.test(text)){const a=el('a','',text);a.href=text;a.target='_blank';a.rel='noopener noreferrer';parent.append(a)}else mark(parent,text)}
function field(parent,key,v){const div=el('div','detail-field');div.append(el('span','detail-label',label(key)));const body=el('div','detail-value');value(body,v,key);div.append(body);parent.append(div)}
function showDetails(id){const n=nodes.get(id);details.replaceChildren();details.classList.add('active');const heading=el('div','detail-heading');heading.append(el('span','eyebrow',labels[n.kind]));const browse=el('button','browse-artifacts','Browse artifacts');browse.addEventListener('click',()=>{details.classList.remove('active');constellation.querySelector('button')?.focus({preventScroll:true})});heading.append(browse);const close=el('button','','Close');close.addEventListener('click',clear);heading.append(close);details.append(heading);const title=el('h2','',n.title);title.tabIndex=-1;details.append(title);
if(n.kind==='blog'&&!origin.has(id))details.append(el('p','','No originating wake is established by this export.'));
if(context&&n.kind!=='journal'){const back=el('button','','Back to cycle '+nodes.get(context).detail.cycle);back.addEventListener('click',()=>select(context));details.append(back)}
const order=['status','lede','summary','body','statement','task','question','findings','limitations','next_questions','reason','changes','collected_content','source','confidence','evidence','notebooks','project','time','provider','model','as_of_cycle','cycle'];
const entries=Object.entries(n.detail).filter(([k])=>k!=='title'&&k!=='type');entries.sort(([a],[b])=>(order.includes(a)?order.indexOf(a):100)-(order.includes(b)?order.indexOf(b):100));
for(const [key,v] of entries)field(details,key,v);
if(n.detail.working_set_metrics||n.detail.retrieval_metrics)details.append(el('p','exact',data.meta.shadow_note));
if(n.kind==='journal'){const inv=nodes.get('invocation:'+n.detail.invocation);if(inv?.detail.working_set_metrics){field(details,'working_set_metrics',inv.detail.working_set_metrics);details.append(el('p','exact',data.meta.shadow_note))}}
const relevant=(adjacency.get(id)||[]).filter(e=>!context||e.source===context||e.target===context||[e.source,e.target].every(k=>k===id||(nodes.get(context).expands||[]).includes(k)||data.blogs.includes(k)));
if(relevant.length){details.append(el('h3','','Recorded relationships'));for(const e of relevant){const other=e.source===id?e.target:e.source;const row=el('div','relationship');const b=el('button','',(e.source===id?'→ ':'← ')+e.relation+' · '+nodes.get(other).title);b.addEventListener('click',()=>select(other));row.append(b,el('small','',e.record));details.append(row)}}
const exact=el('p','exact','Map identifier: '+n.id);details.append(exact);const link=el('a','','Read the exact history →');link.href='events.html';details.append(link);title.focus({preventScroll:true})}
function select(id){
if(!nodes.has(id))return;
lastFocus=document.querySelector(`[data-node="${CSS.escape(id)}"]`)||lastFocus;
const previousContext=context;
selected=id;
const n=nodes.get(id);
if(n.kind==='journal')context=id;
else if(n.kind==='blog'){const origins=origin.get(id)||[];context=origins.length===1?origins[0]:null}
// Keep the existing artifact nodes and scroll position when inspecting the
// same wake. Redrawing is only necessary when the wake context changes.
if(context!==previousContext)bloom();
showDetails(id);clearButton.disabled=false;emphasis();
}
function clear(){selected=null;context=null;constellation.innerHTML=emptyConstellation;details.innerHTML=emptyDetails;details.classList.remove('active');clearButton.disabled=true;emphasis();if(lastFocus?.isConnected)lastFocus.focus({preventScroll:true});else timeline.querySelector('button')?.focus({preventScroll:true})}
clearButton.addEventListener('click',clear);document.addEventListener('keydown',e=>{if(e.key==='Escape')clear()});document.getElementById('map-field').addEventListener('click',e=>{if(e.target.id==='map-field'||e.target.classList.contains('spatial')||e.target.id==='timeline'||e.target.id==='constellation')clear()});
const theme=document.getElementById('theme-toggle');function syncTheme(){const dark=document.documentElement.dataset.theme==='dark';theme.checked=dark;theme.setAttribute('aria-label',dark?'Use light theme':'Use dark theme')}syncTheme();theme.addEventListener('change',()=>{const dark=theme.checked;if(dark)document.documentElement.dataset.theme='dark';else delete document.documentElement.dataset.theme;try{localStorage.setItem('wake-theme',dark?'dark':'light')}catch{}syncTheme()});try{const systemTheme=matchMedia('(prefers-color-scheme:dark)');systemTheme.addEventListener('change',event=>{if(localStorage.getItem('wake-theme'))return;if(event.matches)document.documentElement.dataset.theme='dark';else delete document.documentElement.dataset.theme;syncTheme()})}catch{}
})();
