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
  "generated_at": "2026-10-31T01:15:03.992176+00:00",
  "head": "snapshot:2cb97571869d09d5916ff50b8c3779f26418bc71f4ebf0a5671fb4881e1960b7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T01:11:34.345383+00:00",
      "head": "85c1f737b1bb5d80682595d304c8ef56c793f9feabf3c45f1b032cea58a28590",
      "node": "100.wake",
      "snapshot_digest": "96b95940afae21006eb06f1f9ae428ef8c7c0464c593e9235c1761f0b0ba4a8e",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T00:08:15.473497+00:00",
      "head": "924e19856802417e8157ed5232921b08f2e78af6d750e19784cc85a2022e65fd",
      "node": "101.wake",
      "snapshot_digest": "c2b37eb0e8200a09bf30d8c905d587a559f0d1bd4fb5c99d3030f0f1ae076499",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T00:08:15.757721+00:00",
      "head": "d4b02b149cbe71e2cef33bb5e18bd401b729907e931b2d0c15cf81dea8d6be40",
      "node": "102.wake",
      "snapshot_digest": "0dc1d6283e1cf6ba6c47c68646e76145a2fff7abd1ea8688d7a761d2963b0515",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T00:08:17.240154+00:00",
      "head": "b8d541838059ed079b39fa4826f37f42703790ab2d951c6af0224d3ef4f66daf",
      "node": "103.wake",
      "snapshot_digest": "b641cf3a5c3673e8d5ec6df97e1ca1ace82ecaf21a256743c3d733965a18852f",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T00:08:30.607487+00:00",
      "head": "a9797798ab2b95e46a3dd12d17d7cb354e2b778b76810071c162b3b2975e46ad",
      "node": "200.wake",
      "snapshot_digest": "346cd3f6e789e0e1e1f1f0992b741ca2064538497e84c994f6c21484465e34ad",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T01:13:12.155515+00:00",
      "head": "b8d158f05567ed547a5c2a6acfdf29736f71eb8e0a603e197b7c8f33b3bb45cc",
      "node": "201.wake",
      "snapshot_digest": "d2eac082ce380926d985f97a0012c64df26cb9c0b1edadd190434db1c37856a9",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T00:08:11.534630+00:00",
      "head": "79ac379ba95e041a792b165f39f0bc30c58f7021018ea61f636dcfc07425af89",
      "node": "202.wake",
      "snapshot_digest": "3d6037c298855c543f048182d52b60a76c2779672dc0263c8d34983d528468ff",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T00:08:12.244476+00:00",
      "head": "59423d382dca8b6a498ecfe75f32dc5be7fdf3b26bf64fcd2fafd225c14d12bf",
      "node": "203.wake",
      "snapshot_digest": "333951dff3a5123b9859704bd261c6bed2f07f5ccceda75642ac00af89534802",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T00:08:30.357228+00:00",
      "head": "4878df560364c1df31ecb88df3725e4ae423909092a18caac75dfdde5c3aa901",
      "node": "300.wake",
      "snapshot_digest": "b93fbc6aed5961d7aaf8318190883301ba5e1149b4476242220e824c24619322",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T01:15:03.992176+00:00",
      "head": "b56005cc5799c29d300a0376245ff75c94478f006f7caeaf065447583c6e7de0",
      "node": "301.wake",
      "snapshot_digest": "2488c523abb17559831e7b98d8c29f6af740c06e2a5fe4d16f4572c117b84aa0",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T01:09:44.647595+00:00",
      "head": "6aef8d08f194a761d21e1b8ee0e3c13426091d05828f22556d781db0a6973d7a",
      "node": "302.wake",
      "snapshot_digest": "24133eadcc789db4179ffbaab6dcc032b66841d0affc695acbcec965d05a6764",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T00:08:13.267602+00:00",
      "head": "6229bb988b0501413f61448bee791514c19ac08cbef19899b2c4a45bea483a7e",
      "node": "303.wake",
      "snapshot_digest": "08536cc6ed9ba4151c82316170f74855e08cccbe2e32b705e83b0da01cb779f9",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61663234633138303635366534656238.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34633262363731616631383434666364.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
