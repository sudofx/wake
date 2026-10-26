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
  "generated_at": "2026-10-26T07:57:58.090142+00:00",
  "head": "snapshot:ecedc9293cde1f696937258a2f85adca420c9154f8d50423ce454d7016548390",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T07:28:39.617107+00:00",
      "head": "cd99d997697989a137d7a3458287dca81b30a9d124c86453908ee8a9e56117ca",
      "node": "100.wake",
      "snapshot_digest": "207b0a9f895bcabd58ea59fc34c5c8a643affe57d27c6ca57099e5f0c86aa2bb",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T07:28:40.772678+00:00",
      "head": "99d50ef74d385720cb3e9703e3ddbbc721dcdf0b78957db4c42d5f43c3eecb88",
      "node": "101.wake",
      "snapshot_digest": "544a9224cc748a11cd94cb7f6dda851c2081442cdfebb3484db7b7a8a43adbe8",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T07:57:58.090142+00:00",
      "head": "d774175900cec0650e1981f6c5be5b5d0fbfd3b5e7f9795d9ee94154346db43c",
      "node": "102.wake",
      "snapshot_digest": "bf50939804d3d313f9545434f18c44b9acdcef66bcfe0692f41c62a4964c53bb",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T07:28:39.703998+00:00",
      "head": "e91053dc51bb271b2c3ecb0dd02c253f0499e554335bad5d1f18a0863d461742",
      "node": "103.wake",
      "snapshot_digest": "f88dd2962b905d1ac4a4586a489c46cad59588310ad233ead19cbf52f4d65866",
      "version": 43
    },
    "200.wake": {
      "generated": "2026-10-26T07:28:36.951021+00:00",
      "head": "e0257c53519912989cf69bb085662ee68827fcbffc0cea07518ac169caa1546c",
      "node": "200.wake",
      "snapshot_digest": "e6e46b63eb7d10e911fc4282ab1d8dd113fe75bd6d914c35db13e158f1d5e53d",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-26T07:28:38.122985+00:00",
      "head": "bd1edf07c5f496b1f9c9ba5e1d5bb63a46469256555d0f7a73152e1caed17910",
      "node": "201.wake",
      "snapshot_digest": "d7982e0d0f1004816828e6e4ab47b1abaaa237f8d6bb2c8d9c2dcca77e874e73",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T07:28:40.934856+00:00",
      "head": "535a14417626ede0aed554a8b0bd07175c3e5239fab86e33637793f9e96a8c9f",
      "node": "202.wake",
      "snapshot_digest": "a683a14c44ee761ced6a0487741c541ebbd32c6590126a5d4cfc81c819cfc261",
      "version": 57
    },
    "203.wake": {
      "generated": "2026-10-26T07:28:40.890307+00:00",
      "head": "cfb4c7b4e119f68f16f1f8b7a5d6a2b26adfa319bb42c12611cb65895fd7f36b",
      "node": "203.wake",
      "snapshot_digest": "15754ddd5b753deabf34a40f2390428d0bded81185735e54c0f93f38ec87142b",
      "version": 33
    },
    "300.wake": {
      "generated": "2026-10-26T07:28:39.988042+00:00",
      "head": "d627255f665c645eeeac13878db4062e9405011f3d723b0d19eed1e334625c53",
      "node": "300.wake",
      "snapshot_digest": "cc1de7015339e0f158aed76b9e46b145d9409cdfe3f9656aa491f63dd64da0e2",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T07:28:44.001212+00:00",
      "head": "45c94ed6a149e21707759018c3a3f35a6ef2c4cbf2ead6efaa67f948ee687b71",
      "node": "301.wake",
      "snapshot_digest": "ecd988bc9035a462d7c9344a64c4d6a985bc817969c3f838bb17db2a6afd8b72",
      "version": 60
    },
    "302.wake": {
      "generated": "2026-10-26T07:28:40.168678+00:00",
      "head": "7e100c205d807b4ca9e435bdb5f25dd4c001cdb5a7aff816f325851b37ab415c",
      "node": "302.wake",
      "snapshot_digest": "af81cb87619b4f3a5f6545162a1215d898d0bbd8f5b1d67540c45d2308cc8bd9",
      "version": 45
    },
    "303.wake": {
      "generated": "2026-10-26T07:28:42.035202+00:00",
      "head": "6dcd897ec2b389ba884f161e2d2e21484ee174a97f5fae153a66c42557cf9b0a",
      "node": "303.wake",
      "snapshot_digest": "6ae58ea67f0c9f3b28ef663f473f68e3c3a5c0bdefff656bdcfa4f25914eef1e",
      "version": 53
    }
  },
  "version": 550,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d363263333238393838323366343462/30.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d633734396235353237616535343465/37.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
