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
  "generated_at": "2026-10-27T11:30:04.237739+00:00",
  "head": "snapshot:bb806f127f1485ae6366f923539b3c98728a021b52c049c5d59c443ef4230b6a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T11:29:53.726716+00:00",
      "head": "79a5c6681abeff6dbca7e3442c4a37d6f591999bed3db56c2e4cc7cba71d1862",
      "node": "100.wake",
      "snapshot_digest": "1a45bfaba2591e36b1eb89c57a03177e72e40f598ec226b8e184328a9a448aee",
      "version": 34
    },
    "101.wake": {
      "generated": "2026-10-27T11:29:57.252808+00:00",
      "head": "2df77c5a2c47f777f63a167379a9eef9c6fda351d10397c25b79304a0929d478",
      "node": "101.wake",
      "snapshot_digest": "7875446f4f89ac96addee680ed2785727eeb5ecd17822239ae918f882dc71321",
      "version": 50
    },
    "102.wake": {
      "generated": "2026-10-27T11:29:57.837665+00:00",
      "head": "2d1f7a96452ed682a1c8a8c189bec5b3be823e4bcceabc36ebf3c0965dd13c30",
      "node": "102.wake",
      "snapshot_digest": "0e0c33ad14cf548b0bf4cfc53bced78f836835bac5ee5e7c93d4aaadbfa54cb1",
      "version": 64
    },
    "103.wake": {
      "generated": "2026-10-27T11:29:58.781717+00:00",
      "head": "e5f25b93ee444326afbc47f9ac3c1cbebffde20f5cbecbf164eb258b918a6e35",
      "node": "103.wake",
      "snapshot_digest": "0cd9dcfa971dc157dbddf8592447c706d7c5fa60782b64211463dc475218e219",
      "version": 46
    },
    "200.wake": {
      "generated": "2026-10-27T11:29:56.569138+00:00",
      "head": "6340745f465495b17089e6f75595054e91b264ae5e551aee88e64bb05e856c0f",
      "node": "200.wake",
      "snapshot_digest": "545be4c60c90bd0c08dfc4e6140053d0385603135ee20ca2c7aa01a16a9e3a76",
      "version": 47
    },
    "201.wake": {
      "generated": "2026-10-27T11:29:57.568033+00:00",
      "head": "0b571ea79ddfd50657063ac028bcc9d170747bac0790676c1b071b83f34496fb",
      "node": "201.wake",
      "snapshot_digest": "f26de7052433de88ba3bd17f8da63fc07cf92b2c06bbb6138aa3815d6402b546",
      "version": 47
    },
    "202.wake": {
      "generated": "2026-10-27T11:30:01.911872+00:00",
      "head": "db1ff5ead4061a14efc8ee9710c82005c5ca04ba6f66feda8962d5157518d661",
      "node": "202.wake",
      "snapshot_digest": "743861a95924ea652743526c8f36abe9672a8ba4041a9e5790454f6d6265508c",
      "version": 64
    },
    "203.wake": {
      "generated": "2026-10-27T11:29:58.474519+00:00",
      "head": "22103f60173b59da9cb0b85e66e4828fee443f2cf66021afcd67fca4651681cd",
      "node": "203.wake",
      "snapshot_digest": "d4da388cf68a03659c730373265f3f77ba32c1983f620410d910e12fdfe69b33",
      "version": 41
    },
    "300.wake": {
      "generated": "2026-10-27T11:29:59.910440+00:00",
      "head": "be94e5cf464fc935e503730ed0242beba02d119a0752b24717e679b0f878ccf0",
      "node": "300.wake",
      "snapshot_digest": "5905176409a973655b5d573898e706c0d79ee4577c0565b5a02b699081fb95d1",
      "version": 42
    },
    "301.wake": {
      "generated": "2026-10-27T11:30:04.237739+00:00",
      "head": "73ad5937a9e3bbe945481c40732793cd5ba494891e2250c367535e8b21c88338",
      "node": "301.wake",
      "snapshot_digest": "eae117f5486da6ca37a6596dfef198b60a270d303a321ab782d83d5f1e24f7d5",
      "version": 69
    },
    "302.wake": {
      "generated": "2026-10-27T11:29:59.579229+00:00",
      "head": "dd33defa6981e3d829844d7f375205c3c7fa3ffe613e621f5dde10823b3c7f32",
      "node": "302.wake",
      "snapshot_digest": "9747e609d685cddae9c7a0ccb003c7d2db0fa74fad926ddd36e661a83a9d9605",
      "version": 51
    },
    "303.wake": {
      "generated": "2026-10-27T11:29:57.285408+00:00",
      "head": "45e1a9d89e33ee14387848a9fd1c501d8f7dbfe99a92f3f6608e5e8f107db739",
      "node": "303.wake",
      "snapshot_digest": "166e9774a6ba9d738cb53b8fd8acd5cbc79d3ec1c71d6b4a87d6b6f8a1431cc5",
      "version": 59
    }
  },
  "version": 614,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3139.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d32356239353465383265326334393864.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35386635343365386661626334616633.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d636f6e74696e756974792d7261/74696f6e616c652d73747564792d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
