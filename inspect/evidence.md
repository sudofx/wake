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
  "generated_at": "2026-10-24T11:32:18.155874+00:00",
  "head": "snapshot:43b1751f248f61a5897841fffec5233a15de5b24225908325a85ebf11c3c78cd",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T11:20:07.678577+00:00",
      "head": "adf5536a5fdd3d09738aa0de78f2b899414c55b320ad0b486fa7c513925ed561",
      "node": "100.wake",
      "snapshot_digest": "ec21ced5c5d4830b216ff5d7e6e17970bb9530968f56a0ad0f6c83b8efa84c8a",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-24T11:18:48.371168+00:00",
      "head": "1eea5c148a377054bc474943dfdcaf7fdc3e2f0cf68e707669dc8237cffbb5dd",
      "node": "101.wake",
      "snapshot_digest": "b4fb5ae33c1ae3d815614f6cab01cfecf560f0ce5d3ff2a178ae1c77220feaae",
      "version": 35
    },
    "102.wake": {
      "generated": "2026-10-24T11:12:10.202141+00:00",
      "head": "af21dde59ce1c3e114b4843829826b14704eb437ebe64b890ca86bc55394eebc",
      "node": "102.wake",
      "snapshot_digest": "f6e0491538c323e207ad95fb3d9f3181cca0c326837221be01e6028072c85a15",
      "version": 42
    },
    "103.wake": {
      "generated": "2026-10-24T11:12:53.045755+00:00",
      "head": "1357d4da3cd039aad79761b0ed27ae505c4fc97216adab044b4ec7ad4543e8b6",
      "node": "103.wake",
      "snapshot_digest": "878e29ef5c1e25cfdef6cece38fe923108ebe91e8d27eca8ad04568bc968344f",
      "version": 32
    },
    "200.wake": {
      "generated": "2026-10-24T11:11:38.397003+00:00",
      "head": "b594bc879a66b83f1bc89768853bd787b0438a150f73bdef0aee64c908dd0c95",
      "node": "200.wake",
      "snapshot_digest": "d9012c0bf3db5ec7a7d6eef783132418b50667345e83639c01d046cfd5694b9e",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-24T11:16:06.652168+00:00",
      "head": "e2562cf6b8214efa8af46defa404c58bab47e91a5b74983d753fd0d9b36f67f5",
      "node": "201.wake",
      "snapshot_digest": "af131e3de600b8a0627f9f723353e01366172b655a60c7bfa74604f4194f6606",
      "version": 30
    },
    "202.wake": {
      "generated": "2026-10-24T11:29:20.034138+00:00",
      "head": "407e9dd39b3f50027e341bc418817534e9e085a3c50e3ffafbd17286046dce8d",
      "node": "202.wake",
      "snapshot_digest": "c6ac89ff4845df64c20f3ddf26961f4e4c93ff28d65b6bf0a873cd239a138be3",
      "version": 42
    },
    "203.wake": {
      "generated": "2026-10-24T11:13:54.054449+00:00",
      "head": "192b832dd0a4d2838c4c07dc4278de0b24ac42033b4179178c4e75dd21f928da",
      "node": "203.wake",
      "snapshot_digest": "3d4b1d6d0849f78c3455527fd8d850ddac6c03cd5063e5d8dd961996e4814173",
      "version": 22
    },
    "300.wake": {
      "generated": "2026-10-24T11:27:28.466397+00:00",
      "head": "a372f8f9404910930259d5908281dd884bc5f56473c4a767418e1eb1f0a746e2",
      "node": "300.wake",
      "snapshot_digest": "c67afeee49afe4126404cab078f2899f1f3cb8a56eff439a3869ee53b34f9b9a",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T11:32:18.155874+00:00",
      "head": "33fea9672b9e92273953ff06f460ff0571d4a2b1e3c57b017764dc30015ba2a5",
      "node": "301.wake",
      "snapshot_digest": "fd7b32bb3008fd8564a976d283f6399856e4272b581333d69eb5241d49809b47",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T11:23:16.792333+00:00",
      "head": "cb930eb8f36256da73e76c5d2efb6c481204e5f69c4e29607f1c6ecc3725ad79",
      "node": "302.wake",
      "snapshot_digest": "4fcde040a728e1943068484edc134d917833a5cec7744e5e39975b36682be05a",
      "version": 23
    },
    "303.wake": {
      "generated": "2026-10-24T11:27:37.889489+00:00",
      "head": "029f9c57aff374af278a80ce1fc436fced6ba719e8489ee687327e9202b8f666",
      "node": "303.wake",
      "snapshot_digest": "bc1169fef47e46d975e712692b5a75f4fc83a446db229e5297ee729a84da9b5a",
      "version": 42
    }
  },
  "version": 380,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d386336363666303564373238343761/61.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d656331386234343631303834343732/38.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d636f6e74696e2d72/61742d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
