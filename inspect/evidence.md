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
  "generated_at": "2026-10-28T17:00:43.057038+00:00",
  "head": "snapshot:53b7e52d5692f44af8b83737ef01a813aedcbe732ba7ce6cfb96312c8acece1a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T16:59:34.455222+00:00",
      "head": "42638c7af348524461109fb988964b1268295ebb6db542a33395aaaf8f46c3a7",
      "node": "100.wake",
      "snapshot_digest": "cde4ab3364fa22c2e514dceb57ff3b024de7939532734b4c2ac10f4c26809d83",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T16:57:42.882108+00:00",
      "head": "e65064f0c706cff217e80919d6118bddd2ce27a6456b4aff7003cbe25a1e8558",
      "node": "101.wake",
      "snapshot_digest": "723134f528bd8fd337e686c9ad731440f8a40bb153f506d3b87414026825d618",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T16:58:48.324608+00:00",
      "head": "4d4becdda9575590d76609fc709c46362acc0b499c46433ad4b3eac08cc24144",
      "node": "102.wake",
      "snapshot_digest": "a3135b00f1c3f5cfc0b744f11f22b798d3d2bb78bea963c39c02ada50a46777e",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T16:59:16.395333+00:00",
      "head": "16b9365186ed0034ef9391e2d03e38e2204bfb569c3f65a2bd018564fd58e810",
      "node": "103.wake",
      "snapshot_digest": "7d9d67be463e3bb181942e751a5e28dc78e3207d52c693aded5cb8ec6abe9893",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T16:58:56.401035+00:00",
      "head": "c1826d22d1cac9adf52b6323b99780dbc86b8674937b6faeafb53e5431f2344a",
      "node": "200.wake",
      "snapshot_digest": "e3472de198067d8eea4787ca1fc8fe498e66ffc772f121398d76b842d86e8230",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T16:59:02.647952+00:00",
      "head": "de8700f215f8f5da56646c4d3ae36682707a9a73e7673308fb3c891f8b86762e",
      "node": "201.wake",
      "snapshot_digest": "a1bbac3350dc04722271267743307b0862ec51e0c5c8903630fdcb449bedd59f",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T16:59:04.582091+00:00",
      "head": "19b16511c7f314d56d5cc47529e55f33a90d3ebedb7c050087819aa7c24a8407",
      "node": "202.wake",
      "snapshot_digest": "d495f07b2ef3e6831bd482670035be63238e2a9a5ebd7600c7c73878e995eb88",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T16:57:20.163304+00:00",
      "head": "82d25fb86229201741b123f861f1f31038a00a93fd89a3a90a2fc7f4665a73a4",
      "node": "203.wake",
      "snapshot_digest": "076f6ec4838ffccabc34cc53b863f565a895d55a7e7802b523ff8091138cd28b",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T17:00:32.427517+00:00",
      "head": "47e4e2c471fd51554a3f3e5a8739a52b36fbeaa4311152a9fe8c50e043a6168c",
      "node": "300.wake",
      "snapshot_digest": "05a866ad3bb6c21230482be1184bd50191cfce6265e18ae3b8ce417a7c13541b",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T16:59:41.195685+00:00",
      "head": "710970df0b90aeb9b7eb470bb94572b423916a2ac15f258dccd2274cca8bdc4f",
      "node": "301.wake",
      "snapshot_digest": "b05349b35fb800f814db9601810746983ce481c277b82cc26821703bb46b36e1",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T16:59:13.200672+00:00",
      "head": "67345b0f0a5f91ad1ad8a500d94f4c4bea79730e348b5bf9c527044f49d0807b",
      "node": "302.wake",
      "snapshot_digest": "2a3396dabd0d43529c86e3ed251bbb96b9807e0be678e6b6061af6d32fb90b8d",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T17:00:43.057038+00:00",
      "head": "fb88d6b90b4e589e1cb4795274aef59977571fc2b6a29649342f11f162673314",
      "node": "303.wake",
      "snapshot_digest": "b2558753dfa25b11ca44dd8134654a09403e52be259659bf6df8e00b1642a2a5",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d66366239363234393432323634646666.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d34323932663930353335376634643634.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
