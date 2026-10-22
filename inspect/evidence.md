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
  "generated_at": "2026-10-22T21:27:16.005773+00:00",
  "head": "snapshot:b5e2286a5b54ca063ca3e8bced88b3981d5bb5fb7be1788c00e86cbfdb5efa65",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T21:26:32.793904+00:00",
      "head": "ad9249922312b00120eb084303a06a53d0914d257edd8002a703279b70396ae6",
      "node": "100.wake",
      "snapshot_digest": "16a54ce2ce211f9ba5f2ee62db8ac2a390e2f2473fbd4a19b289b26be3ce4333",
      "version": 1
    },
    "101.wake": {
      "generated": "2026-10-22T21:27:11.610301+00:00",
      "head": "c20f7a58bc7bf311637bc0de50c4a12fb59a9e6ae74036239cd84e86ea6f426a",
      "node": "101.wake",
      "snapshot_digest": "8a7adf7ff36876c046e775501ae921f576d94c366d3000b1256f6eb9af5792e1",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-10-22T21:20:11.223586+00:00",
      "head": "8ff3300bf8a112eaa37f3fcd56c87505eeb809bf8b8e76dd972379acff32c469",
      "node": "102.wake",
      "snapshot_digest": "e135fc14b5a5c443680a43e3d939fa208cabf32082d668dcaada3df9c70489da",
      "version": 1
    },
    "103.wake": {
      "generated": "2026-10-22T21:25:21.155093+00:00",
      "head": "24fadae509e35b0d2ff3514ce9392be0d3aa5be808290b73d72b014202c6dfcd",
      "node": "103.wake",
      "snapshot_digest": "8c46328d6f9e8dcf618ec521e8fca11dc1738ad57dd70d9c3a01fb80684e37d6",
      "version": 0
    },
    "200.wake": {
      "generated": "2026-10-22T21:25:30.953711+00:00",
      "head": "5bd5be7a01fdfdb29c46639ef221dacfe5d08674bd80a19b66752730d22fe308",
      "node": "200.wake",
      "snapshot_digest": "93c9a312ef22c1b99bce4304e9f5bb30546562625dace72b1e2427c95b7dafa5",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-10-22T21:27:04.366526+00:00",
      "head": "c1ee017eb0559908dd7bac07ad2ffc7a3974662c4e191919ee2055f8102008ec",
      "node": "201.wake",
      "snapshot_digest": "45b704b4b21be663c18336841e5896c86712e9131a08e01f0f387a744452341a",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-10-22T21:20:01.943028+00:00",
      "head": "320c2dc717074ed0a18a2fb897b957ff03b742decc6c196ca4699fab9458e00b",
      "node": "202.wake",
      "snapshot_digest": "0bf8e97e43d33703c4d5888021c52264f367d80cba9f5fbfd530e6b7959cff7e",
      "version": 2
    },
    "203.wake": {
      "generated": "2026-10-22T21:27:16.005773+00:00",
      "head": "b19f2f8f3c2f23536c7f4261d726f54fc8e6dbf0da6e5863c4241cee002c2bdf",
      "node": "203.wake",
      "snapshot_digest": "4cc58883e57da591714563ff1f9d855912e2b84db3a7f3237a37b6c8bc69a185",
      "version": 1
    },
    "300.wake": {
      "generated": "2026-10-22T21:25:37.915968+00:00",
      "head": "06b53de210a50711ac662996ea2461758d27b415a4d44f9f9c750da708a6eb6a",
      "node": "300.wake",
      "snapshot_digest": "32e410f1526418c15092e88ab0c5951bd4015fbba1380a655ad46d1b877ae5ac",
      "version": 1
    },
    "301.wake": {
      "generated": "2026-10-22T21:19:06.281578+00:00",
      "head": "b2ba5c8a6c10218b55ca224c1d5baf121c7e2ac720245911723cc6723dbe69ea",
      "node": "301.wake",
      "snapshot_digest": "f8e4071aacbda33f1fae5a04ffd022690a4fa06dffd5cd76eb08d5e1c7ee00af",
      "version": 1
    },
    "302.wake": {
      "generated": "2026-10-22T21:20:08.971801+00:00",
      "head": "44dcf370cce567135b514d7fbc2d6a827f6b7b4ad2a83d6f42e03020ab447a2f",
      "node": "302.wake",
      "snapshot_digest": "a4e33bfa0acd87a374fd39a957f6e6bcb77061985d4b902650652acf3d612365",
      "version": 1
    },
    "303.wake": {
      "generated": "2026-10-22T21:27:13.843287+00:00",
      "head": "23b6eaabf31a62e409ee4a059b3b595158f9872cedc8d7de47473b6ec05d5b07",
      "node": "303.wake",
      "snapshot_digest": "8469104ac2bbfc90ee302ed71e8dc8e0413e4dc6e33ed7c86a0cfe70280106cc",
      "version": 1
    }
  },
  "version": 14,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d343038323864336131633537343531/61.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35663132346338363039323134313763.json)
- [notebooks record](../reader-records/notebooks/3230312e77616b653a3a6e622d656d657267656e742d70726566732d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
