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
  "generated_at": "2026-10-25T17:24:44.072887+00:00",
  "head": "snapshot:c06e9b5fd86c710d4c2463b124991d8fb4497de8f4c2c7c421b251363bb9a189",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T17:14:05.129231+00:00",
      "head": "cde237d48251b3ed5be8dcd2182d40bc0a4fc2585315db836acbeed4dfc59770",
      "node": "100.wake",
      "snapshot_digest": "bfd76e98626624d9e547ae309821e39aa0d21bf1d956b52d1c0d2d46798e37a9",
      "version": 27
    },
    "101.wake": {
      "generated": "2026-10-25T17:14:18.516243+00:00",
      "head": "2ab47fac57038502887ee2c3d6ba0a727a3c485dbe3a6fc6ef18658d5367c08c",
      "node": "101.wake",
      "snapshot_digest": "560dfe3b335226e5445b89ad795baddd38e3729ee336a6b3fa9417932337eed9",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T15:53:15.368140+00:00",
      "head": "4af706a85578fb1724fedc89a8ce09df402b1fe8b57cd5c408cd06b7258d52b0",
      "node": "102.wake",
      "snapshot_digest": "e59911c9ebe726246c9329e1a181af1731f41ebd284b20bf725290cc48e279db",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T17:23:41.244236+00:00",
      "head": "928f4fe3acfeab79c42014d00c7b4d1dc948af849774b0bdeea2a88080bf694a",
      "node": "103.wake",
      "snapshot_digest": "83b28605f4a50334c340f885a45878ffaefcbab0e2b69f2a52818e7d2d1f23d3",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T17:19:03.920988+00:00",
      "head": "d2e72f9fb699714bfafdee373e96cc22d16c10439f7d23af2923789b468e6588",
      "node": "200.wake",
      "snapshot_digest": "07eb815e8487c579bc3a8a5f77e3a2ad2f0804c1bc113c7e4a0c5186eae78f6f",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T17:16:52.433192+00:00",
      "head": "f2d3907ac62ef1dd6f934502bf3fd8b37d632f3caa00d6f789e832a1d835c79c",
      "node": "201.wake",
      "snapshot_digest": "d091657ee8880eb13fa2ef3ffcb0b26897e4cee86858867b8b6ada7a8cb1aea2",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T17:20:55.733862+00:00",
      "head": "3acb2c878d28836a78f0b306eaab47ba22d4feb1d458312c3bd8c5519423e8c0",
      "node": "202.wake",
      "snapshot_digest": "5ea2f94fe2c14dac172fc645cb4fc58a230319406bef12bec07fc15241b77d2a",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T17:22:43.173803+00:00",
      "head": "0d3a037bdd494dfe7c7f01e46b99c7be6c207712ff5334fd939f76772f2eb9db",
      "node": "203.wake",
      "snapshot_digest": "d267f7c72a30719779c4d69bc7998eb51fece5ba66d77fea0f46ae562d4356d3",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T17:24:44.072887+00:00",
      "head": "7f7f34b8d427d3d3dad4c6a41a7311b0251a3bd97a10605894f210bb6ae4facd",
      "node": "300.wake",
      "snapshot_digest": "c684b863fc40222b949e9838472c3bbd468f5fb19baf34d16e0bda5474ae7a80",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T17:20:10.891973+00:00",
      "head": "4cb7e39356d0ce0e2c477f43e0f9b941de2bc5022890d1a468103091b0bc0536",
      "node": "301.wake",
      "snapshot_digest": "9e1fd54f7cdc6c73875f5fb6e6f9515c40bd9b084660d40156c54085c2c77703",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T17:05:09.545003+00:00",
      "head": "a6d17b5db534b4d95a22f61778e6b2c9b8879ca2a7c75db16409332f4d53e956",
      "node": "302.wake",
      "snapshot_digest": "82741f4a81f9ce7fa7363768b8feec30930d67e2ce78ffb0a974099de7884971",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T17:17:06.359524+00:00",
      "head": "207cc98ab2e16ce168e512552a086d8c659b9d380d85a3d3be0edc615e7f35b6",
      "node": "303.wake",
      "snapshot_digest": "e176528e7da4edee309cb8b806fd2a10d72019e99832dadb2fef516a5659fdb9",
      "version": 51
    }
  },
  "version": 509,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d33663863663130303136303034373236.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36396665333762333362356634353231.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
