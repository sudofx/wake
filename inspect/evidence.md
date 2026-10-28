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
  "generated_at": "2026-10-28T22:55:35.685552+00:00",
  "head": "snapshot:5a93ef4b8e88029f402170b1295aa43b0b54c437c970d107f1430a6ab6292d02",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T22:54:11.598647+00:00",
      "head": "86fb081d4f4f3895e0ce8ad65c4b2ee351e57e90718925a0611618fcca0ef13a",
      "node": "100.wake",
      "snapshot_digest": "e889b9f4b7328eda9cd5a7c1e4b745a02fb6fdfb82b73f5af6d6f42425b977f8",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T22:52:57.369331+00:00",
      "head": "e3fbdbfcb54cc62449a5a42a0c468f79ab58ff6df1f8ba64204e0fba76bc4947",
      "node": "101.wake",
      "snapshot_digest": "691c78adb8592ae5b38734a78b786615dbbb6c2f1a5538b4db2168ab9713b90e",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T22:53:15.662377+00:00",
      "head": "ba6356e833ed05139f95e9de7b1da61fd38baf7949bf4b718831bd0ddffb4c4a",
      "node": "102.wake",
      "snapshot_digest": "95d359f00f7b55ccdee88908b9a8306b519d71a10febb4c0f95e3e44508a4256",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T22:53:41.840226+00:00",
      "head": "bd0cc9c087086a8fcf098dae379b1c679d75c9b4a75f2870d478d5ec0f894447",
      "node": "103.wake",
      "snapshot_digest": "dd693becaf22fbcb82f59a6e7c3b23c2c2da916713c56418d26e686967737472",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T22:53:46.839136+00:00",
      "head": "83049f2330af6b5f37f93e3a862dc7e19f9acdedbb8140e4b46117cd5717f433",
      "node": "200.wake",
      "snapshot_digest": "e28408670666fd3e0c072bab79a34aea3ced254a5440a22516dfb6cea7c27fdf",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T22:54:46.819879+00:00",
      "head": "618f3937992a6c4b50365a14e72b73947eff94014353503b34a62a98260db816",
      "node": "201.wake",
      "snapshot_digest": "55135e1d8e8a95e463847b2931c9ad0b93dbeb1582b9a86eed5421287de57459",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T22:53:23.008145+00:00",
      "head": "a445321fdf40e9cbd97ec7df493d4fb09bf63ed08b809c4988b0d9b22b43117b",
      "node": "202.wake",
      "snapshot_digest": "6a0256461a9fcd9491b8680ec4a99604ff5d1536d10573e7cbf7c016702e3dbd",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T22:52:13.283876+00:00",
      "head": "720e9050c95f65d5f61b992d0e052fb1246bb61791539bcb7540b31d2976aac9",
      "node": "203.wake",
      "snapshot_digest": "726b03e83f2cb4b489a10c8b2e537a21d4b6e99e5ee6819fba76cf135c1343b5",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T22:53:10.478239+00:00",
      "head": "0417fb15a65e7e6c0b61ba80b7d9dc28a34f6cbe47ac16f64c65d9a62b6b7052",
      "node": "300.wake",
      "snapshot_digest": "b4ad414d24390aa7407f363d2deeec89e75ca842f0a8da8c06eb367c1060dd52",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T22:55:35.685552+00:00",
      "head": "f9df07c1131c50c8181737bd71de311cd68380cec5d6f42a8deed1c2d0368253",
      "node": "301.wake",
      "snapshot_digest": "13a5481b574bac5243bc27f2e0ee894d4d2c8656c1b2b136c0b7b5a4114497c4",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T22:54:34.916307+00:00",
      "head": "b2e70159f7c1f7805b7b3c0ff3a227fcffa6bd59d1a2ed70f2482348bee28c22",
      "node": "302.wake",
      "snapshot_digest": "35708f264b96c1da1266c6b61a13c25554a70737bd070f5b657d6820c0cadd7e",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T22:52:56.442729+00:00",
      "head": "e76cf89be94789af24ba56e31b62a883aeac915aeccfd96d2ba733ae54faf83b",
      "node": "303.wake",
      "snapshot_digest": "90c55698d097c5a42630c77b2e06f5dfcb2bc5f52be182ec9398720a4f8a1bba",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d65613532346265373761353734313639.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d36306264343463636331383234666331.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
