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
  "generated_at": "2026-10-24T10:27:14.649745+00:00",
  "head": "snapshot:e400daccb49532811ade8d592991ff73b4de9d35bb52fb7e19cf80b609071dce",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T10:25:22.865061+00:00",
      "head": "f495c8fa302a646d99257280572b4bafa6ac36d5c4dc677ebdedbe5706c47235",
      "node": "100.wake",
      "snapshot_digest": "f98ceda331bcde57285e8eb94d7a224848f1653d3f67a8e1d89786d217c9446d",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-24T10:13:10.116812+00:00",
      "head": "3d322e19f003da6fd600ec31427b438fee7db40ffca135f6d6500e53f01e4ec6",
      "node": "101.wake",
      "snapshot_digest": "2821e2f64b5ff2294c3cdff0eb20d00533a401988780adccd6428da5e7cd2a0a",
      "version": 33
    },
    "102.wake": {
      "generated": "2026-10-24T10:27:14.649745+00:00",
      "head": "729ecf067cbaf6dfcd736476dae15f7fdfa3d3cd62b2955feed18153a2ba7e8d",
      "node": "102.wake",
      "snapshot_digest": "4679d9d7ed26519be2d259ef3b07dc7b05828da0da5a892a3e633c5674700f9f",
      "version": 41
    },
    "103.wake": {
      "generated": "2026-10-24T10:20:43.794655+00:00",
      "head": "81ed52f73fedb0c1df2bedcae6c153954b58837a506f4704424171d9893dfa78",
      "node": "103.wake",
      "snapshot_digest": "3b1a57bd3723274cc1507bb6fb4a23df58c798fa57efaccd33d7252d440a79cd",
      "version": 31
    },
    "200.wake": {
      "generated": "2026-10-24T10:26:55.484097+00:00",
      "head": "43b3234b83845b5818cfb9817231f5fc44ec461579a80de5718772a02fb2a85d",
      "node": "200.wake",
      "snapshot_digest": "6448eb561085d013c3f7acc8b3d71530ca91c614cb0c90cc77ec34b8f1e2dc16",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-24T10:11:08.625578+00:00",
      "head": "2ac494506179ed557dfea29f2f595eee1803ac9ff0fb4fadc997fe5f3210f601",
      "node": "201.wake",
      "snapshot_digest": "d7a58c22351e1e60621b1b4b6f381d2b5d82d2f2f7a172570a5233c0d2a5f765",
      "version": 30
    },
    "202.wake": {
      "generated": "2026-10-24T10:13:21.659279+00:00",
      "head": "5188424df158a755500a191535856672f92bee1dd91e1078e5e6ab116befb242",
      "node": "202.wake",
      "snapshot_digest": "15a2af1f3415964882fe7e2ceca57b0f90fb1d90b0db236c1c3f17737a52e9a6",
      "version": 40
    },
    "203.wake": {
      "generated": "2026-10-24T10:10:45.467860+00:00",
      "head": "7a30a1d92655c0d796f0d9289a53734fb5a458c49be7b34c2d6d53df1c7a71a2",
      "node": "203.wake",
      "snapshot_digest": "f18f034e113e4a29e046767feba74d3346f3c0385779e5fac35322b56a4f1f93",
      "version": 21
    },
    "300.wake": {
      "generated": "2026-10-24T10:11:59.597073+00:00",
      "head": "cfeb65a84d536da728e81d59c6031f910bb688a8674a83db3bf3b4f7a8b19a17",
      "node": "300.wake",
      "snapshot_digest": "45653a18f586285734731c45337da3ff75ae94de203668fad75dbe34b2efb2b2",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T10:26:17.494438+00:00",
      "head": "8e0c7644d5d315827b57f5b478ba9c713d1870829091d53989ceca810cf90da0",
      "node": "301.wake",
      "snapshot_digest": "eedf3aeb23b946a74b748bc5c4f5dca66b5b80a1059247f3592018b6a0658544",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T10:17:33.830568+00:00",
      "head": "e8329d82afefe3d14de1fd8f801611f9acf10d96b6c31d2eca20e35ac8291bd6",
      "node": "302.wake",
      "snapshot_digest": "1e22f328451539ea225bb0ad014a64c8092bdad3578cfd09e0765e193a466e19",
      "version": 22
    },
    "303.wake": {
      "generated": "2026-10-24T10:12:59.830314+00:00",
      "head": "19039b425c820a6c26fc220775663af992f9a684c683d34db3c2009a9f1758fa",
      "node": "303.wake",
      "snapshot_digest": "9dcdd35e34dbf9ff7f76db0f5111cd08e8e80131044d1276ab685bd480e3ec0d",
      "version": 42
    }
  },
  "version": 371,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d653737343838336466633964343163/61.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d33336435653235363034353134333962.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d707265666572656e63652d7374/6162696c6974792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
