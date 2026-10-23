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
  "generated_at": "2026-10-23T22:30:41.923594+00:00",
  "head": "snapshot:c6feba2e729f83bba3ee93c082c223ff08ce635aadeec2fb3937a88574555a63",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T22:29:35.369492+00:00",
      "head": "8b7e537a521c30233f69e23888d7aa989cd9812838b4274e01c4c4ed1a45e0fb",
      "node": "100.wake",
      "snapshot_digest": "c33d3c009fe2990eca2cda53229cc6c637ce4dcc5d90126806f25727e68b5f74",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T22:21:26.849274+00:00",
      "head": "daf05be65c7b898e14f32d3f357a794b799e3778214c735e18516180fcd5c8ef",
      "node": "101.wake",
      "snapshot_digest": "0804f71643d8505c92d2a3b34057d8b7c66eef3a80e9c8c48f62f98c1a8017b2",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T22:21:24.487575+00:00",
      "head": "fc395c774fbbcc8a80a52695de84e2371de1acd27b242572b99932a3bb18fa6c",
      "node": "102.wake",
      "snapshot_digest": "e24c5ca730a520dfac628f31b205154edcbbcb3b53cd8ad22cf208babbf3fffa",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T22:30:41.923594+00:00",
      "head": "fedc1f413dd7980a82b9c7c67b64d740d4a95ac125c81ff0315f18f6f9bff9a0",
      "node": "103.wake",
      "snapshot_digest": "27dbc46dcc578619eeca801d9047e57cb15f2bbdc67e404edd70ebcb57683e9e",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T22:21:26.722541+00:00",
      "head": "d81838f038cfef68f76f2380cb26db85fa715c61513b8e25c93eaffe618a0bf5",
      "node": "200.wake",
      "snapshot_digest": "10e37fbca09eabcbf2d315b70be8de536109dda36d4c134f7855cf93f3e6b90d",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T22:21:26.502104+00:00",
      "head": "79892960bfd51fe45b16c2cd2df867b787cf8a0916c4fbbb3eea800d6f00ae6c",
      "node": "201.wake",
      "snapshot_digest": "26c00b72278a0a90568cd6b9b497b6de22b51eb5ac77544a79c643ec6b61e65f",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T22:21:26.826163+00:00",
      "head": "ecf4a2bf7eacf3b24280db82d430ba1cb6cf0aedbdddc280ff0876177c7b7d97",
      "node": "202.wake",
      "snapshot_digest": "1249cdb4fbd3b168d02fe4c378be92155da7f359bf8ff4d9657a6b5bcf3cd3da",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T22:21:26.448803+00:00",
      "head": "7d513a5c3ac3814afb4e93cdcf088c430be29d6d7ee6fa86e320a06502280a3d",
      "node": "203.wake",
      "snapshot_digest": "cd6edb9bc5d0f37faa452d276b95897e289dfd781f3263dd2760dd751517ceb1",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T22:21:26.639029+00:00",
      "head": "7792bc1cc3f1c60cf9fefe230f0b4a15146a6e2bb717c657b117b6443c00fa87",
      "node": "300.wake",
      "snapshot_digest": "7daa5a6e115facf702d657ebac32c29bc0fc23ffe0d80ae77581ffe3431ec33f",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T22:29:57.520114+00:00",
      "head": "714e3f73a08834d9a0905e4cbbd7495a34bf7835334096f3a1a360cfc996b5ce",
      "node": "301.wake",
      "snapshot_digest": "d5ec7a20160705f4a3a1404838a69fae029d8e8bf0ba12efe9d1a79b859a8320",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T22:30:27.973445+00:00",
      "head": "79f0658c559273047cbe3ef44de7faa21958ee2cec2f9b791dfa24178f5b39b1",
      "node": "302.wake",
      "snapshot_digest": "fd1b69ebc98ea9d07ddfb5cd328acc4c696e5e265afa87f4c9f7d045a1035987",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T22:30:34.885194+00:00",
      "head": "886bd92e55a5604841bc7a218e12e89dba0ec27bd15f6209c8da518ae124d3da",
      "node": "303.wake",
      "snapshot_digest": "b4083ed65ca2577932fa792bb0afd8a0e71462eefa0f2e8eb4591cd6be344f17",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31346432306138613535373034376466.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d31383265346562306464326234353534.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
