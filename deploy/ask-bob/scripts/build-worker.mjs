import {readFile,writeFile} from 'node:fs/promises';
const root=new URL('../',import.meta.url);
const entry=await readFile(new URL('worker/index.js',root),'utf8');
const ui=await readFile(new URL('worker/chat.js',root),'utf8');
const seam="import {CHAT_HTML} from './chat.js';";
if(!entry.includes(seam))throw Error('Missing chat module seam');
await writeFile(new URL('dist/server/index.js',root),entry.replace(seam,ui.replace('export const CHAT_HTML','const CHAT_HTML')));
