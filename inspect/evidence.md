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
  "generated_at": "2026-10-23T02:44:53.974772+00:00",
  "head": "snapshot:d2feaa7da4203a690742a0b9a0f802424478f2e100b661972a1a2059d6ca79cb",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T02:44:52.897773+00:00",
      "head": "0e55017388c316d6f3432fc13a5c4181c82084d88a5213ab2007e923aeb2797e",
      "node": "100.wake",
      "snapshot_digest": "f485a7b9c908508cf50835907946f034197d057b0adef12dcb3f258ac721f311",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T02:44:53.886732+00:00",
      "head": "e5acc7fbc212f8cdd82535973da4b1439df73143123e571660b1d1ab6bee47f3",
      "node": "101.wake",
      "snapshot_digest": "ee198af71565439b1243ca3ec0e464db86de322475e5aa9f82cf4512db42c905",
      "version": 15
    },
    "102.wake": {
      "generated": "2026-10-23T02:44:53.312378+00:00",
      "head": "6d6d3b97ad8114042fd9411dc37c89f10b0f08f93e666520172efac0970d1696",
      "node": "102.wake",
      "snapshot_digest": "8468a81aee1988a2c055426d944fb30d62c3c8e2b315fdb9c6fe44ba7ad35ad1",
      "version": 14
    },
    "103.wake": {
      "generated": "2026-10-23T02:44:53.192371+00:00",
      "head": "f6d5c1d0278d040bb24836f48cab46770f03bc4bc68ee8e14861c4e7395730e2",
      "node": "103.wake",
      "snapshot_digest": "ea11d3189c3bc2ce6bed10c813ca8d8ec7d9eda5661db2ef5dcb3fa916d7e007",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-10-23T02:44:53.563977+00:00",
      "head": "e8a6ea5af19043ae5b600026fa2fb55fb12801a3367a500c91d54153885d4837",
      "node": "200.wake",
      "snapshot_digest": "464c86a7ae4b3eebe2d8537607634ba3e4b4163237bb1fcc245a2cff4ceab581",
      "version": 8
    },
    "201.wake": {
      "generated": "2026-10-23T02:44:53.172973+00:00",
      "head": "8d5ffd66859df9ae4ea9e5e7a282af3c367c073c00ef9f04ab2d0e314205cfa0",
      "node": "201.wake",
      "snapshot_digest": "65143f64871c2539a570db524f8e834c46d9158944314ce085229ab6759bdbb3",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T02:44:52.430734+00:00",
      "head": "4c6574dd132820453f0a564f773144559eb69360d4eb1562f95d461007aab9e8",
      "node": "202.wake",
      "snapshot_digest": "7ce20c48fb8c7e14c1cae496170aa98abc2816ba259b90626e2fba3cd12c30a9",
      "version": 15
    },
    "203.wake": {
      "generated": "2026-10-23T02:44:53.686696+00:00",
      "head": "74eea087e15ce8982e425ae15646db03929286dc1356ee7d6038efb253cfc5a0",
      "node": "203.wake",
      "snapshot_digest": "57cd417070249da47ae895adeb13778c1641f14f4d6c6a3c64ac03373be578b3",
      "version": 8
    },
    "300.wake": {
      "generated": "2026-10-23T02:44:53.261891+00:00",
      "head": "5b6003c4ea3491aad3412ed861115319cf0383f7a995b064cec112a98f8d6fde",
      "node": "300.wake",
      "snapshot_digest": "59d800072e9083b00ce06eadccb7ac8f97435c4f27555179aa5099f175e16f66",
      "version": 6
    },
    "301.wake": {
      "generated": "2026-10-23T02:44:53.974772+00:00",
      "head": "0ea8ca902766465bf32d8c25012c8a3e60ba745264306fecea48abecac23d150",
      "node": "301.wake",
      "snapshot_digest": "f5cd4bf3c2cb9c7abcd8df65874a0301198d8781564f39990fe31f81ccdd8ab3",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-23T02:44:53.309384+00:00",
      "head": "958df55cfeb6ad97cd8cca6c033a82abb0cf4b11daf0281f6160c8b6186f40ce",
      "node": "302.wake",
      "snapshot_digest": "e18c248c1bee7bf160147a827aba304bb38230929b71573f8339713ae2b58dab",
      "version": 8
    },
    "303.wake": {
      "generated": "2026-10-23T02:44:53.941411+00:00",
      "head": "4d75ea3d5dfd22e0187935cac1227930a3726aad28eeb1113dcaf13f36e0b1f4",
      "node": "303.wake",
      "snapshot_digest": "9de719a25c12ae3f836ef880cea40f4d26125b88c2902f0ec49b465a0c1f0dc6",
      "version": 19
    }
  },
  "version": 129,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d343461616562303933616637343462/63.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d626633356466303832326637346131/30.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
