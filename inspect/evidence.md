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
  "generated_at": "2026-10-27T13:57:35.048421+00:00",
  "head": "snapshot:a12be83ce8e3be19228575bf4aa4eb2cb7843f6a93e05edb097f3483c4300b75",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T13:55:22.263480+00:00",
      "head": "ed7e893db29693e80d8eb2b4018033b75f998ff320e7616123535acfba215c08",
      "node": "100.wake",
      "snapshot_digest": "7e056e0199c9292b18b585d3e81a541eb3e26d8b5cbf08b0355b3ec5cc1596e1",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-10-27T13:53:34.419835+00:00",
      "head": "d67ad0f9e54597eec6f8d996c09d7b971da09272ebeb9634f1f90bf292e7083a",
      "node": "101.wake",
      "snapshot_digest": "cebead5525b4d91a803bdf1ec2a9267c44c3cfeeebcc1285a7e24c7b1c360d93",
      "version": 4
    },
    "102.wake": {
      "generated": "2026-10-27T13:54:06.154174+00:00",
      "head": "dfda6ee77476799949be111b39f38085397cfb9cbf47cc5ae3792361f98fce6f",
      "node": "102.wake",
      "snapshot_digest": "a3cad2e5a657b6be20c3d68f12ca1f4026874cc6d26d945d8fb3cc4d50ba4b52",
      "version": 5
    },
    "103.wake": {
      "generated": "2026-10-27T13:55:57.729977+00:00",
      "head": "226ca52f7b087a728f53b9b6be3caa755ed5345113f511806824f48d981d2ad8",
      "node": "103.wake",
      "snapshot_digest": "cace45c3eee5163c01ea35c4252f7e3178998aa62fdac93c73b4b46bb1133162",
      "version": 12
    },
    "200.wake": {
      "generated": "2026-10-27T13:54:54.257457+00:00",
      "head": "19e1a316f2432c241c9f5737d3e012b44d77385e02c8174824065ca36d615045",
      "node": "200.wake",
      "snapshot_digest": "ca1b30cbad7cb581555fdf9aa9745ce16d94b25a31a2247b49ed175405f90a17",
      "version": 8
    },
    "201.wake": {
      "generated": "2026-10-27T13:55:07.483887+00:00",
      "head": "c94facbbc9d0eda1a8e5116d06cf24fa08dda5db2dc465453624be14ca6ad6d7",
      "node": "201.wake",
      "snapshot_digest": "4f023b1323e4af26556cd6b99de274d2b237de039b43c336556380e24f24cc3e",
      "version": 8
    },
    "202.wake": {
      "generated": "2026-10-27T13:57:06.384013+00:00",
      "head": "49473b3b25f72ef9073f9f705d799c03bbfb5a389b9ed04faa3817a188a70670",
      "node": "202.wake",
      "snapshot_digest": "885e7f5b9fa8a0a5456301c82c9fd936f3f0d2e3490decca18cc737f2bd6352e",
      "version": 10
    },
    "203.wake": {
      "generated": "2026-10-27T13:57:25.780744+00:00",
      "head": "54b3d37a3fe4e55d7e0fb03125caed22b7619951f37bead130d277676b103a02",
      "node": "203.wake",
      "snapshot_digest": "ab7a6e800a1707455f96c1d3195e3f999bd593d42b6eeaab29386241b315bf57",
      "version": 11
    },
    "300.wake": {
      "generated": "2026-10-27T13:56:24.545837+00:00",
      "head": "8f1b95261d2f0e26281b8ba645394c008a4e5833e9f4948c768974021c57a349",
      "node": "300.wake",
      "snapshot_digest": "f7e53b75eecd9b91940ea0b99812c93cd361c84a49df06c33308294526d102de",
      "version": 10
    },
    "301.wake": {
      "generated": "2026-10-27T13:57:35.048421+00:00",
      "head": "57fc9e13e90c89bd36f015c79a494e413f98dee37659369accd8642fb6fcbc62",
      "node": "301.wake",
      "snapshot_digest": "03e4cdbb156c65cfa014bad2b8ee42c886814f1a0564038800f601270aa3623d",
      "version": 7
    },
    "302.wake": {
      "generated": "2026-10-27T13:56:37.287015+00:00",
      "head": "aca4014822b2149d82791c2c972083fd54fb852e65146e255696e44b68d7dae2",
      "node": "302.wake",
      "snapshot_digest": "45e50893b1bd2fb12b51f5117e3388b040a1380a130fc0f2b241777a7c48d954",
      "version": 9
    },
    "303.wake": {
      "generated": "2026-10-27T13:57:22.737102+00:00",
      "head": "8e58e4ca32b306435e2a8d3fa5fe2e03419bb7492fd4f9c6704111b5d8f3f23a",
      "node": "303.wake",
      "snapshot_digest": "703ab07c45756f46b834ec54f1ec97bbf1cac3cfff8549eeeb8917e8b960e39b",
      "version": 10
    }
  },
  "version": 98,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d32.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d316463336235393261643736346364/63.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d666239373734356235646532343933/62.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d636f6e74696e756974792d7072/6f762d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
