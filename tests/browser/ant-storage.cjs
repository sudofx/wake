const test=require('node:test'),assert=require('node:assert/strict');
const {ColonyPersistence}=require('../../wake/assets/ant-farm.js');
function memory(value=null){return {value,getItem(){return this.value;},setItem(key,next){this.value=next;}};}
test('reload and delayed duplicate events do not pause or block saving',()=>{
 const storage=memory(),first=new ColonyPersistence(storage,'colony');
 assert.equal(first.save({ticks:1}),true);
 const old=storage.value,reloaded=new ColonyPersistence(storage,'colony');
 assert.equal(reloaded.observe({key:'colony',newValue:old}),false);
 assert.equal(reloaded.save({ticks:2}),true);
 assert.equal(reloaded.observe({key:'colony',newValue:old}),false);
 assert.equal(reloaded.conflict,false);
});
test('self notification is ignored even when storage reports synchronously',()=>{
 const storage=memory(),slot=new ColonyPersistence(storage,'colony');
 storage.setItem=(key,value)=>{storage.value=value;assert.equal(slot.observe({key,newValue:value}),false);};
 assert.equal(slot.save({ticks:1}),true);assert.equal(slot.conflict,false);
});
test('another current writer or storage clearing blocks stale overwrites',()=>{
 for(const changed of ['{"ticks":3}',null]){
  const storage=memory('{"ticks":1}'),slot=new ColonyPersistence(storage,'colony');
  storage.value=changed;assert.equal(slot.observe({key:changed===null?null:'colony',newValue:changed}),true);
  assert.equal(slot.save({ticks:2}),false);assert.equal(storage.value,changed);
 }
 const storage=memory('{"ticks":1}'),slot=new ColonyPersistence(storage,'colony');
 storage.value='{"ticks":3}';assert.equal(slot.save({ticks:2}),false);assert.equal(storage.value,'{"ticks":3}');
});
test('failed atomic saves retain the last known stored value',()=>{
 const storage=memory('{"ticks":1}'),slot=new ColonyPersistence(storage,'colony');
 storage.setItem=()=>{throw Error('Quota exceeded');};
 assert.throws(()=>slot.save({ticks:2}));assert.equal(slot.value,'{"ticks":1}');
});
