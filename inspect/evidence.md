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
  "generated_at": "2026-10-27T17:33:55.311417+00:00",
  "head": "snapshot:9aa6aa111f3fba54a05e9c32b9b53a9e77529db51b8d8144db30b7524634fc56",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T17:33:46.873758+00:00",
      "head": "10a94645fa0114e43cdf094aa74b3c7d448138448e0ef09491b2eb6a75ed5224",
      "node": "100.wake",
      "snapshot_digest": "15cb789191b3526567d9514e8356faa37ee8486982e7765fd3e7bceefb698441",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T17:33:32.612983+00:00",
      "head": "f12085a07377a3e5b63e8818432d620664ab8df1bf36ab0315134e52cc2b2e90",
      "node": "101.wake",
      "snapshot_digest": "5d12ca33a7f9c9cc973d1fce214ae4ff66daa36aafc2386d70f3aaa281c63b22",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T17:33:32.584444+00:00",
      "head": "514e8c1e45afb823050440c6bf4f964a4aa26a871fbbcf01ee42da3c003e4f74",
      "node": "102.wake",
      "snapshot_digest": "e95067e09fb157a46ecebe7852037eabcb631991fc73f26d55ef4a98fb78fbfc",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T17:33:46.590386+00:00",
      "head": "901d4e2ea72872274d4bc4c7111b99d6ab6b1dcd17f08b6a962e1d77b6a1f830",
      "node": "103.wake",
      "snapshot_digest": "5f59463e490bd0c29da05ec3aa0bee296b59d8d03734682ddac1a853189122cf",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T17:33:54.653220+00:00",
      "head": "895cc3ed15ae0fc01394a2e7c34a82870dc5df7c6c04ab9546d66491d7381c4b",
      "node": "200.wake",
      "snapshot_digest": "7146e7a967243f786287557a22cfe2c2493a36d112d14e512998f0ccb6230258",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T17:33:55.311417+00:00",
      "head": "6685bb5515315131d3701106f324303b2dc1c3bd7fa7a012ba6933dc2203676e",
      "node": "201.wake",
      "snapshot_digest": "9dacc2def816df3deff6fd20cdde1e19ed07b7b2d9205ea215e864b7befa2cf7",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T17:33:33.825746+00:00",
      "head": "26e261ab87778e68776d3717457d2a84a7b947da78f777fb8191700ccf55e943",
      "node": "202.wake",
      "snapshot_digest": "1884913724c0e36dcbee8e075e9918c5bc95593afb67e7638ff412b325dfdb2b",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T17:33:29.583150+00:00",
      "head": "fa36a79ca349020fd4ad12031f7a37b9e48d407dff94ca26a8a9bcac270d9de6",
      "node": "203.wake",
      "snapshot_digest": "2eb17b1a30fabea672893c6d79757d9255229f30cdd8e3121e676dc6be226adb",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T17:33:29.052624+00:00",
      "head": "b67fc4c7f5a4e28e86e1748a20a09ccf84747058bbfcd0ab82320670cb29a796",
      "node": "300.wake",
      "snapshot_digest": "e90f075da7bf98a54882fe313746f7f9e0731abb00ee05d57cc9cba2e665325d",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T17:33:35.571700+00:00",
      "head": "4f862bea5256104df53adbda41afe2eaf209876c0a56cd86c0a820fdc2276706",
      "node": "301.wake",
      "snapshot_digest": "ffab0fcc74670a9fe971d35be295fd4db7fb947fdc0abdd874d795f2de47bcd7",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T17:33:25.759245+00:00",
      "head": "e188549e08b06e01dd5265a6e2cdb40e05d8c1f27aecd825ac24bc3c9daad4a3",
      "node": "302.wake",
      "snapshot_digest": "32838c2a0427f575f55bab23a869794fef1bff1843d042d5642c2699756b51f0",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T17:33:38.707384+00:00",
      "head": "607d49321d507af24aeb75468bffdc263cc52066274f16cdbc60f78baf06d658",
      "node": "303.wake",
      "snapshot_digest": "0941eb2faeb52cdd14879e0e7297a39dcc7410fa15f359f9d73287cbf7a280ce",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d36373533306162373435373334646135.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d34303839366631383136663434366363.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
