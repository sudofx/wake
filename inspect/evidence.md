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
  "generated_at": "2026-10-24T07:01:04.672541+00:00",
  "head": "snapshot:1d580fd0fd4d38aa09b7984b559e0ecb3712a8b87258f907eb6f5335ce8ab72a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T06:56:50.825192+00:00",
      "head": "597e173b0a397e29dbccb2f6c9ab2dfdbf414d6cb686519a4d4aaa16146d9bd1",
      "node": "100.wake",
      "snapshot_digest": "59c9f7a4a6549adcad5674f0a8dbe9dc6e699ee5bf8f2ee857a6a122b7022d79",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-24T04:54:47.889330+00:00",
      "head": "bcfdd4af91658db4397b9a195dfd91af0aec963c770bf3c845f68049dbc80149",
      "node": "101.wake",
      "snapshot_digest": "40a3bf6e0b11e8d6b00520754dda29061f23f2f8b8bd234a9d26d7402e7cf729",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-24T04:54:47.072044+00:00",
      "head": "cc13edbbb74a7291785b364f4a243bfce834515b76f7666c08e301395ead7202",
      "node": "102.wake",
      "snapshot_digest": "82fd861e6a7b87afd13dfaf8db917d0c4db8e6951baaf5bb7404ae183011dbd5",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-24T04:54:48.832662+00:00",
      "head": "981c2ea9925cb14624439b9bea2c667defccdb8b3c33704225c7bae2a709e755",
      "node": "103.wake",
      "snapshot_digest": "b31460603921fa1982532c0350e3b80c2d9a9a2ab341686ef2dd216bdbd4998f",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-24T04:54:48.342207+00:00",
      "head": "47156d943d257929ca0600be1e9bc7e4631fa236dbca711ee5b52391266185ea",
      "node": "200.wake",
      "snapshot_digest": "d45777ba398e737a8110d1baa436dd354a5814a121b0762275d532c34674ce43",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T04:54:48.716992+00:00",
      "head": "0cfe4e97ea00626c5c5d8473b3e534f0511bb5dd7c74da157b4226d126456186",
      "node": "201.wake",
      "snapshot_digest": "d4c9488beb506d08a31e5f75542ab3d30872fee59cb0fdfaa156726b0754f1e6",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-24T04:54:48.456575+00:00",
      "head": "7cd62ac3281dbccb279d7af2144efd3fb09dea1c5c7f17fd22fd67951095420e",
      "node": "202.wake",
      "snapshot_digest": "8c8e66bfe7d8946e4e756d556fadc1e00fbb68f43727ac48ab0bab81c6b8fb6a",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-24T04:54:48.176484+00:00",
      "head": "537cb8b1e60836fbd98e7dce5bc2b767e888f5df10a25cab81d0f155c83eba59",
      "node": "203.wake",
      "snapshot_digest": "b0eb07fec2d144bf923ff2ac73edfa2c6352d8bbca4089f64c69960727d1e067",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T04:54:48.287939+00:00",
      "head": "8c2952a63312d98f514072b874c19c2a73f8f3b8e60b6a57580d5e2d7f5ed619",
      "node": "300.wake",
      "snapshot_digest": "c210e9c695370c1059b1da6a23f8121402533cc425d0101f179b94aca548532a",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-24T07:01:04.672541+00:00",
      "head": "d358f33a84152b66df12d2b9bfce12dde8c78c1ac6041359cb8cb75b32f7e6dc",
      "node": "301.wake",
      "snapshot_digest": "0f4fce159b02ff25cc6967f724a69977f1a1b94a9e56d50fc62d323dfe875e39",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T04:54:47.355738+00:00",
      "head": "71a0cafd0eb552fba396d5c8396bb5d1867769ea0d1bd76bc953dc986a9c777e",
      "node": "302.wake",
      "snapshot_digest": "20b94af272bd4cdcdc8661a3eabd6b2e7f0e868cb91ea1b6f30c59c6f74af066",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-24T04:54:47.898576+00:00",
      "head": "451b574fe139ed6993e0d653689ac52b3dc215014cccc194cf159ab1e54c49ca",
      "node": "303.wake",
      "snapshot_digest": "5b2f2cf352c149785160505aacaf856a5a7fb394c41c34e868cfd252fd5e6fd4",
      "version": 36
    }
  },
  "version": 337,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a722d64383561663633336561373234356463.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61323233316364356162356434636665.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
