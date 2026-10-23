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
  "generated_at": "2026-10-23T00:06:02.327706+00:00",
  "head": "snapshot:a0a506c7d28b1c9a3370ca08d7c6826df0572038a3849ffcd88f29ade8c73804",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T00:05:22.349153+00:00",
      "head": "7734fc1ff43757a19cf2c724f991c8721991aaf2042a20ec0bc1424ab9278c9f",
      "node": "100.wake",
      "snapshot_digest": "7eabc0ddb98d6029f0783e584e1a65ad3d15ca0af55da38757b79b5759a29a09",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T00:03:13.412438+00:00",
      "head": "44c2cc1a92322a5f4a07138bbf1a48999bfc10aea086e498a262ad9c974c299b",
      "node": "101.wake",
      "snapshot_digest": "78e3bc4e8273a3cf1278087927a90a48c7633d04fac26eb33c9ae8a804387d84",
      "version": 8
    },
    "102.wake": {
      "generated": "2026-10-23T00:06:02.327706+00:00",
      "head": "f2a771f3b06231b3b38d4305e61eac2ebac24caec32449d425716cdd3c62cad6",
      "node": "102.wake",
      "snapshot_digest": "2cd63528576fb9a26745a9059a61ef543ab1ef959224faca3297efd2e77aaf38",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-23T00:05:47.928854+00:00",
      "head": "fc99aa41c317592c87642d3b18a63e0b857f32c1468100bf45c3e015225ae7b9",
      "node": "103.wake",
      "snapshot_digest": "446ad38572bad6b6a08ba39f89839009315ee8ce39695fef743cfca4dc678986",
      "version": 6
    },
    "200.wake": {
      "generated": "2026-10-23T00:01:50.565234+00:00",
      "head": "bb1186fb91acf864ced3226ac97381027b4a6530dd4629d48ed31313183da568",
      "node": "200.wake",
      "snapshot_digest": "d0e2127f79b7d2591539ad4d2ab8f84d9ce20a93857dce5ed7be38e0877b5901",
      "version": 4
    },
    "201.wake": {
      "generated": "2026-10-23T00:00:35.725041+00:00",
      "head": "8c2fa4e46fca0d4170ecf0811fdfb74df8a7b3f9c3ff7726c386fb3cecc3d7b5",
      "node": "201.wake",
      "snapshot_digest": "44edab4b21dc8e6a5ba1b5780cf6d9649a36f334d6236ca75a865050662c0069",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-23T00:03:35.661950+00:00",
      "head": "80f29a36ecdc2443240c4ea6a658cd705256d5e5b4832181a2570dce9c951bb2",
      "node": "202.wake",
      "snapshot_digest": "6498fc11d2f1a5109543d7b46b54a7832c72b8fbee080e7b3eab0e4044af4a0a",
      "version": 10
    },
    "203.wake": {
      "generated": "2026-10-23T00:04:40.501588+00:00",
      "head": "1b330d16f713cb844d70f8e7f920f10ceede0dde263a99141f8bc9ab85bdfb48",
      "node": "203.wake",
      "snapshot_digest": "a312b23daa2c1b92e983588393c517111d61505dfc99a7b80b9b866725220784",
      "version": 4
    },
    "300.wake": {
      "generated": "2026-10-23T00:04:23.477402+00:00",
      "head": "04c7b11210e7049936980cb7436cc7a95e3931a243a182f880d67fa12370acf0",
      "node": "300.wake",
      "snapshot_digest": "b5bdcb51962b21a6fd76b4b69b7e2b9ca2671d6f5cb4eebe1efd4838360057df",
      "version": 3
    },
    "301.wake": {
      "generated": "2026-10-22T23:55:53.197737+00:00",
      "head": "3fc5edddc06e0e680578b69aa0c2599b6ee4c986eec2ccef6f7ffbc79f9b31c3",
      "node": "301.wake",
      "snapshot_digest": "9afdddf8777a751129bccb3da2968a7a8c31f75b76daceadbb6fc3a2543c51b4",
      "version": 5
    },
    "302.wake": {
      "generated": "2026-10-23T00:04:59.631513+00:00",
      "head": "181dc51d699a7f9e8d59662c6feb6d2dc95d2b8da192d45f4a547c11dee02f1e",
      "node": "302.wake",
      "snapshot_digest": "0d4081c790beb433f35192485d5afc3f5348f8ff0e2abca137a4fc4de91018bc",
      "version": 6
    },
    "303.wake": {
      "generated": "2026-10-22T23:56:03.455174+00:00",
      "head": "1083d666beaa24952297bcf1ec45a23ea6705ced46892b513c0aea2cf5f0f280",
      "node": "303.wake",
      "snapshot_digest": "44dc737f58aac531cf385b21a5a269129a9eac64f5a74413c148ad42105b30cd",
      "version": 11
    }
  },
  "version": 80,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d33.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31306330353330616231613834653764.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d343936623334636633613961343364/66.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
