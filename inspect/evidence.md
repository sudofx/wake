# Evidence you can inspect and reproduce

[demo.json](demo.json) is a generated, synthetic task-list demonstration. It is
software evidence about recorded decisions and replay, not a scientific result,
a live research record or an assessment from an external model.

Examine its actual receipt identifiers, revisions, reasons, hashes and final state.
Do not infer missing fields. The intended sequence is:

The isolated record begins at revision 0 with an empty task list. Each event
contains the fixture proposal, its base revision, the receipt identity, decision
and reasons. For accepted operations, `proposal.operations[].value.next_state`
shows the resulting task state; the rejected completion leaves that state alone.
`result.state` is the replayed final state. These are actual recorded proposals
and decisions from the supplied run, with no model call.

| Request | Decision | Application revision afterward |
| --- | --- | --- |
| Add the example task | accepted | 1 |
| Complete a nonexistent task | rejected: task does not exist | 1 |
| Complete the example task | accepted | 2 |

All three decisions are recorded. Only the two accepted transitions advance the
application revision. The generator verifies replay of the record chain and
agreement with reconstructed application state. A successful replay establishes
consistency under the selected rules; it does not establish that a task was
performed outside the example or that any scientific claim is true.

## Reproduce from source

Use an inspected checkout and Python 3.11 or later. From its repository root:

```sh
python3 -S -m examples.task_list.inspection --output /tmp/wake-inspection-demo.json
python3 -m unittest tests.test_kernel_boundary -v
```

The generator uses a disposable example record, not an operator's research
installation. `-S` disables Python site-package initialization, helping demonstrate
that this example needs only the repository kernel and standard library. No model,
credentials or network is required. Independently read the output and compare the
semantic decisions, revisions and replay result. Generated IDs or times may vary;
do not require identical bytes unless the generator's documented contract says so.

These links point to **moving source on master**:

- Task-list rules: https://raw.githubusercontent.com/sudofx/wake/master/examples/task_list/app.py
- Inspection generator: https://raw.githubusercontent.com/sudofx/wake/master/examples/task_list/inspection.py
- Kernel boundary tests: https://raw.githubusercontent.com/sudofx/wake/master/tests/test_kernel_boundary.py
- Receipt implementation: https://raw.githubusercontent.com/sudofx/wake/master/wake/kernel/receipts.py
- Replay implementation: https://raw.githubusercontent.com/sudofx/wake/master/wake/kernel/record.py

[manifest.json](manifest.json) describes the delivered bundle. Check any recorded
file digests against downloaded bytes. A digest can detect a difference relative
to that manifest; a manifest delivered beside its files is not independent proof
of authorship or protection against replacing both. Missing provenance, failed
reproduction or unavailable sources should remain explicit findings.


## Captured public presentation

This is dated exported presentation, not a live status query or a second authority. Generation time does not establish upload or serving time. The executing source revision is unknown.

```json
{
  "authoritative": false,
  "generated_at": "2026-10-27T21:37:04.645605+00:00",
  "head": "snapshot:9c9ab23c4c7659db93f3966f86f34b2d95171c084852657d568d051e640fa723",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T21:36:59.914128+00:00",
      "head": "bbd4c04ee8494d97c80f757e02c7dce0e3fa9b65d29cfc8a340022411a584bb1",
      "node": "100.wake",
      "snapshot_digest": "ed38d4e1f92149bd4d67c1cfb14512097ede689e091929e848bf587016fc7e43",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T21:36:43.152062+00:00",
      "head": "c0bbbb12d2bcd6f75feb7d9abe0509b58e0791c2a60a4ab7b4d5579d3af72f2e",
      "node": "101.wake",
      "snapshot_digest": "3c64613d633f67e1212d034a31214c4c20db79e0f7a64a60801add161ee1fa1d",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T21:36:44.923185+00:00",
      "head": "c1c688782c16f3399431b8b358cadf48c3c5e5c11ec338f7a51ab3db8bac78f9",
      "node": "102.wake",
      "snapshot_digest": "684653f2b2022ce5362f19dca375dba9777ca414f07c927c87086a560110b7ac",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T21:37:04.645605+00:00",
      "head": "227fa801489a73b4406e6d12574b13a3b7cd2a6c2ffae882db782e9c27df3f7b",
      "node": "103.wake",
      "snapshot_digest": "23016b4621b22ea0254e456b8c0aee5f03fd16c09cb302855656e1ea13bb73d5",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T21:28:42.774130+00:00",
      "head": "4061c93148590e450098045296d352893a55e4359e50a666fd8afa81eb246542",
      "node": "200.wake",
      "snapshot_digest": "5d6da1f335fdbc27b1ba9c305e1176add7b743edca708a31c95f2fa850f218d7",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T21:28:43.649440+00:00",
      "head": "9126a606e13a15a7ef0a927158e9c622f2e83509686259bcecee6b1159502e3e",
      "node": "201.wake",
      "snapshot_digest": "9f5b13b7c9f112a080bfcad20780d6fd31be184423a142ceed456c449a7000bb",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T21:36:50.006582+00:00",
      "head": "1c8bc059b52051b174cbc27737e6da590028a79a6562bbe0c04ae4f992b8a14c",
      "node": "202.wake",
      "snapshot_digest": "f7ceaffbebd52cf99518fdd5fb96a1bcdbade0d562495daf33e4f58bfc93c686",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T21:36:43.168865+00:00",
      "head": "7be6fa20ce10cb64975e8c6ee94e71c80b6cd76e36eb4d6b9649acad24402b7b",
      "node": "203.wake",
      "snapshot_digest": "a0d8be1cfdd159f33ac786fb946ecc2499530483a26b833c7a87ce808d523e5b",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T21:36:43.509764+00:00",
      "head": "ff7b93c302230ebd0cf97a9535f6f9f63293c99512028ea38a4348ea9bf22e2c",
      "node": "300.wake",
      "snapshot_digest": "ae333214d677dbaa4a3e4a2641bf14195a5b7837c41f265947561538115c7d16",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T21:36:41.321589+00:00",
      "head": "aae393be947d7ba9407fb62fa74d15128a875125108af8c2ff387a36fae8e048",
      "node": "301.wake",
      "snapshot_digest": "23faabe0a2448640e85c2b768010b40ea1b74a93fb593b5204d44ae60417c01d",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T21:36:39.907492+00:00",
      "head": "088f17469025f399a70dc5b191ce33a6556e6bdcbbca83e57145a24b4d355d86",
      "node": "302.wake",
      "snapshot_digest": "4a7242a9321c72b558f78acd44be4436533affb45a6968bc3a5f98a007036c41",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T21:36:46.995152+00:00",
      "head": "27729c60c6b51364d5b5a48b1d0e9e4dadd4e93ad756fb884e2cd17eeda4fda3",
      "node": "303.wake",
      "snapshot_digest": "d4712fd39023744f6f81148e0c5872549a592c23d0e40bd2216cb835a6bd9d29",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d38653034626463303861633634353566.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66666534316234393537313434353063.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
