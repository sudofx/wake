import {test} from 'node:test';
import assert from 'node:assert/strict';
import worker,{sanitize} from '../worker/index.js';
const installation='fixture-installation';
function fixture(){return {schema:1,installation_id:installation,run_id:'100',source_revision:'a'.repeat(40),observed_at:new Date().toISOString(),members:[100,101,102,103,200,201,202,203,300,301,302,303].map(n=>({id:`${n}.wake`,runtime:{mode:'standalone',state:'running',runtime_id:'runtime-1',activity_schema:1,capabilities:{live_activity:true},observed_at:new Date().toISOString(),activity:{stage:'provider',active:true,coordinate_id:'axis:1',private:'never-publish'},prompt:'never-publish'}})),coordinator:{queued:2,active:{confirmed:true,member:'100.wake',model:'model',token:'never-publish'}},passenger:'never-publish'};}
test('public projection strips private fields, expires, and rejects other installations',()=>{
 const p=fixture(),safe=sanitize(p,installation);assert(!JSON.stringify(safe).includes('never-publish'));assert.equal(safe.members.length,12);assert(safe.coordinator.active.confirmed);
 assert.throws(()=>sanitize(p,installation,Date.now()+13000));assert.throws(()=>sanitize(p,'other'));p.members[1].id=p.members[0].id;assert.throws(()=>sanitize(p,installation));
 const q=fixture();q.coordinator.active.confirmed=false;assert.equal(sanitize(q,installation).coordinator.active,null);
});
test('only authenticated bounded ingestion can update the expiring public file',async()=>{
 let stored=null;const env={INSTALLATION_ID:installation,INGEST_TOKEN:'fixture',BUCKET:{get:async()=>stored?{json:async()=>JSON.parse(stored)}:null,put:async(k,v)=>{assert.equal(k,'activity.json');stored=v;}}};
 const send=(body,auth='Bearer fixture')=>worker.fetch(new Request('https://relay.test/ingest',{method:'POST',headers:{Authorization:auth,'Content-Type':'application/json'},body:JSON.stringify(body)}),env);
 assert.equal((await send(fixture(),'wrong')).status,401);assert.equal(stored,null);
 assert.equal((await send(fixture())).status,200);assert(!stored.includes('never-publish'));
 const get=()=>worker.fetch(new Request('https://relay.test/activity.json'),env);
 let response=await get();assert.equal(response.headers.get('access-control-allow-origin'),'https://sudofx.github.io');assert.equal((await response.json()).members.length,12);
 const older=fixture();older.run_id='99';assert.equal((await send(older)).status,409);
 stored=JSON.stringify({...JSON.parse(stored),observed_at:'2000-01-01T00:00:00Z'});assert.deepEqual(await (await get()).json(),{available:false});
 assert.equal((await worker.fetch(new Request('https://relay.test/runtime/control'),env)).status,404);
 assert.equal((await send({payload:'x'.repeat(33000)})).status,413);
});
