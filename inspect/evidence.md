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
  "generated_at": "2026-10-26T11:37:31.551615+00:00",
  "head": "snapshot:ce4f6761f850b2f524ae7a9d6c17686170b0e9698070b6fb0e9546a7a225be01",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T11:13:53.760964+00:00",
      "head": "10f073764b9646777b89d76826b126c423697c1894650436f8f6152e8282dbe7",
      "node": "100.wake",
      "snapshot_digest": "83832ad8cd7829df0cf9781894328b7b6eeb05313aa888f160c67eef4049b77e",
      "version": 30
    },
    "101.wake": {
      "generated": "2026-10-26T11:36:40.665825+00:00",
      "head": "84c803ea9a1b5edc10e650d9b7706089a1cab01f2e1d9dcb6894f637985f7e4f",
      "node": "101.wake",
      "snapshot_digest": "401aeaeebaa39c5ff3834b737015c40b3d515b03eba987eaa79de037f302ad8c",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T11:34:36.612006+00:00",
      "head": "66a9d01bd3db43b6223434ab6cc3ab316aeaffe8050ee59c53f35c6738b204c7",
      "node": "102.wake",
      "snapshot_digest": "bd1418f43090196cfd0569ccb62cea057af2d496a08df85798ba8a0826f8d5da",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T11:28:11.894158+00:00",
      "head": "2853d1dd2e8a8cdd0acd98deb1f20fdb86b67b376feb2100a6b625fc9f3daa97",
      "node": "103.wake",
      "snapshot_digest": "424d3e77b162ed4582f8df325d92edb4399a44a0b1133a03a47cf64339305842",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T11:36:20.986982+00:00",
      "head": "71ce186e243430e95d0032100f42c3d6545eba87b9b5d566446cfefb9d0a0093",
      "node": "200.wake",
      "snapshot_digest": "3107a03a8dc5c23b120030fb9035a2608965ddd938091883abf09c0e9123ef68",
      "version": 41
    },
    "201.wake": {
      "generated": "2026-10-26T11:12:45.349012+00:00",
      "head": "920b250952dc92ea9484ba3c6d8fef32f5981e31e0270d9d64004c7f6a5f021c",
      "node": "201.wake",
      "snapshot_digest": "5069b1002175fab98ef0e62c94a15254e9fc8de4297f7feef0607ddf797d7d8d",
      "version": 44
    },
    "202.wake": {
      "generated": "2026-10-26T11:37:31.551615+00:00",
      "head": "5be2acb74eef0c1f75a664533d53b54fc5ee698c106096df51cdb0550e60992a",
      "node": "202.wake",
      "snapshot_digest": "8690b1cc2c7c257175301747959e10b4a00dca68038b6c9f8a93e14c4bdb2e7e",
      "version": 58
    },
    "203.wake": {
      "generated": "2026-10-26T11:08:54.800934+00:00",
      "head": "20abc2c2ddc90a4a99e778d339ba2be05f065441badbb79ae619d2278e1861d3",
      "node": "203.wake",
      "snapshot_digest": "0032bdd5cc6c095a2c37ee3b0a614a660f791fab2c961066e3c97e8600d92264",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-26T11:17:21.000510+00:00",
      "head": "b2873b44442ee9bf55eeab7dafaf8a6d8f0d8e9f328494d92dbc64d5e8b43d00",
      "node": "300.wake",
      "snapshot_digest": "1576b4e263258d5939ee951195c04d18512d76ecbdfa59b448f4125a1c0d11c6",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T11:16:06.075520+00:00",
      "head": "89df7239003be0c722bc5319383bbdf4ef421735b623d9537032cacbf6e24557",
      "node": "301.wake",
      "snapshot_digest": "8f1bdb4f2232ded33b7d8d7a7cc638cb88cfddd32d4de672a331817adb935eea",
      "version": 63
    },
    "302.wake": {
      "generated": "2026-10-26T11:11:34.823820+00:00",
      "head": "f9d7f5d99bba1d0c9796058f8123cb226fb6bc14c0f920fdd5d7224d5933a494",
      "node": "302.wake",
      "snapshot_digest": "77121c18038c65118a490ddd2d6054412cab736bff023c01e126fbf97aaa9a31",
      "version": 47
    },
    "303.wake": {
      "generated": "2026-10-26T11:15:47.103490+00:00",
      "head": "fcb2b164018d1527b116b0a1c0194fd8a9ae7f93f3aa3852b651781a6d9fb1eb",
      "node": "303.wake",
      "snapshot_digest": "b62e7b383089a7213d73b84f3364c80d04d9879c83bf42d717cd3cb4789b02ef",
      "version": 56
    }
  },
  "version": 566,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d36636564643330303465313634353531.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d356337666639356364393636343930/61.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
