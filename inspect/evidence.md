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
  "generated_at": "2026-10-29T12:51:10.730962+00:00",
  "head": "snapshot:94ce3b0a6aaeb2408e8886a739a09767d83b38029f8f4f7c8b88992c49a30ada",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T12:39:05.806502+00:00",
      "head": "323dba482a10fdc6ece701392170c74bbbf22225997f7a7370e975e85da20bad",
      "node": "100.wake",
      "snapshot_digest": "11f031fda44603e64ab040d566b95f132be95245a30c4d2ec6b4506af41eccbc",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T12:34:00.144405+00:00",
      "head": "a0394766e301359684d6365528f10578a7824e5acf938b21482de5aac0bae28d",
      "node": "101.wake",
      "snapshot_digest": "9feecc600fdbabf379b74f2bc55908a6685c1991444b46300b6e5d32ecb3accd",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T12:49:30.182168+00:00",
      "head": "e5dbf6f2f1998b6dedac5889a5ea7ada495f35c07891236cdcabdc19999eed4e",
      "node": "102.wake",
      "snapshot_digest": "f97f364a94662e95f8ec104375b7859957463773dbc105948de0d964080c2e5e",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T12:35:36.218468+00:00",
      "head": "9c792a6062d8bf842f848742ac0ad05e132786a45101762c589142abccbf926b",
      "node": "103.wake",
      "snapshot_digest": "dd4ab60a977bf9c0d8329ecdc45c5e99d60f6ff571cb5c7c529d07419711f415",
      "version": 29
    },
    "200.wake": {
      "generated": "2026-10-29T12:37:23.045290+00:00",
      "head": "24a83c564055a2fce703f57d6ed25894bb1c9cde37693c38c66e5b8ae5e7bf60",
      "node": "200.wake",
      "snapshot_digest": "8b1bca6242c9704b01c8037b8fdc068fade34fbe42e84e55f72aff52334b2270",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T12:44:14.108940+00:00",
      "head": "9f04a7e26ad2e96fe3f054ad3e13d5446b8f91c1626802303895a998fae0bc89",
      "node": "201.wake",
      "snapshot_digest": "cc57b33c8f9d8f7585347230cd8c599e6994b8f3ed42f1bcdf818aa2a793070c",
      "version": 23
    },
    "202.wake": {
      "generated": "2026-10-29T12:51:10.730962+00:00",
      "head": "185e80bad23509a23d899296e9f9442a551bb96665bb3edffc84f01bbe0d69a2",
      "node": "202.wake",
      "snapshot_digest": "413db310d81bd4df11755014ce5f25696b9603822be95cdfe69741a8a6d656ce",
      "version": 31
    },
    "203.wake": {
      "generated": "2026-10-29T12:32:08.435363+00:00",
      "head": "b9e5525f0ea15e73ffc7958081ffbe2c667517b4bce0ba8874434a40cd6b7099",
      "node": "203.wake",
      "snapshot_digest": "3a5057f0f841ad24a6516276e117f93e1c9a5dd6a18825ba43db562bf80ce361",
      "version": 29
    },
    "300.wake": {
      "generated": "2026-10-29T12:46:07.070586+00:00",
      "head": "2eba6962b0e87fbdcb33bb3a7c0ec15e4adba506be4b9ad4d7d2658cc78d1ecf",
      "node": "300.wake",
      "snapshot_digest": "339bb95597d0387b919522c76bec0f5a18b220c8f5c6fd8bf676ebb7c805f8e9",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T12:21:12.134013+00:00",
      "head": "04e41a310cd98f7cfff9de0cf0c69f806d4ce8afd0efa5d58c707355de592859",
      "node": "301.wake",
      "snapshot_digest": "e1af5fd630fab41ce4f249f046c83415ceba27b03c075d863049349d8ce83e70",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T12:40:50.476074+00:00",
      "head": "ae7a6b1ffc8e198ae9311c781c8dae2a43b34f461ce66e489d2a736e6bf6d960",
      "node": "302.wake",
      "snapshot_digest": "29d0fadc4fdfdbbce47f88172b4b43ceafc14a18906eb8f79a6175887c1ebcd3",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T12:26:58.154431+00:00",
      "head": "9bf53e23d7bee3b09ab45989ee03fbe6b97c4140d9e0ac814ecd7fc2745b4c01",
      "node": "303.wake",
      "snapshot_digest": "815b0372adc609853c134f9fe9156feefab466c2c6a4f35a230cc061c0839f8b",
      "version": 24
    }
  },
  "version": 292,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d323835353566363164336266343564/31.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d363030343334313833346638343532/32.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
