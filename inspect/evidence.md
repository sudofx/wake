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
  "generated_at": "2026-10-23T20:39:39.614637+00:00",
  "head": "snapshot:f51e5f162fec9ec87e904092e731f73108e46dfe0bdec619abfadbecb5f02a41",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T20:31:21.033347+00:00",
      "head": "bea08d7d93826363b42500ab4a4f94c2116ef8c0dd400b495c4710da7b75f3a6",
      "node": "100.wake",
      "snapshot_digest": "2d7157c5f59b8d0a60a6be1f5606e780b6bdd063bc5f58d307ab8389b867a3c0",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T19:59:48.440478+00:00",
      "head": "190ea79644a9accf284065ee5040f508d99c9b753cd50f296900f77a47d35ebc",
      "node": "101.wake",
      "snapshot_digest": "d06ecebadb205405e864865ea46aae175628979646c29ac45ed2ddc9869edca6",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T20:35:22.954047+00:00",
      "head": "7511a19dd689bee449ed4cd32af9d99ff684591897330b876d32ac30e953cd54",
      "node": "102.wake",
      "snapshot_digest": "ce958df9d4500a1b9c393d53b886362697308cd3b8a443296019978087afa6d0",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T20:39:39.614637+00:00",
      "head": "909289776d67641c44dbedff284840559a5024617c4d5a9ad01a619f1902f264",
      "node": "103.wake",
      "snapshot_digest": "29e3a073d2f76d1e2012d1b76a9b4804b3a717d6aad85b2304800cbc3010955b",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T20:34:11.649927+00:00",
      "head": "83ddb512cbb57038fce29f8694ade5e9f3caf52fda6c514e43881c573e691b2f",
      "node": "200.wake",
      "snapshot_digest": "83212eed9de588770ab9ce5de184feaa99c301be81c776a50f1b5a973e406ce6",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T19:59:31.938237+00:00",
      "head": "87a9296ec6686e03220fe7acb1dd8d1b1a954e3f68ab34d4304106e4b097e252",
      "node": "201.wake",
      "snapshot_digest": "d835d7bf6c10907797c18cf571d334785b909f64c30aa1e87cc91597f1b4d2b0",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T19:58:24.986488+00:00",
      "head": "4e81a910422f71079fd4f1e83eacc022c97e86278e011b6c0c639f19e5bf89e3",
      "node": "202.wake",
      "snapshot_digest": "06fadc776dc5afb42d4dd67e94765dcdd12b97f54d4f46c643b6ecd8d070b6bc",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T20:34:04.156593+00:00",
      "head": "fedebf1d0046a6bb37c3e8183a7f011f880eefd03532564bbb48a9c62b2af7ca",
      "node": "203.wake",
      "snapshot_digest": "c2aaaa69e8448b2eb205c776580cf1cdead3c173a1879fe101aafe28eb8012f2",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T19:59:25.510814+00:00",
      "head": "4825d55fc48939db7a523e9dba132af108caa5a2359767f43d56f4bb5959a1d4",
      "node": "300.wake",
      "snapshot_digest": "13546404938dbb89ff873a79889ded0ca9795bc81ad812f5bac10968d24d8c52",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T20:33:13.615118+00:00",
      "head": "f1dbe99552c51e3d2a4ff82d8b5dfef31174e54f842a635fc690d262a95841c1",
      "node": "301.wake",
      "snapshot_digest": "ef2e2859c10f3d111c06e4bfaa4189769284571c974972b0e68a45e0b43994a5",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T20:33:06.516076+00:00",
      "head": "a55ae298d5b340c6cacedbb810adf8d2e3b388c56493cfe1a8f24c9e9c4edf15",
      "node": "302.wake",
      "snapshot_digest": "c4d992c7e06f923a9b2bed59deb80dff65f336a67d652b8bd41a595d6242f2c5",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T20:31:45.212119+00:00",
      "head": "cb19ec0df532f0f2871e6dd35862f337f8f2647e1b1bb9316b25aed6fda00f33",
      "node": "303.wake",
      "snapshot_digest": "9c3e84ea2da1ccafe081ddf676ae735dc69905875666c4098f7fe9ebaea64c76",
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
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d346130376132626365323537343334/66.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d613036636264373761643834343135/39.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
