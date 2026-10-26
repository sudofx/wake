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
  "generated_at": "2026-10-26T19:54:33.955973+00:00",
  "head": "snapshot:2533f12815c19fcf5fedbc2f1371c160345bbf0a2a52c852595c625c16c1103c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T19:31:42.960944+00:00",
      "head": "132d4d1bbb5484423a2420490810ce673e4a160e00d06729d03a05af35bf1a6a",
      "node": "100.wake",
      "snapshot_digest": "a38f7e403b31c22f3a5646a1a2053359d90c381b749795f8b6ab1c06d3c20245",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T19:31:45.421795+00:00",
      "head": "a79e6b5edc7648ff28047b5c26dab75fad2e1aacaa86f56ef81a3179865b9a15",
      "node": "101.wake",
      "snapshot_digest": "85e3d232733f5dd2df66de89bb33d6dde8b604493b55b0e04ca42d6d664e40f2",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T19:50:03.376976+00:00",
      "head": "1f4fab760693f7097a57cfa2265296147d287e2b1099ff01621f47416d248864",
      "node": "102.wake",
      "snapshot_digest": "72b4c6703fcd1e794f04923925ee00efe3aee2b57df098a4ade8dfc2043c388e",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T19:54:09.203776+00:00",
      "head": "230282e52375a88c93aec4a8f3dbee1ca5f680eff89c5f4089af228ffae485d0",
      "node": "103.wake",
      "snapshot_digest": "d8d6b46f93aad4addacdadeb80de5c8d8c5635a56c5ae1ed5e04296aaa5853ed",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T19:52:47.094938+00:00",
      "head": "ac6a85922363d6607bcae397d4272f1f777c9f483642e06990ba8751b85342dd",
      "node": "200.wake",
      "snapshot_digest": "00f10911ebca45c499b56f74ca06acdac97324c8b7759376da428db9cee682cf",
      "version": 44
    },
    "201.wake": {
      "generated": "2026-10-26T19:31:45.030143+00:00",
      "head": "ecaa76092c19da46dcd44018f5349434c6fcec73f8fdf2469fa580217d64636b",
      "node": "201.wake",
      "snapshot_digest": "3210b7ae18608452e5ade8d0b3ff8286341ad3ef30eefad2f79a0139bf597f2b",
      "version": 45
    },
    "202.wake": {
      "generated": "2026-10-26T19:53:05.211169+00:00",
      "head": "58a9165e8b9463ce21f6ece2897c2049c3f82c8efc6f6fc7a41784108f9427e2",
      "node": "202.wake",
      "snapshot_digest": "1a25925ec2351082e73bddbb54773fc591c3385ba9ca8b6f1e8079df665267c0",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T19:50:36.176814+00:00",
      "head": "c9de9133ea4025489c8ebf4e0fe61164e9806aaf7d0e6b482f9f79419614c799",
      "node": "203.wake",
      "snapshot_digest": "c3ebd61bb2a3e17d52fbeb9588e7a1c8e83d4009a1bd90d29eb53b8026bc1fba",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T19:52:04.905763+00:00",
      "head": "25e2bc7fb11422c22fdc982ce7089e56f7b02e72c360604f1467b14f225c1513",
      "node": "300.wake",
      "snapshot_digest": "938df48813e9b780fdbb66c6d8354911b5b7b4f93e2d8daa0a83352d001177d8",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T19:54:33.955973+00:00",
      "head": "7c1e1561baa3165896d9338c320ef1f0e68f2a6d102455aa7f6d2efd839fba83",
      "node": "301.wake",
      "snapshot_digest": "b85ad63c2621fed2ac9ef3a951fb6761903fa8405bca1544102fe01868caba90",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T19:31:44.537226+00:00",
      "head": "96fdc2af7f2a7e33f075b39a58ec56057f8e17c35bf3d568d4e5432bbc60411c",
      "node": "302.wake",
      "snapshot_digest": "abdd6d479dae976f632df7dcecf20127090065f6b2c8fa5826b400d7fc2e14b3",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T19:52:25.831051+00:00",
      "head": "a6a96f8c058f000f59c262f05be769962204bc612b27afab86eca73d53f07513",
      "node": "303.wake",
      "snapshot_digest": "97906bcf6345679d67a4a971bb62bf43b697242b3bf68701c7783c644c94707e",
      "version": 56
    }
  },
  "version": 577,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d34343763646331626632643934643664.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d39663337383463363532623034623961.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
