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
  "generated_at": "2026-10-23T08:00:17.471491+00:00",
  "head": "snapshot:e228809e68d33c4544822f4e0b07f53c5c45f330691caebef659305991099ded",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T07:59:24.740437+00:00",
      "head": "dda9712836cd310c13ff9a47d361365174cc3ed4827bc93275500e27e20afa22",
      "node": "100.wake",
      "snapshot_digest": "a9f34c73f1ba515c6f6c4de7af937ee9f5728b2e05e35098c3d039069c630b89",
      "version": 6
    },
    "101.wake": {
      "generated": "2026-10-23T08:00:17.471491+00:00",
      "head": "95e89fe0656a925fb2c8b2c44440272c542c9c0ffda76198b4b41e4967b06b99",
      "node": "101.wake",
      "snapshot_digest": "edcc60cbbbdeeacc42b037eefb296354e46d4a7432a09f1757e186e5ae958a31",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T07:52:37.508332+00:00",
      "head": "05cc166ee18bcf76e1968932b1508c4b0d22d9424d09d828bc0c804d4e2b8511",
      "node": "102.wake",
      "snapshot_digest": "19babd685f6475e574487ef879793c492d9f56c53d300de7681aeefea488863f",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-23T07:59:46.079074+00:00",
      "head": "007b754795a972b95d64f67033d9f800274f68c2005a52540de7b79606f43a9a",
      "node": "103.wake",
      "snapshot_digest": "0a2b691a92d2b278b0636fd776bba45a55c589fa9d70416d53835b767e551934",
      "version": 11
    },
    "200.wake": {
      "generated": "2026-10-23T07:57:44.636034+00:00",
      "head": "9036e44f946540692e369ae823501c28eb542e078b71530da86e9af2c44c4cd9",
      "node": "200.wake",
      "snapshot_digest": "f84f709c81d63c0545b47c90d4198b502ef0d52450d1e5a0034ca230a5f57409",
      "version": 10
    },
    "201.wake": {
      "generated": "2026-10-23T07:56:39.046028+00:00",
      "head": "d64dfb20043d4b830f0d3363a265b833f6b968d6a68486c5737bf30b1ea47ef5",
      "node": "201.wake",
      "snapshot_digest": "507cfcd344f919a06459b1b640f6b17a8af49a64a61d921b754da45a049d9eb6",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T07:59:37.361190+00:00",
      "head": "eff1d55866a23141bc4a8b34698037629d4f27d66ae1e64cb25f48ff4dca2642",
      "node": "202.wake",
      "snapshot_digest": "acaa02fd7c621179bb045e6589129feebdc7bb502afab92cb11831cd7eed2a7c",
      "version": 17
    },
    "203.wake": {
      "generated": "2026-10-23T07:56:43.612104+00:00",
      "head": "44adc0a8d4face6c94d8893810413f32955b7a7a2f858ce297237f8770bb2a74",
      "node": "203.wake",
      "snapshot_digest": "8092265500b6278ac065871e43ea18749d5464b65bc65010b22a8d0e8cbb06fd",
      "version": 9
    },
    "300.wake": {
      "generated": "2026-10-23T07:54:01.156339+00:00",
      "head": "16ab9ddbac9395ed8ebb9da40ebfa7e5fb56086516f93961bd4b59c8cd4b953b",
      "node": "300.wake",
      "snapshot_digest": "65542257a070ba53e3b8392358e5e6294076ae0dd3a9cea8023c075a41d0713b",
      "version": 8
    },
    "301.wake": {
      "generated": "2026-10-23T07:56:53.588532+00:00",
      "head": "f3d37051fbd27b1b7af09a8728426dcf693f0cc95b9ff28228cbe35ef15b377d",
      "node": "301.wake",
      "snapshot_digest": "db4f8dcbf95281fb49054a7c3a066e408f22a831fe0269eac3c93d72e577ca56",
      "version": 14
    },
    "302.wake": {
      "generated": "2026-10-23T07:54:31.440089+00:00",
      "head": "2b4b94c4c1b4be92ddf70d1190f0ca94f2818bd3b25bfb23942ae48232cedd98",
      "node": "302.wake",
      "snapshot_digest": "1d9a0b34845eeab4c68c570734d4c08f4bc7787ea11a6a68f0914d9c46cf1cbf",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T07:53:46.958959+00:00",
      "head": "f9199ab82411640cc8e45eb23332d6be8ec623892a69961f8ccc13b2fcc76a0b",
      "node": "303.wake",
      "snapshot_digest": "d86b936fbdfd31b6035e658fa1d75a51eb6df8dc69c720f75fe3b652c0724774",
      "version": 21
    }
  },
  "version": 155,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d31373133323162656332636334613137.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d65306530366263616465616634343062.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
