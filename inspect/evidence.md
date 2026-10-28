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
  "generated_at": "2026-10-28T20:41:28.109864+00:00",
  "head": "snapshot:aac6de09e0753877208ecff100a2de921df9cd7b1315db8adbb7066cae94ac6e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T20:40:04.835860+00:00",
      "head": "f36444ead945c0268b693bc871026569668bf447bcc3a14957ea49b200cfa54c",
      "node": "100.wake",
      "snapshot_digest": "bb74bae0e19f9bd71d6fbc122d8de20a8c78fdf42e627172b0f382d0e6a9ffa2",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T20:39:11.897843+00:00",
      "head": "7d2a25271c34b4bee65723c717a70b527fca63ecb079231796a1ad15b18df6be",
      "node": "101.wake",
      "snapshot_digest": "28e76b4024dcf39b8b6762ea33eb56a99f86639e771b93f6a9b64668338d34c4",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T20:39:08.313494+00:00",
      "head": "a365f9580957fb599eebdd30c116bc4e70e78a434217889e2b54a0e1b87d4cf0",
      "node": "102.wake",
      "snapshot_digest": "0aa33177049f53dd8c904569a4467e20ddfb0310c598fe49fd82b4d051e12f27",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T20:39:52.009484+00:00",
      "head": "668a9fdf1fab13381b978c80975a479f41c67cb562c0bfd0c32891afa404bfc9",
      "node": "103.wake",
      "snapshot_digest": "5aec18408ced7306b1f9fd2e99edbe26c2b7d92a8096bd97a62ee6deec0b3825",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T20:39:56.519110+00:00",
      "head": "6793e9ada679de74c68dbd9dcd793df57007c7d216c564384b387a1479e7daff",
      "node": "200.wake",
      "snapshot_digest": "cc7dbc318dcd0200a2a8a9abcd88c1863b4a4d78be87cb3a1e2ca90369842443",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T20:40:01.087506+00:00",
      "head": "e2a0ce76bc01ed056026e17eb3841da901f0d74e9aa863e784eddcb652f9199b",
      "node": "201.wake",
      "snapshot_digest": "2d0905b601fbae5b4ba199ec17a1ee19cd82b8e8db8add6d7610cf8aefe7847d",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T20:39:44.264455+00:00",
      "head": "6cf0e3b85fd32e8d3fcc5aedaa177b5de2c84901ab88889770f80b9e3280a53a",
      "node": "202.wake",
      "snapshot_digest": "266f2fa9e4dc7f7972c42fbea6a3b8b4a448e83299e810fdf6a2ee8798d957db",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T20:38:58.146077+00:00",
      "head": "fff1129c673e95be2b50cbd6ddd49f159f64156c15c38848a410f9de4d77380a",
      "node": "203.wake",
      "snapshot_digest": "a682a640878970af80b1f9bca23464d3082945274dae0e37ea48acb7470266d3",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T20:39:02.646549+00:00",
      "head": "321c6ba7ac57e8ee0f546ae225334f13fce5c89870d70e292dee57aa03c2f2a9",
      "node": "300.wake",
      "snapshot_digest": "e0768e54b1d69c82cb760183549370624b573baf683a4f95c14d9bc2858687c6",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T20:41:28.109864+00:00",
      "head": "ab0c56aad8b185899b0e8ad9a52e655deca80b31ea62e80c6f7fad27e9b7613b",
      "node": "301.wake",
      "snapshot_digest": "0d0cd0dfe34354463144b431866f0e8b1bbc4ee488df869b80e27497b321d010",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T20:40:33.772580+00:00",
      "head": "9865ed9c93f69db7434d5c34a7a4fe0f789fb8451bd98030ce8af00ef95018c7",
      "node": "302.wake",
      "snapshot_digest": "4caa3bf5f87a8ae9995b6eb7f4fe00851029af56b80034d627e18ac37cd27d4b",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T20:39:41.395905+00:00",
      "head": "e8418a47e4db96c6a6f3b10d99daa5fc045bd6127d52caac33c9a07b49f579d3",
      "node": "303.wake",
      "snapshot_digest": "0ad2a511e5d65d21e0f3cc0ead200cb6c232942e1ea4b65b61933c4544c2aac8",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d34323735323337663464366634386539.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32636432343663346566373834323434.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
