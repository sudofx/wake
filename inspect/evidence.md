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
  "generated_at": "2026-10-23T21:55:52.576099+00:00",
  "head": "snapshot:da5c707a6a55bd98ca8a7ae05d1c899194708c4d602614e1089d1bff275f5c0b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T21:52:28.620501+00:00",
      "head": "5e341cc2a3c97c4d714b7e0840ea0ec9fe90fb794f11d1c88f530b1b32639528",
      "node": "100.wake",
      "snapshot_digest": "1513f4a999cf83b94b7fde87bf7dbe4090d09f5ab0971d5306c5f63bb7dff59b",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T21:55:01.679638+00:00",
      "head": "e0d68c2a0b67500ed993f27f31aee5e437b85cbb9766298fe812e0d7de413e87",
      "node": "101.wake",
      "snapshot_digest": "405a1e606ea68c5a0fb4e7e98969bed106a8cbac2d5cd653a9592853a4c70653",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T21:55:52.576099+00:00",
      "head": "3a4f258e508c27e060a8680e9cf9df2e0d77df51c8cbe0a154b967e69ade173b",
      "node": "102.wake",
      "snapshot_digest": "072f46a8980a6ad60b4d9a5b16305923d8240e98ce3abf4557e65c1fd352420a",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T21:55:16.290856+00:00",
      "head": "efbc6f56cb57797cee5b2a29eb26b100832fa32dc7805e174d380d38e365bdcc",
      "node": "103.wake",
      "snapshot_digest": "aa6989f760ecc8d0096423ea4befb71f0a8469b58d06b6e0925ed97bc2522166",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T21:53:41.609229+00:00",
      "head": "273b4ec678e5e27ab695d9093b94a2f7501f4159680ff1ce6851bd773263f386",
      "node": "200.wake",
      "snapshot_digest": "7b8ea32f15d6ccf93714dcc4f60dcb98e66f605951fc69c516b93b07ae2ed32e",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T21:53:56.222192+00:00",
      "head": "7906b294492be5939a812ba97fb3d9d99a7f376f13a428b2e39d460ca84fc4e3",
      "node": "201.wake",
      "snapshot_digest": "c4f43f8b59c899bf61c41f0f965439bd41bbfd4525fa09c0b6fd280d02621588",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T21:55:38.596395+00:00",
      "head": "0dfb1768f04f3ad2dc194ba5630390a496b70690ac2af422e3ae4008214e899c",
      "node": "202.wake",
      "snapshot_digest": "af1dceeb2ceb6701c817c5278a8454530bb3d795fd4b058ac4cd94c828f90b79",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T21:55:46.055751+00:00",
      "head": "0a8c8597bf334b2233315157a44293459ca2d3a10066db2c84825e54d9c084ec",
      "node": "203.wake",
      "snapshot_digest": "4e929d97fb7874732aedc719e23c1c721f78fb3379291ef322b97b065d8da8c3",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T21:55:24.252576+00:00",
      "head": "7fc8a910d9f3e3a16e3fe5a274d0497438bc2443dfd0160f1b93c7882648a30d",
      "node": "300.wake",
      "snapshot_digest": "927029e12f5147907fab704606fb57695e46b1b0bb9619839bfc483dcc157e06",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T21:54:24.898282+00:00",
      "head": "7fcf103e7c2523ec47e6ccd9ac48e23f4be5600da7be5a71945f5510e76fabad",
      "node": "301.wake",
      "snapshot_digest": "3f9365bb2b087885e49381c321ad66da63975bd27e96202387fe6e5190e0c0d9",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T21:54:32.776130+00:00",
      "head": "bbd49da508d5727551b86a46bcd3417053e6a8e95d45e3859011092804e83796",
      "node": "302.wake",
      "snapshot_digest": "2735cc9af618ecda52fb839c49d52ef7c06bfcb73eda7aa35202487f15f3dd0c",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T21:54:10.908875+00:00",
      "head": "e9c42272bf1e49c9ecdcfe88c41d27cdfc3a29de11b9d3d928812bbcce5ebcc3",
      "node": "303.wake",
      "snapshot_digest": "596e7d00c9fcdba8121ab7270f7a6604a746c23a849a0f6e2ba7897a51454ec0",
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
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d64613233383962306537336534636562.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d61643235613439353465633234373137.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
