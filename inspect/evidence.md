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
  "generated_at": "2026-10-23T16:15:14.006689+00:00",
  "head": "snapshot:d72cee428d63ec70d8921ee0c16f54cdf94b55af270f394ea882be36aa030b01",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T16:12:24.251472+00:00",
      "head": "73e88fa27de250dbaf8bcca8e8a128ea6d28d6b0b52bd500a803627fe013d1d5",
      "node": "100.wake",
      "snapshot_digest": "b4d1c50ecc7b1819a466e073b4c17a6e250ebbd7034a2e8735b76e75a8256da3",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T16:00:42.424898+00:00",
      "head": "ca36f2fa9102c164d67f5b65fc6c9cb1b0ca72cd0a5828141f8d597110c6df72",
      "node": "101.wake",
      "snapshot_digest": "b35bc15944de34ca7ae1f80c3860bfb05794f2fd9c58f25d9f79a161fb08483f",
      "version": 26
    },
    "102.wake": {
      "generated": "2026-10-23T15:58:45.510519+00:00",
      "head": "9446bba9acd57ed6642f45646807c6c5c6687557165c91f661e477a0b12c11dd",
      "node": "102.wake",
      "snapshot_digest": "120aaf191dd0123aeb9161dbe4e8c2af846c67eb036e0a02df2cd275bf04dd99",
      "version": 32
    },
    "103.wake": {
      "generated": "2026-10-23T16:06:07.657368+00:00",
      "head": "18bedfd80d8ecb8407c29035ad425d09522ae2c401a9d52380d623b010d68bc0",
      "node": "103.wake",
      "snapshot_digest": "4218429d598683606702806de94641127df9155c687deae92145fbae5182c48e",
      "version": 23
    },
    "200.wake": {
      "generated": "2026-10-23T16:15:14.006689+00:00",
      "head": "4631e10d481364bbc74bb3695b299788b6300e9b6e6c24de0391cf84920fba1c",
      "node": "200.wake",
      "snapshot_digest": "a421283636f769179edbe4175f06f8da93c86df769544dd680eff4840c711218",
      "version": 21
    },
    "201.wake": {
      "generated": "2026-10-23T16:06:28.725642+00:00",
      "head": "40e6612197e3bd96de3a5693d8624227d68c38525281a703fca4815f59b2b077",
      "node": "201.wake",
      "snapshot_digest": "18c2bcc9a867a3a30573f8c53f7623698283c1acb61620193a821f9de3a313a7",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-23T16:00:09.104343+00:00",
      "head": "187bc87fb76e4b02740f4f64b949ef4274b7964f7ad6a60407bad1eecbfe1a77",
      "node": "202.wake",
      "snapshot_digest": "357ea4e037ec927dc83d5ff891abb422d5b40c3c1b43b756b143cd39441c7064",
      "version": 35
    },
    "203.wake": {
      "generated": "2026-10-23T16:11:11.711681+00:00",
      "head": "413ee36565034bface4148550d49ce17c3491302a2ac8f368b1771a21aebe143",
      "node": "203.wake",
      "snapshot_digest": "775b64c4b97ab6de04eb23e4ce56c3a61a95ed860b6dcc73b0c31729ba140849",
      "version": 15
    },
    "300.wake": {
      "generated": "2026-10-23T16:05:02.547728+00:00",
      "head": "8ff2552a8dcea5273092ae2565e706b2e5d340381bdd7116c8708158154563c4",
      "node": "300.wake",
      "snapshot_digest": "4ac951b5dcd05442570622323beb6c0baa08f3f3966c1bbae5a2311a47e6e70e",
      "version": 21
    },
    "301.wake": {
      "generated": "2026-10-23T15:59:24.381773+00:00",
      "head": "cfa71ab35d2f0822e4629c2e3f22c6c32e62a34cebb6706f52ad87e43511bd51",
      "node": "301.wake",
      "snapshot_digest": "d67bfbc497eb1dfd9cef5734571375edcd1cc7ad39123e85482a2ead531bf029",
      "version": 32
    },
    "302.wake": {
      "generated": "2026-10-23T16:14:00.279189+00:00",
      "head": "7f6b0ce1ddef1319483e165140baae2c4ce5be4cf9dacb0a01d6b956835b8449",
      "node": "302.wake",
      "snapshot_digest": "a75681d31bd567f11975da1241555d43a98543aaf88c5e854979aa36981a8bcf",
      "version": 16
    },
    "303.wake": {
      "generated": "2026-10-23T16:03:26.598087+00:00",
      "head": "b847863af4cd745ab79699da78bf414cafa0afe6b3f59729aec9e582d19ff689",
      "node": "303.wake",
      "snapshot_digest": "db6c83a3d201eaf3975ecc956da19b1d6c96e9bc88cc805fd450c896cb0fe9b2",
      "version": 30
    }
  },
  "version": 289,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d383734386165363265663334346436/63.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d633935313736393561393766343739/38.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
