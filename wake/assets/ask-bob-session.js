/* One compact device-local engine. Conversation remains owned by bob-chat. */
import * as gpu from './ask-bob-gpu.js?v=20261027-phone-recovery';

export function createBobSession(notify = () => {}) {
  let opening, openingController, busy = false, closed = false;
  const tell = value => {if(!closed && !busy) notify(value);};
  async function start() {
    if(closed || gpu.ready())return;
    if(opening)return opening;
    openingController = new AbortController();
    const promise = gpu.load('starter',() => tell('Bob is getting ready…'),openingController.signal);
    opening = promise;
    try {await promise;tell('Bob is ready.');}
    catch(error) {if(!closed)tell('Bob’s published introduction is available. Try your question again to retry preparation.');throw error;}
    finally {if(opening === promise)opening = undefined;}
  }
  async function answer(messages,{signal,onText} = {}) {
    busy = true;
    const abort = () => {openingController?.abort();gpu.stop();};
    signal?.addEventListener('abort',abort,{once:true});
    try {
      signal?.throwIfAborted();
      if(opening) await opening;
      if(!gpu.ready()) await start();
      signal?.throwIfAborted();
      return await gpu.generate(messages,{signal,onText});
    } finally {signal?.removeEventListener('abort',abort);busy = false;}
  }
  // Do not prefetch or switch to another model between replies. A successful
  // load cannot establish that a phone can survive inference with larger weights.
  function close() {closed = true;openingController?.abort();gpu.stop();}
  return {start,answer,close};
}
