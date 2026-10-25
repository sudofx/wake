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
  "generated_at": "2026-10-25T01:24:01.064970+00:00",
  "head": "snapshot:c19b981262bac1d437584f2154546db564817d5590208bdd7f4039f905b28e0d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T01:23:57.439507+00:00",
      "head": "606a35a3cfd586365060822b25543d392103810ce075aa7d20ff1619fc807811",
      "node": "100.wake",
      "snapshot_digest": "89d97f264670ed858f5984a2e4a0fb2adfcf191938edf26f524e4984582824b3",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T01:24:00.415108+00:00",
      "head": "750a8705170a860220d485528f852faa5558990f4a7a6993df467ecb0b7aef79",
      "node": "101.wake",
      "snapshot_digest": "db0b5ecb1505d77b1417fbde328e88a16705c7ad428cfec2d5a73b650bd5dbf1",
      "version": 41
    },
    "102.wake": {
      "generated": "2026-10-25T01:23:53.569837+00:00",
      "head": "aa248f60e9c094303afc067b6f9d2a24b45566b399dea63342b144cd37930238",
      "node": "102.wake",
      "snapshot_digest": "8ee0a9cce60de6a99b3db2872bafeb196e6db2a2106cfdcd612b93abc779566b",
      "version": 53
    },
    "103.wake": {
      "generated": "2026-10-25T01:23:59.776885+00:00",
      "head": "655262832df72760a58bf1a355a87d0da36b2a0f843aa1ebeba83f7692391ebe",
      "node": "103.wake",
      "snapshot_digest": "60fd73e8280773686b33f9a7f61df0301494b2e1fa15f3a909a5df2f9eee2cd5",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-25T01:24:00.731601+00:00",
      "head": "76f920439d629104f539253bf799b3eec406109c624c04cc3a382197d12ed3f8",
      "node": "200.wake",
      "snapshot_digest": "f1d968af5ce69711fe9eb37b1268f0760473e6655cd6e972ada1f3ea12d752a3",
      "version": 33
    },
    "201.wake": {
      "generated": "2026-10-25T01:23:59.908481+00:00",
      "head": "2e8f7ccc69a0a9929f574ff913e09d291d418e5d92c0f5e0a9c2c6c060b2b6cb",
      "node": "201.wake",
      "snapshot_digest": "e630a3b6ef0d77f47f2556d4750fb65f98654b72b3b1cb60dd0ffc2530c14fec",
      "version": 38
    },
    "202.wake": {
      "generated": "2026-10-25T01:23:58.837164+00:00",
      "head": "b70590511a317a38d014be1254fdb067b588893ab78f2167f89964437a4c5cbb",
      "node": "202.wake",
      "snapshot_digest": "359dd91612eed2ff633ee9d45d0b20daad5676df1f90edb764dc96a6ca39d7f5",
      "version": 53
    },
    "203.wake": {
      "generated": "2026-10-25T01:23:59.183135+00:00",
      "head": "ed6f234c350a128667cafeece122732a8b0a1b89e7f45449471258c0e1b960d1",
      "node": "203.wake",
      "snapshot_digest": "5106fb9f0c15c88526eb5b59063e86f050891866c41e38f789a41d5b2d23cc45",
      "version": 29
    },
    "300.wake": {
      "generated": "2026-10-25T01:23:59.495843+00:00",
      "head": "d64178a1cd43fa6949d8f73416bdd2431ed0fa21aa3e74931e6dbaa55b6cc862",
      "node": "300.wake",
      "snapshot_digest": "673918c8a9cb4285056e063d784e5b57e81bb20519839d0ae9303be263d6c7d7",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T01:23:54.976474+00:00",
      "head": "7d39260a7b36725957a8c4b83dd60b51502894637aa52f62b18017c14530ec2e",
      "node": "301.wake",
      "snapshot_digest": "60dd56fa25053acafc363cdd0f2bf2b913389d8ec8e3f1b3f4344099640a370c",
      "version": 54
    },
    "302.wake": {
      "generated": "2026-10-25T01:23:58.698769+00:00",
      "head": "0d3c98d4bd7fb22ca0a0ce34ac7cf543790582d1bfbf5d9430bc80a559091fa2",
      "node": "302.wake",
      "snapshot_digest": "9499304bdc46ac75bdf825cb3f90f664f3a007e8d48f9918d9fd82d0f3acf570",
      "version": 33
    },
    "303.wake": {
      "generated": "2026-10-25T01:24:01.064970+00:00",
      "head": "b96bda6cfccf6f1081dfe7af43fd1944d85c9701fcd27887bb3fda2d6753f6e4",
      "node": "303.wake",
      "snapshot_digest": "fae4a4be82b65292b0398fabb964ef428417b4014f44c178b80f4ebb5b8cfb7a",
      "version": 50
    }
  },
  "version": 482,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d613832336138383366663966343163/31.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d653731366535613862336265343135/30.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
