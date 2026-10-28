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
  "generated_at": "2026-10-28T05:24:57.550941+00:00",
  "head": "snapshot:9f1ea52d6fceec80d9c06e2c9bd9094dbbfdb09b96960c38f4f6cf8020d31c02",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T05:24:33.128803+00:00",
      "head": "af4048e660d5708db46f84a740b876423daf0f096443cbfc2328f71ad1ab6c68",
      "node": "100.wake",
      "snapshot_digest": "296c9090b5685bc97e73c59d08d3faa5cc8997adfed541b5fda0d5204b2a3d6e",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T05:24:30.597999+00:00",
      "head": "f8fbd8a6f2902a076f2230f4b22fcc3f75c9062b775a66c2df05d3df5eb39fdd",
      "node": "101.wake",
      "snapshot_digest": "56783694148b44577e01a68564edee8f522d6bbc0dd4e8b2631eb3a70a305103",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T05:24:33.148882+00:00",
      "head": "285c4e672934199f5303e546fdec2eafdf1dc3784dd7f930e5e563d72101b421",
      "node": "102.wake",
      "snapshot_digest": "761d0494bd608ac0a8f1425a4215c302576553daeb44e68d29f0c6135c8585f9",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T05:24:48.381618+00:00",
      "head": "4bb1057835a39d268a3bb32295e308d9983ac811dc101c8adaa6ce9d4f2deb3b",
      "node": "103.wake",
      "snapshot_digest": "0ccc110bcd8fc9c21d09521e7992009199d3996cc45a1c6e9fdf12163bc6696f",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T05:24:48.304345+00:00",
      "head": "7d907120932ec83576ee9c73923dd225835e60a69ecba51751c48515ea9b9198",
      "node": "200.wake",
      "snapshot_digest": "be462c588ad361ca039cb682c17cf4558753ec14283aae2a202962f15a5072af",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T05:24:57.550941+00:00",
      "head": "18d226d74745e5f44a860274a9ceca489fb33f4c511e82e77468e41aad8b2748",
      "node": "201.wake",
      "snapshot_digest": "38950bbf8fc5e3366fe919b370b431ff5fd6935f4320d541b7e5215508d91ba1",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T05:24:32.825423+00:00",
      "head": "4de70eed7ba21186a6e0adda6370ac65dc01ce546977a58ac8e5591f49f8071d",
      "node": "202.wake",
      "snapshot_digest": "79039339ed66e41d21ab0e87f13f50c05e45175ac1f1a768d3a6899bc2fa4669",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T05:24:31.017193+00:00",
      "head": "a3859dcab8887138a8b612024e1ccdd98dab00fd4165e5ca38c984d3cfc2ed11",
      "node": "203.wake",
      "snapshot_digest": "87e3ef7ed9b74e8a21227f81f53c0229e70eaec624220ca5fea039b4b28463d1",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T05:24:32.046745+00:00",
      "head": "dcfac50f93a85964d0d5356b29a7ececc4b6350b229ba5cb3cf8d02f8a12aa98",
      "node": "300.wake",
      "snapshot_digest": "81774066958d24473846bb387ce6c199394ea4f72e50336cd3515067b093250f",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T05:24:33.319605+00:00",
      "head": "9b4e98c8fdf7958ef1d2e2cadf7ae936d6109de9c8f74753634c83a3b5448216",
      "node": "301.wake",
      "snapshot_digest": "7b4f2b3764c02a2dd324b57529098820b9314160dc1df08d66edc5ae5c6b8f2b",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T05:24:28.473358+00:00",
      "head": "8f37876b3dd2f5cd87c38ca98bb4b932d4560417d046755a2493b0833689aade",
      "node": "302.wake",
      "snapshot_digest": "2f273fdce7134722ca77fb7dad6ce99cb1feee0ea7ceba5c170296b938d517c0",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T05:24:41.427928+00:00",
      "head": "4be95502ccd1328aeae8671863d1009378e26ce3c109c122f1cccfef3acddc2c",
      "node": "303.wake",
      "snapshot_digest": "045b557519598de2df1421f3e317c1bbacdc467d7356ffec1168fd525c0eee7f",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d65326239366361623538336434626437.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d37383533343466336332363934653434.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
