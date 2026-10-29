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
  "generated_at": "2026-10-29T16:52:39.166358+00:00",
  "head": "snapshot:24636900c287e0de76e02eac58730e610be4b722f6d629ff0fd48e77b741d319",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T16:40:54.574072+00:00",
      "head": "f5cc48ee50aabf6aebe6d4f466d49e8a6a17d44df528efc46c9ddaf97c59071e",
      "node": "100.wake",
      "snapshot_digest": "0e41f56ced5e4ed1ba82dc68a7c0553bb217ba6c9c1581d0f23b4f0461718d95",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T16:42:07.768428+00:00",
      "head": "0aed9c58b95d0c9886744cf65b2de95fc607a1cea315c44f8bc182dce6f757ae",
      "node": "101.wake",
      "snapshot_digest": "95259c1f5a17f9922105f03527e3fd19cac19f1fdd8f4548990315231c47f5fd",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T16:28:43.915351+00:00",
      "head": "8d7b867769746e4d67cd3b5d262c86fcada7a7ffe26682636278ecdbfdc2f351",
      "node": "102.wake",
      "snapshot_digest": "1011d6b830f8b14399aa8d56be3e68725a8990fb8870dc5329c14215b6524ade",
      "version": 18
    },
    "103.wake": {
      "generated": "2026-10-29T16:52:39.166358+00:00",
      "head": "af516556b0b895710b27a1e0c5af80e1c7afdf36dd1a2e4a50d21780983fa51a",
      "node": "103.wake",
      "snapshot_digest": "af6fdae2012bcbd3124feec037fac4ca3aa3b41998e0953cf48f3bafc7c70136",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-29T16:34:48.998755+00:00",
      "head": "1836e84e8eb13ae04ca34682c43cf50e1d447b4772db86b06bdd3d749cd78446",
      "node": "200.wake",
      "snapshot_digest": "f85303cce0ffa3242b00e4c9494e6912dca87a216308194a782dd082c9f0b9f4",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T16:50:51.800734+00:00",
      "head": "94770d5ebd82cbb9d7e3ed19a85dba32b02ce023b7ed2216ce63eb9cca81b365",
      "node": "201.wake",
      "snapshot_digest": "b3ba8c3f41646202ab4b959bd13481dc345c5629fc31fc9b4ed6ecb4ec94d162",
      "version": 25
    },
    "202.wake": {
      "generated": "2026-10-29T16:45:49.462852+00:00",
      "head": "3a9d4792086a600a540157b6a92a2acde58d57e0f1b8911e5f68c4e63af28ff2",
      "node": "202.wake",
      "snapshot_digest": "653ffc8881f9fbb1d9fcb0ca3d63ad7e6561d34300f29ed72b35e0c64abe46ad",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T16:43:32.934313+00:00",
      "head": "8171899bcea551aa4a9453a31c752203203898596c89f84266b85ebaecd9ad25",
      "node": "203.wake",
      "snapshot_digest": "1465191c6608cc134dc0c5904a212cbbaa5d772f41fc09e1a2547e8bb3a68d79",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-29T16:39:44.869716+00:00",
      "head": "aebf1e31eadd14e0258fe8be7fe9f5249a6e90aa44ca0398f2b9d4acdf905099",
      "node": "300.wake",
      "snapshot_digest": "45411cbdf1cfb52b1bccdce73e6f406e1acf02b7a11ceb46241d3e1144bb0835",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T16:33:50.939086+00:00",
      "head": "7aeba747ca9676fca506813589871814f0f9e5120dffe46159d81d7b8856f2c5",
      "node": "301.wake",
      "snapshot_digest": "32191cc47aaa6753314629320a8fee5f8ea237d31e91f4b0ac6eec0eee0427ac",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T16:16:28.602585+00:00",
      "head": "f7289faacbbfe0b868b5df24b3d4c4642eac61241280aff8291381d2111e43db",
      "node": "302.wake",
      "snapshot_digest": "bd4c34314a10b6668c149f7c58aefbfccaae7e27c3788a6c7f00c1542c9dd038",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T16:26:50.083229+00:00",
      "head": "e08894c01c9761d510b6c4e485de9c257178597950173019d7b8b022b152170c",
      "node": "303.wake",
      "snapshot_digest": "131d6ff7862642c67d8b41423a9421b20166fe751ec869774279941ff7e0d8b1",
      "version": 24
    }
  },
  "version": 298,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d383934366262343132326633343437/64.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d616238653039383535343864343966/36.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d726573706f6e7369/62696c6974792d666f726d6174696f6e2d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
