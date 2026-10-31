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
  "generated_at": "2026-10-31T16:19:50.414863+00:00",
  "head": "snapshot:83809853e9de21910b5e58ec77c63e36327bd4cc2e1e5f8e8fbca29c4372f066",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T16:16:35.758008+00:00",
      "head": "d8ce57e9efc1ea0ba64158677fed96fc88cdcc3a0466c09a5e81fa8ffa6aab84",
      "node": "100.wake",
      "snapshot_digest": "488656a7ca5ec9d7fd5cfd7ef08a4933483d8192d2c90ce132a61988cec30cb5",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T14:13:02.348956+00:00",
      "head": "14b3cc74a859cc89878a8d9f8d2ff17aa95b950c1b6c26f3c91aa1ef5df02c4c",
      "node": "101.wake",
      "snapshot_digest": "4b1e643c6b5aa7e55fecc0119a5473bc0b779b376142718b27417dc17b8fd200",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T14:12:58.179695+00:00",
      "head": "eafb89f2de7368506a22f94dc96f6d6052d1a4a8d0e6e64e0a15faa922621c02",
      "node": "102.wake",
      "snapshot_digest": "f6eb1e7721ef2ef8e6f123ab4fad5d65f96e53eab94a54d9b8de358f4d71e23e",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T14:13:18.264030+00:00",
      "head": "6b0b9ea69ba240d919914304a22f9ed3f78088ea15ad83a7a4aab72a7ed45f8f",
      "node": "103.wake",
      "snapshot_digest": "04776aad782f8ebd719ca41eafcef03c77525a66d931ead156f2ca94c847ff59",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T14:13:23.212448+00:00",
      "head": "b8d14e19edb9a247714a8e7367571cc5d268c48c5acc137a9984491e4633c056",
      "node": "200.wake",
      "snapshot_digest": "7a18490bfb4cd9c1fe0bdeb11b71ed71e5eab12d00b3d47b8cdb47b9f42d4f28",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T16:18:52.474645+00:00",
      "head": "7d5cac7dea529b5be61182c91eeaf4bdb064a162923570c4ed17dd45cc797a98",
      "node": "201.wake",
      "snapshot_digest": "a24cfe66d3e71d882414e6c04ef0099c2982858d4048ec6ff07ff00c49943bf9",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T14:12:57.060164+00:00",
      "head": "171269ddff1b438e553dfe76090be06ffc1db15e06ed419ce1035dbadf278c6f",
      "node": "202.wake",
      "snapshot_digest": "b4a7450772d7b97c49e622425fbf402581396b5a84e36852948a7a10a993106e",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T14:13:00.692308+00:00",
      "head": "daa2ca6bf2cebf453488a92dd79c707ad475e3d31e184c6d3a50a9edfb46a7e3",
      "node": "203.wake",
      "snapshot_digest": "5011e4277915a4c5c7e431f2fc79b62d4f5694279944e729521cf1ed413f1284",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T14:13:13.068832+00:00",
      "head": "01694650feee1554b890efffd6a4c8bc1b3f2898af1be698719d6402cb80f589",
      "node": "300.wake",
      "snapshot_digest": "1ab7fc6c7873363902d85adf886b2811e12d427b7d51654d71b1664580fa448b",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T16:19:50.414863+00:00",
      "head": "26332a1604a84c34787063cecee73423c0882e3d98d7bfed6b7aed3a5fbb0f49",
      "node": "301.wake",
      "snapshot_digest": "18cfb3ab3eea82ec861350a28a7c7ea85d63709ea2f932d3b6437eedf9ef4cb6",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T16:13:26.863086+00:00",
      "head": "71e871d4e70e2dd8d99fd5b2eaa52b84bbfeed851eaeed936fdf5dff46e64356",
      "node": "302.wake",
      "snapshot_digest": "9ac39ca45d63962dd278a9a8ec4a8b5349ac2a0b4aaeeea855eb86b81a4399a6",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T14:13:01.557997+00:00",
      "head": "3bc13c7412854642cb4c0a172c3dcf025806b698eff6b6a0de00d970d1210946",
      "node": "303.wake",
      "snapshot_digest": "b45daf592c23847856d7de65e35b5d24b6a21fa1219cd7541cc686e9f5493996",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d35353434366636376134353734306565.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d33303165663864343432313834366235.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
