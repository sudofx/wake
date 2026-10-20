// This expiring JSON file is an observation, never a record or control plane.
const nodes = new Set([100,101,102,103,200,201,202,203,300,301,302,303].map(n=>`${n}.wake`));
const stages = new Set(['idle','record','context','collecting','provider_wait','provider','provider_uncoordinated','provider_response','governance','continuity','receipt']);
const states = new Set(['running','idle','paused','stopped','waiting','standby','blocked','unavailable']);
const ttl = 12000;
export function sanitize(value, installation, now=Date.now()) {
  if(value?.schema!==1 || value.installation_id!==installation || !/^\d+$/.test(value.run_id||'') || !/^[0-9a-f]{40}$/.test(value.source_revision||'') || !Array.isArray(value.members) || value.members.length!==12 || !Number.isFinite(Date.parse(value.observed_at)) || Math.abs(now-Date.parse(value.observed_at))>ttl) throw Error('Invalid observation');
  const seen=new Set();
  const members=value.members.map(member=>{
    if(!nodes.has(member.id)||seen.has(member.id))throw Error('Invalid member');seen.add(member.id);
    const r=member.runtime||{},a=r.activity||{},fresh=Number.isFinite(Date.parse(r.observed_at))&&Math.abs(now-Date.parse(r.observed_at))<=ttl;
    if(!fresh||!states.has(r.state)||!stages.has(a.stage)||r.activity_schema!==1||r.capabilities?.live_activity!==true||typeof r.runtime_id!=='string'||r.runtime_id.length>100)return {id:member.id,runtime:{state:'unavailable'}};
    const active=['running','standby'].includes(r.state)&&a.active===true&&a.stage!=='idle';
    return {id:member.id,runtime:{mode:'standalone',state:r.state,runtime_id:r.runtime_id,observed_at:r.observed_at,activity_schema:1,capabilities:{live_activity:true},activity:{stage:a.stage,active,invocation_id:typeof a.invocation_id==='string'&&/^w-[a-f0-9]{16}$/.test(a.invocation_id)?a.invocation_id:null,coordinate_id:active&&typeof a.coordinate_id==='string'&&/^[A-Za-z0-9_.:-]{1,120}$/.test(a.coordinate_id)?a.coordinate_id:null}}};
  });
  const call=value.coordinator?.active;
  return {schema:1,mode:'installation',installation_id:installation,run_id:value.run_id,source_revision:value.source_revision,observed_at:value.observed_at,members,coordinator:{queued:Number.isSafeInteger(value.coordinator?.queued)&&value.coordinator.queued>=0?Math.min(value.coordinator.queued,12):0,active:call?.confirmed===true&&nodes.has(call.member)?{member:call.member,confirmed:true,model:typeof call.model==='string'&&/^[A-Za-z0-9_.:-]{1,100}$/.test(call.model)?call.model:null}:null}};
}
export default {async fetch(request,env){
  const headers={'Content-Type':'application/json','Cache-Control':'no-store','Access-Control-Allow-Origin':'https://sudofx.github.io','Vary':'Origin','X-Content-Type-Options':'nosniff'};
  const reply=(data,status=200)=>new Response(JSON.stringify(data),{status,headers});
  const path=new URL(request.url).pathname;
  if(path==='/activity.json'&&request.method==='GET'){
    const object=await env.BUCKET.get('activity.json');
    if(!object)return reply({available:false});
    try{return reply(sanitize(await object.json(),env.INSTALLATION_ID));}catch{return reply({available:false});}
  }
  if(path!=='/ingest'||request.method!=='POST')return reply({error:'Not found'},404);
  if(!env.INGEST_TOKEN||request.headers.get('Authorization')!==`Bearer ${env.INGEST_TOKEN}`)return reply({error:'Unauthorized'},401);
  if(!request.headers.get('content-type')?.startsWith('application/json'))return reply({error:'JSON required'},415);
  if(Number(request.headers.get('content-length'))>32768)return reply({error:'Too large'},413);
  try{
    const reader=request.body?.getReader();let size=0,parts=[];
    if(!reader)throw Error('Missing body');
    while(true){const {value,done}=await reader.read();if(done)break;size+=value.length;if(size>32768){await reader.cancel();return reply({error:'Too large'},413);}parts.push(value);}
    const bytes=new Uint8Array(size);let offset=0;for(const part of parts){bytes.set(part,offset);offset+=part.length;}
    const packet=sanitize(JSON.parse(new TextDecoder().decode(bytes)),env.INSTALLATION_ID);
    const previous=await env.BUCKET.get('activity.json');
    if(previous){const old=await previous.json();if(BigInt(old.run_id)>BigInt(packet.run_id)||(old.run_id===packet.run_id&&Date.parse(old.observed_at)>Date.parse(packet.observed_at)))return reply({error:'Superseded observation'},409);}
    await env.BUCKET.put('activity.json',JSON.stringify(packet),{httpMetadata:{contentType:'application/json',cacheControl:'no-store'}});
    return reply({ok:true});
  }catch{return reply({error:'Invalid observation'},400);}
}};
