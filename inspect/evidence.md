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
  "generated_at": "2026-10-27T15:00:53.644895+00:00",
  "head": "snapshot:3abdea5e7839a40dfe99566fefeb0da04b6a648799e9bc5d4b0db402de97f1fc",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T14:57:33.821214+00:00",
      "head": "42acc3f93b360cfa48bbe116d58335b54a6346c85ec25a10e8752ebe4927bb3a",
      "node": "100.wake",
      "snapshot_digest": "a4e0f11b1c93960e3d58b556b9bfd70e857c0806886fd89f76bed7e1c1a69362",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T14:55:08.067537+00:00",
      "head": "01112ca47599880efbf12ab73c67c762ad5d2a9d58ad4624c1642414048f42b1",
      "node": "101.wake",
      "snapshot_digest": "661b712fe6d431310f6f610b85b17160d8ad44395a06df0516d3d6dc11df2dfc",
      "version": 11
    },
    "102.wake": {
      "generated": "2026-10-27T14:59:42.804095+00:00",
      "head": "5b8c458f3dd632a350f6cc3f8378017d3b24de348104365b22455a6450605b59",
      "node": "102.wake",
      "snapshot_digest": "1958c128df043c5cfea68673b4780ccbaba424c7873716cc0914fee8deea9e3e",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T14:57:29.934889+00:00",
      "head": "555a3c178598362c44211e00b76e50da0118b5cb3b634a810e4bdc961c6b3c41",
      "node": "103.wake",
      "snapshot_digest": "bb7838bb70b3c6b1fd8df05066b092bf4b3518492c23498b1915bad7425e27a9",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T14:57:58.501631+00:00",
      "head": "68bd3cf37a8895fb7aa46dc0005d93c703deffb586a5dd64651f60c48280db85",
      "node": "200.wake",
      "snapshot_digest": "1c690c1f46bc53b796e35b5248fd6197b1d0ab8859fe38d874bc37bd1fd6839e",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T14:57:48.339163+00:00",
      "head": "d9cbc1693687be935fcf56c17a5b3c1cbc007c47faadc6bd8951b26925828e25",
      "node": "201.wake",
      "snapshot_digest": "6683a9baa2e92b52e0500e9da2d3e8ccb7ad3cf28174f32fc2ffc824d186b723",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T14:57:06.667559+00:00",
      "head": "79820976f2b8d5d8c64ed7741db1ed7ce412c813805583c9ec888114e65d4727",
      "node": "202.wake",
      "snapshot_digest": "60d2326e6c3f8a98408786a547d4b2fc52937fdfceb06cc2dff297ace46c5746",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T14:57:25.776178+00:00",
      "head": "5ff2cefa1e3793f7d037bac593bf5c8933b3551acb699e0de9cc4d4a7504ca2d",
      "node": "203.wake",
      "snapshot_digest": "2c7a7c05b79ffd8b39bf5e6876bdcab3d298b5475dac8d767f218d2143af70cd",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T15:00:53.644895+00:00",
      "head": "92db2629a59b33f98edc2c02f161c204316bf8e15129f35bf46158bea7a69364",
      "node": "300.wake",
      "snapshot_digest": "2d7a00f937d7e07861a8be5ebaa6e92c6a28475aec16593e5eaa90ad0cc4db90",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T15:00:46.490134+00:00",
      "head": "17702e9f6ce594c5d6352533727be33b75fb36742232220b2c78beb25488d32d",
      "node": "301.wake",
      "snapshot_digest": "3fe1e3d08fd75045d47e5498ec867890c84909264d0ac9391f45787eca07e9cc",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T15:00:32.214046+00:00",
      "head": "9dc8000c35a73c29be96f0c1470941f43ddc7d31d02505e5fe489a9d71f85a40",
      "node": "302.wake",
      "snapshot_digest": "24eeab4eb1a3537c2eec4b6752b7de71784694784254425c48eaf1f04141e2ef",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T14:54:54.537517+00:00",
      "head": "4735030466ceb8f318c571fb5c4a8bcb570f0d7c51e925ffd2225f827d45a6b5",
      "node": "303.wake",
      "snapshot_digest": "c01955636cce81ccda7216684403c79d31e04fae4bb5774ee348f3598129c66f",
      "version": 14
    }
  },
  "version": 150,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d373532316237646161376263343839/34.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d376235623265643431656338346433/36.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
