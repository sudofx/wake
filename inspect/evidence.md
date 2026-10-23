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
  "generated_at": "2026-10-23T10:10:59.341053+00:00",
  "head": "snapshot:f1893876e961261494a6ef4d862651f7e3d642accba76d60f96b652d55c348b8",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T10:10:21.730496+00:00",
      "head": "9497be7483a8a99a05fa01db22ade6610de50f67e37e7710b6876b905e493a6b",
      "node": "100.wake",
      "snapshot_digest": "f174e8cd007d77c23de204b407f6953b699c29d913f24082e4c133689a5bc544",
      "version": 9
    },
    "101.wake": {
      "generated": "2026-10-23T10:09:51.517456+00:00",
      "head": "2885730e78bcdb97de4ebeeba747c745be24775466c8fb2ba065a8605165cf88",
      "node": "101.wake",
      "snapshot_digest": "c45fcd1ec597e2ef537b5865721d850c3f15d6d7d741929dc917d6c0726255a6",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T10:09:31.672527+00:00",
      "head": "c977e146119c7070723b9042d55c36ddbff8fd2758a44679df80c7ba9e8d80e7",
      "node": "102.wake",
      "snapshot_digest": "5a126e4768dce863b808bd663790b676541c756238a521fe345ecc8d6a2bfacf",
      "version": 23
    },
    "103.wake": {
      "generated": "2026-10-23T10:10:59.341053+00:00",
      "head": "a0064e8dae04cae79c160d70b726629c5d4e2f5d2d7e10c0d5a55c02b43f9fc7",
      "node": "103.wake",
      "snapshot_digest": "55a034027abac894fe334228caf7167ee48cf522f56d6be0f3170e12bd02006c",
      "version": 13
    },
    "200.wake": {
      "generated": "2026-10-23T10:09:21.003134+00:00",
      "head": "bc8f79e19bd8ed17fc09ad4f075e29da333abf0c11f91591bb360c7cf26946ee",
      "node": "200.wake",
      "snapshot_digest": "647774f3be0bbf4895e2f1750ac7f02dc216e4974df785aff39849bedf631092",
      "version": 13
    },
    "201.wake": {
      "generated": "2026-10-23T10:10:32.623473+00:00",
      "head": "651fd8cd3448fdb42fe206c6b8b24d2af273a42d90b50eabf6473e647e0408e1",
      "node": "201.wake",
      "snapshot_digest": "0dab01f8ba92a98fb62a0c213b8ae8261a8578655d111e330ee7fb4640c572e8",
      "version": 14
    },
    "202.wake": {
      "generated": "2026-10-23T10:08:24.964154+00:00",
      "head": "b26d35abfa3e601333ddd2f315702da048869cd1bbf08824a856876540afca08",
      "node": "202.wake",
      "snapshot_digest": "3c38c238dca71d20fbb3c3c431433c0644b13a64e0af1cdc85d5b7b08b6dff12",
      "version": 23
    },
    "203.wake": {
      "generated": "2026-10-23T10:10:06.542613+00:00",
      "head": "6cae46b0dc5c2306c04e8ad6427862e6b92be6754e4df870f664df2895bbc068",
      "node": "203.wake",
      "snapshot_digest": "c843b0fd4010796e411f2082633d5e30eb0af173f7e4cab2deb7ae6cf4b29455",
      "version": 11
    },
    "300.wake": {
      "generated": "2026-10-23T10:08:00.001556+00:00",
      "head": "17a75cb557de84ed36de881e4734ba9df92ee834eebbaaecabf3b69616aec285",
      "node": "300.wake",
      "snapshot_digest": "429ff6130a4858ad78bc5bdd29d685dcc9c300dacc1253ec3c198b9425e56bee",
      "version": 12
    },
    "301.wake": {
      "generated": "2026-10-23T10:09:10.514154+00:00",
      "head": "110328dbf8df084574b1b33f70e6a9c917a4b885eb465f351c37948e43e256e0",
      "node": "301.wake",
      "snapshot_digest": "58ed6975d86ec71e5ea69d41f0038cbd418b0f6fb235123c5edcfb39199aacfa",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-23T10:06:34.933674+00:00",
      "head": "1fbc320ae527ee796043619e940a0dd5ecdef592cad4b14e07932c8de841edce",
      "node": "302.wake",
      "snapshot_digest": "2516e2ce2330111939078c528fda2bb1d2da612da60aca00b78da922094d19b0",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T10:10:01.558269+00:00",
      "head": "8fb809fbc1ecc0de57fa0811e20bc6abcb22104eff1909cf2e523b9f7b5d5fb8",
      "node": "303.wake",
      "snapshot_digest": "cb1b6394583b686465d6e4f11fcc7e7b3bc6920b6d628de8e9eda75ae1920f35",
      "version": 22
    }
  },
  "version": 189,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d366366643733656533653230343165/66.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d633266363163656363353935346434/36.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
