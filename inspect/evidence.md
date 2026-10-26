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
  "generated_at": "2026-10-26T12:00:13.998807+00:00",
  "head": "snapshot:584087bf897bff0cf8b3a0f0ed2da8096db0e7d42cd81fd8afd4a583fe4c8aa7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T11:48:00.259502+00:00",
      "head": "18619834e7b32f7bd940d8e0cd7a64dc485efe85aa874a8e34e155c11636392c",
      "node": "100.wake",
      "snapshot_digest": "cf835f52808f60195d682728ae7c2f8aa675f8c73760763a8d6305e1d64a2014",
      "version": 31
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
      "generated": "2026-10-26T12:00:13.998807+00:00",
      "head": "31309ce195f518b55063ecb8df287f672098ddb2e78b11af0cd1a8612ea7ddb1",
      "node": "103.wake",
      "snapshot_digest": "746ff2c8d8c4bde11545611a874f178bdbe136942902e38451c45125d46ffc79",
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
      "generated": "2026-10-26T11:47:42.924260+00:00",
      "head": "6b87319db0ed764d57fedc4925edf1cd3819e05b4ecc5e075950b899e88a49b7",
      "node": "201.wake",
      "snapshot_digest": "d47bf646c905241606391a80879a6c07e0d17d910683281d4db800a2cb60d810",
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
      "generated": "2026-10-26T11:39:48.926953+00:00",
      "head": "ae715a3ad9d45c9e3f47cac0a2401afb7ae88e052c07707d09c106485bf2136c",
      "node": "203.wake",
      "snapshot_digest": "bfeaeb03846f6fbc8cab16a4e0e8624f4d22c9560f598ead97ea8f493ebb108a",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T11:53:55.598201+00:00",
      "head": "bff7ba5b8e88af54bafc7eeb05aa50dcfebe6814e622a4a0d7161e24e95988ad",
      "node": "300.wake",
      "snapshot_digest": "6047bd39f789bad846277abc39dc18f46a7e4832fd3b20b4e2d68492aa8ab484",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T11:51:23.841919+00:00",
      "head": "71622776d4113f9d6f282e81e3c98662dcd97b7121f3476bab62cc091158a34f",
      "node": "301.wake",
      "snapshot_digest": "61fb4fa44fe0bee1090dac46b24359efa30b202bc14fc42120d5302919afa3d8",
      "version": 63
    },
    "302.wake": {
      "generated": "2026-10-26T11:46:28.259845+00:00",
      "head": "2396968b2b3b1e2a65aac9767eaf54597a0edc87e19c48240f56dff7fc1d0117",
      "node": "302.wake",
      "snapshot_digest": "acea93f14edda60699dd64b1571973c5df252c2704a3741f62270d85aa66fe65",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T11:49:46.666491+00:00",
      "head": "df65afc68b9313aa736178b0045ca5937e8ae086dff71344060617a6aa381f0b",
      "node": "303.wake",
      "snapshot_digest": "da34d08abe2ff18a30dbf92823c4d457498bbbaecc824c26134d6841e19d95aa",
      "version": 56
    }
  },
  "version": 569,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d66623639336166313766636134313830.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d346235346561343032383133346138/65.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
