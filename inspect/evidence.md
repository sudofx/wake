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
  "generated_at": "2026-10-24T19:46:57.356565+00:00",
  "head": "snapshot:d044f224c250d6f880b9bac0c46a1c1d5439c9e9923b3a6c6c1a8cc8c2ce8281",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T19:38:19.891342+00:00",
      "head": "99f76ec9f865f1273b1ea7919e781c05d9ea5b1cddf8a994b27c5e30dd1ea9c7",
      "node": "100.wake",
      "snapshot_digest": "7713636bc6fd75215196d2efe9b73d53b530ec6487ae99d8b46467bd6152af56",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-24T19:40:39.795168+00:00",
      "head": "3aea38e418c78be5a9cea88a4e21b0b5b624f5f31ffd99829a55c1a4787e780f",
      "node": "101.wake",
      "snapshot_digest": "517abd10cf94bad1cc6c65ddd7bf71ae9a6c911dd92979ffb44b49d5a54c241d",
      "version": 38
    },
    "102.wake": {
      "generated": "2026-10-24T19:46:57.356565+00:00",
      "head": "c654608a8cc5a04f6b7bd763f0bcad11e159ae10c3098d9420f313d2625a294b",
      "node": "102.wake",
      "snapshot_digest": "ed639781a7c5bb8f6700cba5b5e4041e38f3de78fbaaeba8d510c67ee8f45da8",
      "version": 51
    },
    "103.wake": {
      "generated": "2026-10-24T19:23:19.130798+00:00",
      "head": "2c1253d1dbffd47a3a83af2eda28c6e4d5429d8f5935a765bca8877f5fe545d3",
      "node": "103.wake",
      "snapshot_digest": "0086efde687981d17b900f0b845b93ab7e222158c6b25c9b632a9efff53c225c",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T19:21:31.496451+00:00",
      "head": "aac61b211b4d53c4322ebc35985be1b6cf96006aae379aacaaaba96888c3c94e",
      "node": "200.wake",
      "snapshot_digest": "0dd65d831647d865e06990e24b19777563e9f02af13e53ee8c2bb1609a673205",
      "version": 29
    },
    "201.wake": {
      "generated": "2026-10-24T19:20:50.207731+00:00",
      "head": "5601677c3edbb74982ecbb0bfefcbcfb230778851ddcc5939e73d1a009f435fc",
      "node": "201.wake",
      "snapshot_digest": "2bea4552b32914b0189c3e9cd1dd30f35259492b547e04433a36d2c7d134ffbf",
      "version": 34
    },
    "202.wake": {
      "generated": "2026-10-24T19:21:03.965494+00:00",
      "head": "b549d05f493c8c0f11f7bee0dde6cc2c69ab3539cf1447ccb6f64a0ec9104337",
      "node": "202.wake",
      "snapshot_digest": "e0d32cba9de4a15eda6b16fdc68a3adac871702cab6c547f0a3022b782c8d3f5",
      "version": 47
    },
    "203.wake": {
      "generated": "2026-10-24T19:20:37.858407+00:00",
      "head": "b4d48167a0c0f089065fed51cbcb84ee1d318457f6d704bb38917faba053a2e4",
      "node": "203.wake",
      "snapshot_digest": "6ba6f97f2e3e4edad751e7c71de3733fd5e3c077f79d4b21e1e372e27b71045b",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-24T19:17:41.719558+00:00",
      "head": "0a08f9505830b900fce52d039c9efd1fb0bea9279d19110d33275eb177b78581",
      "node": "300.wake",
      "snapshot_digest": "bb41b154b82f6d486c15ce0a71192621354b3c58eb633ec221478d3b0afe5343",
      "version": 30
    },
    "301.wake": {
      "generated": "2026-10-24T19:15:42.117899+00:00",
      "head": "0659d30ec6b2c97b845f4d3544b2e9948d1b717ec6743851bbabbde714c6b7d7",
      "node": "301.wake",
      "snapshot_digest": "1610d8f3aabaf7ba23a271c5e96ec8dcfc0bb52043a315bb6f2f2b133a5b2e7f",
      "version": 48
    },
    "302.wake": {
      "generated": "2026-10-24T19:17:53.206437+00:00",
      "head": "752d5ccc163b4cb2bad8b6d6205035084381f67af454b5e4365ce8b38f5ebcb5",
      "node": "302.wake",
      "snapshot_digest": "7a165bb5d6a6342e2d1253a81018f9caa143e6a25d1b2aa59b62487983bbd15f",
      "version": 27
    },
    "303.wake": {
      "generated": "2026-10-24T19:20:26.593385+00:00",
      "head": "d37ea6fb520c8875f0a0f8676ccca2ff46983d0d492fdadf24724c807803fcf0",
      "node": "303.wake",
      "snapshot_digest": "8c6dd473820cc4de585ede27b50ed58f3842d717e33fd9703fd4d1e6033c52b0",
      "version": 47
    }
  },
  "version": 438,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d643261363137633236646263346133/39.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d666232333531343331656262343738/31.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d656d6572672d70726566732d70/6174682d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
