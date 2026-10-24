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
  "generated_at": "2026-10-24T03:48:30.033273+00:00",
  "head": "snapshot:763f794aa1d2f67de4bc1c1a48e282c17dd349162c7602d34f5910a8738f9833",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T03:48:30.033273+00:00",
      "head": "647a479d59a9d7f19e8141b38c5a255cebb269acf268fc49cfc6436a4365bdeb",
      "node": "100.wake",
      "snapshot_digest": "1b51b88716c4597852015ef82c47bf7585aaf56ed53d05f541607bdad37edd67",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-24T02:48:13.596898+00:00",
      "head": "bcfdd4af91658db4397b9a195dfd91af0aec963c770bf3c845f68049dbc80149",
      "node": "101.wake",
      "snapshot_digest": "cca8d0f44ba1ceec771e4b4362d941adb6f094b30ba0caf3dd2e03856ddd8c58",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-24T02:48:11.111188+00:00",
      "head": "cc13edbbb74a7291785b364f4a243bfce834515b76f7666c08e301395ead7202",
      "node": "102.wake",
      "snapshot_digest": "eed6b26903f2e849f0a14a2bb7bdf621bdd8445938310ae12b9cf355e7d2dd22",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-24T02:48:12.825391+00:00",
      "head": "981c2ea9925cb14624439b9bea2c667defccdb8b3c33704225c7bae2a709e755",
      "node": "103.wake",
      "snapshot_digest": "817a17047066315578ca942bc8309165a639e5465ae037114ded2ce926d7632e",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-24T02:48:13.626914+00:00",
      "head": "47156d943d257929ca0600be1e9bc7e4631fa236dbca711ee5b52391266185ea",
      "node": "200.wake",
      "snapshot_digest": "6e20b7cd3108e3578163da496cb89f3921166b33e168772851e746408697d211",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T02:48:13.070187+00:00",
      "head": "0cfe4e97ea00626c5c5d8473b3e534f0511bb5dd7c74da157b4226d126456186",
      "node": "201.wake",
      "snapshot_digest": "931358fa4c3fddeff2078d16066e6366d134a53b3b5dada001346ae46c445f2b",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-24T02:48:13.090975+00:00",
      "head": "7cd62ac3281dbccb279d7af2144efd3fb09dea1c5c7f17fd22fd67951095420e",
      "node": "202.wake",
      "snapshot_digest": "bd0d3ac423f1cb215764cfe43768385aeb473b4d38474c31406f9f950b832942",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-24T02:48:12.335249+00:00",
      "head": "537cb8b1e60836fbd98e7dce5bc2b767e888f5df10a25cab81d0f155c83eba59",
      "node": "203.wake",
      "snapshot_digest": "2330eed16d3a56ba3dcadf52c76c9fc2e3f5cd49a0da4e2acee2ad5ec2994795",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T02:48:13.919653+00:00",
      "head": "8c2952a63312d98f514072b874c19c2a73f8f3b8e60b6a57580d5e2d7f5ed619",
      "node": "300.wake",
      "snapshot_digest": "f58b14b32244f6f3de14895f1e50c6bcd7d4aa86e27515be93a0bf0dbc16ebb8",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-24T02:48:10.999493+00:00",
      "head": "8811036be58b88e593077e7004cb902c1fa5e6775be55bc8099f28b70175cd0c",
      "node": "301.wake",
      "snapshot_digest": "cd72407dbad7bcfa70728ce4f05926287f18235415677ee46db38a5b1a4e8892",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T02:48:11.455417+00:00",
      "head": "71a0cafd0eb552fba396d5c8396bb5d1867769ea0d1bd76bc953dc986a9c777e",
      "node": "302.wake",
      "snapshot_digest": "81b509dd88591a9813930b029cdf6e2b592bdd483c9d340a5f6a77e0f0c2dd5b",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-24T02:48:10.969283+00:00",
      "head": "451b574fe139ed6993e0d653689ac52b3dc215014cccc194cf159ab1e54c49ca",
      "node": "303.wake",
      "snapshot_digest": "dee8b6e495f1c21faccf9e3b9be10ed869b49e84c35c020cba7cd4b3de7f6157",
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
