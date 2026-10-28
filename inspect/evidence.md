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
  "generated_at": "2026-10-28T21:20:38.403009+00:00",
  "head": "snapshot:509fbaedd1aa4c3f2054e2f4017fb9eb2b1b8f556fbba2f16e51a74e6e709b12",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T21:17:47.963641+00:00",
      "head": "bdc7c6b8367e5778a5ce2ab85fdb00fa5656416b71fb97fa3e05af442ada8c0b",
      "node": "100.wake",
      "snapshot_digest": "9488a8367cae7d5a4d966fd4feb72e23fdd86aef27bfe7bdf02ec1ad6e8edcc0",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T21:15:49.121183+00:00",
      "head": "638bb189a16a4f897d6aa49b5cd8c8abb51bc50091da4aa5a9dad3c5bb509308",
      "node": "101.wake",
      "snapshot_digest": "e551d1fe5570b233d0071ba9fa132a5e4042cd5aac5491870589f0512ea245a5",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T21:16:28.467502+00:00",
      "head": "01d92c3cd51dacc310a7d7585169d182ca1ebc9cf9030d6c65f8612cbeed5957",
      "node": "102.wake",
      "snapshot_digest": "f26dc94e1dda8ebfda9f7cbb810dbc55a42e1536d37be21d3c050b18caeb8e7a",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T21:17:36.360911+00:00",
      "head": "6878804a1a9e4b310264e40a3a9b94d0e816ef31757b492af7f2168d4a9957fe",
      "node": "103.wake",
      "snapshot_digest": "ac1aea8e7adcc37683a94bb06cec5a05c09e66c0c5a20d36099261e928ad1e60",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T21:17:53.853954+00:00",
      "head": "dd5aeb642a249be74280976160bd1592bbf017b2409aeebe66b8a0b22affac18",
      "node": "200.wake",
      "snapshot_digest": "ba26b1d286617bec2ba8af214bc1d72b933eccaaed5970edcf579c40b7ef0c68",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T21:18:32.701999+00:00",
      "head": "e7f4e63ff73fc4b4f1f1a7d37ddf2bab27c167d1b0119c2e4e4e13d357db2a64",
      "node": "201.wake",
      "snapshot_digest": "bcf30ee2d345b686cbd17b1349e1a84fd35edd456477e94747ee47b82e6b64b2",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T21:17:20.310985+00:00",
      "head": "0d7982bf3dd000c9ad01b12a0a2873c600cfe43b30d381869cbc19ccecafa32c",
      "node": "202.wake",
      "snapshot_digest": "b640fb94ee8a1a867b72a4869bca17cc94960057169170b13b1bc04c0d1629db",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T21:14:57.750038+00:00",
      "head": "47a5188b5c1ffda5d703817fb92deec02f50374385c215a89716ba044e99d529",
      "node": "203.wake",
      "snapshot_digest": "1a4324d3e41464e0e41e7bdcb2563e9816613f20c8e9bafe544ceb33170bd7dc",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T21:15:44.282472+00:00",
      "head": "c46f1d6cc86542b0fcb27cf986934b8facdcfc0646033e4f68f57cd8a8f25052",
      "node": "300.wake",
      "snapshot_digest": "bc180e386abf9061bd88be477bf32dd15ad15375667f9463f518f667d66c748d",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T21:20:38.403009+00:00",
      "head": "45c93953f443ed4182d534a50921835c34519ff583602f3a7a1fb8585ee38b66",
      "node": "301.wake",
      "snapshot_digest": "80c37af5e45a6578b7a24b88c851ceee3214e36e1f9365e684db85ac3746db12",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T21:19:27.353429+00:00",
      "head": "dd353b2630743c4ccee799e23934cee9bd4589d8e0e0802291c888363e06c015",
      "node": "302.wake",
      "snapshot_digest": "81b37dbdd5ac48a05fc9bbe2da05c34833ce95420b3b3dcdcfc6d6ddf19b13ee",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T21:17:30.171416+00:00",
      "head": "b5a239414814f40ba23c5e5467892cebbf00061de2ffbf57cebac3541f5c28c7",
      "node": "303.wake",
      "snapshot_digest": "8d16c3437c9995c72b411e0538da0b0393df06c951506f6f39efc468245c40eb",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d39353335663432663063336134333135.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34646236656232333666623534393136.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
