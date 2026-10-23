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
  "generated_at": "2026-10-23T21:10:31.750125+00:00",
  "head": "snapshot:9f49d174945333bde1b25b0936b43bd27efed62635afbfcfaeca4a06eb523682",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T21:08:52.289329+00:00",
      "head": "24e2a564ceb97ca123f3aaf90cda2330e424f1f53f393d39f4250e677cc9271e",
      "node": "100.wake",
      "snapshot_digest": "3f67e3d9b1f521779c9cf4761760d0862722b6b62639498970a87d38877c0f3c",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T21:03:08.380691+00:00",
      "head": "422b3f7b4b17380ffa89b003b27733b57fd48433bc4d79f4ff5e08c26370b2cc",
      "node": "101.wake",
      "snapshot_digest": "84ff6ccdf0fa94a95f0951753233202e1fd9e161895b598194c56ae7d8ff55db",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T21:08:14.494293+00:00",
      "head": "e4a8e0feed6d9910630728028f65d400f6a0632fa0089d025b0672b5aa8b8bef",
      "node": "102.wake",
      "snapshot_digest": "6bd957ad171d121705126dfbbf1e1418445c122066620d879817c9c951c79e3b",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T21:08:59.815192+00:00",
      "head": "ff805d64eb3017d0b5a1b77c6a2dc31883a1959d0c068ff29b1ce7e8c704eb42",
      "node": "103.wake",
      "snapshot_digest": "43f01d29c1a4350d6340b1b2fb944ce51783d90a12ce0b64e48da79dd472a33d",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T21:09:29.168381+00:00",
      "head": "8e470943498d5229d0914caf174b3e0a4c12d05abdd3849237077cf467085f82",
      "node": "200.wake",
      "snapshot_digest": "2fee2a9f68a06ce535f62c397311093cda07d73c3519e9d6bedb792468e1b7a6",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T21:02:39.129889+00:00",
      "head": "6ca53996210dbbdb238608d5e38fd6e8e7d3beb072c0564b73c41069b0ecc7d6",
      "node": "201.wake",
      "snapshot_digest": "9513ec1300027caa1a5d409cff3e614ffc2d093460afcd83ca4a9b9b9e649313",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T21:10:31.750125+00:00",
      "head": "8595da3d2afb7009978fc1ef73bf4c5615b78f62d92589835857e18fcc538f20",
      "node": "202.wake",
      "snapshot_digest": "ab4fc0289f7112171d939953a10f2d66e565a8dd300b3ab038867bcd06b8a551",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T21:07:59.850510+00:00",
      "head": "a9b5af5e49fe886eb9673240cda9e58f7e7d2f5874a562a4a90e7fe92c07a0ee",
      "node": "203.wake",
      "snapshot_digest": "1cc564594216336214890e9709eb9ee5df13444e81008e4e144d9b4b973d96ac",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T21:10:18.091111+00:00",
      "head": "dc622744a38979397fc9fcb0dded17c69e9b598d69588c276b5e3d7458967f3b",
      "node": "300.wake",
      "snapshot_digest": "01650ac80a1caca5a2123b20632503eac8bd368ac6f262b2dfd4131b04326f00",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T21:08:07.742439+00:00",
      "head": "ffb0eb0758eab652a7808d0daf1959f518dc79bf3ec83e90fdb1ebb3de42d1d8",
      "node": "301.wake",
      "snapshot_digest": "a0f4e51a2e73c93f0b7e034bb5fe90d767abe02b3c17bc1cf63beb9769a32405",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T21:08:21.559158+00:00",
      "head": "63d77b0bdc6db4a55ac0816d24081f83905284f1a53f8c09dedad5af10823b72",
      "node": "302.wake",
      "snapshot_digest": "4f5172ed0fa8ea66283aae7f2fbfdc771ea0eba7e865d0df128a7daea618f8c5",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T21:09:13.660265+00:00",
      "head": "0842d12b984e0c2df9842ae8090599d9090c6bce560742290a08200930784fc5",
      "node": "303.wake",
      "snapshot_digest": "37f15d9b6f7d0817944191e3636e6057ecb6bfecfce5f04cc4731602c2b0ea76",
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
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d33366432623164386630663134636236.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36303935393462633561376434336639.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
