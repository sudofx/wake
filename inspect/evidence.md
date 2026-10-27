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
  "generated_at": "2026-10-27T03:13:26.378107+00:00",
  "head": "snapshot:6244c163b5e26be9776381b8e51235511f376b60d3cb3f612bffc343cafcaf4c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T03:13:19.670914+00:00",
      "head": "9dd2f4960560b7f8e1805e9a5423a1378c448b03bf853f5bd45a0735cd783217",
      "node": "100.wake",
      "snapshot_digest": "bf9907950f216ec410f7bbe35317a1bcfa71b2bbc345f734341120c5397b1b4a",
      "version": 33
    },
    "101.wake": {
      "generated": "2026-10-27T03:13:21.219585+00:00",
      "head": "d056f57c404827276ad4a32619d292e7d3a35cc534da87655f25bc7b8cefe172",
      "node": "101.wake",
      "snapshot_digest": "bcd71dbb9485fca12b300a0a5e5aabed63575bba50804026aad1d454bf97a5fc",
      "version": 49
    },
    "102.wake": {
      "generated": "2026-10-27T03:13:26.378107+00:00",
      "head": "7d616df768e7f0ce0a0001b6eda60c1765401058b3e98e6cdd2f8b18d5cfbe9a",
      "node": "102.wake",
      "snapshot_digest": "8c7d0e7b0fa81d9847f8c4b55ffc2d8c75910885edfba5784904669daf321918",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-27T03:13:20.627085+00:00",
      "head": "9d8a382a08e4243b40bd4ec4f68345067ff77236e232ba1320db43d3240237eb",
      "node": "103.wake",
      "snapshot_digest": "df43b752abffe266e2c7288febfd6f79bed178a1eaca2b1d7cde1998fb3e369c",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-27T03:13:20.181897+00:00",
      "head": "b6e1c1d719066e9d72fbf71df2ab07b0eba1fe075da327f772a2278288733d79",
      "node": "200.wake",
      "snapshot_digest": "3cdbb5f4ece2ff6345bce977faf0f3ed1b675c7a8fbcb9efb4d4926ef8cf2d42",
      "version": 47
    },
    "201.wake": {
      "generated": "2026-10-27T03:13:21.427995+00:00",
      "head": "b22f712a9a0f033ce05e9adda53e40da26f80ec991577da05e00c4c54c337d22",
      "node": "201.wake",
      "snapshot_digest": "fae00a7255902f24e1c7d0eb630770ae204911d2cd95aab4301c787f7653fe7a",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-27T03:13:20.116265+00:00",
      "head": "4c5d6770835bc1fc5ba65a6b1472e3475ffbc1562eae176f0e621fffd7daf108",
      "node": "202.wake",
      "snapshot_digest": "23bb2d4c100408de3af3fd5f977b7d6f58c995334e6ca3c44acdb8b8f0b4e3c6",
      "version": 62
    },
    "203.wake": {
      "generated": "2026-10-27T03:13:21.278103+00:00",
      "head": "a82ac475b5a2421418a950222a98f8f7135f45283fe36c609b47e6def4e074c6",
      "node": "203.wake",
      "snapshot_digest": "7be608e233cdb14f52f63b482fbcb2ce9dab957ce73c0654e88c0bd3a6b785cf",
      "version": 39
    },
    "300.wake": {
      "generated": "2026-10-27T03:13:21.244489+00:00",
      "head": "f6d4a91fded6f0f2cda1faa41a30cd1f2267f0d327fdb5bafe2256e6d960571f",
      "node": "300.wake",
      "snapshot_digest": "dda252e43e6f1f4882cffbfc26e77bab7c13269fc9cb50e8c3c20fb5f41ffa29",
      "version": 40
    },
    "301.wake": {
      "generated": "2026-10-27T03:13:23.917351+00:00",
      "head": "318f7cfffbe0465031b15f1927d5652394a67a0b38e8b83eba15fd9411803f94",
      "node": "301.wake",
      "snapshot_digest": "c95f74f1696e51c4e28cdaf8bea8015702f4fb6a9b91ceb5cfe2f8667c54b2b2",
      "version": 68
    },
    "302.wake": {
      "generated": "2026-10-27T03:13:21.574133+00:00",
      "head": "14789d747a69ea80b92a4463f8b94c666414e8d781c3d19d4ca007a45cde667c",
      "node": "302.wake",
      "snapshot_digest": "a28d6e9efc714ccba9ca6b733a45e43383323a5bef21f3aa40c80dc9eedf3026",
      "version": 49
    },
    "303.wake": {
      "generated": "2026-10-27T03:13:23.934862+00:00",
      "head": "06ff509a61330eae0b65173849a2b5faf9137dd7ff3c8ea163d1f95737050276",
      "node": "303.wake",
      "snapshot_digest": "d5f3cef245e43bcd0ebf24fa0c55a867d3441021a021a7d3b775ceaac5857e2d",
      "version": 59
    }
  },
  "version": 600,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d31633832303764646265636634663531.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d666266636539633865353238346364/34.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6761/702d69642d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
