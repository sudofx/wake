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
  "generated_at": "2026-10-27T15:33:03.937427+00:00",
  "head": "snapshot:4302a8e1c3ba888700c482d778a13b106823fb64f1604b8ff9c543b038817991",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T15:32:54.013998+00:00",
      "head": "d5c82242f8beb11e8b6c79057a13caf2b49d28bfbab209b186b37f877e4e5fee",
      "node": "100.wake",
      "snapshot_digest": "ffa4eb5d8e9dccfacc8deaa27ab4d729642bd8f5d4e3fd2cc4871d403d75791e",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T15:32:38.593347+00:00",
      "head": "9c09f4340ac184e41f78f3e094128af79e95bd2f46dfe502e7042dd30a7e57c8",
      "node": "101.wake",
      "snapshot_digest": "fa306a38ae261a484b76feb83e0f921c233053e88993b09e5cb97f0c0e297a61",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T15:32:52.088168+00:00",
      "head": "efdc2aad5880aa7db9ede3be1d3fbb114c26de2be16bca8dfd08923be0daf46c",
      "node": "102.wake",
      "snapshot_digest": "d64d5cb724a6b22bb7ab619f94b788e42b8e95adcc6fbd8237f7ad1c500162b1",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T15:33:01.689560+00:00",
      "head": "1f86371ddcfa82b11a45f48c2716be4c9c9e48f63f0c735e8fb57bfc74dfb14b",
      "node": "103.wake",
      "snapshot_digest": "0af7638e123611c26045db05da731899043f4baf53038af3a8d3ec3f0e31103c",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T15:33:00.166212+00:00",
      "head": "c94fca95681f634a9b34e6fffee8c7805bd436308f571ef4a8e463a012237243",
      "node": "200.wake",
      "snapshot_digest": "5a757ef2260c16ef2961d691f13749921d7553eb74c61cb649a7b6f2466d216b",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T15:33:03.937427+00:00",
      "head": "2bd1b9d17781dd10912616ad53012623fa17e2cfac62f55701d1b213feeea0d1",
      "node": "201.wake",
      "snapshot_digest": "399c814b9b63287cdc04aaed162a482b162b8f5fad682a7e49afdaef4fed31fc",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T15:32:39.510753+00:00",
      "head": "3fd2919208da8bee97b4309087d327673215a09c1f38695b5c9e1d0a089203ba",
      "node": "202.wake",
      "snapshot_digest": "9f2fc04565ad801de2270921e2ae2bc3f04978e12d673309d08210d5c7237e07",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T15:32:45.136680+00:00",
      "head": "ddfde13bef4623ad2dfd274b78c66b32de6e63799e0f74d61f561f13eee63d4e",
      "node": "203.wake",
      "snapshot_digest": "69fa8a20f89c47f4f4902c229b7fa931602b5d64431668a07d0cd928e3946b0d",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T15:32:44.271621+00:00",
      "head": "64f8cd96db24f8302b9d8a985166ca3f5322ee37e75f32aa00671484d53b4db1",
      "node": "300.wake",
      "snapshot_digest": "0470da77e00abe591242a24bdce6589e04a6a1f026dc4aea80b5e70955e65aa8",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T15:32:41.771795+00:00",
      "head": "8b54288f9e785cacd5cac26de09247422f41b12848e5bb06d4947c11d206818b",
      "node": "301.wake",
      "snapshot_digest": "d531a68bbd9a57f056861da17b3f67a28f9d402b87d3dbb0144852226dba727c",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T15:32:11.526488+00:00",
      "head": "f437df32413720496612411cff3b638f4e2a405014d8a3c13b99bdf6b65eb69a",
      "node": "302.wake",
      "snapshot_digest": "7a2e3fe5ed14288510984ef8431304fd2d344e15df448b0ea41853897ca6b6c2",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T15:32:44.097755+00:00",
      "head": "9feb1ed7910387a9d0d96fc74f9b88fcc4aa5f3d0a046f50eaff9e85b0153330",
      "node": "303.wake",
      "snapshot_digest": "c2edbf19276da5dadc9aa52ee258519021c18090ae5218f4192b4946cc9ffee0",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d63326562343332383333643034323262.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d36653230633064373739336334663933.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
