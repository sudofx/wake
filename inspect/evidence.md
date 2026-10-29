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
  "generated_at": "2026-10-29T02:27:47.840296+00:00",
  "head": "snapshot:b3c0eb44f502c553710257269e7a65b6953c840d6fbd31acd22cf24e9ba1b527",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T02:23:01.570447+00:00",
      "head": "cc957681f47ddf6985673c350d2bbdeeb8ca96d1766e1b056e712348681ca45b",
      "node": "100.wake",
      "snapshot_digest": "fb58ee22fc3bdd0115e8c9bab8cbdc15e4dbd581a08095af06943d6dd4a4a0e4",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T02:25:34.672578+00:00",
      "head": "6cf92866d37fa40805bb17c35f71e6accdc7bea29ba85638b6acec9277ee0d02",
      "node": "101.wake",
      "snapshot_digest": "1184185f1327314052828212d9e7be21a6b8e90c9405b697fde27d4a9c37683c",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T02:27:46.810199+00:00",
      "head": "442d4760d70b7add05de98d9c76d2209b6e17daf2e185f4ceeebf3bbb5c12e7e",
      "node": "102.wake",
      "snapshot_digest": "309e3902a2608b6c4ed8fb43e4842910bf652497043c88603517ac78ce7fe8a8",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T02:24:30.930742+00:00",
      "head": "73605a476347869625013cb9b09bcdb4f08b6fe2d680ead1397ff1bdda734b8b",
      "node": "103.wake",
      "snapshot_digest": "eb1003a3b8fc4ea69e7ccdb5a084950316830bbe41538fd312f50adb4663ac7e",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T02:23:24.244817+00:00",
      "head": "31311ab8be80fc94aa4325ae388996e7e91755c87f369c8eac86408cae922a59",
      "node": "200.wake",
      "snapshot_digest": "589fbc5e637c614e3892b8acd0cbe5c7b12a180af620d30c755439a2784c73f6",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T02:24:32.941827+00:00",
      "head": "7a5d58e0ad7e62a76c0969caa18cda7e6260dfb9923f306bdda7eff8e3ffd223",
      "node": "201.wake",
      "snapshot_digest": "40dc8ad2c11a3b87370881e3bc2657dd06987b942b9d8bf2b952e358a5ff483d",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T02:27:47.840296+00:00",
      "head": "b3212fa86d75634a1dbb90ece06e222bfaef843397cf4f1bfbc51833a5eac54d",
      "node": "202.wake",
      "snapshot_digest": "ef02b373b2238786cc6b11b56c90547d6e51311b41f6b723a58097ec9baff76b",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T02:24:30.752914+00:00",
      "head": "1da96d58e6899dea331cea96272fee42f7706f8c334c8ecc465c25d096067760",
      "node": "203.wake",
      "snapshot_digest": "8962df101611cac3566c22c24835c1a37f5b3290001a21a77d8c96a3cf03d4ee",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T02:26:30.369340+00:00",
      "head": "77ce068a5fe332624d84b570d1d88c9239ee339bfc4098c5fb3d1c275fb5fc8e",
      "node": "300.wake",
      "snapshot_digest": "36d75324d4d98bed8bd1d7a7e71b4f7db3e1ae8078002222edd6bf5b2568f614",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T02:27:33.085846+00:00",
      "head": "212313f27299850c3c6488e93bff943cb84e965de0a50abfcb97d89229694dac",
      "node": "301.wake",
      "snapshot_digest": "a2038fbfc4a795342b90607ff2df348d8eddce21e292b4a9a2513bd0ebd2aeed",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T02:25:01.910667+00:00",
      "head": "b05bcf8e59423ad8be756063486fecae9462806ff1a71ab61d36d9311acbc8e1",
      "node": "302.wake",
      "snapshot_digest": "059a6876c82881fee0fe584b78c765512dd0c8df8f47b62d5031a9ac72b48181",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T02:27:15.925817+00:00",
      "head": "4fa8d3a9ac6d99850e3e20e142d707755f6b0d477835ef0f927d5fbd2819a118",
      "node": "303.wake",
      "snapshot_digest": "199f5364309ca080eec5bc9ba6be7e52b94bb1abc9dd29a40aec6e35e7add0aa",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d33323039363437623539386634396433.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d62303732376166303663383034626164.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
