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
  "generated_at": "2026-11-04T01:32:32.263143+00:00",
  "head": "snapshot:75bc94da2dec1341910388ee497e73bb737be588871b45b3b6fe95d22059695b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T01:02:56.281468+00:00",
      "head": "4ea1b9bfaaeea9d2a52f1ada644cece1ce34964db822a5ad0011098244c73c01",
      "node": "100.wake",
      "snapshot_digest": "a3f518b8c766b9043bd773e654ccf32e0a6b46097b4ec8ba91b0602a5f4ee3bf",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-04T01:02:56.458763+00:00",
      "head": "330204ec2d19213dcb85a641807d0f69d7f55a5ef84c3653dd9803a4e84f7aa9",
      "node": "101.wake",
      "snapshot_digest": "47de833eade479f440f88064cc65a2c36785e8104763ade845c7eb7793d74e37",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T01:02:56.204792+00:00",
      "head": "c4c912feb47bb74dfbfa436ba5b7c9f173518d617d0c5084c78d268b0d2f832e",
      "node": "102.wake",
      "snapshot_digest": "69e39ced3253404c366d00e3b1029059157707e94c78b3583ed7211bfbad2f1e",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T01:30:50.998004+00:00",
      "head": "4052c23409c78a55361af557278672ffec149d982210d5c9e6c01b25f9fba6e9",
      "node": "103.wake",
      "snapshot_digest": "9709619ac16960a4c0b03018a20206216ff0c9bcc8ad8f0b1b291b81293166e5",
      "version": 7
    },
    "200.wake": {
      "generated": "2026-11-04T01:13:33.638193+00:00",
      "head": "60b805404b87c3f9c641b7c2f80b7740be3d81b292100255a04cd5efa10c6acc",
      "node": "200.wake",
      "snapshot_digest": "acb740da2e40abb58c0671fd43a9f8a9c483ea67401ae2527d5f76474edf7671",
      "version": 3
    },
    "201.wake": {
      "generated": "2026-11-04T01:25:35.909384+00:00",
      "head": "7c61b57cadcde568f8d575700069080dd02615e425c1af39604884f494465cd9",
      "node": "201.wake",
      "snapshot_digest": "ab626799a06954ec1bd6ea92c1b86164984d82331c89467bc9d1843651815223",
      "version": 3
    },
    "202.wake": {
      "generated": "2026-11-04T01:22:05.459594+00:00",
      "head": "ec6cf56b5f9335c6363ce1035c3dc2863b1b0449e33e410478414223d886b062",
      "node": "202.wake",
      "snapshot_digest": "c5088935d5b261002a7b1c278e256e8fa79bef965b9f383e46ddb9938a4b7d5e",
      "version": 7
    },
    "203.wake": {
      "generated": "2026-11-04T01:27:21.457177+00:00",
      "head": "1c3fcd19750498266bc92155a23b53e2200549e406910c3773987035a1940997",
      "node": "203.wake",
      "snapshot_digest": "dca71c29ba7f5a1da8d178dbcf209a145bdeb09e6d0f28fe7ee3858f76790730",
      "version": 4
    },
    "300.wake": {
      "generated": "2026-11-04T01:20:34.474353+00:00",
      "head": "23d8a5c8decb4205d40ba526d00a9da5b746ad4c4d5bf4a815e299bc6145821f",
      "node": "300.wake",
      "snapshot_digest": "26a216ad3d9eb5d424060416b1d34847afce9872d238cdb9be3497dd7f7b9612",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T01:23:52.217794+00:00",
      "head": "468622a5fe78b7c7eb2106fef62539e67bd458e859d644e120009e172fa8c722",
      "node": "301.wake",
      "snapshot_digest": "d5e7bf0b6e3a2469f0f471480941295138bf37ec7f38d9a89a38fe8d9e9ceffb",
      "version": 3
    },
    "302.wake": {
      "generated": "2026-11-04T01:29:01.026476+00:00",
      "head": "18197f4b23b0c16cbb929ed9214c7dc28b65b0f955cf7e30406331cf04d8c469",
      "node": "302.wake",
      "snapshot_digest": "924a6cc0d181aed47884f5584b5580d3c0735d82d7ecfdc379d42ef889de5044",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T01:32:32.263143+00:00",
      "head": "55a7e80a28282af98966caacc040e35b282f8b0801fbba219cb53c94edd51a6f",
      "node": "303.wake",
      "snapshot_digest": "ccb866bb4f0331958e98a05acc65b92f06f743f6fa8541efde4af43eb4704493",
      "version": 7
    }
  },
  "version": 54,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d30336136356361326136643034336362.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66636538356533393661363634623037.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
