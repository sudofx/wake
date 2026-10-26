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
  "generated_at": "2026-10-26T18:46:13.004238+00:00",
  "head": "snapshot:102401067f6bb2834c9faf707f4751b392d19f099e340b90697e6835009324a6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T18:36:14.328849+00:00",
      "head": "3ad5ec983e1cef0391ec502eea0b9f881f665fe53a092076001af17c9c0b50fd",
      "node": "100.wake",
      "snapshot_digest": "a1ac02a77e11f89e50e44e3dba5667218334a4a2279927d0be25cb455c4ee166",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T18:29:41.279785+00:00",
      "head": "9c3b88cdfc9132389c3465f965ca8013d3572eedaed75f5951593a6475ffcd0b",
      "node": "101.wake",
      "snapshot_digest": "642b806edbf914844784bdaac2a1ac4d212fd76dfe7a3544f82223385a7e4a61",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T18:40:52.790167+00:00",
      "head": "364f1ef99a1132c4cbf465ef4929cc1d8ae59b5b195ce3321b2217b166182c26",
      "node": "102.wake",
      "snapshot_digest": "058efbfb27bc79a89654e164eb18cd3b97db28cbf37dd843c5dc61de2ae779cf",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T18:32:34.215954+00:00",
      "head": "857843ec090429bd06ccd9e317bd31ba806773c2040dc1ae688c0a1406dcb48c",
      "node": "103.wake",
      "snapshot_digest": "37cc820567851b75c1ee352e5d5cab47f3fd9f3d988777b52b840d7df537d580",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T18:29:18.998089+00:00",
      "head": "176a407f2bcd2dfd0ede25c19e207e9c5f5197e8841cf4d0824518c0d1449809",
      "node": "200.wake",
      "snapshot_digest": "f8e7607d1b13bf21b8f7e3a21eae1ba2569dd47ee6055dd02fc364b7d85c3457",
      "version": 44
    },
    "201.wake": {
      "generated": "2026-10-26T18:24:21.722759+00:00",
      "head": "dfb7bfc2e766785399a739c9304dcf9082cc9c93fa61a1935ca4feb6d75f3256",
      "node": "201.wake",
      "snapshot_digest": "f21be0a9e7162762067b83e02f4c2c5e53899c6883718de0ae8deac4db579662",
      "version": 45
    },
    "202.wake": {
      "generated": "2026-10-26T18:41:30.813319+00:00",
      "head": "92df79f6ab9763aed2eaff317dfb7bbef2680f83ccba578df26440b9b6be10ef",
      "node": "202.wake",
      "snapshot_digest": "fa8331a1928128be5126f51e9d2f4662b716bc142608def903a96949678b7cdb",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T18:44:37.746447+00:00",
      "head": "3203d1852f8796798b1a01041195f6fb060059cf58ff99a1fc7002da3c2daa3f",
      "node": "203.wake",
      "snapshot_digest": "aa10b383e3d05478b31bf8692540be598c061981713e889e829b1027497a77b1",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T18:45:32.208001+00:00",
      "head": "e94f8561fc25455d3ed6e21e5a4fef763b8b43d30b4580e42f4de7fe39aa79c8",
      "node": "300.wake",
      "snapshot_digest": "511f089049eb6b7ef7ac87422f40ff0137347143cbd68d4705a937bd95f03f08",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T18:37:33.212865+00:00",
      "head": "86b47e53bdb576b4a2aae1a14eeeb99d21b97d8c4e588e9c5d875488a01741fa",
      "node": "301.wake",
      "snapshot_digest": "22f52345ac6c887444fde0b76130c679050dac1cf26ce0fcdb692663aab18ead",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T18:46:13.004238+00:00",
      "head": "f6a1d1c2db6033a0daff304a48d09822df184c9a5c115d7669af63f3bb8b3daa",
      "node": "302.wake",
      "snapshot_digest": "786d1bcf5e578a7930703bd24f764677fc90f22d187f03ead277f7cc99873a3e",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T18:33:12.208229+00:00",
      "head": "f29e729c4f51317452cae5adaa36f10e9deca4a177d59a8181e7ba7e9548af86",
      "node": "303.wake",
      "snapshot_digest": "97580ca5a228fa7ffcc44c91e338e5bdcb826bf7dc0abc92507246390315ef27",
      "version": 56
    }
  },
  "version": 577,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d61663465616336616131363634333563.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d64373563306661316132353934303062.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
