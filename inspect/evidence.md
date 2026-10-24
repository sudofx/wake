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
  "generated_at": "2026-10-24T21:53:10.214134+00:00",
  "head": "snapshot:9be2fc9942f0e316aed05bfe9bbff367db6f7d4f1336ae8d25d34913c166e4ce",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T21:27:44.804777+00:00",
      "head": "a7129785d947b213f2dd9898a73cf28dff6515bbc3db6a6e8ce0c1445aea3f2d",
      "node": "100.wake",
      "snapshot_digest": "c3d1dc5b39afc0cfe858eae9ee03aeaef5daf14030b607e30ad562f615a54555",
      "version": 25
    },
    "101.wake": {
      "generated": "2026-10-24T21:27:28.165914+00:00",
      "head": "093208862f4d1174a0c77e32bd005c9d8952a79525c68533c08d1d747f105a5b",
      "node": "101.wake",
      "snapshot_digest": "92e9caabc37d3ab930221a67a3d6cae865c3792411b92a86ae68f69c091bee40",
      "version": 39
    },
    "102.wake": {
      "generated": "2026-10-24T21:47:56.750641+00:00",
      "head": "957c7699cbcc3dc00272b6f7a9d93809b4060522025b54109781e3ac24680461",
      "node": "102.wake",
      "snapshot_digest": "f349a9bb2f6a14f9f75c035342b9a58dbf23b5b8f4a9f45fb08a7ba7d3d3d983",
      "version": 52
    },
    "103.wake": {
      "generated": "2026-10-24T21:25:44.264684+00:00",
      "head": "37c1777a48e5cce63deb3d8818512cfa235f11d3f81e7a0cd0590e627c7cb448",
      "node": "103.wake",
      "snapshot_digest": "5d35ccc29d116defc5fe5c756f9bca0d0106bd5f36b5f0b4a54c71d2b7dcd9ee",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T21:27:15.201542+00:00",
      "head": "b4103542229be1e383d7a4f4bf3d8d4f3acf871ddba251196e13c3b158d93169",
      "node": "200.wake",
      "snapshot_digest": "625be107f05dcca72414153dd0079e0e6e6bb0acbcbfe73796341aac26ca77ca",
      "version": 31
    },
    "201.wake": {
      "generated": "2026-10-24T21:28:36.460878+00:00",
      "head": "dd1c485576fff62918d8b463e610742f463b99123e726e9d26a39c619e2f8c9c",
      "node": "201.wake",
      "snapshot_digest": "e3f082097c1064d381b6ded7a334d1889e424f0e1a215d6c3d62dcfa40f6fcce",
      "version": 36
    },
    "202.wake": {
      "generated": "2026-10-24T21:24:34.486121+00:00",
      "head": "cad60b06ab3e08441fa0d21bee5b3387c8ffe2c45128176dff3673229096aaa9",
      "node": "202.wake",
      "snapshot_digest": "6fa17e68a9809f8f28ac83b4708d31665da3b0f61d3683d663162178a20ab37a",
      "version": 50
    },
    "203.wake": {
      "generated": "2026-10-24T21:27:00.352126+00:00",
      "head": "78f7dd510d5e3784ef368e1c1d8e3f1624a65e69c4221375db549b59d47c7e90",
      "node": "203.wake",
      "snapshot_digest": "5c1ce6274ba338c185b7d6b98511ad23d8cab7b523d713aa652235dd077e02bf",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-24T21:26:21.974859+00:00",
      "head": "69331a3ff2bfb0667fa6b69f8dbbe2d717aceb328c1b8b962f607fccf8217013",
      "node": "300.wake",
      "snapshot_digest": "bac8e99cbcc3c50753a5bf178434e213ae1334f00ebce0ce964a5de75a4ef22b",
      "version": 32
    },
    "301.wake": {
      "generated": "2026-10-24T21:53:10.214134+00:00",
      "head": "ce8dca965728f73d0b78d4fbf699e57f4a7906e496fa13afc92210c8d70c4f1d",
      "node": "301.wake",
      "snapshot_digest": "0b02b17870e3365e45c5da3a370edb4196865a42521557cada4e6858eb96fe5a",
      "version": 51
    },
    "302.wake": {
      "generated": "2026-10-24T21:52:40.684945+00:00",
      "head": "8436a621da9f7fabb957eb6460cfbbdf789f850971d0cabb77da88aea1afab87",
      "node": "302.wake",
      "snapshot_digest": "50dd8d500d68812971d7074649ec96a88128a1c72b7354aec487d85e74ece8c4",
      "version": 30
    },
    "303.wake": {
      "generated": "2026-10-24T21:27:59.499951+00:00",
      "head": "36262260f9db7cdf082c6d180dda1b2734487f7bfb4d7f444ad8efa358fc81bc",
      "node": "303.wake",
      "snapshot_digest": "d2a8546b57a1f746abe45dad7024e593c0fa475813c71ecf1cadc6aec222df66",
      "version": 48
    }
  },
  "version": 458,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d383938303239306337326565346131/39.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d39643433386263313065313934636533.json)
- [notebooks record](../reader-records/notebooks/3130322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d6f62656469656e63/652d696e74656c6c6967656e63652d6661696c7572652d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
