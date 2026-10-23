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
  "generated_at": "2026-10-23T10:44:44.303440+00:00",
  "head": "snapshot:e2165c1a308e86f6ff16ad3ce0b3b02812c5eea6da344ad4997d211e81b943c0",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T10:44:19.424056+00:00",
      "head": "bf262bb90391a4c68393805be59ed1d7173ad359612bb894b26d4e3b3536d929",
      "node": "100.wake",
      "snapshot_digest": "ec4a42752564205e2327153e25b00e2329c692e77d329a77d6f78b7ecf268062",
      "version": 11
    },
    "101.wake": {
      "generated": "2026-10-23T10:36:50.296461+00:00",
      "head": "dbc0426ef1793bcf11a3bde7fe92643deebb141396c2357b2f86ea475f763889",
      "node": "101.wake",
      "snapshot_digest": "537da5aeed3926224e3df1ff1ea3c4ba521687f72c8b20bac23a604045b15a45",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T10:43:11.982916+00:00",
      "head": "5b4b1e75973a9a75c50b3355a86a0af304a3b016dca4fb8cf0a393467df1f36e",
      "node": "102.wake",
      "snapshot_digest": "dde107cd3845df0f343ebc6a062ee020817506325f8cfe2159acdd9b3be012a7",
      "version": 25
    },
    "103.wake": {
      "generated": "2026-10-23T10:44:44.303440+00:00",
      "head": "4f1f4c8980c5b83941586c5a9c9b44378a049d18cf5c8815377251dbe8539447",
      "node": "103.wake",
      "snapshot_digest": "5c2cdc844b9c42eb79cbc0fd5c465b4debea931bc200dc8b5d32252d27c08046",
      "version": 13
    },
    "200.wake": {
      "generated": "2026-10-23T10:41:52.202922+00:00",
      "head": "e0a3ab793d0b6eb80bc185f99e3c5487be6d2de1e702ba4564f92551a4642cca",
      "node": "200.wake",
      "snapshot_digest": "2a832c917a2b293e1e0370093380bb6671f937a0648836d1a2f6b64c91cd7f79",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-23T10:35:21.314274+00:00",
      "head": "ede9690d2c18de50de285ef6d9e633d6c4f7307d31e1b93d5542163eef23904d",
      "node": "201.wake",
      "snapshot_digest": "a6be23a6e104a73ebb6d6ed4494e7a714f344964267901db3ef0e7f5f8a5c7c8",
      "version": 14
    },
    "202.wake": {
      "generated": "2026-10-23T10:40:48.646002+00:00",
      "head": "3c826993cb2536d21675c46109cb7743f98a1725427fb02cbc30c10c7372c625",
      "node": "202.wake",
      "snapshot_digest": "cd8e16a760faf0fdabc71b6d06a40b8c436a191aa28704f237b6d0cd52dc6747",
      "version": 24
    },
    "203.wake": {
      "generated": "2026-10-23T10:42:59.299407+00:00",
      "head": "7c8bfbee774e9f86d5655ece4ce8ee71597bfd5f4c7c73db3c610414e6f346b3",
      "node": "203.wake",
      "snapshot_digest": "d2a79d9e55929e567363edeac075d3d44ccf460ce21a80613ab1cfcc4742bf9b",
      "version": 11
    },
    "300.wake": {
      "generated": "2026-10-23T10:44:31.795990+00:00",
      "head": "ccc887a87d0bbe1f1d07fffe82f52bdfd0f528848da0c686431a6d15a1023323",
      "node": "300.wake",
      "snapshot_digest": "490d2d45b9f9a851a580e045e621a39c0c8b05bfa2909bf32b62883c0f0125c2",
      "version": 12
    },
    "301.wake": {
      "generated": "2026-10-23T10:41:45.942039+00:00",
      "head": "1ae6c00d73aea88c30a86e002dd6b89a5bd0879cabff0df20b65563e6d68d518",
      "node": "301.wake",
      "snapshot_digest": "9d9d3d253c976ed8c5688ea18b70471321802acc5642acd09e2cb5c991072486",
      "version": 20
    },
    "302.wake": {
      "generated": "2026-10-23T10:40:42.374597+00:00",
      "head": "6f3e7a4ffa28622987d89f582856aaecd1a50b5a28181fc1fd5efbb4d2c033a6",
      "node": "302.wake",
      "snapshot_digest": "3995bf382ae934b13de1178d97d926c4e05978ebb13688943ae57ff693eeeafb",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T10:34:30.832027+00:00",
      "head": "9ef0325ddde12e46a56c8194e8341470f4d489f6b4e5aacaef390f2af6c217ea",
      "node": "303.wake",
      "snapshot_digest": "f710f91b625b28c3765e522eee6adc9f0f75d2168f7954b213e1240f076e6131",
      "version": 22
    }
  },
  "version": 196,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d343535376131346234383061343861/65.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d646339323239383831373066343133/34.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
