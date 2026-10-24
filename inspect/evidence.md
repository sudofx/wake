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
  "generated_at": "2026-10-24T02:02:39.017965+00:00",
  "head": "snapshot:bb37fdf8eda0000324d76e829b28b1417071b719113709e3acb697470200bff2",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T02:02:39.017965+00:00",
      "head": "96bc393eb94bb2e3037182553297d7c5f6ee187685ca92326c8b61c623ca459c",
      "node": "100.wake",
      "snapshot_digest": "d045f0fa39f1b8d3656c7e686c0823cf4bd6a8bb528b091179ba8ebadc023901",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-24T01:06:49.842235+00:00",
      "head": "bcfdd4af91658db4397b9a195dfd91af0aec963c770bf3c845f68049dbc80149",
      "node": "101.wake",
      "snapshot_digest": "b7bb2a45709fbf2de12d9a68e09abf743d112bc50617166d37cd8a10647abb1e",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-24T01:06:46.973687+00:00",
      "head": "cc13edbbb74a7291785b364f4a243bfce834515b76f7666c08e301395ead7202",
      "node": "102.wake",
      "snapshot_digest": "d23798b1aea1195136ac4f6d2470d3ff12281470b855dd9ed4022b30cc6fa7c0",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-24T01:06:48.845013+00:00",
      "head": "981c2ea9925cb14624439b9bea2c667defccdb8b3c33704225c7bae2a709e755",
      "node": "103.wake",
      "snapshot_digest": "1a7f3def060dcba744f40c587d634c4796b3a1161a0eb1201f06ff7f6882cdc0",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-24T01:06:49.559044+00:00",
      "head": "47156d943d257929ca0600be1e9bc7e4631fa236dbca711ee5b52391266185ea",
      "node": "200.wake",
      "snapshot_digest": "b9a647a2d4e4a0fab348d020ede0c4d1e16cafd711b26f4c849701d4a17badf9",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T01:06:49.533132+00:00",
      "head": "0cfe4e97ea00626c5c5d8473b3e534f0511bb5dd7c74da157b4226d126456186",
      "node": "201.wake",
      "snapshot_digest": "82b5addc2d492968487c9347ae37cb72b8a72487f22d4f032e35b93d6a1ad88f",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-24T01:06:49.316191+00:00",
      "head": "7cd62ac3281dbccb279d7af2144efd3fb09dea1c5c7f17fd22fd67951095420e",
      "node": "202.wake",
      "snapshot_digest": "e50d83909eefd17c6014122299162a63a8e1d9412cdaf433276975da05084c49",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-24T01:06:49.488965+00:00",
      "head": "537cb8b1e60836fbd98e7dce5bc2b767e888f5df10a25cab81d0f155c83eba59",
      "node": "203.wake",
      "snapshot_digest": "5a9c69be5fa2cc2c8f45c5ba335f8a4493dbca5a28e75665f9d817cd10ed7d52",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T01:06:49.743531+00:00",
      "head": "8c2952a63312d98f514072b874c19c2a73f8f3b8e60b6a57580d5e2d7f5ed619",
      "node": "300.wake",
      "snapshot_digest": "512f331feabb9ac9fd185a28b7bb2b2925dc9b56eb446a284fd4b30b3adec731",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-24T01:06:47.503379+00:00",
      "head": "8811036be58b88e593077e7004cb902c1fa5e6775be55bc8099f28b70175cd0c",
      "node": "301.wake",
      "snapshot_digest": "7b44ae6025af999590778a4f78604229e885efc5e55e5237fe86631a2179e3d0",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T01:06:47.962456+00:00",
      "head": "71a0cafd0eb552fba396d5c8396bb5d1867769ea0d1bd76bc953dc986a9c777e",
      "node": "302.wake",
      "snapshot_digest": "d70dcd4c75d1746d1dc2d19cc2b9395e4410a9d3f4638f65cd47d5c5bafda1f4",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-24T01:06:47.599457+00:00",
      "head": "451b574fe139ed6993e0d653689ac52b3dc215014cccc194cf159ab1e54c49ca",
      "node": "303.wake",
      "snapshot_digest": "aa88c16f55666453d2af9a918e6c452d3df916850b58f38f2e074826f5870d0e",
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
