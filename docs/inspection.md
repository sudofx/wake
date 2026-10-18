# Let another AI inspect WAKE

The inspection interface is a static reading path over public documentation,
exported snapshots and an isolated kernel demonstration. It gives an observer
evidence to examine without access to research controls, provider credentials or
writable records.

## Start with ordinary text

The public paths are generated under `inspect/` in the unified website:

- `README.md`: compact orientation.
- `manifest.json`: versioned inventory, hashes, snapshot identity and evidence links.
- `architecture.md`: concise structure with links to canonical technical sources.
- `demo.json`: an actual isolated deterministic execution with exact recorded events.
- `evidence.md`: how to inspect and reproduce the evidence.
- `limitations.md`: known limits and reasons to challenge conclusions.
- `evaluate.md`: neutral unfamiliar-observer questions and review procedure.
- `packet.md`: a self-contained document for pasting or uploading without web access.
- `index.html`: a plain HTML list of the same resources, requiring no JavaScript.

The intended public entry is
[the inspection page](https://sudofx.github.io/wake/inspect/).
Availability depends on a completed mirror publication. A source change, generated
local artifact, successful upload and verified hosted response remain separate
outcomes. There is no live inspection API or public executable sandbox.

A model with ordinary web retrieval can begin with
[the orientation](https://sudofx.github.io/wake/inspect/README.md) and
[manifest](https://sudofx.github.io/wake/inspect/manifest.json).
For a model without retrieval, paste or upload `packet.md`; it cannot verify
unprovided URLs merely by reading a link. Supply further source files or records
if the observer requests them.

For example, give an observer this neutral instruction:

> Read the WAKE inspection orientation and follow its evidence links as needed.
> Explain what the system does, how proposals differ from accepted changes,
> what the reproducible example demonstrates, and what remains unverified.
> Cite exact resources, identify unsupported claims and explain any retrieval
> failures. Do not assume the project's conclusions are correct.

Use the uploaded packet instead of the URL when browsing is unavailable.

## Reproduce the kernel example

From a source checkout with Python 3.11 or later:

```sh
python3 -S -m examples.task_list.inspection --output /tmp/wake-inspection-demo.json
```

The generator uses the existing task-list application in a newly created temporary
directory. It adds a task, rejects completion of a missing task, completes the
actual task and checks historical replay. It never opens a production record or
calls a model. The artifact retains real proposals, receipts, event hashes and
timestamps from that execution; it is an exported fixture record, not an invented
transcript or scientific result.

UUIDs, timestamps and resulting event hashes differ between runs. Reproduce the
decision sequence, revisions and replay agreement rather than expecting identical
bytes. Preserve the published artifact's hash when evaluating that specific run.
The [kernel guide](kernel.md#executable-non-research-proof) owns the application
contract and its limits.

## Read the manifest accurately

`format: "wake-inspection@1"` and `version: 1` identify the small schema. Resource
entries declare IDs, content types, relative URLs, canonical public URLs and byte
hashes. Relative URLs resolve from the manifest directory and retain the GitHub
Pages project prefix. Claims name their supporting resource IDs and their kind:
architecture, demonstrated fixture, hypothesis or limitation.

The resource index covers the eight content files; the manifest does not hash
itself. `project` identifies WAKE✳︎. Every indexed resource has a SHA256 and byte
count over the exact delivered UTF-8 bytes. These hashes detect disagreement
with this manifest, not authenticity if both a resource and manifest are replaced.

`generated_at` dates the inspection artifact; `uploaded_at: null` does not assert
deployment. Snapshot metadata describes dated public presentation, including its
head and available node origins; it is not another authoritative record. Unknown
executing source revision remains null. A fresh checkout's HEAD cannot establish
which source produced an already running worker's export. The fixture's source
identity and hashes describe its separate reproducible execution.

The manifest does not embed a research archive. Selected public record links point
to exact reader shards; the recorded export head identifies their generation.
Those records contain claims and provenance, not a guarantee of scientific truth.

## Maintain and validate the public export

Maintain prose in `wake/assets/inspection/` and generation in `wake/inspection.py`.
The unified site exporter generates these resources after deployment metadata is
finalized. The public copier accepts only the declared inspection filenames;
private neighboring files are excluded. Package metadata includes the small
inspection asset directory. Normal node research and provider execution are
unaffected.

Regenerate `demo.json` explicitly with the fixture command when the relevant
example contract changes, retaining honest source metadata. Do not manufacture
historical receipts or describe a stale artifact as a new run. Updating the
demonstration does not modify the live research record.

Run the focused inspection tests and the existing kernel-boundary/export tests.
They verify manifest shape, resource identities and hashes, Pages-relative links,
isolation and public-copy exclusions. A byte-valid artifact is not an independent
model's evaluation. Follow `evaluate.md` for a fresh observer and retain the actual
inputs, retrieved resource hashes, reading volume, answers and review rationale.
Report internal automated checks, human review and external-model evaluation
separately; do not claim an evaluation that was not performed.
