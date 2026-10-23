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
  "generated_at": "2026-10-23T02:12:15.133375+00:00",
  "head": "snapshot:6bed8d7d73f5e2b976ba2bea26b9c869aefd0407a2528b963ab4a39e28de7d89",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T02:03:44.469342+00:00",
      "head": "c4c05b356342c44a31fb0290c515301146b7998aa86ee081e6d5c57f93e74bca",
      "node": "100.wake",
      "snapshot_digest": "0e72e97e07d730087ce6a6af2316e4a20ed1393e5aaaa147b8725e77ac5add3d",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T02:07:02.857371+00:00",
      "head": "4af38e3643b9b0e7619be1df922a3572bcf26354cade0f9f69f42310f6eeca9a",
      "node": "101.wake",
      "snapshot_digest": "5519bfdd6bc6692417d77de731502a799c5793c999e1fd7f57ba3095891623e5",
      "version": 15
    },
    "102.wake": {
      "generated": "2026-10-23T02:11:27.507334+00:00",
      "head": "5365fba7cea385f8435dfbfeb75da3f00347d3f850860a793315b66d15a4d76f",
      "node": "102.wake",
      "snapshot_digest": "ebbd3e43c13cde997b13af787f5ee12dd16b9b41f9e45fbe6be6a86cc7482ded",
      "version": 14
    },
    "103.wake": {
      "generated": "2026-10-23T02:08:52.868875+00:00",
      "head": "ba5c787c93c71bde966e28e6b489a8c1ebaad22cd6e4e9098739330ecf577355",
      "node": "103.wake",
      "snapshot_digest": "0c32ae58bd277b19df06ade6b9d3773fd47f3a1babf1b3d7d0234786077fecb1",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-10-23T01:56:18.074069+00:00",
      "head": "8eb2737d4dee4cfa4b5908d37b79df26aa2984d0143dfd812d91602a7a64c13b",
      "node": "200.wake",
      "snapshot_digest": "2527e74f49e1a8f62a27b5a73471d32d6e09699ab4769cbcc0474fc9531c2b40",
      "version": 7
    },
    "201.wake": {
      "generated": "2026-10-23T02:04:17.724563+00:00",
      "head": "ef8a1ac5a2d47cc50a6b31a9ef551d9f8c776b1c8627296f43e1b315b20f63e7",
      "node": "201.wake",
      "snapshot_digest": "c6bb1c1566586b002dc4f4065578efbc06323cc2114cb37b41c763a523fcd2a7",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T02:06:39.075423+00:00",
      "head": "08111c2f964ce7a67e7f790a5e3d4158cb229210aca61e9574402d43a190c9f4",
      "node": "202.wake",
      "snapshot_digest": "991076d84872ff97c99e31f2ca9d17b235fbb2d55cae3fe5d4e942407b4efd74",
      "version": 15
    },
    "203.wake": {
      "generated": "2026-10-23T02:12:15.133375+00:00",
      "head": "5b4c018ad3c48949295fa002e8a3b64311b2f49d1bfada485b0ca53c4ae1f932",
      "node": "203.wake",
      "snapshot_digest": "37d5790717d7e1a5461d5e56ec29074733ab5c7669161ca63abeec193f50d4df",
      "version": 8
    },
    "300.wake": {
      "generated": "2026-10-23T02:05:18.012564+00:00",
      "head": "5a4ecdd3363a6300bc021a68a4fa230a18ca0cf5f7011f8b38bb00d63f247330",
      "node": "300.wake",
      "snapshot_digest": "4335946a93e0746da9a57e062062054951e73a287daa5719d48209c5a4d36cdd",
      "version": 6
    },
    "301.wake": {
      "generated": "2026-10-23T01:57:44.062818+00:00",
      "head": "0f530a4cda9443a886c03de7217c6aa4ea93efbd58d3d289c17b215ca78564d9",
      "node": "301.wake",
      "snapshot_digest": "c7a0d9c8b47377d24b2b94b2a9866d250fa5c26254acc9ce7723f9a3de6e63ca",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-23T02:10:31.749193+00:00",
      "head": "771d882bcacc3d212f18caf1972316cff0237df7465ba282e2f5b26ab4970d89",
      "node": "302.wake",
      "snapshot_digest": "d78d1b858219d2d49bb558e0b2e6d9cc6b30165274665d44e10dd45b458b1651",
      "version": 8
    },
    "303.wake": {
      "generated": "2026-10-23T02:05:40.099971+00:00",
      "head": "b993ce708306c5f725311a30c67851021eb8de3654d282dd389ee6c11aca7d40",
      "node": "303.wake",
      "snapshot_digest": "6f8e8a0a0cc99aa76cb409e22358fe9fc104f139f531b9957a7d1bc30ba3c306",
      "version": 19
    }
  },
  "version": 128,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31646337373337653434343534656161.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66396366396235633835333634333630.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
