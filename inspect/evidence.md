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
  "generated_at": "2026-10-26T04:25:35.991077+00:00",
  "head": "snapshot:2c4b0d71b44d5fd836deb5847384616be3660e00920d935b5de386a484ed811e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T04:25:35.991077+00:00",
      "head": "ff5df6d147b5e4196758176402346d850d3e5e29f73baf88c00391b65cfe83a7",
      "node": "100.wake",
      "snapshot_digest": "fe532ddbf874c0120d6d61e559841b739afff5fb597f8f737edd629f106a75e2",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T04:22:12.995383+00:00",
      "head": "84fbb1e3bb3e249e8062ef40f4cf2b9ca772af1632d7f3616d2cc1315e937420",
      "node": "101.wake",
      "snapshot_digest": "fb2f7bc65b2865cb8597a93d23189138deb8ed7a1882c25aec69743cb16b1a65",
      "version": 47
    },
    "102.wake": {
      "generated": "2026-10-26T04:13:56.461176+00:00",
      "head": "a16c2d2690fd438a5c7de191602b1142939136422386ccc5379d866c1ac67d25",
      "node": "102.wake",
      "snapshot_digest": "ca53913e22feb5cad53f261c924e14398087840705a20c0c41f40c9cb3f2512d",
      "version": 60
    },
    "103.wake": {
      "generated": "2026-10-26T04:24:37.273302+00:00",
      "head": "01837c01246c0785eddcecf906f965df75d914514103aff3bbacd16d83d4fd38",
      "node": "103.wake",
      "snapshot_digest": "1cd93222054384d6b8fa44e49a7a86d8d003e8b4370c4d821a38b59c104352e4",
      "version": 42
    },
    "200.wake": {
      "generated": "2026-10-26T04:18:58.265744+00:00",
      "head": "d3106858d2bb95f18be040dd7e145302ef8520a41f503e32f81f64c1f524231c",
      "node": "200.wake",
      "snapshot_digest": "87e0aea8779e5a01d57b9cdf80489221b561b07ea8aa5ec5a9cf6460e0303aa4",
      "version": 37
    },
    "201.wake": {
      "generated": "2026-10-26T04:22:50.773875+00:00",
      "head": "be2873d07a9bb33f57362eb7951db2278d69fff6e00aca04c7cb04b448d15078",
      "node": "201.wake",
      "snapshot_digest": "35f142d20ed0effa8b3bb69213663a7a18d49eff7d03ac53a88b135210cd28c4",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T04:21:55.926690+00:00",
      "head": "b8efbf4b9b7620d274872913a365db21ab5ab8bce315ca5ec5297c5ff26d2ffc",
      "node": "202.wake",
      "snapshot_digest": "fb3cd2e5a33e9b0bac9b4c8f3055e94d410975f41ff09c1ede43424f6aedde94",
      "version": 56
    },
    "203.wake": {
      "generated": "2026-10-26T04:14:27.055871+00:00",
      "head": "7a6da955a6352943cb36568b27c64c3af66a36fac9e55bf26343696f8a160b23",
      "node": "203.wake",
      "snapshot_digest": "01092d55c6661bd2c731e352eecc951a655b9ddc9ac4f76223e00e267ed2ead7",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T04:21:40.153314+00:00",
      "head": "0f59b052362ed5b39770e63e4c6300d85e886d64fc4c89bb2f0d2b58e608a10b",
      "node": "300.wake",
      "snapshot_digest": "7bdd7528164d30ddb94011b814e771571b805602686776e2b86799a789740512",
      "version": 37
    },
    "301.wake": {
      "generated": "2026-10-26T04:15:40.312213+00:00",
      "head": "aa13dbc1df77aa6b2d33ad7580f41ea536ef3c261487aea3f77a8aca3d0cd6ca",
      "node": "301.wake",
      "snapshot_digest": "299ad29ebf9f9256b8b4dcc12096a102aab0bf6945fd6aa76b49f079cebf06c2",
      "version": 59
    },
    "302.wake": {
      "generated": "2026-10-26T04:17:47.363164+00:00",
      "head": "bf2982c5223b1a5689549ea2450820fdda771bb5f2e492d88fa3437f81cb4f16",
      "node": "302.wake",
      "snapshot_digest": "afa9f6d5bf405535b883a57c87b3c7453572b086c97cbcc7fb4658240d23f362",
      "version": 43
    },
    "303.wake": {
      "generated": "2026-10-26T04:21:05.598289+00:00",
      "head": "2aaf400a2927fe5299386b98f42966b9a178809528e246afd74de7a70e32ad5b",
      "node": "303.wake",
      "snapshot_digest": "4cb337ae83e71aefa7f09d415e947346026ea904517fd310220c087c548d1815",
      "version": 52
    }
  },
  "version": 537,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a722d64336163323534393332363534383466.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d39333439636262316561663434626264.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e6f7465626f6f6b2d726561736f6e696e672d6c696d/6974732d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
