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
  "generated_at": "2026-10-22T23:34:37.650519+00:00",
  "head": "snapshot:0eeb6c141dcfec49401a50cf1804a533561940a33d5be81dfad77bd31fb932b7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T23:30:10.540422+00:00",
      "head": "ce49480001929e96db343ee85ef9e10bb33b236c7ce013b193aa4f326ffbf63e",
      "node": "100.wake",
      "snapshot_digest": "90a17513f669a226b16b8287d2bdd44b237f5df516c7a758ec4843bc1e2cd356",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-10-22T23:33:33.071229+00:00",
      "head": "b1efb82d4202f8117209b98b59bdb3f3160797e351e5f478f16247e465d1d500",
      "node": "101.wake",
      "snapshot_digest": "11c5e3c74f4c54290c99c03485bbc3a5dfdca1502b497984d2ac1c5711ca1a35",
      "version": 8
    },
    "102.wake": {
      "generated": "2026-10-22T23:25:03.511349+00:00",
      "head": "128f003bda1735b1346e09fb1248f1c9591955d7d2648d5d61266b4c86d500d4",
      "node": "102.wake",
      "snapshot_digest": "b6f54537ac9e465da8e0412c66d5400274126377d21801952c0f5399f038ddba",
      "version": 4
    },
    "103.wake": {
      "generated": "2026-10-22T23:25:00.150634+00:00",
      "head": "87f95c70341832bd28535a5390a7d1fbe4e3bf69c1e61e32e58fe9facc26b589",
      "node": "103.wake",
      "snapshot_digest": "c86d7986ef92a1dd6bc79a022167e0e950a0cf1b891e29515cd26538dbd0a7d0",
      "version": 4
    },
    "200.wake": {
      "generated": "2026-10-22T23:32:44.828155+00:00",
      "head": "753b38ccc87f0b2c32a89b4aeaddebfcf73ed0ba8219d882c3b3d3258fe1b2f3",
      "node": "200.wake",
      "snapshot_digest": "4e27151fcde86ae492aca08fb6da458e23953d4d4874ac469c5b736c12ba06a9",
      "version": 4
    },
    "201.wake": {
      "generated": "2026-10-22T23:29:51.364595+00:00",
      "head": "4ea5c6c1b1d45bc85a5cc02f8ee405f6a3d3dc8b42a1598d569668707e3155f3",
      "node": "201.wake",
      "snapshot_digest": "1d3e5e9e1a77241c11bfe80323a6e803d3f97dada1707fb047c546170e7c5d42",
      "version": 9
    },
    "202.wake": {
      "generated": "2026-10-22T23:34:11.355360+00:00",
      "head": "debd336e15b941ea47c1ae8d2e2722177f836f24e04113fdd5f6cbc159f66cbd",
      "node": "202.wake",
      "snapshot_digest": "48a89a5c576059e57108dfa0469a80957ea33326df78746541b31a5385360ed6",
      "version": 7
    },
    "203.wake": {
      "generated": "2026-10-22T23:34:34.500407+00:00",
      "head": "308367bdb9899aa4f079b9094f255f2b9d1d10fdb23ae092f8c18eec49b39610",
      "node": "203.wake",
      "snapshot_digest": "ae9ce4a6cbc2b9da8882544b623b434426157acc9b3fe1353535877e5ccb3965",
      "version": 3
    },
    "300.wake": {
      "generated": "2026-10-22T23:33:44.369937+00:00",
      "head": "0017d8e45adb39ff1ca1ef54fded9aa95c04be4f9d9bb4558d312bc4981a7b13",
      "node": "300.wake",
      "snapshot_digest": "17720585e1011c79b4987b5230e096392f4f5a1bd92b4ebd8058c21da72256e7",
      "version": 3
    },
    "301.wake": {
      "generated": "2026-10-22T23:25:17.503340+00:00",
      "head": "15bc901a774cd4bb0a7e073869e1fa9ce7f5fcc54049b23404aef3ad46a00b19",
      "node": "301.wake",
      "snapshot_digest": "80a05a40bf1288faeb11c77fd2011bbedf4b5bfe7386106a082b79cb4319193f",
      "version": 3
    },
    "302.wake": {
      "generated": "2026-10-22T23:34:37.650519+00:00",
      "head": "76aa5c567506cee214e0f030db13b5564eeef8519aea89d4e56e3b55c99a5027",
      "node": "302.wake",
      "snapshot_digest": "e691e488ffd0f5afa7b3f03623c636d8b8dcbde37d5fa724ed586148234873ce",
      "version": 6
    },
    "303.wake": {
      "generated": "2026-10-22T23:25:41.630621+00:00",
      "head": "1999c958bfac13ba161e0591ddcc50372cc157c49e13c62f950fb8765e1043fe",
      "node": "303.wake",
      "snapshot_digest": "f366559f01f4a31fa71ff29d2d884670f8f3047d2693a185fc4ace79f346debb",
      "version": 8
    }
  },
  "version": 63,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d32.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34646161396130333034313834646533.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d643336613031313438376564346137/66.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
