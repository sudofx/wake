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
  "generated_at": "2026-10-25T18:41:59.859892+00:00",
  "head": "snapshot:4ab8b72cb65649c2541c3c922575b4d6f763afb34c139ba0ab96109ada904257",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T18:31:20.823421+00:00",
      "head": "18545966b31502645c4fc75c884a2077642b8aba8b0f0e5a27844834738b5c37",
      "node": "100.wake",
      "snapshot_digest": "3ff6c845723d3b17b3e48354f47e9980e3346721827cd31d69494fbc40184dd0",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T18:39:56.284286+00:00",
      "head": "18985739b35fdc5cc3f8bebe9668a734cfac63f0cf41c45e47bec35734419f17",
      "node": "101.wake",
      "snapshot_digest": "168b73debedc16cc22c208b545a99ac53c70a462418ad66ebe850fcbd7b07a32",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T18:31:31.548769+00:00",
      "head": "befa74d64fafc8b014553179f5243345170df60ea10d0fc09742d9c7546fdb1a",
      "node": "102.wake",
      "snapshot_digest": "a9aa5b41aeaa11d8323a1aff88ac350e73c8c0abc6a4d4e4ba9e23bd11de882c",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T18:34:04.302592+00:00",
      "head": "78ff186d999d8001cb2ca8cd2f4748099533d777e0bfdd68faefc8dc5edb0993",
      "node": "103.wake",
      "snapshot_digest": "cac7f85c70521ebe0b317faba403838ce5ccc89d72db60fafb1379c229f2c0c7",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T18:41:08.738637+00:00",
      "head": "a3d284f5b87661e3455a6f13258a61f4cb5a4ea0b582b490c1bba0d846b213c3",
      "node": "200.wake",
      "snapshot_digest": "647b29141adba4f666909c0f95a7effbfec0a6c79ebc6676a36aba9928dbaec1",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T18:41:59.859892+00:00",
      "head": "95f349e47b4a7701ed734c5329ab92531042c8669858ed8345d7e76a751d26f0",
      "node": "201.wake",
      "snapshot_digest": "ba72f749ad38e45407003fc6c504fc5878bd39477917177dfc5d100417f95382",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T18:39:35.623685+00:00",
      "head": "83f775e722f63a52c8d3969598fb0733cc1ac54dd9daa1a11f3209ab4777f8c8",
      "node": "202.wake",
      "snapshot_digest": "a15fdc109577ae3568c589d13cde93131e332eaae567d03c3f0bf60093dddff2",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T18:37:27.593866+00:00",
      "head": "ca41d8a6d7d7e86a4840036d8b176c5169bad4c548f487532b5b77dce866a7ba",
      "node": "203.wake",
      "snapshot_digest": "0f298ccb9ca2e87233af6a0bf58c1b43b9e21eeca540a8bcbda66fb0e9784fd2",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T18:35:40.767572+00:00",
      "head": "e13f768a53af295ea1a166a39f590c8a7e93a3dd91336ee68db243e0491efca5",
      "node": "300.wake",
      "snapshot_digest": "b920afa7a136c122c483c73258ebd08a4bac2c2e68c8ea15708e9a3c64087210",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T18:33:52.806700+00:00",
      "head": "b3caf5c886e5e109a021ea6e8803ae4cdf86ed9e7bb97d7fadb1ed8eb99a86cb",
      "node": "301.wake",
      "snapshot_digest": "4414bcf995f37b8d0cfb2a083f1b2c0297a8aeb6da691c423f7fed913102d11b",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T18:32:26.784645+00:00",
      "head": "42d96ce441d3be73a5e7aef98b15983ae4ad92d723cfd1e7861f851d80d970a4",
      "node": "302.wake",
      "snapshot_digest": "f8b8c9156d5e510026be6f917484d42c18fd039f9a0be4bfb8c7787c0e69e454",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T18:19:15.147979+00:00",
      "head": "80d0782ea4eee55f13a5312b4c05da221d38cedc4699a197316252f6af160485",
      "node": "303.wake",
      "snapshot_digest": "bfe4b63724ad3c6ceaa93fae37b77af6b2c96355218cec81ff0ccc62214a5151",
      "version": 51
    }
  },
  "version": 510,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d65333534356466366231396134386535.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d32303765366230656437326634326630.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
