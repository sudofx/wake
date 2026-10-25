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
  "generated_at": "2026-10-25T02:52:10.243541+00:00",
  "head": "snapshot:034cd4fa29dd4132043a2edaa732c93597731457f517d241d0523363d4ec0cb1",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T02:47:55.149202+00:00",
      "head": "a64e7247a54e6cae60aa4d1ddf95abcc632751e4029c0c02590926226b97b613",
      "node": "100.wake",
      "snapshot_digest": "e3e52a1d4672af3509d9c97e1000a7de8e574b05dd709186ec6d9501269436ab",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T02:47:44.279686+00:00",
      "head": "1862a7db78e8a1e6275e50e7d4f1c64d5ad1fff42e011b6f9b655428170fc04c",
      "node": "101.wake",
      "snapshot_digest": "1bcd84b3aff140e4e439919df2ec013f715d441414d6f2b9555df89704d7fca8",
      "version": 42
    },
    "102.wake": {
      "generated": "2026-10-25T02:37:27.817809+00:00",
      "head": "ef597136b71b7a466d1be6fae8ee03574421c7493db72b23194c836d7429c231",
      "node": "102.wake",
      "snapshot_digest": "423c580ee741df03744475284d4b17c344bb44ff2cb82ff3e7553f32e8509779",
      "version": 54
    },
    "103.wake": {
      "generated": "2026-10-25T02:47:16.760796+00:00",
      "head": "07777fe952fde9d3bb851c415420cf7e75bf69313df21db502cbbcad3f1f1e53",
      "node": "103.wake",
      "snapshot_digest": "1f0294517272d5e589aa50ccbb5dab72b12fb123425795c5fa4accb987cd311d",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-25T02:39:46.954182+00:00",
      "head": "52ecb7075aaaa377440feffff1a6e65c54364a5c136f46a25c5ba5e6b08f8adc",
      "node": "200.wake",
      "snapshot_digest": "7e372897cb3e77875f56f5793d449b6fa52e524b7e59c4d2eff451e54959eb33",
      "version": 33
    },
    "201.wake": {
      "generated": "2026-10-25T02:46:13.791692+00:00",
      "head": "7bae2b50b7df872059d9f44575e5cbc784cd766b75d051858456ac19624fd8f1",
      "node": "201.wake",
      "snapshot_digest": "3c79b6aeaa10a8ebe27b4924c780ec481376300f13cb54ee7216f608ece0c7ea",
      "version": 39
    },
    "202.wake": {
      "generated": "2026-10-25T02:49:54.480060+00:00",
      "head": "8dda3d4de5805adb698bb7a1573d020a0ebffb49a74da29d0a0eabf77f21677a",
      "node": "202.wake",
      "snapshot_digest": "01494574399bb4f2bfa875b7bd6e639739fadc6a5c7e4bebd9ad17afae636c1c",
      "version": 54
    },
    "203.wake": {
      "generated": "2026-10-25T02:46:48.919505+00:00",
      "head": "c7265d9f9e6416c8e526432fa9d7439466ac625b2d3ebe3ad342bab5480f4ac7",
      "node": "203.wake",
      "snapshot_digest": "0c067cc8640f6aeea4fc028b68e3079aee7fabc3e58e3526137e6e50417d1e14",
      "version": 29
    },
    "300.wake": {
      "generated": "2026-10-25T02:45:24.629538+00:00",
      "head": "59a8927574f7995c5f95de45c25b1eb917847846f31cb64a8431207f2d03f219",
      "node": "300.wake",
      "snapshot_digest": "835c1f9087f6c7523be3885e0c374ccf0d99c1ca3647d6723bb3d407c3bca199",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T02:35:25.296145+00:00",
      "head": "83d7044938469e7cc657ab12f3d4fc017391bbd62d594450874378d93b44ce98",
      "node": "301.wake",
      "snapshot_digest": "05ec774430d131bc734871d0a46ce6663cbeb023067c8812630aa957f9366645",
      "version": 55
    },
    "302.wake": {
      "generated": "2026-10-25T02:41:30.827520+00:00",
      "head": "113659a18423de8974aa930c88075bebcbb0dc99bffc077fe2b411d1bb301f0b",
      "node": "302.wake",
      "snapshot_digest": "c751084bcb1963120beba7bbd6cf1cc55009707d623f6e9e66e9413d3f35edf6",
      "version": 34
    },
    "303.wake": {
      "generated": "2026-10-25T02:52:10.243541+00:00",
      "head": "2182c0fdcb94323a569bb4d10a3d733636e25ef5b3b3d022a7a118860552e16d",
      "node": "303.wake",
      "snapshot_digest": "aea88e48fe92902cc00eb95886208a86b987938498271e17881252816d8a91f8",
      "version": 50
    }
  },
  "version": 488,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d336363316231393531393262346339/30.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d653835383534336531653535346336/38.json)
- [notebooks record](../reader-records/notebooks/3230312e77616b653a3a6e622d6d656d2d6964656e746974792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
