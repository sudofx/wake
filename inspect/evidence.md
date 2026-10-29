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
  "generated_at": "2026-10-29T06:18:32.416474+00:00",
  "head": "snapshot:ed4e59e42890b8eaa784ff0a42b77149d25a6ad692fa8ae7e942a8c6bc395783",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T06:11:34.332858+00:00",
      "head": "cad01bcb2e6d99d90f0276875c421e63bb26fa1c80d265307cd3a4308513fa61",
      "node": "100.wake",
      "snapshot_digest": "fd7afa78dbe61754dcddb139d73fd1ad0206e108f242db502b6e5b204f142efb",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T06:17:30.560484+00:00",
      "head": "8a8e538cf6c3aff212a690fad375cdd85dfebba6084900071dcc22e2086169b2",
      "node": "101.wake",
      "snapshot_digest": "3ee496f8fc0d110827c104856807ec4d2e32a5fd46ccbd8c93129a51d6925977",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T06:18:03.526186+00:00",
      "head": "eea9526eb88a021ae1178efe15f47748f7be2665f9c18f232b2624165ef5f1b4",
      "node": "102.wake",
      "snapshot_digest": "e2be61d05ee47e34cba41cf148673204428789ac3daa5b92bf32bf103553cc96",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T06:12:52.574116+00:00",
      "head": "7c70638bf8c32ef626ab6c4063b3fb55c1f225803c7e9c1027bc2bac0c0480a5",
      "node": "103.wake",
      "snapshot_digest": "aca19b8cd128717c9da4ff2228ad0fe5050b321d008448c46d9bfbd37d23ba84",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T06:11:14.105015+00:00",
      "head": "d235c7318839b7b1cbb61f356e0dd29e8d115222362bc38f01b6556479b20137",
      "node": "200.wake",
      "snapshot_digest": "6e6fc05db91638c42d5037e204350a50682182dd7fae6386753ae6a8447c4f5a",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T06:13:00.807216+00:00",
      "head": "76549b98cfa98bb1bc6214c456b8c9fdc3eb5afcdb5cd715d4f452f1a28d111a",
      "node": "201.wake",
      "snapshot_digest": "e7faced82ec143e89078efdb09ef1a489d3cd3c78f1fc2a7851cc1e1feec721c",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T06:18:32.416474+00:00",
      "head": "7aa3ed53084226a94df834439a949b884d8a6b33c9114a317809d02b07730981",
      "node": "202.wake",
      "snapshot_digest": "c2245f81e63bdacd805cec0dbc647f347bc9db356c45f79eeaa151806948d270",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T06:17:39.610295+00:00",
      "head": "c01ad978f5ee82e9d680c1a39690bd2b2f27d56ee0b298c0fa2a5f929611fba4",
      "node": "203.wake",
      "snapshot_digest": "feb2a5c7df808b0b320dba2a898cbd55e2de98ab1e61738535b1191658819305",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T06:17:40.730645+00:00",
      "head": "ef5437c96f10e3a2dcf803e5622d1fe68bc1b1c9d317092de0ae910e6fffbd8b",
      "node": "300.wake",
      "snapshot_digest": "46713c0bb61e5306f448d181883a01d0af6af20c6ce96c1fc85be7de8f352613",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T06:13:44.655192+00:00",
      "head": "fdf595f2055f9486251978f4e9603bbeb74fe9de6dda72d6c7e432172fad0a03",
      "node": "301.wake",
      "snapshot_digest": "2f57e7176775cb245640bfcf23db6b0d936e4863c5658c5a69595285e2a9abfc",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T06:13:02.015109+00:00",
      "head": "0780ed6c115af0f068c2757b31b4b921e14562396e256ed7ff49df19d74a464a",
      "node": "302.wake",
      "snapshot_digest": "7597006e7365f24f75f1b28456831244ba4a9b734e7b23419f07e99db71636bf",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T06:17:49.842825+00:00",
      "head": "e10f82ea070dcf156ab3a5f188bfa568d2d92815aaf739568d3b5343cac16596",
      "node": "303.wake",
      "snapshot_digest": "ef175dd0de3ed86d03af26b284221c492e55fe04ecf0c0018291af0651f1fd9f",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d63333733353036326331313734633761.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d36393465633030663634656434303161.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
