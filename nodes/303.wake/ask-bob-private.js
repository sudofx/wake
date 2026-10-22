/* Use the same runtime/API with the CPU-only, wasm32 private-memory build. */
export function privateEngine(Wllama, paths, config) {
  const engine = new Wllama({default:paths.wasm},config);
  // This public native resource hook also pins wasm32/Asyncify on browsers that
  // support Memory64/JSPI: the private binary has a different import ABI.
  engine.getWorkerResources = () => ({
    wasmPath:paths.wasm,jsPath:paths.worker,compat:true,noWebGPU:true
  });
  return engine;
}
