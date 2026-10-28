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
  "generated_at": "2026-10-28T18:28:05.839343+00:00",
  "head": "snapshot:0b198a2b041fa6307d3ff214aa97523e7763b9b81293ec4ea4880c7f491f6e09",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T18:26:42.820988+00:00",
      "head": "544fadea659f170efe73a7dbc1e0f5781ab6947076c911934cc757be08eb30c0",
      "node": "100.wake",
      "snapshot_digest": "20cb5f300e9f08d0bc169f7b334659a59f93d4d009a15c1349ef12e0ca2e1967",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T18:25:25.706915+00:00",
      "head": "df24125f1fcbef026766c24039541c3af19d42fc1f04277d13fa032d1433d969",
      "node": "101.wake",
      "snapshot_digest": "b7a4a45c90244c956385066c659c071dee1de530716696567535202885220759",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T18:25:29.128669+00:00",
      "head": "b3ed74e7bfb8806d57304ff48455972e7cc8eeb1eea9e3f19d04f4d805876df7",
      "node": "102.wake",
      "snapshot_digest": "8e130dfeb9bc7b52f04d5439da45200c9b7a5c4ad18277a5e429c97ef2f329a9",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T18:27:06.459240+00:00",
      "head": "feceee99ffb9238d4b74c58c00fd3a7d47528b3bc818d35da2a906ebe12a0cb2",
      "node": "103.wake",
      "snapshot_digest": "6c30d2c6e6b67b461f0d82ebae45a65bf4ab1b96cd0c2cd2eaad4e7e8d2fb29d",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T18:26:51.208380+00:00",
      "head": "487cf0d2f209cab1f20d868d102a21bc629cbc2434f74c028dcc749c58cb4107",
      "node": "200.wake",
      "snapshot_digest": "2796d3770d548f457d9895c5c5d58040fd79cad62c69f494584ba40a752d72a2",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T18:27:08.457539+00:00",
      "head": "8a2d5b63b41600dacdedc348bb55eeac9493ac9e9ff8f5323838acc77b552b74",
      "node": "201.wake",
      "snapshot_digest": "18dcb7524ba5ff39aea30517655d5ff733527d2f9d0a2b06740dd440c4a71a97",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T18:26:02.599020+00:00",
      "head": "6e32e3506d90f9687f5c0c01ef484b3c00fe886e671a6316d8a19eb1eca9ef68",
      "node": "202.wake",
      "snapshot_digest": "7dd509c40fcb0fc0afaeb7f25082e734352297c5823a3ed57fad38badae987bd",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T18:24:45.919874+00:00",
      "head": "b1df230ed9c17b6fc9a16edb6ba027b92797fd3d0fcad8a12e88e794f36ff75e",
      "node": "203.wake",
      "snapshot_digest": "40403d9b921a18b6eca800ba98b11b664fe8c8169793aac1aa7317e88ba3dd1e",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T18:25:23.722028+00:00",
      "head": "b2bcf19be45abee6c80236a7634baccdd2ae10ce974ca964996f3fe969d01c82",
      "node": "300.wake",
      "snapshot_digest": "333e6b67a11a9221dec48800853ece19144941fda91c016b42b8985b17f18df9",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T18:18:22.980327+00:00",
      "head": "6ba904fe62808ced2715e46dd96e8aa89a24facb54206ddd9d8e2cce149a0e31",
      "node": "301.wake",
      "snapshot_digest": "b6e272dd8e6d62e17accdb3cfefb621cb72f8fe344a1bd2f0677d85ee22c75a3",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T18:28:05.839343+00:00",
      "head": "6fb715cec2e316be10c91db168c1432db9dced5888abe126253621da1dc6f198",
      "node": "302.wake",
      "snapshot_digest": "91f4436d5ad230f74f0205672b26ff0969a1c153479afcb93fa393b6d36693fe",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T18:25:41.918708+00:00",
      "head": "e207f3a57a4aed6cb28be8b82d059af99701f5459fa72536af19093a839fb5cc",
      "node": "303.wake",
      "snapshot_digest": "0ba01d048559a08fc3e8c20b90679a68bdc08c0c30702b8eea0635b8178e7881",
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
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d39643636666531653238336234363433.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d65646632653431643565663134363237.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
