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
  "generated_at": "2026-10-28T13:17:35.581247+00:00",
  "head": "snapshot:29a05976aac2d5372e14af18d3ebc5a0a0c6105c723c3249b766454a34b087da",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T13:05:15.989051+00:00",
      "head": "956eca61bb9219a52248d82a49a730efa17733a2cb5a1be381ce4ef0a4498c69",
      "node": "100.wake",
      "snapshot_digest": "aa107ff2e94c2fa381eb19efe427e5cc9c49a4e7a65c4d67090f6324500002e4",
      "version": 18
    },
    "101.wake": {
      "generated": "2026-10-28T13:16:55.377599+00:00",
      "head": "50d7714376aa92437692502d62c443b01c47830fcc36331181de2a9eaa4d0670",
      "node": "101.wake",
      "snapshot_digest": "26360474b91d000e61a662764787efb3351b9d6a3f39a862134c4f6d92a4ec76",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-28T13:16:14.982932+00:00",
      "head": "9a5689f46fd5a9982959fc2620b85051ae0d7b40a6f1dc31f507899e2d7031f7",
      "node": "102.wake",
      "snapshot_digest": "d1e4bb5fba59915009be1bc198e2998e20edbcd13288fc1b90647a8c6265fac9",
      "version": 14
    },
    "103.wake": {
      "generated": "2026-10-28T13:17:35.581247+00:00",
      "head": "df7e3571c8b3c6918f3a2e37b5c23dfac4dca3f6232a97421fe3e9c2422ae318",
      "node": "103.wake",
      "snapshot_digest": "b36ae407693b8d9f73f959d9f001466876c4e4d27150f7cd24dbe3b0ad59d23d",
      "version": 26
    },
    "200.wake": {
      "generated": "2026-10-28T12:58:53.700203+00:00",
      "head": "f753d538bee8a64c877a46510e6cb7b460eaf0e436326676aad92e8797c49ba4",
      "node": "200.wake",
      "snapshot_digest": "b885d11ac5fe82e8359b986bde9a9ac35cb48f2ca94669c6b44342877c49ec88",
      "version": 22
    },
    "201.wake": {
      "generated": "2026-10-28T13:01:21.606071+00:00",
      "head": "ead8dfd227eb8c403886eb27ad658f71b2865c4c1af8f505b6d40ee564903324",
      "node": "201.wake",
      "snapshot_digest": "0539b71e8e98e3ea9d6c1415fe4048e4a8c1788ad5a7c6104647e5bb6b90864e",
      "version": 19
    },
    "202.wake": {
      "generated": "2026-10-28T13:16:35.671901+00:00",
      "head": "7b6873f05bd1e111b498573fa5c5a9c4a4576212d0f78c1ee2b80fa7573a47ac",
      "node": "202.wake",
      "snapshot_digest": "37d0fef3dcd571ab0348a29f75e4d7023b6b51a1d5140bcf8f2462ade40b0299",
      "version": 24
    },
    "203.wake": {
      "generated": "2026-10-28T13:14:27.444637+00:00",
      "head": "8f54b9cb5671a805b244d5e6cf499985f25cc5222892c5274bb51d43a73c65b9",
      "node": "203.wake",
      "snapshot_digest": "11d761e7d48a0b0fc8dbd8d645774b0671ff73ba1f9d436677f8b05359733711",
      "version": 23
    },
    "300.wake": {
      "generated": "2026-10-28T13:15:31.407701+00:00",
      "head": "ffade36033bf2b3b9ab73d19b6cb53a77effbc3568566012516c3fd8b15935e4",
      "node": "300.wake",
      "snapshot_digest": "d2a9c0f98686259f427b9d4132080041f24d75d644751337e366bd8aa96dd1b2",
      "version": 21
    },
    "301.wake": {
      "generated": "2026-10-28T13:02:37.748225+00:00",
      "head": "1d204905548f936555061fcd1abcc01da1bdb58759a1f97394e3bb120eda02ea",
      "node": "301.wake",
      "snapshot_digest": "efbbdb2e11bddbf16d768ca880e249349feb8b9107699888b81e72108b875252",
      "version": 15
    },
    "302.wake": {
      "generated": "2026-10-28T13:02:30.994634+00:00",
      "head": "3a6dc4c03debbed72776c890d8db06e7feb776028e5c51a12d6e5d729a4784f2",
      "node": "302.wake",
      "snapshot_digest": "173c62eca6aa7b0932b09963c688fb787c1e7379bbef489d750e193346b503d7",
      "version": 18
    },
    "303.wake": {
      "generated": "2026-10-28T13:15:40.030073+00:00",
      "head": "b1eac1495754127a9f03ec5245b98bbea12187f8a9ffc503c9b6688cf84d36c7",
      "node": "303.wake",
      "snapshot_digest": "ddf39a7634105b2d3646f54931e26bf39db247a14efb7fb0c2978dd28313522a",
      "version": 21
    }
  },
  "version": 239,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d39633666343463633931306134323964.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d63653462386436646461336234666566.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
