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
  "generated_at": "2026-10-28T19:08:39.283828+00:00",
  "head": "snapshot:ee2ba29c1818ab1345c855b22de66534445d81d2719702380403dc78ed0e012e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T19:08:07.711680+00:00",
      "head": "221558fdd326cec438ad4087200db36bc4f4b3ff5950febddde316ec77418a8a",
      "node": "100.wake",
      "snapshot_digest": "c0d2b6d3512e1a8a570913c14d5cc9203f7a9ef2649c84250df499dc8f20fda2",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T19:04:09.000695+00:00",
      "head": "dc7ad637166e710a1dd5d275a3636fdf23b1a296d77037ec0ec34426b1b107e7",
      "node": "101.wake",
      "snapshot_digest": "2a1297824d2f82e638559d82a3c70d87861d8ddb5cb846477350f182287102c7",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T19:04:52.961841+00:00",
      "head": "cb64f2cb50f83657f44c3993ad9a16149c3468d35cdb57308baa70c45f8db530",
      "node": "102.wake",
      "snapshot_digest": "28b40e3c981495cb1f36a517175646eed08221ca8a41b1d15f346b045940b406",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T19:07:56.851744+00:00",
      "head": "661827c8bbc999474de0b31bb32b1bb91f6a4ab7690f2aa70ef43d8079441b62",
      "node": "103.wake",
      "snapshot_digest": "7afeb3630afe557ab33e11dd14e443720f1e16e04efaa35c2db54396373461ac",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T19:08:06.346192+00:00",
      "head": "7acee203d2cb18021bc063a0470a00abe9fda94336bb5212edde75f00a77be70",
      "node": "200.wake",
      "snapshot_digest": "ab836fa51388bca1bc67b2b3f92fb8329fbc20bf51ffa8cd0faa9fa912824590",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T19:08:39.283828+00:00",
      "head": "c069ea76ee9828df58e54578a369a4e576608e22a9a0c82323b4c10468bd6822",
      "node": "201.wake",
      "snapshot_digest": "7c6dd4942a8d0925c85b22d0bd01d991049262c62ac481e1648028afc09cf8db",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T19:05:38.847234+00:00",
      "head": "0bbb50332b3b9d7e64b191bcfcdf6a47c9103dd9583eb6e4454cc0f656316550",
      "node": "202.wake",
      "snapshot_digest": "e2c7cb1454b2cc47fd9d3d32c54bf1979556c6234b656782c247ac528fc4a424",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T19:03:10.524670+00:00",
      "head": "af30be67212ebcda82eb3c0671fe8758347a2925b32148cd79d5650e34bb425a",
      "node": "203.wake",
      "snapshot_digest": "d3e8b0591928b17dec384c9fc09dd734269c25d4af06a93fa91d23a40f2f23af",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T19:04:29.100689+00:00",
      "head": "fc450eef1e71197ac2dcddd2033ea1e005b93c7a8f5cf50febf5d56f3c43811f",
      "node": "300.wake",
      "snapshot_digest": "6b6b5497cc524ed59a1bea09c801133b7f7fc02bf87c45a5ce5d32e3dda079bd",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T19:00:58.079625+00:00",
      "head": "99c8ba6a3b1a6f01ef5ee49a2b1ffd8ef4e2b179e5ddf74c23b42f25444a260a",
      "node": "301.wake",
      "snapshot_digest": "ece9a2601e566d67d787e0be531e237ceb20ee38de89774779f80249a47987e7",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T18:59:52.313846+00:00",
      "head": "21a166dda2d8fb2c0d88a68a78fbf947b76dfd82ca2489af97793c3bea3c02b0",
      "node": "302.wake",
      "snapshot_digest": "b994fe235df828853b2d47c21cb6aff65c24c6b3e6da6007838675167814a0e9",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T19:04:56.252412+00:00",
      "head": "39b6a2146baac63cefac182eb933bf9c4fe2c547f130ce3b20643466b9c0ae2d",
      "node": "303.wake",
      "snapshot_digest": "404a34591ef5d37aba809954ae25f013bad8d3c00b8c9cbcf0c66d9804dda649",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d66666162666231663866666634356533.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d64353662373235363036636234633662.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
