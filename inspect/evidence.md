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
  "generated_at": "2026-10-23T22:51:36.023129+00:00",
  "head": "snapshot:583a2db938dd60bbd533fb50ed5ccd95774e5a5280f5dd3b578b8227d6936ed0",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T22:42:03.382688+00:00",
      "head": "dd9ac8de9ad02af859324ce366e2d9422a32c1c52220237b291c122723104cec",
      "node": "100.wake",
      "snapshot_digest": "a07e13b3d782ebd8a46f60d7971483f53cb67be1546b96c3c4063fe279e24e13",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T22:51:28.863848+00:00",
      "head": "52e1b694d715ecc7cc886daca488bfaf0bdb0d7c03fd61150aae2fe66f756f91",
      "node": "101.wake",
      "snapshot_digest": "12348f51d1a53d2497f0890786b9d868e10a9026ed56e7ba9a45f0f99d60be65",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T22:50:24.695542+00:00",
      "head": "b6bf569bb20a2307abad4c5c86182c438428c4fceffc6c05927dfb665ffab678",
      "node": "102.wake",
      "snapshot_digest": "f2171fb57c3ec470a44c23e6a47625fa874601a2d140497201b9060b3e05760b",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T22:50:59.269856+00:00",
      "head": "c2012173514a742ae63175d5f377ca02bcd0b8224b9c001e7691bb124b08fda4",
      "node": "103.wake",
      "snapshot_digest": "63f91066f62caee60bd6ce9585f457c9a641a824629be0d8b858f7e6b6b8a3f4",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T22:50:31.217187+00:00",
      "head": "789516d7ef76636425a5545729a9471076271d3ef653bfbeabf194fd176891b2",
      "node": "200.wake",
      "snapshot_digest": "cba651ce5899bbb7a30d3ba8f66e22a800a6014d408c1877ef24a1734b39597e",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T22:51:36.023129+00:00",
      "head": "24df5f7565283de67ea3fd975d5a7130abeca6def5acf4423a9478e7e3b03a41",
      "node": "201.wake",
      "snapshot_digest": "4931d46d7e168a30f77bef57c59804addbc5dbd87ec380a8355cd6ee355c6f75",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T22:51:06.845486+00:00",
      "head": "303cf435c9829b2e2eff7889c122577be8eaa34ed6c9a3cd0cf41ea778a0e516",
      "node": "202.wake",
      "snapshot_digest": "052c3a017cecb79fdd713b6dc49ec1fcfa536d7abf39a27c72db9c94d3b77d33",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T22:50:03.945283+00:00",
      "head": "5adb2eb5dce51aab267f15446aa92821b7010b98fed8448c31f52df7e89efd5c",
      "node": "203.wake",
      "snapshot_digest": "4c062c80b9fcfd5cb2ca32e275590be0655eb9275a7adc4b45ccaa475ba663ef",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T22:51:13.836307+00:00",
      "head": "4aa87e19926cb26e477595c12e0d508706bf7298d5f3ca591daebc4dca1e4d29",
      "node": "300.wake",
      "snapshot_digest": "fee256d32a9870a4526116a49417aaf5718edc09ea0777cb3e37156b316b7d7e",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T22:51:21.936729+00:00",
      "head": "37ca5e92b049661ef769e807794f98399fda01d0878963d77e0b220373fee4d3",
      "node": "301.wake",
      "snapshot_digest": "4de21f313115aa8193c20bc28bb012694de1281913ebebf59fc7144d4e7ce35e",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T22:49:57.093507+00:00",
      "head": "d0c9d32ccaadc7cf868acec33d24f261d4e4917f7fa45c08bb8a1a8d1b801fc7",
      "node": "302.wake",
      "snapshot_digest": "4982502c086073bce30aa54f8cde2e383776835e5144c4e4d1a72cf51d406037",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T22:49:43.336108+00:00",
      "head": "2568c1b9c33d83c6010be4f111bcb93bd0b1b6e2952ee1eb73d66e224c8368d3",
      "node": "303.wake",
      "snapshot_digest": "f5fe0daf9183534b4959a0e2ab8ebfb70e73501dcd4c23a6e7e0349e582e1635",
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
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d38616532363632333636343334663138.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d31393335383135326333346334653130.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
