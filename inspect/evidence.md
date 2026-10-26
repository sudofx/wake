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
  "generated_at": "2026-10-26T01:50:21.876136+00:00",
  "head": "snapshot:62d1ded9f3ca504cf14218b755cd64dc0c33dcd43ebbe4f627021d8af3cd1d01",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T01:50:18.519589+00:00",
      "head": "5b848a40acb876bc9b12bfc9829c23987e2c81f63ada3cf6cc817d995be1a23f",
      "node": "100.wake",
      "snapshot_digest": "a5af28461e5cb610cfdc8987f6f94d162cadd28e1198f4194358355a54a3c4fb",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T01:50:20.145455+00:00",
      "head": "0276b52461970530c041bb2986f604fbe97fb83a157298006b7f0c84c05e0953",
      "node": "101.wake",
      "snapshot_digest": "9dec4360a10add6b10114405a9f677176a80fb89f1a13109b2d77cb79e8aadd8",
      "version": 45
    },
    "102.wake": {
      "generated": "2026-10-26T01:50:12.657125+00:00",
      "head": "5de2a912287723742bcb1cafeaa0fe990a1e8695f76a92235152a1f882a8727b",
      "node": "102.wake",
      "snapshot_digest": "c35950e10f71523cdad2826706e3bfd011370a49c92fc3ac430515d1eda21d61",
      "version": 58
    },
    "103.wake": {
      "generated": "2026-10-26T01:50:19.206875+00:00",
      "head": "687c5a3215acab3527cf7baffaeec091ab01b712088e9615d0b7cbf6f0a78aa3",
      "node": "103.wake",
      "snapshot_digest": "dabbe74443e0851948cdc964bd8ff4aae0e0899e5279685e290f0e2d87b8928b",
      "version": 40
    },
    "200.wake": {
      "generated": "2026-10-26T01:50:18.947826+00:00",
      "head": "acea0d1f3a2e407c47d402aa83e6542cc9f48ee49a7707708774aa83b405397a",
      "node": "200.wake",
      "snapshot_digest": "738929efce099b00ef8f45e3619730f800c12a1b8a56a0e612c12f4ec7a9527c",
      "version": 37
    },
    "201.wake": {
      "generated": "2026-10-26T01:50:21.876136+00:00",
      "head": "b8cad2c777a3e15a97a2ee4e03b5effc46a387314095038303ad3fc78907a0b1",
      "node": "201.wake",
      "snapshot_digest": "cf78859fa6b0dbf1160005cef197749e35b9a10b9dacff8550ea3ad9f83ab902",
      "version": 42
    },
    "202.wake": {
      "generated": "2026-10-26T01:50:18.855725+00:00",
      "head": "d81984755027a0e43ab5dee5e71634f31cdd5c752c8d53cffd51fb929400b8da",
      "node": "202.wake",
      "snapshot_digest": "4cdaa54f287d534bb741f9beed37c35e62d90590efd3ded6d431126490eb393d",
      "version": 56
    },
    "203.wake": {
      "generated": "2026-10-26T01:50:17.783164+00:00",
      "head": "74a1ee5f65277021ed2b7efd05aee42bc211165946048db99d8f9c3701e0ca00",
      "node": "203.wake",
      "snapshot_digest": "7b3c3d9261a1b213b85fc5359e099e44f2431efb1497c370d8f6791ce72b26e2",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T01:50:18.938612+00:00",
      "head": "4c1244fc3e1ae0057593c9edd14472a45658ef3eea7e58d76e21b5fd405766d1",
      "node": "300.wake",
      "snapshot_digest": "52523ae3ab97716ea567da59c4f70e08a1c6d847fe0c437d0f2237724ca348b4",
      "version": 36
    },
    "301.wake": {
      "generated": "2026-10-26T01:50:12.561504+00:00",
      "head": "7949ef4aa3fffa39b4ec6ec0c8ecf819dcae4e16bc597bb2b52e35c49f39c769",
      "node": "301.wake",
      "snapshot_digest": "a190c6682f590a772c571207cc1b046904315a5d7bee1996acffdd653bb8a00d",
      "version": 58
    },
    "302.wake": {
      "generated": "2026-10-26T01:50:19.525256+00:00",
      "head": "ecd3b6c7d03f2efbc8fc1e6113d5175d32865c72afad013aacf0108fb860ed49",
      "node": "302.wake",
      "snapshot_digest": "7c5a21f5df17a70b39c39fdd9d9648095937a4588cca66c928709abe9217d02d",
      "version": 40
    },
    "303.wake": {
      "generated": "2026-10-26T01:50:21.125912+00:00",
      "head": "3275eda753d51b409ce4de36f887998bf27986bd1455cf1a52834fb4df84f375",
      "node": "303.wake",
      "snapshot_digest": "6f6cfd6109d72e40459c9df21ba8e074d32857d372826912c17cfeba22f44a88",
      "version": 51
    }
  },
  "version": 524,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d316262623163363362626266343638/32.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d643033633031616434616138343738/36.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d726573706f6e736962696c6974792d666f726d/6174696f6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
