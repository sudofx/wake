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
  "generated_at": "2026-10-23T12:50:11.718856+00:00",
  "head": "snapshot:5835e1f8d69b2b43a0372c49650f9a11f7031110a561d4d40f1412eda503d392",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T12:50:11.718856+00:00",
      "head": "ec8bdd4f80273b66572b6c7af6b89717b54633fa7c252aee576976cca2c5023b",
      "node": "100.wake",
      "snapshot_digest": "903d7e92cb71708265f7d1bae09a59251c9d9409ead7f7f04e58cd3e4379c75c",
      "version": 14
    },
    "101.wake": {
      "generated": "2026-10-23T12:48:41.524195+00:00",
      "head": "26ac0e2278beba14de618ae00a85eb7ed749f5757bd717846f34e8dd67a674ef",
      "node": "101.wake",
      "snapshot_digest": "de690a4de011f66c2f4b6064c2c41bde68161b5f04c8cc3ce200f0541e18dacc",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-23T12:45:30.950192+00:00",
      "head": "5b412cf429494a16952198077b0462aca8534d583e83d57acb6710aee3e792a7",
      "node": "102.wake",
      "snapshot_digest": "81f538b9b51fc76a2dafb23114cac184591884e85c1caeea78d9426922a91cf5",
      "version": 28
    },
    "103.wake": {
      "generated": "2026-10-23T12:48:06.877758+00:00",
      "head": "f977e9f81fbb767e97cf6d2b7b63d7bc7fc5e201d851fffcfe2d3f56bd1eee92",
      "node": "103.wake",
      "snapshot_digest": "9778c7df312d2a59c1c9a8e15e59860e2551ce72fa5f4461427f88ec920bdbcb",
      "version": 16
    },
    "200.wake": {
      "generated": "2026-10-23T12:49:52.520833+00:00",
      "head": "1244d4e0c5147fdbea0d02983b9973adf1945aa5fd48b6648dd763f9a01e5e97",
      "node": "200.wake",
      "snapshot_digest": "3c21660a7e525dbdd953ea1f867107c370534e898855c5dad61223da216f9aba",
      "version": 16
    },
    "201.wake": {
      "generated": "2026-10-23T12:49:59.189371+00:00",
      "head": "8800d706a9ccd3ec67771abed7c58f8c6e3ae78f39185962526216c7a2c54e7e",
      "node": "201.wake",
      "snapshot_digest": "1c6b51fb3f6cf0795a1974b805cd5ee27a24b232d146a9f3d3027ef5e5df4b9c",
      "version": 18
    },
    "202.wake": {
      "generated": "2026-10-23T12:49:02.323200+00:00",
      "head": "b373e6f706c7107c310cd9075a921298fc225999fae689e3e43cf37b91ef721b",
      "node": "202.wake",
      "snapshot_digest": "2ed4187afec4a02cb331890a049049d458cc53dcced52505d58a6724b66a43bc",
      "version": 28
    },
    "203.wake": {
      "generated": "2026-10-23T12:48:55.990365+00:00",
      "head": "57d95a720c7696ba859078d460d9fb351db291544332e341cc85c30f4d04a7ba",
      "node": "203.wake",
      "snapshot_digest": "cb91c872f27ff8174b1341559c6acfb1d36eabfaf108b688767eef6b7a243531",
      "version": 12
    },
    "300.wake": {
      "generated": "2026-10-23T12:44:49.966145+00:00",
      "head": "8843392648f4550d4885938e6d2a29b6b349874616bcfb53258c388e3a168398",
      "node": "300.wake",
      "snapshot_digest": "8882e1464ee6063a6e1bbad6c8b45fb5c49f10cac4b59edf2c66de0c1d60c90c",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-23T12:45:43.374277+00:00",
      "head": "933a3fc2e9eb5d5d03be8a33b1a39515c7eadf47093e580257cf31921e9d8ec8",
      "node": "301.wake",
      "snapshot_digest": "ec5928b3bcbd43304af4a20c1ddd95c016b5c0df74e8d2fb4c336daf83905cbb",
      "version": 24
    },
    "302.wake": {
      "generated": "2026-10-23T12:47:27.059718+00:00",
      "head": "e764999e9110100780f38baaf1960ae4ef9ddb0a0cc3009e2dacb369245c5164",
      "node": "302.wake",
      "snapshot_digest": "b7efa2b2d79c9474cc5d56338be6a4cac1cf6ec6a0adddfdfe267a6ca35ec61b",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T12:47:31.557829+00:00",
      "head": "43e467f8f22498f50ee9f107410ac5c77a2a61a164b5040155b759f89a280ec1",
      "node": "303.wake",
      "snapshot_digest": "c5e12cf44e7f50acd6cd9ffcc6dfeeb7653d641dc49b510710a8c73bc10b0260",
      "version": 24
    }
  },
  "version": 228,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d61356663373463626333366234626665.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d65313131313466393433303134386130.json)
- [notebooks record](../reader-records/notebooks/3230332e77616b653a3a6e6f7465626f6f6b2d617373756d7074696f6e2d6368/616c6c656e67652d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
