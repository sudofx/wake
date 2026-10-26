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
  "generated_at": "2026-10-25T23:57:45.730149+00:00",
  "head": "snapshot:cb471a1c99523b4e2b6cf972d1dac3c35ab20bc646102fbdf3376f593cb0e235",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T23:26:37.424531+00:00",
      "head": "4540cf51b60cf330f737cbfa9e9dfe1cab365a80df1a2380b9dd87e605e3f95d",
      "node": "100.wake",
      "snapshot_digest": "15e16118f19909dcdfb45d6d49ebab074f6020f29a7334409b7944952ea0acad",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T23:46:36.374900+00:00",
      "head": "b90ada85cdfac42f4edf6bd0acd70c51586b5ee83e7d787b48f4f34b1feb703b",
      "node": "101.wake",
      "snapshot_digest": "b837360e86b9cc001b96aa532daa5431cabdf556c3cc44fd8b2b70bf0344ce7f",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T23:44:03.543999+00:00",
      "head": "8ee85d70ffcf88697cb771e824329f4af45af3531493ee03d3effc0a608ca0fa",
      "node": "102.wake",
      "snapshot_digest": "3449b28c2f6a8f4531fe565daa4027d2e4483625fb7530f152d499967c59a134",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T23:26:38.780185+00:00",
      "head": "b660e4dc9b4f6f153e2f2a35b34bf366c2fc49f6eb70b131f3cf98b6dbd9429c",
      "node": "103.wake",
      "snapshot_digest": "9aa1add9d9fcba1a6c27171cc817acbfb7d1d6538ce14fc7da1e7d00e82ae020",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T23:26:37.208291+00:00",
      "head": "b93240fd046abd327aced762414303c502f5058473fce88f0537ad561ac6060a",
      "node": "200.wake",
      "snapshot_digest": "5e2cc7a886ab07c1a5a94a531561412f0cfd4ae416016b0d2e82c1ef7477d0f0",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T23:26:40.345540+00:00",
      "head": "0aeed16e7e3082106bd161a1f8d1e643ca76d07e7e9b999fa66663ec3c9bec10",
      "node": "201.wake",
      "snapshot_digest": "d2706d6c74aa4772aca877232a9ba25d13f7658ae6157452c369b954b5b60557",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T23:47:39.623262+00:00",
      "head": "4777671daa4ab9e81ac585a5fda136bda728bb097809b34c27a074341c7c7f5e",
      "node": "202.wake",
      "snapshot_digest": "2ca5022b231e79b2a7362880e49f8d32be3c26ca22e111df77b7ef3b1ce4a9d3",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T23:26:38.803001+00:00",
      "head": "69227005e81e8fa6fb2eb58639d470d132f630a26d42bbcb63a4f1274c73438e",
      "node": "203.wake",
      "snapshot_digest": "3c80d39a0e103cc65832905eaed1fe1aab78cae62b81186d7a5181294c582f93",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T23:57:45.730149+00:00",
      "head": "56efeab4ff1754552df6c8d298425365cc00f5949fb8af31f89515df290f1902",
      "node": "300.wake",
      "snapshot_digest": "9ee8bfff90a9a51c6f434058abc972cfcd1e464838681edd98154f254aae87c2",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T23:26:33.535776+00:00",
      "head": "7961392d437c0391fa7e190b3c4fcd6cc9720b05005d971e67b3aac9e73eba40",
      "node": "301.wake",
      "snapshot_digest": "096330f33cfc22f168001887f0bf7bba4efc775cfdec86547ae5e759870755ae",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T23:44:52.730689+00:00",
      "head": "cd805e772774f84acc64e2ad7be9e7f6097b9d36a5eca947c2ec860a64ed9804",
      "node": "302.wake",
      "snapshot_digest": "b069bc3d26595e4a9e8cc81b9b58c9c7212f0c36a52281eea5466517427555a8",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T23:26:40.042479+00:00",
      "head": "fb529f8c8c6dd523eb84176d6b449aa95031728d22119d19bcdd9b85de89ba1d",
      "node": "303.wake",
      "snapshot_digest": "77cfb8896a2254b3f82d7b6840d93430e12b54752999508637b8f4ffad1aa40a",
      "version": 51
    }
  },
  "version": 510,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36666161643235373966383934313230.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d37323434393862643835386134666536.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
