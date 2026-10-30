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
  "generated_at": "2026-10-30T16:05:03.408144+00:00",
  "head": "snapshot:2a80250852154de326696253bb281a31693b87a68526ec4365ea47feeaee2cab",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T16:01:44.221535+00:00",
      "head": "5fbdd478c0ed8a1b556a3bb6cc063022b488f70d89e8ec21257ac20b8f4c0445",
      "node": "100.wake",
      "snapshot_digest": "0a9d46b4b17e215aacc306ffaa0eed2808bbad03cf138a7bf4c0e31ca4d0d7fe",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T15:00:53.528380+00:00",
      "head": "89cf73447b618864e13db80d5f9829afa4d6f52bcb04f0d180310d1d8b39dbcd",
      "node": "101.wake",
      "snapshot_digest": "253f67ccfa209f64f9a4c4e9725f02a7d484ead2253fdcee2610a87983c28cda",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T15:00:51.272704+00:00",
      "head": "520e219cea1e6086617026c6d5af8c853518d0f0d01edbc35855ac1cadf4271c",
      "node": "102.wake",
      "snapshot_digest": "d0b9871ecfd160e9a25a9572ae03c570c150ac80f799144deaba36797c2075f9",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T15:01:02.266917+00:00",
      "head": "e1d77366b6375b11e1902d8271be6e2ccf0ea7b92e9728e3c99b6905b34474ed",
      "node": "103.wake",
      "snapshot_digest": "1b5ca431d3f9e134a6bc5a63f63f4a496e21b9dc53288b2315d14f71ff20ca70",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T15:01:03.358767+00:00",
      "head": "0c528bf25a2f725db1e4a34c5d4cbae75a00139e6af7591bd6a5c5e17d242cdf",
      "node": "200.wake",
      "snapshot_digest": "cc889d76911c855956cc1b65135d3e3c23af80c29c76d4cf3c7c1fbc2ffa82b3",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T16:00:02.065732+00:00",
      "head": "6bba107dae80b7302b871eaca4d1e8fbbb6c353b0761d967124ca32fe11369ff",
      "node": "201.wake",
      "snapshot_digest": "45268b85784c13570766d34c809784231a97977e1d505681244efa49f82f7629",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T15:00:55.758276+00:00",
      "head": "1b5b27ab4ea93f2479ed1bc0e6ef4f675c940f7e36dfcecee6fb4b655854fd8e",
      "node": "202.wake",
      "snapshot_digest": "79db5b502d709156db1b271cca773b2690a20b1c8385935c20eb3cc96e43e679",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T15:00:54.042360+00:00",
      "head": "596f2c8dfc29e52b30b00f5bc47005fda1d8b92a2485d79dba108f1a044eeca4",
      "node": "203.wake",
      "snapshot_digest": "9976ac451970eed713293a46addb77aabf69a65b1119162ed5dd34156863d7c0",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T15:01:06.058858+00:00",
      "head": "5ec943f4e4874db22dd0f264fc19abde887d684351fcf29ccb9cf72f9ee5bec3",
      "node": "300.wake",
      "snapshot_digest": "8c4402f033b32736e5445879887e7044a043db8f1dfb4872e901feaaad5bfdf5",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T16:03:20.753473+00:00",
      "head": "94b9df9e815f7829bc9daed81dbfe9053e1f31c59673348fe467d3d014b7de46",
      "node": "301.wake",
      "snapshot_digest": "1c6e98d49d932a833fe0c9f68506372ffd681f9b75a2b54f23476587b12e79e4",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T16:05:03.408144+00:00",
      "head": "4d5942e72da1ebd27add92782f2a79efe65f486b7663846ebf1019c92fce3149",
      "node": "302.wake",
      "snapshot_digest": "f6b6326b4ce7564436c60199f68a8c336521b946af4c629fb9bea9270cdc3149",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T15:00:57.323285+00:00",
      "head": "1144a106521ddf2356c619c88998ccb8b3e0a39b7ad681c48f8576e72ab2fa63",
      "node": "303.wake",
      "snapshot_digest": "0f82f5cc43485274e3f7151b0faaac783c228591efd8322a38e1c0b11b54d9f2",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d37353130633165303066616234396637.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d36343865633165363461653934643565.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
