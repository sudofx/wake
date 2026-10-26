import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const projectRoot = resolve(fileURLToPath(new URL("..", import.meta.url)));
const workerPath = resolve(projectRoot, "dist/server/index.js");
const manifestPath = resolve(projectRoot, "dist/.openai/hosting.json");

const [source, manifest] = await Promise.all([
  readFile(workerPath, "utf8"),
  readFile(manifestPath, "utf8"),
]);
JSON.parse(manifest);

// A data URL forces ESM parsing even though the generated output has no package.json.
const moduleUrl = `data:text/javascript;base64,${Buffer.from(source).toString("base64")}`;
const workerModule = await import(moduleUrl);
assert.equal(
  typeof workerModule.default?.fetch,
  "function",
  `${pathToFileURL(workerPath)} must export default.fetch`,
);
const page = await (await workerModule.default.fetch(new Request('https://bob.test/'), {})).text();
assert.ok(page.includes('<span class="avatar" aria-hidden="true"><svg xmlns='), 'Avatar must embed the canonical vector');
assert.ok(page.includes('viewBox="0 0 512 512"'), 'Avatar must preserve the vector resolution');
assert.ok(!page.includes('<!-- BOB_ICON -->'), 'Icon build placeholder must be resolved');
const report = await workerModule.default.fetch(new Request('https://bob.test/self-correction'), {});
assert.equal(report.status, 200);
assert.ok((await report.text()).includes('CONTROLLED DEMONSTRATION'));
const results = await (await workerModule.default.fetch(new Request('https://bob.test/self-correction/result.json'), {})).json();
assert.equal(results.fixture, true);
assert.equal(results.production_changes, 0);
assert.equal(Object.keys(results.scenarios).length, 5);

console.log("Artifact is valid ESM, exports default.fetch and embeds the vector avatar");
