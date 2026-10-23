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
  "generated_at": "2026-10-23T01:06:46.158404+00:00",
  "head": "snapshot:f7796ff6b1a04c9c34c6a886d1db46b31dfd8aaa628f18e973802f7e39ac5c18",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T01:04:08.489102+00:00",
      "head": "bdb6b4457e3d08e42e60fcd797532097dd6c9f227d0dfc54cc0a9a105ee4ea9d",
      "node": "100.wake",
      "snapshot_digest": "330acfc3b5b4a3b7e134fb53e96c25d17a308706e1f08f77f5f80537e64bbd37",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T01:06:33.723846+00:00",
      "head": "f7940b5343d8844acc941dbc095692b03bd3fa20e7afc442c2af1e0c872fb0d0",
      "node": "101.wake",
      "snapshot_digest": "b0928d361dc1b4155ea0fc4cd289fe17bd4137fab6a3fc2f8c883dab06e0f136",
      "version": 11
    },
    "102.wake": {
      "generated": "2026-10-23T01:03:50.993169+00:00",
      "head": "de33b82c05d56db11594f1100f4d4e8c88f3b7f0108afd94e577250410f5eddc",
      "node": "102.wake",
      "snapshot_digest": "9d33413f0484893636253208a109eca5a9333213cc73271a3ad3396f74054a93",
      "version": 10
    },
    "103.wake": {
      "generated": "2026-10-23T01:06:46.158404+00:00",
      "head": "1fa94f4e5ccba162b2e98628c638dde411a2f0421167a3ef09ac9416143abebe",
      "node": "103.wake",
      "snapshot_digest": "2cd27c270ea87e9b15e4902507cd01ea7f33a906217d9b3eb848cd13da2114d1",
      "version": 7
    },
    "200.wake": {
      "generated": "2026-10-23T01:04:52.538789+00:00",
      "head": "3bc26447566a1e5586cd6f01af4147a657262d5fb97aab655f4a072f5caf90ec",
      "node": "200.wake",
      "snapshot_digest": "170680384e1af098008cdbbe313f415a5c35b3ca63865f5c793b113869d20c12",
      "version": 6
    },
    "201.wake": {
      "generated": "2026-10-23T01:04:47.429116+00:00",
      "head": "837b72a4b8fce5c2599b6e6ad7bfc1962ff0773a02b535abae9d0d98f2564575",
      "node": "201.wake",
      "snapshot_digest": "a68237d42f412114c9dff751507581e0c8dfd6055a307441988a743f77656b64",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-23T01:05:51.801279+00:00",
      "head": "11ef09b89db5bda6432413be42302bcd305d8d2b417fc13c4b5b936e20307129",
      "node": "202.wake",
      "snapshot_digest": "b9f45c9bb93dc2cf534740504048fe3b7fca6f576ac21344ec6c9a2a2299d5d1",
      "version": 14
    },
    "203.wake": {
      "generated": "2026-10-23T01:04:17.632046+00:00",
      "head": "df95cb4f8f185f9b9a36bed57252b4b0ee687251ddc69039644080edecba0b2f",
      "node": "203.wake",
      "snapshot_digest": "b8709ba4ec0eb415d3f128515d19861d07b5d24103909eeffb3ce8780bb0d69a",
      "version": 6
    },
    "300.wake": {
      "generated": "2026-10-23T01:05:42.908638+00:00",
      "head": "88b5286c20b26ac94b00a1dc6b884e47deef5015e5beb42f47a90272ba22cdab",
      "node": "300.wake",
      "snapshot_digest": "426afdff367a8433c55f855acaa2ef7590007597964aa4fd1913e981c2cbb78f",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-10-23T01:06:25.568667+00:00",
      "head": "f91dc38e429bf597c723cd905cff451af2a966da95b5f5e28ddf364587c83a70",
      "node": "301.wake",
      "snapshot_digest": "b648033e82c6720c1695dec0a009076e4fdab4599d8d3017de696a831a791ba7",
      "version": 9
    },
    "302.wake": {
      "generated": "2026-10-23T01:03:18.378107+00:00",
      "head": "1ace0842fea429bd1d068d298401a9ba48d201e3e105ce0969b38f1f8c8debc0",
      "node": "302.wake",
      "snapshot_digest": "8f19b9a34cebfa114f1ed2558b645a5957ebbe88316f0ae1226cecf8bb91ea00",
      "version": 7
    },
    "303.wake": {
      "generated": "2026-10-23T01:06:06.483295+00:00",
      "head": "31296061ad7f24d18b824939c4597400ff390c900a81d646aeae41d392d6d4eb",
      "node": "303.wake",
      "snapshot_digest": "63274379efd864dd26b6bb020af14be03d7f5a8bed6803daf26ddf02e0db6c15",
      "version": 15
    }
  },
  "version": 106,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d33.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d313232326335643465396236346664/63.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d376630323465363439613633343037/38.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
