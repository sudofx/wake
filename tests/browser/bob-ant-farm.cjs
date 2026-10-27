/* Shared farm is a bounded presentation checkpoint, not research authority. */
'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const model=require('../../wake/assets/ant-colony.js'),farm=require('../../scripts/bob_ant_farm.cjs'),clientPath=require.resolve('../../wake/assets/bob-ant-farm.js');
const client=require(clientPath),sourceRevision='a'.repeat(40),at='2026-10-27T01:00:00.000Z';
const initial=()=>farm.bootstrap({sourceRevision,at});
const advance=(packet,options={})=>farm.advancePacket(packet,{sourceRevision,at:'2026-10-27T01:30:00.000Z',ticks:6000,...options});

test('care and replay reproduce the exact checkpoint without mutating the input',()=>{
  const before=initial(),original=JSON.stringify(before),after=advance(before),colony=model.Colony.restore(after.replay.start);let cursor=0;
  assert.equal(JSON.stringify(before),original);
  for(let i=0;i<after.replay.ticks;i++)cursor=client.applyReplayStep(colony,after,cursor);
  assert.equal(cursor,after.replay.care.length);assert.deepEqual(colony.save(),after.checkpoint);
  assert.equal(after.checkpoint.addedFood-after.replay.start.addedFood,after.observation.food_added);
  assert.deepEqual(advance(before),after,'The same input, source and capture time are deterministic');
});

test('upkeep advances bounded model time even after a long calendar outage',()=>{
  const a=advance(initial(),{ticks:100}),b=advance(initial(),{ticks:100,at:'2040-01-01T00:00:00.000Z'});
  assert.deepEqual(a.checkpoint,b.checkpoint);assert.equal(b.checkpoint.ticks,100);
  assert.throws(()=>advance(initial(),{ticks:6001}),/6000/);assert.throws(()=>advance(initial(),{ticks:0}),/6000/);
});

test('the actual care policy sustains four model hours with bounded food',()=>{
  let packet=initial(),maxFood=0,feedings=0;
  for(let i=0;i<24;i++){
    packet=advance(packet,{at:new Date(Date.UTC(2026,9,27,1,i+1)).toISOString()});
    maxFood=Math.max(maxFood,packet.observation.after.food_remaining);feedings+=packet.observation.feedings;
  }
  const m=packet.observation.after;
  assert(m.queen_alive);assert(m.ants>40);assert(m.born>64);assert(m.deaths>0);assert.equal(m.starved,0);assert(m.eggs+m.larvae+m.pupae>0);assert(m.dug>0);assert(m.delivered>0);assert(maxFood<1000);assert(feedings<100);assert(Buffer.byteLength(JSON.stringify(packet))<client.MAX_BYTES);
});

test('a dead or malformed colony is never silently replaced',()=>{
  const packet=initial();packet.checkpoint.queen.alive=false;packet.replay.start.queen.alive=false;packet.observation.before.queen_alive=false;packet.observation.after.queen_alive=false;
  const original=JSON.stringify(packet);assert.throws(()=>advance(packet),/needs attention/);assert.equal(JSON.stringify(packet),original);
  const bad=initial();bad.checkpoint.rng=-1;assert.throws(()=>advance(bad),/Invalid colony/);
});

test('identity, recorded care, metrics, notes and model compatibility are checked',()=>{
  const valid=advance(initial(),{ticks:100});
  const reject=mutate=>{const bad=structuredClone(valid);mutate(bad);assert.throws(()=>client.validate(bad,{ColonyClass:model.Colony}));};
  reject(p=>p.colony_id='someone-else');reject(p=>p.model='unreviewed');reject(p=>p.checkpoint.seed++);reject(p=>p.replay.ticks++);reject(p=>p.replay.care[0].tick=p.checkpoint.ticks);reject(p=>p.replay.care[0].action='eval');reject(p=>p.observation.after.ants++);reject(p=>p.observation.food_added++);reject(p=>p.notes[0].html='<img onerror=alert(1)>');reject(p=>p.notes[0].workers++);reject(p=>p.notes[0].feedings=100000);reject(p=>p.source_revision='main');
  assert.equal(client.validDate('2026-02-31T00:00:00Z'),false);
  assert(client.notebookText(valid.notes[0]).includes(String(valid.notes[0].deliveries)+' food'));
  assert(!client.notebookText(valid.notes[0]).includes('I recorded'));
  assert(!client.notebookText(valid.notes[0]).includes('useful comparison'));
});

