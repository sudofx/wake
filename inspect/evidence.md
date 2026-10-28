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
  "generated_at": "2026-10-28T06:01:33.572006+00:00",
  "head": "snapshot:f8e04e45e007bd16860a1b1883c76ded6a944f2d6751ee100ab4e7c9ee40634d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T06:01:33.431938+00:00",
      "head": "43028a472b25739fe9e85a0ec170407572219497573f095c49befc946389c6e5",
      "node": "100.wake",
      "snapshot_digest": "013636379354a15c5165471a17df1813aeae91dde28f2c55a53a8e4c6b34bde8",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T06:01:29.071943+00:00",
      "head": "0384317ab6d7839f6307452b2b1ad30bdbb24b5e4f0a894f06f0f261e2a86e43",
      "node": "101.wake",
      "snapshot_digest": "07567a43df90741d2bb4d89da7b2fc8cb76e71495efd9bd71b9055dd47159434",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T06:01:31.174006+00:00",
      "head": "c61b90655d1853ce883f8c70b4f3bbf37b09c6148daa21dd05b8537b7e32f55b",
      "node": "102.wake",
      "snapshot_digest": "f598c3bd3716b31fc573e3cde954a24f730f6f3c7ae6daa3786716f199c6d499",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T05:53:25.929145+00:00",
      "head": "78b2c0f85ae0a7af7d49ef5b84123ecdedabe56e193497738af74036d397248d",
      "node": "103.wake",
      "snapshot_digest": "16bfab1374117e502a5f23f81cd8767e0ab36e1b94cebc992ca8936f47a3a0fd",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T05:53:21.557920+00:00",
      "head": "79554b600a73d84e4d1299c2e8ac6bbcea728f823980529c5588ee3a6652eaa0",
      "node": "200.wake",
      "snapshot_digest": "5c07b082a71a4a8c591495b3a0d413c06160e250a6a4ab754577d9d585ff8fe0",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T05:53:27.285557+00:00",
      "head": "22be26dda69e3b643a1b5c70a71dda03e9cd802a0f9658390b26116acb968762",
      "node": "201.wake",
      "snapshot_digest": "1ebd1bdc6ee9caecf253bf4ab97468f1e15d94fdc4660bc5f5383992421da032",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T06:01:33.348847+00:00",
      "head": "7139e38b59dd05012d6930600e483ae563230ff0e25f6eaa1269265edcf463b4",
      "node": "202.wake",
      "snapshot_digest": "a1db0d216538b90a7ceba1d46122db0b0710b9508bdc48ca74ec8cd5a8ee43b3",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T06:01:33.572006+00:00",
      "head": "467407719b775629316d92624b10574fb9bf983160daef0a9e6fafb2558f6323",
      "node": "203.wake",
      "snapshot_digest": "042faddd375679d608ac30cb450781d38459df270157005ec35d732f51f03b4c",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T06:01:29.017475+00:00",
      "head": "9259bf3ccd639e7c9f840ff794fe308ae045bd2b14bac1e220164c9120d04dff",
      "node": "300.wake",
      "snapshot_digest": "04d5a8c532c372ba961c1e6279d4bf697670078ab1d131816a25da05c846f2c9",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T05:53:16.607215+00:00",
      "head": "e5c2618514809fe4ea359bbe80e2560010c7cd15a39b2e00d43705777eb62e3b",
      "node": "301.wake",
      "snapshot_digest": "f7671e495803afe39e2467a3839bef7be6dd51d31cb22a5d5a4f4cad2675d7a6",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T06:01:30.799139+00:00",
      "head": "a99cdc2bdc0ee55a909edbeebe54156d3bae8c5b7e119e0b0f45a781ba76f3d7",
      "node": "302.wake",
      "snapshot_digest": "2c55ea28524f1a6c55ce336a8ac96d2cc7a1242d1003f264bf5dd8e707fdcce4",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T05:53:17.506663+00:00",
      "head": "3d0bbe616415c6e54acae1aa3c8e4d9080a9966e31dded259ba2542d2d6ef857",
      "node": "303.wake",
      "snapshot_digest": "80e75f3e817f32d041adacc37c131768b7aa591128e40351f3c665a1c683d80c",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31633936343935346239373434663437.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d62316665326132363164383734616336.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
