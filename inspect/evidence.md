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
  "generated_at": "2026-10-22T20:57:04.488071+00:00",
  "head": "snapshot:73d650139b422df7fd55407cbe7c2ae9aed7f2f80662a0f9d96ecb066f3e5dca",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T20:56:47.645506+00:00",
      "head": "190476c88f48c2ca743f1a66b810ca48f12a76ad7840ce174aaf97c8ae5b0d29",
      "node": "100.wake",
      "snapshot_digest": "8f6b5667d1e4c08436a6070385d5738780dac4825292b20f5991cb2c5759f570",
      "version": 1
    },
    "101.wake": {
      "generated": "2026-10-22T20:52:55.934668+00:00",
      "head": "d7bb58a34051694bc8bdde22b855414ff86b1ecd4add45b4128197175f778a19",
      "node": "101.wake",
      "snapshot_digest": "9424df68200711d4de53dce49d439a829d60ba0374485d15fc722ed6b33019a0",
      "version": 1
    },
    "102.wake": {
      "generated": "2026-10-22T20:57:04.488071+00:00",
      "head": "e8fe13ef95cffd11193aff0243f6984cfcabb9b7f6392ddc54a7e37d954095aa",
      "node": "102.wake",
      "snapshot_digest": "1649204f51378a2859daec2c4a487d477dd7a06bec119bdbcbdb98ffdf917750",
      "version": 1
    },
    "103.wake": {
      "generated": "2026-10-22T20:55:44.454442+00:00",
      "head": "b3c6c356a36bf582964cd82465125374c4f536cddd82b49872c29a7cd7c51cef",
      "node": "103.wake",
      "snapshot_digest": "d5e62509856efb03736c62f11bab1fc3c17c4899323638ff2a44c66a2ef27cb1",
      "version": 0
    },
    "200.wake": {
      "generated": "2026-10-22T20:53:28.185254+00:00",
      "head": "16527a99be81065a66e7eda2166e92b24896e2d53e11d2305ca33d3aebfcca71",
      "node": "200.wake",
      "snapshot_digest": "d4e8fffc2e550271cbe5c820503b9f2cf44f1f4f006a3d9ca9da32dfbc1f325f",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-10-22T20:53:19.676418+00:00",
      "head": "ace0c0c9b6f6fb59e33ff423d1c090ffc6a1fe06855409afefaf3f3db582961f",
      "node": "201.wake",
      "snapshot_digest": "858e01f09f947c80e076276dd29db11b64a6bd14575d972201fe1c1540275810",
      "version": 0
    },
    "202.wake": {
      "generated": "2026-10-22T20:54:06.758515+00:00",
      "head": "00a9d58e8aa8449c485f8eea7edee5bc251425992788f33d73fc143806a9b1cd",
      "node": "202.wake",
      "snapshot_digest": "1af9afaae50e516d399a8891736ff0ab117da1a1ac6229ad339174acd75ca2f6",
      "version": 2
    },
    "203.wake": {
      "generated": "2026-10-22T20:55:33.570692+00:00",
      "head": "626d877b5375ce77760fae0f20b9d37266d17940a6ec3c3c70b2d1b73458a64b",
      "node": "203.wake",
      "snapshot_digest": "1553efaad5cf50894825d25440f42b68b72da7ddc46d0f88755aabdeab5ae1f8",
      "version": 1
    },
    "300.wake": {
      "generated": "2026-10-22T20:55:31.475939+00:00",
      "head": "b6e1ec6f1304ec11277c956dbf76ccbb16f7adce1f9415e66c12779a55ba9932",
      "node": "300.wake",
      "snapshot_digest": "6af6d89aabaafc734acf55dd4320ed4f4da86ebf286bf9e04e1692cfefdfcaa9",
      "version": 1
    },
    "301.wake": {
      "generated": "2026-10-22T20:56:21.882618+00:00",
      "head": "491d493f014d9e68e328d4ad68526142892c94efe3225876f85ef5963712087a",
      "node": "301.wake",
      "snapshot_digest": "2927b155fd3fe68a36d6500f9c72b872ff53a7a6dd699aa061c22d610b109e79",
      "version": 1
    },
    "302.wake": {
      "generated": "2026-10-22T20:56:45.140098+00:00",
      "head": "b039dc1b0acbfef903daf3b6be66b5084657a937cf83d1f05e36d95766a6cc00",
      "node": "302.wake",
      "snapshot_digest": "10eefce6d246686d58d50be001052b58bc6f3519f63d29a0720d8c5da6d66e5a",
      "version": 1
    },
    "303.wake": {
      "generated": "2026-10-22T20:52:59.767597+00:00",
      "head": "01fb5e14d96954d43d2cd43874ee3d45acefd19c59232a9b4adf90fceefe3881",
      "node": "303.wake",
      "snapshot_digest": "44dfcb313e499eb80f1757769013ced8cb09ed0190f5a0b20e0659e99cda26d0",
      "version": 1
    }
  },
  "version": 11,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d636363316261663433343163346534/38.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d663563306633626564313233346266/66.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
