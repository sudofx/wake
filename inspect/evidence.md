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
  "generated_at": "2026-10-23T18:57:43.703194+00:00",
  "head": "snapshot:0e6ec613e1a1641b5e43e5d4971584774478e22119d09ca8d9fc936804f0422a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T18:55:09.104429+00:00",
      "head": "fc4de8807881b29fc7151940acf1d7204d82b57388f5e5906f3b78750f667573",
      "node": "100.wake",
      "snapshot_digest": "70999604b352f8c870d2979e1c3834a9153182d2fe1d6da39659ed02751873fa",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T18:57:20.219620+00:00",
      "head": "0183bb7ec62d1851c32138520ef8bb28ab6ce3495bd6bba8d53ceeadba2a049b",
      "node": "101.wake",
      "snapshot_digest": "649f49cd56324d8513693086633921ba9f720eb1e413f0fd6e2b40642a8a5825",
      "version": 30
    },
    "102.wake": {
      "generated": "2026-10-23T18:56:03.464481+00:00",
      "head": "42f886215a3dfddb21847199bee48a06aa353e4494561b9b1b7cd073d72f7c22",
      "node": "102.wake",
      "snapshot_digest": "e2afd83132893884158aa1522f061a7b4578fdf9bfed67b7783c6a711ac809aa",
      "version": 34
    },
    "103.wake": {
      "generated": "2026-10-23T18:57:01.118578+00:00",
      "head": "200c075cd0c038ca184fa11cb457672087cbb4674171bc69a2ac0b549974b499",
      "node": "103.wake",
      "snapshot_digest": "05a4fe8c009c5ee4a784067a257007ac87c14d4343e26dfb7c2d6ea481d7855a",
      "version": 25
    },
    "200.wake": {
      "generated": "2026-10-23T18:57:43.703194+00:00",
      "head": "ba3d37dceadb6a2691b721ffaf85bec2336e51b8bf671d47a9f53d615b29c599",
      "node": "200.wake",
      "snapshot_digest": "4e43b9ecc09dbf0829af1b2e3dd6c8095df607fe47d902a0217e64744946d3d5",
      "version": 22
    },
    "201.wake": {
      "generated": "2026-10-23T18:56:10.917790+00:00",
      "head": "ceeb0a00fa2382d002571e938860fe3b2e8a40d1def727ad2946c3c1ef95827f",
      "node": "201.wake",
      "snapshot_digest": "25cbd284ab5636a487860234407e633a45d63eefc1426e0936e2fed422ffbf45",
      "version": 24
    },
    "202.wake": {
      "generated": "2026-10-23T18:53:47.505227+00:00",
      "head": "b2dacbf57eff18932b8a4c93be5162eb4720d02c091cd423e8a7b96f09e9d94e",
      "node": "202.wake",
      "snapshot_digest": "12c9ca5cae5c8bb4e829469d8070853a8f168f835f939419adbc0b6a17d4d8a1",
      "version": 37
    },
    "203.wake": {
      "generated": "2026-10-23T18:56:24.816008+00:00",
      "head": "146822ffb00c3650f9e82593bad45ee2bcb71f47f08e6e0baf367ea619bf2c99",
      "node": "203.wake",
      "snapshot_digest": "8cd4a52c0656f50a70435451fa7ad03c51641ca66a7fef6c54a620e585aeb5e3",
      "version": 17
    },
    "300.wake": {
      "generated": "2026-10-23T18:57:26.971468+00:00",
      "head": "60ed37b7985582f43f9300838ceee7ee954166fbd1077b87723472d7ea3d5569",
      "node": "300.wake",
      "snapshot_digest": "2c5c4e8ab75509eb9dc3d9b1e98f1d7d6f18f8e9b683590f197e5cba0a817fbc",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-23T18:55:57.562224+00:00",
      "head": "469011bc1528b0ad354e4f451935e343946d9a3ceb0bf6a6943e9f5a00459cdd",
      "node": "301.wake",
      "snapshot_digest": "f4b27a594957ec110faef1fcd14ea49b40fcea79d73d0bf15dd41038d7b61877",
      "version": 36
    },
    "302.wake": {
      "generated": "2026-10-23T18:52:03.751541+00:00",
      "head": "5c5eeb245bf1c73e0bd8a142072cf0521b105064c5cd0d7d6d18e36b4747ab35",
      "node": "302.wake",
      "snapshot_digest": "d5ff79d7cdc97b5d180513d502cf10f594934cf07f50a3e773f2bb6e7cd332f4",
      "version": 16
    },
    "303.wake": {
      "generated": "2026-10-23T18:54:55.820270+00:00",
      "head": "fddc321957b4a2135eb0380f5b59fc167670bfd9212bbe93e46218b3781ba9bd",
      "node": "303.wake",
      "snapshot_digest": "cf87a2596324bed93abeef0a2ab8ee89c719dd8040de14371b3c67323ee1c817",
      "version": 33
    }
  },
  "version": 314,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d636564393133346536303132343861/33.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d666336323661366134336236346364/35.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
