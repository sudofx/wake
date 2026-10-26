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
  "generated_at": "2026-10-26T05:13:53.368204+00:00",
  "head": "snapshot:144e3d5d3a62fd61a7af6d1d245b03f7c3d9f1a5c67a4de554951a71fa057303",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T04:48:44.061890+00:00",
      "head": "2ffc7e7ba14bccc3c4d381c8fb146483be99f4c72765aa988f5384ea60590336",
      "node": "100.wake",
      "snapshot_digest": "9fbd8c570676fe27a901927c1720339a6b9f0a84e6d39afaa25bdb58c4996cf2",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T05:12:47.682252+00:00",
      "head": "01746b62b506200bbf111dfea7b30b971052581c604cd8665181491819036f82",
      "node": "101.wake",
      "snapshot_digest": "751c97402e19aeeada6d45985152a40b78dff5436ef961c3cf61aa8baa972968",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T04:57:23.467926+00:00",
      "head": "c031851e067d5e000ef28ecf8b2e368885193c9427eaf6908c4dce1a8e58e6f3",
      "node": "102.wake",
      "snapshot_digest": "600d3ad327413425f5f1b392fb752b9580ad705ccd1bf433eb12df1806ed5890",
      "version": 61
    },
    "103.wake": {
      "generated": "2026-10-26T05:13:53.368204+00:00",
      "head": "58a3b3ee644effac75c196f2715ceab0c539581ec9b91398d64a6ee005cd94c3",
      "node": "103.wake",
      "snapshot_digest": "fd6c3bd056a9374db245517b8c6fcd915b49e609d381800f5988e1fa1d7871ef",
      "version": 42
    },
    "200.wake": {
      "generated": "2026-10-26T05:06:43.602299+00:00",
      "head": "10a9fb11c340aff7ebb97873f122225c0df643d679b921805cbdf27c6b819430",
      "node": "200.wake",
      "snapshot_digest": "fe933b9378ac85aecad5335d065a78dcbb366b0ebae3216e2bdfd633448e0364",
      "version": 38
    },
    "201.wake": {
      "generated": "2026-10-26T05:13:06.562398+00:00",
      "head": "8349b2689c7efab399f636c735ffff63421aed5544ef119efcdb11d6128b648c",
      "node": "201.wake",
      "snapshot_digest": "cf273f84527dbe23be9cc6737c11652484af78d940436022c85b97d4bb765ee7",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T05:12:06.066716+00:00",
      "head": "b477cad7657f918cf3d93722aedb8ac137e9e7fd2dbd18c4c9402e54ad3a30a8",
      "node": "202.wake",
      "snapshot_digest": "7c292476da7458d49458c0870d63bbd77267846b9c9d95b4e89ef3d14756d109",
      "version": 56
    },
    "203.wake": {
      "generated": "2026-10-26T05:00:46.381949+00:00",
      "head": "dfdda0e789711e6571db51e4c670f6d13e679c025082a53aa11be92e5cb1d7c8",
      "node": "203.wake",
      "snapshot_digest": "0bd2aacfc1a00ba2ec329cb4fdb77ba0740d43ad90905d745f7de455eaa34ae4",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T05:09:26.641368+00:00",
      "head": "e5ce55045c41cf3f067dd653749f08ed3dedc38078e3dd6f03446c63e1f0ca37",
      "node": "300.wake",
      "snapshot_digest": "dbcd3d2492ee78a1a2de807da2610d41408a1680fa9442ac64f5af5252142cbf",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T05:02:54.510762+00:00",
      "head": "5cf4d4fa1b0565bfadc4e24971db25800681136b60ef1097238a39defe73556f",
      "node": "301.wake",
      "snapshot_digest": "ecbe33010b54712e28e03cb41ddc9f97e86715add711ecf9f61f99fa6e5e8894",
      "version": 60
    },
    "302.wake": {
      "generated": "2026-10-26T05:04:15.360635+00:00",
      "head": "133044e3a2fddeffbba96a25a662109c3b86d941ebcdbdcd0e4105f355ba3c6c",
      "node": "302.wake",
      "snapshot_digest": "13874df13681232355733a1bcbfbfc5643f332c1db4ce5a300f9a485f509f266",
      "version": 44
    },
    "303.wake": {
      "generated": "2026-10-26T05:08:44.446428+00:00",
      "head": "5d1dec962b5864aa0c4bc79a4e617cca70be4157d7002c407b3fe19f33aa5bdf",
      "node": "303.wake",
      "snapshot_digest": "f9cc385d3789458b0ee82efeb7561a491ac9e8ed44908ac9c785b764a2ff8c52",
      "version": 53
    }
  },
  "version": 544,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d373733613265363163323430343165/66.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d62326636613033616166343434653537.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
