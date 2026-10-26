/* Dedicated inference worker. Messages never leave this device. */
import {WebWorkerMLCEngineHandler} from './ask-bob-gpu-engine.js';
const handler = new WebWorkerMLCEngineHandler();
self.onmessage = message => handler.onmessage(message);
