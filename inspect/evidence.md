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
  "generated_at": "2026-10-24T23:38:45.498684+00:00",
  "head": "snapshot:2f9589b44c5c58884b5a17180ff0ceb6c9caefa58c69934970197c8650cdde17",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T23:14:54.750274+00:00",
      "head": "7e9fcf312dc38e44428b2dd8b1111283502958b73c55806d6a4ba006a4f3ee49",
      "node": "100.wake",
      "snapshot_digest": "140ae9a7c7522feb224e6bdfabc7f051518a2f185f3f82e0ef7e8bd6b44b40b4",
      "version": 25
    },
    "101.wake": {
      "generated": "2026-10-24T23:06:51.720846+00:00",
      "head": "f3eaa559a03132574051ef1b900e28e777daeadc11333205da357d2e177fde91",
      "node": "101.wake",
      "snapshot_digest": "8d59ded261733d50b9496bb8319fb3a0f9cc55cff1dc6b3e831b0394ed517dd5",
      "version": 40
    },
    "102.wake": {
      "generated": "2026-10-24T23:06:48.865453+00:00",
      "head": "7a1d8d43ad6c1edcb00040e59e6daf32f72461be24272a32961f7cc39734b5c1",
      "node": "102.wake",
      "snapshot_digest": "aa415443d1fc6380229cfc9b07116520f10ef21f22367f6d9ee96bfd189fd956",
      "version": 53
    },
    "103.wake": {
      "generated": "2026-10-24T23:06:51.316726+00:00",
      "head": "54e6a5b11882c7251ecc7cd90e703b41b0f4d4f5cb4d284d0ba339fe8d578c88",
      "node": "103.wake",
      "snapshot_digest": "154535cedb55ab30cbcf97cf0c258aab9f4bca9e7892040d810919b7df883425",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T23:06:49.351930+00:00",
      "head": "9bea522530f50ccac5a93d09a2632c14756cd4dbf1ee7652fca9ce4a690287c0",
      "node": "200.wake",
      "snapshot_digest": "6cd3094ce500bf43ed803cba27c430720374f9e96f8e2fed140a028b646dc021",
      "version": 33
    },
    "201.wake": {
      "generated": "2026-10-24T23:06:53.040573+00:00",
      "head": "95863561020ea14ad37efb58e80512a341c35e65bfbcc4e182278f40f037bf2a",
      "node": "201.wake",
      "snapshot_digest": "cb9c7b23ec9d03603ef67602b6def08de8e9e1ce5e3b46b4c0b47ad52b7b0210",
      "version": 37
    },
    "202.wake": {
      "generated": "2026-10-24T23:06:50.208731+00:00",
      "head": "922926102cfba7a051fbb95d1c8236b6f880dfcdb87ed9632118d4f612aed267",
      "node": "202.wake",
      "snapshot_digest": "1d418e0bf466bc906fea80e5df8fedc1c62ed73f53f166666789b16aa0124aec",
      "version": 51
    },
    "203.wake": {
      "generated": "2026-10-24T23:06:51.427626+00:00",
      "head": "8bf89a1780c1c1411053de5cc49bc5c418f2ca831d9751f3cd861c83fddbf528",
      "node": "203.wake",
      "snapshot_digest": "e3873fb838e33625d3ceb6281e96fdadbe20030826da5d48e83cfc276a4f4584",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-24T23:06:51.592762+00:00",
      "head": "5903765b69f2c204c19f3f17ad383bcca36e9d38946e5f1558af16ca938cd3c8",
      "node": "300.wake",
      "snapshot_digest": "c8b979d56ef389aa69c2d207c914544128b6f069de6a35aff4348203eea88111",
      "version": 33
    },
    "301.wake": {
      "generated": "2026-10-24T23:38:45.498684+00:00",
      "head": "86576de9ed39a011d8f8e738349a87087311a52218e32e9ae61b34cebb1a13ba",
      "node": "301.wake",
      "snapshot_digest": "80db78bf64a759464872a56a830dbf45659b7481f7db311461031a2b1db5dedb",
      "version": 53
    },
    "302.wake": {
      "generated": "2026-10-24T23:06:50.959282+00:00",
      "head": "99b17876449de6bb371bf516067de2c0aba86450b7d4aefd435e8f3b8cba3f13",
      "node": "302.wake",
      "snapshot_digest": "0cea6ea562af3ad63cce77fdfa66c8ed554589d789bd210779a6593cfee636fe",
      "version": 31
    },
    "303.wake": {
      "generated": "2026-10-24T23:06:53.877886+00:00",
      "head": "755befa8a318401ebf55587c54396f37f343e685e98a43c4c1b0a03fb631207f",
      "node": "303.wake",
      "snapshot_digest": "2a27df75eb20423717f339a07335e3a8fd04ae22f14f14bb37b40d14f543bf6c",
      "version": 48
    }
  },
  "version": 468,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d323563346332353933636439346132/62.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d366563323363663333353066346538/65.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d726573706f6e736962696c6974792d666f726d/6174696f6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
