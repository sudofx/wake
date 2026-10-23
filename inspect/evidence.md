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
  "generated_at": "2026-10-23T11:17:52.416944+00:00",
  "head": "snapshot:d62c370ded88d41734a04cf5d8b90e53b084a4ff26c47d1f62b638cf8b04003a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T11:17:52.416944+00:00",
      "head": "b69943a3b504737de84815942a5aa51610d260e43f41c99dd1c55c7bd9e4591e",
      "node": "100.wake",
      "snapshot_digest": "04d00693df8eef0bda1485bb0d91cb3b3b395e32009e3e3f6f61fc07204019d6",
      "version": 12
    },
    "101.wake": {
      "generated": "2026-10-23T11:17:25.389786+00:00",
      "head": "81da4fed562b62f901782d46703c93a30ff05625e881dd8f509670b9b8e4bafc",
      "node": "101.wake",
      "snapshot_digest": "4fedfe6fd4fac5ca1dff7f74482bb5336d0dc60afb4b5a2cda2faf524b44bdb2",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T11:15:33.561190+00:00",
      "head": "be7a169e79bc890c3569bc3abd81eee05548fad5307844d24f9176afd7524eaa",
      "node": "102.wake",
      "snapshot_digest": "3f3e904af7f995f7a4e0136efd446a20407015b46c049538de0ea4f8ff0dfb07",
      "version": 25
    },
    "103.wake": {
      "generated": "2026-10-23T11:12:54.418339+00:00",
      "head": "0f75de36cafd4e047bbade883b60b4cca16a2abecbe027d2b8992111367953a6",
      "node": "103.wake",
      "snapshot_digest": "524b3181ed80809360c25c69ebcf304b2e2a100da73320093818396a676a5160",
      "version": 13
    },
    "200.wake": {
      "generated": "2026-10-23T11:09:45.209853+00:00",
      "head": "3fc8f3b9689f3e64f7b04753cac4ec06918d891a32b6f18934352a5646eee535",
      "node": "200.wake",
      "snapshot_digest": "e4f4d3a383ea33021e2bbff3b8f89443cef2ae3cc5e165001433f08fc44cfae3",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-23T11:14:39.461531+00:00",
      "head": "f812c0fd6e8f54b37ac0e3fc4df59694ff7d3cd27bdb1a8169ce71f1132b4cbc",
      "node": "201.wake",
      "snapshot_digest": "6b1970f28d8a7d66d14b7bcec34d0a56cd22683c1479bc537c19f4880d35647a",
      "version": 16
    },
    "202.wake": {
      "generated": "2026-10-23T11:07:10.763248+00:00",
      "head": "771472fd0927cad901c89b31f14235aad724694ac252431626e65a36d0a61aab",
      "node": "202.wake",
      "snapshot_digest": "d567da9ac9acad931dc644a7cbce02d8a63f111162e175b9c29e4ebe24ad7578",
      "version": 25
    },
    "203.wake": {
      "generated": "2026-10-23T11:10:13.056179+00:00",
      "head": "fe7d825f13d72e49afd5a493b2eedf98da44bce748a3dda5ab318a170bdda7e6",
      "node": "203.wake",
      "snapshot_digest": "b9d2703c9e98a37bc74042f4af93f7e90d8fca3cf55f70d6b9929b32fbe62d3f",
      "version": 11
    },
    "300.wake": {
      "generated": "2026-10-23T11:12:47.980269+00:00",
      "head": "29c2c7ca052a958fdff0b47c958bb66323789c9d1178858014f213ce8c685db2",
      "node": "300.wake",
      "snapshot_digest": "8b01e4ad5332cbbc14fe88fabe4c09448f6011531b91df8191119925a87c989e",
      "version": 12
    },
    "301.wake": {
      "generated": "2026-10-23T11:07:59.131973+00:00",
      "head": "92d2863b3ea645367a01c42002ac42001893933995a3145e750ca225a804e759",
      "node": "301.wake",
      "snapshot_digest": "4c207f84fcd39ba38541d8cbc48a83494f2b5ef97055cfaede53cf2438a9e5c5",
      "version": 21
    },
    "302.wake": {
      "generated": "2026-10-23T11:07:01.951194+00:00",
      "head": "56c49096abd0fdc90ba3056a02eb280f18708ccb98aac567e82eef92e81f27c0",
      "node": "302.wake",
      "snapshot_digest": "3aed760f9e9f65a173ac04c70b30261be69277d1760038a00ce532f0d2339057",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T11:13:34.595987+00:00",
      "head": "1f912bdc2aedef699f22469cb462f1e8ad7d05100eddce9dc2009bce76be3194",
      "node": "303.wake",
      "snapshot_digest": "9001a0f903282bd0d086736c4580afb8104aa9c66925aa1459a918e88c046f7a",
      "version": 22
    }
  },
  "version": 201,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d346336356462363639383366343230/62.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a722d36633162616466366365316634636239.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
