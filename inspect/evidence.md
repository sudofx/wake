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
  "generated_at": "2026-10-23T15:10:14.798960+00:00",
  "head": "snapshot:9700cade1766e0da44614d4fbb61307c51f210a33237c77ab76bab47d2bc6075",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T15:00:30.120271+00:00",
      "head": "d1259c4d3195e2b5db9d22f5e17ef8f66d94e73819a0335e53a53c0171b1163f",
      "node": "100.wake",
      "snapshot_digest": "55ba10f4de9286eec446c87fb43a7fc9b1c9e3f247a2aa23b39619cb729b5a34",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T14:59:49.785284+00:00",
      "head": "53e602cc5fa50bd8205a6aa434d9c7d50d2fc28488a15161b8b86a572576bb32",
      "node": "101.wake",
      "snapshot_digest": "e3100333c81fb2402245e5e7d385276e9cf0d467db3b807b2a589a1d9291c171",
      "version": 24
    },
    "102.wake": {
      "generated": "2026-10-23T14:58:20.890834+00:00",
      "head": "1a83faf68b75f9959b78f845b62ae3002b0e5c8b0c135ab8411e5860f5af2240",
      "node": "102.wake",
      "snapshot_digest": "5102cda0c12516c82bc455ff30e2bc37d5ff318676a79a95e92a00089e22cbbe",
      "version": 31
    },
    "103.wake": {
      "generated": "2026-10-23T15:02:30.339070+00:00",
      "head": "d11ea9911d56e56e5ee5dabb9438c9c1480e4363ac21c1f2e6be701d696e0657",
      "node": "103.wake",
      "snapshot_digest": "072b4c0f1347ef941fb0b135c93148efa57eba1bbaaaeb0bec628ff535fbbbc3",
      "version": 21
    },
    "200.wake": {
      "generated": "2026-10-23T15:01:36.310831+00:00",
      "head": "29044fcff032624359f75badff7294cca7db0cddf8ac4c935ab5006769aa4825",
      "node": "200.wake",
      "snapshot_digest": "9af17d490ed13e83c26e13e8174d81c7c7507a73b3600f5ce2045cebdb577296",
      "version": 20
    },
    "201.wake": {
      "generated": "2026-10-23T15:02:42.305801+00:00",
      "head": "ec777a63e80aef9c703b3f74332714111750d1182239aa1278f2107dd8d9d132",
      "node": "201.wake",
      "snapshot_digest": "5ff5ca4086c55b123079643b51ef05144ac4ad5d487c4b10baed0dd17144294e",
      "version": 21
    },
    "202.wake": {
      "generated": "2026-10-23T14:59:35.835980+00:00",
      "head": "b8839f6540ed0c42eca881f9b9cedecb426c08c30f8cd4884961cab3da62899a",
      "node": "202.wake",
      "snapshot_digest": "a4c317c1d3ae9145cec1219bd5eeb4a68fab8ee52168595f6a6fd685c452eabb",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-23T15:10:14.798960+00:00",
      "head": "e21bb6662c99eb2d5608c558011c1518cf35294f605a548aade5f4f2078997dd",
      "node": "203.wake",
      "snapshot_digest": "04a50bad5489db8e331652713ccdd3f7a7791ed37b78dc1b95d49328ef769ab2",
      "version": 13
    },
    "300.wake": {
      "generated": "2026-10-23T15:01:56.890734+00:00",
      "head": "0ed51a1658144fd33dd9d9388142eca03bbafc8c1b8e41597fe7a505c14283b6",
      "node": "300.wake",
      "snapshot_digest": "b91f4eb474356e59bea36e4c9bb00882cd4e837948f3c4d1d47560f63e81612e",
      "version": 18
    },
    "301.wake": {
      "generated": "2026-10-23T14:59:28.564906+00:00",
      "head": "b045279fe461182968d3c7f750b35e32581e6e9665c23466f4749340ceb3bcfb",
      "node": "301.wake",
      "snapshot_digest": "aaadfe2ce8cd9b827ab71e650ed686ee502f3cf38d8b0ed461a20c3a05ac376f",
      "version": 29
    },
    "302.wake": {
      "generated": "2026-10-23T15:01:23.960141+00:00",
      "head": "1f7164c811adba257a69476f7879f94a7a9dc72a2e7f1c07fbe51f9fbe638eb3",
      "node": "302.wake",
      "snapshot_digest": "891f6cb1534f4b4da9e77efdf4500e1c7f61411aa2709d4a45e5198c96988d61",
      "version": 13
    },
    "303.wake": {
      "generated": "2026-10-23T15:01:11.396013+00:00",
      "head": "bf74c99ed772d259b6eb3e4efb19a2fa9272d9a172f33898b6a6fcd7e8d1e81d",
      "node": "303.wake",
      "snapshot_digest": "641025b9e1cdea4a8dc737d98076a4c08164e4b04ae0dc0ba21f341afde970a2",
      "version": 28
    }
  },
  "version": 266,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d38616461626161643733376434356133.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a736f757263652d376534643864626632343730343231/39.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
