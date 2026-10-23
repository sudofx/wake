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
  "generated_at": "2026-10-23T23:29:11.616288+00:00",
  "head": "snapshot:fd63fafbd1538436b8e35ba40ac87a2b5ba4e179f8dc5e028d28c8aacf2de7f5",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T23:11:40.249843+00:00",
      "head": "08a5e2f79b0732b6bb45293e60edd7b64988d40570e3d7f25103788c1e7d5b93",
      "node": "100.wake",
      "snapshot_digest": "f70cbf798cf5647669a1279a0291b81f47e08be293203fa8901db0de98bd85aa",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T23:29:11.616288+00:00",
      "head": "98b0ca731d7c8135e22a013c1c8c6f0c0b11fcb25a12d626723fdb26c76d808b",
      "node": "101.wake",
      "snapshot_digest": "e6c0f8fb6b61d3f1158738bf99f4e35f6833d811d5f263822e351089c9c24a04",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T23:15:27.859759+00:00",
      "head": "4789730054eb8bbfc777eda3867efed4666f31fb9291462689b8eb8c1eb50cb5",
      "node": "102.wake",
      "snapshot_digest": "aa078babe38ca80c5f652b874ffc2d5c7b12a38b145b55775527340cbcac7c3e",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T23:15:56.170935+00:00",
      "head": "205c911e25581cb57b356cbee30d6d545e4c8d3b9278ebecf2f81d65aa52b4c2",
      "node": "103.wake",
      "snapshot_digest": "d6a2c20cb497c92bbdec827394aee0cffc34ba434da2e6168e628ac99a416649",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T23:15:48.747253+00:00",
      "head": "9e96f3981481c62815c774d2828c9a7c9334eec2fa01cdccdfc96589095cc508",
      "node": "200.wake",
      "snapshot_digest": "6ea08396a1586302f1b246c9414febeafe5882d93702a0f843b98a579e65577c",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T23:15:41.766768+00:00",
      "head": "b9b67208850ac4700a169bbf3274a34fb472e084cc9d4aaf3af5fd919ee63d7f",
      "node": "201.wake",
      "snapshot_digest": "ab21b1aa8b324f06afc76912b5cf8d9a9baa9dedae319faf673648fd12aaa0cb",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T23:16:10.692283+00:00",
      "head": "9c74e13a37738153180c1ceb7e7b5a7d16f3b5fbd87443c78ca0cbe6dee988bc",
      "node": "202.wake",
      "snapshot_digest": "369bd770e79b18506ee37819019df3cb82068aba1351056a4d09a44e3f8cb44f",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T23:15:34.898467+00:00",
      "head": "1aadc11db3e36a3aacc495d80944f72f2df6dbce384248fada1c8cd5b878375f",
      "node": "203.wake",
      "snapshot_digest": "a44d72437fcf64194bef624dbce0ad86c65f953dbcbb56fe4622dd32b2650ac0",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T23:16:03.549038+00:00",
      "head": "88ebf122d4d3791735d52713f52a8e99ea63e86a0214946230484aefb91ef7ad",
      "node": "300.wake",
      "snapshot_digest": "f066b2c65ffdb0de473f988cda27778ea7774f60817c844eabb07078fa33a465",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T23:16:38.868091+00:00",
      "head": "f7e7cc0c734cc699004aa14309b000e37d288512e119c83cda39fe3c22d7e9b9",
      "node": "301.wake",
      "snapshot_digest": "3bf522a8c34ab326cf8331c3c8530d9ece27f68de8c491adf6333c3d4bac1fe0",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T23:15:13.528457+00:00",
      "head": "e030bea5983e8bb4d1107fedc44dc8d1060c43c0cce291c76edce2462da25c92",
      "node": "302.wake",
      "snapshot_digest": "9f424b0fcb7fdb3d4b18e1ce0f1465319ebe8a25b9d90a240bb3fc6ac587219e",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T23:15:19.961243+00:00",
      "head": "a41c502861b88080f3bc312aed9910eff8ee46d1981afe2edd11a185f6e29e3f",
      "node": "303.wake",
      "snapshot_digest": "1ea1506008e92c6c190b684ae95d4615eb09158babcb4bfcfb3817c7669bee47",
      "version": 36
    }
  },
  "version": 337,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a722d61626338336135333461336634383163.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d62313830656366383635626334643765.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
