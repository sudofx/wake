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
  "generated_at": "2026-10-28T04:27:16.329598+00:00",
  "head": "snapshot:d662735b5240078f0941895504784215732397d04659c48b567aac10552891a2",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T04:26:59.375184+00:00",
      "head": "4affe4a262c890410264f145c998fd415fb9fa220f4d38d7f1e4a2a7ffc35eb9",
      "node": "100.wake",
      "snapshot_digest": "11a2692551a4ab84bee1f23a9bd142af84c0ee868f9d3a8fa972bc28ee4323a6",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T04:26:50.183761+00:00",
      "head": "c808b5225d8243d93fdff7c920ec396f9de62caac218bf376bbc22bf0c328243",
      "node": "101.wake",
      "snapshot_digest": "7e85f6946eefb93401666967542cab98fa786a58efe22e862042e21d0a63a779",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T04:26:57.548600+00:00",
      "head": "05a45e4e17aa9f417958a370d40026e0f9e7e8abb129faea8d712bb9073fb023",
      "node": "102.wake",
      "snapshot_digest": "95269a676822dfa11c304c4c1932551c1029849ae9e876ea8d04494084e1679c",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T04:27:09.598429+00:00",
      "head": "e3c734371e1e32181172b5622af5079c2281e6dcf98b856e1492177d2f275f9f",
      "node": "103.wake",
      "snapshot_digest": "8b1fbe934ed5ac8e5959750d1b1f5c92b1954f1450c7527c6f5c5a60e53d05a3",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T04:27:10.908928+00:00",
      "head": "f2357d0c4f7419d723245c648ad58b2d9173b2cac71cb2b021fd87c4743284fd",
      "node": "200.wake",
      "snapshot_digest": "6833227e38c90b22993a1dab18bb8a6aed9cec8ce7025a2c37f92c02770b337b",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T04:27:16.329598+00:00",
      "head": "f13d0038359a467c753ee307fe2dfab16312db5fa7b05ae188acfc9790fb4988",
      "node": "201.wake",
      "snapshot_digest": "17626c5d654ed9bb3193c0e89e28b12651595784942cb18a7ba71cd594000a9d",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T04:26:57.383648+00:00",
      "head": "27e59cbf2696e79b66990c8490c0f4980a120994549c3ae8eaf79ed9772df234",
      "node": "202.wake",
      "snapshot_digest": "c69c36e774a9f8acba156ec3c02ad0eefc4cd5a0a2f86107755eb2dbf39200b9",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T04:26:49.014750+00:00",
      "head": "71a84c0b917fcb460e861cd2d82707f83afe994b27a3b3a53ea13611f547beb0",
      "node": "203.wake",
      "snapshot_digest": "bc24e6013bb48c20016dcaa48ccad0dfc7be4a0af5e2623d99115bb1195e6752",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T04:27:02.649703+00:00",
      "head": "9d44f3be67afee988d5660785a88e59b7357805cc9307c1315ad80c8410762c3",
      "node": "300.wake",
      "snapshot_digest": "d1d5dd5b03884b63f2a33ca88be33dd4351983e471625c0a853890a4184e81de",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T04:26:54.089115+00:00",
      "head": "efcfb209467ac54c20fe7e226f24442f20a3966b375c59c41a34d97d48f90d08",
      "node": "301.wake",
      "snapshot_digest": "da0c185a454d2448e5c842d4a525768d7f97434770436f1da82b74250c2c8874",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T04:27:00.030417+00:00",
      "head": "3a29ba167d898168b7147280a2ac5c9cf627d7f7e00dc351db78b29ebb44c9ef",
      "node": "302.wake",
      "snapshot_digest": "07585864224ae21297c6619e8ac727f7b4f27544ddb6671ad84bdb64f2f9996d",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T04:27:00.602862+00:00",
      "head": "0fc818677381e732cd4be4c6dd449876accb9691f01e40a1d4f566e77ede9b4c",
      "node": "303.wake",
      "snapshot_digest": "f6046ebfd7a32b7572b827b5df3c59e43e2463e8b3f7663f9fff33b35d2fb9ae",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d63653031326662346235373434376338.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d37666133353231643132383134613062.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
