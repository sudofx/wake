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
  "generated_at": "2026-11-03T23:59:45.824078+00:00",
  "head": "snapshot:8327c8664ee6ca1431c35926bc00a6b7e05da7effad1929e687c98ba26460387",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-03T23:58:00.743209+00:00",
      "head": "0166ca78cc29cd9e86039001de799c107d783ee02b97a39e0befa691edbd8976",
      "node": "100.wake",
      "snapshot_digest": "b7a7e58dc7e20ff8d67002a09e4d7b0ca3315e2dbbc1327341fcf4519f2b273c",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-03T23:49:44.885051+00:00",
      "head": "fd8a1b96d7645467b87f1c736e7f504cb7a012deffd833dfbb8b757db08d4f3c",
      "node": "101.wake",
      "snapshot_digest": "3a235dc27370d848a6ff395740878d7bf103dac90afa0ca7590b60e8ffb7f509",
      "version": 1
    },
    "102.wake": {
      "generated": "2026-11-03T23:51:04.933750+00:00",
      "head": "6fa22f960f2047b1162a495f66845e08a8ef53fce01a3a41f1486ca16441263f",
      "node": "102.wake",
      "snapshot_digest": "528dfa465df3f53c4795a6e82ae8842635a755a2c3ee0acbbd3dc06684e9d26d",
      "version": 5
    },
    "103.wake": {
      "generated": "2026-11-03T23:32:02.019015+00:00",
      "head": "ffbb6e79e4ec908abda2d453248e5549ae4cc64ef7ee9cd6251bb5962e2a69b2",
      "node": "103.wake",
      "snapshot_digest": "4726a2fcb750c81ad938553269b90c2a49c8b1bd3777a49fcc33eb45fb198a6c",
      "version": 5
    },
    "200.wake": {
      "generated": "2026-11-03T23:20:02.536713+00:00",
      "head": "9d66701261f17c79bd670afc5ec19cfb49cff4a01555d0b2ac3753672c779d22",
      "node": "200.wake",
      "snapshot_digest": "f9c37d5d56360c19cc36d6be91b5d2508fe569b20d9d082785d78696a4d65c67",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-11-03T23:54:36.078107+00:00",
      "head": "d535753bd85bf422c3958b08278970b8c154bfafc2c28e0655a09cab45035159",
      "node": "201.wake",
      "snapshot_digest": "9a69886e6c4b231c02275956c4ce3423f3ed0ec3b49783c1174574f6c7a4678f",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-11-03T23:47:36.556554+00:00",
      "head": "7e06e58e3f8603ad9f408341e5c584c346b96f1ec982cbddc59b1b9abbc14777",
      "node": "202.wake",
      "snapshot_digest": "48cc025612aaf750704606813ce0d9f3d58a5c1690f27420c943c07b04a72dd0",
      "version": 5
    },
    "203.wake": {
      "generated": "2026-11-03T23:25:09.483756+00:00",
      "head": "703be4c51d6b31d94b44afd259d3a9adb68582753a68fbccd34ec49f6b9f3c87",
      "node": "203.wake",
      "snapshot_digest": "c8e2cfc288397a58f7da275194e302832bb3185b08d7c8749b91eab2ff7ed0dd",
      "version": 1
    },
    "300.wake": {
      "generated": "2026-11-03T23:59:45.824078+00:00",
      "head": "643c85d84baff7ec6aaac7cd53bc6fe6a194c22570ef0dbd9d6b7fb135ba9e2c",
      "node": "300.wake",
      "snapshot_digest": "3a35715c87142440efe73565d56eca771def88979f60c9299fd1993a88edcc50",
      "version": 4
    },
    "301.wake": {
      "generated": "2026-11-03T23:00:44.189508+00:00",
      "head": "d79cc98a6585deefc99f5e984c08990c70109af900eb2a4349ee7e8615906e62",
      "node": "301.wake",
      "snapshot_digest": "272f781d27b1ad72a410f7d7b4d7063536ddcd7b8a1babfcfc7f2bbb94b57930",
      "version": 2
    },
    "302.wake": {
      "generated": "2026-11-03T23:00:44.497102+00:00",
      "head": "105460cf6ccd86f76799be087e8c376ddd97ff6f6328b18275ce9e65010e1d0a",
      "node": "302.wake",
      "snapshot_digest": "7f0db0bd39f804e05a4f28239b88ba15e6a9543dad705367ef88cb38ff689d73",
      "version": 1
    },
    "303.wake": {
      "generated": "2026-11-03T23:56:23.526737+00:00",
      "head": "5bfb4e8fb6fd1465a32e6e6456f6a2fd1c517a0e02c48b39dff4d3d1911139cc",
      "node": "303.wake",
      "snapshot_digest": "48adca31fc547234e273758226a2f1ccf7af8abd6fa28cb3424b62915cb2e0e9",
      "version": 5
    }
  },
  "version": 36,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33326235656263383832303434343533.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d62346264356338663933373934393132.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6469/73636f766572792d696e666572656e63652d626172726965722d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
