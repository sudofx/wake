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
  "generated_at": "2026-10-24T07:02:56.007837+00:00",
  "head": "snapshot:beb704b5f956305ac21861a2abfef051411e881601cc65314d5ae4d4bc5f737b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T06:56:50.825192+00:00",
      "head": "597e173b0a397e29dbccb2f6c9ab2dfdbf414d6cb686519a4d4aaa16146d9bd1",
      "node": "100.wake",
      "snapshot_digest": "59c9f7a4a6549adcad5674f0a8dbe9dc6e699ee5bf8f2ee857a6a122b7022d79",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-24T07:02:28.783548+00:00",
      "head": "f6c0bab9d3122ba5e57987a969109cfacb7199407dd8d8f84196040c5d07c947",
      "node": "101.wake",
      "snapshot_digest": "8bae1955d0e0241ba70b2aa3adc253960d18fe88a70fd16a479aa9ea12be5138",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-24T07:01:23.845679+00:00",
      "head": "8e3c5ca4bb0d5515997c453b411b81165d2129268a9d390851cda631e1de8e57",
      "node": "102.wake",
      "snapshot_digest": "e0d03d05b1bd2e2ab6c398864003095b91c3ef3844477ca3f5ddf505a2bd86fb",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-24T07:02:49.566377+00:00",
      "head": "6a6a8b13b72dce4c9617e4cd225a3efbc719ffb704fa095df87eef2ee9c55828",
      "node": "103.wake",
      "snapshot_digest": "19d4bc33d101fcb5b9594bfb3abebbc796c7b4c3342e1b16353f64509b36e1b6",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-24T07:02:36.266774+00:00",
      "head": "c6e612ae95c45cdb3d7a36c18b3872f64858ec9c732de26d58291362dec79e43",
      "node": "200.wake",
      "snapshot_digest": "eb97aef465a6c15c41c2096aae8ba445bdbce28a1a98b94ab58fcb067125539b",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T07:02:10.053133+00:00",
      "head": "54196f5aad0d37d89bf11c883947890386f135baf16f68a1753f07033d6342ed",
      "node": "201.wake",
      "snapshot_digest": "11d181e955d27ba93887de765e11871673e97bb652efb8e5e7f377f281f0a75e",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-24T07:02:43.144756+00:00",
      "head": "cb2fd9cc89d24242b5288b34432599a20f451ecd4101626e95645df04b445f1e",
      "node": "202.wake",
      "snapshot_digest": "8294001d1bd1c3e113b933ab0ff29a0c609241c23db3f59b9292431e20725b73",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-24T07:02:56.007837+00:00",
      "head": "c24c07edddc3beaac9a6fadbab1db9aa72df5672c018ddf9bb7600136f12e5cb",
      "node": "203.wake",
      "snapshot_digest": "7e47093ef479fb375f5e3b52ef802d3f61ee446dac1f8f7434adcc55500de173",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-24T04:54:48.287939+00:00",
      "head": "8c2952a63312d98f514072b874c19c2a73f8f3b8e60b6a57580d5e2d7f5ed619",
      "node": "300.wake",
      "snapshot_digest": "c210e9c695370c1059b1da6a23f8121402533cc425d0101f179b94aca548532a",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-24T07:01:04.672541+00:00",
      "head": "d358f33a84152b66df12d2b9bfce12dde8c78c1ac6041359cb8cb75b32f7e6dc",
      "node": "301.wake",
      "snapshot_digest": "0f4fce159b02ff25cc6967f724a69977f1a1b94a9e56d50fc62d323dfe875e39",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T07:01:55.767937+00:00",
      "head": "5eac6f53b0d319dcf8d5e8bf49e6520d6828d60e931699cf3434649c2a17b821",
      "node": "302.wake",
      "snapshot_digest": "b3265e11a149d2f1a0e5f3423d74fefa4ac52a05a2e9596a5526ab3ef91dd2ad",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-24T07:02:22.583783+00:00",
      "head": "1cd661c22ea932ea5ea2ff9f2ca1f3c7ec15c00126fb68193643669bde3b1d8a",
      "node": "303.wake",
      "snapshot_digest": "965b33b619eb0c58575c361086378d09839f99b1138276c7732cc74fe48ce401",
      "version": 36
    }
  },
  "version": 337,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d61323735656430613166386534646434.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d37613436616330303839383134633631.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
