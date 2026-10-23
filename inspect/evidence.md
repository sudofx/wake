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
  "generated_at": "2026-10-23T17:19:59.819939+00:00",
  "head": "snapshot:0e2245c3e21623002f9beeaf2cae627bd1eacf4364344c1b9b000d6ab3a914cd",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T17:11:30.183244+00:00",
      "head": "93880b9a4f565a58a1e7a8507ac4b17c33316d604aea5ae667a05f5b497df3e7",
      "node": "100.wake",
      "snapshot_digest": "bdbad648f652d08b54beac0266b476d54c36d97e473f32f634345a419c33256d",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T17:12:47.787288+00:00",
      "head": "10ce8ac6f0c20eadba7f84f69c1c11540fc4f9b340ee15afde6f07371ed32049",
      "node": "101.wake",
      "snapshot_digest": "c455b42bf8e81b2f72b7e36fc1296a07f343ad7e5f7df37543f983545a2609ee",
      "version": 26
    },
    "102.wake": {
      "generated": "2026-10-23T17:11:15.775206+00:00",
      "head": "3cb0d9a73e1db72d1903081d92e9bc0b836f0436163d3da7157c0e3c040b355b",
      "node": "102.wake",
      "snapshot_digest": "6e6de6b909fe43dad53992e9030fdb0b0fa6aefebb121c06d0310059bb362488",
      "version": 33
    },
    "103.wake": {
      "generated": "2026-10-23T17:12:08.140780+00:00",
      "head": "a0c4d8cd76a2efe618df4317988c6cfdfbd13de5a5f47d3787ba80077948754e",
      "node": "103.wake",
      "snapshot_digest": "6109f4f0cc65d9b57e0c947e70bd688cb1f77ac475bbe8978fec63d9cd687e37",
      "version": 23
    },
    "200.wake": {
      "generated": "2026-10-23T17:14:48.693355+00:00",
      "head": "f82fda87ab23010d82193354ea4dfa38d4b547dc571cf5154260d6f4a5921b24",
      "node": "200.wake",
      "snapshot_digest": "f0157818ca1caad063969e19ca0f24a014de62e0e87cbab494e144b0ee381e5b",
      "version": 21
    },
    "201.wake": {
      "generated": "2026-10-23T17:12:40.371679+00:00",
      "head": "9966f1934dc70ab7c6315631a973c98ddaaf5c5b3b70ecc0ab142f6d9d887d2f",
      "node": "201.wake",
      "snapshot_digest": "739955f113682346b825532456bc7bcf8e1198d0c3b27cd64d0e150ccbb8876c",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-23T17:14:06.967129+00:00",
      "head": "ef37a6a18e6ff8385fdd0508d57b46e0a8ad1f64454b4e24f57ec21f3048ce05",
      "node": "202.wake",
      "snapshot_digest": "aaec640f59164f6c4f2d98902f05477241472035ee53a84ee75a0e1790435b45",
      "version": 37
    },
    "203.wake": {
      "generated": "2026-10-23T17:10:08.552982+00:00",
      "head": "17ba29382d6a9430bf16dcc2f903fdc1b3b089735cc34f1c5e5a7377c78c5881",
      "node": "203.wake",
      "snapshot_digest": "20371f25d6103ed947c17958d0935b9c190e418dee8d9503506f8f54bb51703c",
      "version": 15
    },
    "300.wake": {
      "generated": "2026-10-23T17:13:38.287379+00:00",
      "head": "a9af7f5961153a2f07c932cc3cbeb380e9bf6998ccf85bd6e991b5e1c1546235",
      "node": "300.wake",
      "snapshot_digest": "12b28e5ffd35f6186737934762d6fff98427c13019452715bf870ec0df3f69a8",
      "version": 21
    },
    "301.wake": {
      "generated": "2026-10-23T17:10:21.804062+00:00",
      "head": "e3b66b7eeb531e589de1c5dc8c575f12ba3d5eacc9ff0b184ecc6fcbd5353f8d",
      "node": "301.wake",
      "snapshot_digest": "5f57c483ecfc9075e715c48621697b9eb557048f41fd81e84448edd77a74dd56",
      "version": 33
    },
    "302.wake": {
      "generated": "2026-10-23T17:19:59.819939+00:00",
      "head": "2533b96f3c703259daf18f1d7f4da94935cca76ccb693a9cc07c5a238bbef5ff",
      "node": "302.wake",
      "snapshot_digest": "095f823a83daa55c8dbc200d7e4ba66c3705e62b228115b0e926db59705cce40",
      "version": 16
    },
    "303.wake": {
      "generated": "2026-10-23T17:11:02.697065+00:00",
      "head": "caf3e7f223935e179bd38b6bd061a2c00c18e906722f78fcf584e5f462da06b4",
      "node": "303.wake",
      "snapshot_digest": "2ef57a3f13d28e74882156298d28307306e4e89e337f016468d772d829355c17",
      "version": 30
    }
  },
  "version": 293,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d37323063663066643464636334316236.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d64333438323364383664396434366631.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
