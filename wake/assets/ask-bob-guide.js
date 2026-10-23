/* Source retrieval, not generated claims. All preparation belongs to public export. */
const BASE = new URL('.', import.meta.url), encoder = new TextEncoder();
const STOP = new Set('the a an and or of to in on at for is are was were be been this that it its with from as by we our they their not can could would should what how why when where which does do about explain please tell mean means'.split(' '));
export const terms = text => [...new Set((text.toLowerCase().match(/[a-z0-9]{3,}/g) || []).filter(x=>!STOP.has(x)))];
const stem = word => word.replace(/(?:ing|es|s)$/,'');
export function search(guide, question, history = []) {
  if (!question.trim() || question.length > 2000) throw Error('Ask a question of at most 2,000 characters.');
  const summary = /^(what(?:’s|'s| is) (?:the )?(?:main point|takeaway)|summari[sz]e|summary|(?:give me |in )?(?:plain|simple) (?:english|language|words))/i.test(question.trim());
  const summaryQuestion = summary || /^(what is this (?:article|about)|what happened)\??$/i.test(question.trim());
  // A short follow-up may borrow only the previous question, never its answer.
  let query = terms(question);
  if (/^(?:why|how so|what about (?:it|that)|explain (?:it|that))\??$/i.test(question.trim())) {
    const previous = history.at(-1);
    if (typeof previous?.question === 'string') query = terms(previous.question + ' ' + question);
  }
  const q = new Set(query.map(stem));
  const rows = guide.passages.map((p,index)=>{
    const words = new Set(p.terms.map(stem)), hits = [...q].filter(w=>words.has(w));
    const rarity = hits.reduce((sum,w)=>sum + Math.log(1 + guide.passages.length / (1 + guide.passages.filter(row=>row.terms.some(t=>stem(t)===w)).length)),0);
    return {p,index,hits:hits.length,score:rarity / Math.sqrt(Math.max(1,p.text.length / 500)) + (p.source==='S1' ? .05 : 0)};
  });
  const evidenceQuestion=/\b(?:evidence|sources?|citations?)\b/i.test(question) && /\b(?:cited|used|supports?|supporting|what|which)\b/i.test(question);
  const limitationsQuestion=/\b(?:limitations?|uncertain(?:ty|ties)?|unknowns?|caveats?)\b/i.test(question);
  if(limitationsQuestion) for(const word of ['uncertain','uncertainty','limitation','limits','unknown','not','unproven','failed'])q.add(stem(word));
  // Re-score expanded limitation terms without accepting instructions in source text.
  if(limitationsQuestion)for(const row of rows){row.hits=[...q].filter(w=>row.p.terms.some(t=>stem(t)===w)).length;row.score=row.hits;}
  let selected;
  if (summaryQuestion) {
    const article = rows.filter(r=>r.p.source==='S1');
    selected = article.filter(r=>r.p.field==='lede').slice(0,1);
    if (!selected.length) selected = article.slice(0,2);
  } else if(evidenceQuestion) {
    selected=guide.sources.filter(s=>s.collection==='evidence').slice(0,4).map(s=>({p:{source:s.id,field:'reference',text:s.label,terms:[]}}));
  } else {
    selected = rows.filter(r=>r.hits >= Math.min(2,q.size) && r.hits > 0).sort((a,b)=>b.score-a.score || a.index-b.index).slice(0,3);
  }
  // Exact source text is displayed as quotations, never as a synthesized answer.
  const unique = selected.filter((r,i,a)=>a.findIndex(v=>v.p.text===r.p.text)===i);
  const matches = unique.map(r=>({...r.p,source_info:guide.sources.find(s=>s.id===r.p.source)}));
  return {matches,kind:summaryQuestion?'summary':evidenceQuestion?'sources':'passages',query_terms:query};
}
const pathFor = id => {
  const hex = Array.from(encoder.encode(id), b=>b.toString(16).padStart(2,'0')).join('');
  return 'reader-records/guides/' + hex.match(/.{1,64}/g).join('/') + '.json';
};
const cache = new Map();
export async function loadGuide(request, signal, read = fetch) {
  if (typeof request.article_id !== 'string' || !request.article_id || request.article_id.length>240 || !/^[a-f0-9]{64}$/.test(request.expected_article_hash)) throw Error('Reload a verified article before asking.');
  const key=request.article_id+':'+request.expected_article_hash;
  if(cache.has(key))return cache.get(key);
  const response=await read(new URL(pathFor(request.article_id),BASE),{signal,credentials:'omit',cache:'no-cache'});
  if(!response.ok||!response.body)throw Error('The article guide is unavailable. Reload the latest published page.');
  const reader=response.body.getReader(),chunks=[];let size=0;
  try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>98304)throw Error('Article guide exceeds its reading budget.');chunks.push(value);}}finally{await reader.cancel();}
  const bytes=new Uint8Array(size);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
  const guide=JSON.parse(new TextDecoder().decode(bytes));
  if(guide.schema!==1||guide.article?.id!==request.article_id||guide.article?.hash!==request.expected_article_hash||guide.article.head!==guide.head||!Array.isArray(guide.passages)||guide.passages.length>180||!Array.isArray(guide.sources)||guide.sources.some(s=>s.head!==guide.head))throw Error('The article guide changed. Reload this article.');
  for(const p of guide.passages)if(typeof p.text!=='string'||Array.from(p.text).length>1000||!Array.isArray(p.terms)||!p.terms.every(t=>typeof t==='string')||!guide.sources.some(s=>s.id===p.source))throw Error('Invalid published passage.');
  cache.set(key,guide);if(cache.size>4)cache.delete(cache.keys().next().value);return guide;
}
export async function answer(request,signal,progress=()=>{}) {
  const start=performance.now();progress('Finding published passages',{stage:'answer'});
  const guide=await loadGuide(request,signal);
  const result=search(guide,request.question,request.history);
  if(signal?.aborted)throw new DOMException('Cancelled','AbortError');
  const lead=result.matches.length ? (result.kind==='summary' ? 'Here is the article’s published summary:' : 'These published passages may help:') : 'I couldn’t find a passage that answers that in this article or its linked public sources. Try a specific term, or ask for the main point. This does not establish that the claim is false.';
  const value=result.kind==='sources'&&result.matches.length ? 'These public source records are cited. Open each reference below to inspect it; citation alone does not verify a claim.\n\n'+result.matches.map(p=>p.source_info.label+' ['+p.source+']').join('\n\n') : [lead,...result.matches.map(p=>'“'+p.text+'” ['+p.source+']')].join('\n\n');
  return {ok:true,answer:value,article:guide.article,citations:guide.sources.filter(s=>result.matches.some(p=>p.source===s.id)),
    warnings:['Source excerpts, not a generated explanation or independent fact check.',...(guide.omitted?.length?['Some linked material exceeds the guide budget or is unavailable. Open the article’s source links for more.']:[])],missing:[],
    metrics:{mode:'published-passages',latency_ms:Math.round(performance.now()-start),model_bytes:0,passages:guide.passages.length}};
}
