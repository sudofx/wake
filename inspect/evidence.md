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
  "generated_at": "2026-10-24T09:17:43.375574+00:00",
  "head": "snapshot:1d6a342cea3a11deae10298b7658490179e91dabc038adb2be656665070f9e76",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T09:17:11.577455+00:00",
      "head": "f6701dcffb865a8f5fc084c8147ea11eba5be86531b7f4d7206c4b8b097d1ee7",
      "node": "100.wake",
      "snapshot_digest": "716436375c8425596992a5fc051f705d0e0020b70f92e7d5f83c4f1cd5b334a8",
      "version": 20
    },
    "101.wake": {
      "generated": "2026-10-24T09:11:32.528343+00:00",
      "head": "b27acfef906b58c4b8ae929c3e74bf07302047279836151a23621f6eed02597d",
      "node": "101.wake",
      "snapshot_digest": "ae59fdf55bef469ca2cc55445c8ed1ad9d4fe6887f6354b7d92812886182395b",
      "version": 32
    },
    "102.wake": {
      "generated": "2026-10-24T09:11:39.906228+00:00",
      "head": "bf40e8c9558ba738647c3bbe46a72326ad7ea01ac1bacdb7f78bc727f7abe4bb",
      "node": "102.wake",
      "snapshot_digest": "d3075a9df17747a4d568aac931c957dc1e184742deafad1a38fcffd18c970d2a",
      "version": 38
    },
    "103.wake": {
      "generated": "2026-10-24T09:16:22.660086+00:00",
      "head": "fd91d97d2523166e598101b7a34a7158026ce6618ed671227a3594306f8e5c98",
      "node": "103.wake",
      "snapshot_digest": "7ba59d4a31c65890148bdd5099e0cca3e5a325450f5669fc3200a971495e1da1",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-24T09:16:39.243128+00:00",
      "head": "c72968e6dba918def1f8710c9dceccd2db9d903c3c2ab4d44b0a710c12f52b9c",
      "node": "200.wake",
      "snapshot_digest": "48b8175b7cb624cb63c6340b5e6b8b3c9cc87d5eea4dff23cec1fb1f51f13dff",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T09:05:16.307283+00:00",
      "head": "49bb9b565831e4375c3f388b39ad8f9ddd335e9da1755d14293f272b7e39c237",
      "node": "201.wake",
      "snapshot_digest": "42684178d803f424b7981c11730192f8491aa162279e5a9ab23a4582d10183e5",
      "version": 29
    },
    "202.wake": {
      "generated": "2026-10-24T09:14:58.905708+00:00",
      "head": "98c308ae28686fcf85c25906e1bc124d1aed3c6a95555e8f93b1c27cd5f96b15",
      "node": "202.wake",
      "snapshot_digest": "07124a37f03707340025a15e32517a45c247ea1cd50ff8c9d3bf8f45ad599f6e",
      "version": 39
    },
    "203.wake": {
      "generated": "2026-10-24T09:13:08.062885+00:00",
      "head": "2e25298f733ec55f3d5e2c61f71f2169689911ca173888b675e66e8380fef6c8",
      "node": "203.wake",
      "snapshot_digest": "927fe30c3dc8e920ae443fe914958c5eb1860182aae9dc109a2b6a5ead4c45b9",
      "version": 20
    },
    "300.wake": {
      "generated": "2026-10-24T09:17:43.375574+00:00",
      "head": "fdee6d34b1ca138d20f8375a2d0f7f0cc8109d7339694e27022e2af955a1e91c",
      "node": "300.wake",
      "snapshot_digest": "fb75a0b823f77af54e9b628138b8e7e8add4e300646c54c0241556f854c82cbd",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T09:10:25.329621+00:00",
      "head": "e4decb17250d47e4ea48fc6f5e38a7048cdba36367c544d68c68b57e7055b580",
      "node": "301.wake",
      "snapshot_digest": "39c9c4f481c65ff06d0d1801b2831d74fb7cfe959029f03f73aa86514754877e",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T09:08:55.867212+00:00",
      "head": "5daf5983a9a5ac5f3c3ccd52bc2f97268aee0c9acae8c69eef46c894e5fc1109",
      "node": "302.wake",
      "snapshot_digest": "c52510c8c657f24271f7271891e99684e02229f435fd691f93743d31e36b56d0",
      "version": 22
    },
    "303.wake": {
      "generated": "2026-10-24T09:15:09.385413+00:00",
      "head": "6d31709b57eaffa412fff1dd0a7d86ee9aa3a2c556a81ff021576e6459bc65f7",
      "node": "303.wake",
      "snapshot_digest": "ea7953c22de1550b0e3f644caff2dc35b24bed9385c6d203eb1f18ed108d5a57",
      "version": 40
    }
  },
  "version": 358,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d39303366613061376262323634383066.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d653032303762643461303063343631/35.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d707265666572656e63652d7374/6162696c6974792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
