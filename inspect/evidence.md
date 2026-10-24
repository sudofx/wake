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
  "generated_at": "2026-10-24T11:00:39.561027+00:00",
  "head": "snapshot:ba93413c8194df63202ef9ee82d8c19a13fb80de9a7c7a6915de862550a76d1b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T10:47:33.162141+00:00",
      "head": "3e1d7eed2eb974b7f3c7641455e80809885895d15bc44f903d833a8f9383e306",
      "node": "100.wake",
      "snapshot_digest": "302a509009c6f397dbf99afdad7f67ba3ee86c3a807b49967c27107352127f0d",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-24T10:56:23.355962+00:00",
      "head": "a725cda600ee137398111fe7de05b066345d43a1814bdd3a95ab54a02b243449",
      "node": "101.wake",
      "snapshot_digest": "7a4cafc02035bebda6424a420ab303e816c900481f52ef2cf58068ca5917f2a6",
      "version": 35
    },
    "102.wake": {
      "generated": "2026-10-24T10:49:27.110449+00:00",
      "head": "500b455db0658152ab2caadcf1dd4dd6b26fe6ce3a602685d9a9a14f6c10ed9e",
      "node": "102.wake",
      "snapshot_digest": "37fdb9177a45b36121d69b15817c235c2c3f7532c33e06591c54d22382db1ee8",
      "version": 42
    },
    "103.wake": {
      "generated": "2026-10-24T10:51:26.895722+00:00",
      "head": "d61eb848ac879c4d4d43bb5467ff63bf160949a1e02e1b542e5c72697e4aee1d",
      "node": "103.wake",
      "snapshot_digest": "36428947eb1b9496fbacf7ae46ecbafca0daad4ac5eac7d7283f0f37ac6bf881",
      "version": 32
    },
    "200.wake": {
      "generated": "2026-10-24T10:48:54.378675+00:00",
      "head": "fd4f1cf3547ab1086627e6e466521679cdf1e0d54eaf5560793b9870772d74c1",
      "node": "200.wake",
      "snapshot_digest": "0d0a1be72b74d308ff31b5c6344313e07ea4ce9173cf75df07134044561c6058",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-24T10:54:04.104134+00:00",
      "head": "0a2c9b8f3e7f5e6a678ecaf484bce7075b2820ecff518a9055a3fe195d5b0baa",
      "node": "201.wake",
      "snapshot_digest": "073f0092158d5e72655a8a237125a4d391e3594a9e73b0cf4c93298b814e5539",
      "version": 30
    },
    "202.wake": {
      "generated": "2026-10-24T10:58:03.556610+00:00",
      "head": "c496128c0cfc692a88bf0e6a0a5819ac8190f75f6d5730dab25071d4ccb2fa36",
      "node": "202.wake",
      "snapshot_digest": "8d2e76bb2830b82fa9684a4b26b319bf1082839caa256a1f3e339eec14e18538",
      "version": 41
    },
    "203.wake": {
      "generated": "2026-10-24T10:52:09.747789+00:00",
      "head": "29da9e557264418fd13c3ade0164c1a459e54d4f294460df6fa9dc820bdb7c58",
      "node": "203.wake",
      "snapshot_digest": "b12bb3d4a8b9e39325c1ff03cf112a987609a670cebf2997039935f7cdc9066a",
      "version": 22
    },
    "300.wake": {
      "generated": "2026-10-24T10:55:30.238309+00:00",
      "head": "a129c423c8bf2d9ccd81b19d58884de6c354b56edd50935678e978c171d2d34c",
      "node": "300.wake",
      "snapshot_digest": "3c81eedfdf6fb55262376fd24cedb82d04c3fd24487f2beab5d6326762fadd4f",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T10:48:33.018775+00:00",
      "head": "682acad19982333ce3113c500b552efe3fa94a0b13a2c40d0b3ae04d460bf7f8",
      "node": "301.wake",
      "snapshot_digest": "c12f18d811a48d5b1b03f7ab16fbb5ac61b20c02fa114432e9f7affcdb74ac2d",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T11:00:39.561027+00:00",
      "head": "68fe68d1e33c0f034f1de32cda4d36c1b502abecd0ed9577b15ee003d63303f2",
      "node": "302.wake",
      "snapshot_digest": "390926351ee3316b5da4baa5b1a4fce2651a516c9f5a4a7e2b4adb3e37d33e66",
      "version": 22
    },
    "303.wake": {
      "generated": "2026-10-24T10:55:51.422260+00:00",
      "head": "8b09625cf3fde9a9498217b416a7357ad6d48db73ea9bb73bd1355ffd7fcac3c",
      "node": "303.wake",
      "snapshot_digest": "35e09a70e6aa59e5e6a84ba6a0072e782be553f7d60e601dbadcc44564bafb9b",
      "version": 42
    }
  },
  "version": 377,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34336335396461616337366234626134.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d623464353530633063633164343764/32.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e6f7465626f6f6b2d6f62656469656e63652d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
