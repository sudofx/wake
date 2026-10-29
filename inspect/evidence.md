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
  "generated_at": "2026-10-29T09:27:54.958558+00:00",
  "head": "snapshot:4d9a2ca9910a61fad4342a93ca32fc4e1ba1c465ff821de8d6e2010bec82b262",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T09:26:27.217964+00:00",
      "head": "3ee80279bff7e23107e5deccfbd63c986fd5b99e5fc48f1384fcb4c77480719e",
      "node": "100.wake",
      "snapshot_digest": "1ccd41c2719b98fae25026e8f2c96fdd5eab4703e611999e7444b709bd00602d",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T09:26:25.921743+00:00",
      "head": "542302b28d387665f09bc8791feffb508d1e0fb99f2e3d870e66d566b6ff3a03",
      "node": "101.wake",
      "snapshot_digest": "44b29b5d407b5dd6c9655b88784b50d473af0ddd045f66a218bfdd9286bc1ef2",
      "version": 22
    },
    "102.wake": {
      "generated": "2026-10-29T09:26:25.174536+00:00",
      "head": "26e4a32143afa5e9b9c21cc8b83f2a1bb8f12554672cffc1b51e0e6bb27a08ee",
      "node": "102.wake",
      "snapshot_digest": "77a39d2e092bc0f4543eedc2ddc025d5b0fc56a29822543b95c0b6716a42c25b",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T09:26:25.740164+00:00",
      "head": "9aa160f7577727431134775f3bac9637dfa4adc95359433f60d59619d00d7341",
      "node": "103.wake",
      "snapshot_digest": "6ebfb76e63044bede0df906a58910d2a244c7594508d5346de7f9f058cf113b3",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T09:26:28.754413+00:00",
      "head": "ab9d15700eee92a319fcf46dc6e87b5c60825376eb77af754228b6241dffec76",
      "node": "200.wake",
      "snapshot_digest": "dfb90aa1857716e0f7d2053fed674fd6ff7f40e45366773a8743e407c7e7345b",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-29T09:26:26.486685+00:00",
      "head": "34163577bfcebb02d022359d3b5ec2492c43017935397d670757588d884f797d",
      "node": "201.wake",
      "snapshot_digest": "2de1034bc9f91c95a7438517cf5b6ebd9f667857f30de951f88168f59e3650c0",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T09:26:24.051778+00:00",
      "head": "bea9d7a58f89eb9b908faaefc342c7a95dde515de915dea9cfdeaaa764a7df3e",
      "node": "202.wake",
      "snapshot_digest": "5625e0be5c72055ff839201246e28d9af080030324b95b494dba97d02b031d22",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T09:26:23.688878+00:00",
      "head": "ad12da99c455d6c65c0ef00f7c1a8e6da6b0cc6366208bdde3688bdd057d11fe",
      "node": "203.wake",
      "snapshot_digest": "724632fae3ef89dc1f4c79adf4ffbbc0089b1e9335040b33d2e76488e7b5f619",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-29T09:26:40.490662+00:00",
      "head": "ddb8bd67b5b7a4d37efabe792b40cd2e25562bc5271ce19c75f3e389984e88f7",
      "node": "300.wake",
      "snapshot_digest": "6f9b6996f85760436c08899868ab27b4db89ef43a09685957df05e95554a3bd8",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T09:27:54.958558+00:00",
      "head": "2bc21048539477029ba2f21a1342f3905dfc2ebbf6e325d743c0891398684dd8",
      "node": "301.wake",
      "snapshot_digest": "d67108ee8dc46c83643787b6aa8e8fd7b7fc44a91fd31740b0534b907b3f107a",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T09:26:27.759352+00:00",
      "head": "92e079ca42a72d857d692ae27ee8eda5c5a5a163254a82e5139108e1ecbd3bcc",
      "node": "302.wake",
      "snapshot_digest": "f05031978dd8dc692dc0fa5cdbaaa386b6b132d90ff58754309cf9e9a8c30e61",
      "version": 27
    },
    "303.wake": {
      "generated": "2026-10-29T09:26:17.362225+00:00",
      "head": "e9974963a29f87a363e6f96c6dc0efd07bf06302440eec228f341ab5774f7843",
      "node": "303.wake",
      "snapshot_digest": "faa83bb44a4e3f78d3ad8c5065016518599bb6de48bb137d88be87a873706a14",
      "version": 23
    }
  },
  "version": 284,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d663836386238306636343861346232/35.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d63326337623763343431643534613135.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
