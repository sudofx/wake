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
  "generated_at": "2026-10-28T23:40:05.074913+00:00",
  "head": "snapshot:1e83ae991d589ebc72b0968f66eb5096c9faf20726619e343fa45a2845c20b26",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T23:37:43.903121+00:00",
      "head": "7872df22779a70a655a95b485c017646f12685891400bd350ef3a31f178aa819",
      "node": "100.wake",
      "snapshot_digest": "a0e5ac9e6c522ff903bca2c5de0cd4c419273fe93f33bcf2d3bf6102df578137",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T23:33:44.190364+00:00",
      "head": "9bc73072398426d53e3de470fe4fd185b0e056a767bdee40ff34b2eb8049e86a",
      "node": "101.wake",
      "snapshot_digest": "5bed582b043732cf5a8494362e6c130164e23c5dd272ed7ecf3e347cee8c8da2",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T23:34:44.226105+00:00",
      "head": "609d65cec147e8073f4ecb571b58e72efcbcfae20244a4ce91b1959efbd5d1f9",
      "node": "102.wake",
      "snapshot_digest": "e1c0f3c5a93b06a6d7dedb3deeb217c6444d431dea2dfa679beb3b5b57321a2d",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T23:37:05.828687+00:00",
      "head": "51ee94546f08cdf2b778bc371ff8bbbf0a877450b77592d348ff40d2d41d7d6f",
      "node": "103.wake",
      "snapshot_digest": "8786daf86def2a176cef0530ec2c31daad14646647da0f7b5b6b3fbdead821fc",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T23:37:02.409588+00:00",
      "head": "eaf5fc2d1f7c82e74f3c13b3de9c446d72e8330ba615822fcf8fc142732dc1cd",
      "node": "200.wake",
      "snapshot_digest": "9db2a84eb05d78c68de899c8919f2038d27a42539bd83bdc1fb31adca5eb9016",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T23:38:18.578590+00:00",
      "head": "181de2209548d8e524ee897d8527ceff4c6142bac7f86b5b279d23090bb59740",
      "node": "201.wake",
      "snapshot_digest": "89fa94835763d46e00b2189a6b2a7da9c0c11b928f0783c12f7b5933a03e4cf7",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T23:35:35.317788+00:00",
      "head": "6d953dcf60a146f244ea60b29ae51b1a6fa1330c1bfbea65df9d3cd02d77d479",
      "node": "202.wake",
      "snapshot_digest": "df1954473367c1e5cbf6d6670e5235b63853b6ee6a764db9d2431cbd82a58d7d",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T23:32:27.824349+00:00",
      "head": "5c7f8d218d04d0402eceea194b1953c5d9e5c8c3ccc48d756d2a5234356edf4d",
      "node": "203.wake",
      "snapshot_digest": "a229f17283de98dc22e367e560b99746a29a3b10917c1e1e0609381753f26d1c",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T23:34:56.148189+00:00",
      "head": "2aceabb00a24d7fc0dd6b5c029e5b83298d27e35019ea329c7a58ffa07f1bd55",
      "node": "300.wake",
      "snapshot_digest": "8e9931f91084ce64590774f4d3ec7808e8fed4ccc70650371aa3f705d891f315",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T23:40:05.074913+00:00",
      "head": "4314a10c9b291c899518cc432dd2f5c7e3024ba124160a8b0dfff0e8106e688e",
      "node": "301.wake",
      "snapshot_digest": "e2a5444b010b7842fc2a9b4f000de8585c6645b4bb8a16b9f90c8f9c7a095eda",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T23:39:11.834706+00:00",
      "head": "da020b2f55e20fd73752608694b45ff36805b66157f50a2a87e839974df19301",
      "node": "302.wake",
      "snapshot_digest": "d19b72da239de8bba4cb5eea1cb6295993fc95596d8526819d0811fc5ba2229c",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T23:34:33.405990+00:00",
      "head": "697033b8dd0f4b2be7bdee62992608e423c995e67330863ca8b4f74fe8d8bab3",
      "node": "303.wake",
      "snapshot_digest": "c42ec2744d3b16a019c990638aac772bcc8f52459905d30cd23d5f9bac82a489",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62303835376262636565653234666136.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d36386632666337646639313734346633.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
