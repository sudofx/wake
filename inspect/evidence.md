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
  "generated_at": "2026-10-23T00:36:19.927602+00:00",
  "head": "snapshot:67e52fbd31eb47088abde04fd3f763b3ab3623db1200fb3fd031afde0fa3df99",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T00:36:13.928284+00:00",
      "head": "c123f5b6f4030a4e171cc4f34ccb36045a74a7e9fbb4f22e71625c0d67978178",
      "node": "100.wake",
      "snapshot_digest": "bc94243cc657a11715e6c78c60c80aa5da57624fc50bfbfd1ba8e25c289f5922",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T00:34:38.570782+00:00",
      "head": "0e90e30d2bfb29985c05b8cae0c3cfcea795d9e5b87f02e6ce858f1a4769a3ed",
      "node": "101.wake",
      "snapshot_digest": "8d6843816c0ccc17fbb275e2c6140f38bbfd71dbd8dfee9d61e0edaec87e5f4b",
      "version": 9
    },
    "102.wake": {
      "generated": "2026-10-23T00:35:32.354315+00:00",
      "head": "e4238b2a357096431a0065590acdf8b778a83223b86c4baeb9c4173d6ba5ff4b",
      "node": "102.wake",
      "snapshot_digest": "1112a148500edfb4e4ff0ede5614f9f81fb6ed8691f6c78765744daa223c9662",
      "version": 8
    },
    "103.wake": {
      "generated": "2026-10-23T00:36:19.927602+00:00",
      "head": "7ac44f18b2af3435a0bc80f588f8e5853fca9895f427672fa501e1d4efb923be",
      "node": "103.wake",
      "snapshot_digest": "7a511c51ce9bb10fd7145e1f2df3d55fb0930332ec8235a2399265c80fba8bbb",
      "version": 6
    },
    "200.wake": {
      "generated": "2026-10-23T00:36:02.179058+00:00",
      "head": "2a994c5981e3f2f99353a146372611923563c7b3df0ba5e9ec20ac57973f5666",
      "node": "200.wake",
      "snapshot_digest": "24ed629f1b1e01aac1e26aed31a1c4af4f652dc77293951309c972419423e540",
      "version": 4
    },
    "201.wake": {
      "generated": "2026-10-23T00:36:17.083774+00:00",
      "head": "3b0b6d0b9d4e58cb9051e277687fa60755eb5fd6067543d1791caa5cd023011d",
      "node": "201.wake",
      "snapshot_digest": "fc419d8fdc81abef7aac94e68bbde3ebf7026cc54ccf58790dfa6877cab1b052",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-23T00:34:41.905589+00:00",
      "head": "8de6ae46451279638b6f7e9cf961f02a6c2f0a790ab58410c4f70ae08c5c409e",
      "node": "202.wake",
      "snapshot_digest": "5ada02e9c3929220de589dc8b10ad53d9a13737767b889c0079fbfd0d16947be",
      "version": 12
    },
    "203.wake": {
      "generated": "2026-10-23T00:35:38.961047+00:00",
      "head": "0d5d278cf9ff6030c5e3c6d194381e7cfb624d8e4fcf732fae99914b5057d5bf",
      "node": "203.wake",
      "snapshot_digest": "22e71c811842ca6ac6a669ade2613cc5020978f6044ce861d744bcf5cfa04ede",
      "version": 5
    },
    "300.wake": {
      "generated": "2026-10-23T00:35:21.961833+00:00",
      "head": "3e9b9d3a9304631607ea17f9217aac494babcf81ed9545d917bedb1520395603",
      "node": "300.wake",
      "snapshot_digest": "15ec1e32a66a06ad2e3eace33f5715e39cfbd95fbb4c03036bf104eda89a8ba4",
      "version": 4
    },
    "301.wake": {
      "generated": "2026-10-23T00:35:45.716869+00:00",
      "head": "d5e056c9f3a63f009cd72df5543d4eaba7a5db686b79ec69fe527e85797b0f6c",
      "node": "301.wake",
      "snapshot_digest": "0252dbe35d853d9b02bb833059dd5120b7d12a2b5c61985b5fb815c67ee1dcff",
      "version": 7
    },
    "302.wake": {
      "generated": "2026-10-23T00:35:52.158919+00:00",
      "head": "7cb320958ba16c1b6b03cbb1e352a712a8f1f825dbc2761fa3d09ae22a9825f5",
      "node": "302.wake",
      "snapshot_digest": "4fdbda9c847bdbcade1a101a57baab0c8b8c6cb5a2ae458913c24081ad40fa9d",
      "version": 7
    },
    "303.wake": {
      "generated": "2026-10-23T00:35:55.648660+00:00",
      "head": "485088b578cc5de92cca9be985feaab7b2483effef9403be9a1fae21702e3253",
      "node": "303.wake",
      "snapshot_digest": "4f779f5d1a798c91b8b3bef32472139c11047e94e076ebaeeab24e5087b63e8c",
      "version": 13
    }
  },
  "version": 91,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d33.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d386435323466633134643865343466/37.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d626632646562393538633237346161/31.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
