/* Execute the real transport against cold/mixed publication responses, without a browser or provider. */
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const source=fs.readFileSync(process.argv[2],'utf8');
async function scenario(matching,live){
 const calls=[],state={posts:{old:{id:'old'}},journal:[]},old={head:'old',state,events:[],reader_transport:{schema:1}};
 const next={head:matching?'new':'another',state:{posts:{},journal:[]},events:[],reader_transport:{schema:1}};
 const packet={head:'new',collection:'posts',item:{id:'article',title:'Current article'},article:{id:'article',hash:'a'.repeat(64),head:'new'},related:{},events:[]};
 const window={WAKE_DEPLOYMENT:{snapshot_only:true}};

 const fetch=async path=>{calls.push(path);return {ok:true,json:async()=>structuredClone(path==='reader-data.json'?old:path.startsWith('reader-data.json?')?next:packet)};};
 vm.runInNewContext(source,{window,fetch,AbortSignal,TextEncoder,Set,Map,document:{},setTimeout:()=>{throw Error('Unexpected polling');}});
 const data=await window.WakeData;const identity=data.state;
 if(live)window.WakeApplyLive=value=>{const state=data.state;for(const key of Object.keys(state))delete state[key];Object.assign(state,value.state);Object.assign(data,value,{state});};
 if(matching){
  await window.WakeReader.ensure('blog','article');assert.equal(data.head,'new');assert.equal(data.state,identity);assert.equal(data.state.posts.article.title,'Current article');assert(!data.state.posts.old);
  const before=calls.length;await window.WakeReader.ensure('blog','article');assert.equal(calls.length,before,'Exact current details stay cached');
 }else{
  await assert.rejects(window.WakeReader.ensure('blog','article'),/site is updating/);assert.equal(data.head,'old');assert(data.state.posts.old);assert(!data.state.posts.article);
 }
 assert(calls.some(path=>path==='reader-data.json?head=new'));assert(!calls.includes('wake-data.json'),'Recovery must not download the entire archive');
}
(async()=>{await scenario(true,false);await scenario(true,true);await scenario(false,false);console.log('PASS');})().catch(e=>{console.error(e);process.exitCode=1;});
