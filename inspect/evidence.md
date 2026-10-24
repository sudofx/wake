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
  "generated_at": "2026-10-24T09:53:46.161427+00:00",
  "head": "snapshot:e4350b0e67bd78a3ec146a45bf7f930094525f0641feac5aa71d333c1ced1b9a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T09:51:22.384156+00:00",
      "head": "d4c9417c9a27df1fd61538d3ea9b95e8807b03bd281f9851508e78336b01e9a7",
      "node": "100.wake",
      "snapshot_digest": "797c54743193494da48dbd2e3d45a8be6a5fb394db218d0f6410c11538cbb979",
      "version": 20
    },
    "101.wake": {
      "generated": "2026-10-24T09:50:58.058752+00:00",
      "head": "ed2cb033fd2b5f7d3024c5986bca74bf59ca58bafc700c74ceaaabc2ac2fede0",
      "node": "101.wake",
      "snapshot_digest": "7c69ba645d2d56453c7aa1e915be9e331bd4574dcd03965702d8525352610309",
      "version": 32
    },
    "102.wake": {
      "generated": "2026-10-24T09:47:01.097070+00:00",
      "head": "19f46bcade43827e473b9fb87db06b53aa3ec20a17e0b13ab918114facfa2a66",
      "node": "102.wake",
      "snapshot_digest": "217cd101d62ee2f3f54d975f879f0890159c14499d494be8c84db54b92446044",
      "version": 39
    },
    "103.wake": {
      "generated": "2026-10-24T09:37:52.589744+00:00",
      "head": "2ef0bfed904388ce6023a062c8681de28663b5076f17b57d11a437981ab60773",
      "node": "103.wake",
      "snapshot_digest": "e5e56ab9436c69a378776e949f7bcdb82f1718a65acd97afbba136b08453dad2",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-24T09:53:46.161427+00:00",
      "head": "7a8c11e400f8c5ed9afd8a8b778c2237af4bf5630fe4a17483e23fd00aebb498",
      "node": "200.wake",
      "snapshot_digest": "41992e194bb4c5382752d67f7924f2ad3d09d384c6f082a79f090faee2e915b1",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-24T09:49:44.602480+00:00",
      "head": "17ff4cd6931be310186758fa2f8f2ea4de42dd26e48a608e28262ee3a8558c01",
      "node": "201.wake",
      "snapshot_digest": "d33eb3cc1e1f4c1f383a8ed618d6d214027f56fc1e056283639a319a6fe36aaf",
      "version": 30
    },
    "202.wake": {
      "generated": "2026-10-24T09:51:09.698157+00:00",
      "head": "a8b77735539c191a2beb026c9e5ad269fa6a48ee55223b9068dce9c3776117f2",
      "node": "202.wake",
      "snapshot_digest": "3f19ec9ade014fdb79ee17c4c887c94224ac42779af74377cee5155d6afd72cb",
      "version": 40
    },
    "203.wake": {
      "generated": "2026-10-24T09:49:08.256001+00:00",
      "head": "c7decfb25a6049bbe4066da31fa291af1602700fca07177109c51e699b9c02dc",
      "node": "203.wake",
      "snapshot_digest": "07c3ca2d7b8077b6446ec95d31ddcb8252843097964912dcd8318cbc9dec05a2",
      "version": 20
    },
    "300.wake": {
      "generated": "2026-10-24T09:50:33.110566+00:00",
      "head": "dd0cd8991c9cd96a72b2493ae3f22686231c32f17a74f990befb9ded3e2e1721",
      "node": "300.wake",
      "snapshot_digest": "364dbca73b6b402d22b9582fe67c639ba0e75bac635600625e094aa1ca197de7",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T09:53:37.905603+00:00",
      "head": "349af7e01fa9f5e426d815972bf0bc03a49cec3787ccc7094b6c7b694d6b99e1",
      "node": "301.wake",
      "snapshot_digest": "d0fea0b1dda8d862de83ab76dde67265a3b20a205a7abbc673161f22456be653",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T09:48:36.403784+00:00",
      "head": "f52c43f16811dca64f7adaecebd56adfb7a6eb82eb1b5f20e619a6d447f3aaaa",
      "node": "302.wake",
      "snapshot_digest": "f8d3562da119a8f7f646aae8f4370ce6b4c2c695472f7b93df31f9d0f390951f",
      "version": 22
    },
    "303.wake": {
      "generated": "2026-10-24T09:50:44.409245+00:00",
      "head": "d583167e6115079aad8405b872bc9351b7580af17765d30aae36229d68c864d2",
      "node": "303.wake",
      "snapshot_digest": "4d6a8fd4ea18b4c9cf29942bf65bbc7bf3a54bf8fa03dd5309e5adac8e43a52d",
      "version": 41
    }
  },
  "version": 363,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d32303565333831663531643634336137.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62393332363534663131353634306563.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d707265666572656e63652d7374/6162696c6974792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
