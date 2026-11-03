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
  "generated_at": "2026-11-03T23:00:44.815167+00:00",
  "head": "snapshot:18048b23829be16dc6b7ce1a1de46ea8c61689350c0baabe6103b4cbee3b9f6e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-03T23:00:44.815167+00:00",
      "head": "d7e2d1efaa0cd29064f42165e876f22cc45ab9e3d3ff5ac6b36012ed2f43444a",
      "node": "100.wake",
      "snapshot_digest": "c772edf8963372810b37a0df7d5a95e807d9579113ca688fa4b1ed3c8002b468",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-03T23:00:44.115972+00:00",
      "head": "340720f1af4bec202f25c96366a6c86140f97736f8e3ba331ed40829c55bcdb3",
      "node": "101.wake",
      "snapshot_digest": "b29f2a6a45bef831e6aec1326e3b35e36dfcad59dfc6899b6d525906acdd5354",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-11-03T23:00:44.453642+00:00",
      "head": "2b2b05085f6a8d16609f5d925a6297c781a8d5be892df980c6059a3ea31a9906",
      "node": "102.wake",
      "snapshot_digest": "b68eed81f392510234c9c1d666f3534f1f14a369e0f0eec5fa715c389ee08dba",
      "version": 3
    },
    "103.wake": {
      "generated": "2026-11-03T23:00:44.092852+00:00",
      "head": "a94466e12054d45448886cb95cca88ee3a244cd711d19c93cee99a0205379eb3",
      "node": "103.wake",
      "snapshot_digest": "090b0f0891550752a64a2ace24dcc910ca89dfc21e5924538721871abf10d605",
      "version": 3
    },
    "200.wake": {
      "generated": "2026-11-03T23:00:44.781261+00:00",
      "head": "a8f911eb8a856ecf4d52791c44dfd79aa97160000dba8d93c195aeb860a549fd",
      "node": "200.wake",
      "snapshot_digest": "85e3c231b05e15ac12c8ee20ec1b3fce9d60b9bb91bcbf11c5135dcf074d9810",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-11-03T23:00:44.534853+00:00",
      "head": "fb43e3510712572d18575540883fa108a9c939cd05a2fe944742745ec261d37f",
      "node": "201.wake",
      "snapshot_digest": "7c53fb49e990393c295064cb2d70cf9e1cc7835527f8d104b6bd38fb091e2dd6",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-11-03T23:00:44.341851+00:00",
      "head": "04b40c2811e85984971d356f57149eaceafaf64c3fd6812caf102fc07577a7c9",
      "node": "202.wake",
      "snapshot_digest": "4b86d89f63f4d31d6edfbdc024c1f302cf19f19b6288ff08b0c7799fb67e155a",
      "version": 3
    },
    "203.wake": {
      "generated": "2026-11-03T23:00:44.200889+00:00",
      "head": "a7dfc5a8933e8e89e5ba5eeceeaf7a3c70662be247292c555425067565c80ae6",
      "node": "203.wake",
      "snapshot_digest": "6a843fa7ae05a063d271ed453f7c44430ee470797760e5b8a4059d039835bcc7",
      "version": 1
    },
    "300.wake": {
      "generated": "2026-11-03T23:00:44.284752+00:00",
      "head": "9efb9b3d009aa35fc9e1486afdf408a621163ac9b5a8827294f7a7bce276f945",
      "node": "300.wake",
      "snapshot_digest": "d28add45d48cc3dc7cfb7b75a9a92f798979aabc65d39c1891d0dee6554c691f",
      "version": 2
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
      "generated": "2026-11-03T23:00:44.711446+00:00",
      "head": "18914f4206e86ebc4d285c91df66f7a882f4aee03dff00b392897f4bb54c001e",
      "node": "303.wake",
      "snapshot_digest": "023e8d24e6eb230c995f1f934882608c808ad678340b5cdb1ab53915738208c9",
      "version": 3
    }
  },
  "version": 25,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d64386331633564363364613434366635.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33306134656630323065643134316636.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6469/73636f766572792d696e666572656e63652d626172726965722d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
