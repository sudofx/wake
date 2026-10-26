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
  "generated_at": "2026-10-26T22:22:05.568594+00:00",
  "head": "snapshot:2243b67c59c2ec99f5c4c20a3257bcd2377760bf27652e0bcbb9b2af4c017b0d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T22:18:59.525285+00:00",
      "head": "ebaa4a388d3bbd3f7d0674ddf7d61c634451eca545f34e7eca3829a7c0d6636a",
      "node": "100.wake",
      "snapshot_digest": "17ee846dcf255b85bea6f9200d448b1b2b420c8a8d1def9754662bdc9a1778be",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T21:56:03.999675+00:00",
      "head": "8bbb5eac1ab0df6b024296b7c99ce1405b409756251eb9f0556f8c166c1c2980",
      "node": "101.wake",
      "snapshot_digest": "a1a08fb398f271b69a12cdb6ea9b73e25f9c62219d908a9da5da8ab812521634",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T21:55:57.585230+00:00",
      "head": "e37bd58e37684bce68bbf04e1e80e039085144c9320b182096ddbdecda82d6bf",
      "node": "102.wake",
      "snapshot_digest": "00988b917174c64d69f5beaa3b3d1378a45a14e9ce493cdd8452d0bd2a3a9d99",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T22:20:25.190051+00:00",
      "head": "62aafdec468e64bf62c4bdb179d8ab06e37b47f8e3bff587922543fe1dd3d565",
      "node": "103.wake",
      "snapshot_digest": "27bedcc4d3dd240d46254e3c9a2229354e622809f60d3c07fc9444e5aae0103b",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T22:16:37.311569+00:00",
      "head": "ae2ff21a34228f3bd887bd55c807a7adefb3aaaa3476e27d38ebbec4ec23ef2e",
      "node": "200.wake",
      "snapshot_digest": "cfe025cad92bef6cf023caef5f5b76a18758732db6b6c9b3de76c97202718978",
      "version": 45
    },
    "201.wake": {
      "generated": "2026-10-26T21:56:04.237509+00:00",
      "head": "291dade813a94bdcedb12c076af02cfc1f63085eb93b2cfec41bb0a50416aaca",
      "node": "201.wake",
      "snapshot_digest": "af2ae4c5fabe1fa8e175bd2aa9fd525435ff5fed913297c280202e2ccf366256",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-26T21:56:02.157262+00:00",
      "head": "fb826fff385cd42b96ccba7ef3dddb193a082b19e01d9bf9448a0a54b2ede0fd",
      "node": "202.wake",
      "snapshot_digest": "9bd1102d9a102ab3fa43110934294b3152b7ae0242869c9f8e21d98dd2d55f8b",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T21:56:03.033250+00:00",
      "head": "9dfb14f05002fb92327c4a3bef1db87812dab2a71b77ec38c3ba4d5c214e5cab",
      "node": "203.wake",
      "snapshot_digest": "8e2462cf82a6ca410b18b2558938e1fa4c3dc682318caf886e80ef4dda950c30",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T22:17:16.999833+00:00",
      "head": "ac40a43645d0bec98be53122f4fa6b0822a2406d9cd7480ed3b921d9eca31d1f",
      "node": "300.wake",
      "snapshot_digest": "2de4ab24df0dc930e80628c555e90d308cfac8752137c7277ae4608237eacb5b",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T22:22:05.568594+00:00",
      "head": "f0767b436a6a10c1c2086bb17a9f53328dc77bdba40e8ea350e85d7f544cbec2",
      "node": "301.wake",
      "snapshot_digest": "0d33be84600d1dbe47cac118dd0b8961ffbf87e16ebecbe9315581140543d577",
      "version": 66
    },
    "302.wake": {
      "generated": "2026-10-26T22:16:56.522344+00:00",
      "head": "a6c09252744f55e8ba3b0e05276a920384ae05eadde433acc6c4cf4400698d93",
      "node": "302.wake",
      "snapshot_digest": "01514ee1029384f6a2998264608f1613e67fcb7821d19271540797a27b8e3307",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T22:21:34.679960+00:00",
      "head": "85600fe456451331b44cc255a31acd1c7bce6667b72c6e94a1952724676a6883",
      "node": "303.wake",
      "snapshot_digest": "53c156c56f6d520670f632ba0d48c86171680b2c4449543c9ba798773a567f90",
      "version": 56
    }
  },
  "version": 580,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d63306264633539646336653634613331.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d37663062376533343936616634316633.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
