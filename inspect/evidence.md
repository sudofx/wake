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
  "generated_at": "2026-10-24T16:04:45.687353+00:00",
  "head": "snapshot:01ed005a4c30e6afa13fe37e3c65d5bb927fd9f08eb5f3c8714b1d601a82824a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T15:47:30.443172+00:00",
      "head": "02b7875333a06086267f8a9ce0cefb02277cd2a0ebea27444139f111d1dc60ac",
      "node": "100.wake",
      "snapshot_digest": "411b8ca182beef0ab6e36722c5bca310c724f31f717b00095294d71ffc748f60",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-24T16:03:24.889404+00:00",
      "head": "2e3de8f825586132fedf94a946370b5229b21ec8b546378a60887562a047cd62",
      "node": "101.wake",
      "snapshot_digest": "05ed5f74118a907bdb58e900596f11feb7681271d9e0bb9a0277853bc29c1758",
      "version": 37
    },
    "102.wake": {
      "generated": "2026-10-24T16:01:16.826454+00:00",
      "head": "9400ce5b0c215b42d9da41c1f85cb4dfbc305e6a1f5fafe96fb2daa563ee3509",
      "node": "102.wake",
      "snapshot_digest": "591f8f9bcccb305413adeb4670959af14a3cf567245b7e27902c023367889579",
      "version": 46
    },
    "103.wake": {
      "generated": "2026-10-24T16:04:45.687353+00:00",
      "head": "a334dab9ce2cd573ce2784443c3139961e244281022e8731340055f0ab800c46",
      "node": "103.wake",
      "snapshot_digest": "c99f9daa7510bc1945905a96b36ffc414ed52c5ee74651346d834d16b893ca97",
      "version": 34
    },
    "200.wake": {
      "generated": "2026-10-24T15:46:34.315733+00:00",
      "head": "0b84c008fb82e353bc11b45a7aa22df6c6140bfef30e34bd10c364c457f5e44d",
      "node": "200.wake",
      "snapshot_digest": "36b11259ae446dbd668e19d92c2c81be58e5938da6a639e9edf365abb774a0dc",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-24T16:02:31.128473+00:00",
      "head": "44ff04a47ca0fef51bad5a5adbac45d6dabd83183e74e9d9c2ac71680ddc8d30",
      "node": "201.wake",
      "snapshot_digest": "d7804221d57c2e0bb855d5ca663d7630c9defe3192b783d1abb8877e9f28d783",
      "version": 34
    },
    "202.wake": {
      "generated": "2026-10-24T16:04:06.778205+00:00",
      "head": "e20380e09c85233bffeaaf4337eee0eef1923fdc91a729dc712ad5dcb47dff3d",
      "node": "202.wake",
      "snapshot_digest": "f5549f9c57d4e9100fa81c55f368bfc829edc1bcf9f807c806c9d593f2c9113a",
      "version": 44
    },
    "203.wake": {
      "generated": "2026-10-24T16:04:15.230152+00:00",
      "head": "01af1a3cc34a9d40d45d598b186b827cb9e4c50db59a17121d91acfc2109629d",
      "node": "203.wake",
      "snapshot_digest": "f4794eb09978f7e78bf1eec900442bb79e06e8e6a1d35e433d70c09707afda64",
      "version": 25
    },
    "300.wake": {
      "generated": "2026-10-24T16:04:37.707291+00:00",
      "head": "88b091a68fce9bebfd8c61c6647f5bd7de6d615b12bdc7011a6305c15df55b0a",
      "node": "300.wake",
      "snapshot_digest": "1a64a2927dd1f196a1dd20fb543e96255e8bb3c5c815a6a8bd3a32be3160f5e0",
      "version": 28
    },
    "301.wake": {
      "generated": "2026-10-24T16:01:26.047281+00:00",
      "head": "277bd0afdd8b1aa8b46e91e41c31ea5f20c7f3571fa35f3c78865b041e96fdba",
      "node": "301.wake",
      "snapshot_digest": "da0354a43595c84a59f00320b0a35aaef589544bc44eb9f44b239f26d7509174",
      "version": 47
    },
    "302.wake": {
      "generated": "2026-10-24T15:45:47.488936+00:00",
      "head": "91dabb0db4078dbd731bc8cfae2943b4c04155fd86a060b49a79865a5ded9f81",
      "node": "302.wake",
      "snapshot_digest": "8a91b7bf9e073dbe845f2b2b00ed0326659f4a31e284e8f0db79210271542e76",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-24T16:02:47.780674+00:00",
      "head": "7d32ba5b86db2c05dd1b803f402ae0be925069fa4302040f1fdb41b7a6ab85be",
      "node": "303.wake",
      "snapshot_digest": "e032c03eeb6615feb00f965c996144185b97f472325e0a54ab8b0360256559e5",
      "version": 44
    }
  },
  "version": 414,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d66393935653835643461363034323566.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d61356539653362303666316134623437.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6f626a6563746976652d646973636f76657279/2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
