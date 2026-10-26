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
  "generated_at": "2026-10-26T20:33:29.600371+00:00",
  "head": "snapshot:6fc0c10d174b9e1d19a74e9c4848d3d962f39c60194b797e50ccb24ef7528b61",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T20:31:32.700168+00:00",
      "head": "808437fb31a73673a18d9a5209f5a94ade3118f2f6cd44c9a3db3cc1c34aae68",
      "node": "100.wake",
      "snapshot_digest": "be6ebcb8fc19341ec1688c3b4c57375f9723dab37b2b2654c0073e3b752ab2c6",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T20:14:39.150532+00:00",
      "head": "e0d1232d2a0388fd301bc77b7a997cc622a02141bbed8041139bf923ffbdb913",
      "node": "101.wake",
      "snapshot_digest": "57d06b2fc5c26da541fb089507cc24329632d418e87b7387a3f18cfaabd4c72d",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T20:25:19.790088+00:00",
      "head": "82edf18a1a0b23b19218b8ba9379b297bf6968ab8c82bbf33ae4104d8d120ec1",
      "node": "102.wake",
      "snapshot_digest": "5deb814d1619d4d9fa0c97e9bcf0568b54f3fe0e992daf25affda4475cb05710",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T20:32:47.676550+00:00",
      "head": "43edd317361340807af89a256387d0e58f94ae27e90d857f7ee80d295dcb5081",
      "node": "103.wake",
      "snapshot_digest": "9820ac79903ed85b745d8b2f2455cf8ed963e865dc89890c2280e63b29a2ee38",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T20:31:14.723598+00:00",
      "head": "6796c3649c713cab5225e3de161175c95592d126f0fbdd64ae1c3d8c7d2a1321",
      "node": "200.wake",
      "snapshot_digest": "5cb179a095d48efaeccfe621dd32ac4ca8b0b2fa5043b703380f51a45306d8f9",
      "version": 45
    },
    "201.wake": {
      "generated": "2026-10-26T20:26:12.207515+00:00",
      "head": "a0302077ae86497ada0558f47da0301c660c4758c16f3d6fac7de64e5be9f199",
      "node": "201.wake",
      "snapshot_digest": "ed62e818513de6e4b41f4f494681e49196df076e24db9f41727b7a543f352baa",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-26T20:31:51.181434+00:00",
      "head": "0b7b912df1bc40dfb65985e8528c001d417da4839a3300bee35b2d0c8f43b39f",
      "node": "202.wake",
      "snapshot_digest": "31a1d3468fa69a439ac35ba239d90763217b77d2f6d3234701768706db86e719",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T20:25:35.298317+00:00",
      "head": "e1135b24b6a7e52e4e66077837f5d94d0a1b4e5a45d94038cf59826cefa0660e",
      "node": "203.wake",
      "snapshot_digest": "f1fab74d5d4e3c75c3905f560699185a8432a8650a178e7fb278380644284699",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T20:10:32.408185+00:00",
      "head": "2f5d55e82e911962054746cf905c58cb38acb732c64855b1c8e50b8dfa809f5c",
      "node": "300.wake",
      "snapshot_digest": "8a22329b92d6516d58ae70e91d6d026aec875d53f08298f9e8854add8632a525",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T20:33:29.600371+00:00",
      "head": "747c15b92a7cd85b5f22e0dae16795f5bd34967728b7166483c62f2836b963ac",
      "node": "301.wake",
      "snapshot_digest": "254db7d19fc0358dc8c5171dfedc1a2e2e44a098c943f11982a1c2c6702fb9c9",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T20:08:40.798449+00:00",
      "head": "d853b1b72766b8c3d98ecb050d48d3781dbcebee0dbcb05eee1d6fb27545e6fa",
      "node": "302.wake",
      "snapshot_digest": "2bc8f18d8062e5b710f5264683de86fda94fa48a49f7626464488ef40a62a638",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T20:29:33.420056+00:00",
      "head": "4ef0ef71cfb3ed2ad65b9166e10177916aec3ee40730d1f7cb27bae8bc6521a0",
      "node": "303.wake",
      "snapshot_digest": "de0222edb4c92dd1368dbbce97839f82946e9e33370f22373c076227a52b60d2",
      "version": 56
    }
  },
  "version": 579,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d36613734383963636636643734306331.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d633232353330363039633934346436/31.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
