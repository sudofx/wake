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
  "generated_at": "2026-10-28T07:35:10.075088+00:00",
  "head": "snapshot:d49c1e9129fb3f4f0d6c5ba911d8ed5eb9a78d6904f933100d1643f8b4795e79",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T07:33:15.571012+00:00",
      "head": "755b3b5b8b821ee340b6998a6528a3f4db73e37f94883ebbdaf2a4f955494b84",
      "node": "100.wake",
      "snapshot_digest": "2f4e77ce83a20d66afbfb95876719641a9addc3095ad64099fb4faa71eca7f1c",
      "version": 10
    },
    "101.wake": {
      "generated": "2026-10-28T07:34:56.745420+00:00",
      "head": "8c663763580b476b334c9f8060bc66f902a80ad3ceb432cbdd7c2763c8f33d23",
      "node": "101.wake",
      "snapshot_digest": "1569d7b0faa475ef94a90ca7cde46c46c9b13f81184231fc27d8b661d8dd4bf9",
      "version": 14
    },
    "102.wake": {
      "generated": "2026-10-28T07:33:28.678871+00:00",
      "head": "e38c8aa31a163e89c90c5f7c1bf6a1867abf2c8221ba277db2c6954c9040d8e1",
      "node": "102.wake",
      "snapshot_digest": "be5e56a47e579338ff2744bf655c52eef0eb88c1b25b9fb70266cf7fbbc84ad4",
      "version": 8
    },
    "103.wake": {
      "generated": "2026-10-28T07:35:10.075088+00:00",
      "head": "01be8e66e5a5b9da8cc35960e2738275f296055aa4be1c44cb999bf78f537083",
      "node": "103.wake",
      "snapshot_digest": "aaa7fb605bc3249f47409e1c2c6c5800483ad3177be26e34e0596fe8c169d464",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T07:34:06.583455+00:00",
      "head": "2db995ce1a8d23f29ca3c28fef76c8a0509584674f7aecc5c743347bbed4913a",
      "node": "200.wake",
      "snapshot_digest": "b53d00a204c201d2d29626d2380c50765e7888a1bed5a1fa540d3b3b2a6a0151",
      "version": 15
    },
    "201.wake": {
      "generated": "2026-10-28T07:34:00.956918+00:00",
      "head": "6b77be6fb93917d80ffd655e21d776942ef1c123d7e23caf342052a1ee404024",
      "node": "201.wake",
      "snapshot_digest": "9359abf7891226292550d345a981f6554bdea231b11bd4a4d2c4262de3edd404",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-28T07:35:06.827385+00:00",
      "head": "fdb0df8353af391e6cd118aef7358a96e9ee3ee4ad51940bc0f7cd2f7da3dd99",
      "node": "202.wake",
      "snapshot_digest": "a29de9804f636eee08acaef05bf8e26a2bd893bd56fd3185ad0132b0c6582218",
      "version": 14
    },
    "203.wake": {
      "generated": "2026-10-28T07:34:32.198097+00:00",
      "head": "38ab6159617317c91e1eec9d18fe9fac3065c8c33f314485110e170f230e04da",
      "node": "203.wake",
      "snapshot_digest": "a7e6e5339e1484005f43cd07ff4215cca2a41df596f704cc237bdf9facf7fc57",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T07:34:49.327327+00:00",
      "head": "5a1f0a670f470ac2834338f5dee2e2e968aea5997cb3f95eb5f104ccedb54b73",
      "node": "300.wake",
      "snapshot_digest": "6d99fe3fe612619ac86fc6695793c2812ba2bb0d1aca09298b2a58b0d34b46fe",
      "version": 16
    },
    "301.wake": {
      "generated": "2026-10-28T07:32:44.462366+00:00",
      "head": "c8e59e8582c18527c1e7fbcc64876f54555a20e2ebd196a3116d666b7725e00e",
      "node": "301.wake",
      "snapshot_digest": "6934ade1ba0b55300fec29ebc885ed9c5317d02ab245b796cb76332f8df6694d",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T07:34:15.931443+00:00",
      "head": "13744f924ca752d18e42c4dbcf18c9fc74fc3e1531bdb5b1fde3dcc72c4fae94",
      "node": "302.wake",
      "snapshot_digest": "645c46a081f6681dde36def6677c254371b20170d98b5a925e9e15551ee1da5f",
      "version": 11
    },
    "303.wake": {
      "generated": "2026-10-28T07:34:17.543681+00:00",
      "head": "279ca16aa26b0d5b206bc0436e4f9f460198f91f2c997d2fc2def0157cef2331",
      "node": "303.wake",
      "snapshot_digest": "7d1c98fdb73e4d0aacc8e0660c1f137c264d6597aad1a17929f0b6f062709823",
      "version": 16
    }
  },
  "version": 163,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d65643163636138393265346334313936.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d37326530643937326334346134633235.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
