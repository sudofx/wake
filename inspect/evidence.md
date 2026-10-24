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
  "generated_at": "2026-10-24T02:36:26.284546+00:00",
  "head": "snapshot:4e5b46508b8bb779957e8ee0c2128da3624a31a2f1a4f596dc91f5985618856d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T02:36:26.284546+00:00",
      "head": "5fdc4ccc83dcfa5ce98c8cba68464a3246163df6584cfa9f7ef964a98f787269",
      "node": "100.wake",
      "snapshot_digest": "26d8f0b681cab7c3934e919b76e84024c5f848876b6cc5a65e65f4e2ad51599d",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-24T02:33:43.672184+00:00",
      "head": "bcfdd4af91658db4397b9a195dfd91af0aec963c770bf3c845f68049dbc80149",
      "node": "101.wake",
      "snapshot_digest": "f8f0246dde1903c5acf817cdceabf1db5a4ac0844084d01203ae2788b4572bec",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-24T02:33:41.672733+00:00",
      "head": "cc13edbbb74a7291785b364f4a243bfce834515b76f7666c08e301395ead7202",
      "node": "102.wake",
      "snapshot_digest": "b1fdd29aed3b306849e9c209d3ebf727a8aaf549817c2b22c7b43b6ec19c0f7d",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-24T02:33:43.478345+00:00",
      "head": "981c2ea9925cb14624439b9bea2c667defccdb8b3c33704225c7bae2a709e755",
      "node": "103.wake",
      "snapshot_digest": "261dcc90f5439f375bf439e215963537e5aa5958b667225e94f301be06321bc9",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-24T02:33:43.458708+00:00",
      "head": "47156d943d257929ca0600be1e9bc7e4631fa236dbca711ee5b52391266185ea",
      "node": "200.wake",
      "snapshot_digest": "ed6bda17ca8109fc8f250c0a2f90c203e056e46c40fdb6b29531f22f58faff03",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T02:33:43.452706+00:00",
      "head": "0cfe4e97ea00626c5c5d8473b3e534f0511bb5dd7c74da157b4226d126456186",
      "node": "201.wake",
      "snapshot_digest": "634a6cf880ebae2ac34674d4213569c18cf88b248b351c64cedbcdb820752e6d",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-24T02:33:44.133074+00:00",
      "head": "7cd62ac3281dbccb279d7af2144efd3fb09dea1c5c7f17fd22fd67951095420e",
      "node": "202.wake",
      "snapshot_digest": "a22e80ec7d50ba72f8db3d9f146f09219b8310d0c839f233e7474a4815098d2b",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-24T02:33:43.075800+00:00",
      "head": "537cb8b1e60836fbd98e7dce5bc2b767e888f5df10a25cab81d0f155c83eba59",
      "node": "203.wake",
      "snapshot_digest": "903751d262e2302f640ecea6ca667a18a3b2a473a4061425084a7063ab65eb85",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T02:33:43.869561+00:00",
      "head": "8c2952a63312d98f514072b874c19c2a73f8f3b8e60b6a57580d5e2d7f5ed619",
      "node": "300.wake",
      "snapshot_digest": "f8856545722faed404b86b1d30bbe37a563934c95b3dfdda1996c10d1b5289db",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-24T02:33:42.163293+00:00",
      "head": "8811036be58b88e593077e7004cb902c1fa5e6775be55bc8099f28b70175cd0c",
      "node": "301.wake",
      "snapshot_digest": "244394c7e059c9f159acb7d1c4f5a9ce30303393cbf9c784f400876747f84f4e",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T02:33:43.072584+00:00",
      "head": "71a0cafd0eb552fba396d5c8396bb5d1867769ea0d1bd76bc953dc986a9c777e",
      "node": "302.wake",
      "snapshot_digest": "0a4c43fb969fc1113f7081fb1904419ca0c28535e63c7117b2e0108fba2d4fd0",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-24T02:33:42.474168+00:00",
      "head": "451b574fe139ed6993e0d653689ac52b3dc215014cccc194cf159ab1e54c49ca",
      "node": "303.wake",
      "snapshot_digest": "57ad0055e282e8ad4b94ec71809ec666bd8b6ea8f47ab8c7098a65e0fa44e6a7",
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
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d656364343263636331383663343638/63.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a722d64383561663633336561373234356463.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
