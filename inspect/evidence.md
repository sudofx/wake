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
  "generated_at": "2026-10-28T00:10:55.208356+00:00",
  "head": "snapshot:f91563b85efc7ea84b09c997c46e55a6be47cfebda6f92f2a69ca65fb447c907",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T00:10:44.506972+00:00",
      "head": "ecaada6742d98abf6d04672f965534c3ef36481bc53aae35493e5be537624f17",
      "node": "100.wake",
      "snapshot_digest": "3bb0138dc2064849faf4cea47368e19eacf5e788a8ed36f7269a5372992a6798",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T00:10:34.465799+00:00",
      "head": "c4ba8d88861245add18e9d5a42b2e5cbc98aec332e2c5533d163f2f849f57566",
      "node": "101.wake",
      "snapshot_digest": "6a0ba8c2bc3304e99581932549518e2146644f3b256b41a872f7f006e7813c03",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T00:10:38.411766+00:00",
      "head": "1682cf81ccbe16559ade67ae8955b8cca546a30d5043d5f8006a15a6f916d79d",
      "node": "102.wake",
      "snapshot_digest": "e63fd715cb4857b530f6ab30416cc1780faf44e061d4be145719285f3f58fb76",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T00:10:44.992254+00:00",
      "head": "7b642dfd657f4b74952daafd439b308893e6d0fac6b84ff0c6524cdc1e2fb818",
      "node": "103.wake",
      "snapshot_digest": "9f070ba1b3d93ad07b756a7c51cdadbd32c1fc1f29f8fd42dd5045dde6e43c07",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T00:10:52.605311+00:00",
      "head": "4e3d89bfaf0b65003522534f6661355cbdc6647f61255dc551d3355c4a8ff9a8",
      "node": "200.wake",
      "snapshot_digest": "5e4c27dbf0bc0bb69e7f08310c0fc43e562a12660982c05818d6a942f18876d3",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T00:10:55.208356+00:00",
      "head": "4ac2b21d06a1b41904530dc19e5a6d5f934cc93dc26882778bf11c7396e1fccf",
      "node": "201.wake",
      "snapshot_digest": "f888e959742d2e182aaff59e9d19fbc114919a119a39e8a351f03895feb96cd2",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T00:10:28.523514+00:00",
      "head": "f312e48d298353a865f7a2333d435514e5829560d5291a9055a36bb28802d0c3",
      "node": "202.wake",
      "snapshot_digest": "ac7c2c88cd11ac867d813936f7839b7debcabba1271135f2b9191b1227e91d1a",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T00:10:29.439229+00:00",
      "head": "7421c2a7fef78c76a752b8a34fc1ed5eae9615403bbaa136e02094d65d768032",
      "node": "203.wake",
      "snapshot_digest": "bf43edd434c9ba0864b100093ab7d2963e42755da26df67b772ea7d35db618bd",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T00:10:34.050261+00:00",
      "head": "3283ca7d426eaf3c661ed72216628ffe9651265212c272e8daec7171994b8fa8",
      "node": "300.wake",
      "snapshot_digest": "edd6c65f7861f210147f46208fa56b6d2195e9276fa866368885c5f1e37965fc",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T00:10:35.321596+00:00",
      "head": "79470a4307aa5fcebb4ccf51091ed1f5ffeea7933b5f13386ad13ef657a1e3ce",
      "node": "301.wake",
      "snapshot_digest": "9e8040333d8b572c392d7e5c4b72b1132564c8a309d08ff87f3848c4fed21c64",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T00:10:44.861984+00:00",
      "head": "320a4cc3eb1e5a164714d6d129dd043aef4ba9910ee043c354b91f4ab7ea80c6",
      "node": "302.wake",
      "snapshot_digest": "8ea9e45f7c0e11fd54867a6d335869cabb7c9319cb3ce4fda9b1ed170e46f9a2",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T00:10:42.221835+00:00",
      "head": "eab4d73297a2ca4f5bc505c3e64b278a6b0654ab51170174709df4f9dbb79a2f",
      "node": "303.wake",
      "snapshot_digest": "69a87eba59bef25616bdfe1aeab6402d79097dc665e611da1c2c91a6d2a15f5a",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d64383339323731343662303334306562.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d62303663303339383435613334633937.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
