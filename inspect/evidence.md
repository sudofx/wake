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
  "generated_at": "2026-10-27T14:26:39.831240+00:00",
  "head": "snapshot:1a1d7f906b7cd55536e66b71745a75e533471e34e5e7384124421c49f3f45565",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T14:26:25.834988+00:00",
      "head": "43d7ff8f331f95c45dadf47c502da044445efa24d9ad6bae7567f0a7bda89454",
      "node": "100.wake",
      "snapshot_digest": "3f1bbbb41752a3284485a13c16fa85fa74998097a42fe9bb2dd0aa910fce09b5",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T14:26:39.831240+00:00",
      "head": "09bfb701caa9f02a839659574ae837b82b477dc9670bbac7db0dd0aec3570d6e",
      "node": "101.wake",
      "snapshot_digest": "8f34df70c218c0c8e470632f3987e134044e3d7e7d1b51c376a39f25913fb9a7",
      "version": 7
    },
    "102.wake": {
      "generated": "2026-10-27T14:26:31.752794+00:00",
      "head": "849afdee513a6a8f11ca81507ff68340ca00abe49e332a9401445897883cc9d5",
      "node": "102.wake",
      "snapshot_digest": "9fcd9c0cce83e135a33a42a121f65ab0d6621c4db1c6af7ee56b428df175b655",
      "version": 5
    },
    "103.wake": {
      "generated": "2026-10-27T14:25:21.713978+00:00",
      "head": "b60876f2dc14d980bbfb9d51836d74d5a66844003587ce57e27177aa79cbc91c",
      "node": "103.wake",
      "snapshot_digest": "18f414062c4a654564c3bcd4652b38b634d4218ff08738dea4321a49e69b379d",
      "version": 15
    },
    "200.wake": {
      "generated": "2026-10-27T14:25:46.397339+00:00",
      "head": "f8fafc906fd78803ef9243bf4b550d55c366f1cab6c2193122f9dd8ab5212cb6",
      "node": "200.wake",
      "snapshot_digest": "d119325500b8685fe80de639d065334480d349c1b56fe9de90c89506c12f9d74",
      "version": 12
    },
    "201.wake": {
      "generated": "2026-10-27T14:26:14.177713+00:00",
      "head": "5438a132db45471207fc9e547a5312413acfdb2e480e7e23dbdf4b3ab78df69a",
      "node": "201.wake",
      "snapshot_digest": "3e355305b02db0ec870307fd5f9c7a09a462a176ba7cf0aacedee11da6a7143a",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T14:25:56.385499+00:00",
      "head": "3ae80c03ccbcb0f949d785e37c9199845b8483a5a6295a3b87aeb062efbe57c7",
      "node": "202.wake",
      "snapshot_digest": "3b464bcc68abfbe3a1714720e030611ccb19daab66857071f008aaf8b4ee6594",
      "version": 11
    },
    "203.wake": {
      "generated": "2026-10-27T14:26:26.332679+00:00",
      "head": "ac7e6b13f53b9396f4d782d3b424a2a922c74da116ad7b3791697ce2b3ef9a24",
      "node": "203.wake",
      "snapshot_digest": "aa304826dcd5aa73fdc4fb9bf85ec1ee282aed049507b2724321fe7b44df74ec",
      "version": 14
    },
    "300.wake": {
      "generated": "2026-10-27T14:25:07.559531+00:00",
      "head": "e154bccd180996096e547facaad4d81d33498d4e5a346336e29af055d4a7303b",
      "node": "300.wake",
      "snapshot_digest": "fc9482f61a15719673bda9d14ec3bb9dfcfb8de0932db3b3326f793dcfd1e10c",
      "version": 13
    },
    "301.wake": {
      "generated": "2026-10-27T14:25:12.535589+00:00",
      "head": "aa5225843c1625ea0d400c729d11b16988cdb0ceb6bc3bace10f8b7e03c5e75a",
      "node": "301.wake",
      "snapshot_digest": "7de1266e49322437f6722070281cb01f20a12f56d062f7b64fc682dc800103d1",
      "version": 7
    },
    "302.wake": {
      "generated": "2026-10-27T14:26:31.113784+00:00",
      "head": "bee8304c932e2e7beaf1818d69a8a38f0a698256d6ecde7f84ca2cbff2a6f186",
      "node": "302.wake",
      "snapshot_digest": "fba525cfd0873623446e1afccf98e9b5e15f5763255253009c45c3d42ac88000",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T14:26:34.273174+00:00",
      "head": "0cb6c2a493c58853321fb34730d04c2848f487dc4ceea8aa24c31e774b48213a",
      "node": "303.wake",
      "snapshot_digest": "469d1de3f38544c1651e15121073edbe1f458fb6c14885db0bd59dd3e08adccd",
      "version": 11
    }
  },
  "version": 124,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d33.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d393430626139396266616536343139/63.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d623865333664636261626363343434/37.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d636f6e74696e756974792d7072/6f762d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
