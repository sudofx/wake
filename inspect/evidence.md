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
  "generated_at": "2026-10-23T11:47:41.182006+00:00",
  "head": "snapshot:594a0c03193f5e550bd859c8f9ac01e7c8f6486b5e5d11cbde966c7cc53b3024",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T11:33:08.651884+00:00",
      "head": "15739c52e677ffeb11781f6a7bf4b3150cb9dbfa17a1f0afc4a818da8c76b953",
      "node": "100.wake",
      "snapshot_digest": "7deb16fbf57a28fa10581ff0776c160ea1811d7cc13686ed8ff4d69937711af5",
      "version": 12
    },
    "101.wake": {
      "generated": "2026-10-23T11:40:50.257979+00:00",
      "head": "2d5bc165663a88059997975e36f69a212fa619f3ecef05fc4106d73c06b06b1e",
      "node": "101.wake",
      "snapshot_digest": "8ececed73e08b21edb8dc500f024610ec8c36b6a41392f2554c901d89bb28899",
      "version": 19
    },
    "102.wake": {
      "generated": "2026-10-23T11:31:24.722929+00:00",
      "head": "865987593d5d9b4e249680a6c9391e753c514a668b9b5886d1176a590b90b88d",
      "node": "102.wake",
      "snapshot_digest": "26f3268e4022a65ed81886fe4de16c2860d4a4b5d791d93d6ab3aabc9fb848ac",
      "version": 25
    },
    "103.wake": {
      "generated": "2026-10-23T11:46:16.080655+00:00",
      "head": "04142d7b94d8d84f8d24ee0468733f6ddb1b0d7f2d58af27f5e6fde3ff7b7127",
      "node": "103.wake",
      "snapshot_digest": "d1e0d0ed252a7a636dfbef717079fb9d2d86ed4f29e8c92a44dc27f8e0828d23",
      "version": 14
    },
    "200.wake": {
      "generated": "2026-10-23T11:43:40.844192+00:00",
      "head": "b0357eb3983895c51c06ab5384cd424eb847490372bf0933a521ce0143c820b6",
      "node": "200.wake",
      "snapshot_digest": "cb570d243fd33723fcded2b2f3b0a78c33a64b8920ab82c75d83f658705fa558",
      "version": 15
    },
    "201.wake": {
      "generated": "2026-10-23T11:47:41.182006+00:00",
      "head": "4970511f5fffa700dd770cce014c7a8599e093fffe5425174bfcd496e90eb7b3",
      "node": "201.wake",
      "snapshot_digest": "d2bf91cb46d28a2f263a858ee46faeb81943304348755cb76a7fc6f8d129480d",
      "version": 17
    },
    "202.wake": {
      "generated": "2026-10-23T11:36:16.393628+00:00",
      "head": "9d22885de7c6728da39b902d6b49f8e793b074a22df9dc3f7afa9db85df951c6",
      "node": "202.wake",
      "snapshot_digest": "4b96cb411d6d7753f52653809e6ebdb63fae7c6a850e88acab1c06c1565ac9d1",
      "version": 26
    },
    "203.wake": {
      "generated": "2026-10-23T11:44:16.225246+00:00",
      "head": "2fef0c1762678ebbc2d64dba191e719042673c5100e835e503fd7bbc28a1cd50",
      "node": "203.wake",
      "snapshot_digest": "ef8e46255b4cd84f42862986bb3413f1a0b225868a64ea2b40ddf43045f25507",
      "version": 11
    },
    "300.wake": {
      "generated": "2026-10-23T11:45:10.798835+00:00",
      "head": "3514c9a29029906808d6b7ca5e8c426445c6ac6dfa7a2b9edc6646045de2f6c1",
      "node": "300.wake",
      "snapshot_digest": "8e03c2a8f27ddff450eb9b85c820a22511bace94cb17553fce0cbe0ad4e64adc",
      "version": 13
    },
    "301.wake": {
      "generated": "2026-10-23T11:37:39.358285+00:00",
      "head": "36bdcc9b7a2c7ffada78c6814dbe90c8c7fa11131e7c67b322b5948b33d5c1b9",
      "node": "301.wake",
      "snapshot_digest": "2df9d0b68cc0e92dee9b1d2cccebfca68bd57306b3e6f43c58fd395400c6bc0f",
      "version": 23
    },
    "302.wake": {
      "generated": "2026-10-23T11:37:25.431902+00:00",
      "head": "848c4cd7bf1337b9fc4547a46cb8e473c7e5719072c314ac59b1a8009640df2a",
      "node": "302.wake",
      "snapshot_digest": "230f484dc8b2c5a422b1712347e946b3482fa8a8b27e231f174f3d19f73b124a",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T11:47:03.156545+00:00",
      "head": "61396985491ff487274e2daf7717387ec5fd385c36175be16bc6a5592e5dabbb",
      "node": "303.wake",
      "snapshot_digest": "1d9c818ed23172e6b923e027a9e4ca5a302fd89c16ed9cafa2dc33e6c7d8deb4",
      "version": 22
    }
  },
  "version": 209,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d633561656334613761313766343230/39.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d666330643532323465303136343031/61.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
