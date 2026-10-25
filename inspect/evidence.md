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
  "generated_at": "2026-10-25T02:05:37.290480+00:00",
  "head": "snapshot:69a648ff1323444ae4ed892f352fe45382f50b140aa6b9eb48fbb62512963026",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T02:04:44.779428+00:00",
      "head": "97ede6e293c291836e5a48caac6b748f357349bbb2e8dd349d1c02991a10a015",
      "node": "100.wake",
      "snapshot_digest": "a3bacfa259859117ac6a9e5fb4cfddf81f96acede694f5440da91951f1f441a6",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T02:04:27.281179+00:00",
      "head": "69fdfb56efe2e98c854cae96f69978dc088886d5dc2ad08a717d1c87a2511c52",
      "node": "101.wake",
      "snapshot_digest": "919a44b386653631354b8b21aea21829d5342c5f2105caad0734f25fc224c135",
      "version": 41
    },
    "102.wake": {
      "generated": "2026-10-25T01:57:14.534820+00:00",
      "head": "7a1721c2eab9fd18f81dea48725fcca537b97fafdec971fd8505b22075779bda",
      "node": "102.wake",
      "snapshot_digest": "5985b9fc7d9385a7b9bd9e5cd2051e20d9e27ccd8432b412a9e61d766db23fcc",
      "version": 53
    },
    "103.wake": {
      "generated": "2026-10-25T02:04:13.599306+00:00",
      "head": "6d94266fc08a01fb23344faad3412861914a79da412d810ad12f6aa6fc51e924",
      "node": "103.wake",
      "snapshot_digest": "76c87a6959003c13decab9d2f071204365e5906b63b9dc3b48bee84993a4a032",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-25T02:01:26.950741+00:00",
      "head": "1f8f023ed487432f4f1d4ef9df0ed7c2a2bca5c1479e4ca6d4f9a7870f8fecf7",
      "node": "200.wake",
      "snapshot_digest": "424651e832dae6b4015638a0d4d6e86354379f40511b90e3aca74ac346a2f6ed",
      "version": 33
    },
    "201.wake": {
      "generated": "2026-10-25T02:03:31.095066+00:00",
      "head": "fe9ab3e7d11366459512a3545ac56d638075f4e3bb98781f2fa66b4125739a3d",
      "node": "201.wake",
      "snapshot_digest": "527f33e36a1fe02be1e9530438b850aa3dfb519202777c40ae0e7ffe59f3c7a5",
      "version": 38
    },
    "202.wake": {
      "generated": "2026-10-25T02:05:18.032899+00:00",
      "head": "a664908c9f231650b5c5d2023f6c51a54111870a59f74a02483c73e09c46e225",
      "node": "202.wake",
      "snapshot_digest": "b4898fc4a5c5547e51a0ef8c51813b29e8824a33b918c5453c7d0f7f3e5f7294",
      "version": 53
    },
    "203.wake": {
      "generated": "2026-10-25T02:03:58.770072+00:00",
      "head": "58f4b5b4e7c7e0d6e1af0370cbdbfa392a1c43ffd4288e51bba94097420f284f",
      "node": "203.wake",
      "snapshot_digest": "1974bd27c22f7ee0d0da747832f6d9180c4355ccd660c9e16bab6d997f70ba18",
      "version": 29
    },
    "300.wake": {
      "generated": "2026-10-25T02:03:17.339691+00:00",
      "head": "203dc1a25a295bf8bb531e597e00808bf89b81b87a578d590fcdf74e872eef26",
      "node": "300.wake",
      "snapshot_digest": "2c9f76d91e196fea24a997102d760c8aa70b2ba132d7aee3f00f8e59498e6976",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T01:56:43.131177+00:00",
      "head": "bcee1cd71ef064a7771129af5d7b1dccaa6ed308881723b5263170e4ada23722",
      "node": "301.wake",
      "snapshot_digest": "b51b806cae6462e67e4b5c3c8f80cfac44f6a9fc6fdb07e4867c7212b59cc64a",
      "version": 54
    },
    "302.wake": {
      "generated": "2026-10-25T02:02:30.886579+00:00",
      "head": "9c772d9127bc7c31049dea78de4e8821c00bbf563294abfc63feb4018ad12bdf",
      "node": "302.wake",
      "snapshot_digest": "c1956f3cdcc0f0e618a4e04bf22bb6ce46ea11ad5cde49ecd8c7ff9ac1f583ce",
      "version": 34
    },
    "303.wake": {
      "generated": "2026-10-25T02:05:37.290480+00:00",
      "head": "f5d0392d9084ab504bce5fb7b05e9fbaa5d857af871c2b231642da4dd6200993",
      "node": "303.wake",
      "snapshot_digest": "1b5020c7752a7b3e9f2d510429e74b2388277268ca3e8fa79eb929ae1de64230",
      "version": 50
    }
  },
  "version": 483,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d33656232306465343632323034383037.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35363332633936653139663134613465.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
