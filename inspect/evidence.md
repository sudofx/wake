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
  "generated_at": "2026-10-24T13:48:49.902760+00:00",
  "head": "snapshot:9a7339d22e667ee2a566d4064bd57f457fe0a2404466929468c59f9dd627c1dc",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T13:46:09.317487+00:00",
      "head": "907547467ccadd50d20c556fa19f6d7f78b3d027eb89956ea6a16875a6b14a09",
      "node": "100.wake",
      "snapshot_digest": "8a0d9c94b4076dbf6e5cc967da2d4fafe3be51f6fd1550155ad905a37ec9fb87",
      "version": 22
    },
    "101.wake": {
      "generated": "2026-10-24T13:45:41.981093+00:00",
      "head": "02de4fb92e4f18a983827326ec134a4c435dac9d0806ea6d6e82e6a1c4fae102",
      "node": "101.wake",
      "snapshot_digest": "5312a751b56ed9c15e93174d97584c547eada82c3e5aaf74115c3534d25a329d",
      "version": 36
    },
    "102.wake": {
      "generated": "2026-10-24T13:48:41.977434+00:00",
      "head": "9a0d028e3adbedf9be42307004cd583825de4c67d2c19b50a320725de88c3d31",
      "node": "102.wake",
      "snapshot_digest": "6f0c4641deeb40e2f42804629c532ac4b6f5202f0261f17dbdddd8fff01da759",
      "version": 43
    },
    "103.wake": {
      "generated": "2026-10-24T13:27:23.329394+00:00",
      "head": "30af5854796a98eb7923e87b3a0efb8477de6cc13aca71a4bd50e3d50696f5ff",
      "node": "103.wake",
      "snapshot_digest": "6cc21e38ef6acbc3b1d17c6b546e6463cdff7a2e518c557a714049abb8b421a3",
      "version": 34
    },
    "200.wake": {
      "generated": "2026-10-24T13:42:52.208773+00:00",
      "head": "f97c985666c94a3153d1ace097a6f03d0714ac95381f965e81a18c881c2dd1f6",
      "node": "200.wake",
      "snapshot_digest": "8200f5f4ca08de23b47774e299af3ed71f8d6f9c4e29cc2e141969b54507d0dc",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-24T13:41:12.061500+00:00",
      "head": "18b3cea89da7aaf60b09e6aefcd0007a6c044f98efdebb043378d49243aad826",
      "node": "201.wake",
      "snapshot_digest": "186d2320bdd9d7408d7f11d6db61228dc79ed6311e0b12e682cff2dd99776e74",
      "version": 32
    },
    "202.wake": {
      "generated": "2026-10-24T13:41:50.288333+00:00",
      "head": "dddae5cf39b434cf01597ed6887b5749bf2954876007013e9df08223da01fdaa",
      "node": "202.wake",
      "snapshot_digest": "14a7b0889decc469fd168b3a1136382d21997c28ebe35e8b0f4992c73cde6dc9",
      "version": 43
    },
    "203.wake": {
      "generated": "2026-10-24T13:46:19.004223+00:00",
      "head": "929e40d8c4c4cc58fc52458fe8e81b9a34b1cf1fe598d95d009d67624af32937",
      "node": "203.wake",
      "snapshot_digest": "3d31b4d41f6811d80428be89138d4cda55c843917a5ba91dafff65bc6ef055f8",
      "version": 25
    },
    "300.wake": {
      "generated": "2026-10-24T13:44:20.561649+00:00",
      "head": "75b011a2f853eaa79acdf2cc86ec534309c5a91e562ac68776e6964fc74dd98a",
      "node": "300.wake",
      "snapshot_digest": "a8618d5836af3f98bf331b6ac18c4d5552e655ce0933ab957e7073a9bf1f6b48",
      "version": 28
    },
    "301.wake": {
      "generated": "2026-10-24T13:48:49.902760+00:00",
      "head": "c279f70105561de4eecce345b0b69d34a3c9b275f09fa723c80c3613cc15f676",
      "node": "301.wake",
      "snapshot_digest": "cdfe5d4fa8eb577c6fb0a5990d3235bf537ea0c2b86ab5d36964e8b642a32fb6",
      "version": 44
    },
    "302.wake": {
      "generated": "2026-10-24T13:47:54.928186+00:00",
      "head": "90ab0b0932e9a15bcfe3896ea1c3b239bea58d5f76455f61acd481d561d746ae",
      "node": "302.wake",
      "snapshot_digest": "909ccc7e2f94e05521c3fb5f949827105844f43b6ec6f6bae417be46d63ca412",
      "version": 24
    },
    "303.wake": {
      "generated": "2026-10-24T13:39:25.201222+00:00",
      "head": "16b82201b2aced9cde21cb7ae0a7b10dfbe5a03753fc3d91de84499dec1e6b52",
      "node": "303.wake",
      "snapshot_digest": "3bb780105927eb34ad468a6f6e0ae2f6a4ff10acdc92b5577f7a980c1ab666a5",
      "version": 42
    }
  },
  "version": 399,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d333564643239663335613261343964/33.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d363332353134383637396436346130/32.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
