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
  "generated_at": "2026-11-04T01:02:56.504473+00:00",
  "head": "snapshot:f91d1ec94938ec1e0f15fda7cd50982f076a286c6e9242fc770f8032d3cf2740",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T01:02:56.281468+00:00",
      "head": "4ea1b9bfaaeea9d2a52f1ada644cece1ce34964db822a5ad0011098244c73c01",
      "node": "100.wake",
      "snapshot_digest": "a3f518b8c766b9043bd773e654ccf32e0a6b46097b4ec8ba91b0602a5f4ee3bf",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-04T01:02:56.458763+00:00",
      "head": "330204ec2d19213dcb85a641807d0f69d7f55a5ef84c3653dd9803a4e84f7aa9",
      "node": "101.wake",
      "snapshot_digest": "47de833eade479f440f88064cc65a2c36785e8104763ade845c7eb7793d74e37",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T01:02:56.204792+00:00",
      "head": "c4c912feb47bb74dfbfa436ba5b7c9f173518d617d0c5084c78d268b0d2f832e",
      "node": "102.wake",
      "snapshot_digest": "69e39ced3253404c366d00e3b1029059157707e94c78b3583ed7211bfbad2f1e",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T01:02:55.599107+00:00",
      "head": "d114a0da6305ff79c9280d5bfae73ba68e4711dd0e5c48ea3eae959659d74f70",
      "node": "103.wake",
      "snapshot_digest": "3cc02e7322169f25a53647eeedf335ad4119991a9c01484983d6b3b86921aa32",
      "version": 6
    },
    "200.wake": {
      "generated": "2026-11-04T01:02:55.961562+00:00",
      "head": "88df8e9ad29ed2dfcdfa9b5c3d4b791e15c69deda8c79ed7c209783d792e328f",
      "node": "200.wake",
      "snapshot_digest": "78bac1ee6aaa38c6429a86ff280d5c6795194df7b13e3735d661d3bd86df4fdd",
      "version": 2
    },
    "201.wake": {
      "generated": "2026-11-04T01:02:55.675724+00:00",
      "head": "5ff6756ad08c11a0562acdf11748b052076a69e8c77e5f6e81966821d8421c46",
      "node": "201.wake",
      "snapshot_digest": "bb33a637dd7ea88e70712e3856f0675cfe2077e76318edaa11b9185cf83e17b5",
      "version": 3
    },
    "202.wake": {
      "generated": "2026-11-04T01:02:56.175755+00:00",
      "head": "3fa2a07b66b7c774b879c6c8149f86dd195d8f958567799954454d01d3257bc6",
      "node": "202.wake",
      "snapshot_digest": "a4632df0a90fae425441a2787f934543cf6d2e7a6f6a10ce50900d51d21edc3b",
      "version": 6
    },
    "203.wake": {
      "generated": "2026-11-04T01:02:56.193314+00:00",
      "head": "0828fa8b3e703f6a4ed35a35d433601b6cb51e6a92f3e9ba40070329b395a8fc",
      "node": "203.wake",
      "snapshot_digest": "dc33d7b9390d2ed64a8edc15edf0b3ac93e010d1a5b739c859affd279fd9674d",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-11-04T01:02:56.504473+00:00",
      "head": "c3d1fd9effc45fe98739404d074d6d37a2d1511f850dcf466f158fa37baeb561",
      "node": "300.wake",
      "snapshot_digest": "e62a1c1c6507de646e55d7472392bfbdcf08c250ab0ab68a1ab3d6ab056a14ec",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T01:02:55.464940+00:00",
      "head": "5b147cffa5554b8a0ef5d67e60a26f8d0f320a771815033844681698ed5fb606",
      "node": "301.wake",
      "snapshot_digest": "3af07db237d576cb8acbaa34e4245b2fb29591f7120bf50967258415a8f0d2bb",
      "version": 3
    },
    "302.wake": {
      "generated": "2026-11-04T01:02:55.830702+00:00",
      "head": "00eb0bfd1f9c2a2dd027489d8e2dc934b085562748825dc4fddbdfc204985d99",
      "node": "302.wake",
      "snapshot_digest": "0b8742a52e175e1ead45ca54aeccb92637cac1bd424433236b776c5001ed8782",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T01:02:55.639284+00:00",
      "head": "6124e3dd50a6f8cf8538987b1883e7470da0a0a82876e36489b31438029eb70d",
      "node": "303.wake",
      "snapshot_digest": "63f7af047efc72077e82e3c129240b1fbc9f0705037f7ed9777c848c653f3909",
      "version": 6
    }
  },
  "version": 48,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d38356433656261656563353034343437.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d32363133336638313431316434303139.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
