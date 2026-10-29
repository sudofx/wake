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
  "generated_at": "2026-10-29T16:22:36.888123+00:00",
  "head": "snapshot:cf9ea817646448d5458de104c854e0207e5324335b9e0845a3665fe86c5d4322",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T16:00:23.127664+00:00",
      "head": "04e465934bb0d73807947476dbbe90e614f2324bc7eef945bf480bf8189f06c7",
      "node": "100.wake",
      "snapshot_digest": "87dee9ffe5fb626071e8547935a95ab3fc75a9e2c553e14f95354f76cb20603a",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T16:01:31.105737+00:00",
      "head": "0f0dd94a2f852e6840cb1139f89376fafcdd9f2dc79b756398253388444c9985",
      "node": "101.wake",
      "snapshot_digest": "b40923f25b91293a9308249c2141bb3e96669a19cb12cd60f8ed56b805ea3cc4",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T15:51:45.773735+00:00",
      "head": "7c5e2cf595ffb7c20de8b85abddb49ed3adc9e05fe2e663583f99008db9262cc",
      "node": "102.wake",
      "snapshot_digest": "8b6cfcaef226b5421ed7ca8f072dd3ebf1c111d5bdfc19ff8eefe6d8655b07bc",
      "version": 18
    },
    "103.wake": {
      "generated": "2026-10-29T16:11:12.976375+00:00",
      "head": "4f1dbb5dce649e3a2f18d48475271aaf7e5dab75872c86de32f8b9cfb68929fe",
      "node": "103.wake",
      "snapshot_digest": "84f9df2196d690da8f771105084791b2e43675b79bf971b689fcffab0016ca14",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-29T16:14:32.894544+00:00",
      "head": "84a5067d17cc09e93a502914450f647cebb7d1ea93caa6c600ac423bf64e283c",
      "node": "200.wake",
      "snapshot_digest": "a706fb4834b2aac4a8f1fe1877a771b7a76ff40bebb6cad7d5f21f23395a86d6",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T16:09:24.963008+00:00",
      "head": "00cef24e1def6dfad080276f8e49e69f7a06ea3718aaf85ed93bb4cc409a66b9",
      "node": "201.wake",
      "snapshot_digest": "d2d0835e5a9ebdf3bace1f1e9d3240142f927f341934808e2a6f4782ec7c26e5",
      "version": 24
    },
    "202.wake": {
      "generated": "2026-10-29T15:51:42.935133+00:00",
      "head": "31644d297780fa618582adfa03283cd22eaf102f4472afc36c2cfc20d13748fa",
      "node": "202.wake",
      "snapshot_digest": "0feca6d0fdc23bcab5127727396c1a5cc29a4ff6aff01c8a6a78f20c99bddcc4",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T16:22:36.888123+00:00",
      "head": "1581415233824b60b639d062812585313e2619cb5b7c1ce631e0feb2dbe067dd",
      "node": "203.wake",
      "snapshot_digest": "7dd82855f5eb46d11ae7a5b38fa60f0ceb764e3507cf0738ed35cb6ce8024787",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-29T15:52:05.188013+00:00",
      "head": "50d337062294f4bd789cd63cf6c7149d9926424d7585ddf98b5b6ea05e62b187",
      "node": "300.wake",
      "snapshot_digest": "aa279921e87049f694d50bc8702d0e9e1e55f8cdce9a24c6fb33e5a1300639d6",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T15:51:59.671648+00:00",
      "head": "28cd33ad3387a6b7a2f42fedf46e4f4f352dabba00dd26a96f1ab7337eab99cd",
      "node": "301.wake",
      "snapshot_digest": "969af6fde8541bacf237d8f216481b37e3b26755cd25326d58d480c3ab6db2ae",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T16:16:28.602585+00:00",
      "head": "f7289faacbbfe0b868b5df24b3d4c4642eac61241280aff8291381d2111e43db",
      "node": "302.wake",
      "snapshot_digest": "bd4c34314a10b6668c149f7c58aefbfccaae7e27c3788a6c7f00c1542c9dd038",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T16:06:02.832063+00:00",
      "head": "c93eb5500ede90bedd9846607e9d29f061a5539a4e2d8687e9f98a2dd8bf9144",
      "node": "303.wake",
      "snapshot_digest": "857f3b88e48e84797b79719d99e7e37f37544229d3abae5adec74e1ccd7aa295",
      "version": 24
    }
  },
  "version": 297,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d63363839393939373838376434633365.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34646161356432643037316334316337.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d726573706f6e7369/62696c6974792d666f726d6174696f6e2d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
