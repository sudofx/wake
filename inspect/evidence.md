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
  "generated_at": "2026-10-24T20:14:58.695426+00:00",
  "head": "snapshot:c4bf88daa6575d08e85d25f3a8f617a45d719ba101e8d54437b42bf92da1fdbf",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T20:11:47.663560+00:00",
      "head": "525b957d00ff07dfe7aa96897d31ecf7620bab9b32c747cb9d4db856a895fe85",
      "node": "100.wake",
      "snapshot_digest": "0f1568c56abd6d4888a3d609873dfdc36701a8d49809ab3434a150102183a825",
      "version": 24
    },
    "101.wake": {
      "generated": "2026-10-24T20:14:58.695426+00:00",
      "head": "24c2bf2dd9ca725a5a27c85f302428b70616111afd3d7ea23f6a9281edced396",
      "node": "101.wake",
      "snapshot_digest": "47d2c8b79d616c913bd0ba1b003f95c77a23552225cb05e38d7fc4647a3151a1",
      "version": 39
    },
    "102.wake": {
      "generated": "2026-10-24T19:46:57.356565+00:00",
      "head": "c654608a8cc5a04f6b7bd763f0bcad11e159ae10c3098d9420f313d2625a294b",
      "node": "102.wake",
      "snapshot_digest": "ed639781a7c5bb8f6700cba5b5e4041e38f3de78fbaaeba8d510c67ee8f45da8",
      "version": 51
    },
    "103.wake": {
      "generated": "2026-10-24T19:58:48.332997+00:00",
      "head": "d6c159496cbac8b17568704c3a40ee6d086b747505d76882a6cd38b7511cc12b",
      "node": "103.wake",
      "snapshot_digest": "704ca9bc062f8450f1a0f438cc9ea697d49c4abea3d3a3686319defed1960cf0",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T19:57:21.490776+00:00",
      "head": "1a7574c3e7c86a45c41dee4287e2e435dcd070dd2ef8c0b84b2b39f20b993246",
      "node": "200.wake",
      "snapshot_digest": "2eb6e0ef643bf60a0b924840f2e016b730668a78f0eae7a37d9e8ecab41af77a",
      "version": 29
    },
    "201.wake": {
      "generated": "2026-10-24T19:56:14.493690+00:00",
      "head": "a5cf3002725720c0c255498035bf39776a710274bbea77cd03c3dc2a59fbe551",
      "node": "201.wake",
      "snapshot_digest": "a325017a47b4f010c20544cdfde398d880ca0cc82a8d2caf6fe92b52bc95006f",
      "version": 35
    },
    "202.wake": {
      "generated": "2026-10-24T19:58:05.816840+00:00",
      "head": "9ab8adffe4320cf35a9319c1261ecfb8d78153c8112ff760a6495a1338c16cc6",
      "node": "202.wake",
      "snapshot_digest": "5fb78599915ecd103af12b1b4a715173b751462bbf493a852bab5cb7d5daf380",
      "version": 48
    },
    "203.wake": {
      "generated": "2026-10-24T19:55:36.678944+00:00",
      "head": "0565f13ae799c21e9947f83d58131b0d9f18500b057b2833969d89b703e3e6ab",
      "node": "203.wake",
      "snapshot_digest": "a1f186427d9541a94af60f5641a0ebb64949444e80970aca6afff5ae33b11a03",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-24T19:51:06.696818+00:00",
      "head": "94b5ec00ea8d75cc9b1a71f2fb948a4ac07817a9e883b1fad2547146037747bc",
      "node": "300.wake",
      "snapshot_digest": "88db4d74e84bc6d6227a6cb7d5d7b98a6a63bd7de4cffe32a8bb0405bb8bc63a",
      "version": 31
    },
    "301.wake": {
      "generated": "2026-10-24T19:50:41.550704+00:00",
      "head": "cbf5e9522eb5e2ca9061cb65a37f7650c0497aa592161de69480af0b27585f9d",
      "node": "301.wake",
      "snapshot_digest": "f5301b86be239bc4065aa55af20e43ef941757189138e6ef9cd55aca16dda1ac",
      "version": 49
    },
    "302.wake": {
      "generated": "2026-10-24T19:52:30.686832+00:00",
      "head": "6724d005f84adba1cfda3836de4ee1df278ef6e4f1df97efdc226b0f4560d910",
      "node": "302.wake",
      "snapshot_digest": "d78880b65ae790a43bb2b5f2fac495122cfd85069d0c6931d6bf5143348b95b6",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-24T19:54:49.822719+00:00",
      "head": "0eda4626f170d0606a77e4a267e2fcc4f7822b7d7b71fd32b8a12e8a8aec8764",
      "node": "303.wake",
      "snapshot_digest": "2ce38eb593c3bd836b76b0c910ebbd5b5e4a8b86ccab00f6d8e1369ceea22fd5",
      "version": 47
    }
  },
  "version": 445,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d396236353239373338313630343230/35.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d616339316330646633316631346433/31.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e6f7465626f6f6b2d726561736f6e696e672d6c696d/6974732d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
