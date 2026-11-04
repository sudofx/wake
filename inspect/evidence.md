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
  "generated_at": "2026-11-04T02:01:55.406942+00:00",
  "head": "snapshot:1ff978122003fa2e953a4f4d758f783ea3177a0ccbc9560311d184baa059035f",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T01:56:48.555632+00:00",
      "head": "96e0a8d472c838e43663a1465bbf909e5f4c7e31baa51d15b9c5552f2efb5aea",
      "node": "100.wake",
      "snapshot_digest": "7e0465a0b185911492bbdf1ae9f97b2b738be581d80a301f52c2841e43c50f06",
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
      "generated": "2026-11-04T01:39:30.054920+00:00",
      "head": "a61ea6c8f69af6c757f54707088eca5b7fb0796c1e9c482eadf1c6d23b6a6d53",
      "node": "102.wake",
      "snapshot_digest": "73a4340943893028545291b1cbd1e5ab8b2077d265384637547d6ff1ca4af2a0",
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
      "generated": "2026-11-04T01:55:01.216183+00:00",
      "head": "013fe4a6b2f1f97c3b0c9578768228e1ae2873d5d9b46d9a262c1b663050550f",
      "node": "200.wake",
      "snapshot_digest": "a75613142bca32b8972e8ffb93236204584a79bce5de16c198b8a9b9ac24b606",
      "version": 4
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
      "generated": "2026-11-04T02:01:55.406942+00:00",
      "head": "f11548b76cac9f041b3b3da559139ab339ce01ffec4a6e95f91a7c85d36b1fd0",
      "node": "300.wake",
      "snapshot_digest": "22a5a057629d207c46bdc62d67327236cc21477f26f9db2fd1f8385d3f7809c1",
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
      "generated": "2026-11-04T01:49:49.061048+00:00",
      "head": "06b60956ba6f87a824c1d00b0c3da0191cd24d6cfea7a8a11276f1fcc51b8e1b",
      "node": "302.wake",
      "snapshot_digest": "540035276c583c832e5a636ae79a2a48707f818645ed65dbdb8d082f98a78fa8",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T01:53:21.622659+00:00",
      "head": "2ee141e2472897db47a9e7a15c81024b1e6aec09f3b65635ae52f2121ad20dd7",
      "node": "303.wake",
      "snapshot_digest": "f9571d3e039eee076a15cb4890c619ced4366afb681edd4c4bd8f1f20b256cee",
      "version": 8
    }
  },
  "version": 56,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66633938323739343830313234636563.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66636538356533393661363634623037.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
