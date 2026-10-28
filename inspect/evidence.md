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
  "generated_at": "2026-10-28T22:16:52.993517+00:00",
  "head": "snapshot:6802a999f39e989181ff73df5c5516fb430d2492f10b36218754d080ce21e45b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T22:14:47.935138+00:00",
      "head": "0d0df15814ed650788c5d33a48d07a0676ee6fe29774a6908f83ec0ff142a174",
      "node": "100.wake",
      "snapshot_digest": "4b522d4e0ce15b9ff701bb638bb9b8f676d19a7bdc984d16938860727fe9e463",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T22:15:49.485786+00:00",
      "head": "13aa24e67470562672a7fa34776a6c8fef04ccbabdb1d7272ff36023c3fa81f7",
      "node": "101.wake",
      "snapshot_digest": "709d0b9c9ac1c8ecf37dbbc202a47053c4fa1171caa5c33cbca9dde51f0dd8b8",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T22:16:35.744656+00:00",
      "head": "6a35c5bf7d19c1c90298c37b3e6e16b00715de19993faf48a8542d825c56514f",
      "node": "102.wake",
      "snapshot_digest": "2c6003382326e2f29fe9d9e69cc3b8ac7cb46494694fec094cf80b2b4a29805e",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T22:13:57.122331+00:00",
      "head": "7ceaa1865ab1255948c5aa3e3681f7cdfd7dfe86145653af8d9adcdc076953a9",
      "node": "103.wake",
      "snapshot_digest": "0bda713958ab5f2ccb91758265239cb4d58391eb5917895720ffbcaa190d2b4b",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T22:14:56.477095+00:00",
      "head": "923d6fec20df69c147ca4341fb7fa838134def98203953b33078352abf93eb54",
      "node": "200.wake",
      "snapshot_digest": "05170b86970b7e3e32571633e81b5e57dc0f8577571a0353ede4276c6809932a",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T22:15:49.976150+00:00",
      "head": "258997d8aaf83bdb146a11fae50fd8c18f9f57136b2344158028e4213dc28b1d",
      "node": "201.wake",
      "snapshot_digest": "07f6c14462107cf93ee1fbcd5f87f520db3b79729182385b2db8e17396a9c643",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T22:13:40.572738+00:00",
      "head": "61b8574258ce19b2ba2261d0587cd2196efae6ac2faba207072123c89c28aa60",
      "node": "202.wake",
      "snapshot_digest": "b9e0a76a6de3ef6210a5b99ac367b4dfd8771c7945b20693c1cfebfb8a7e5fc8",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T22:15:37.121000+00:00",
      "head": "a5e42e2ff37113d48a8cc6c9eaedbe21b1d7ead742a586b9ee7fc31af99c4329",
      "node": "203.wake",
      "snapshot_digest": "4510cfcf933230ddf7faae49bae7d301ca5e5cbdfb8db2ce2cdf4e0977ac3226",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T22:16:09.001833+00:00",
      "head": "e2f8b65e4a1c6041b4cd79da092f2370d0bf911a44f67cc588d41cec906983f6",
      "node": "300.wake",
      "snapshot_digest": "ea8972f2c88b5d26863df23c2bfd3becfa2c69bfd022831badcea8455bc007b3",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T22:16:07.491334+00:00",
      "head": "8d0df6774d9bb9cea5a4c7b1003adb1e12bc5fa9f2316e72ff49da3cf89729b6",
      "node": "301.wake",
      "snapshot_digest": "92ec0820127e43bf0dc144cdc1df6a836e707b8674199bacf09f04dc4c290f2b",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T22:15:58.537410+00:00",
      "head": "13c9600b4d34302ff02f318eeb7fd42474a8befa36327c6358a0d90cb4cc3b04",
      "node": "302.wake",
      "snapshot_digest": "a048ef6d2bffc5a24327bff9b126d9389e00e0c989ed97a4a90cb00a87528178",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T22:16:52.993517+00:00",
      "head": "d004093e76ed21ae3a4d4718342f51c8a67a929ca40d0a189c73189561d0c960",
      "node": "303.wake",
      "snapshot_digest": "d29f3b2220fccf1d2aa2e0fe7bece4228303713b87b6d6ed53d65b4ad149f974",
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
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36353865303036353433663834366361.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d63336130393462666662303234633635.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
