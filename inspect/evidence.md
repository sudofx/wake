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
  "generated_at": "2026-11-04T03:03:05.890748+00:00",
  "head": "snapshot:d925aa15cdba63118fe89ad895b47f1d2ace96247502465bcfe86360b9fab914",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T03:03:05.890748+00:00",
      "head": "8254a70f683ce5bbf443efcc820c5d22d2c6f7154e7df592265846f9cfaf34ae",
      "node": "100.wake",
      "snapshot_digest": "b234a85248efa22d5a1846764118b0fe0a295361c25a1e697fab757e6180dfe3",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-11-04T03:03:01.505074+00:00",
      "head": "11193d1c15798a8570fc8411202c824a657a15a6c2b8c83cb6b053e5101966a5",
      "node": "101.wake",
      "snapshot_digest": "a28ac58952047afcc835c8311a5d9001f0df970c0d3bc228bb64b7a58aca6441",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T03:03:02.342880+00:00",
      "head": "f152c9c4d3f21a5ede3c4716d91d75af97dd555e5606577cc8716dbbf15ead49",
      "node": "102.wake",
      "snapshot_digest": "cea9ce23cdb22ba4674acf658f71366cf26ba5791e3fe745bb9b00d88f12faad",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T03:03:02.088083+00:00",
      "head": "c61c9f09565bd077a90b9ef95872bff114ea765bcec5dec4faacc523fb29a290",
      "node": "103.wake",
      "snapshot_digest": "724d871222d241a4da536b48a800b1f0a023fd4d585b02231233ae989c5a6d86",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-11-04T03:03:01.119650+00:00",
      "head": "a163581d00468ee7ce589cbde15f7d7d35a946dd036942d9aa055e6498639450",
      "node": "200.wake",
      "snapshot_digest": "7f1cdd9b3d2e316a4a32b0126c7d0e3eafeeccfadabe7abd9d724eeddfdd6a90",
      "version": 6
    },
    "201.wake": {
      "generated": "2026-11-04T03:03:00.948530+00:00",
      "head": "65cc636c4359a851324850db1d2bbe2d94dcaffbec7b3c1aa7e04b076e946a42",
      "node": "201.wake",
      "snapshot_digest": "3984819007d956ed0b11b2a867b8b87c6853cef532fd2bef73cbad2234735912",
      "version": 3
    },
    "202.wake": {
      "generated": "2026-11-04T03:03:00.757739+00:00",
      "head": "130f2ab7c7ccd4ac9f5ef9cff722861cd75c57137b7209701b20fe220b984d6f",
      "node": "202.wake",
      "snapshot_digest": "dee3f2061afdd88da633ee844d863c0f3bf454d037e78d082cb5e28d42f4c091",
      "version": 8
    },
    "203.wake": {
      "generated": "2026-11-04T03:03:00.948076+00:00",
      "head": "cffed390ecac1c8eb90303e6e3b8eb802dea894f0c225102cf49fdd90cb5f682",
      "node": "203.wake",
      "snapshot_digest": "df719d758647021633462a597865a0ed18d86314e437576dcd63faa5960bdc48",
      "version": 6
    },
    "300.wake": {
      "generated": "2026-11-04T03:03:00.463409+00:00",
      "head": "d084031eb0e3ec695db3772d32cc26a7bff048cfe36ed789dbc7eb5abd47fc50",
      "node": "300.wake",
      "snapshot_digest": "c7d90aed38d105c79ae8019e2d19bacbf7ea84d8af900db7843c902422fa4650",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T03:03:00.240845+00:00",
      "head": "8e3e91aec008b3562d540bdd8a2e2451098707002ec2fe58df169119425a8c0a",
      "node": "301.wake",
      "snapshot_digest": "4629363b9e1a0e59a8938792d42918076da81c4f1d645e2f71b137bd8c5a5928",
      "version": 4
    },
    "302.wake": {
      "generated": "2026-11-04T03:03:00.021111+00:00",
      "head": "2ae62ecff998e6759298d25c0e285a95c523dd4deb7e664245bff7f671b80ba1",
      "node": "302.wake",
      "snapshot_digest": "97c8eaddd3bdccfc5ad47868c01363d7f8c245e82a638c5062525a11a5c08954",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T03:03:02.309888+00:00",
      "head": "2e8f3f69ee9c43f610e399a6611498b48eee4e1c2aaabff476af6c3c7c1a5d78",
      "node": "303.wake",
      "snapshot_digest": "2609f585c4e70656aff5cc020a516952bd0e62ca5a666ed766bee733924ac040",
      "version": 8
    }
  },
  "version": 65,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d323631646538373733623739346433/61.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d663961353830346561636332343863/35.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
