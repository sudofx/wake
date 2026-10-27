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
  "generated_at": "2026-10-27T16:19:39.533118+00:00",
  "head": "snapshot:da4c549075c149b66bcf80751cc250928beb2d736f461bc6b0a4217558ab07b3",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T16:19:33.311349+00:00",
      "head": "35facd1c2e266d364e02779b8a808619d30484612c80b54d7eec94642b2b997e",
      "node": "100.wake",
      "snapshot_digest": "4ee306f2e40bfcb71bff21c1435e87948483975689746051b1f9631ece9885b2",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T16:19:20.999948+00:00",
      "head": "399a4d8054d3968d4bc19986b489ae58765c13e774c4b20436b9d2c51d581b9a",
      "node": "101.wake",
      "snapshot_digest": "175435b6e7c1be6b1b6e8efb5df7c08c54f36a8c2e5d027b58d3ee82dc70823e",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T16:19:20.675678+00:00",
      "head": "11ec23a6bc180dc33301acd6fa3e8691ce5d261bf7a6c237e79e546863d11f9d",
      "node": "102.wake",
      "snapshot_digest": "21157fbe419cb4f37ab6899e03095388ab141f78d112456aa64c835ac6af1f0b",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T16:19:37.195240+00:00",
      "head": "9fbb82a09d64874f31512089b4d672fdb2361579995b703289021d06fc6a1e14",
      "node": "103.wake",
      "snapshot_digest": "7273ce6211b17ff570be4c9ab9d7da33da89adf6b00ed14064ddc2ba0e22a46d",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T16:19:34.405565+00:00",
      "head": "af223e53c69a5eb5d1d485b56e94165d9a43de9833ecd4912550da5a1c0f3b97",
      "node": "200.wake",
      "snapshot_digest": "36f135b6424b2930dadf09f5c7e8799f4490d18df1d72b580a70c8c384f883f2",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T16:19:39.533118+00:00",
      "head": "685b627670f77883cb2d3b636cddf0a642c1d3b33c49df9c13b4f3c4d6131f6e",
      "node": "201.wake",
      "snapshot_digest": "c5d25acb4006791c0e96e5f51a78c2444f40cff9c955cbc1598b94df911d550d",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T16:19:18.197638+00:00",
      "head": "75992e8c66f5cb7f9654a82720cba52db292906caffa239b0b151deda932d879",
      "node": "202.wake",
      "snapshot_digest": "459e9f7f7fc95ce91c33dfee30708f87d4b47b2b68ba272f99f43d08edb51234",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T16:19:15.437750+00:00",
      "head": "e8dffcddb940262e1f90acf6c1e9a56819c12caaf8299edf815608c97d2a9705",
      "node": "203.wake",
      "snapshot_digest": "f38ad3d65824f0cb0e5568ebbe89b426ca2aa49f693aad01aee7684c64327d69",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T16:19:11.862370+00:00",
      "head": "231d9dbcf59b44bcbb7e2841603ecb25321c7d414a32807d470bae701e5b0151",
      "node": "300.wake",
      "snapshot_digest": "b7f8de24cca1d7e057658d4c23a53c035438613006662490baa6598e878e778d",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T16:19:13.813496+00:00",
      "head": "6f369fa426e7964a4d1767f9460733c40882f0bdd31663053712000f6f6ff0d6",
      "node": "301.wake",
      "snapshot_digest": "c7c689c63d2b9b9a2b5316aaf06a9476e97bfc00c27d8f25e0c967e7d59ee9cd",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T16:19:15.913351+00:00",
      "head": "367e8c1cfdf695565f274192ff20157b85331dc7d9cb9e633091cc730b199667",
      "node": "302.wake",
      "snapshot_digest": "6869d444fae19b6841834d749a91f218370fac3e6b60990351f5176c3c57c902",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T16:19:20.365015+00:00",
      "head": "7a4595053a872a4fe119c240957f103bda7861b05d5a140d93230bc8a1cb9831",
      "node": "303.wake",
      "snapshot_digest": "7e5267994f27c147e896c1d1845b8e4119f60faddf06b1608019db2fc0b4b984",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d33366632373333613937373534396136.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d61303237663535346231336334653731.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
