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
  "generated_at": "2026-10-25T00:44:28.278218+00:00",
  "head": "snapshot:d8efcf4d62f14c165202ec92ee4b1baacde61073ee41c48f366e845c3695f320",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T00:44:28.278218+00:00",
      "head": "84b3158a877b8038576e1f78855dbc43b43787a387ec6fb1cb7167b6f564d056",
      "node": "100.wake",
      "snapshot_digest": "1f0361460cd627281b97b8dcc2b2477b2dfe00e322fb9c31bde0d6a8bdc4ab29",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T00:16:43.081811+00:00",
      "head": "10cdf5e16ed62b1db2bb7d632c2ad0b457df590b988a11124b43492126cdf306",
      "node": "101.wake",
      "snapshot_digest": "ecfb17a3343693c75def7b24ba1b8b773762dd1c7b448f42c2fdbdba6a947e3b",
      "version": 41
    },
    "102.wake": {
      "generated": "2026-10-25T00:08:14.342641+00:00",
      "head": "ca5b823fd6bc0455eb3bc48fb5775e870948e1b29c18957b715a7df850c6fdc5",
      "node": "102.wake",
      "snapshot_digest": "0ffed47677a680136d609d3d85d9878cce62ede9f93ca2c0987c71a118c1ffc7",
      "version": 53
    },
    "103.wake": {
      "generated": "2026-10-25T00:16:24.502713+00:00",
      "head": "937be7d48aa4047823e1e4469bdb1da3fa79679fb08dc3be1b5eeb09271b6353",
      "node": "103.wake",
      "snapshot_digest": "a3751be04b19345734065145ad0de4c6970175bf13266b5c5d29406cac597393",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-25T00:13:23.990881+00:00",
      "head": "7d91b4fec4dc68f1fb0a66673c5479a6487e762fb5de683077a285120592e3db",
      "node": "200.wake",
      "snapshot_digest": "ac804914ee87fc39c07e67845ac092a8ac948bc6268dfac745c8c85b2b98cd4f",
      "version": 33
    },
    "201.wake": {
      "generated": "2026-10-25T00:13:46.170481+00:00",
      "head": "e48d8d1be5ad439abb84c0599d3fb9a46ba69733a48350efbbc63788b04d1d37",
      "node": "201.wake",
      "snapshot_digest": "d42c4252da1d5648500777adb3a902f8f36cf9687e44def959abf9d7315a3865",
      "version": 37
    },
    "202.wake": {
      "generated": "2026-10-25T00:16:09.577897+00:00",
      "head": "10005596373887a63511fd5584e786314794e019e32debd10287524040f734f1",
      "node": "202.wake",
      "snapshot_digest": "1675d894259b52b35c3a76a617d25b40853cfee534f5292d98d7fc306d29c0b1",
      "version": 52
    },
    "203.wake": {
      "generated": "2026-10-25T00:11:21.237687+00:00",
      "head": "7cab2bed8d344be5743e78ed8c5af8d1f7c54dc4f49c3dee106de40d23b1ce01",
      "node": "203.wake",
      "snapshot_digest": "506bb384ee21193ce27a741aff559351a704e6c641004ef89c69a2225f9ee051",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-25T00:14:45.572623+00:00",
      "head": "23afa54eabf94bcda6c9f33bd12f80fe1f86e720a2edcfa0f287f28be459d47a",
      "node": "300.wake",
      "snapshot_digest": "1dcb74425552f25d609ac5aca2e3cc7f8cdcdeb5dc9f83e3e4ef2605b6fc3bf0",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T00:06:55.198216+00:00",
      "head": "68b8ad788b26850d495da541a966b8c99859ac10e5626817514f40e7a491c448",
      "node": "301.wake",
      "snapshot_digest": "c6b72b87f94ebe437667a0217c7fbd119cb79571993bad126605db5b243fc128",
      "version": 54
    },
    "302.wake": {
      "generated": "2026-10-25T00:09:32.681620+00:00",
      "head": "520368b1901b0bda851a25ac337150075d8ef3e2b3003428e7d1ec0624051c71",
      "node": "302.wake",
      "snapshot_digest": "7a3205f861e70c837912abc454bcdde374f5b813434ebf3c807f6ddc02ef2608",
      "version": 32
    },
    "303.wake": {
      "generated": "2026-10-25T00:18:19.521264+00:00",
      "head": "4e4d4879afa36bd9fdb6e675c820715a9529d239d34e78d91e870068e69602b5",
      "node": "303.wake",
      "snapshot_digest": "97b21191b726e712ed17136e9f4713468f983ea33e8550f2d71a6337f3609ed2",
      "version": 50
    }
  },
  "version": 478,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3130302e77616b653a3a736f757263652d646166373534353437666437343262/31.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d31393432333935303462366134666466.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
