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
  "generated_at": "2026-10-28T02:45:18.466339+00:00",
  "head": "snapshot:01965432ea0e24211ee3d25220acda9546a2f26063d06c53ed4236f8782ddbf3",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T02:45:08.287710+00:00",
      "head": "a730fc8aaf13722b778f49fe7f3ccc0bcdca23d20f3e8f8aca2f219a7df6eac2",
      "node": "100.wake",
      "snapshot_digest": "b71019bc097d8c9f9c4552ed3810c2756166241829adea128c7f9d1fc9fc8110",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T02:45:02.533632+00:00",
      "head": "9dc4f16f912f3beb8eb3b84fec82f9bca3e6c527a6b352ec5a7911d6fb1b595a",
      "node": "101.wake",
      "snapshot_digest": "5e05304fe72dcd8ed8b62b3314b1fee8a3b78161607108ebc0efacd1a6ca0f01",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T02:45:06.121890+00:00",
      "head": "26622f87288126da67599a88560e78e670a378675256156f8974a2fd14b1be77",
      "node": "102.wake",
      "snapshot_digest": "b30c9b964f6db06c74e360422be4f591178c449354ba173d1a0f3246230f3619",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T02:45:16.755270+00:00",
      "head": "b70fa89237132aad1d5c9160162a404846abce019dfedf4598f5cd4dc5caf0e8",
      "node": "103.wake",
      "snapshot_digest": "8aa338d069269cd2daccf7fd48731aa68f01429442d429de4260f7722aedf38d",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T02:45:18.251593+00:00",
      "head": "550af42daaf6c60d03f95fa3dcbc54b0d4992a3257069a35981d190078d503f3",
      "node": "200.wake",
      "snapshot_digest": "c78e9f6f0a4cb5d0b3925365fdac8e7c8b2fb17937ec3b1b076e6e1bb78350e8",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T02:45:18.466339+00:00",
      "head": "58da038ab6ca7b5ee435fdc10c77a7ce58fa34610bf936873e8b14552daea807",
      "node": "201.wake",
      "snapshot_digest": "be4c858a9ecf9d46728a89534ec0e1f3fa90a3dfa80b34d7ee486bb323c95df1",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T02:45:03.494739+00:00",
      "head": "f21be1df360cc43f4aa5dcf5f5a88e194afff4755c1c590c801b8992409ccd12",
      "node": "202.wake",
      "snapshot_digest": "a1af70b76e1ee70a86fb5b18003075fca20b7faacd2fb3155a6aaee603e11136",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T02:45:06.555841+00:00",
      "head": "e70345b5e90f8b120f536d31baba9791849cac6e9a98ac32adc6c3ae9e771b7b",
      "node": "203.wake",
      "snapshot_digest": "7782d8e988cfe15f51c0d9a5554bce1a8eecb79faf67d489605fc579f94b3f74",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T02:45:06.229625+00:00",
      "head": "d49b9057a39f64db56018c467748fa33e871406fc6fc6fb9d1d28f4e0c6f6015",
      "node": "300.wake",
      "snapshot_digest": "ecadc365108daa677a3f07e086facb9162bc74f3447b12a33cd9d77c381a08d4",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T02:45:06.749304+00:00",
      "head": "e34de9cecbca8cddd9ea6c668f91307ac4416e1f9565cb480be593f87e1390d1",
      "node": "301.wake",
      "snapshot_digest": "8026919371b231c9b9b870bfd76fcaa2f128a3b888bc122f70eaf97451f883dd",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T02:44:57.803920+00:00",
      "head": "40c5ae6c46fdf0af60ec13bf2b9bb37995535f2301fbb09d352808f85e5497d1",
      "node": "302.wake",
      "snapshot_digest": "bb283645b87b18ac9ed743fca83ab09d56c29493ffb9dea2bb4040e3e1cb237d",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T02:45:07.389366+00:00",
      "head": "69e297d8d773874b25bb69e5dfe8a4be2d2a3c51ae16a7ef9cd11b3ea81ad91a",
      "node": "303.wake",
      "snapshot_digest": "2becc9accc4360f93006111d341158dbfc60322a0059a11076013a327e6b02ec",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d63343962373563333561303634363665.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66656339343964626264383334663733.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
