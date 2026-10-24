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
  "generated_at": "2026-10-24T00:46:09.929069+00:00",
  "head": "snapshot:a0d2359313680eb3bc9c5fc4a3111d9c331b0ed1cff59a057ebfe51711059097",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T00:46:09.929069+00:00",
      "head": "441c2bb214367844efd0f85aa156f53784bdc8f121d92527bd7d3399cd7942c3",
      "node": "100.wake",
      "snapshot_digest": "bb99a71776b26bc0b3219730a0df878e2c8d51c1f5387d5f0ce6795721311b4c",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-24T00:13:45.296379+00:00",
      "head": "bcfdd4af91658db4397b9a195dfd91af0aec963c770bf3c845f68049dbc80149",
      "node": "101.wake",
      "snapshot_digest": "520db977c77b1ff33f3143f5199197900296f0c72ca455c323562c30583a68f8",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-24T00:13:10.598274+00:00",
      "head": "cc13edbbb74a7291785b364f4a243bfce834515b76f7666c08e301395ead7202",
      "node": "102.wake",
      "snapshot_digest": "8cb6c69215e7567513d1501885c9082c0350bc34963cab439b92323beb3336e3",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-24T00:13:39.071216+00:00",
      "head": "981c2ea9925cb14624439b9bea2c667defccdb8b3c33704225c7bae2a709e755",
      "node": "103.wake",
      "snapshot_digest": "347a1118d50ee19cd75e767feb2b02c72717a2789f5023eb800b1a6d3a019e8a",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-24T00:12:28.466454+00:00",
      "head": "47156d943d257929ca0600be1e9bc7e4631fa236dbca711ee5b52391266185ea",
      "node": "200.wake",
      "snapshot_digest": "57e6c3db95c71ab7a015db9a6456e74fcac82ff9badd6ec5646da334eaa3e61b",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T00:12:49.887451+00:00",
      "head": "0cfe4e97ea00626c5c5d8473b3e534f0511bb5dd7c74da157b4226d126456186",
      "node": "201.wake",
      "snapshot_digest": "5bbf7fcc14d10731d6a1426c56bfdbf7e2c75cf58eae92d5de0ce3111a86b483",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-24T00:13:03.994874+00:00",
      "head": "7cd62ac3281dbccb279d7af2144efd3fb09dea1c5c7f17fd22fd67951095420e",
      "node": "202.wake",
      "snapshot_digest": "6dd741b177d15b56c967357a5f838b6cd44a5b543b04f0878ed50f1d7b764934",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-24T00:12:08.753443+00:00",
      "head": "537cb8b1e60836fbd98e7dce5bc2b767e888f5df10a25cab81d0f155c83eba59",
      "node": "203.wake",
      "snapshot_digest": "10c468bc97e130ce4c73c1f12a2f71e226da9a4bf55f5f07a598148a8b192ab0",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T00:13:30.839159+00:00",
      "head": "8c2952a63312d98f514072b874c19c2a73f8f3b8e60b6a57580d5e2d7f5ed619",
      "node": "300.wake",
      "snapshot_digest": "f866c1ce7e1859b26b93cac33cbd71c9f2212c2fcf7ae4a04828f2f2453eba5e",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-24T00:12:02.150836+00:00",
      "head": "8811036be58b88e593077e7004cb902c1fa5e6775be55bc8099f28b70175cd0c",
      "node": "301.wake",
      "snapshot_digest": "2e667848a96b41519e516ec36b595a3fce9b7b92e1e190e16cf77fb01496aee9",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T00:10:50.107359+00:00",
      "head": "71a0cafd0eb552fba396d5c8396bb5d1867769ea0d1bd76bc953dc986a9c777e",
      "node": "302.wake",
      "snapshot_digest": "bd78a34de7793f0b6b38cd8c169333322b9e4a4937c41fea4f786ee413fe6f89",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-24T00:10:36.125788+00:00",
      "head": "451b574fe139ed6993e0d653689ac52b3dc215014cccc194cf159ab1e54c49ca",
      "node": "303.wake",
      "snapshot_digest": "70ff6855cb9d539b2284fa14025cfe518bd76f53dcaa7a739722f2e17bec7bbc",
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
