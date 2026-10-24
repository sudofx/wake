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
  "generated_at": "2026-10-24T18:07:41.474165+00:00",
  "head": "snapshot:d78b6c5a2ee12535616734d04d6242e7b242fcbacf2943265c8b008420cacd3c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T17:53:54.762238+00:00",
      "head": "e3e29273b1a1fe4d14ebdcf1fd7611003196e663b5b44a13053f635c9f5b7fcd",
      "node": "100.wake",
      "snapshot_digest": "175751e49609413438154d0decb393d4ec5dcbaf7ba9dfd0eb061cd03d587b6e",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-24T17:37:31.388688+00:00",
      "head": "a1f91cca7d080f0f4d5ff6eab850340b9f38be12035ce845600cc0144f131794",
      "node": "101.wake",
      "snapshot_digest": "b2db356e82153a2571b52f01b4349dc0060f7c560f893ed408ea9ce858ccc5b2",
      "version": 37
    },
    "102.wake": {
      "generated": "2026-10-24T18:02:06.684937+00:00",
      "head": "6c8c6b653a1d7a0b494184c8c0559767f5e5457b9f494e32d9190fa585309ebc",
      "node": "102.wake",
      "snapshot_digest": "5922cdd9ec2445a396d70cd6f3414379fb50c59e542a4b4e6d76fdcb3639d9e9",
      "version": 49
    },
    "103.wake": {
      "generated": "2026-10-24T17:52:28.026993+00:00",
      "head": "20dea100fc886a1b431f2e307c987dea5cd5b566d39a9e6aa89ddf88d0926f94",
      "node": "103.wake",
      "snapshot_digest": "a0414e3faf9c2c2b95c06d791e62b38184f24de1d4c2f7781e8848fc2330d930",
      "version": 36
    },
    "200.wake": {
      "generated": "2026-10-24T18:06:52.148584+00:00",
      "head": "2ee277924dfca0da7b33de53e9124b3bf5618bb529b1878d8945e2c808d7f1d7",
      "node": "200.wake",
      "snapshot_digest": "063156bd2d2cd48f80fca8672117489c0d58bb759ebf60cd6ef251d166445de2",
      "version": 28
    },
    "201.wake": {
      "generated": "2026-10-24T17:54:08.476676+00:00",
      "head": "67fcf1fd4ff09b22f7fe9c08ed99f1b069a445be9ab5f3fad15530b89400c089",
      "node": "201.wake",
      "snapshot_digest": "39926d9de7b850d0d3ff0f277eb946b0b71100a0facdf3746562e6522549509d",
      "version": 34
    },
    "202.wake": {
      "generated": "2026-10-24T17:53:40.097216+00:00",
      "head": "6f4b1bea922584e43a3dd9e8b43974e4e75baf3ec692e7d37d29d1cc5eb87ba8",
      "node": "202.wake",
      "snapshot_digest": "de4910f8ffd21a48c5f1078e5e513fe389db09a02432128c0f2f35e9aacd5d08",
      "version": 45
    },
    "203.wake": {
      "generated": "2026-10-24T18:05:59.213226+00:00",
      "head": "4491eb18d949c2708b82627171f763d87617b786fe16d2f8dc9c8f07c7f45c68",
      "node": "203.wake",
      "snapshot_digest": "9e0ef7f752dd02d5dfabc9d0fac9cd6c91e771df12591bebdcdf9c69b6593103",
      "version": 26
    },
    "300.wake": {
      "generated": "2026-10-24T18:07:41.474165+00:00",
      "head": "b97c5486e73ef4069927ca1f265ed6421e4fa3389ff9c56a54af54144d68ab57",
      "node": "300.wake",
      "snapshot_digest": "0af985c4ad64b7371362d7e01aba52ca26faf353ef031d7c506fea8f2aeea3a1",
      "version": 29
    },
    "301.wake": {
      "generated": "2026-10-24T18:05:30.788541+00:00",
      "head": "6b2b05b614d1250243c26f7f813746097c278f98134cad2a9447c77f2579875d",
      "node": "301.wake",
      "snapshot_digest": "7e8e4f478159897406642bc4dcf46892b5c9c55c445a0fd14d2733413370617f",
      "version": 47
    },
    "302.wake": {
      "generated": "2026-10-24T18:05:21.512480+00:00",
      "head": "7d1db7690bf26cd65e2d167cd256f9132ce4d76dd53db18e0f23f9da66ab8ca3",
      "node": "302.wake",
      "snapshot_digest": "e57aad086450fcd98171c46f8d28bc60f0f3b8d9f334ef6cbb60733aa11a1db4",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-24T18:07:32.792209+00:00",
      "head": "3f3ca8ade0ae7540cfb7108a54984a32fa229f4b00f4a5f817be035fb31f5309",
      "node": "303.wake",
      "snapshot_digest": "58bd5cfcd11b8b6845cfb06cc79a06b602b765f30244030168b22d1587da0cec",
      "version": 46
    }
  },
  "version": 426,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d38393232363862343965633134346335.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66383665396166396563663734666133.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
