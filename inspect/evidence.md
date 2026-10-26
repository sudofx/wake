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
  "generated_at": "2026-10-26T13:24:43.463609+00:00",
  "head": "snapshot:25e687210e46046b23e6738a7f31cb572a28f4d6098928364b021e678d9fe1e8",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T13:06:15.407930+00:00",
      "head": "2d8ccbc091d6d9ea899a6d72aedf70b0fb21e44fc0234c806c90c9a09baad85c",
      "node": "100.wake",
      "snapshot_digest": "c7600848abc12fea0667c1cd0a97eaa1fc2ae1c68f3ce87b5aa5bb6acf08d3d8",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T13:21:28.826356+00:00",
      "head": "8d3fc092b1db416f4c70f77403191cfeea3afcd2850508262d435b54f9b4445e",
      "node": "101.wake",
      "snapshot_digest": "6404780447de0d5d5eeb01f39f1d7bf200709622238e77345f4400a6393cf469",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T13:11:31.731960+00:00",
      "head": "81dac2d14eebf07fad56d67e3fa5b5a1e02bcf0126e0e8f2dd90977e38647d9b",
      "node": "102.wake",
      "snapshot_digest": "3deadbadbfc295297c1550c3bfc9e93c6c4dee7fbf60f0d755ad44db44f7a697",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T13:23:13.354321+00:00",
      "head": "b428a210d2f303f52964433e1b2993a7cc7f0d717aa1ca02e3c526e4a3e26216",
      "node": "103.wake",
      "snapshot_digest": "9bad2eb097d88ad982138d28d11b099d85e51416a5ca1d27ecbfe9f87dddfe7d",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T12:59:09.415217+00:00",
      "head": "508bd280a9b0a5f41d2ce2e32200ba0d368bac7bbd9942cc172000def8b5202e",
      "node": "200.wake",
      "snapshot_digest": "9bbae15a1c69633cbf8c3b683c05bdd826d120efc7c5307e0c954ca4e0b42b7a",
      "version": 42
    },
    "201.wake": {
      "generated": "2026-10-26T13:08:38.708583+00:00",
      "head": "c94f85c184d2256fdafd2284673c5cc68a95d92ed8b6ea69041a48702060f932",
      "node": "201.wake",
      "snapshot_digest": "1609e7db1d602c5f678e8884fc021ae9e0503fec210f6a1ada17a952b07f4c15",
      "version": 44
    },
    "202.wake": {
      "generated": "2026-10-26T13:16:35.445594+00:00",
      "head": "31a4f521863fc9e04defb24ab4d88dcd599bc70ae0476e9722a17644bcb4a582",
      "node": "202.wake",
      "snapshot_digest": "7bce3d5be856f2abf269115ba30914d2ea3250da27271640b915d5fa49388e67",
      "version": 58
    },
    "203.wake": {
      "generated": "2026-10-26T13:05:20.488637+00:00",
      "head": "8772f80540336902159f81effb6303dde44382e9d7f0f3a526a754ab7c61cc6b",
      "node": "203.wake",
      "snapshot_digest": "9c7dad284329d1134080cd9051799c7fa2418a069b40564a4e2c04f5f3286e90",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T13:00:35.788124+00:00",
      "head": "9c6516b8f3802cd6e5f010b50421a24b37bd9fd25e64ba84a1696dc9597dac21",
      "node": "300.wake",
      "snapshot_digest": "fbd93ba302e467ccd717fe21b04fc88049d0ff1859dfb18391dc1949539cc8f6",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T13:24:43.463609+00:00",
      "head": "ebbdaaf4f6373c54f3970771bedce3b26c07f1a1960be8a67a6c036c71bc882f",
      "node": "301.wake",
      "snapshot_digest": "7bb465a1c069f8769a36869fedb68ca6a7fef5149da8e51d9c847a1ab8ad16e4",
      "version": 64
    },
    "302.wake": {
      "generated": "2026-10-26T13:22:12.262108+00:00",
      "head": "54c679ecc4eaf2602ad0d01d978729765daa62f2e81b3f4528e2881db157481e",
      "node": "302.wake",
      "snapshot_digest": "faada0f193572acfc26dc28eb8cae92f687b3510cc590687976b52790d6587c2",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T13:09:07.502090+00:00",
      "head": "f01fcb64e63556aa07d4ba03d55984630422c4a6fd9098e55716d449bc3e190a",
      "node": "303.wake",
      "snapshot_digest": "c21fb24786cd01b94cdd41504f88b8abb1f36b69fc8c890601fe938f9acdf298",
      "version": 56
    }
  },
  "version": 571,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d63623364373363636662636434363163.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d62306639326530343639323734366564.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
