#!/usr/bin/env node
/* Separate deterministic caretaker; never a Bob model tool or research writer. */
'use strict';
const fs=require('node:fs'),path=require('node:path');
const {Colony}=require('../wake/assets/ant-colony.js');
const client=require('../wake/assets/bob-ant-farm.js');
const SCHEMA='wake-bob-ant-farm@1',MODEL='pellet-tunnels@9',COLONY_ID='bobs-ant-farm',SEED=0x0b0b5a17,MAX_TICKS=6000;
const METRICS=['seconds','ants','born','deaths','starved','food_reserve','protein_reserve','food_remaining','dug','delivered','eggs','larvae','pupae','nurses','queen_alive'];
function metrics(colony){const value=colony.metrics(),result={};for(const key of METRICS){if(key==='queen_alive')result[key]=Boolean(value[key]);else if(Number.isFinite(value[key]))result[key]=value[key];else throw Error('The colony model is missing metric '+key);}return result;}
function compatible(colony){if(colony.save().schema!=='wake-ant-colony@4'||colony.observation().model!==MODEL)throw Error('Bob’s farm requires the reviewed colony model '+MODEL+'.');}
function bootstrap({sourceRevision,at=new Date().toISOString(),ColonyClass=Colony}={}){
  const colony=new ColonyClass(SEED);compatible(colony);
  const state=structuredClone(colony.save()),m=metrics(colony);
  return {schema:SCHEMA,colony_id:COLONY_ID,seed:SEED,model:MODEL,source_revision:sourceRevision,updated_at:at,sequence:0,checkpoint:state,replay:{start:state,ticks:0,care:[]},observation:{from_tick:state.ticks,to_tick:state.ticks,before:m,after:m,feedings:0,food_added:0,care_failures:0,scope:'simulation-only'},care_receipts:[],notes:[]};
}
function advancePacket(input,{ticks=MAX_TICKS,sourceRevision,at=new Date().toISOString(),ColonyClass=Colony}={}){
  if(!Number.isSafeInteger(ticks)||ticks<1||ticks>MAX_TICKS)throw Error('Advance must be between 1 and 6000 ticks.');
  if(!/^[a-f0-9]{40}$/.test(sourceRevision||'')||!client.validDate(at))throw Error('Expected an exact source revision and capture time.');
  const packet=client.validate(input,{ColonyClass}),colony=ColonyClass.restore(packet.checkpoint);compatible(colony);
  const before=metrics(colony);if(!before.queen_alive||before.ants===0)throw Error('Bob’s colony needs attention; refusing to replace or reseed it.');
  const start=structuredClone(colony.save()),care=[];let careFailures=0,advanced=0;
  for(;advanced<ticks;advanced++){
    // Events refer to the state before this step. Replays apply feed, then step.
    if(advanced===0||colony.ticks%100===0){
      const entrance=colony.nodes[colony.exit],x=Math.max(4,Math.min(116,Math.round(entrance.x)));
      const nearby=colony.food.filter(f=>Math.abs(f.x-x)<=3),stock=kind=>nearby.reduce((n,f)=>n+(f.kind===kind?f.left:0),0),near=stock('sugar')+stock('protein'),m=metrics(colony);
      const sugarNeeded=m.food_reserve<40&&stock('sugar')<35,proteinNeeded=m.protein_reserve<16&&stock('protein')<20;
      if(near<200&&(sugarNeeded||proteinNeeded)){
        if(colony.addFood(x))care.push({tick:colony.ticks,action:'feed',x,units:100});else careFailures++;
      }
    }
    colony.step();
    if(!colony.metrics().queen_alive||colony.ants.length===0){advanced++;break;}
  }
  const after=metrics(colony),checkpoint=colony.save(),sequence=packet.sequence+1;
  const note={id:'farm-'+sequence+'-'+checkpoint.ticks,at,from_tick:start.ticks,to_tick:checkpoint.ticks,workers:after.ants,worker_change:after.ants-before.ants,deliveries:after.delivered-before.delivered,new_tunnels:after.dug-before.dug,eggs:after.eggs,larvae:after.larvae,pupae:after.pupae,feedings:care.length,food_added:care.length*100,queen_alive:after.queen_alive};
  return client.validate({schema:SCHEMA,colony_id:COLONY_ID,seed:SEED,model:MODEL,source_revision:sourceRevision,updated_at:at,sequence,checkpoint,replay:{start,ticks:advanced,care},observation:{from_tick:start.ticks,to_tick:checkpoint.ticks,before,after,feedings:care.length,food_added:care.length*100,care_failures:careFailures,scope:'simulation-only'},care_receipts:[...packet.care_receipts,...care].slice(-120),notes:[...packet.notes,note].slice(-48)},{ColonyClass});
}
function flags(args){const result={};for(let i=0;i<args.length;i++){if(!args[i].startsWith('--'))throw Error('Unexpected argument.');const key=args[i].slice(2);result[key]=['bootstrap'].includes(key)?true:args[++i];}return result;}
async function github(repository,token,resource,method='GET',body){
  const response=await fetch('https://api.github.com/repos/'+repository+'/'+resource,{method,headers:{Accept:'application/vnd.github+json',Authorization:'Bearer '+token,'X-GitHub-Api-Version':'2022-11-28'},...(body?{body:JSON.stringify(body)}:{}),signal:AbortSignal.timeout(30000)});
  if(!response.ok){const error=Error('GitHub farm operation failed: '+response.status);error.status=response.status;throw error;}
  return response.status===204?null:response.json();
}
async function publish(options,{request=github,repository=process.env.GITHUB_REPOSITORY||'sudofx/wake',token=process.env.GH_TOKEN}={}){
  if(!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository)||!token)throw Error('Expected GitHub repository and scoped workflow token.');
  const sourceRevision=options['source-revision'];if(!/^[a-f0-9]{40}$/.test(sourceRevision||''))throw Error('Expected exact checked source revision.');
  const branch='bob-ant-farm';let parent,old;
  try{parent=(await request(repository,token,'git/ref/heads/'+branch)).object.sha;}
  catch(error){if(error.status!==404)throw error;if(!options.bootstrap){console.log(JSON.stringify({status:'uninitialized',branch,message:'Explicit bootstrap is required; no colony was created.'}));return;}}
  if(parent&&!/^[a-f0-9]{40}$/.test(parent))throw Error('Invalid farm branch head; preserving it.');
  if(parent){
    let file=await request(repository,token,'contents/farm.json?ref='+parent);
    if(file.type!=='file'||!Number.isSafeInteger(file.size)||file.size<1||file.size>client.MAX_BYTES)throw Error('Invalid existing farm packet; preserving it.');
    if(file.encoding==='none'&&/^[a-f0-9]{40}$/.test(file.sha))file=await request(repository,token,'git/blobs/'+file.sha);
    if(file.encoding!=='base64'||!Number.isSafeInteger(file.size)||file.size<1||file.size>client.MAX_BYTES)throw Error('Invalid existing farm packet; preserving it.');
    const raw=Buffer.from(file.content,'base64');if(raw.length>client.MAX_BYTES)throw Error('Farm packet exceeds public bound.');old=JSON.parse(raw.toString('utf8'));
  }else old=bootstrap({sourceRevision});
  const result=advancePacket(old,{ticks:Number(options.ticks??MAX_TICKS),sourceRevision});
  // Construct a tiny independent tree, never copy source, research exports or records.
  const content=JSON.stringify(result)+'\n';if(Buffer.byteLength(content)>client.MAX_BYTES)throw Error('Farm packet exceeds public bound.');
  const blob=await request(repository,token,'git/blobs','POST',{content,encoding:'utf-8'});
  const tree=await request(repository,token,'git/trees','POST',{tree:[{path:'farm.json',mode:'100644',type:'blob',sha:blob.sha}]});
  const commit=await request(repository,token,'git/commits','POST',{message:'Maintain Bob’s ant farm at tick '+result.checkpoint.ticks,tree:tree.sha,parents:parent?[parent]:[]});
  if(parent)await request(repository,token,'git/refs/heads/'+branch,'PATCH',{sha:commit.sha,force:false});
  else await request(repository,token,'git/refs','POST',{ref:'refs/heads/'+branch,sha:commit.sha});
  console.log(JSON.stringify({status:'published',branch,revision:commit.sha,tick:result.checkpoint.ticks,feedings:result.observation.feedings,queen_alive:result.observation.after.queen_alive}));
}
async function main(){
  const [operation,...args]=process.argv.slice(2),options=flags(args);
  if(operation==='publish'){await publish(options);return;}
  if(operation!=='advance'||!options.output)throw Error('Use advance --input FILE --output FILE --source-revision SHA [--ticks N], or publish with a scoped GH_TOKEN. Bootstrap requires --bootstrap.');
  const sourceRevision=options['source-revision'],at=options.at||new Date().toISOString();
  let old;if(options.input)old=JSON.parse(fs.readFileSync(options.input,'utf8'));else if(options.bootstrap)old=bootstrap({sourceRevision,at});else throw Error('An existing checkpoint or explicit bootstrap is required.');
  const result=advancePacket(old,{ticks:Number(options.ticks??MAX_TICKS),sourceRevision,at});
  const output=path.resolve(options.output),temporary=output+'.tmp-'+process.pid;fs.writeFileSync(temporary,JSON.stringify(result)+'\n');fs.renameSync(temporary,output);
  console.log(JSON.stringify({status:'prepared',tick:result.checkpoint.ticks,feedings:result.observation.feedings,queen_alive:result.observation.after.queen_alive}));
}
module.exports={bootstrap,advancePacket,publish,metrics,SCHEMA,MODEL,COLONY_ID,SEED,MAX_TICKS};
if(require.main===module)main().catch(error=>{console.error(error.message);process.exitCode=1;});
