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
  "generated_at": "2026-10-27T23:03:37.481091+00:00",
  "head": "snapshot:37c35660815f16860cc1cef415a00a4e289f5e182e42be16428ccd948adce32b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T23:03:18.820787+00:00",
      "head": "bf6c60017236f5c631c770491f7db3ef3cf7b38fbcab8de9a4cc595b9e84defc",
      "node": "100.wake",
      "snapshot_digest": "e65f0b5516afbcd37cd834ff11265d0050915f3fc23d04e17b7c52e71461f1fe",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T23:03:16.812147+00:00",
      "head": "3e9148df688d337c003c3d665326b38cd352e7aa63f0dc0f9e22a73caa2409ed",
      "node": "101.wake",
      "snapshot_digest": "e8cff515fab5cfe58748acc2825f45101cd9da6b2d5f3822073b62fe383ae7b6",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T23:03:18.321697+00:00",
      "head": "940c18e4a7eda779f6d9cd04af0cfb8bf696a848e974a4b9068ada925df275df",
      "node": "102.wake",
      "snapshot_digest": "aa34e2cd54c8616c4059e0f16d5e0c2c91a95c3f0f11f2995cffcb6e3a410b8c",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T23:03:37.481091+00:00",
      "head": "248c228eceec47acf4ff73a4d783f72636bd016606bffbdcfcc0e70a0e040e1a",
      "node": "103.wake",
      "snapshot_digest": "b6919faffcd797828607094875d7c7f7adcd499188c28f0515e778b708469460",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T23:03:30.772624+00:00",
      "head": "a1accd947eca37cb38a394291502d512607a49f9209ec29c8c4916c6abc207a5",
      "node": "200.wake",
      "snapshot_digest": "c35d1e565c8482014b4e83d7f1cbb98d22b3ef254316e3427a61ff9e1d7e4ede",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T23:03:36.837028+00:00",
      "head": "ca699e58a191cc02334a3b3fcc32458f92b7702ab6ae22100313645b0dc9ad9a",
      "node": "201.wake",
      "snapshot_digest": "2ebd9f1d38230990440be6563ca8f142c23f16f6b685d14d5675887f6cb07475",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T23:03:16.296013+00:00",
      "head": "019e01f1c74c94a6afe86cbf29b51e6f06febef2d2115120a323be515cfa7596",
      "node": "202.wake",
      "snapshot_digest": "988de3f23be7c74daa6f7ad1317a8cd6f8f71a3bf4aba377f13c583cf97c945a",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T23:03:13.925309+00:00",
      "head": "45e9d81659680d6991d747d3e4ce20b6b7d9aa00a8aca55d0d1c50233be8d3ee",
      "node": "203.wake",
      "snapshot_digest": "03c1699df5674cd146de7eb54136319e8be1f02739fdc2faa6dd6fd8ac7d8c61",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T23:03:09.538515+00:00",
      "head": "cfe2b72bffdcd0e565399e3e7b57bd9c811f42e022d28c776cf78d5400ec8014",
      "node": "300.wake",
      "snapshot_digest": "b768a5c7390de735d3266021738b57b30e7c57cc48e9dcb6fc3e57f6217e8fa3",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T23:03:17.445571+00:00",
      "head": "d1d280c752be3b3dcf0be1677fabd1f7408d7874468c169b85c9860d4b4200c6",
      "node": "301.wake",
      "snapshot_digest": "c5660dbe75abbe672a7a37d06f26efeb6708198cc4ba3b0ad6e22c5d34928a9b",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T23:03:15.358580+00:00",
      "head": "6696c7333deafba8c6acda8743a40679fb398f055d6ffabbdb8a90d2e55f31bb",
      "node": "302.wake",
      "snapshot_digest": "b3ca797c21d10c3c2d705dcb1d85ae870ba95c98ac364055b0dd98bb8c82a31c",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T23:03:21.712692+00:00",
      "head": "523901f094d4fa7b5b274e6397fa75f776508ca251afb385f1f47fc69629bb3f",
      "node": "303.wake",
      "snapshot_digest": "9b111600e505a3c70e95c2e594ed42b4af3b689bff4eac1205ef96cdb852e0b2",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d39633936326132656461386634333665.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d30393230316266656533633634623662.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
