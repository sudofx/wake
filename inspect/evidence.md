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
  "generated_at": "2026-10-31T07:38:52.791268+00:00",
  "head": "snapshot:3ac03f7e5ae8657126d42a0afde4e30f607db79cead45131a0f89e004b8f9612",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T07:37:14.738496+00:00",
      "head": "93c2b27faa0b3ff43fd51d01e09c129196f99dfb3589b855d9225ad0f901bdb4",
      "node": "100.wake",
      "snapshot_digest": "e53ec2d1554f47ded5ece01b2eb71ee3e19d805f8ef80a746d0935d6990e9470",
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
      "generated": "2026-10-31T07:38:52.791268+00:00",
      "head": "1699480992ca976e7b418f0f141383038867fe2bb096fa479ed7e013c931e788",
      "node": "201.wake",
      "snapshot_digest": "cf6353a0adf2386ab003e66af3d0af05500375aef37cbf9780a30da810e9b258",
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
      "generated": "2026-10-31T07:33:51.005404+00:00",
      "head": "a9b67b4a4544486a5d143694eb42f92d2dffa7e72f0f2df435a015dcbe009245",
      "node": "301.wake",
      "snapshot_digest": "0f0092e42704fbf520e95123e14d59c93d8c46f76976680c8971a6477c17536a",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T07:35:31.755497+00:00",
      "head": "f621665d2e6dd2a2aec8c9f52f5400ab229f2e92fc727c67b2c727ac559d01e1",
      "node": "302.wake",
      "snapshot_digest": "dd41715a9904b1a38d7f4340e9799c4c9802c9216e7ae38bcd846ecb3ce5f38f",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61643561636333323966383834393362.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34353136346332643166316434666635.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
