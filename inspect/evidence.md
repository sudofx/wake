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
  "generated_at": "2026-10-23T09:40:05.585862+00:00",
  "head": "snapshot:207fd15541adbd52f6ffc1124a43d4b1ad71988e61663325351d410439a2281b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T09:36:01.605240+00:00",
      "head": "791035a95a39bb65bcffab5f67eaf36520bd8ca52c259dba99b4612c2bd35814",
      "node": "100.wake",
      "snapshot_digest": "6609612b0374c982f217e907dfcaccd5e290f16b5d0b44a99030e1a1283419c5",
      "version": 9
    },
    "101.wake": {
      "generated": "2026-10-23T09:28:44.853134+00:00",
      "head": "fa8b6d405ba99e905b59ad913c912222f69f72348747d7875c12148472123a41",
      "node": "101.wake",
      "snapshot_digest": "61a8bc7cb694d3aeea8d4c1f3923902795e6ffa004f5fe382820f826e36c26a6",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T09:40:05.585862+00:00",
      "head": "9d018e53609ee1a0f7a267824448cb6b98a35d081566d35eff28db593d70b1d6",
      "node": "102.wake",
      "snapshot_digest": "82b586c161add31fdbb3c1d3c52bb835439f54364da5869d92da4f593c7f88b0",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-23T09:37:37.592243+00:00",
      "head": "4841792ad9ad04fada7723903b39fe443d5221a25cfb5e298da09ce15d7a4ce5",
      "node": "103.wake",
      "snapshot_digest": "c4b1382690312e92e769819ce8fa344921cb149910595534622f6e0e392e18c1",
      "version": 13
    },
    "200.wake": {
      "generated": "2026-10-23T09:32:21.438735+00:00",
      "head": "c557e3233c926e0b7b55c7a83410432b852aeee211833904161783c656da4a53",
      "node": "200.wake",
      "snapshot_digest": "a56f47b503d94ec64d76ec1ad1eb899194f5498cb9af36a9c6e613e35edbfa83",
      "version": 13
    },
    "201.wake": {
      "generated": "2026-10-23T09:36:15.027636+00:00",
      "head": "8f19607ad68cfd79729f282538196e2320a67e1ee1313cd9844d10b2f3e5c77e",
      "node": "201.wake",
      "snapshot_digest": "786cfa458612193d78e9a95ceed9a7eb17db9958cfe2fb26bafee400772ee118",
      "version": 13
    },
    "202.wake": {
      "generated": "2026-10-23T09:32:15.337950+00:00",
      "head": "5183fe0db5e543c01d1e6c5c0fce3905f14fc13bdb7f23940e4521791db2740d",
      "node": "202.wake",
      "snapshot_digest": "6dcf3b168cf310ed4daa115ed5202d19f8fe759938f782ca79cc71c3e7dfcb13",
      "version": 20
    },
    "203.wake": {
      "generated": "2026-10-23T09:35:38.682938+00:00",
      "head": "14a270c9f250b56a894e71db071c585d640d53558c8700c0156176c3360a8710",
      "node": "203.wake",
      "snapshot_digest": "f7055089c38b0e781fab80b9c96f45bfdbecfaab5a7b075c90f79a1a5770e485",
      "version": 11
    },
    "300.wake": {
      "generated": "2026-10-23T09:30:10.880923+00:00",
      "head": "8fc6483b2b32282e90fb6db0531f7b8b270fb61658a3deb6f363888e231e009f",
      "node": "300.wake",
      "snapshot_digest": "eb7ad2d69ef1f783659545ed3e52b2e0448698f832a876921c6cd585661c4460",
      "version": 11
    },
    "301.wake": {
      "generated": "2026-10-23T09:31:24.296720+00:00",
      "head": "a9ebd060e65d9e827d9fb848688854322b239145bf8e31f61d1f3442c30e6f42",
      "node": "301.wake",
      "snapshot_digest": "b496275060eb9a6fe6de13284c05b3cea048050463f25c11210ceeab56a88109",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-23T09:29:21.433394+00:00",
      "head": "f21f6efd8b42d63852e4b0ce9fca14739722ffd59934c7f3d657b5ed7b7ff94c",
      "node": "302.wake",
      "snapshot_digest": "f917c2b6bea727df3ae3211cebacc59570f47ea41fd5fd177fff1a7c3cc005c7",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T09:32:47.104609+00:00",
      "head": "e6064dd48760033090fcc2ddabb66bf58252a897c6688aed8700ca31bc77491c",
      "node": "303.wake",
      "snapshot_digest": "c36aa6db471d250feb13b77e5ceec80612a6c2269b2f9c116558261473c3dd56",
      "version": 21
    }
  },
  "version": 181,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d663732666364636238343863343130/65.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d30393739613638393364373934313736.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
