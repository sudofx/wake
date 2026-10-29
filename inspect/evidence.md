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
  "generated_at": "2026-10-29T08:20:07.766023+00:00",
  "head": "snapshot:10bc8610a8bf477faf8eb3d5c0cc5710ea49a7f6add8a93654e99e932caa3f3b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T08:04:32.349120+00:00",
      "head": "e0b595847d22bac9744e957b73da8e2aab6f891888307485e1a6dbffe1c1778b",
      "node": "100.wake",
      "snapshot_digest": "04efefb98ba6fcec671905955d93bf12b27610462f5565278868141136af481e",
      "version": 20
    },
    "101.wake": {
      "generated": "2026-10-29T08:20:07.766023+00:00",
      "head": "d1bb77c500b86a2af78fd63d059f85014e75e06e0f91e2a3e741705f662ff5e9",
      "node": "101.wake",
      "snapshot_digest": "0e76b1c9567a2b461ec6cdb4bdccf2fca24639f9deb35350ff3da7650ad2b6c0",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T07:52:24.198084+00:00",
      "head": "f72ccae52ce790bcc35c02c51f228d7d497f5a4d0e52c9ccf82d5d374b3cf5db",
      "node": "102.wake",
      "snapshot_digest": "9f71fbde5569afd39bd427c6daaccbedf56f54847330d1224a9f2546834f6480",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T08:02:51.186544+00:00",
      "head": "6c7639fefc60f547dbcac7a02d3310e5a178e7f45dc9ea33d31056c7486d1109",
      "node": "103.wake",
      "snapshot_digest": "107856c36b6289556fee4f5b6f492de3b383c6e13300614f65fb8351435f96cc",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T08:08:02.961995+00:00",
      "head": "63d52f7c6df9dbeb6197f4c7d5d34f0171b66b9ceb59048d72e7d82a86404a50",
      "node": "200.wake",
      "snapshot_digest": "cb92017f237765680fc39dd5c68d0a8b848466823348d6b7896fc76f1ba2415a",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T08:06:18.237200+00:00",
      "head": "5f3b069098b2401540692e57359cccdab9580248ba62345eae62c6b6e0ae4874",
      "node": "201.wake",
      "snapshot_digest": "70f651991dc1fe662842020fa44e8dd51cd9afd98bc2eb4c1f4b42bd477f913a",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T07:55:55.773152+00:00",
      "head": "fb126329325f3373cf2fdbd9eaa16edd640be69f3bca1f9688d940bd1d25eca2",
      "node": "202.wake",
      "snapshot_digest": "9fc04cab93bedd2e6430d8f4d18cc3bbad653c64697a4e26dc44c1a8b684c65b",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T07:54:08.499610+00:00",
      "head": "ee193dd35426522f6db6035632378aaf4e6a103fc3c7f3c0c68ce18bec42c19b",
      "node": "203.wake",
      "snapshot_digest": "2884c5667efd432e4507c73eac3fbb418539cba50568937388f1333d5b2694bd",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-29T07:57:48.021832+00:00",
      "head": "b70ea40b07d5c016157c74ab4665fdbac2f85cf38d6daf2a6aa9ed0a849b7cdb",
      "node": "300.wake",
      "snapshot_digest": "81fc0487e30f52154b86aacd42d1374cbea60bcc714f6a5545472d634df9b663",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T08:01:04.524195+00:00",
      "head": "a211ab9b25ccdd2a6e52bd43887f24e33825883f3e0cf8ed68736a131eb76711",
      "node": "301.wake",
      "snapshot_digest": "02656f233af983d87cf048ebbc55125afb083b36a68428fd8fde2c35c3f82909",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T08:10:00.716500+00:00",
      "head": "3a2a80c95ca74accd04a9fb4b10da375368472db86bf329c2f460b303f227900",
      "node": "302.wake",
      "snapshot_digest": "cd06b9deab7d072f1f0ba5cfa0ccda8156728a62ca5817fe7a67f40fd03d39bf",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T07:50:41.870346+00:00",
      "head": "a8650b06243bcd050a4345ca8133f5aecedee2827e50805b920f201485cbfc74",
      "node": "303.wake",
      "snapshot_digest": "c3bfadb3291d7b0e8a6072fb45b62aa35de24d8e2ee7774ea511aa502c308e2c",
      "version": 23
    }
  },
  "version": 280,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d343631623439653866363634343833/63.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d353631313437366666333730346631/31.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
