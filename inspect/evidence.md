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
  "generated_at": "2026-10-28T09:45:37.889623+00:00",
  "head": "snapshot:1905aaa63c117edd2c8211b986383882d310e016ac71dbf3cf1f6381f03d5f27",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T09:45:30.055604+00:00",
      "head": "701e1f2ab96238743464557c47b5289eaada679e9eda0acb26698d6c8a6edc10",
      "node": "100.wake",
      "snapshot_digest": "bf4c5acdd65da28b318461ce1ae1624b24d227cdba8d864c23c19d06f02329cc",
      "version": 12
    },
    "101.wake": {
      "generated": "2026-10-28T09:45:16.365203+00:00",
      "head": "fb78cc2517cfeadd90f55f1f5d10b4b6709b35cd13ec44939ddc2078abb294cd",
      "node": "101.wake",
      "snapshot_digest": "fc08d95d6c832c10b7fc440434604c2d3c40c7f9931aa655e02ad118148d2f33",
      "version": 15
    },
    "102.wake": {
      "generated": "2026-10-28T09:45:05.041101+00:00",
      "head": "b09b4b086a86b49064b0870fd350100cceda6f15c05ce261d8be29da51163f0d",
      "node": "102.wake",
      "snapshot_digest": "31cf68f4fdf559c24c1876e6ada0933f99268c42d84552cf1d53aae93bd5f33a",
      "version": 9
    },
    "103.wake": {
      "generated": "2026-10-28T09:41:16.241657+00:00",
      "head": "9dab7b25230b5b13390e9864cd5b646a777e549b12daf2e6bc8e6d9bac564a3e",
      "node": "103.wake",
      "snapshot_digest": "0acabcc09f68984d0fb7c2f283df27f661cddbf34b36cd3fe3d80a7d34f915a2",
      "version": 24
    },
    "200.wake": {
      "generated": "2026-10-28T09:45:37.889623+00:00",
      "head": "5f48581fb717442076311a1766f09df76884bd4d845f7b3954e71bebcf02c372",
      "node": "200.wake",
      "snapshot_digest": "24dde1272df959208d2259321fb9f3060663633bfe13cc35d91382931de6f536",
      "version": 18
    },
    "201.wake": {
      "generated": "2026-10-28T09:42:49.711546+00:00",
      "head": "e753136cf7bf309f116033d029399747863404ece3780f9197dbd866f04dcca6",
      "node": "201.wake",
      "snapshot_digest": "b2785551d86ce3454bcd6f7acd0a2db0d9176be581529f464e26bfce2478a0ee",
      "version": 16
    },
    "202.wake": {
      "generated": "2026-10-28T09:45:22.187039+00:00",
      "head": "3c2a085c24611b460dc0adec56b0b29ff0cc500abfccfad6dcd199626f527dff",
      "node": "202.wake",
      "snapshot_digest": "ea2142a86b80418d7238116317e7aab0ebadc194ac305c5bb282d76900faadf1",
      "version": 18
    },
    "203.wake": {
      "generated": "2026-10-28T09:43:06.649639+00:00",
      "head": "72b9a6330bfd0c286eff11451d4c508ae61ba6501ade67fcf247bae012183aee",
      "node": "203.wake",
      "snapshot_digest": "3ef21ad22bc6bf7a82727acd6be60e75f8886d2f694755efabf0582bd293977e",
      "version": 21
    },
    "300.wake": {
      "generated": "2026-10-28T09:43:30.161193+00:00",
      "head": "fde580e90cd5853a36b52ac429ed0225591b7ce9cf75a135a79b8dc037826fcf",
      "node": "300.wake",
      "snapshot_digest": "7578a26ad98e3f8f33bbb70bcb981fa20a5db247cd34c02b095a23aff0d5a86c",
      "version": 18
    },
    "301.wake": {
      "generated": "2026-10-28T09:45:17.508188+00:00",
      "head": "9a04b11717b0649a0a9da54eb7169c7706b72fe7e22a4d49260c40308dc5d5e1",
      "node": "301.wake",
      "snapshot_digest": "76db6584896d302939fad21af7ed835238549b4ade1719f026d5e37fdbf01fa3",
      "version": 13
    },
    "302.wake": {
      "generated": "2026-10-28T09:44:42.484737+00:00",
      "head": "83fb47e1f97148a11bca1034e8a814c99a586c6d44600ec1160e1fc466d729e3",
      "node": "302.wake",
      "snapshot_digest": "0fded6b4c7bd1617429db374b91a1d5b5d561723b315e30537298c393bc82ad8",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-28T09:43:12.752463+00:00",
      "head": "1c7cc772fa535ec17c5b8a8181a830b48e5568997c9d6d4194baab2ac2dbfbb7",
      "node": "303.wake",
      "snapshot_digest": "c566a64117b64161ae25a9da1be03bf1fd7bbccee6edbbd90b23177632ae1a6b",
      "version": 18
    }
  },
  "version": 194,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62393438356435316435363334376436.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d66346230353236663433376134326237.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
