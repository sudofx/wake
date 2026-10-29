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
  "generated_at": "2026-10-29T07:14:03.194875+00:00",
  "head": "snapshot:03fa9db43ad1cdefb13346fbbf3a2ee714401535831e70809cc50d308fca1be3",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T07:12:31.431910+00:00",
      "head": "f3773ed0f94d74f086eb6db3613621800269b05984f8e06e45f50846940a3bc5",
      "node": "100.wake",
      "snapshot_digest": "a9b590b69ef8c1e2a4c3dc04f34f9825992523b8f0dc83892f224af169be1f95",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T07:12:19.448192+00:00",
      "head": "6bdb3afc3bc97422ec9245abb76380c73c071eac7cd5236e6658ae697dfa5d5b",
      "node": "101.wake",
      "snapshot_digest": "f89ca23ce60467ea7709182ea817193d49ee452d4d17314c3e98a12d1f2f5fb7",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T07:12:25.510983+00:00",
      "head": "604f2f5f1590ec634aeb9cd8258faaa4d13cb81fb369f900d6a056603a1bf259",
      "node": "102.wake",
      "snapshot_digest": "8f4866188e1e1aa0646530df5bfbc4429ea3f6920a9e4db2f21929ffb696bca9",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T07:12:25.806536+00:00",
      "head": "1bffe27420ad75592e30bdfa85871fd29d6c86c406afa277fd24259f7af7cbb5",
      "node": "103.wake",
      "snapshot_digest": "7932b67f3629d3520e7581f484a870f7d5d0c7a7cc783be4e40fb9fccfb824f1",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T07:12:29.245564+00:00",
      "head": "c0062768daa19cd09b0596081a74a5ce8a1b63877f3a6917255c7e01a1737a53",
      "node": "200.wake",
      "snapshot_digest": "799b8ead3cb6d0195c4c2da48d8569eb6e1d1cf726c9bf8ab4aff50c6499ce4c",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T07:12:24.554184+00:00",
      "head": "e9916eb4ccfe0f3a4c7f30b47dde76f2bf19633c677f163fa20df6572f9b1706",
      "node": "201.wake",
      "snapshot_digest": "52a2f3a062d12ee195148dedf24524fb5ba8ceb5d295ab5c7ef0ff5583dc2379",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T07:12:21.984591+00:00",
      "head": "eb6f1fb491be209d3282303798875b30bf932e0972a5fdf6f0233a4d8a320763",
      "node": "202.wake",
      "snapshot_digest": "c6acd9885b112d542e2a93ea951d49559d3a25956dc4e376ed1e9137ad4576b7",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T07:14:03.194875+00:00",
      "head": "b4f0d72fd490b09e55460a033618ecb76d4f37240e1664bd64648211e17959f2",
      "node": "203.wake",
      "snapshot_digest": "a159999f1eb7ebf580d7e2c384a4d42eaeae5d56ecfaa6ab7a750423e859aeb8",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T07:12:17.576008+00:00",
      "head": "17bc6c85d17842a813e00fc3c3f7471fb0eabd59de0ca03e38dd10069d868b20",
      "node": "300.wake",
      "snapshot_digest": "25618db6cd9d7eb4e52b8334a008cb1f91fda40c22803cac1eddf6f3c78fee90",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T07:12:31.727821+00:00",
      "head": "4b753ed87e1e1f7dd334e092587b156f322706327004f7a5dd14a40801be4792",
      "node": "301.wake",
      "snapshot_digest": "a360362185eb18dddef770a039eba6a83fb85ac386f1aeba58aea1fb763311ef",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T07:12:52.546564+00:00",
      "head": "6f8d174f3ac159880107e87963abab9c63eb0d463cc0d0f7800a44268536318d",
      "node": "302.wake",
      "snapshot_digest": "b06f58481386069292ad36bc04901097b00800aebd7bb57b1a20c7f16cde86cb",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T07:12:23.364816+00:00",
      "head": "b645431e0326932ca5b3f615b58c05938694cc637124621134d7b3efd9e1f3ab",
      "node": "303.wake",
      "snapshot_digest": "3e07d9ff8fea704eef0600be328c7c7cc95e463c88d0725ae7b11605e0b9f8c6",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a736f757263652d636439303063313166366134343061/30.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32333633633538616134336434616533.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
