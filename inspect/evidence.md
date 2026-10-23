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
  "generated_at": "2026-10-23T03:53:55.609465+00:00",
  "head": "snapshot:26fbe0420f05f51f44f09551c3a604acc9ebd3300ab33069b055afe043661644",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T03:53:54.289522+00:00",
      "head": "0e55017388c316d6f3432fc13a5c4181c82084d88a5213ab2007e923aeb2797e",
      "node": "100.wake",
      "snapshot_digest": "91ef0570cd1bae8bafab276908039d341cb596d0a469424a82d9d25bb0ae7d52",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T03:53:55.233334+00:00",
      "head": "e5acc7fbc212f8cdd82535973da4b1439df73143123e571660b1d1ab6bee47f3",
      "node": "101.wake",
      "snapshot_digest": "36aa179075737504e6953d579cf93aa64fcb8160234296e926652afa29981d21",
      "version": 15
    },
    "102.wake": {
      "generated": "2026-10-23T03:53:54.164232+00:00",
      "head": "6d6d3b97ad8114042fd9411dc37c89f10b0f08f93e666520172efac0970d1696",
      "node": "102.wake",
      "snapshot_digest": "b9b53b2b34be5adf10431078ecf71a93cab93175bdc5a1ced1d2b5ddf7be5eeb",
      "version": 14
    },
    "103.wake": {
      "generated": "2026-10-23T03:53:55.448476+00:00",
      "head": "f6d5c1d0278d040bb24836f48cab46770f03bc4bc68ee8e14861c4e7395730e2",
      "node": "103.wake",
      "snapshot_digest": "daebe4396487d69fa0c3a1ef3cefc3d451f58b25217bc8fc95541d2696cdb106",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-10-23T03:53:54.809094+00:00",
      "head": "e8a6ea5af19043ae5b600026fa2fb55fb12801a3367a500c91d54153885d4837",
      "node": "200.wake",
      "snapshot_digest": "2866c831511ebc46747051780ad665eb64a5ac103cf95d403b37ef3aa6ef1a20",
      "version": 8
    },
    "201.wake": {
      "generated": "2026-10-23T03:53:54.620636+00:00",
      "head": "8d5ffd66859df9ae4ea9e5e7a282af3c367c073c00ef9f04ab2d0e314205cfa0",
      "node": "201.wake",
      "snapshot_digest": "e308e2f9923099b4731179577d3f62400ac75c036ca7462a8a4f8e2749660c67",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T03:53:54.064406+00:00",
      "head": "4c6574dd132820453f0a564f773144559eb69360d4eb1562f95d461007aab9e8",
      "node": "202.wake",
      "snapshot_digest": "f4cd0c2b3c532c13f0978741a2267ab47e5db20b39bcdc240e1318fedd0b7ff2",
      "version": 15
    },
    "203.wake": {
      "generated": "2026-10-23T03:53:55.609465+00:00",
      "head": "74eea087e15ce8982e425ae15646db03929286dc1356ee7d6038efb253cfc5a0",
      "node": "203.wake",
      "snapshot_digest": "6e446b2b035a10e72ddc09b681ada277c4c29322fa6f333bffb84a26a0c3c150",
      "version": 8
    },
    "300.wake": {
      "generated": "2026-10-23T03:53:54.580370+00:00",
      "head": "5b6003c4ea3491aad3412ed861115319cf0383f7a995b064cec112a98f8d6fde",
      "node": "300.wake",
      "snapshot_digest": "2fa1bfe49e930d22ed5d08e9549e375c3aa6e1b9fe245973b8e04903f31cf29a",
      "version": 6
    },
    "301.wake": {
      "generated": "2026-10-23T03:53:55.044497+00:00",
      "head": "0ea8ca902766465bf32d8c25012c8a3e60ba745264306fecea48abecac23d150",
      "node": "301.wake",
      "snapshot_digest": "5a0b3f0f29fc2917bee4708ea3c363e8bcee748dbebcf0d92ec40899a7d1c4bb",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-23T03:53:54.779372+00:00",
      "head": "958df55cfeb6ad97cd8cca6c033a82abb0cf4b11daf0281f6160c8b6186f40ce",
      "node": "302.wake",
      "snapshot_digest": "d69344ac013affcd03341ee578241eda19e15f3b75fc0bba095bceb3a4f64d64",
      "version": 8
    },
    "303.wake": {
      "generated": "2026-10-23T03:53:54.965196+00:00",
      "head": "4d75ea3d5dfd22e0187935cac1227930a3726aad28eeb1113dcaf13f36e0b1f4",
      "node": "303.wake",
      "snapshot_digest": "032da435c0b2d5105f7edd6bae26fde391b5d99cf01eb2d9268e2bddb197c1df",
      "version": 19
    }
  },
  "version": 129,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d343461616562303933616637343462/63.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d626633356466303832326637346131/30.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
