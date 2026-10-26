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
  "generated_at": "2026-10-26T09:35:37.742520+00:00",
  "head": "snapshot:6b6341d2677ea769c31df2554c2d58ef9ad54aca98a4ae6a08980365d6b9713c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T09:10:56.788062+00:00",
      "head": "73fdb228eef0b88811b1ae505cafa632f9bae5bcaabb832660d31193b874d66e",
      "node": "100.wake",
      "snapshot_digest": "c6d4816a0581c232e222481cebddefa9ce08873ab028479a90b6e5b60e97688e",
      "version": 30
    },
    "101.wake": {
      "generated": "2026-10-26T09:35:37.742520+00:00",
      "head": "1dc30a9fd6902d0a0b57d39bffc3deaf730acdbd972753e2a3eea53a09b7c195",
      "node": "101.wake",
      "snapshot_digest": "8cd0ca39767e37c8998f10748127811db1b7d428b25e33ec7adbe72469cb885f",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T09:35:02.685017+00:00",
      "head": "c88def4ffb2559a1b623c1f34a4420a320b152a749387f9e2e47eed2ed6ad18e",
      "node": "102.wake",
      "snapshot_digest": "00c551a0728e5bcdee43da8f0e0401a3edbe7c2f5e74d124eeed58e6ddbf5415",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T09:15:18.025353+00:00",
      "head": "773b1bf4e0bc674a908a992007a72f7381604f8d0d90ab3747bbbdfd7010882a",
      "node": "103.wake",
      "snapshot_digest": "9ead2ba6563f5daccea6d3b93f3b0371cd2544ba483204ff802f2e9aa925b2b6",
      "version": 44
    },
    "200.wake": {
      "generated": "2026-10-26T09:09:01.777059+00:00",
      "head": "626716f170dd3553dd59963eb48c182e294d6f40fbbefae6c077d65d91c30250",
      "node": "200.wake",
      "snapshot_digest": "b372a29183962bf9b2592ef102bd6424b24c7889c4b27a69cbe93d6779ea3744",
      "version": 40
    },
    "201.wake": {
      "generated": "2026-10-26T09:18:16.108331+00:00",
      "head": "c0c4f819ec08e62728f8f12d268f269e9b49032cc919d42dfd4d363b311465e0",
      "node": "201.wake",
      "snapshot_digest": "0918178540b24244ab992ffd51417f0de3a70716e0904f3b5b9f20f430c9496a",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T09:16:13.747115+00:00",
      "head": "f1e8901d72002d09cf2b50b2986a4973e38d252f96970b4043625765a9488712",
      "node": "202.wake",
      "snapshot_digest": "a813d495f5c724496e53ed355ae8e07cfa5d8f104744a3d2f580dd5fe5c844be",
      "version": 57
    },
    "203.wake": {
      "generated": "2026-10-26T09:07:00.873846+00:00",
      "head": "0b6ccecddafdb709ab69fc6dba141572475476a001d6ae42fdabc641087fedb0",
      "node": "203.wake",
      "snapshot_digest": "fd6505586dcbcf3f99d18d6be8402f610545107cb86f9293110934c166fe0aa6",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-26T09:24:36.011506+00:00",
      "head": "d4c3fd1deeceacac76e81fbc62d7255904725f7f64594156ce021b15ffbac780",
      "node": "300.wake",
      "snapshot_digest": "f56c84b08166defcdd21ee49abd7ba22bd0c3322314f19053fad0e0824aa96de",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T09:22:36.797286+00:00",
      "head": "9f3b55a55542f33882c2794f5c7f86bd4eb46b9b868e855b394fcf0170c6d7b8",
      "node": "301.wake",
      "snapshot_digest": "c6eafd65a70789e4c9fb1b190621ee03ca653a8490427a8ee879400e77e28598",
      "version": 61
    },
    "302.wake": {
      "generated": "2026-10-26T09:14:25.867425+00:00",
      "head": "25aa0b14bddd096d436881d8dbc22000164f5f176a7e528c630dae9302afbb99",
      "node": "302.wake",
      "snapshot_digest": "d4ac64383dda1d7e1f80b2b570122bd2d35967d03758ceb79bbb3db787b9d89c",
      "version": 46
    },
    "303.wake": {
      "generated": "2026-10-26T09:09:58.426761+00:00",
      "head": "617336146a9a19fe3e0d39d13d06ff41dff8f6df0f950a601ea8a7d741792b47",
      "node": "303.wake",
      "snapshot_digest": "e18fe2be7ee6f59589adbeb7bafce826c5b27a8297666f0d0b25d22fae42fcef",
      "version": 55
    }
  },
  "version": 558,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d616530376331336530373030346235/38.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36386630616265303664373934333232.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
