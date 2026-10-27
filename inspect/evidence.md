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
  "generated_at": "2026-10-27T12:54:53.934949+00:00",
  "head": "snapshot:2780ae0f9e28cb04447ce99e5c01c07e6a06e8563c32a969489d97f311f354e1",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T12:54:16.972178+00:00",
      "head": "68418a03b994d523b32767a95b71a3d0baa766ddc931f7262bfcbe7447e064c9",
      "node": "100.wake",
      "snapshot_digest": "6718d10512847aaceec146b3d244d569a71ee3802afa9dfc51d27c929e29270b",
      "version": 2
    },
    "101.wake": {
      "generated": "2026-10-27T12:53:59.288641+00:00",
      "head": "0c102640979312330aa66dedfbdcdae9632023100ad9b0a79416f8243bec6f26",
      "node": "101.wake",
      "snapshot_digest": "199176b9ec87f31e814f0182a92a79857ba5c988c07f64f59942d7383418ecf8",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-10-27T12:54:53.934949+00:00",
      "head": "474f1dcf0469207659c96cf8b97c88ed23362e89d2edfc298778ad766d4ce14d",
      "node": "102.wake",
      "snapshot_digest": "fe7cecf7bddddbea066e58e1abdcb2e7480ee70c0cc4fe8d3a099d319c760fd2",
      "version": 2
    },
    "103.wake": {
      "generated": "2026-10-27T12:54:05.643385+00:00",
      "head": "c853c8a6bf464badbac747ec9acefa076cb14b2032f11be875865fe004916c1e",
      "node": "103.wake",
      "snapshot_digest": "8ab27ab3d3b5e465ce3401690b4172ee7601ffcc41c3828794a5809ad4fefc1e",
      "version": 7
    },
    "200.wake": {
      "generated": "2026-10-27T12:54:16.811949+00:00",
      "head": "0ec730fc65710b878c878c954dc79dde3ab83c4dae148e31a7618aa357085e3e",
      "node": "200.wake",
      "snapshot_digest": "4cdf1347cbbae020510a1ba973d21a892aab0e89804e1d77a1f0aa48924429a6",
      "version": 2
    },
    "201.wake": {
      "generated": "2026-10-27T12:54:06.899243+00:00",
      "head": "e843e19bd4eb634b3ea847d732cf1e54a96261220c1095adb754610c8134f168",
      "node": "201.wake",
      "snapshot_digest": "449beea3592c7a94cd506de2ba9c76d5c103a875ac1dca0406b9ab96c0154c1b",
      "version": 7
    },
    "202.wake": {
      "generated": "2026-10-27T12:54:02.091639+00:00",
      "head": "739e452a6d31c28fe70647bef234c5b960ce310897326612d2a9d1d2327f73c6",
      "node": "202.wake",
      "snapshot_digest": "7385cff3d1417b36af6cd8f7260a35fa8dc8e4960e0231db66042801d3b788cf",
      "version": 6
    },
    "203.wake": {
      "generated": "2026-10-27T12:54:04.913361+00:00",
      "head": "1f73bafbd8326597235a05580fe600cbc6a3a84192f6f90edf2928ccb01f0346",
      "node": "203.wake",
      "snapshot_digest": "f9d8c42ea85c452f21e50ba19b268e38d3458c7104d6f20217d3c2ddb46c66d2",
      "version": 6
    },
    "300.wake": {
      "generated": "2026-10-27T12:54:17.704218+00:00",
      "head": "a6150d21f2ff508f9444e9450f671a0f7011b2929f1be9acb3b55267c968de9d",
      "node": "300.wake",
      "snapshot_digest": "1ef4865accfc1f4d546f16a3c2bdeb5807afbdd425bbd692352e7fb4c9180a8c",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-10-27T12:54:39.385039+00:00",
      "head": "90581dd4e417a7bb78e41ab501a34eb1596ca459b74c7c76d8b70335304aa548",
      "node": "301.wake",
      "snapshot_digest": "b86a88bb43fcc0d10eb7bc9e6a6dfc5e4365ddfcbb89b687919c753f7e114779",
      "version": 3
    },
    "302.wake": {
      "generated": "2026-10-27T12:54:03.376974+00:00",
      "head": "0f72cc35bbe3a63802143c3b1829c5b86ffcd81b1feee3a848361bdcec01fdea",
      "node": "302.wake",
      "snapshot_digest": "2af6bf9caaf2f601b3dc1c701ca28be1b65ec40c4284b1b4b72cb7c52121db59",
      "version": 4
    },
    "303.wake": {
      "generated": "2026-10-27T12:54:43.248799+00:00",
      "head": "624e29a32fc1ae03954051c0bc82466861fd46e46846c62d48d11a20e27f2552",
      "node": "303.wake",
      "snapshot_digest": "edbd9a4c0ccdaf25fc64480def1c995b9fc8f2b4bc76c13a90c147e8c5c4e892",
      "version": 6
    }
  },
  "version": 52,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d643061343630363333393735343630/64.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d666132333432386237323333346237/62.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d636f6d706c65786974792d7072/6f762d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
