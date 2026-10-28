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
  "generated_at": "2026-10-28T08:45:21.696109+00:00",
  "head": "snapshot:783de90d428787a16f9871c2872764bc96e09cad229358a2b353843bc086df42",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T08:40:46.652504+00:00",
      "head": "349171cd87724130019e3843006cd354822e8820d90d8e7a0c80bba55bb01a19",
      "node": "100.wake",
      "snapshot_digest": "2cb1f127d4ea319829411d6e8cfb2fae762be86c4bdab4ff67708d0000fb1c14",
      "version": 11
    },
    "101.wake": {
      "generated": "2026-10-28T08:41:36.299441+00:00",
      "head": "abf7d41793c3bd355988a44afb6c20f1a910bdf1212aeda81ac4bdf96937c347",
      "node": "101.wake",
      "snapshot_digest": "7dda61262a8c63eb765d07d3b0aabc829c821eac0e5ae701eefe5625e6189e83",
      "version": 14
    },
    "102.wake": {
      "generated": "2026-10-28T08:41:43.730083+00:00",
      "head": "0b6c4edf79a85ebd33b95688003fd056cb4ce4222eb85381a0d6fffb366b6680",
      "node": "102.wake",
      "snapshot_digest": "40ca9518f6a1e51b18aa5da498da08edeb1cea214dab2384718014d2ac4776c3",
      "version": 8
    },
    "103.wake": {
      "generated": "2026-10-28T08:40:04.853156+00:00",
      "head": "bf643ff350ab68bcf3e3ea5af6c9e598d82272bfe2d3946d59483f4545c68432",
      "node": "103.wake",
      "snapshot_digest": "4f60c254df5921d8e70907c4df539c9a9c80361baec960f7708680b0bb1c174a",
      "version": 20
    },
    "200.wake": {
      "generated": "2026-10-28T08:45:21.696109+00:00",
      "head": "052cf8688b2b5abe0fece3d12a46ecd6929b198651212df5abbf91b554cd8bd1",
      "node": "200.wake",
      "snapshot_digest": "0ece25401e649ab2ecfc4ce49a46330439b32cc95ee9f283bce9c6d55f231513",
      "version": 16
    },
    "201.wake": {
      "generated": "2026-10-28T08:41:00.530050+00:00",
      "head": "319c55547f365a30547ac67285b9463a22bcb80cc82cd6f0eeaf7d1802ca2c88",
      "node": "201.wake",
      "snapshot_digest": "da51a746c91755d7ebf3617ba5d1600e67cdc9c560cd0618b49df0bd0173518b",
      "version": 15
    },
    "202.wake": {
      "generated": "2026-10-28T08:42:21.829639+00:00",
      "head": "195dc557f7a19ed16032d339673b85bbbb3731f2685aa1c910699a5b33d3e18d",
      "node": "202.wake",
      "snapshot_digest": "67b82d9f5ede8bd919763b1c8f4630250a0b6a9f14132d01d85d9ed6f38be51b",
      "version": 17
    },
    "203.wake": {
      "generated": "2026-10-28T08:40:09.065134+00:00",
      "head": "58c9b233e5396d11db3adb69a925f93cc0635e25d762a210e3c4cd9c30a429dd",
      "node": "203.wake",
      "snapshot_digest": "f0a04578875474fefae6d553880b7846625ea451ff21c6d3c13352bcea11ee67",
      "version": 20
    },
    "300.wake": {
      "generated": "2026-10-28T08:40:58.998963+00:00",
      "head": "90c7ec4e3beb24ff9d381442077f203785ee37a24318533a2715a4c314ede7f1",
      "node": "300.wake",
      "snapshot_digest": "0c0700d86135acdabf193dd362ad1b32a3356792634fb1309812611bc3cdf2df",
      "version": 17
    },
    "301.wake": {
      "generated": "2026-10-28T08:40:27.244020+00:00",
      "head": "8296550e974f3f5026b29e570d8fd65652b2561cf77b8718148c9a41b4ef4ef2",
      "node": "301.wake",
      "snapshot_digest": "f575b9d012bbb876b7a87bd78409f2759412367d4cba4305517cd5d652f5660a",
      "version": 11
    },
    "302.wake": {
      "generated": "2026-10-28T08:44:20.431350+00:00",
      "head": "ef855dcc7b16f3cdf6f0535a6982544b861534cd2b71f3c99ce2c122f3961897",
      "node": "302.wake",
      "snapshot_digest": "c6881ac05fd9badc0fa638b37cc24507c49df6e913a6e65c7abb6a9bdf47dede",
      "version": 11
    },
    "303.wake": {
      "generated": "2026-10-28T08:39:48.635732+00:00",
      "head": "7789bb5734d96281cbb181e39520015342d7cfc4b13bf1329a2a67a4fed48ae8",
      "node": "303.wake",
      "snapshot_digest": "9e75a48d86a649ceef7ed3af990c537a301e9fb7288a93634b35d774adcfc861",
      "version": 17
    }
  },
  "version": 177,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d366335303563343130373739343832/38.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d663730666635313130313064343966/38.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
