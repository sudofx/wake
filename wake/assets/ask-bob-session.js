/* Automatic device-local preparation. Conversation remains owned by bob-chat. */
import * as gpu from './ask-bob-gpu.js?v=20261026-automatic';

export function createBobSession(notify = () => {}) {
  let opening, openingController, background, pendingUpgrade = false, busy = false, closed = false, upgradeAttempted = false;
  const upgradeKey = 'wake-bob-upgrade-opening';
  // A killed phone tab may not run catch/finally. Reopening must not repeat the
  // very allocation that killed it; the compact model remains usable instead.
  let avoidUpgrade = false;
  try {avoidUpgrade = Date.now() - Number(localStorage.getItem(upgradeKey) || 0) < 86400000;} catch {avoidUpgrade = true;}
  const tell = value => {if(!closed && !busy) notify(value);};
  function open(choice) {
    openingController = new AbortController();
    const controller = openingController;
    const promise = gpu.load(choice,() => tell('Bob is getting ready…'),controller.signal);
    opening = promise;
    promise.finally(() => {if(opening === promise)opening = undefined;}).catch(() => {});
    return promise;
  }
  async function upgrade() {
    if(closed || busy || opening || !pendingUpgrade || upgradeAttempted) return;
    pendingUpgrade = false;upgradeAttempted = true;
    try {
      localStorage.setItem(upgradeKey,String(Date.now()));
      await open('best');
      tell('Bob is ready.');
    } catch {
      // Includes failed storage access: never risk a crash loop without a marker.
      if(!closed) {try {await open('starter');tell('Bob is ready.');} catch {tell('Bob’s published introduction is available. Reopen this chat to retry deeper answers.');}}
    }
  }
  async function improve() {
    if(avoidUpgrade || closed || background) return;
    background = new AbortController();
    try {await gpu.prefetch('best',background.signal);pendingUpgrade = true;await upgrade();}
    catch {/* Background network/storage failure must not interrupt a conversation. */}
  }
  async function start() {
    if(closed || gpu.ready())return;
    if(opening)return opening;
    try {await open('starter');tell('Bob is ready.');void improve();}
    catch(error) {if(!closed)tell('Bob’s published introduction is available. Reopen this chat to retry deeper answers.');throw error;}
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
      const result = await gpu.generate(messages,{signal,onText});
      // Loading weights is not proof that full conversation inference fits.
      if(gpu.current() === 'best')try {localStorage.removeItem(upgradeKey);}catch{}
      return result;
    } finally {signal?.removeEventListener('abort',abort);busy = false;if(!closed)void upgrade();}
  }
  function close() {closed = true;background?.abort();openingController?.abort();gpu.stop();}
  return {start,answer,close};
}
