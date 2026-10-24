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
  "generated_at": "2026-10-24T07:33:42.224716+00:00",
  "head": "snapshot:6c4322ddaf309e3de35567f3526e22750baa6804a88b5a2326fa4819cbd77e13",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T07:32:53.534739+00:00",
      "head": "d835cbcab0a8971919b25c8f9d69161e7e85cdf5263e91cecfd9b754105cee28",
      "node": "100.wake",
      "snapshot_digest": "22b29a81df1518f5f93cffec98e68ba632cd520517c2af3a7c796031472641a8",
      "version": 20
    },
    "101.wake": {
      "generated": "2026-10-24T07:33:27.967793+00:00",
      "head": "5bba958a431d75a4e01a3b5d4600cb6e0073f9c22d9d2a4f321581d5792f464c",
      "node": "101.wake",
      "snapshot_digest": "2926e52467a58479c3c97bf9283b230a5ba8675aae87ac0a1bb42d378f8c2ea4",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-24T07:29:20.801215+00:00",
      "head": "200b1b26ec4ef34843f8c233ce7e3b0f043b359ae2cacb83805d34e4c78df71c",
      "node": "102.wake",
      "snapshot_digest": "1b55c341861b216bf748b227340e7057b22501b35db84867ccd5aaf79ccf35b6",
      "version": 36
    },
    "103.wake": {
      "generated": "2026-10-24T07:32:59.425465+00:00",
      "head": "8286fd845476f5929413d5f1e3c680efc2cb6f9e59f02b7eeb48d7c912fdd599",
      "node": "103.wake",
      "snapshot_digest": "11cf2ac45f4b6dea24bbe4a880b3ad0d6bd686afa4b76080051dc12ef7cc3afa",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-24T07:32:08.738624+00:00",
      "head": "7467a1fb2c2cea94875f1d595cd24db7babd277ee5f3898f49fd2a9417387959",
      "node": "200.wake",
      "snapshot_digest": "d3a49a9a75989e144134745e5881294852dffce52ed223378617d42c453f5029",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T07:32:31.639724+00:00",
      "head": "eb3b4e4e1bffb98a33078d58e17c9efaa17c0d8711e880844296cedb6b180cbe",
      "node": "201.wake",
      "snapshot_digest": "a4edf5b7ff6daa55034f3449cfc6bb88e5f6781e80858306c625145ea89d0052",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-24T07:31:35.548444+00:00",
      "head": "70ada52fe5b65c4fa82ceaf2c0f4f21d580fdef1465c414e2516d9662319863c",
      "node": "202.wake",
      "snapshot_digest": "f0528b1e6e27af24c36983175d43838f74e22722e9c3670ec704412822e9817a",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-24T07:30:35.904863+00:00",
      "head": "b5f6372ebf60eabb1dee9f0dda72e7d746f0427a7f03e66717deab70dbb99b49",
      "node": "203.wake",
      "snapshot_digest": "a9031e0aa631771b01ab02588ded730f1ddb402a5220df842f834ca258c95a50",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T07:33:16.221526+00:00",
      "head": "0cbd10dd6b8e9d3607daf479306e8b7e5c60e10441085881f7907f7face40395",
      "node": "300.wake",
      "snapshot_digest": "52a0ff5724894efca65bb33c84ed33473fdb46182518a591c5302dcab3d3de94",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T07:33:42.224716+00:00",
      "head": "16fd39ca15d1e8e74e195846117e1c643943ffbf29b725e15975cc7ebd8d0afd",
      "node": "301.wake",
      "snapshot_digest": "371e0ffa453f347b013a80d3dd6ae203940ce5aa1128f0ce7944547723893c85",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T07:28:18.550043+00:00",
      "head": "85595f963521473d5d323fe41f152f3b73b4a9b9ca405fc792f35034b63aff55",
      "node": "302.wake",
      "snapshot_digest": "80c49666cd3ad3b4b0f23a4461d431481182147e13b117691af5e3d4bd7b38f2",
      "version": 20
    },
    "303.wake": {
      "generated": "2026-10-24T07:30:54.624775+00:00",
      "head": "9d1eabcd307801bb803746fe2fa2a95f8eef7132dbdc1d334e659e8e49253634",
      "node": "303.wake",
      "snapshot_digest": "a1f2ff2ddbb4098a13969f4ea8075d3ff99be09ecb6b7b49c2c59ef512eed521",
      "version": 37
    }
  },
  "version": 343,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a722d36383066613762346237393834613065.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62666364646265613561363134393730.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
