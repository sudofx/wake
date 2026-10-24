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
  "generated_at": "2026-10-24T17:18:05.344806+00:00",
  "head": "snapshot:128304b683f404c985c57c206af3be245321787e175fbab5a70a30a45d733b69",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T17:18:05.344806+00:00",
      "head": "8e1397fa90caf7ecefe10405ed5ea7afa0de4e57c7d0eb17c39ea5e7e84c06a9",
      "node": "100.wake",
      "snapshot_digest": "a668bae56f5023ed9ca5bc5b155965c1f1d227cea878a7a3fe1ae338df424325",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-24T17:01:03.100559+00:00",
      "head": "bbbe2d56f65e77bc171f230699739c70d21505ca6ef661f8425d007ecaa1c8d7",
      "node": "101.wake",
      "snapshot_digest": "84518e6509e8d0ffb0f994fa4a74dd38ceb24d485f2dd08ecad0750a701c3740",
      "version": 37
    },
    "102.wake": {
      "generated": "2026-10-24T17:07:30.617717+00:00",
      "head": "84a7adab89c12f7d5143bb0418e6521d1579545a19ad69e011433abadfd3a5de",
      "node": "102.wake",
      "snapshot_digest": "4a5f6181a74b38f5892a28148f46a0b0c6ca5d98deaf4d48f4c1511463f17224",
      "version": 48
    },
    "103.wake": {
      "generated": "2026-10-24T17:11:01.771258+00:00",
      "head": "5ba835533bd7ec3f4a8cca9eed1729b60351bdfee09c84921bd2c09f17fddd99",
      "node": "103.wake",
      "snapshot_digest": "006e797dd8692c98c7cca03a30e74e2774ab0c1b3e7860343e18f7373519e089",
      "version": 36
    },
    "200.wake": {
      "generated": "2026-10-24T17:00:45.443456+00:00",
      "head": "a8a5d4f565684446fe89a8f93905c9e4bb2edb8af4cff1a349bd5f237dd2998f",
      "node": "200.wake",
      "snapshot_digest": "36313ca9333481fa4615c2d9db678ac09703720fb5d7e161e935bb29f8babc84",
      "version": 27
    },
    "201.wake": {
      "generated": "2026-10-24T17:17:31.522224+00:00",
      "head": "62aba8e5fb36e96da4dbe48bff0e5ea26775600ede7b18830e2531943d5ab031",
      "node": "201.wake",
      "snapshot_digest": "5ce9162ac02a51fe7f483874c395f31fefd4e0755692bff0e02237cde2405307",
      "version": 34
    },
    "202.wake": {
      "generated": "2026-10-24T17:17:07.721729+00:00",
      "head": "7424f76a7c7a27ffa46c6d135de3a9633844173774e8146ce2e15dd3d3dd1886",
      "node": "202.wake",
      "snapshot_digest": "aa416a2066302b640c53514a7186b63e89aeb4e8f563adf58279d0d4e45b6ace",
      "version": 45
    },
    "203.wake": {
      "generated": "2026-10-24T16:58:35.309327+00:00",
      "head": "7fb48da71a8dd081bced10a52938c234a0fadecedc771da78c7254a06b748cbf",
      "node": "203.wake",
      "snapshot_digest": "325cbcd95e987172f7c0c3c5bbd63fb2a4e86266506c5a316f61c90e15e6dfac",
      "version": 25
    },
    "300.wake": {
      "generated": "2026-10-24T17:00:18.076206+00:00",
      "head": "be646ab282544b04a8a526e8acc79d985da724e3239b857677cee58f3274ce0b",
      "node": "300.wake",
      "snapshot_digest": "84178d44e696109e7a2562d3af98e07eb78ca5ec3176610a0dc0949c1e4d5d8c",
      "version": 29
    },
    "301.wake": {
      "generated": "2026-10-24T17:06:32.108290+00:00",
      "head": "ee0a95a3fd26e345fdbf02c5a067378cf3002e9a88d96728181b4910c759d5ee",
      "node": "301.wake",
      "snapshot_digest": "6d807d90ced3832feaf35195a03c8c06fc3bf05bce29015b47b20d0a655c3ed4",
      "version": 47
    },
    "302.wake": {
      "generated": "2026-10-24T17:10:01.968831+00:00",
      "head": "c3ff4a83d81ecb69ed85de7e30fb4d65bf48f1540053f0ea10eac1859820f733",
      "node": "302.wake",
      "snapshot_digest": "27d2f0731a21b41bd11e47b2527f50bf01d6ba7dd4f22e463e86f3770578027d",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-24T17:13:32.601562+00:00",
      "head": "38f26310ca9ea55c8a097bf794f2bda3548ad18d15b454b92bf416b9906da3d1",
      "node": "303.wake",
      "snapshot_digest": "8b66dc0d1d5bec417a4eb65dbbe5ad503a412c3ea822f1b9a8ebb090f44da27c",
      "version": 45
    }
  },
  "version": 422,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [evidence record](../reader-records/evidence/3130302e77616b653a3a736f757263652d383031633564653939313134346661/64.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d32316465653766333763326434326632.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
