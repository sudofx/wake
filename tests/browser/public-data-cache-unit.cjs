/* API discovery failure must not discard a newer, validated immutable export. */
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync('wake/assets/public-data.js','utf8'),revision='a'.repeat(40);
const now=Date.now(),key='wake-public-snapshot:example/wake:fixture';
async function scenario({bundleNewer=false,wrongIdentity=false,backoff=false,cache=true}={}){
 let saved=cache?JSON.stringify({revision,time:now-240000,...(backoff?{failedAt:now-1000}:{})}):null;
 const initial=saved,calls=[],manifest={schema:1,installation_id:'fixture',live:false,nodes:Array(12).fill({}),record_heads:Object.fromEntries(Array.from({length:12},(_,i)=>[i,{}])),generated:new Date(now-60000).toISOString()};
 const window={WAKE_DEPLOYMENT:{snapshot_only:true,public_data:{repository:'example/wake',branch:'wake-public',installation_id:'fixture'}}};window.parent=window;
 const location=new URL('https://example.test/wake/');
 const fetch=async input=>{const url=new URL(input);calls.push(url.href);if(url.hostname==='api.github.com')return new Response('{}',{status:403});
  return new Response(JSON.stringify({...manifest,installation_id:wrongIdentity&&url.hostname==='raw.githubusercontent.com'?'other':'fixture',generated:url.hostname==='example.test'?new Date(now+(bundleNewer?0:-3600000)).toISOString():manifest.generated}));};
 const localStorage={getItem:k=>k===key?saved:null,setItem:(k,v)=>{if(k===key)saved=v}};
 vm.runInNewContext(source,{window,location,URL,AbortSignal,TextDecoder,Uint8Array,Date,JSON,fetch,localStorage,document:{currentScript:{src:'https://example.test/wake/public-data.js'},readyState:'loading',addEventListener(){}}});
 await window.WakePublicData.ready;
 return {transport:window.WakePublicData,calls,saved,initial};
}
(async()=>{
 let r=await scenario();assert.equal(r.transport.mode,'published');assert.equal(r.transport.revision,revision);
 assert.equal(r.transport.discovery,'last-verified-snapshot');assert.equal(JSON.parse(r.saved).time,now-240000,'Recovery must not refresh discovery age');
 assert(r.calls.some(url=>url.includes('/'+revision+'/installation.json')));
 r=await scenario({backoff:true});assert(!r.calls.some(url=>url.includes('api.github.com')));assert.equal(r.saved,r.initial,'Navigation cannot extend failure backoff');
 for(const options of [{bundleNewer:true},{wrongIdentity:true},{cache:false}]){r=await scenario(options);assert.equal(r.transport.mode,'bundled');assert.equal(r.transport.revision,null);}
 console.log('PASS: API failure recovery, immutable identity, newer bundled data and bounded discovery retry');
})().catch(e=>{console.error(e);process.exitCode=1});
