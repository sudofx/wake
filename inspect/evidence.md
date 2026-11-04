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
  "generated_at": "2026-11-04T03:05:11.587148+00:00",
  "head": "snapshot:b8fd80e95eb3d0ce530b0e975ec4eb7c65aa2f7d5057eab676953e174854f7ce",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T03:05:11.029392+00:00",
      "head": "8254a70f683ce5bbf443efcc820c5d22d2c6f7154e7df592265846f9cfaf34ae",
      "node": "100.wake",
      "snapshot_digest": "6b3b789edf12c98ec8893e274454510982d505d70c8a36dd17880177dba1e4cd",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-11-04T03:05:11.452850+00:00",
      "head": "11193d1c15798a8570fc8411202c824a657a15a6c2b8c83cb6b053e5101966a5",
      "node": "101.wake",
      "snapshot_digest": "6ec588989a8eaa28017cd8b206489e4938e9e4f41e5c47ee89422125c27c9cc2",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T03:05:10.822271+00:00",
      "head": "f152c9c4d3f21a5ede3c4716d91d75af97dd555e5606577cc8716dbbf15ead49",
      "node": "102.wake",
      "snapshot_digest": "4cabf85019f2c20ff162659d7b3261d4f1ec60c37f5b217614d4db0f5cb58b52",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T03:05:11.163139+00:00",
      "head": "c61c9f09565bd077a90b9ef95872bff114ea765bcec5dec4faacc523fb29a290",
      "node": "103.wake",
      "snapshot_digest": "f74180d14cb92c99ee70eb7845d186b53bf30e5776da379edd217d12c7c84543",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-11-04T03:05:11.358795+00:00",
      "head": "a163581d00468ee7ce589cbde15f7d7d35a946dd036942d9aa055e6498639450",
      "node": "200.wake",
      "snapshot_digest": "535dcb762ebc1efe7a74d33b8670137283500043baed2933e574639106308399",
      "version": 6
    },
    "201.wake": {
      "generated": "2026-11-04T03:05:11.203320+00:00",
      "head": "65cc636c4359a851324850db1d2bbe2d94dcaffbec7b3c1aa7e04b076e946a42",
      "node": "201.wake",
      "snapshot_digest": "e213a7e8a899065e6c19b02994daf2ed33194c8de623fd0ebba1a3bec4f4b4b0",
      "version": 3
    },
    "202.wake": {
      "generated": "2026-11-04T03:05:11.096223+00:00",
      "head": "130f2ab7c7ccd4ac9f5ef9cff722861cd75c57137b7209701b20fe220b984d6f",
      "node": "202.wake",
      "snapshot_digest": "1a688ca90b4e06a1c6ab55c2da4f05590de866d0252562bc3bf8f3dcaca0aa59",
      "version": 8
    },
    "203.wake": {
      "generated": "2026-11-04T03:05:11.587148+00:00",
      "head": "cffed390ecac1c8eb90303e6e3b8eb802dea894f0c225102cf49fdd90cb5f682",
      "node": "203.wake",
      "snapshot_digest": "95efbb39fb474b9e00cb820502c7a66adbd98c1c6e6419eff71de05fd13cc46a",
      "version": 6
    },
    "300.wake": {
      "generated": "2026-11-04T03:05:11.582166+00:00",
      "head": "d084031eb0e3ec695db3772d32cc26a7bff048cfe36ed789dbc7eb5abd47fc50",
      "node": "300.wake",
      "snapshot_digest": "7f28a92ba251ebfc7e8018156e6f7fbcdc2fd00783373f819eef81f2367dc2a7",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T03:05:10.835468+00:00",
      "head": "8e3e91aec008b3562d540bdd8a2e2451098707002ec2fe58df169119425a8c0a",
      "node": "301.wake",
      "snapshot_digest": "7f45f131ca1580e61a73882ee50f059dd88f96368e4b551f5d2ace5b8000c810",
      "version": 4
    },
    "302.wake": {
      "generated": "2026-11-04T03:05:10.730199+00:00",
      "head": "2ae62ecff998e6759298d25c0e285a95c523dd4deb7e664245bff7f671b80ba1",
      "node": "302.wake",
      "snapshot_digest": "f21bced85392672c759b8442515b47b5bc11bf8a9b75372a248ca93f04ce41be",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T03:05:11.088371+00:00",
      "head": "2e8f3f69ee9c43f610e399a6611498b48eee4e1c2aaabff476af6c3c7c1a5d78",
      "node": "303.wake",
      "snapshot_digest": "6f0f8e0e7de4c889b86fd8a9ad4d6b34fc527bd31b953e761a594c59e0abbc18",
      "version": 8
    }
  },
  "version": 65,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d323631646538373733623739346433/61.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d663961353830346561636332343863/35.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
