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
  "generated_at": "2026-10-27T17:42:08.392144+00:00",
  "head": "snapshot:8813f262ad7cd4bfa7d716c12b645f94baea8910f867e1024efa0f82ea5fc522",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T17:42:02.342522+00:00",
      "head": "52391aad6643778d809421fe3856d949d0e968e74271b1df94f0fa215f381052",
      "node": "100.wake",
      "snapshot_digest": "c15bc938fcaf4729b28250d931e0e67b45da18bbec61fea4c64f64f356878894",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T17:41:49.750294+00:00",
      "head": "2dd1daba12083f701f7b4058be34d7db2f0614be2758344cd217e55bed4322b6",
      "node": "101.wake",
      "snapshot_digest": "b06a3f51397eee83f02667d73f0c30a38c732b1e1e0f931df43c6dce0110baf8",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T17:41:48.536337+00:00",
      "head": "bfd09b51ba8cb0ced4aac25a8dc2e23c4e62084a96cfbefbbce3b2c7292a656d",
      "node": "102.wake",
      "snapshot_digest": "b80ec3c8a7157264b53c520163811fa33357bcc7933696369182cc2854d51174",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T17:42:04.610260+00:00",
      "head": "6fca6c0651f000438bacd472dd554c2497efb0c00171882a953895bcb22a8ee1",
      "node": "103.wake",
      "snapshot_digest": "543ab6509abada50494f54c3a7a7c34104d566bb93ed0f524979f8d93768d5b6",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T17:42:08.392144+00:00",
      "head": "763ba34c21cb857ce7a725849923a1240b16f24ec9e4164b54631ac006bde1d4",
      "node": "200.wake",
      "snapshot_digest": "fa325fed37dced9da7e1781f096facfb41a206227f0e6caba5b8bae5ed8d16fb",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T17:42:07.838841+00:00",
      "head": "93b0aebafe071dd06c8b2c9daac020dd3e96340a05ca63b449eca7dcc659cc55",
      "node": "201.wake",
      "snapshot_digest": "bb8147496dfb7ab16251d1292df9b9f3ebf9df0fe44b166d44384e67cf1f2d44",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T17:41:46.946456+00:00",
      "head": "5e0e6db65ece36911e789eaf319c20593bc6e4d4a606b240efb3ee500797644d",
      "node": "202.wake",
      "snapshot_digest": "a331f7c201469df1b7716106ef278dd426254e78e57a8ca44a7e4b4220a6aa3b",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T17:41:45.707394+00:00",
      "head": "03fecf3dc4b4e503ae001748ccce748bc17765a74c3189b73c82c87e86776b17",
      "node": "203.wake",
      "snapshot_digest": "5ddb83b919df2d02ed7dcb7f44cd5244532ac9d398a0560116a806bf72bed05a",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T17:41:38.425828+00:00",
      "head": "f51f590dece0bbd828d6876f055a54e0807043a5da100d58218dad3e075a861e",
      "node": "300.wake",
      "snapshot_digest": "6cb99e903db10248d54ae67b8fafd66d596883e39345ecf34bab1ed06248b268",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T17:41:42.772244+00:00",
      "head": "c778708a0030b93fe54a0223a26929073a189849f94326d196e3d1204169df95",
      "node": "301.wake",
      "snapshot_digest": "0723e9d13322a833a3534e757ea76729b6fa905298a5a771e09c42a2d9b97731",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T17:41:43.745038+00:00",
      "head": "9696072b8e353659c5f6afd26a5c6d291796f75f14cb6923badc4e00becd2035",
      "node": "302.wake",
      "snapshot_digest": "944474ab0847da985db2bbdaea0969ea0c3dceba685a2943f0e37779f1a6bff4",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T17:41:49.261645+00:00",
      "head": "ff6621fda06a3094be5d0f4ff2f9e5915a2599ccfc6b9296e35e69fedf39cd1b",
      "node": "303.wake",
      "snapshot_digest": "857df591fa302264dc5a5baa566e1f663118d5c8916b2ea7b0b999fe26b7f698",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d61336631336236636131656634386139.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33373931393465363833383834376637.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
