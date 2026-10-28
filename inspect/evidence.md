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
  "generated_at": "2026-10-28T13:58:44.565437+00:00",
  "head": "snapshot:2bf270045df532e056f5202b5e30ce0ea77050af5ac1b26e21ef895bc8f78867",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T13:52:22.280234+00:00",
      "head": "a4b2477fc4850fd0173e9bfd578514eef54eaa5060ea497c3099848532966e04",
      "node": "100.wake",
      "snapshot_digest": "4ef442c45a2e9a44566f3f70b1c62f1e86eeef947c19254c25ef869d2444e769",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T13:54:33.280411+00:00",
      "head": "be1c3725a0047ca72f594e3981b6c44cdb0791653f4e7649a08dc8f7c9b1c126",
      "node": "101.wake",
      "snapshot_digest": "e7e3b529caafe5e8adcc3784d31e398de0a851831df6f55f8e12df4d1d5d79e3",
      "version": 19
    },
    "102.wake": {
      "generated": "2026-10-28T13:58:44.565437+00:00",
      "head": "1cb0c5d5d0054fbeff0ba3d60c95eae0f0ddf8fece5e3899420e4a461596e571",
      "node": "102.wake",
      "snapshot_digest": "e6606830b70a6aff086116ea8e59fd8de9395b50d62b282ab8031666ba210730",
      "version": 15
    },
    "103.wake": {
      "generated": "2026-10-28T13:58:19.748692+00:00",
      "head": "1897aba80a71de9b625713d14e6fcd6e2f356f5087a5626cf69b40af9fad5aec",
      "node": "103.wake",
      "snapshot_digest": "cbb68f3d91121bfb4bd33e6fcdf11e2bfd587aa2854e49cb0dc427cb9d277cc8",
      "version": 26
    },
    "200.wake": {
      "generated": "2026-10-28T13:58:36.931577+00:00",
      "head": "01f161313e34ce54f2cb9412086ff6da08a4f69e512f3e047ff4b93cc0804eb1",
      "node": "200.wake",
      "snapshot_digest": "f152ef0528b94bd10b13eac0f7773216db2630f3abc13d9a7a1739153dd60807",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T13:49:48.713225+00:00",
      "head": "aa3dd39b94b1bc7180add1f0e0b16c333dbf955fb663842f1e33164946ea47a2",
      "node": "201.wake",
      "snapshot_digest": "31ec3e199632e235a7b7d13c5a9981595314a41cf3d3b7e122edb87c651c5315",
      "version": 20
    },
    "202.wake": {
      "generated": "2026-10-28T13:54:31.660755+00:00",
      "head": "821c936b4c61a9594f8adab21d44e1dbbe20aab503fcfcc7d2828ba5af3884e1",
      "node": "202.wake",
      "snapshot_digest": "7473dac152eab930b0faad1ecd15c0dba500b239ed7af897b3b0bb88e036adcb",
      "version": 26
    },
    "203.wake": {
      "generated": "2026-10-28T13:50:46.225087+00:00",
      "head": "95b419649318c546e10f727131e18c4768308ff7c2a3cb25abec2225dd6f2bb5",
      "node": "203.wake",
      "snapshot_digest": "15961821c3952d3ebb0ba4566445212b402dc924b2d1e7c8eeba33979291c880",
      "version": 23
    },
    "300.wake": {
      "generated": "2026-10-28T13:52:25.029301+00:00",
      "head": "6fcebc3680cf4836385faa8552940edb083d5661feae4f30eb5d0467379c3156",
      "node": "300.wake",
      "snapshot_digest": "591b13fdd9e41b8402f8718927bae04ce85000d705cf4fbce0264a8de5f17c23",
      "version": 22
    },
    "301.wake": {
      "generated": "2026-10-28T13:45:31.912439+00:00",
      "head": "c4857c2d4610cac2a500ccf8f6a8884464b6e71524a3633f04b9b31207e5780a",
      "node": "301.wake",
      "snapshot_digest": "6feed9b92913400a036e8995552dccc5f33b2f62cfe94662f43306cc40e272e0",
      "version": 15
    },
    "302.wake": {
      "generated": "2026-10-28T13:45:17.593540+00:00",
      "head": "569036bc054e332610bb337f26db0cda143a9f578592900e0712742a2609ef47",
      "node": "302.wake",
      "snapshot_digest": "07f50a3ef58b3d43e2438bb74abe391b13a9e4ee1f52e52af7ad5c7db03b7395",
      "version": 20
    },
    "303.wake": {
      "generated": "2026-10-28T13:51:32.666078+00:00",
      "head": "77de62e005edbf7614753b395a6af5743c449f67f8041717710f3eb3a5ec2493",
      "node": "303.wake",
      "snapshot_digest": "cc812197f7bda385397bb5a2ce8b4112aa688e5e34bf76dd438923253f7366b3",
      "version": 22
    }
  },
  "version": 250,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d393334613032346665303664343832/36.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d34646161313139656337646134623932.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
