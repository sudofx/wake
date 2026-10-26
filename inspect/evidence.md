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
  "generated_at": "2026-10-26T16:45:19.862507+00:00",
  "head": "snapshot:8a4d81781ac87091e53da48266e555533c0028b8bc508871622a346640fcc620",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T16:45:19.862507+00:00",
      "head": "3c88a14a12fd56292a8d03ae6cae2b3d4381234f20d73e3d9bd2101b46b2c615",
      "node": "100.wake",
      "snapshot_digest": "9900d0c80647e2988a664378c20cae45e5865eedae8e097d1d4458eb7747c9eb",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T16:23:18.862474+00:00",
      "head": "ea86d1bc9ed9048997437314e4d4fd9c450321f23ab370c0ccebca751e412002",
      "node": "101.wake",
      "snapshot_digest": "1a62b99a604185f30a0014f3658089733b9cc68077f6e76d729857a6e6b7882d",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T16:14:28.489316+00:00",
      "head": "4e7214e2647ed18701fa61bf2c1bd11e9700ca1574f8989829a48184a2e0ffb1",
      "node": "102.wake",
      "snapshot_digest": "f0dfa388b29b330df32ae20ae230a3822fa60f82939a1e4d9a0c1bf24fb56f6a",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T16:26:26.685262+00:00",
      "head": "5010922d8f6af7247168373e00e6204c8c47002a2d569ff7be1aab7c41062dde",
      "node": "103.wake",
      "snapshot_digest": "442ded6f55aaabc6ecafc7f72ebf12cb74ecf00bf307a786f1e58c227f4e595e",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T16:15:22.208429+00:00",
      "head": "f53e6f1ac8642d7437fe317937cb062a4b58431250824f17a5d411fccee9925d",
      "node": "200.wake",
      "snapshot_digest": "e3d8ceed1e7b8c0f7d102ac2150910159e73ccddf324f67041b183b6762cf896",
      "version": 43
    },
    "201.wake": {
      "generated": "2026-10-26T16:43:22.357806+00:00",
      "head": "2763e5d9c07a057ba3842ebfd17ef4ac8f8f87c6bc986085facf052e9fa442ed",
      "node": "201.wake",
      "snapshot_digest": "e45636e4b7b81c320507839f7d6ecef9acec9d19c249ead2f0af37895af0b86c",
      "version": 45
    },
    "202.wake": {
      "generated": "2026-10-26T16:33:46.539476+00:00",
      "head": "407f3ca54d3c97d453d01aa9a95de2cef5ee9ccd57016bd4ee3fe34f1837c884",
      "node": "202.wake",
      "snapshot_digest": "0c00bb21da78682b37a847d0cdbda16fd8290212250b10fc8c4165bc8af613c8",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T16:19:41.002460+00:00",
      "head": "4fbc321040f7348b353e5b7b1a4530f187d8b6e8b0c712176b6993b84a270148",
      "node": "203.wake",
      "snapshot_digest": "d0f80302b6d833cbea646ca67c65ed00e16006bbe62b55c9d969b196a03618f5",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T16:38:14.519836+00:00",
      "head": "712439efc365dd11117980a24aee877727d45df700c2f1a40d448d14e6696634",
      "node": "300.wake",
      "snapshot_digest": "d816d98afbcbbf5b4b790b049cbd3aef4736c6d88bdf207f247aad38a3992d9c",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T16:29:59.993566+00:00",
      "head": "4835d0a871c0aaea89b1498b26407a8c725fed77810ff1bb21bbebd59400d73b",
      "node": "301.wake",
      "snapshot_digest": "2070ec6c17a12135cab46eff1c01e6b9a94c1ec8d899dbd2e459422f5acc3fa5",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T16:17:54.467511+00:00",
      "head": "ccceca3326c72fbc74d6f9a9be03601120602baf5ec966a1333e450fbd5dcd97",
      "node": "302.wake",
      "snapshot_digest": "b1635e418a17f978f8205f592f55c0b708e1a860300776bb2cc0dd95f31bb9c1",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T16:11:18.626966+00:00",
      "head": "d419ff393ea3ff044fac9c34848c4446db0481e80e3b00f1a4987510773fe0e3",
      "node": "303.wake",
      "snapshot_digest": "d9bd642e86eecfe5d8fe36f4d68febf7a78c57ae2cf01c06ac76855e71a02634",
      "version": 56
    }
  },
  "version": 576,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d64633166633836663439626334626631.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d633033613231306533636636343633/33.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
