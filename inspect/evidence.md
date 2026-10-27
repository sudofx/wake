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
  "generated_at": "2026-10-27T17:01:12.291094+00:00",
  "head": "snapshot:b46026609fc8a7339088f198319eaa035ef660cee0c49be87a5ab723d3ab2c5e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T17:00:52.635464+00:00",
      "head": "46380da5e64ecec7870cbc0fe9c1bd64d1805697eb74807df6d22b874e9cd70b",
      "node": "100.wake",
      "snapshot_digest": "eb44ca3d03ee551ddb638c8670f245d637a8b95db02f1ec0c16fa18777f871c3",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T17:00:52.657137+00:00",
      "head": "c6dd794fa5a4ed3110305b7628e8821c94f02ef14ad9e470dcd2876ae9cbcc5f",
      "node": "101.wake",
      "snapshot_digest": "26ba978dece06c112419bcf8e8ba28e20199279c52e547213f89d1010bcf9c4b",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T17:00:52.831740+00:00",
      "head": "c6bb4dea5c082b3196f196bddababb0ea791c0bf71330010879e2546f3b0727b",
      "node": "102.wake",
      "snapshot_digest": "da02a7a6c3ca28b1be1275c9300c6333ce0e974b1b9a76722507052a66938184",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T17:01:09.723901+00:00",
      "head": "ac893bb55308566877b97b09fe998bf1f2f8baaa4f37d92d2538f444eb35ce38",
      "node": "103.wake",
      "snapshot_digest": "d66aa784981c9f7fd33724e3e6f46c65c44ce7ae111ef82713ff8cb2175b14a1",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T17:01:10.803820+00:00",
      "head": "e72ac67c7159becbecc8a1b210885e62263d9fb62c6f0313f388ed640dc791a2",
      "node": "200.wake",
      "snapshot_digest": "83f88dca8bc470ad0930edabbf3b935d9127f9bf870d9552cccacd133e3b83e4",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T17:01:12.291094+00:00",
      "head": "8084a56e2c0e0f9b10935c39cfa0a6f1df7eaaf22e6a825a17c961d910171407",
      "node": "201.wake",
      "snapshot_digest": "ee33bdc9a89de700e04a63326a1127deeac42e7e7f0742c76d34e2642c3abd53",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T17:00:51.961665+00:00",
      "head": "ba38e9d14acdd0537bb80b7c57eb674b39b3b3146d5dbe10ed281a11f242a998",
      "node": "202.wake",
      "snapshot_digest": "b38ea3cc149bdd9276737c81bff43ffa13831ee068b41961292c93691bb7f44c",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T17:00:52.553612+00:00",
      "head": "2b8786b9bc206bb4f7eb6ba0bb2f4b9ccef62458c384935494f4cd68cdb7f2d6",
      "node": "203.wake",
      "snapshot_digest": "1544ccec4796b0e778fa4ab37b984221e764df0779db5b22a3437a1f12d9d63a",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T17:00:45.654411+00:00",
      "head": "e1cbaf2726cc54a4c25f638dd8251aba811ff038a7e4697289a5d66e34b8451c",
      "node": "300.wake",
      "snapshot_digest": "6d21098a6a609dee66a6b89bba554887c1cd67073aa37c683c7c6dae08174bdb",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T17:00:50.797160+00:00",
      "head": "df4ffe7257bdc2747b8e9293fdc3dc7ff705c2a743a5b7779a60e37ac17ed8d8",
      "node": "301.wake",
      "snapshot_digest": "3178bae3e3c7ac5d9ef6db01773f878371b14c02b5d9efb72dec3701ef67d1b5",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T17:00:45.883044+00:00",
      "head": "fee37f626449d9b41b5b5a475d0bf17a398c24c4c8261267f3da6d42c9d98017",
      "node": "302.wake",
      "snapshot_digest": "41d189cb77b180fd18043f777aa043c6554d75c2a4a93f82491741aed715086b",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T17:00:49.991869+00:00",
      "head": "4a2d1db1fc927a6941ca615bf10c54daea81f59b8634c609cb10574eff85a212",
      "node": "303.wake",
      "snapshot_digest": "a589807db64e3ac067a2f8107b19006d83f0d052df55f160c0d14fe77ab15bb8",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32346231393834663437316334316330.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d37663263383637653939333334356338.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
