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
  "generated_at": "2026-10-27T06:01:44.515203+00:00",
  "head": "snapshot:e7c1bf23ca7eabefe18f84e73bb82df89a23ea10cfe3b10aac957839a9bc25d7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T06:01:44.515203+00:00",
      "head": "79a5c6681abeff6dbca7e3442c4a37d6f591999bed3db56c2e4cc7cba71d1862",
      "node": "100.wake",
      "snapshot_digest": "3d7c7339293b018325e43fae0cf004f45cc540fdaccd7aef8ba80f2239e47876",
      "version": 34
    },
    "101.wake": {
      "generated": "2026-10-27T05:50:07.897959+00:00",
      "head": "57da007e659b82fc38838f11d8c35d3b845bf945ffaf34ecd8d4b78c76a1d3c9",
      "node": "101.wake",
      "snapshot_digest": "535aafb1e815f7da7a0857615839f4980aa18d96586d27d2878960e9eff3f812",
      "version": 50
    },
    "102.wake": {
      "generated": "2026-10-27T05:59:11.678544+00:00",
      "head": "2d1f7a96452ed682a1c8a8c189bec5b3be823e4bcceabc36ebf3c0965dd13c30",
      "node": "102.wake",
      "snapshot_digest": "75ce1474169b2e805aabe138074049461d01babe3b6ddc804ac7d71691ae4572",
      "version": 64
    },
    "103.wake": {
      "generated": "2026-10-27T05:58:36.893331+00:00",
      "head": "e5f25b93ee444326afbc47f9ac3c1cbebffde20f5cbecbf164eb258b918a6e35",
      "node": "103.wake",
      "snapshot_digest": "f5830e7bc55a69ece3a93571813ebce097f90265e956705a697b590b04ccb751",
      "version": 46
    },
    "200.wake": {
      "generated": "2026-10-27T05:56:28.045427+00:00",
      "head": "6340745f465495b17089e6f75595054e91b264ae5e551aee88e64bb05e856c0f",
      "node": "200.wake",
      "snapshot_digest": "ec30f5a4fe6c2817c989306f19fadd8ea3d6afdc989cd06fa89aef53f7ae82b9",
      "version": 47
    },
    "201.wake": {
      "generated": "2026-10-27T05:41:13.383677+00:00",
      "head": "6e06ad39ac72d735543ca505760d44a5c65c3ae9c9ed8d42061a329e6a666bc1",
      "node": "201.wake",
      "snapshot_digest": "4affb7e38094c817e457f8653dd6ad88cef8a395a6c101c1a7ad6357c9e6b92b",
      "version": 47
    },
    "202.wake": {
      "generated": "2026-10-27T05:48:33.334873+00:00",
      "head": "a758217b0dce8d1fb310c54226388a05b0a71e1e01526028b769a6d0e15ad9d6",
      "node": "202.wake",
      "snapshot_digest": "a8834dfb6f6865e6bd122625c5043ca807f41378a498ec879995283ab0731d2d",
      "version": 64
    },
    "203.wake": {
      "generated": "2026-10-27T05:47:56.626227+00:00",
      "head": "73b28dc4f94f7d6ff264bb180bf732b7610b519e8728aa6977e312823e3b4159",
      "node": "203.wake",
      "snapshot_digest": "9014ec4b81025dfa8c288107febc127b6911544419b34d3cc1af29e9a8b263d8",
      "version": 41
    },
    "300.wake": {
      "generated": "2026-10-27T05:54:19.027565+00:00",
      "head": "9cfee30c4d8bcbb350e8b28b01f15b985064dde9b80e49e681e3591b21173ee6",
      "node": "300.wake",
      "snapshot_digest": "7db80537a936875a6561a768d5c0df6bbda99409347240636f5d816343df978f",
      "version": 42
    },
    "301.wake": {
      "generated": "2026-10-27T06:01:28.694431+00:00",
      "head": "73ad5937a9e3bbe945481c40732793cd5ba494891e2250c367535e8b21c88338",
      "node": "301.wake",
      "snapshot_digest": "84dd39cdb8034e1029751cad477fcc70480208b558f19c43b15c45de74bd9216",
      "version": 69
    },
    "302.wake": {
      "generated": "2026-10-27T05:45:51.372061+00:00",
      "head": "a3d36af06f0bd3fa63fc15c71e572565042a73e0f2b00ca29c4315829def3176",
      "node": "302.wake",
      "snapshot_digest": "ea5d55173cb747a42c27d5052f02f1a19a88fa684e25fd79b5f3094d6628b9e5",
      "version": 51
    },
    "303.wake": {
      "generated": "2026-10-27T05:55:26.559470+00:00",
      "head": "d36a570df60d8ff28354645ca071a48962a8362223d9b33041d0440eff1f676a",
      "node": "303.wake",
      "snapshot_digest": "27eaff2835119579c5a08de094a5cbb4a9d7d7fa0cb6d5bfc8061c18d27a66f9",
      "version": 59
    }
  },
  "version": 614,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3139.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d66393939633535633438616534613530.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d303564303734306661376535343466/63.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d636f6e74696e756974792d7261/74696f6e616c652d73747564792d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
