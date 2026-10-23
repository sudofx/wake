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
  "generated_at": "2026-10-23T09:08:06.085514+00:00",
  "head": "snapshot:bf5000d0f24526a7c9b48cb5bf9e1e51b68a525faf1e56186c2eedcf65094092",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T09:04:49.943133+00:00",
      "head": "c9aa1ebef4ae25d027439d697fdfd8481617f623ae5474511e8ac0bf20577514",
      "node": "100.wake",
      "snapshot_digest": "acb60012a76de51b0c94bfaf4789162d6a13f2c296fe0ffd4540915071f943b6",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-23T09:03:38.278195+00:00",
      "head": "887c853f48c32d4ef37df0efc597a2a2f4ca12294f401f965bef70a7f3e2e9a0",
      "node": "101.wake",
      "snapshot_digest": "44b98089027ea63f81dc9fe4d090bea4415644ac5f46dcca50c9a137199b188c",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T09:08:06.085514+00:00",
      "head": "241d816454af4820156d471e3b96585cf7ef4d1562819826f2da0cb2c0fced5c",
      "node": "102.wake",
      "snapshot_digest": "d52cdda10b757cc0dace67268bda0327103c62fca4153fe8b2d0b1e6471c963e",
      "version": 20
    },
    "103.wake": {
      "generated": "2026-10-23T09:00:06.575606+00:00",
      "head": "710ad5b431e9391a8fd0cfd30c75d4de8cb42ff74e59f336e52de970f767f37b",
      "node": "103.wake",
      "snapshot_digest": "998291c306b84a11e6b8476690b99d4a877fe01d772371fac5cf56855921eb85",
      "version": 13
    },
    "200.wake": {
      "generated": "2026-10-23T09:07:19.295505+00:00",
      "head": "4fa6e2c5aaf06ab24ec8069235c5f47582e2e18b8ea6a85f2f7f3300979194d1",
      "node": "200.wake",
      "snapshot_digest": "8734e5c126e0350b3a90faeecb0a017e9786f0486025025f566f92a3eb38fad1",
      "version": 12
    },
    "201.wake": {
      "generated": "2026-10-23T09:05:39.859796+00:00",
      "head": "2f9231b7c6a376df31858b4dc1985d8c83fece99bef1c90afd05c4e384d47205",
      "node": "201.wake",
      "snapshot_digest": "043486094febb8dd48d9f56eee2db8d8e07a5a9e0d900d6ca8eccf43f3eccabc",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T09:01:01.669592+00:00",
      "head": "a9bdde6a7766f4ca1f1dbfb73498e38246f2a1d19fd60e05ec8f66fd77effd27",
      "node": "202.wake",
      "snapshot_digest": "3c7df2bf122aab209bcf89afbfb517e372ad50e9d9e123717eeea5d50671ac10",
      "version": 19
    },
    "203.wake": {
      "generated": "2026-10-23T08:57:41.798219+00:00",
      "head": "f0535316cb97eed2825c8ee9763b39e9d544a4343267caae94ce5b1eef247385",
      "node": "203.wake",
      "snapshot_digest": "8f92db1aaa7a862b2eddb2ea1488226fde68096b48d4a1b79263a037df23a0ca",
      "version": 10
    },
    "300.wake": {
      "generated": "2026-10-23T09:04:22.329414+00:00",
      "head": "37913ede2f03fc9ae2983f7e2450968ff34b5e5e8126088b787d5e64545690d9",
      "node": "300.wake",
      "snapshot_digest": "757f955cbeb062aaa05ff13143d701bc999dffd3fed3c9d78a21bee4f05c107c",
      "version": 9
    },
    "301.wake": {
      "generated": "2026-10-23T09:05:45.915880+00:00",
      "head": "6c7f6f4d05595dced782d2733ee343fab744346c2dbb08ddc9206f172120d78f",
      "node": "301.wake",
      "snapshot_digest": "7b83218b89c9235bc6128d00b74b12b556e8493c4239549c6bb57f7c711f9ecb",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-23T09:05:23.339002+00:00",
      "head": "6fbaf04caeaa717447ccb8a90934484a897367d99b5f6c1fc1a1af38ec7470c8",
      "node": "302.wake",
      "snapshot_digest": "929d6f4478f767b9e489d315b8a6bbbc90d83be57fff65d7f893c1fa6535c98c",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T09:07:54.917510+00:00",
      "head": "86150a3c11ed1b5622949e03f8c3186f1c68de0f4d0cdf406c026c803c95c4c4",
      "node": "303.wake",
      "snapshot_digest": "d600222ff7917b8f2a542ccc43c56ffd470373423755101a065a2f29e109e0fa",
      "version": 21
    }
  },
  "version": 172,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d323239323839636339393130346563/34.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d356532393036353833393032343438/66.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
