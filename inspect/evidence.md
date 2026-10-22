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
  "generated_at": "2026-10-22T23:00:04.423666+00:00",
  "head": "snapshot:979c8a7e2272077c9c92182d727765305435b688bf4c8db3228fc81a7f2f4796",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T22:55:08.752042+00:00",
      "head": "23e277104d5cfe955442958b96d1ab6cbc80d83218a6b85346e24e0e4fa0a2b7",
      "node": "100.wake",
      "snapshot_digest": "963bb9ad777a714983466dbc5a58ed9dd0ccaea185db6500e8a6592ad54f4d45",
      "version": 3
    },
    "101.wake": {
      "generated": "2026-10-22T22:58:40.353733+00:00",
      "head": "e2148d6650339034d3022e760009714d896881fc8a8e1dc443904230dd093fb1",
      "node": "101.wake",
      "snapshot_digest": "a9d206e419163a0d842ed8b8b0802acd15919ed2f28b2b99109db599bb2bc2a7",
      "version": 6
    },
    "102.wake": {
      "generated": "2026-10-22T22:59:52.806237+00:00",
      "head": "9c8891b274c5753c9a6b5cf0e95b58e4007e5ae4fe419f893c3f676c11c5b2a5",
      "node": "102.wake",
      "snapshot_digest": "b046485610e00ea66e624a6e5a2ba04908f36f507bae6629a20d90fc0d2a3e67",
      "version": 2
    },
    "103.wake": {
      "generated": "2026-10-22T22:59:37.055154+00:00",
      "head": "964e3ebacd56d6203f6aa0908a34c9ea0bf71f0265e66e694b76bb171d1b2240",
      "node": "103.wake",
      "snapshot_digest": "86fc8069da781e4d22e0ba6ce9cbf801060dfcf6b107aa3b268cf6d4a22920a1",
      "version": 3
    },
    "200.wake": {
      "generated": "2026-10-22T22:58:04.462051+00:00",
      "head": "d7ab4fdffdf91a65053bedb40c00cbcc01331d39b396b542627f23e06ff56936",
      "node": "200.wake",
      "snapshot_digest": "11c2f60a2f57bc0531938f4c5b6fdcee69ff2204290541150351d94e8a65ea83",
      "version": 3
    },
    "201.wake": {
      "generated": "2026-10-22T22:59:28.079497+00:00",
      "head": "47f18de1a210cbba691e9128312cbaa687e7f5e91272775bf06b6dd442179adb",
      "node": "201.wake",
      "snapshot_digest": "ad097d0fa2530128f4e47becbd1c7a7592478733e2dce5cb4fa19cb8b94f5802",
      "version": 8
    },
    "202.wake": {
      "generated": "2026-10-22T22:59:14.150112+00:00",
      "head": "d7ce715464af7d1611e3ee5caf7b07363741b53ba1288554bed065abc86900a2",
      "node": "202.wake",
      "snapshot_digest": "cb57af13b0faa62fbe8a1dc0f9e607f29b89665116854b92826afda5829169fc",
      "version": 6
    },
    "203.wake": {
      "generated": "2026-10-22T22:59:22.363058+00:00",
      "head": "8d6e7b33d54e253dbbc7780b4bd95d4baccc0f1c0889259b2d4b5ef993601d87",
      "node": "203.wake",
      "snapshot_digest": "bd0792d5760a94de1fb6929e8e5a113f030055c637fe8049598dbc9f4b4e7c50",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-10-22T22:58:51.409267+00:00",
      "head": "b754ed8cb58a49a283d9c6f67185b364dd795d25cab8045a570538a22832d8db",
      "node": "300.wake",
      "snapshot_digest": "31150d954427e65a0d136f7c9ccb33bbce50c390e3dc6b3b83731e4f079240e7",
      "version": 2
    },
    "301.wake": {
      "generated": "2026-10-22T23:00:01.121058+00:00",
      "head": "56dabd0ea85d2c5bea9edd32f91c0ec75ffcbe141fd05c867a725c22f276122a",
      "node": "301.wake",
      "snapshot_digest": "a5fd9d84660a01a83eee3899d8c08ab6da025d6cabc0deaacf10eebad736fba1",
      "version": 2
    },
    "302.wake": {
      "generated": "2026-10-22T22:59:33.401863+00:00",
      "head": "d820ee20e4520e7989e816fe93034933027b327d755f0f3bda2db0a540c0cf4b",
      "node": "302.wake",
      "snapshot_digest": "f08fb6f35ccd28ee04800aa6670b70aa2b363fbe9c37d8e72f7bb5fbf9f75713",
      "version": 6
    },
    "303.wake": {
      "generated": "2026-10-22T23:00:04.423666+00:00",
      "head": "8a199ade05d2c72ed17f3a978f26aaf031801d23d70092fb51657a2542fc2526",
      "node": "303.wake",
      "snapshot_digest": "b4cda5ff81b78bc3e848aef667fe6b063435dbea47b47ad6a799ededcfdc336c",
      "version": 6
    }
  },
  "version": 49,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d32.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d37353136343963663936306134323634.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d323734353833373836353433346533/35.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
