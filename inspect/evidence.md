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
  "generated_at": "2026-10-24T08:17:01.850677+00:00",
  "head": "snapshot:5daab586229ed7bac2fd28dffb2bf1b489745932fa6b2ba35647a21d93d2fa06",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T08:02:07.889336+00:00",
      "head": "75682acb91fd945e969ed14f9dbb94710dd76e9270cbc4a10ee421d666cec5d7",
      "node": "100.wake",
      "snapshot_digest": "28cedc99bf021538a0aed832b62c30b6f35e772853d34f2a2b87354dc8bf0419",
      "version": 20
    },
    "101.wake": {
      "generated": "2026-10-24T08:14:06.978508+00:00",
      "head": "1c4f1afeaec3cf973de29138189647ac773311e0abd47b5dbd1e36b3c91ff2a4",
      "node": "101.wake",
      "snapshot_digest": "e34189480913325e5516b9d649c1af250d2a056d8e154c952f9a1b3228589379",
      "version": 32
    },
    "102.wake": {
      "generated": "2026-10-24T08:14:30.993491+00:00",
      "head": "18d26cd0ac8fa8f127816143a247d73e8c9ab0daed76250ec8c691e78f18522e",
      "node": "102.wake",
      "snapshot_digest": "68ea5c194074dc771622102aa150af0d7d232af946e9ec6b9e54d37158abbbe2",
      "version": 36
    },
    "103.wake": {
      "generated": "2026-10-24T08:00:11.803181+00:00",
      "head": "edf2c4fbc4702e32b9201bd13178889f0acb12c5a07c27437eca624c8363c1ff",
      "node": "103.wake",
      "snapshot_digest": "3f0bb224ce0a61cf14b6ccb540abff9aaeafb709057ae8da39efc4bb8e076dc8",
      "version": 29
    },
    "200.wake": {
      "generated": "2026-10-24T08:01:25.110175+00:00",
      "head": "9d7db91fa62204c8f66eec9eac3992787803190b1693831bb4ed8e141ecd0140",
      "node": "200.wake",
      "snapshot_digest": "1ff17fc63bd21b850cbf756d847a000c6115e9626889305f1a425401332e7442",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T08:08:14.621832+00:00",
      "head": "87ea0965ad2a14c7684e9a328b6e39b2d80a033d412eafafe74a09e7b01bcbbe",
      "node": "201.wake",
      "snapshot_digest": "eb84718dcd28d31220fe12b3123a6f965c9be599b0be3cec86d0bbbb5771411f",
      "version": 27
    },
    "202.wake": {
      "generated": "2026-10-24T08:17:01.850677+00:00",
      "head": "16190e23c2438f1ee362b57d42f81c8ded1dbbdfc96c0441c424e2f9f39775c5",
      "node": "202.wake",
      "snapshot_digest": "7ed2fb462ad14ac4d152a3b376f28571669396079727ea2b3c1033a73a237279",
      "version": 39
    },
    "203.wake": {
      "generated": "2026-10-24T08:14:52.178212+00:00",
      "head": "8da5da486a36aa7e75695c93565043a16251c3f09bb3d58d0bbda80cec2ae4e4",
      "node": "203.wake",
      "snapshot_digest": "88cb43b27412540e430104f7d26752846ef448515a630c2b8d711773eec0f8f4",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T08:03:29.874502+00:00",
      "head": "8237b2b3576fc3c952996d1d657e98c9379921f6de8311448aeec3177b251be7",
      "node": "300.wake",
      "snapshot_digest": "9c6d5c1cb8c09f1747b0bd646f339c76f574af35b14c9b5a1a279d6d4c33792a",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T08:13:17.014058+00:00",
      "head": "750c690201ae46845711ae2e83332865f32307985d57147a77122770e2384c6d",
      "node": "301.wake",
      "snapshot_digest": "5205430512b2970f275eeee1fb11cdf46e4daffd3191b2cb082466f5b370b436",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T08:04:13.630242+00:00",
      "head": "5c7a3fe918e2fbc3bef12c9c75425cd711aec555953a75d18e9f84bf96300576",
      "node": "302.wake",
      "snapshot_digest": "59437012ee38dd5ea485a223888fe4adc28aeaedb9cb579234a089794006a5db",
      "version": 20
    },
    "303.wake": {
      "generated": "2026-10-24T08:15:14.689377+00:00",
      "head": "1b6f20060fa26f76ab6f6d15eb9ce6bd41bc1adf8759f265a75168ee44b95ebe",
      "node": "303.wake",
      "snapshot_digest": "d40d308379651badd9314f8cd78b5bedbb1f0a5985dc7623f12e7b34943a23f1",
      "version": 38
    }
  },
  "version": 348,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d393032313935376166303164346466/36.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d643535333234306337663334343739/64.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d636f6e74696e756974792d7261/74696f6e616c652d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
