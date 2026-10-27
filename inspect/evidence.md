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
  "generated_at": "2026-10-27T16:03:36.205696+00:00",
  "head": "snapshot:9bc994531691a1eaebc9e2b126527622ace3b9c7f11686dfbb2bebebda65e00b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T16:03:22.440944+00:00",
      "head": "e4693f9f58a65815d69ca6e8c7eee4a2394d0a0e2ceadd754f549ef9605aa09f",
      "node": "100.wake",
      "snapshot_digest": "72050efc32a19a8951d041cf9622021b38b4eaba1ba6c8c027920e13f03ede98",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T16:03:15.357331+00:00",
      "head": "ffd9b6471fdb1667f3334649f1e98cf6361d1cc1fc3739267025f37a8246a5f9",
      "node": "101.wake",
      "snapshot_digest": "7507abe42025ae4ec0c6cfb73ee6c4434973dd8e5e3f9c7eab5d21810e3c647b",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T16:03:17.421754+00:00",
      "head": "935aeaa21599a5ba80102761ec99dce9e1c75f004289c2bd6d796c636a019ccb",
      "node": "102.wake",
      "snapshot_digest": "2c95feafc4c7595be3bf05457c86045911cf79402cb81d96827c57797183100e",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T16:03:36.131620+00:00",
      "head": "990bb7c94a4538e3d13087343a74eb83b15fec676281cacfb181c5c61a487f30",
      "node": "103.wake",
      "snapshot_digest": "e5d2aa8652df9342a19d12c72d57f229bcbf900f458ffe624a17bf647a9f5e58",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T16:03:30.128985+00:00",
      "head": "544ad4b0ae3491787754af4f4935ec226c48304e9b2b871cd2958083912c4e37",
      "node": "200.wake",
      "snapshot_digest": "61e1b3f15d9d9d8d8ab060be8add410bb6916260edfcc5c276bb0b54d59b4535",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T16:03:36.205696+00:00",
      "head": "6e0615399267e3df7139eb33dd65568f19c3395f7504b4f1f7980660f2984137",
      "node": "201.wake",
      "snapshot_digest": "d41c2488aa14eb0591c27dba57813fd0f6fedb1fcf166a8a7c2ef6fbcf7d61b5",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T16:03:16.259452+00:00",
      "head": "503fc76d42b17b221d964ebe1c4220789b79d771d0843ae31ee1deb61dd236b4",
      "node": "202.wake",
      "snapshot_digest": "25e5626816ef0e60efa869519545f76f8cbece4d33b3c655047a240d0f3ccb1d",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T16:03:12.548066+00:00",
      "head": "d73b6dbde5e9a0c16dd900438f29327a9cbce1fe496b81abc5a2763975fd23ac",
      "node": "203.wake",
      "snapshot_digest": "f56a1a43c27b0c8e396894e7f264378903f4cabaf68e442b832db1b7becb0d52",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T16:03:06.555236+00:00",
      "head": "c8a3cdbd6060dcbae9ba046e11b50a549443119c9838d1feca61abc606671dd4",
      "node": "300.wake",
      "snapshot_digest": "447a7c703c6b08773089b42d3cf8c0741a776b6a0e63721084495a61ed323a41",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T16:03:13.572410+00:00",
      "head": "a76d608542618289ab47105bad2a283325a6e5026a82b066c74a211fda17bf4e",
      "node": "301.wake",
      "snapshot_digest": "1a03588d6c9102b90cc42494da516f5733d131e199e3903cc00c28ce7205c7a1",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T16:03:09.516747+00:00",
      "head": "80bc30c99ee26e0499c6e181511b36afe3212a9f6ffe7f320fd26458cbb42b46",
      "node": "302.wake",
      "snapshot_digest": "6b7625664f42aed9a65c14da83829862695234e4083f4512922a17be7f6cf6f7",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T16:03:21.761430+00:00",
      "head": "fe44643c2c4b469072be03c18bd6717502c9e9a36fac8a259d9a5ae32da0a127",
      "node": "303.wake",
      "snapshot_digest": "19f1be0d1a924fb8e52ec98a3ec99b8d79cdcf898d9bfce56868c2e183b6ccbd",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d61346236386363316464326534613864.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d34313439656361313365636534393438.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
