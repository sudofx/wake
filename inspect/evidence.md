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
  "generated_at": "2026-10-29T10:10:27.713025+00:00",
  "head": "snapshot:fce5f203bc82c0e49a86c2884688c5db97589c379b5e41e1629e93d25e3e2aa6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T09:39:46.357414+00:00",
      "head": "3ee80279bff7e23107e5deccfbd63c986fd5b99e5fc48f1384fcb4c77480719e",
      "node": "100.wake",
      "snapshot_digest": "7490f8caf05849099e6d2133354b2dc5c40ed9f18ed5b9232a281a4596e7cd45",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T10:10:27.713025+00:00",
      "head": "88809f97550de875760939b4cbd5b04a7863a150fd0c6008b271bbc95040495c",
      "node": "101.wake",
      "snapshot_digest": "159c6a0fb7a52354dd2e8695329bff0308dd456b3373157a582cd96900910633",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T10:08:49.432717+00:00",
      "head": "8561037edac6bd6f11602d96cc454abda9b81956b6c7dc19ecbe481a5f42093a",
      "node": "102.wake",
      "snapshot_digest": "f1d25eff68b21d00b95deffc42490993ceae516df2175bc204cf326fdd4dcdfb",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T09:39:39.451435+00:00",
      "head": "9aa160f7577727431134775f3bac9637dfa4adc95359433f60d59619d00d7341",
      "node": "103.wake",
      "snapshot_digest": "3292edfe69776220f5b1f3346350c25843f75deb6b706ff1f1e90b9591c09008",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T09:39:52.401986+00:00",
      "head": "ab9d15700eee92a319fcf46dc6e87b5c60825376eb77af754228b6241dffec76",
      "node": "200.wake",
      "snapshot_digest": "aa73a7bfacc0ed2e1f959010e8740efac9cb120019c75546a0a28f83e3753012",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-29T09:39:46.655613+00:00",
      "head": "34163577bfcebb02d022359d3b5ec2492c43017935397d670757588d884f797d",
      "node": "201.wake",
      "snapshot_digest": "b640546f7a74ce9630fa6df39322caf88c611dd2bd7f94a754f4938c87327808",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T09:53:25.624144+00:00",
      "head": "9fe1994ed9bd569851d443e4dcb6693276f044510ba3d5b0fa1e2535d2d91192",
      "node": "202.wake",
      "snapshot_digest": "4d1250524790990840ac816e9f32c2c496acbcbd5fafd0b1ee38fba70f0de045",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T09:39:36.138935+00:00",
      "head": "ad12da99c455d6c65c0ef00f7c1a8e6da6b0cc6366208bdde3688bdd057d11fe",
      "node": "203.wake",
      "snapshot_digest": "3ecb65768930014e2e846af107fe3723820af7e05c573daf2756689647d74fde",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-29T10:06:40.036508+00:00",
      "head": "62dcf667ed5b50a6ea7a52d2a796d819f28d834a0774f772593fef8b4c66193c",
      "node": "300.wake",
      "snapshot_digest": "4d71535beda441b0fe9e72cf0f02ceb7d1340bbd437fc190d74ea78cf76b68ef",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T09:39:54.122989+00:00",
      "head": "2bc21048539477029ba2f21a1342f3905dfc2ebbf6e325d743c0891398684dd8",
      "node": "301.wake",
      "snapshot_digest": "6020ff401eef7b7a42262cdd6e659bf4e01ee98efe2cbc9d1a761f6cc491ef17",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T09:39:57.630486+00:00",
      "head": "92e079ca42a72d857d692ae27ee8eda5c5a5a163254a82e5139108e1ecbd3bcc",
      "node": "302.wake",
      "snapshot_digest": "abd5a6827a83777fc338ba9f1d19618e18128999eb56fbd808511325f58aa95c",
      "version": 27
    },
    "303.wake": {
      "generated": "2026-10-29T09:39:40.365242+00:00",
      "head": "e9974963a29f87a363e6f96c6dc0efd07bf06302440eec228f341ab5774f7843",
      "node": "303.wake",
      "snapshot_digest": "76a27ada85e0f1f2536ceec476affab5d0695b21b9f246a0446e6359a3a8fe51",
      "version": 23
    }
  },
  "version": 285,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d633536333565326333386564343263/64.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a722d65396132346263656637613734643032.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
