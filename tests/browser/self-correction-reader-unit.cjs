/* Read-only reader contracts; no browser automation or native records. */
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const reader=fs.readFileSync('wake/assets/self-correction/self-correction.js','utf8');
const transport=fs.readFileSync('wake/assets/public-data.js','utf8');
const revision='a'.repeat(40),newRevision='b'.repeat(40);
const storageKey='wake-public-snapshot:sudofx/wake:fixture';
const flush=async()=>{for(let i=0;i<12;i++)await new Promise(resolve=>setImmediate(resolve));};
class Element{
 constructor(tag){this.tag=tag;this.children=[];this.dataset={};this.textContent='';this.events={};}
 append(...children){this.children.push(...children);}
 replaceChildren(...children){this.children=children;}
 addEventListener(event,fn){this.events[event]=fn;}
}
async function page({bound=true,pin='',store=new Map(),outcome='healthy',apiFails=false,remoteFails=false,discovered=revision}={}){
 const nodes=new Map(),events={},calls=[],intervals=[];let reloads=0;
 const document={hidden:false,readyState:'loading',currentScript:{src:'https://example.test/wake/public-data.js'},
  getElementById:id=>{if(!nodes.has(id))nodes.set(id,new Element('div'));return nodes.get(id);},
  createElement:tag=>new Element(tag),addEventListener:(event,fn)=>{events[event]=fn;}};
 const location={href:'https://example.test/wake/self-correction/'+pin,reload:()=>{reloads++;}};
 const config={repository:'sudofx/wake',branch:'wake-public',installation_id:'fixture',prefix:''};
 const window=bound?{WAKE_DEPLOYMENT:{snapshot_only:true,public_data:config}}:{};window.parent=window;
 const snapshot=enabled=>({schema:1,live:false,installation_id:'fixture',generated:'2026-10-29T12:00:00Z',
  record_heads:Object.fromEntries(Array.from({length:12},(_,i)=>[i,{}])),
  nodes:Array.from({length:12},(_,i)=>({id:`${100+i}.wake`,snapshot:{version:42,head:'c'.repeat(64),generated:'2026-10-29T11:59:00Z'},
   research:{status:{autonomous_context:{schema:'autonomous-context@1',enabled,policy:{selector:'deadline-priority'},trials:2,adoptions:1,rollbacks:0}}}}))});
 const fetch=async input=>{
  const url=new URL(input);calls.push(url.href);
  if(url.hostname==='api.github.com'){
   if(apiFails)return new Response('{}',{status:403});
   if(url.pathname.includes('/git/ref/'))return Response.json({object:{type:'commit',sha:discovered}});
   if(url.pathname.endsWith('/jobs'))return Response.json({jobs:[{name:`Outcome: ${outcome}`,status:'completed',conclusion:'success'}]});
   if(url.pathname.endsWith('/pulls'))return Response.json([]);
   return Response.json({workflow_runs:[61,60].map(id=>({id,status:'completed',conclusion:'success',html_url:`https://github.com/sudofx/wake/actions/runs/${id}`,created_at:'2026-10-29T12:00:00Z'}))});
  }
  if(url.hostname==='raw.githubusercontent.com'&&remoteFails)return new Response('{}',{status:404});
  return Response.json(snapshot(url.hostname==='raw.githubusercontent.com'));
 };
 const context={window,document,location,URL,fetch,localStorage:{getItem:key=>store.get(key)||null,setItem:(key,value)=>store.set(key,value)},
  AbortSignal,AbortController,TextDecoder,TextEncoder,Uint8Array,Date,JSON,setTimeout,clearTimeout,setInterval:(fn,ms)=>intervals.push({fn,ms})};
 vm.runInNewContext(transport,context);vm.runInNewContext(reader,context);await flush();
 return {nodes,events,calls,intervals,window,store,get reloads(){return reloads;}};
}
(async()=>{
 let p=await page();
 assert.equal(p.window.WakePublicData.revision,revision);
 assert.equal(p.nodes.get('adaptation-nodes').children.length,12);
 assert.equal(p.nodes.get('adaptation-nodes').children[0].children[1].textContent,'Enabled','Bound page reads the newer published packet');
 assert.match(p.nodes.get('adaptation-nodes').children[0].children[0].children[0].href,new RegExp('public_revision='+revision));
 assert.match(p.nodes.get('snapshot-status').textContent,/captured/);
 assert.equal(p.nodes.get('correction-runs').children[0].children[1].textContent,'healthy — no repair needed');
 assert.equal(p.calls.filter(url=>url.includes('/jobs?')).length,1,'Read jobs only for latest run');
 assert(p.calls.some(url=>url.includes('/61/jobs?per_page=50')));
 assert.equal(p.intervals[0].ms,600000);
 const before=p.calls.length,packets=p.calls.filter(url=>url.includes('/installation.json')).length;
 p.events.visibilitychange();p.intervals[0].fn();await flush();assert.equal(p.calls.length,before,'Metadata cache avoids extra anonymous requests');
 assert.equal(p.calls.filter(url=>url.includes('/installation.json')).length,packets,'Polling does not mix snapshot generations');
 const again=await page({store:p.store});assert(!again.calls.some(url=>url.includes('/actions/')||url.includes('/pulls')),'Metadata cache survives navigation');
 p.nodes.get('refresh').events.click();assert.equal(p.reloads,1);
 assert.equal(JSON.parse(p.store.get(storageKey)).revision,revision,'Refresh retains last verified revision');
 assert.equal(JSON.parse(p.store.get(storageKey)).time,0);
 const refreshed=await page({store:p.store,discovered:newRevision});assert.equal(refreshed.window.WakePublicData.revision,newRevision,'Refresh can select a newer immutable snapshot');
 p=await page({pin:'?public_revision='+revision,discovered:newRevision});assert.equal(p.window.WakePublicData.revision,revision);
 assert(!p.calls.some(url=>url.includes('/git/ref/')));const saved=p.store.get(storageKey);p.nodes.get('refresh').events.click();assert.equal(p.store.get(storageKey),saved,'Explicit pins are never expired by Refresh');
 p=await page({bound:false});assert.equal(p.nodes.get('adaptation-nodes').children[0].children[1].textContent,'Disabled');
 assert(p.calls.some(url=>url==='https://example.test/wake/installation.json'));assert(!p.calls.some(url=>url.includes('raw.githubusercontent.com')));
 p=await page({pin:'?public_revision='+revision,remoteFails:true});assert.equal(p.nodes.get('adaptation-nodes').children.length,0);assert(!p.calls.includes('https://example.test/wake/installation.json'),'Unavailable explicit revision cannot mix in bundled data');
 const cache=new Map([[storageKey,JSON.stringify({revision,time:0})]]);p=await page({apiFails:true,store:cache});assert.equal(p.window.WakePublicData.revision,revision,'API failure recovers last verified public snapshot');
 assert.equal(p.nodes.get('adaptation-nodes').children[0].children[1].textContent,'Enabled');
 const failedAgain=await page({apiFails:true,store:cache});assert(!failedAgain.calls.some(url=>url.includes('/actions/')||url.includes('/pulls')),'Failed metadata reads also respect ten-minute backoff');
 for(const [outcome,label] of [['repaired','repair applied'],['republished','website republished'],['review_required','proposal needs review'],['provider_wait','waiting for provider'],['outside_scope','outside repair scope'],['budget_wait','waiting for budget'],['failed','check failed']]){
  p=await page({outcome});assert.equal(p.nodes.get('correction-runs').children[0].children[1].textContent,label);
 }
 p=await page({outcome:'unknown'});assert.equal(p.nodes.get('correction-runs').children[0].children[1].textContent,'success');assert.match(p.nodes.get('workflow-observed').textContent,/does not establish a repair/);
 console.log('PASS: pinned evidence, same-origin local mode, no mixed generations, recovery, refresh, outcomes and bounded cached API observations');
})().catch(error=>{console.error(error);process.exitCode=1;});
