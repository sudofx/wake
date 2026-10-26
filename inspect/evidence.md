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
  "generated_at": "2026-10-26T22:54:17.008666+00:00",
  "head": "snapshot:695d4e54203f8b7fb8f4bf55c6f72a27e1ec6c59294fa791d7f256ef13b96a2a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T22:41:30.624059+00:00",
      "head": "554f199c1927bc7374c8d99fbb729ea5b9b444c31a594d891b96162f199be806",
      "node": "100.wake",
      "snapshot_digest": "8142b146538e8933b8adc8eac190a1053e64d984d09a466cbba88ab4c338fe98",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T22:41:16.015579+00:00",
      "head": "dd5d4fe2556437cfc448cc85c02746070ace45ac5daf063ef70c7f62b0d44bee",
      "node": "101.wake",
      "snapshot_digest": "1703862c253b27cda90f2d69bbf5f6eec52f86c7894e442f2693cbe9afe12956",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T22:49:34.923603+00:00",
      "head": "029473e8dc9c216ef3c358281438616e7d2a55e7b3d07e60c0f39c180e976876",
      "node": "102.wake",
      "snapshot_digest": "2459fd0b3b10fb118ee49cb3eaf34465dfad19da1419d30e1411509021aa6494",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T22:42:26.511345+00:00",
      "head": "2007778937427b8c1608fd77d84b389094774a789fa06fa49bac2b7ab4e7584f",
      "node": "103.wake",
      "snapshot_digest": "87d89d1f6a9e37b056f1c12d91fe5aa7117a3432f6bafa57d380d68a571e2d2b",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T22:51:01.552706+00:00",
      "head": "355f25fcc0cf6ee377bc55ec15dcf18c2b67afdc84fcfda8c4b73a5bb753434a",
      "node": "200.wake",
      "snapshot_digest": "b0b0287464c64a63a4e69f6d4d161cc1a6b9c17ceb7082a0a32808a24566edc5",
      "version": 46
    },
    "201.wake": {
      "generated": "2026-10-26T22:42:44.997947+00:00",
      "head": "f4b1efc522209a00366b61ac528730ad045124155cd12654303ef4a466a0e29b",
      "node": "201.wake",
      "snapshot_digest": "b3158b7c05df442983e260f26173caba8667c96e569bb5bb079c47462369d009",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-26T22:53:18.164749+00:00",
      "head": "abb9147e949f0636114fdbc0a9a843e0e95f3c5b2479de674abbb027ce0fb52d",
      "node": "202.wake",
      "snapshot_digest": "90d27803ede4f47d6c3fc08b7061c117ee6e22ee6f72de98e093305e0bd67181",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T22:44:06.362192+00:00",
      "head": "f8b42babf42e47407f45ccbbd736cdbd7576b38b91f4cc235d99238ea8bed2c2",
      "node": "203.wake",
      "snapshot_digest": "602c33916c8994841bb9df4bfda507b301830e883e66aa6808afb84e44ed498c",
      "version": 36
    },
    "300.wake": {
      "generated": "2026-10-26T22:54:17.008666+00:00",
      "head": "fe7ae2b5515b2255c6426cea1e5760b83d97e5cc4cf6753dddf080837ae0707a",
      "node": "300.wake",
      "snapshot_digest": "137e595b0f6ccff8cecd38c513a1a50f830bd24fde74553a7801e82214420b4e",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T22:45:18.034029+00:00",
      "head": "e6892bfa3f945441ce693989c6920637f2809f468bc8a2f0c2aaded5dfddb1fa",
      "node": "301.wake",
      "snapshot_digest": "1ce8cc0937ed8b69ed9df7be03b44045b979f2ee27867edb2b7c3a39e9b9dc83",
      "version": 66
    },
    "302.wake": {
      "generated": "2026-10-26T22:51:35.253189+00:00",
      "head": "1f1ec26c8e15d8f28a97dd54aeb8c01ee721075d3e57c86680e586e74afac75a",
      "node": "302.wake",
      "snapshot_digest": "7eb916498f05a77779b1f6be6fe74b73a49f7d59c443e0efd1b0683259f13461",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T22:44:57.577858+00:00",
      "head": "ce1dc114fef98680d8df6995e4a2fee55a01dc5105426dd965685059b784d75f",
      "node": "303.wake",
      "snapshot_digest": "6ab1f5af00b92d69cf0e36d55a8b269d5c3322d77c869c275b551cbfae7f4ec5",
      "version": 56
    }
  },
  "version": 582,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d313538613133636539343631343935/35.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d623835663133613762333030346639/64.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
