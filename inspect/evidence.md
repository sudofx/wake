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
  "generated_at": "2026-10-27T02:46:52.877425+00:00",
  "head": "snapshot:e706b44f1ffd6eb07b8f095dfb5e038cf35b467f23d340d63dacb1303932fde9",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T02:43:47.036910+00:00",
      "head": "e8a7db495091c313d3504026fc3cdc843fc82758a8ce704e07639328a48aae28",
      "node": "100.wake",
      "snapshot_digest": "3183db415a72aaf88c76bc5393d56926d7f655c90104c66d3f25fded126f1ca5",
      "version": 33
    },
    "101.wake": {
      "generated": "2026-10-27T02:31:12.722561+00:00",
      "head": "749f28f187164ec334b79667e57627d5295444fe69fade800d42b7bc9c7af453",
      "node": "101.wake",
      "snapshot_digest": "24d607a4c6be9598d676637d05f7ef1ad710ae381d64a99e76f27cc63b7a9aca",
      "version": 49
    },
    "102.wake": {
      "generated": "2026-10-27T02:46:07.972372+00:00",
      "head": "f625a3100466a4fb59e15e2ebb685b5b3cb27bbcbe43109ce25f3582d410b8ac",
      "node": "102.wake",
      "snapshot_digest": "ebfe96e693126cc35a4649903b4b0d60cc184bb9886f7a1ecdf6f1e7aa7c18ab",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-27T02:40:32.463097+00:00",
      "head": "bd0d11422c747c139a8411cceb12a35a8f733a624cf515b4075b4253bde68158",
      "node": "103.wake",
      "snapshot_digest": "f254f2db12cc625bbc72b23781bca1319c36b6424a75eacf4af29d9ee33dbe7f",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-27T02:46:52.877425+00:00",
      "head": "6720c62fba5a61237e3b77fc0c3a1548d9141890eed6dbbf38469f05ae8959e2",
      "node": "200.wake",
      "snapshot_digest": "a8215b23493ed27ea386aef90f55cf34b3b88dafc347d2bea1a051370dc7d8d0",
      "version": 47
    },
    "201.wake": {
      "generated": "2026-10-27T02:01:36.886740+00:00",
      "head": "76a2cdeb6d3394e576cf1e7debe381236bb5486f83852627b7e696a72e7e6c71",
      "node": "201.wake",
      "snapshot_digest": "16ac32fe47089ec08b0849e7c52c702595080fc8b25354a35cea8d3f8cd015a0",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-27T02:27:27.406574+00:00",
      "head": "4ea71f536cc37be3278dc26cb219e02f893b4c8780c18a3ab6e6520a8f56c429",
      "node": "202.wake",
      "snapshot_digest": "dd90475bfb583815a2bf6509245cd7116519a49a55ac97624e81cbdb4389a5db",
      "version": 62
    },
    "203.wake": {
      "generated": "2026-10-27T02:43:32.629282+00:00",
      "head": "63ab7a9d05eea3868bb19a6de451c63343a6e17b743135891127122a434393ac",
      "node": "203.wake",
      "snapshot_digest": "aca66d9b47960c84b82d2ee17fb7179394b3465d1a32c09590c74b887cae9b65",
      "version": 39
    },
    "300.wake": {
      "generated": "2026-10-27T02:15:25.058148+00:00",
      "head": "b812f55b2b94fa13303d70bf60c9a2f5b6eb6e0ae5eee4e3b64ccd15de2046ae",
      "node": "300.wake",
      "snapshot_digest": "8777ae5689727b12901078194199dca1b4e25da0c9032dd846094c4bccf350c7",
      "version": 40
    },
    "301.wake": {
      "generated": "2026-10-27T02:44:30.934720+00:00",
      "head": "9cd7bc4d19db27ec10179c0257ace2ced7a68f819d004ae864acc99135de2c57",
      "node": "301.wake",
      "snapshot_digest": "190c33e9f2df197e7e935962b5977c521ecd9262a1a438fd05c2fe6deb5fcf79",
      "version": 68
    },
    "302.wake": {
      "generated": "2026-10-27T02:36:38.973472+00:00",
      "head": "b4e290dcb1a659e2c92932ef4683ec1370a68916828fc4d6ff6ed346885aebc5",
      "node": "302.wake",
      "snapshot_digest": "5e4c5703dfbff5c0a05ee067f291f27efb60ea8f88d4c5926321a9897a2a2701",
      "version": 49
    },
    "303.wake": {
      "generated": "2026-10-27T02:34:39.473261+00:00",
      "head": "53eee2446a2979f4e71302536cc5f02abeec314043bdac336dd16daeb3c4dcaf",
      "node": "303.wake",
      "snapshot_digest": "9b36440bf2820fe94730a01e51821359a1652414d49ad32c53ad5c19161d340c",
      "version": 59
    }
  },
  "version": 600,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d343937653763633938643230343831/39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61313861646636386238633134343639.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6761/702d69642d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
