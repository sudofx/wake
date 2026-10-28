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
  "generated_at": "2026-10-28T10:22:38.128080+00:00",
  "head": "snapshot:acb447bf44b6421fae04ee25bab8e1399a8773414b4cc0bd3a1788b19101cdd7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T10:20:31.313511+00:00",
      "head": "16b8fdfdb1d86b23dbdd9cda12e442ead6ab12846b765da1bf93e411596fd078",
      "node": "100.wake",
      "snapshot_digest": "38d042e4b3a1cbd6b0e5f8dc267fcc6db737a52ccfd3053910186cd1293edfdc",
      "version": 12
    },
    "101.wake": {
      "generated": "2026-10-28T10:18:41.499075+00:00",
      "head": "eaaf45df25c5f30d70b64fb2e12ad71922e996ee1bf134361d514be9e6d852a4",
      "node": "101.wake",
      "snapshot_digest": "1a658624ca84534350effd7c4585ce6d09c214d272303e60ca08293e7a9c22dc",
      "version": 15
    },
    "102.wake": {
      "generated": "2026-10-28T10:18:18.181888+00:00",
      "head": "893ffc546bc5953abef902de27e99252b6800e939981393034cc94b5b4d1540c",
      "node": "102.wake",
      "snapshot_digest": "2800eebf497b5d0b8bc0655df55aa521ba80289744c268632d7fa81071db6db4",
      "version": 9
    },
    "103.wake": {
      "generated": "2026-10-28T10:20:31.480623+00:00",
      "head": "46fc91e885f2b35325be95659c3765fcfff01d10f91ac968f3c22398c4fbc973",
      "node": "103.wake",
      "snapshot_digest": "f7c9acebb4199ea536c474f8bb6a4e068f72c21da2a521a5a2e40e27c241e871",
      "version": 24
    },
    "200.wake": {
      "generated": "2026-10-28T10:20:21.312591+00:00",
      "head": "4745c4cef66bdfc8a9d2a900cdb38826cffc43589b243a8cf467f121e8a1abd0",
      "node": "200.wake",
      "snapshot_digest": "0cf2a2f888bbce150b6a67fbd5d3815925dc4c3e24409c9c30bd270d1ca9deed",
      "version": 18
    },
    "201.wake": {
      "generated": "2026-10-28T10:21:19.429953+00:00",
      "head": "2927ff7bd93b390409db122221ec1a7a76864a7928c4612c024f6899dd36c8fd",
      "node": "201.wake",
      "snapshot_digest": "6f634280a1e1d2793050b8a7169b22500e7c29d5cf32f070e6d57db148ae5763",
      "version": 16
    },
    "202.wake": {
      "generated": "2026-10-28T10:18:58.663598+00:00",
      "head": "39cbf7e0ab97f571161f1dd7f7145c517ca4f4e6f73ade81e1bd319482ee7b64",
      "node": "202.wake",
      "snapshot_digest": "10fe697a78b879e5bdd4babd47eee4f2a27d59acb18f8912d8c9e0911134fdfb",
      "version": 19
    },
    "203.wake": {
      "generated": "2026-10-28T10:18:33.304859+00:00",
      "head": "f0b20c59761ba76640e35d37aaddfcdb3a9be1738551a92716572ff86e8121a6",
      "node": "203.wake",
      "snapshot_digest": "93001ee989858779fef28edca7b2798b0b6c6c7e6f936ae7458fcb34cfd500f9",
      "version": 21
    },
    "300.wake": {
      "generated": "2026-10-28T10:19:15.912503+00:00",
      "head": "a4645931018cf16abbd472cadbb9c6ba0a237b293f712f7c36db02010babc2a0",
      "node": "300.wake",
      "snapshot_digest": "d6074404c8086a4e1baf9b2b746942a34d5f72f662a2cd1e3062e5e64e9af6ab",
      "version": 18
    },
    "301.wake": {
      "generated": "2026-10-28T10:08:09.922930+00:00",
      "head": "3f4669d6b5be1e310f3ecd9b01fefb2fc00a6e22a1325d54cad532cdb5ef0a15",
      "node": "301.wake",
      "snapshot_digest": "49ca708dcace9c294646f3cfc300eec5ff97a5ea12ecacf675fcb9e0b40fe3a8",
      "version": 13
    },
    "302.wake": {
      "generated": "2026-10-28T10:22:38.128080+00:00",
      "head": "1b1bef51c3082752ffbb1a9674622c29577154d0e0eda77d8183b6e1b1c7832e",
      "node": "302.wake",
      "snapshot_digest": "309c76cddb071183c1e11b3408cf881bed293eb6e9eb4096c8fdc1cad6bd265f",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-28T10:19:57.747645+00:00",
      "head": "de641f69edd0cbbd36a38b11e7bb13c332d27a4ef09a0627fe1d0df7b72487dc",
      "node": "303.wake",
      "snapshot_digest": "18c54c7344322bfccf57eae1e593cbf172b262c69791603473cb6f43d9714c7a",
      "version": 18
    }
  },
  "version": 195,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d343661366364643531396364343966/36.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d31356662313638363439616634336338.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
