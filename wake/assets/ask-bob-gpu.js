/* GPU-only browser inference. No external answer server or credentials. */
const BASE = new URL('.',import.meta.url);
export const MODELS = Object.freeze({
  starter:{id:'Qwen3-0.6B-q4f16_1-MLC',revision:'8c14ce481d4c692769976ad52afea453a102df19',file:'ask-bob-gpu-starter.wasm',bytes:335372288,label:'Quick start'},
  best:{id:'Qwen3.5-2B-q4f16_1-MLC',revision:'dd74e9c8a20c4546df85c844103bff87b6dcacad',file:'ask-bob-gpu-2b.wasm',bytes:1059315328,label:'Balanced · 1.1 GB'},
  capable:{id:'Qwen3.5-4B-q4f16_1-MLC',revision:'44b42469f9e192814bfd90440e3b377d89ba7a13',file:'ask-bob-gpu-4b.wasm',bytes:2367117312,label:'More capable · 2.4 GB, slower'}
});
let worker, engine, loading = false, answering = false, selected, revision = 0;
export const ready = () => Boolean(engine);
export const current = () => selected;
function appConfig(choice) {
  const model = MODELS[choice];
  return {cacheBackend:'cache',model_list:[{model_id:model.id,model:'https://huggingface.co/mlc-ai/' + model.id + '/resolve/' + model.revision + '/',model_lib:new URL(model.file,BASE).href,required_features:['shader-f16'],overrides:{context_window_size:4096,max_history_size:1}}]};
}
// Populate the engine's native disk cache without creating a worker or GPU.
// Download one shard at a time; never assemble another model in JS/GPU memory.
export async function prefetch(choice,signal) {
  if (!Object.hasOwn(MODELS,choice)) throw Error('Unknown Bob model.');
  const controller = new AbortController(), cancel = () => controller.abort(signal?.reason);
  signal?.addEventListener('abort',cancel,{once:true});
  if(signal?.aborted)cancel();
  const downloadSignal = controller.signal;
  const model = MODELS[choice], root = appConfig(choice).model_list[0].model;
  async function get(cache,path,json = false) {
    downloadSignal.throwIfAborted();
    const url = new URL(path,root).href;
    let response = await cache.match(url);
    if (!response) {
      response = await fetch(url,{credentials:'omit',signal:downloadSignal});
      if (!response.ok) throw Error('Bob’s background preparation paused.');
      await cache.put(url,response);
      response = await cache.match(url);
    }
    downloadSignal.throwIfAborted();
    if(json) return response.json();
  }
  try {return await bounded(async () => {
    const modelCache = await caches.open('webllm/model'), configCache = await caches.open('webllm/config');
    const config = await get(configCache,'mlc-chat-config.json',true);
    const tensors = await get(modelCache,'tensor-cache.json',true);
    const records = tensors.records;
    if (!Array.isArray(records) || !records.length || records.length > 128 || records.some(r => !/^params_shard_\d+\.bin$/.test(r.dataPath) || !Number.isSafeInteger(r.nbytes) || r.nbytes <= 0 || r.nbytes > 536870912) || records.reduce((n,r) => n+r.nbytes,0) < model.bytes || records.reduce((n,r) => n+r.nbytes,0) > model.bytes+1048576) throw Error('Unexpected Bob model package.');
    const tokenizer = config.tokenizer_files?.includes('tokenizer.json') ? 'tokenizer.json' : 'tokenizer.model';
    await get(modelCache,tokenizer);
    for(const record of records) await get(modelCache,record.dataPath);
    return true;
  },{signal,timeout:600000,onStop:cancel});}
  finally {signal?.removeEventListener('abort',cancel);}
}
// Ask the engine's cache, not a localStorage flag that survives eviction. This
// never creates a worker, requests a GPU, or downloads model weights.
export async function cached(choice,signal) {
  if (!Object.hasOwn(MODELS,choice)) return false;
  try {
    return await bounded(async () => {
      const {hasModelInCache} = await import('./ask-bob-gpu-engine.js');
      if(signal?.aborted)throw signal.reason;
      return hasModelInCache(MODELS[choice].id,appConfig(choice));
    },{signal,timeout:8000,onStop:() => {}});
  } catch(error) {if(signal?.aborted)throw signal.reason;return null;}
}
export async function supported() {
  if (!navigator.gpu || !globalThis.Worker) return false;
  try {
    const adapter = await navigator.gpu.requestAdapter();
    return Boolean(adapter?.features.has('shader-f16') && adapter.limits.maxStorageBufferBindingSize >= 134217728);
  } catch {return false;}
}
export function stop() {
  revision++;
  engine?.interruptGenerate();
  worker?.terminate(); worker = undefined; engine = undefined; selected = undefined;
}
async function release() {
  const previous = engine, previousWorker = worker;
  revision++;engine = undefined;worker = undefined;selected = undefined;
  let timer;
  try {if(previous?.unload) await Promise.race([previous.unload(),new Promise(resolve => {timer=setTimeout(resolve,2000);})]);}
  finally {clearTimeout(timer);previousWorker?.terminate();}
}
// Qwen can emit an empty thinking envelope even in non-thinking mode. Never
// flash that markup or intermediate reasoning in the conversation stream.
export function visibleReply(raw) {
  const value = raw.trimStart();
  if (value.startsWith('<think>')) {
    const end = value.indexOf('</think>');
    return end < 0 ? '' : value.slice(end + 8).trimStart();
  }
  if ('<think>'.startsWith(raw.trimStart())) return '';
  return raw;
}
async function bounded(work,{signal,timeout = 180000,onStop = stop} = {}) {
  let timer, abort;
  const stopped = new Promise((_,reject) => {
    abort = () => {onStop(); reject(signal?.reason || new DOMException('Stopped. Your saved download is kept.','AbortError'));};
    timer = setTimeout(() => {onStop(); reject(new DOMException('Bob took too long. Try again; your saved download is kept.','TimeoutError'));},timeout);
    signal?.addEventListener('abort',abort,{once:true});
    if (signal?.aborted) abort();
  });
  try {return await Promise.race([Promise.resolve().then(() => {if(signal?.aborted) throw signal.reason; return work();}),stopped]);}
  finally {clearTimeout(timer); signal?.removeEventListener('abort',abort);}
}
export async function load(choice = 'best',progress = () => {},signal) {
  if (!Object.hasOwn(MODELS,choice)) throw Error('Choose one of Bob’s available models.');
  if (engine && selected === choice) return;
  if (loading || answering) throw Error('Bob is busy. Stop the current operation first.');
  loading = true;
  // Await native unload before replacing a running model; only one owns GPU memory.
  const releasing = release(), operation = revision;
  const cancelled = () => signal?.aborted || revision !== operation;
  try {
    await bounded(async () => {
      await releasing;
      if(cancelled()) throw signal?.reason || new DOMException('Stopped','AbortError');
      if (!await supported()) throw Error('This browser cannot run GPU Bob. Use a current browser with WebGPU support, or choose source search below.');
      if(cancelled()) throw signal?.reason || new DOMException('Stopped','AbortError');
      progress('Opening Bob’s browser engine…',{progress:0});
      const {WebWorkerMLCEngine} = await import('./ask-bob-gpu-engine.js');
      if(cancelled()) throw signal?.reason || new DOMException('Stopped','AbortError');
      const model = MODELS[choice];
      const candidateWorker = new Worker(new URL('ask-bob-gpu-worker.js',BASE),{type:'module'}); worker = candidateWorker;
      const candidate = new WebWorkerMLCEngine(candidateWorker,{
        appConfig:appConfig(choice),
        initProgressCallback:report => {if(!cancelled())progress(report.text,{progress:report.progress});},logLevel:'ERROR'
      });
      const crashed = new Promise((_,reject) => {candidateWorker.onerror = () => reject(Error('Bob’s browser worker stopped. Try again with the smaller download.'));});
      await Promise.race([candidate.reload(model.id),crashed]);
      if (signal?.aborted || worker !== candidateWorker) throw new DOMException('Stopped','AbortError');
      engine = candidate; selected = choice;
    },{signal,timeout:600000});
  } catch(error) {stop(); throw error;}
  finally {loading = false;}
}
export async function generate(messages,{signal,onText = () => {}} = {}) {
  if (!engine) throw Error('Download Bob first.');
  if (answering || loading) throw Error('Bob is busy.');
  answering = true;
  const candidate = engine, start = performance.now(); let first, answer = '', usage, reason;
  try {
    await bounded(async () => {
      const stream = await candidate.chat.completions.create({messages,stream:true,stream_options:{include_usage:true},temperature:0.2,top_p:0.9,repetition_penalty:1.1,frequency_penalty:0.3,max_tokens:420,extra_body:{enable_thinking:false}});
      for await (const chunk of stream) {
        if (signal?.aborted) throw signal.reason;
        const part = chunk.choices?.[0]?.delta?.content;
        if (part) {answer += part; if (answer.length > 10000) throw Error('Bob exceeded the reply limit.'); const visible = visibleReply(answer); if(visible){first ??= performance.now(); onText(visible);}}
        reason = chunk.choices?.[0]?.finish_reason || reason; usage = chunk.usage || usage;
      }
    },{signal,timeout:120000});
    answer = visibleReply(answer);
    if (!answer.trim() || !reason) throw Error('Bob stopped before finishing. Please retry.');
    return {answer,complete:reason === 'stop',metrics:{model:MODELS[selected].id,first_token_ms:Math.round((first || performance.now())-start),latency_ms:Math.round(performance.now()-start),usage}};
  } catch(error) {stop(); throw error;}
  finally {answering = false;}
}
globalThis.addEventListener?.('pagehide',event => {if (!event.persisted) stop();});
