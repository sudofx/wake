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
  "generated_at": "2026-10-27T00:47:44.880796+00:00",
  "head": "snapshot:b018700720c6830c1c81f12861bdab7ed8fb46aa2fbff61cc85620a5cb5acb05",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T00:47:36.604047+00:00",
      "head": "cfe9c010efa4c6320ae9eb46acd79990d3ef84df4bf334b3fe3d912e7e95c790",
      "node": "100.wake",
      "snapshot_digest": "cfc6c371d15dc8c05c6bdca7573d000ff47ce35ee45fade594293c1c857d96bd",
      "version": 32
    },
    "101.wake": {
      "generated": "2026-10-27T00:47:37.793590+00:00",
      "head": "81b4b5ed3fabcfdeef3dd3d80cab0a09b721a565b134db3a489e063a183197ff",
      "node": "101.wake",
      "snapshot_digest": "de64a4e256d873c9ad803d1c0066b263ddc97b502ce93b9088630815ea3939e8",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-27T00:47:44.880796+00:00",
      "head": "ab35a356067a2e88e783edaf58fc76cf7a24abf92d453353bdd4dcb3125a5575",
      "node": "102.wake",
      "snapshot_digest": "9c4bcef200b3e5c25e2546627a5baf73798975d2ab105d8f057a0ebb472783be",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-27T00:47:39.824033+00:00",
      "head": "ad4a4afc3c1a0e4fa51b50e6bfd66cc02766ff28edbb9911a9ff9077004d0edb",
      "node": "103.wake",
      "snapshot_digest": "da87fbb347f5d733eb30f2ef54ab7f8b100bdc15434b7427a0a80cbe4074afba",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-27T00:47:37.884249+00:00",
      "head": "4d1313962596322557c484a9d93439c81b9425ccc60dd15d729c35aa65f34997",
      "node": "200.wake",
      "snapshot_digest": "8cac76eef9c03cc5e1fe3794040668b36161ef4803a103cf614675a64ab01b94",
      "version": 46
    },
    "201.wake": {
      "generated": "2026-10-27T00:47:38.043845+00:00",
      "head": "f81a03bc10843119339a674421cf2957bd44747e0284a2b3c1e371505b8ee016",
      "node": "201.wake",
      "snapshot_digest": "ddf69df542648f85faed4360c2e8e07542f20b91acfcdb1705c736e92b99cec6",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-27T00:47:40.520150+00:00",
      "head": "fa442c2dd6d203236a3149941958e29dfdf19c219f291a190b0e3da14927039b",
      "node": "202.wake",
      "snapshot_digest": "d017c828c34791a8170e1f4aad8b17d8620e45b0cbfddc991c03b2951dcd3c23",
      "version": 60
    },
    "203.wake": {
      "generated": "2026-10-27T00:47:37.748325+00:00",
      "head": "17992076c1b1918e5e47c93d77fd3a87ce1f515c4a536896f2ad467f5e405934",
      "node": "203.wake",
      "snapshot_digest": "a1a6f7be97059be2f34aa9819a5d49a3d22b7f7b7f5e27f07df6f528690e2029",
      "version": 37
    },
    "300.wake": {
      "generated": "2026-10-27T00:47:37.026458+00:00",
      "head": "d29ad3f22ed86090098c227deefd05b63381b05622ccdfebfc10a04c8109405a",
      "node": "300.wake",
      "snapshot_digest": "7d323209e5ad82b99585022c156f49c815a0d57666e8c0e7430ce77542b8cafa",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-27T00:47:42.667448+00:00",
      "head": "04741588ebf2ae7b79b937b1febdfd67491ff426599e3e21520c3042774fe570",
      "node": "301.wake",
      "snapshot_digest": "8202549f7378467a010033c860c59c8f394d89dbcb9fabd7a1b7afa14dfca997",
      "version": 67
    },
    "302.wake": {
      "generated": "2026-10-27T00:47:38.854375+00:00",
      "head": "78de098ab8c3fd93845913654acfec98ab5ec08dd7dc1c4533acb2fe559e8968",
      "node": "302.wake",
      "snapshot_digest": "d5c06acc92fb429ac5cdcc8d59f6b13760805e43a580cb0a330692be01981b46",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-27T00:47:41.023094+00:00",
      "head": "aa2447c9b58386840eaa108f1b6aca4a5528d5a73db572d597eb9ee48a2f6142",
      "node": "303.wake",
      "snapshot_digest": "f5013f4d46e57ff70ca6e92800eb4dde7c058e5b909b354b21789b3fc6ec1275",
      "version": 57
    }
  },
  "version": 587,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61356561633235313032343434353437.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33623839353635666265643434303164.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
