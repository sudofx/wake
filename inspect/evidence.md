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
  "generated_at": "2026-10-25T21:24:46.676812+00:00",
  "head": "snapshot:e7d9d7dde8f7195cae0696654487c445740b4f85a84c5feb6736f489fe11ef2a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T21:24:46.676812+00:00",
      "head": "ca798d9e45834ee5c1c565e348b3d37f78ef4934a3a0357729e1d126f4e6a7f9",
      "node": "100.wake",
      "snapshot_digest": "74c944b7c275ac6d69415eccf180347d3f66a6f0c9c8ce0769729752e5a55a7e",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T21:19:39.854575+00:00",
      "head": "cc573b0e48160490e833c7ef87810cd3a49b0903015eaf381cf4087ebd483705",
      "node": "101.wake",
      "snapshot_digest": "59668832c66b3f4690435d4bda575e7d3b64cf50f002f1103567bea7d5c21149",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T21:08:28.752175+00:00",
      "head": "c85220a39b4f0e4e53b4f78933ce2fce184667a32d74dbe9faee3aecc260597a",
      "node": "102.wake",
      "snapshot_digest": "267ac45b2c50d8cfb07d6d0216b94aa8ee1f871eebeae503e14adeac47ed15d5",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T21:06:33.402360+00:00",
      "head": "fcb66f26ec05d85dff5ee1b63bbe4414f0c5e7db3d6b5acd3544dc7dbfc5c893",
      "node": "103.wake",
      "snapshot_digest": "a75ea44b2aa0c2fe4de9d9e2ab12bab8c829f00290aaa2b03997905cf35d8b43",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T21:04:46.942607+00:00",
      "head": "977a2e4264b253ef1d966e9072c19ed076eda20b44dd16ee925f9935919f9607",
      "node": "200.wake",
      "snapshot_digest": "6257c87c72f28d172bda57f36e01ee3894952e925983acd6a7298f16abf4e4f2",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T21:18:09.009789+00:00",
      "head": "53590038e9f06973c1125de67f71d0873080dc5c021e23baa796ee05d9147804",
      "node": "201.wake",
      "snapshot_digest": "eb4dd3d10b63949f65e2ad60bf6239abf59c98498f9aa6ee25ece484c86f1e38",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T20:17:35.928362+00:00",
      "head": "950b13a1f58363546391c599f3cc4a40582771a239698560b8fd3d517793dae1",
      "node": "202.wake",
      "snapshot_digest": "00eb45878f0a39f3d0a7c7e609d0fd79e28be301cc9904e943b1dbf01e1809d5",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T21:01:23.472032+00:00",
      "head": "355cc6aa7cf46edac6bf06189c5719dab964dc5d8c80feb47bfb67ee4a61b062",
      "node": "203.wake",
      "snapshot_digest": "77e6e64369beb71e32bba7dcab718098eca3b9c15b1fd095a0490885c4ec9fd5",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T21:02:28.068407+00:00",
      "head": "14211a1185db1bf71d0440c7e2317c0ce49ccf5385702c373a24abcc2bf3c6af",
      "node": "300.wake",
      "snapshot_digest": "089b0ddf9cbf5695208e241cda8192430648c071cf103d139fb9ae4d70f0404b",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T20:59:36.837712+00:00",
      "head": "7c926c0ac41bc3e1baf12aa50521a66fa34191fbf9c4b7a631133f645724fbe2",
      "node": "301.wake",
      "snapshot_digest": "3248a6cb66f05b3fbdc6515bb967ec545cc366c73aebab50222f2b5a623315c1",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T21:14:40.535939+00:00",
      "head": "3ec2a19f597172208defdae8a8f0a166834b8db350384204d75a52d9c9afc35c",
      "node": "302.wake",
      "snapshot_digest": "855e079933f4ddb2e204fa0dfe631914a5880a23740ad70334bb3a833eac0b11",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T21:11:10.886394+00:00",
      "head": "ea03a54be192a50ca1c2c427aa2b1d83ad1456e6bf033a04a7aafcecd160f498",
      "node": "303.wake",
      "snapshot_digest": "3f02a8ab0fb00b423fe809d6d87ddfff6ad8ecfcf3913da3c665f5d137775c3d",
      "version": 51
    }
  },
  "version": 510,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d613966346535343038643935343239/61.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d38396336613030613333633334386637.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
