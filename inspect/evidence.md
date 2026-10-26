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
  "generated_at": "2026-10-26T08:39:30.889425+00:00",
  "head": "snapshot:8d5dfdd2b09764ff97dcdc71fb30ea8fb5a54c4d1e9ec2e81b7a377e5c7fdf26",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T08:39:30.889425+00:00",
      "head": "c54eb2903ef3a4057669d866e262a504e0d6455ddd8d0675f1db2e023068d1a1",
      "node": "100.wake",
      "snapshot_digest": "61203c971e8dc78f0810edf66bc66dbb8e5aa125b28e25436d6ca40f8e9c84dd",
      "version": 30
    },
    "101.wake": {
      "generated": "2026-10-26T08:10:25.885721+00:00",
      "head": "bacfac2564a56219aece9f5858b2349991dd0574d18acd93bc47d0fa259f638b",
      "node": "101.wake",
      "snapshot_digest": "d1a74e04784b3390b5c47cb1b1a87ac6cb346ef8dcd8b9b204f9b575f43b9927",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T08:29:04.502526+00:00",
      "head": "6295412f23e003ebec36ec40c54598c995e3ff144b44b7863aa9a20be07c3241",
      "node": "102.wake",
      "snapshot_digest": "ee1a7febeb200a8e70a7d81cb76ef1286c64be831972005d5b45390a4023e453",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T08:07:02.620331+00:00",
      "head": "51135eaf8ce78efb14a9d4e5f7ea9a14cb8e8b21931f905c735bfe8d362e9eef",
      "node": "103.wake",
      "snapshot_digest": "ed8ba67af014c2d8f5acb8282e21823be0d342868af7f29dd89fe8bc4e7197fd",
      "version": 43
    },
    "200.wake": {
      "generated": "2026-10-26T08:36:03.574640+00:00",
      "head": "0c748420876b937ca33e5211227fd7a1d76b86aad023d6a732737ffa77647600",
      "node": "200.wake",
      "snapshot_digest": "57f0709a1b1a8612483f962fb0fedc3019bcc4ea740ca52c5c3a6ca44a1f694e",
      "version": 40
    },
    "201.wake": {
      "generated": "2026-10-26T08:08:36.444229+00:00",
      "head": "265cc8f68b8a3a7f1e8da59fcec1729895dfb0bb9a517a04074fee212001fcc3",
      "node": "201.wake",
      "snapshot_digest": "471df5f2521d7758ab5a1ca6ecbf14a4ac95f760ca81f925a7d5fd07234d0975",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T08:08:13.209060+00:00",
      "head": "59d20e629ee748ca57caeed51b4eb2f444909f757f27036b9863f9dea0aa5224",
      "node": "202.wake",
      "snapshot_digest": "fc589fa38c0c019e213d8d81dc7f53b4c55add14d2d875366f567016332311ad",
      "version": 57
    },
    "203.wake": {
      "generated": "2026-10-26T08:31:27.939661+00:00",
      "head": "8cbf5c5484d41cd9447ffe488d77385a6b8029d19427b17af9eb559f4b0b2b65",
      "node": "203.wake",
      "snapshot_digest": "4e6cded64d7fa5555c9bab4c95b1a76cf50c95e0c855ba6437415d59e339fb8a",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-26T08:35:07.371547+00:00",
      "head": "f6e9b435af58ad24565e8e2fb39ba445278ba9d8b6a2134109f32482540313d6",
      "node": "300.wake",
      "snapshot_digest": "898f4567b6101a883fd2e756d07c1a17abf1f5be2559f42a97a2254d7061adbb",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T08:11:24.570195+00:00",
      "head": "732ac8c34da139d50164883bf0055ac3c828a2b54ddf2feff04bdf018d465082",
      "node": "301.wake",
      "snapshot_digest": "276705ff1571bd371d70731ed939d20d2a4fae3a6440d52b5ca94ea43fbfa5c1",
      "version": 61
    },
    "302.wake": {
      "generated": "2026-10-26T08:07:41.004577+00:00",
      "head": "25e08868418a56687c1d4834454a110765c01e41f0b39605037f7481ef540318",
      "node": "302.wake",
      "snapshot_digest": "110e43a4002d354056f1ae5ee8ad1c79a4885d2d3264b86230e07e20b60a4084",
      "version": 45
    },
    "303.wake": {
      "generated": "2026-10-26T08:37:43.236161+00:00",
      "head": "be6a9a023590f2755b1d643fd76ca6ccc1a8fbb903b498ebd70ddb20f3e6e32f",
      "node": "303.wake",
      "snapshot_digest": "8d71e9cc8e771e8d3e91013a2f5b4783889da403ac3d2a0e255f5adb0b5313eb",
      "version": 55
    }
  },
  "version": 556,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3130302e77616b653a3a736f757263652d666339353238383235653434343636/63.json)
- [evidence record](../reader-records/evidence/3130302e77616b653a3a736f757263652d666633653231383439623637343865/61.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
