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
  "generated_at": "2026-10-28T00:47:38.293526+00:00",
  "head": "snapshot:1537247984fbbadadb69d9f0e8f014e07d1146fcd3a62b66b294f75fdce4f0cf",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T00:47:26.405535+00:00",
      "head": "0edeff46bb973d0f9b35b56bd034a7da6169eb54e143c63828de9e9cb929b095",
      "node": "100.wake",
      "snapshot_digest": "d48fb42137d87091b837f34c830b8e4daaa89a6ce3527bee58d35ff08c805efc",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T00:47:11.515467+00:00",
      "head": "8382c6c1c88303c1feb684a36f3a643b2585bab81249982b40cfbeb816fd403c",
      "node": "101.wake",
      "snapshot_digest": "86c76a5ea3196cb194a7e30ec977c1b663035bc3cda9ad149dab4348f5dc2caf",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T00:47:15.141079+00:00",
      "head": "7b7bef7b273499e828dd61e052c6705f9232347891df43d8eba4ab2135677b99",
      "node": "102.wake",
      "snapshot_digest": "d9f3736f89fe98a2b0b173d43c52e2876c047e4120501ba3561522ed7d1a6a53",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T00:47:32.865997+00:00",
      "head": "fe9c84d450452649312d6ab5fd8e1da832825c09733882ff56492c5f1e82f6ca",
      "node": "103.wake",
      "snapshot_digest": "d715692c189bb210afd81a331c82d61c1bf5edfe322c154038080cd85eae0e67",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T00:47:34.886704+00:00",
      "head": "cfb0630577b6fd28509b0c864663efe66118921bca29420c82f0e41d051f9952",
      "node": "200.wake",
      "snapshot_digest": "1cd6582a96e78287dfe3343424b4bc5f8df2d2719eb8524e9f4ba292e8fdd363",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T00:47:38.293526+00:00",
      "head": "ded2a0baeeb0d05517b9791c67fb9bf89c4108b14949bfbc2bfb21f9db280001",
      "node": "201.wake",
      "snapshot_digest": "3b012bc117ca0fbdf57e101c50957134a545a7a5b7dbbb99d0ce1fb0156afc3a",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T00:47:19.608913+00:00",
      "head": "28b8596b47cdbf60a9dbfeee6d527bb2e1dcb6f1423b0b12a64ae9ba63e61c85",
      "node": "202.wake",
      "snapshot_digest": "9087923ab4a4140f022de5c51694fd81a09f3bfa5384cc1713d0c21a2349ec10",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T00:47:05.700576+00:00",
      "head": "b9ae93bcf78005cebd4801b16b2f70fc7bfe5df6880f9b6839bcd6d6fc8a2e78",
      "node": "203.wake",
      "snapshot_digest": "7c8bec5c8c51a847d3c41b9359a97c85862bb0d2f79889dd25a3f27581ce3df9",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T00:47:15.808050+00:00",
      "head": "111acdac3a529a270cf1a971087852e032b91a9d5215b81ac9c15f45857d96e5",
      "node": "300.wake",
      "snapshot_digest": "4cebdd707f984214999353074bd29ec199cd78d70ad734729251ff464b68195f",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T00:47:22.175965+00:00",
      "head": "dd8ed9edb77b32f13a5f63613545a65f5937f75a1f24a90e66dd833268d643ea",
      "node": "301.wake",
      "snapshot_digest": "e8bbcaae99864b2f48db79a4e215cdd0b7ddfbc2aa8c515da6fd38f1d672b5f4",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T00:47:11.527185+00:00",
      "head": "67653fdd80ee692981f5db1ebfb64b82a348e21d225f5a1e37b2fe4c2271a4f1",
      "node": "302.wake",
      "snapshot_digest": "f810dbe1351552524e8266988ca2b23b9a176b3535010f614292ded8ad97aff9",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T00:47:21.607298+00:00",
      "head": "f2e46e5643a21d39af71de7403116675c8398bee156e98a426dc9b758955c7b0",
      "node": "303.wake",
      "snapshot_digest": "fdb3cb8b77373dc9e9aaaa2517649b7bca1ded94239be182fcdef63064720234",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d61653131366638306463306134336566.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d39343338633263316235366334343838.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
