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
  "generated_at": "2026-10-26T01:03:24.358008+00:00",
  "head": "snapshot:a79d0d39ec01cff611557c131f5c571142199e158194b968ce280c81c28138be",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T00:55:04.012698+00:00",
      "head": "74c345ce3cd90222e504caf0a02297ac48993d360b96547b7c95e8409446d029",
      "node": "100.wake",
      "snapshot_digest": "d8643747ed4ea7d2e288eea55c3f7f38a733304f3764ed2b4811af442b4dddd2",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T00:29:16.719703+00:00",
      "head": "3db59bc58f708e114291d9d12795520c104c54e203f3254936a48ddc0ee64bcd",
      "node": "101.wake",
      "snapshot_digest": "326f4aea2f1d60d7b8a19be701ff48a5a78b44201949abaa0bd5bc9d03b8165c",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-26T00:55:21.601444+00:00",
      "head": "f5cb851cb705f937758d2fcb25f14c0816ae35cc23cc3d1da10c338996344a7b",
      "node": "102.wake",
      "snapshot_digest": "4b368b1db7f46c351492c65f676d892ec6a85649f9a1834a9f82a2f8b5f04839",
      "version": 58
    },
    "103.wake": {
      "generated": "2026-10-26T00:54:29.554377+00:00",
      "head": "324a71adb177ea73de4807051f703ddb869b8e4fb9c7e45d071bc091c121331f",
      "node": "103.wake",
      "snapshot_digest": "9ce434d74be0d7e1d3e79543c4d07180995351226fce6d59ef750a77441349b5",
      "version": 40
    },
    "200.wake": {
      "generated": "2026-10-26T00:48:01.553714+00:00",
      "head": "30e90d56afb8e9e8881d3264a8d0df2bc6d1aa88cb30e005295fe7218f15c40b",
      "node": "200.wake",
      "snapshot_digest": "54cc59b281452a289c57cad237b6c5301c250f5dccc7a6f39b3d70fa766c9c5f",
      "version": 36
    },
    "201.wake": {
      "generated": "2026-10-26T00:49:23.290945+00:00",
      "head": "3e0dee3b04a94928957f048cfe508f1c0c6562fe28eb026f22e2840c16559518",
      "node": "201.wake",
      "snapshot_digest": "7870d8074cf90b665b0e9e1226eb90593cb6ee3698bd6dd90005b4a1a14a27dc",
      "version": 41
    },
    "202.wake": {
      "generated": "2026-10-26T00:29:48.696919+00:00",
      "head": "59fb10341690a829d5ba5149dee20dfc8c31172c4cc87c9d6c3567c89b2e94f6",
      "node": "202.wake",
      "snapshot_digest": "2e4d240880f4cef1fa0f244ae0e76968411ca9b6ed54a7e7920b4fdbd7077e5f",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-26T00:50:23.968517+00:00",
      "head": "04927404e8011aec45c04fa323f2189f070afd865db0049e713759b6909305d2",
      "node": "203.wake",
      "snapshot_digest": "fdf82b0d4c2669c81575a38d18c054d86b96dc119118ac2dad5550c46a42c20e",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T00:33:33.210821+00:00",
      "head": "4a98682dca9cda8f7a03c0d857d4d91ef2d6bca57958508af3cdab79d25f76a7",
      "node": "300.wake",
      "snapshot_digest": "d8699faaaa32ceaad07361bc1ea26db4845ef4a55dcc77523e99439bb7f3446e",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-26T00:44:23.193367+00:00",
      "head": "891fe17163134a4586785cc1c65d77e5bafef1ebadb1baf51f2977819d45046e",
      "node": "301.wake",
      "snapshot_digest": "318ad4edb14606bc39bb3467162ef513b9a02eaebef0292b4526771344f70629",
      "version": 58
    },
    "302.wake": {
      "generated": "2026-10-26T01:03:24.358008+00:00",
      "head": "1957c918ed4a36285bb91ced4ca10e593006d1844526cdef30d62058eff8ce8d",
      "node": "302.wake",
      "snapshot_digest": "10499cb340315d11f50c23edd06b744e2ea34ec689944a01b68a2b78fc433b6f",
      "version": 40
    },
    "303.wake": {
      "generated": "2026-10-26T00:50:57.107409+00:00",
      "head": "b801365f2eb14d1f0ef2f274699828205ccb2a8c8375bfe46fa199dfccc06f59",
      "node": "303.wake",
      "snapshot_digest": "1f4db99904a4b171e77837aa648d5ceb7537c63e70d4358a37d82c218c0b5270",
      "version": 51
    }
  },
  "version": 519,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d38366234323232623665626134333535.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d383935663065363564366336346266/36.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d726573706f6e736962696c6974792d666f726d/6174696f6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
