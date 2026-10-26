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
  "generated_at": "2026-10-26T15:48:48.221845+00:00",
  "head": "snapshot:ef945305575466cde31ab8ba5228418817429862e042367636a876b5866c49d2",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T15:29:56.303816+00:00",
      "head": "278fff2a24ef7b3ac50333c4fca3e39c63d56da50ad6863c03a43de7fc34dff8",
      "node": "100.wake",
      "snapshot_digest": "bdfa66b3a8cf9812605228d585b55c0b2f8fff75178d4855eaf03bdf1be33581",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T15:46:25.831139+00:00",
      "head": "73598691bd75e63647d406cad4a2dea21e7eae5f4575008aded1aa53792d8331",
      "node": "101.wake",
      "snapshot_digest": "443fe661701cfca7a8d1ed2ae015927a1c51170d1943f7ac34738ff6a0f7e674",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T15:34:19.452791+00:00",
      "head": "d959626e59b779b8e0d91304e5ae12f354b3e17e0f52e604ebff067fb0b82a59",
      "node": "102.wake",
      "snapshot_digest": "84f92f1665ba120342c3d2048bdabbd0682761ff9412fbf4352f64f3c7d5f083",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T15:48:48.221845+00:00",
      "head": "265470ea60d8207b543f19f7075225f749f90f91107d6bf12453ee37efb96536",
      "node": "103.wake",
      "snapshot_digest": "4c023b73d0d0651557f530cda877b2d95bd91401350048099021e24ac0b92cd7",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T15:36:07.230335+00:00",
      "head": "484bf0a194fa3d000a783ecd0d12e68431e36dfa76887b4ad290efd33805ae61",
      "node": "200.wake",
      "snapshot_digest": "1da97bb4fcec6dba4ada5c4552cf41f467ae5fe32933523aa77af6b26b64378e",
      "version": 43
    },
    "201.wake": {
      "generated": "2026-10-26T15:28:20.321326+00:00",
      "head": "76733599a5a3466321ee3610890623e6ef37f12a89c941119bf5d85f8a045140",
      "node": "201.wake",
      "snapshot_digest": "d69b14e4b7bd778c809aa09b45c6c6071a0f106390d8bc4871bd3a8767d147b9",
      "version": 44
    },
    "202.wake": {
      "generated": "2026-10-26T15:37:54.671493+00:00",
      "head": "71558a0079aa1a7808b08a2bb8d8e49698df276371b3305105cd84d91b611817",
      "node": "202.wake",
      "snapshot_digest": "d6c7e7291295bd2f4feb23751f2cf53445330cc423c00bb8a0a6e5f941ba79e4",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T15:44:03.357877+00:00",
      "head": "970d63c8ec37538cb1e46be7acbfa70a7071fd3892b0b89705f01730440ccefe",
      "node": "203.wake",
      "snapshot_digest": "ba73aeb08c46fd8d65fa4dce4aac4658df7386f27715d2c84097dc46e97aec27",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T15:45:16.304183+00:00",
      "head": "a905ff2b5d08d460de15d92013a799c5775e2eb3e1853a928f3c61533f9b7448",
      "node": "300.wake",
      "snapshot_digest": "ae439520283bae0760d3f15fce696f2f64a49d228e109927fd993be2dc42d236",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T15:08:46.419738+00:00",
      "head": "690de83babfc5b2475e0acb081a79b8ecda3f0650b978c325975a57dac7d38fa",
      "node": "301.wake",
      "snapshot_digest": "0df125ab164dbd2934681f5ea809529895f6ab731eecb74498ac756baebc52a2",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T15:22:42.438529+00:00",
      "head": "ba7ca6d747ec5ff630a8cef0cd6fa6e96de65766320755d90ea7dbd652c229df",
      "node": "302.wake",
      "snapshot_digest": "119cfc47de099b7f0deff962cd4ca988940eb4adcc35ed9a111f375fe94cc263",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T15:30:42.719153+00:00",
      "head": "73e13824a988b6955922046dd8866e929d52ae34f19b2125982f20ed0d2330e2",
      "node": "303.wake",
      "snapshot_digest": "1452bd32b89c127e6e02181411840a08ab98999771f8e9ab4e52abd8894b28a0",
      "version": 56
    }
  },
  "version": 575,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d66613664366533303262323434653730.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36343237613533393031633234313734.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
