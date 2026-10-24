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
  "generated_at": "2026-10-24T21:18:02.383460+00:00",
  "head": "snapshot:4e47750843037bc5c64744554d40f7c397438395c0703857ee7da50bc90af7a6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T20:49:36.105008+00:00",
      "head": "53b466c9282d376468597bbcd13c6be5cfa7f318739087be697b36c3d7f7f4fb",
      "node": "100.wake",
      "snapshot_digest": "3bd57f08f43c8a7bf1f0910e81b1d742431bd2a4a59bb931dec59e36388cdecd",
      "version": 24
    },
    "101.wake": {
      "generated": "2026-10-24T20:49:36.910516+00:00",
      "head": "a48afa7b53dcd2644c04a8014cbdcbc83fc77ca2c83c99fa7a3f7ea248e0b35d",
      "node": "101.wake",
      "snapshot_digest": "19d5d3d96cd004d286bb2209b54d3941d957f5474c39e83516bd27d060df1d65",
      "version": 39
    },
    "102.wake": {
      "generated": "2026-10-24T21:18:02.383460+00:00",
      "head": "3188b68bf84bf1468f913e73a46abdf350047453e57d56db42e8a9d31830ccfc",
      "node": "102.wake",
      "snapshot_digest": "7f4869805d93c28a6c6cae725a2aecc4bfe2d6325152e96c62f3cb2ad2ca1675",
      "version": 52
    },
    "103.wake": {
      "generated": "2026-10-24T20:49:36.714526+00:00",
      "head": "c693ab1400b836d75164f3af5f6eff8630b11fb189f7bd8454b384c9f99aa63e",
      "node": "103.wake",
      "snapshot_digest": "e7e92aa43b48f31d5a93f2617f601d58c817d79aa911690cdb4b3de758701f9d",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T20:49:37.894027+00:00",
      "head": "c3561e0cab9d37223985cba9754ac014f470b3b7fe6b8c63f1f9bd3ebe17c815",
      "node": "200.wake",
      "snapshot_digest": "6f673f2fa36df4727e51fec977d8ee6a2f3215f852f99266bb831176d57ebf93",
      "version": 30
    },
    "201.wake": {
      "generated": "2026-10-24T20:49:37.709516+00:00",
      "head": "ff4c82496a6b2e831cae3d3e1b2678efc056065b62f98f6955143382df0be92a",
      "node": "201.wake",
      "snapshot_digest": "41d203dc6ae1b879efab0099dc515d1552b9e22551d4151d0f511ffd378141d9",
      "version": 36
    },
    "202.wake": {
      "generated": "2026-10-24T20:49:36.737319+00:00",
      "head": "fedb0b7ddb1643a5e60cd863abe51675c40e7e0ea5c554252dc32ab57a5221fc",
      "node": "202.wake",
      "snapshot_digest": "836aa6cb75f890d1e17ab6732e508dee3f23d030dee4f533b971f90188de43e7",
      "version": 49
    },
    "203.wake": {
      "generated": "2026-10-24T20:49:37.638924+00:00",
      "head": "0e6d02815b21d22a85cccde3d6289bf19cf1f3e770db12105277224d2da9764c",
      "node": "203.wake",
      "snapshot_digest": "c15ce688b9f6949df14cfa4e1cfaa58f8d09f64da2be11181bee13b19430f95b",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-24T20:49:37.076763+00:00",
      "head": "02eb0901e6f12f891e0eaf7a517ae3901c993b43efe3adc288e5e681ef3b4683",
      "node": "300.wake",
      "snapshot_digest": "4e6bd68d3e5484cbe44d81c88d8f2fc778ab4358a06bd6887ebaa6a207aed04c",
      "version": 32
    },
    "301.wake": {
      "generated": "2026-10-24T20:49:35.763367+00:00",
      "head": "abc6ac2675ef6d3425f8aa05bf1b5a1521e31202d62e63472143bf5fd116a8ad",
      "node": "301.wake",
      "snapshot_digest": "0797ed7dad1f7e695571f6bc6620f2dfa4586a4d842381d0e8d2751bc3eff9cf",
      "version": 49
    },
    "302.wake": {
      "generated": "2026-10-24T20:49:36.623696+00:00",
      "head": "cfd219f6b62db30a43416bdd355484757c5c93f82b060e71e27adc9e83c57e0b",
      "node": "302.wake",
      "snapshot_digest": "f8f89a45f7f3510dfb8e83c2a7918e5251482308274a77c08c79b8d93663a4b0",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-24T20:49:39.504052+00:00",
      "head": "d1aa0caee37449921f4db3f292ff70db7330013cbc40c6cb8b437d1d53bd18d0",
      "node": "303.wake",
      "snapshot_digest": "d633e33132a463145331074b08264e60d3e30ccb14e80fe274003d96b88794a9",
      "version": 48
    }
  },
  "version": 452,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a736f757263652d376565303537643633646333343864/62.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d37336138383134633365643934393433.json)
- [notebooks record](../reader-records/notebooks/3130322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d6f62656469656e63/652d696e74656c6c6967656e63652d6661696c7572652d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
