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
  "generated_at": "2026-10-28T03:17:38.157869+00:00",
  "head": "snapshot:b3d22c6b233af5a6602947523fe8d68a78f2d8f05addc13e4b19357bca790173",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T03:17:27.081509+00:00",
      "head": "d779142aa926927076744d800e923d2ee37311c8545ddc11f30ead280c3104af",
      "node": "100.wake",
      "snapshot_digest": "b4a17bc54378bab93525914feab47d9b38476612a61d30d081cbb7346b504600",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T03:17:31.181184+00:00",
      "head": "0cc2fc3a32e9925578b26e20763eeebdacd0180a4fd94da48c516cc978b83804",
      "node": "101.wake",
      "snapshot_digest": "605946efff113a3a1e44d1738047bd2940cf7520be9626fd995d76df73c37c61",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T03:17:29.983859+00:00",
      "head": "4b1eca957676e533be2aad1a971e8d0b5c8bdd3bf747c8469eb829de543fc1a8",
      "node": "102.wake",
      "snapshot_digest": "51e2e236ccf0927eff9f958f2a5b0a4645c7b0fc7f30c82d38bece2315af5ce8",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T03:17:37.939967+00:00",
      "head": "f1b3b30f484900d9ed443df18f4d6fb012a6d89c81e36fc008c0dc55d70f37b9",
      "node": "103.wake",
      "snapshot_digest": "a83b157ffb3b5bdaacdbc282e3021c4919460e64cec60d383e2454d9a31a8340",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T03:17:38.157869+00:00",
      "head": "8590cb581e65f39f661ef7810c10b1a6eaf140e476729571e9b12f76878fc283",
      "node": "200.wake",
      "snapshot_digest": "57d1fab0486ba595b1be4e6778d19a194536efe9408a278367f375f1b0c8c643",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T03:17:37.955769+00:00",
      "head": "d479d01718d9a1d8bc3421e42e268e97b6ddba43b0fe38240b95a441ac9711de",
      "node": "201.wake",
      "snapshot_digest": "5db804f616a2d5caf6525fc2a8c09017fba5a3a481c11b3fc250190ad6b569c2",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T03:17:30.010823+00:00",
      "head": "d9de59572c0fbd79388176d1faf99407666c9103e5aa65abde500f37be9bb365",
      "node": "202.wake",
      "snapshot_digest": "d8e721587302560487f8efc627e0c6ba9e11d526843b6ea38cc42df5754d1498",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T03:17:30.295873+00:00",
      "head": "57585039ae441d058a5e325d1c38ff59e9bdaa16298776bceee9c4278143e6c1",
      "node": "203.wake",
      "snapshot_digest": "1871a774690f34e0b2c6bec8f4a1aba0754044a036627b1a890663ffb3fce602",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T03:17:23.925571+00:00",
      "head": "897c642e136c00950564875cc99e0c23b1e266a4de9b4a5802dc600ee17af47e",
      "node": "300.wake",
      "snapshot_digest": "ebcccc3dda2bf5d7c112c81cedfac0e975f8c3954e4789614136bd78fff39a0c",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T03:17:31.611523+00:00",
      "head": "6f49392f4db3c8c19f369ee3750c6dfcaf35e5f79bd612afd62cb5cec3a4bb19",
      "node": "301.wake",
      "snapshot_digest": "33fbdb3d830d3d0a192273a597cd17dca810385c903708d749737472fabf16a4",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T03:17:24.039048+00:00",
      "head": "cfca810852946171ad411bedc67e37494a48077bfd51ca29c9594944ba2b53ca",
      "node": "302.wake",
      "snapshot_digest": "695f9b1e7220eb8593c001e9af01bb3a8a1b6f279f62da389af895b45edb8bf9",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T03:17:29.237919+00:00",
      "head": "2201a4b287e86eca6cd38636e4337880b25ab856afdefb9536c7e525031a6fd7",
      "node": "303.wake",
      "snapshot_digest": "b41164cba0aad281d32fa8091ce6abeda05bb6b552804a8f88553e3adf9596d7",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d36366535336636383430643034383432.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d39326265633739653763383234373466.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
