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
  "generated_at": "2026-10-23T13:31:31.497860+00:00",
  "head": "snapshot:79c563a53fb859ae170f9707c36ded31cbe48ce9e995573f4b5914ef1a8f1a77",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T13:18:16.132374+00:00",
      "head": "5dd9df759fd173aa08025478a91a9a02977b05afa1b5efcf7b3f274a80e5bc17",
      "node": "100.wake",
      "snapshot_digest": "e6da044f5dd7db26c73768c62292648e5c8efc848a4922465f60541cc09529bd",
      "version": 14
    },
    "101.wake": {
      "generated": "2026-10-23T13:06:42.074344+00:00",
      "head": "72f1bed6c9b4363344d68047bfb47fffc8ad8b4bb8302ec42576597507add5b5",
      "node": "101.wake",
      "snapshot_digest": "8e98268372167f5da53a9f5b5a6a2c86470be40776f7e0f4c1a5dead604608dd",
      "version": 22
    },
    "102.wake": {
      "generated": "2026-10-23T13:28:44.520912+00:00",
      "head": "4928da1e0c35fb17f9592526c2c54ea19261802ad13f1b4b56458cc1ace1a48a",
      "node": "102.wake",
      "snapshot_digest": "d677e82069e0309d5de60fb23207df4549871ebee07e7d84e0806c67b59875cc",
      "version": 29
    },
    "103.wake": {
      "generated": "2026-10-23T13:06:54.794405+00:00",
      "head": "fff96d530be12dab11150a07dc1252eb0f646ae6606d8332388be645a2956e90",
      "node": "103.wake",
      "snapshot_digest": "15317f72bff21bf067ee08829dfb14543575fe619245931ff8b4425625178a5a",
      "version": 17
    },
    "200.wake": {
      "generated": "2026-10-23T13:09:02.196141+00:00",
      "head": "997bad284af71a1868af7293fa2e5386f0b491c3e606b3e825d02f0c93f0a76c",
      "node": "200.wake",
      "snapshot_digest": "0706e7dd2ffb58c154eb6360b71892884f6888fa8856c6acfb4ff438162c8fa8",
      "version": 16
    },
    "201.wake": {
      "generated": "2026-10-23T13:08:18.999134+00:00",
      "head": "a25af9d0c87b28822b9a714a30a6c6df03d3a825ff661f6750cffd459ea77c94",
      "node": "201.wake",
      "snapshot_digest": "bc0db3335f3ddd15038e097c6df5dc5787a8ff0539f0a850d80bf8a2e6543c94",
      "version": 19
    },
    "202.wake": {
      "generated": "2026-10-23T13:08:05.306617+00:00",
      "head": "c79fe40ccd1c39d5b85c72c4db2ecbce5dea6f71bed110ae117704d0d4886ce5",
      "node": "202.wake",
      "snapshot_digest": "0962584df8b3e069eec022466d3804da30b0522d89c59d806a539169d010c0fd",
      "version": 29
    },
    "203.wake": {
      "generated": "2026-10-23T13:07:45.836172+00:00",
      "head": "89a24020e4f1ca1638b5ba87b5f516148343975942342a45e0f4cd3a65357bbe",
      "node": "203.wake",
      "snapshot_digest": "30129bd6ef45587eec756c3192fd98e74fc18459b6e1a446f78b5eb7205c2fd3",
      "version": 12
    },
    "300.wake": {
      "generated": "2026-10-23T13:29:25.201314+00:00",
      "head": "5d3c87a2c457c5876cc5d81719ae55f0dd93d903c98796781034d296e29f3ef2",
      "node": "300.wake",
      "snapshot_digest": "bbd5a7b69ba8d28bb483c3ff99fec0b721791712bb2389045450bab639c8d066",
      "version": 17
    },
    "301.wake": {
      "generated": "2026-10-23T13:30:12.692151+00:00",
      "head": "2db7b5535bf1535c87e462ecc4aea7e70d55c98f3a9547a2186b7bd7f2cdc1f2",
      "node": "301.wake",
      "snapshot_digest": "16d7e4d2ed2f2acfeb0bc56cb113ffc963c2248a110c72889c2451f1dc7b0dc4",
      "version": 26
    },
    "302.wake": {
      "generated": "2026-10-23T13:31:31.497860+00:00",
      "head": "1806aa7a3c249be244f4fa245c4502e568171675fd6a114a5cc335612af1adb2",
      "node": "302.wake",
      "snapshot_digest": "c85e4db66c0d8c8b2e7c16b70ea4c4b2ff8bc57b70a0dc39e6e3d97ed75ce069",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T13:05:54.261907+00:00",
      "head": "e15bb1692074f3c365af5e20675250c45c9ec019a8ad528faa735caf544ae9a3",
      "node": "303.wake",
      "snapshot_digest": "6d84bb8c6f6cebb13b360197233f7a5ac34600398f473c5e5497ce1f38e7fddb",
      "version": 25
    }
  },
  "version": 238,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d336161303363393132343036346134/63.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d643036316365643134653139343364/31.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6761/702d69642d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
