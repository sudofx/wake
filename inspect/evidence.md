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
  "generated_at": "2026-10-28T09:25:27.742818+00:00",
  "head": "snapshot:ac5db06cb6950415e20fec13e4049e228a2ba71d7fa371f9b02986530b6d974f",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T09:24:33.562806+00:00",
      "head": "46c8ca22a3e4813704d40079d50743776965e675be198055972d9e011b3d014a",
      "node": "100.wake",
      "snapshot_digest": "c86fea0a6de21182909686c6135d162c9609dff7f231579ed9801d8a53d34b3f",
      "version": 12
    },
    "101.wake": {
      "generated": "2026-10-28T09:24:26.420992+00:00",
      "head": "81677fa6dad7bf7631716015c02f405b0497a3631e66c7c61aa03902018ad761",
      "node": "101.wake",
      "snapshot_digest": "a68fc57991b3eb888e1ca451fecfc4f8680cbd1119aa43dbe73fa98b2c3b6dd6",
      "version": 15
    },
    "102.wake": {
      "generated": "2026-10-28T09:24:46.008537+00:00",
      "head": "6ca462048a4c5d3b6071870a6c7cdb29123bde67f1a9da1dab423bc9f5f4bcd4",
      "node": "102.wake",
      "snapshot_digest": "a446b601f6cdee3303a1892c8f8b832f140fecf38620206ed8c12804afb662df",
      "version": 9
    },
    "103.wake": {
      "generated": "2026-10-28T09:18:02.010080+00:00",
      "head": "e423e77244f97826221f894acc31e61e07c75a7c677ded3c10dbbfe5e768dcda",
      "node": "103.wake",
      "snapshot_digest": "0e5dca8e6d32f8d7435617ae3dfb6ce3df3585cc003489abd557d043ee3924ee",
      "version": 22
    },
    "200.wake": {
      "generated": "2026-10-28T09:19:19.344113+00:00",
      "head": "24ab496c472958f4317d68207656939704cb9d3d919417e453ea492f65f23a22",
      "node": "200.wake",
      "snapshot_digest": "20f51c3450835e6d0834fa69a4748e69445c19f4666ccaaa71a1ece364e1d274",
      "version": 18
    },
    "201.wake": {
      "generated": "2026-10-28T09:20:03.313250+00:00",
      "head": "b92f5e95662b959c702b51af2e3741346e00bbade9d785f1fb7ec9fd530e41ea",
      "node": "201.wake",
      "snapshot_digest": "660e3636f857810478954ae8087ef1de8e244431f4cc0e3011ab488e6b2d430c",
      "version": 15
    },
    "202.wake": {
      "generated": "2026-10-28T09:25:27.742818+00:00",
      "head": "deede521931e6438d28f9e567510466d7158d4efa408b29e233736aea5df0270",
      "node": "202.wake",
      "snapshot_digest": "ba44e1dac59d0d84b5a5890b1aeefbf90b51005eed6a419149c37ceaf0f85d7d",
      "version": 18
    },
    "203.wake": {
      "generated": "2026-10-28T09:21:08.794776+00:00",
      "head": "a264d2bf4528cd0456c6bb646ca72ad5d38c1da9c81369e1c7e1570e0ba21696",
      "node": "203.wake",
      "snapshot_digest": "58f4a32f089fc340e9328fbc84b2c94eb3b15d6878bc8e2f6e023654288b797d",
      "version": 20
    },
    "300.wake": {
      "generated": "2026-10-28T09:21:29.508496+00:00",
      "head": "1f7a4360aba1eeed1b92ddf38d389dfdb0c8cc738e05f92cc0dab49a56f9fb35",
      "node": "300.wake",
      "snapshot_digest": "5281f21fea4abfdbc60036e98ff280c022bb33365adec55f57957ef14f284527",
      "version": 18
    },
    "301.wake": {
      "generated": "2026-10-28T09:23:37.885656+00:00",
      "head": "3be8cafd58316e48c2eb6bd04620c798a6228317fd6e20f5d4d61db189817ad9",
      "node": "301.wake",
      "snapshot_digest": "24e04c71297b41472a41ab74e95c6a3b56ebd1681d02710ab89c16d35ba6a410",
      "version": 13
    },
    "302.wake": {
      "generated": "2026-10-28T09:23:31.696132+00:00",
      "head": "f40e982276d5f6c606fe96084f4539ab11b64af41cd4771261ff9ee467b3d18b",
      "node": "302.wake",
      "snapshot_digest": "171f3267cb3ef87695680188f8d4e75ea28092e600a9cbf5de16a9103642bda4",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-28T09:21:55.953400+00:00",
      "head": "c47c672b9a3d182aef4c6a294873572e0a63635a5a3949816f372b91cdb90c59",
      "node": "303.wake",
      "snapshot_digest": "69cd6c8666f424eed91d296c7d4b99cd4a11fd276f65d06b717c63026d305e1b",
      "version": 17
    }
  },
  "version": 189,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d636365323863626361633366346230/64.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35663739663063383334386134366563.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
