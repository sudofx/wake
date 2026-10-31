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
  "generated_at": "2026-10-31T08:46:24.422391+00:00",
  "head": "snapshot:3a2affdba5ec397966b5258127aba9a21e5f1640b20af7e845b04282069c6e5c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T08:41:21.330250+00:00",
      "head": "e2cbea0f9f3a60347fe9b3b77c8cfefd719d897911e33a78d42d1e79345c9313",
      "node": "100.wake",
      "snapshot_digest": "5df05fcc281993358a0a72be013e852c488cf9cab32273dc9bb54a102e127ce9",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T07:07:08.266448+00:00",
      "head": "cc66f243be58085f543bb7752b89c51b602a25996efc9122ec6d22c0c61af8d2",
      "node": "101.wake",
      "snapshot_digest": "f44d16f03728b9d830f09a394c0227eabf0bab3056789c12bbc5a267f7ccc34a",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T07:07:12.778904+00:00",
      "head": "5c45071edd74df3d12046d9837cfb532093797ccea4d232697c2d6a360d27a4a",
      "node": "102.wake",
      "snapshot_digest": "fd26c81c9f66a7c769daf0d8d741725b27c91efd4d4bbc33c213b1ff61dfd5f6",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T07:07:18.257158+00:00",
      "head": "ba86b8b534cdf68f32db3725587ffd5c7f82576a8305f29d07ebd9a2807d59d7",
      "node": "103.wake",
      "snapshot_digest": "6ed3bc5392786e00b07f29512ac9014c396449609d026fff93109eb3c44839ee",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T07:07:25.720525+00:00",
      "head": "402d217525c9bb76a3d3bde9ea6197e5363396d201279953f3191f02ca2ae495",
      "node": "200.wake",
      "snapshot_digest": "2801927789e05f67e9f992acef8e518f15d27687f5e530662223584a58070eeb",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T08:43:02.457929+00:00",
      "head": "176a9e2666f520e35e70369a0bb0d6c8337374b701ac7b55433b2f0a552366aa",
      "node": "201.wake",
      "snapshot_digest": "d695c72a79c357e79773a3080d41ba055f4127b4e4ea0f3b1cbc1029d0912c3f",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T07:07:07.300261+00:00",
      "head": "11b1eeac5523eea4a92ff573eccc369ca218a19780c5c631ecd74a7aededbc30",
      "node": "202.wake",
      "snapshot_digest": "a49996449a071d8c922f1b1ef82679a16a3e4f87d3b7f167e2b8f8ceef09bac0",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T07:07:12.435361+00:00",
      "head": "d8e4bc5382c5cff17c7523149d5ab020f952140b682311492f134ab0fb4ba2f3",
      "node": "203.wake",
      "snapshot_digest": "9a6af1b1ea998d7efee586657004bc34248773eac4d8443f5f44d674bc7bbdf3",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T07:07:23.100465+00:00",
      "head": "4ecf5d5ade0a5733c2d8105f604e6e916e1a5402ddb6c883d01f828e4fa180ca",
      "node": "300.wake",
      "snapshot_digest": "dbfdebced6a58b8ec4e3aacccf6b8d3d98fd3b7ad393d13c008e26a015b4f923",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T08:46:24.422391+00:00",
      "head": "88c6319e9d7e6f8b01c7b0e426bfe24aa04a22017b9918f6d72ad56d78db416f",
      "node": "301.wake",
      "snapshot_digest": "dc3cb0e54dcc8aa71a43755c57de16ccf8f201d3b9f8562cd8b4ffc0ae21e667",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T08:44:41.915033+00:00",
      "head": "d605d15866d61dffc635c2802081eabdf6826a5619dadfa3d5b94e982edafa37",
      "node": "302.wake",
      "snapshot_digest": "2ffba884d92d39767d778559af3189c3b6a35c2d01fa1dbe8f0beb19b1f01d58",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T07:07:14.231532+00:00",
      "head": "d60a54915254b863ac73b11cd8f05a7aa56aac7a1cd013c294b667ac1fdb206b",
      "node": "303.wake",
      "snapshot_digest": "ba59cf50eecfddab370ebdfa587a32a693d958e815d22256ff0820c21452b487",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d30386261653565373666376234393365.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d39303736663831633565653934373133.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
