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
  "generated_at": "2026-10-29T18:43:20.698949+00:00",
  "head": "snapshot:02d03f8fe4f0dfb487a30b076c52cd134513276743c7753e7623bdceaa6b3d0a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T18:32:54.700036+00:00",
      "head": "045519dec4705f8378f85f110f92736ef58bda76efbba352bf4ecd38dff71785",
      "node": "100.wake",
      "snapshot_digest": "7b33c1aee333807d7b5838ff9591bd34cd3823fc73f0fb4e9be7edb494cc271e",
      "version": 22
    },
    "101.wake": {
      "generated": "2026-10-29T18:38:16.708771+00:00",
      "head": "6a340a8fcf376146f4fdb23236a306134926f2415a7d29a74ae9e583576840d3",
      "node": "101.wake",
      "snapshot_digest": "f5fb395ed1c0329c372c9c2e39f7180e2481d776024743824130f81865ab2b58",
      "version": 25
    },
    "102.wake": {
      "generated": "2026-10-29T18:41:52.005725+00:00",
      "head": "e07b5a2b1d2cd70455f4a8b4684cc04c84d931f4dd830630dd39361ece5ce829",
      "node": "102.wake",
      "snapshot_digest": "b047ebd1b33085ca7503c0d4ce5ebd8d3994fe8ed222bdd106c26700f605d947",
      "version": 20
    },
    "103.wake": {
      "generated": "2026-10-29T18:29:30.102256+00:00",
      "head": "ea4bd9fc66656942665cb4439ae5a1d3340de15628010c8545c40fa2ebaeb8ee",
      "node": "103.wake",
      "snapshot_digest": "846e11d6909353d71f4c7c1c77e2ca1f830f86346d97b75bb016fe0ad272c46c",
      "version": 31
    },
    "200.wake": {
      "generated": "2026-10-29T18:43:20.698949+00:00",
      "head": "510d887472b2b6f9eb7bd70ad9b1b509016af7811e8e9e51ff1e84db6602e616",
      "node": "200.wake",
      "snapshot_digest": "3c26f6ea62481e4d55c3a68d5f28aa1ec8178994bad52e591dc1af19d1b4bc1c",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T18:35:04.009485+00:00",
      "head": "3a569c7d16bbb8d607b2851157f39b6b81983c75d18c3a116afa616389d3f21e",
      "node": "201.wake",
      "snapshot_digest": "a37798aba1d54410bab787b5a62547a1886f4951eda68c8abb701678b5451927",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-29T18:12:18.436124+00:00",
      "head": "82f28d0317597c3289352c49921c76918f1a548f829ecb5d69ba14b602ed6f2d",
      "node": "202.wake",
      "snapshot_digest": "4f750545b6192158c16295b76e254145299e55052cce61d6dd1b4a80bd25b7d7",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T18:40:10.262733+00:00",
      "head": "a30f38cd94fc4113703408caa922458acbf16a844a845cf24c068ccfc6753d3a",
      "node": "203.wake",
      "snapshot_digest": "40083f03a4db6440a02a2e1f58dd0ecf4ec82b0bc304996ab56993baeb6d94a1",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-29T18:36:32.998490+00:00",
      "head": "8634048d600cd4592f634b081c1c38652d8ed3296e27fd0230ba89da871566e9",
      "node": "300.wake",
      "snapshot_digest": "d2da26d511303ae488fa17fbc8782f1b46dfb0cfc55e95ee286af07002ff7414",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T18:27:59.453515+00:00",
      "head": "ce949dae2b77eb17cade5391ec9993ba5265476372c9a8b8bc7e62e43ee38c52",
      "node": "301.wake",
      "snapshot_digest": "89f7892715ab4715e28f2bbd82e31dbc115d89f44b2fa7ed72c326ab84e07900",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T18:31:22.360173+00:00",
      "head": "1e8895dedb617cbdf5f38b036a1706bf20fc653c4ce60561df2a38479d764625",
      "node": "302.wake",
      "snapshot_digest": "177d3c8445189fe857f7f39d648f07673bcc44bda5567dc8a4386bbaa3c6a2b6",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-29T18:12:25.014528+00:00",
      "head": "46c25e2e79c38bed20f1917b2c13e3c49e3e9d72bbad2c4255079ac023799e85",
      "node": "303.wake",
      "snapshot_digest": "1707d85faf96d2ce0c830347e26f1c0ac0c31419451eb55c472fb9ebfe78a705",
      "version": 24
    }
  },
  "version": 307,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d39643662363762633731653534656166.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d35613335376465613566633834333935.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d696e7472696e7369/632d676f616c2d666f726d6174696f6e2d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
