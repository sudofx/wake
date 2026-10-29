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
  "generated_at": "2026-10-29T07:54:08.499610+00:00",
  "head": "snapshot:790d7189388d47b0a92c0ecc6f68fa67e31d14d4741caab0c898bf4066ba06bf",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T07:23:59.390953+00:00",
      "head": "f3773ed0f94d74f086eb6db3613621800269b05984f8e06e45f50846940a3bc5",
      "node": "100.wake",
      "snapshot_digest": "a3f1a8b2cdce2dd2bb0ebd0d2fd0cfa0606226af5464649f2791dfee80ff0c24",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T07:38:06.520868+00:00",
      "head": "b892f9e22914baf7697d5895621ce63c5fbc69108da2a24674137f4dbf79ef95",
      "node": "101.wake",
      "snapshot_digest": "9e3330e23734ecf8b6acc20917174fc215653ebde6644444caa1767c547bd601",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T07:52:24.198084+00:00",
      "head": "f72ccae52ce790bcc35c02c51f228d7d497f5a4d0e52c9ccf82d5d374b3cf5db",
      "node": "102.wake",
      "snapshot_digest": "9f71fbde5569afd39bd427c6daaccbedf56f54847330d1224a9f2546834f6480",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T07:24:04.336826+00:00",
      "head": "1bffe27420ad75592e30bdfa85871fd29d6c86c406afa277fd24259f7af7cbb5",
      "node": "103.wake",
      "snapshot_digest": "9040ae7aee3a9405997f6532d7cf5065a188e044e3fd92014a9d2538cb1be7c7",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T07:24:02.386595+00:00",
      "head": "c0062768daa19cd09b0596081a74a5ce8a1b63877f3a6917255c7e01a1737a53",
      "node": "200.wake",
      "snapshot_digest": "485a319849168e7b787444d96fbe66c47e3e349587b6d5827b4eccfcbd7ecb43",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T07:24:01.578324+00:00",
      "head": "e9916eb4ccfe0f3a4c7f30b47dde76f2bf19633c677f163fa20df6572f9b1706",
      "node": "201.wake",
      "snapshot_digest": "4dc9a9cb302038bdc58610253520a917faeb2d393b09e5ac5142ca5939436016",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T07:23:58.444289+00:00",
      "head": "eb6f1fb491be209d3282303798875b30bf932e0972a5fdf6f0233a4d8a320763",
      "node": "202.wake",
      "snapshot_digest": "2d3697be7b3558e83ef11dc9b0ffa9c1cab170e587c6c6d133b9be2fc9683d32",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T07:54:08.499610+00:00",
      "head": "ee193dd35426522f6db6035632378aaf4e6a103fc3c7f3c0c68ce18bec42c19b",
      "node": "203.wake",
      "snapshot_digest": "2884c5667efd432e4507c73eac3fbb418539cba50568937388f1333d5b2694bd",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-29T07:23:57.151914+00:00",
      "head": "17bc6c85d17842a813e00fc3c3f7471fb0eabd59de0ca03e38dd10069d868b20",
      "node": "300.wake",
      "snapshot_digest": "43d5e540d75bd6a04a8deb33901c7dec4b9952328db9e6c59f224a6e2e08ed1a",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T07:24:01.598728+00:00",
      "head": "4b753ed87e1e1f7dd334e092587b156f322706327004f7a5dd14a40801be4792",
      "node": "301.wake",
      "snapshot_digest": "b6ac116cd0ed88b75d33985b0599513d372a66df396e52976b1041ad8a55f970",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T07:24:00.703416+00:00",
      "head": "6f8d174f3ac159880107e87963abab9c63eb0d463cc0d0f7800a44268536318d",
      "node": "302.wake",
      "snapshot_digest": "bf336a543bcd9ebe1eee1d70ce99e8436b24c44c343a240ec0af941bbfeb8e30",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T07:50:41.870346+00:00",
      "head": "a8650b06243bcd050a4345ca8133f5aecedee2827e50805b920f201485cbfc74",
      "node": "303.wake",
      "snapshot_digest": "c3bfadb3291d7b0e8a6072fb45b62aa35de24d8e2ee7774ea511aa502c308e2c",
      "version": 23
    }
  },
  "version": 279,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a736f757263652d636636653631316566363233346432/66.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a736f757263652d663561633366623531373139346637/36.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
