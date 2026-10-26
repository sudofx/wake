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
  "generated_at": "2026-10-26T10:13:15.673176+00:00",
  "head": "snapshot:5b7fe39f4d26c298d9d595eeb148e95eff5863d56986a6854e7e7d03f6233e43",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T09:53:50.501300+00:00",
      "head": "ea55f848f082ed0ca04bdf7681bd5b3e86340df39cda1d943dd86077f11d77e5",
      "node": "100.wake",
      "snapshot_digest": "1a215c1da15a690212b94e387706e98b7701322fd4268d5bbfbd38aea1589d0e",
      "version": 30
    },
    "101.wake": {
      "generated": "2026-10-26T09:53:53.933378+00:00",
      "head": "1dc30a9fd6902d0a0b57d39bffc3deaf730acdbd972753e2a3eea53a09b7c195",
      "node": "101.wake",
      "snapshot_digest": "294c6d1d63801f2ee1984113d701e01075aecda26db386e5972fbf12d0081e22",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T09:53:47.666992+00:00",
      "head": "c88def4ffb2559a1b623c1f34a4420a320b152a749387f9e2e47eed2ed6ad18e",
      "node": "102.wake",
      "snapshot_digest": "6b818cde5e1dbeb6fc278e9cc9eb47bd6b0e123ce12e4a7cde03e9cef56771fd",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T09:53:53.588398+00:00",
      "head": "03ed77453a3063e10c68101505cc0240701c50a47397b6c78e21ae21a2612554",
      "node": "103.wake",
      "snapshot_digest": "69fe72b28522ca6622c54fe36dcb6d72b14bc87a019b78bf963310fdb1e5c253",
      "version": 44
    },
    "200.wake": {
      "generated": "2026-10-26T09:53:51.640216+00:00",
      "head": "ef402ac92f2320f6e5c369d6614d5b5c3e66d6edd11f22ce4a193dede7a362d7",
      "node": "200.wake",
      "snapshot_digest": "7839349a33221b5b5c9b05c6f6376f85821631e99afbc2b09b75700d6dd9cbf9",
      "version": 40
    },
    "201.wake": {
      "generated": "2026-10-26T09:53:54.249154+00:00",
      "head": "dfce8f52930d2bc694fcaf6376dc88e9293974094ddb82b0f7af33ef3b794419",
      "node": "201.wake",
      "snapshot_digest": "e5d7d54c9cff78dcd66c15f1500cd1d490b0f8df705d0f989738be3bfbb5abb3",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T09:53:53.920984+00:00",
      "head": "85f669398c7106fabd9db1a3ca0edc7aa40792fae96015e6fbd282f2f7b57a29",
      "node": "202.wake",
      "snapshot_digest": "362f0904d0709837ee0da8aaab0c832e1d49f2ff7337691526b214c6d9255188",
      "version": 57
    },
    "203.wake": {
      "generated": "2026-10-26T09:53:51.233556+00:00",
      "head": "c3e89e9c9b83548fb3f982474a67d37eb4090c1f304e942869ee37d43c44deef",
      "node": "203.wake",
      "snapshot_digest": "6637480269ad9953d17c792471b1fdeff1bc9644d927c6b48074bdbcf604b046",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-26T10:13:15.673176+00:00",
      "head": "cb73a88d6da2fe2ce47ad09949c1618801ef7f3a4c2a57f25f872718e48aa85f",
      "node": "300.wake",
      "snapshot_digest": "8911cfd450d954aea66d8f27b30b096ca1c3969f1b17ea40b658b2484a2ae008",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T09:53:57.492129+00:00",
      "head": "bcf1968272440ec0e13dc4c0c332b61f465e4e4fda6c37c9239084441427eda2",
      "node": "301.wake",
      "snapshot_digest": "0f2b86ca39604a5133ef8cae2953d40fcbd5aa7ca146e4209ef952cf430b96f0",
      "version": 61
    },
    "302.wake": {
      "generated": "2026-10-26T09:53:51.702567+00:00",
      "head": "1d6072bef3773f5d255403838571edf1cf199e5103b81df6678616afc0023327",
      "node": "302.wake",
      "snapshot_digest": "55433320573b59b710c82490c85244becf33e884e638a7775cc1f689e0534777",
      "version": 46
    },
    "303.wake": {
      "generated": "2026-10-26T09:53:55.857519+00:00",
      "head": "cec3a626d61c2af288041f0dc477df09b153ed0143b371869bf1307c8195a06f",
      "node": "303.wake",
      "snapshot_digest": "8aff553e5b5c277ecf6b1171ef42b858633635a134aad45307ea506a8d90b3f2",
      "version": 55
    }
  },
  "version": 558,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d39633639336437316562336134383463.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d33366166356230373262666134363762.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
