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
  "generated_at": "2026-10-29T21:37:08.459745+00:00",
  "head": "snapshot:5bc72796a75a9dcd0088b7b11a66a2f68b99947d1a818d80fac76a059dab3986",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T21:30:38.637159+00:00",
      "head": "965b23c703b42466ecb0252d966f8788e3e91652d5c609f9a6dc179d17900ade",
      "node": "100.wake",
      "snapshot_digest": "651f821d02709b5dc3c006007782eb60533ca68a747874644fc2553450bd4f1a",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-29T20:30:05.661515+00:00",
      "head": "fc9e5fc0c12060c89ae9d8abc8a245376555063b2f9cd8ab93e5ccf1258270fc",
      "node": "101.wake",
      "snapshot_digest": "f0386985222ebe261a95bc803554ae8b952a566b33b44a936dc4ba88323f9a42",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-29T20:30:12.330356+00:00",
      "head": "132e02db57d5a72628bab2a5d079759f3956e632a245fe5b8e6ada63a0fd0c88",
      "node": "102.wake",
      "snapshot_digest": "d06fe77a2756c38a4e65594e18bb2cc801292860c3cab339ae3715868841a59c",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-29T20:30:18.782846+00:00",
      "head": "3a46d25d08359ee2ad2bc98fecb4241617ea582d112571214a71dd24ee7d00c4",
      "node": "103.wake",
      "snapshot_digest": "8229d7b2fc9cdf068813a25a97e187f46c7eb93c25e24fb7c3f23e5ff98e5ab3",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-29T21:34:12.656028+00:00",
      "head": "d0fd930545577459d9cd8847993a3810518b8ac7ec0111bc643f8ffff537770a",
      "node": "200.wake",
      "snapshot_digest": "c9ea94dce7e5daacf7c3820bc629399e45566d1b21ac12099db51a87c6a448da",
      "version": 31
    },
    "201.wake": {
      "generated": "2026-10-29T21:32:07.994393+00:00",
      "head": "f8d77256f19691f4704167c26327cc3e8b75775e0620c6faa79af110d0de9de0",
      "node": "201.wake",
      "snapshot_digest": "c1573d499f2d200b797d387e501a6837dc8ccdd0547682211102ce370e61ae2b",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-29T20:30:05.911179+00:00",
      "head": "45138bfaf231134fffb39c149d4b922051efeaf68dc46b858f80589f4138dfe9",
      "node": "202.wake",
      "snapshot_digest": "ece0b928eaf810158099d8010b1fe7436ab61b36c3b620d36f2c12d387f1cf35",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T20:30:06.669347+00:00",
      "head": "5ee094fe876a9ab308642361853c1c77a2f493c1a10efc3adbea078a426d4808",
      "node": "203.wake",
      "snapshot_digest": "cbe6f0a6c41d8cf01b0e83933c2837619a4b90433c361759dbc49e967b3ced70",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-29T20:30:23.180484+00:00",
      "head": "85dd0e64cce313b84916ab62aa653f1320682fc0ecf7c703dc260d44e73383e0",
      "node": "300.wake",
      "snapshot_digest": "163218f8a6cdfef4c206e6b3f85de7e58c55ae41c7adf7067378c19fe9afbc8e",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-29T21:37:08.459745+00:00",
      "head": "f043ddaa332c20b48cbe43ed9870ff0f31d572adc39fe9ab2b394903a17acaaf",
      "node": "301.wake",
      "snapshot_digest": "c6bfbf3aadd95870c0ffc338f2d84e55ea7646c6886f699d0551503eb8484b3c",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-29T21:35:37.391340+00:00",
      "head": "5a8f69bb4d0928346804beb777628f9221b742642d4aa6da624c22e552ab8d75",
      "node": "302.wake",
      "snapshot_digest": "086192fcfb5e74ab5611a6bd519281a3194d65a4800671c2e296dd465415dee0",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-29T20:30:05.521365+00:00",
      "head": "4cff53f5fd2c1df22014bc9969d523c8f26d0633a640b355fa9a8c2fe1596600",
      "node": "303.wake",
      "snapshot_digest": "dbf3836d39d991fae6e23f5bba3050c240f4222717ec227efc799a6c422b6118",
      "version": 24
    }
  },
  "version": 328,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d35636332666632313862303534376364.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32613563616434316138636434323936.json)
- [notebooks record](../reader-records/notebooks/3230332e77616b653a3a6e622d6d656d6f72792d6964656e746974792d30322d/3031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
