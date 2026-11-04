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
  "generated_at": "2026-11-04T01:00:54.223883+00:00",
  "head": "snapshot:9758e3513a77bd442e7056f206da86600f240ee43e7723afcb487a0545a5ef91",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T01:00:54.223883+00:00",
      "head": "4ea1b9bfaaeea9d2a52f1ada644cece1ce34964db822a5ad0011098244c73c01",
      "node": "100.wake",
      "snapshot_digest": "d6ce0b62daaab04e37bac58566d25621eea57867fdeebb4c832ad63d49dd0b66",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-04T01:00:48.777835+00:00",
      "head": "330204ec2d19213dcb85a641807d0f69d7f55a5ef84c3653dd9803a4e84f7aa9",
      "node": "101.wake",
      "snapshot_digest": "d948459b98d00a9b2b3af752beff51956787b91dcab61ab1e095570b3cf43188",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T01:00:49.090037+00:00",
      "head": "c4c912feb47bb74dfbfa436ba5b7c9f173518d617d0c5084c78d268b0d2f832e",
      "node": "102.wake",
      "snapshot_digest": "cd99a6a16dca12507dcf8dab7e3a9bf48b5278541872e9db70d6318a45db1e6f",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T01:00:48.971514+00:00",
      "head": "d114a0da6305ff79c9280d5bfae73ba68e4711dd0e5c48ea3eae959659d74f70",
      "node": "103.wake",
      "snapshot_digest": "b8e6fc052411f80d8d42371d69afbebd826d0e5b3f18fe07f12a095c02d721fe",
      "version": 6
    },
    "200.wake": {
      "generated": "2026-11-04T01:00:48.472533+00:00",
      "head": "88df8e9ad29ed2dfcdfa9b5c3d4b791e15c69deda8c79ed7c209783d792e328f",
      "node": "200.wake",
      "snapshot_digest": "56cf16f1c9f8fad6d6b98b71a32b04dff8924d738800efc749b8acf0303b6441",
      "version": 2
    },
    "201.wake": {
      "generated": "2026-11-04T01:00:48.233147+00:00",
      "head": "5ff6756ad08c11a0562acdf11748b052076a69e8c77e5f6e81966821d8421c46",
      "node": "201.wake",
      "snapshot_digest": "ae6132ffa5f1700e75de319284247afd103a0d58c5889233009795b556edf567",
      "version": 3
    },
    "202.wake": {
      "generated": "2026-11-04T01:00:50.585764+00:00",
      "head": "3fa2a07b66b7c774b879c6c8149f86dd195d8f958567799954454d01d3257bc6",
      "node": "202.wake",
      "snapshot_digest": "e8677617298885bcf8aa779b14c712989d9fd1aa3eb50f12d66cc16e79d562c7",
      "version": 6
    },
    "203.wake": {
      "generated": "2026-11-04T01:00:49.988649+00:00",
      "head": "0828fa8b3e703f6a4ed35a35d433601b6cb51e6a92f3e9ba40070329b395a8fc",
      "node": "203.wake",
      "snapshot_digest": "2f139cbb2dc94d6891e30b98dadac2b2a0d1daa704390c5288824e7b27a3d5e9",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-11-04T01:00:50.410748+00:00",
      "head": "c3d1fd9effc45fe98739404d074d6d37a2d1511f850dcf466f158fa37baeb561",
      "node": "300.wake",
      "snapshot_digest": "fdedad88746619fca63738547d5b4f868c43f5954853b6585c772d5ea53f2d2a",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T01:00:47.775853+00:00",
      "head": "5b147cffa5554b8a0ef5d67e60a26f8d0f320a771815033844681698ed5fb606",
      "node": "301.wake",
      "snapshot_digest": "1faba4af245a4b2842e9db8109260c6ebff020675b8cbe5713b397724d59567b",
      "version": 3
    },
    "302.wake": {
      "generated": "2026-11-04T01:00:48.372885+00:00",
      "head": "00eb0bfd1f9c2a2dd027489d8e2dc934b085562748825dc4fddbdfc204985d99",
      "node": "302.wake",
      "snapshot_digest": "5fac6f5b7badf3ba008a4ad7f56ff8fc8dec5d1ce12d0bf3fdc2ef131bceda6b",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T01:00:50.403037+00:00",
      "head": "6124e3dd50a6f8cf8538987b1883e7470da0a0a82876e36489b31438029eb70d",
      "node": "303.wake",
      "snapshot_digest": "bb05f8fb43c1abc3bdbc9466db794a20793c37b0f5a34bdac887051eda668600",
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
