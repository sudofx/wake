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
  "generated_at": "2026-10-26T10:59:42.740496+00:00",
  "head": "snapshot:969fed4d88f5a5bc9c08956849f811aea64076b771e967ff629374bde84986a3",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T10:36:06.403745+00:00",
      "head": "a774bd334cf42071018e84c68109480fe451fdec1c4272bc4ac9fa6a726e1f57",
      "node": "100.wake",
      "snapshot_digest": "1069f68aa43e04eb8842229360f3e96af206292acdcf6cce05e19dcf6422a648",
      "version": 30
    },
    "101.wake": {
      "generated": "2026-10-26T10:31:21.962223+00:00",
      "head": "6505b18a936b092146390cf13be3b7aa8486c285553be46c717c7ddcf2a54ca3",
      "node": "101.wake",
      "snapshot_digest": "d1d704e3b1fc9a129c46947a21b8ea9a02e1bb33b79756d2b5eee2b7a38337c1",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T10:59:42.740496+00:00",
      "head": "96074ba62b055b39bb82b53dce0d0bc344f32bbf58424d86c3d5b49001e7d281",
      "node": "102.wake",
      "snapshot_digest": "41582ac694bf5ea9c4a619638bb32c6ffc8052fbe843b1e22879f2a0f7e0f1a4",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T10:35:23.249291+00:00",
      "head": "e0a6588d74dbf736d30bf137aeefdf0cee91df8f3a991c2974414d500799f5a0",
      "node": "103.wake",
      "snapshot_digest": "4670aca63dd822e92bf01c4d1378b62b8513fc743d08065ad72c3c9287439743",
      "version": 44
    },
    "200.wake": {
      "generated": "2026-10-26T10:32:18.301507+00:00",
      "head": "53bdfa0d4ccf826c5862d8a578abab58b5579efd0f35022d4c3d560f8122e910",
      "node": "200.wake",
      "snapshot_digest": "d89b4b79838c90c251cac10f6ac2eb2a314930e7067cab40a9d83d8d1b2f8af0",
      "version": 41
    },
    "201.wake": {
      "generated": "2026-10-26T10:35:48.747258+00:00",
      "head": "3474c4d119aa05fdd8c3882da5eb2cc7f987ed76573aafb135c82435a1a43356",
      "node": "201.wake",
      "snapshot_digest": "e79222467be6d148c7486fe5bedb4524d434b0a8cea0892163f704401f952c2a",
      "version": 44
    },
    "202.wake": {
      "generated": "2026-10-26T10:33:10.903996+00:00",
      "head": "aa47a335c695ba04efbfb92054c718f22cd1719573892fb3199e6c2d7567a15a",
      "node": "202.wake",
      "snapshot_digest": "b27c5597c1b7a2a05c56d8cdaf92c692a98446819fad0eb39b3aa0c41e7c5191",
      "version": 58
    },
    "203.wake": {
      "generated": "2026-10-26T10:33:51.801101+00:00",
      "head": "70dc97edf1033bdc66838d803bcff34c509c1f26053e66895818d9c332a44d3e",
      "node": "203.wake",
      "snapshot_digest": "94b8da91aeb192bfe2701411dd5f1b3821020b8bbf2859dd758a2e829211cfe4",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-26T10:44:06.689269+00:00",
      "head": "025bab1d01a1b9532a8d35dfdd03e3cad83233a619556839deac9b7acebb4b0a",
      "node": "300.wake",
      "snapshot_digest": "8c967b32b99213df02eb4c2764fa63c678d6f4670e12f24a8a3f40ac6068d871",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T10:38:45.244816+00:00",
      "head": "eb2f81772fea5bd942d878c15510b137430a6786992f648931a4e4ab63fd3cdc",
      "node": "301.wake",
      "snapshot_digest": "7379475f09a17adf8db5ce968c6079bda7d64f0cd081ab7fda82301266570a8f",
      "version": 62
    },
    "302.wake": {
      "generated": "2026-10-26T10:35:01.947774+00:00",
      "head": "2b52c32074d313aa458563c6af2c1928d9ecc5e246acb6abe859aaa495d134e3",
      "node": "302.wake",
      "snapshot_digest": "38213bef29b2b46859e0f013e7c600e41a6cc3965afe8d7179517a22bc3dfd60",
      "version": 46
    },
    "303.wake": {
      "generated": "2026-10-26T10:37:54.945007+00:00",
      "head": "6c1a7ea5341a77257a2872fdbe91598d07e7cffa3237d03e67db682e1a333b23",
      "node": "303.wake",
      "snapshot_digest": "a32abcddce58a17f68f0d270d42eb961df205dff6ee4b4356ac9cc991608be64",
      "version": 55
    }
  },
  "version": 562,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d393038346432633039333537343233/32.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d623231323663623561616335346364/38.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d636f6e74696e2d72/61742d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