test('reader uses only fixed GitHub or explicit same-origin preview and enforces bounds',async()=>{
  const saved={fetch:global.fetch,location:global.location,document:global.document,binding:global.WAKE_DEPLOYMENT,model:global.WakeAntColony};
  const fresh=()=>{delete require.cache[clientPath];return require(clientPath);};
  try{
    global.WakeAntColony=model;global.location={href:'https://preview.invalid/ant-farm.html?state=https://evil.invalid/data.json'};global.document={baseURI:'https://preview.invalid/ant-farm.html'};global.WAKE_DEPLOYMENT={};
    let calls=0;global.fetch=async(url,options)=>{calls++;assert.equal(url,'https://raw.githubusercontent.com/sudofx/wake/bob-ant-farm/farm.json');assert.equal(options.credentials,'omit');assert.equal(options.body,undefined);return new Response(JSON.stringify(advance(initial(),{ticks:100})));};
    const reader=fresh(),packet=await reader.read();assert(Object.isFrozen(packet.checkpoint));await reader.read();assert.equal(calls,1);
    global.WAKE_DEPLOYMENT={bob_ant_farm:{preview_path:'bob-ant-farm.json'}};assert.equal(fresh().sourceURL(),'https://preview.invalid/bob-ant-farm.json');
    global.WAKE_DEPLOYMENT={bob_ant_farm:{preview_path:'https://evil.invalid/bob-ant-farm.json'}};assert.throws(()=>fresh().sourceURL(),/Invalid local/);
    global.WAKE_DEPLOYMENT={};global.fetch=async()=>new Response('x'.repeat(client.MAX_BYTES+1));await assert.rejects(fresh().read(),/reading limit/);
    let fail=true;global.fetch=async()=>{if(fail)throw Error('network fixture');return new Response(JSON.stringify(initial()));};const retry=fresh();await assert.rejects(retry.read(),/network fixture/);fail=false;assert.equal((await retry.read()).colony_id,farm.COLONY_ID);
  }finally{global.fetch=saved.fetch;global.location=saved.location;global.document=saved.document;global.WAKE_DEPLOYMENT=saved.binding;global.WakeAntColony=saved.model;delete require.cache[clientPath];}
});

test('publication appends only the farm branch and refuses competing ref updates',async()=>{
  const old=initial(),parent='b'.repeat(40),requests=[];let rejectUpdate=false;
  const request=async(repository,token,resource,method='GET',body)=>{
    requests.push({repository,resource,method,body});
    if(resource==='git/ref/heads/bob-ant-farm')return{object:{type:'commit',sha:parent}};
    if(resource==='contents/farm.json?ref='+parent)return{type:'file',size:Buffer.byteLength(JSON.stringify(old)),encoding:'base64',content:Buffer.from(JSON.stringify(old)).toString('base64')};
    if(resource==='git/blobs')return{sha:'c'.repeat(40)};
    if(resource==='git/trees'){assert.deepEqual(body.tree.map(row=>row.path),['farm.json']);return{sha:'d'.repeat(40)};}
    if(resource==='git/commits'){assert.deepEqual(body.parents,[parent]);return{sha:'e'.repeat(40)};}
    if(resource==='git/refs/heads/bob-ant-farm'){assert.equal(body.force,false);if(rejectUpdate)throw Error('Ref advanced fixture');return{};}
    throw Error('Unexpected operation '+resource);
  };
  const write=()=>farm.publish({'source-revision':sourceRevision,ticks:100,bootstrap:true},{request,repository:'example/repo',token:'fixture-only'});
  const previous=console.log;try{console.log=()=>{};await write();rejectUpdate=true;await assert.rejects(write(),/Ref advanced/);}finally{console.log=previous;}
  assert(!requests.some(row=>/wake-public|hosted|checkpoint|actions\/workflows/.test(row.resource)));
  assert(requests.filter(row=>row.method==='PATCH').every(row=>row.resource==='git/refs/heads/bob-ant-farm'));
});

test('automatic upkeep leaves an uninitialized farm absent',async()=>{
 const requests=[];const request=async(...args)=>{requests.push(args);const error=Error('Absent fixture');error.status=404;throw error;};
 const previous=console.log;try{console.log=()=>{};await farm.publish({'source-revision':sourceRevision},{request,repository:'example/repo',token:'fixture-only'});}finally{console.log=previous;}
 assert.equal(requests.length,1);assert.equal(requests[0][2],'git/ref/heads/bob-ant-farm');
});
