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
  "generated_at": "2026-10-26T17:29:32.749503+00:00",
  "head": "snapshot:dedf36b0cf31232c15d16c12429847fbb06e1ce1d577746fa3cc18bae1409ea6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T17:29:32.749503+00:00",
      "head": "da1428b5fdb9aca1726ee2bce64b11c5c118bf446dac8fe4189c53e4bb6c81d4",
      "node": "100.wake",
      "snapshot_digest": "7b78b706f00df753194a7e7a7b0a231e885b6c277a642fc9e86fec7502abf71f",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T17:05:42.366649+00:00",
      "head": "56517818d703c4a6ade9da601e291d81c3a121ee5e709fff2f00d6b8f4325c68",
      "node": "101.wake",
      "snapshot_digest": "d3b9f8066ac4d56f7d7e05b38c1953dc0b9a09e5a223e98b67616183348f45f6",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T17:05:36.585070+00:00",
      "head": "344b5117d36b5a5e9d1674fbececb2cc46131494297350ff2b43b1675afba6ca",
      "node": "102.wake",
      "snapshot_digest": "0a8779391239946c2e51e5ebb00362c8731bab773d22ea25e1eb64f10a8a2844",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T17:05:42.520621+00:00",
      "head": "dae5a736360c18d5376d9e35964f1aa205b3d6889364da77dbd5a0bf58463961",
      "node": "103.wake",
      "snapshot_digest": "313517a308f315d1a4b7f83904b074862ce8b09fd284e9110137e160336cbdd0",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T17:05:42.176654+00:00",
      "head": "9d73e75b0759e46edefd0944753be4856118c0108dd4b87aa3eecbabacdf0465",
      "node": "200.wake",
      "snapshot_digest": "b624e29f5fd00ff38f3878d2afaf6689508d814cd1aa3654306e6f1ccfcedfaf",
      "version": 43
    },
    "201.wake": {
      "generated": "2026-10-26T17:05:40.660685+00:00",
      "head": "2763e5d9c07a057ba3842ebfd17ef4ac8f8f87c6bc986085facf052e9fa442ed",
      "node": "201.wake",
      "snapshot_digest": "4c82e72ff6d299f55c74f87f1fc8da87f66a2aedff8a251a4c2205864f6aae88",
      "version": 45
    },
    "202.wake": {
      "generated": "2026-10-26T17:05:41.412831+00:00",
      "head": "50d4ead2fcb31c1c0ac2737a19492ddb74c3cc323c8942e6deb982e19c592286",
      "node": "202.wake",
      "snapshot_digest": "4c46dd38861aa0f3893d5578198a88c7ff89a9310b01eef63aa580965e62d29b",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T17:05:41.989823+00:00",
      "head": "d1f2478a407877d4288a5c03ab473efeb4cd67d5dba5771d714e73117730bc2d",
      "node": "203.wake",
      "snapshot_digest": "69bfb8413cef219e89d8a4b92efac1787a7dadda6f4fff90768d87808b393748",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T17:27:18.155351+00:00",
      "head": "f42f84acfc76a848b94014045327d3cb9ee065bb7b4235e105e1e0f1d56a28cb",
      "node": "300.wake",
      "snapshot_digest": "d831a9314155619784281ab068f0bd051ab6d18c752b9629feb52d4a212ce763",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T17:05:44.561533+00:00",
      "head": "955c25e3b01239a671866f94c5ae18e898d8b537b04da3562b514601caf0a020",
      "node": "301.wake",
      "snapshot_digest": "33875728b3137d533a5a05559c81f985f050fae848e79a8ddb293f8d4cc8fe5e",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T17:05:42.804859+00:00",
      "head": "b47d3e2de93e7293f6f1ab0ad9fa5ddf45fd1daaab22a03dec9773d98c54c0b5",
      "node": "302.wake",
      "snapshot_digest": "ac1e07a9d2cb601586087654288efc74396d2851e46279c7e78ab953f4e198fe",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T17:29:10.836343+00:00",
      "head": "28395959523a59e4b759c953d008a92463487c269dfe4ed80f491416448d8e87",
      "node": "303.wake",
      "snapshot_digest": "59a169ecbf0289358c69757a94e3087d897b0a9bd6727e0e46116e54988ca111",
      "version": 56
    }
  },
  "version": 576,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d37393533343062326234353434663230.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d34616663366262663261663334383263.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
