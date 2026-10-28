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
  "generated_at": "2026-10-28T06:28:05.885693+00:00",
  "head": "snapshot:122bd64a5cd581c104d4603e154fd484cf35e31eb6af232e242af0ce35ed93ea",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T06:27:45.360581+00:00",
      "head": "9197ebf484bbf6e00f1f09c2b07ba1a5dbfb36565877b6be963e9167e805022b",
      "node": "100.wake",
      "snapshot_digest": "2f311ba54a7f6f0289fbb1a5857c07d98a6d092b836a943d6911790e8ca1c44a",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T06:27:38.668909+00:00",
      "head": "4487253d170560a7234050b1fc3f5886403ab2050098f6a709e5dad0b5bcdb07",
      "node": "101.wake",
      "snapshot_digest": "04da578f31982d87954294641874bbfb5cf5c6cf1f6945dcf0453f7bd2fba17c",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T06:27:46.363461+00:00",
      "head": "d9bf5717ef87206d7cc74c3793c3d4e449f5e3ccd096917b4564aac486027a7d",
      "node": "102.wake",
      "snapshot_digest": "1e3af768e5d4417ecb98bf60c20de3faa8af40133afa4da48f29401830469584",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T06:28:05.885693+00:00",
      "head": "d7c3ed036f484dc7e2a8a1ba07a054a92cc83817c7688ddf84b9d65718e53f16",
      "node": "103.wake",
      "snapshot_digest": "340399a8b56d2f7727fa3bce820ca52bf88b19baa677c43d13bb66c575a85a71",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T06:27:59.639992+00:00",
      "head": "782e9d22307a298a0b8ede60d522c469a627ad0628ce8c2d6765917c4c3ca272",
      "node": "200.wake",
      "snapshot_digest": "89bdf70f2da04504dc20ea0143e51340eaecd91380bbeac04bba7939b506482a",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T06:27:56.965994+00:00",
      "head": "1569ded16cfdc4d792ae4ee5d2a6d079a4b4de55109bf970ed5a96de9c2fc78e",
      "node": "201.wake",
      "snapshot_digest": "04dc46beef370fa2cc2f82e2d80bc2e6a89e9ed3f4f1e27d62aaa3483846d344",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T06:27:50.106048+00:00",
      "head": "c864aad3acf39a4df2d023218843e2bf613efb0565f1a9d34af381601fbab89f",
      "node": "202.wake",
      "snapshot_digest": "99bde527ac04c2ff2124e2749e90ecf5c75c8092eb0edb8b02c64544f41fbeeb",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T06:27:43.697409+00:00",
      "head": "61e2203ba348cef55f8ce8eb394a6023a0105d5401aa3d8320932e6afdf404d2",
      "node": "203.wake",
      "snapshot_digest": "59daba22a5e0a2d0cd553bfdb52cb60f4d31dbae0d148ec2fc34cbbe18a1f998",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T06:27:45.698401+00:00",
      "head": "95dee5d537583b617451e3c88df06eae8fb3cb62765708110571eb7178a63dd1",
      "node": "300.wake",
      "snapshot_digest": "ffc5ae161115305678bc7940c41022f7d1d0d17f721fc6d02446b1233b376850",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T06:27:54.099056+00:00",
      "head": "348571386f8a7a736b499f60bbd0dbf65ded46715925021f1a4c2fa22bd2bc0b",
      "node": "301.wake",
      "snapshot_digest": "98b887999b0679f693df9e25077b769dd48deca49176b040d29e15b04734a5a6",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T06:27:40.475878+00:00",
      "head": "aceb66de10740aa6b1254888c43fd44ff58a706d3d2a764987e6b01f73ef2f69",
      "node": "302.wake",
      "snapshot_digest": "9c79b339d4a2d595314bd6acc53f20cef749227b0498c0d9d2530a8dc40ee3a6",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T06:27:54.972536+00:00",
      "head": "13b9ab607ac6d17c41051eddb63849d45a74b3cf8e1b53f065a4840f4422bdca",
      "node": "303.wake",
      "snapshot_digest": "4bdee7bd258a34b2e2bd5f53e616c59b3a8cf8a18c3a9ad6aef74d6b4e6868ec",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d30396638643532383338626634643731.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d34653631326232346463633034373437.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
