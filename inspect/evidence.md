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
  "generated_at": "2026-10-24T19:03:38.629897+00:00",
  "head": "snapshot:b5be1c878472146d07c2c5785ad4c092e4997591abc46314102e68c31d267812",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T18:43:23.563213+00:00",
      "head": "d090c315bac0d10a89357310daebf72834f70c4326a8b4c146f8ee701f33dad5",
      "node": "100.wake",
      "snapshot_digest": "aec6286934d93732705466307b94bc7690693f496cf13049ab0e78f6688e6cb0",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-24T19:03:38.629897+00:00",
      "head": "41c3c72f7ce7161ba230cad18cb1604cd4b4ef55332670f16d0591fe27afe667",
      "node": "101.wake",
      "snapshot_digest": "725fbd8ee789ed8bcf3fd390b8cd4551ad1900617780a1316a6d87248cc6eaf9",
      "version": 38
    },
    "102.wake": {
      "generated": "2026-10-24T18:43:21.866481+00:00",
      "head": "6e5966df4d2b953717c1aa222340794460cc359b0c1b2686242f7b465e4a7418",
      "node": "102.wake",
      "snapshot_digest": "e77f012f65b0b8d6ac88f2eca2e40fa5e39509ca4d90f56fbd8b9ea347f8b13c",
      "version": 49
    },
    "103.wake": {
      "generated": "2026-10-24T18:43:24.100003+00:00",
      "head": "d57db24a86a9f924ff21cb542f1365d86c45ec2854af170d5c96d33e47015959",
      "node": "103.wake",
      "snapshot_digest": "20cf478f1fc63691dbb190b22c5c44e1b14376399f850971bc6ae081def4d251",
      "version": 36
    },
    "200.wake": {
      "generated": "2026-10-24T18:43:24.532962+00:00",
      "head": "e0d9376d3ec83598ec032d1544c25d90e3d0f4659c51c3f4d912cd00901d516d",
      "node": "200.wake",
      "snapshot_digest": "546dffe9efcbdfc8c3135fc2c3857d0c39210fef945589cdc748556f893d7fc7",
      "version": 28
    },
    "201.wake": {
      "generated": "2026-10-24T18:43:24.590174+00:00",
      "head": "bc2fabfc9d76a318d9eb8fdc77ddeeb93855486a51bb1abe63aa620d5393832a",
      "node": "201.wake",
      "snapshot_digest": "97d78d7b207a9e714a7a08e9baeb9fe842b055e8c8aec787e3adc19e5aac478f",
      "version": 34
    },
    "202.wake": {
      "generated": "2026-10-24T18:43:23.390232+00:00",
      "head": "5f1974993fcc343753a93bbcf01d16939cd744a65aa9addf4e0e23e97e6b138e",
      "node": "202.wake",
      "snapshot_digest": "3218e39eab6dee9f6121fcfe51db747527ce934988c45ca36038ebe3cb016669",
      "version": 46
    },
    "203.wake": {
      "generated": "2026-10-24T18:43:23.489928+00:00",
      "head": "35eed2c900c1a34c28f17f3d64224fae2bf9873282961bfec860bb5d39871dd8",
      "node": "203.wake",
      "snapshot_digest": "9206929ab8323dd5c0a64807e236cea4c5b4abde29c83f4981a65167b9d27526",
      "version": 26
    },
    "300.wake": {
      "generated": "2026-10-24T18:43:23.323291+00:00",
      "head": "b830d11e3ec781c9babd38d5e8ebaa1c67ca2848cded14758835e76c8dd1b908",
      "node": "300.wake",
      "snapshot_digest": "c3cdce323cb7f148a3d682e49644d1ffddfa8124475e13cad06cac2389d020e4",
      "version": 29
    },
    "301.wake": {
      "generated": "2026-10-24T18:43:21.933491+00:00",
      "head": "1856335529724a81819ddd9529894d77f7b0b479c4c0adad2986f09ed0f73d63",
      "node": "301.wake",
      "snapshot_digest": "049a9751f1752c1a563e58f24a919f16625aec9ab220de1d6653b4b90b332953",
      "version": 47
    },
    "302.wake": {
      "generated": "2026-10-24T18:43:23.139589+00:00",
      "head": "db67064229b07b6867151120bf84de86d1cf562968cbfdadc07e595fa77e337b",
      "node": "302.wake",
      "snapshot_digest": "66eb58cfba19cdc94d0dfcb15b0af5f40aa68eb54f7d3ebadbf6b6b27a004fe6",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-24T18:43:25.150137+00:00",
      "head": "4fcc6bb73902f121e3b20251fd393b93f03f6e7b3e317efbd1944d1c6ce390b7",
      "node": "303.wake",
      "snapshot_digest": "5cad904a01878bc9dd1061f9e7e5a953354fd47c7d051b73bdf4bb0f649082ac",
      "version": 46
    }
  },
  "version": 428,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d666534333039663233303864343834/64.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d65393765613534376232633334353861.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
