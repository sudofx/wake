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
  "generated_at": "2026-10-28T12:24:07.933946+00:00",
  "head": "snapshot:1d766d49d8fc13e8d1b517c39b7c16119cf74031c1495643e7cf7f713ea41398",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T12:23:09.874599+00:00",
      "head": "25f4e961526f58a97b2b46646ecce32fad9df68f8a31f8396f108a05d28be903",
      "node": "100.wake",
      "snapshot_digest": "6e020b11f0215925da42e60e1914bc7dbf109b33f19ab45e1ce7e803221e2691",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-28T12:22:28.002613+00:00",
      "head": "f737ab5c8bda03a655567277677009436a4de681dbee758dfdac8b09644dc13a",
      "node": "101.wake",
      "snapshot_digest": "193df59f161429fc7c2c6c7f3d30ae9f37d798d3f63b66eb6749e38092f7019a",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-28T12:22:37.215013+00:00",
      "head": "59426e21dc54c710717e3baa7233c8606d1291260bd606f8596b5c6e8796d72a",
      "node": "102.wake",
      "snapshot_digest": "bd42c75c0422e94662cf1a1a4732c3100b12fc55e6f4464a048fae37688f7f78",
      "version": 12
    },
    "103.wake": {
      "generated": "2026-10-28T12:22:25.502946+00:00",
      "head": "595650d6cf0728448e2d5ac33e34b4c16e93bf069b6b4c91bf56c35579bc9a65",
      "node": "103.wake",
      "snapshot_digest": "ee98f4f382478b72416a8bf52472d5ec6ff0f4c6f781f1a566590bc57105de64",
      "version": 25
    },
    "200.wake": {
      "generated": "2026-10-28T12:22:52.026467+00:00",
      "head": "0c5cd8121f9a5df54c3e5b168eee262bc9ece0ff8e7c4b8a370b4e18cc9f5c4d",
      "node": "200.wake",
      "snapshot_digest": "576467428595bd8ebdfb802b66e15e7a04e96da04cb819c98e36e002e40e75ac",
      "version": 21
    },
    "201.wake": {
      "generated": "2026-10-28T12:23:47.288486+00:00",
      "head": "1d1417c51b59129024ffd1e03b572d7a838b2c9311d253715c2ed26e65cee71d",
      "node": "201.wake",
      "snapshot_digest": "931540057c1e9a0b2a72814a96a2301ce591cf86ec8090f4258da9c631a3398c",
      "version": 18
    },
    "202.wake": {
      "generated": "2026-10-28T12:22:13.541097+00:00",
      "head": "edd5f0fb060f882c01acc7ad71aa85e4e896023e4f1c20a0830ccebe27ca7549",
      "node": "202.wake",
      "snapshot_digest": "d3e5483744be031dd76193f4918904c093ab17a3fddda7d86d9326f5ba95bd6a",
      "version": 22
    },
    "203.wake": {
      "generated": "2026-10-28T12:22:10.932407+00:00",
      "head": "1179dbea3a33847fd77e360c1977be8563712a6c294b7d93c813521ec19716bb",
      "node": "203.wake",
      "snapshot_digest": "34109064fce22e661b622ded2e9fd2eabc78dea468fdec5aa5f4908ac74c7dfc",
      "version": 23
    },
    "300.wake": {
      "generated": "2026-10-28T12:22:05.969513+00:00",
      "head": "35cb3f601b27bdd2132bcf1184a1fe622da92c1e74a92ccb1bdca46339281fe0",
      "node": "300.wake",
      "snapshot_digest": "64ef0ce0c668a858dccc7c0000af195998ab02a8bb0c72ffc750461f19099010",
      "version": 20
    },
    "301.wake": {
      "generated": "2026-10-28T12:24:07.933946+00:00",
      "head": "6755bda0ebe697a0833e6c4ce9ee245877de14c533db2acbc71ed96117cc75fe",
      "node": "301.wake",
      "snapshot_digest": "5321d95dd2d1e7eafcfe11b43cd5b4807bb1d98db684524ed9353f934b8c7e29",
      "version": 15
    },
    "302.wake": {
      "generated": "2026-10-28T12:23:44.055643+00:00",
      "head": "8c0201569e35c0c9df498a4d88a563f82d5fc83a9e0a894927de2002649a90c4",
      "node": "302.wake",
      "snapshot_digest": "72914dfe69d32fd3af795b3ada784dc2ab47f881ee93407802cb4c5255ed190c",
      "version": 16
    },
    "303.wake": {
      "generated": "2026-10-28T12:22:03.871004+00:00",
      "head": "aaf93cf486fa2b16e91d5a6d229883339cc11498f6f3032be355cbd3beb8de86",
      "node": "303.wake",
      "snapshot_digest": "2e9843b545f4305096e5cbd0b2cf8f1caa396915d627d58478379e402f8f576c",
      "version": 19
    }
  },
  "version": 225,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34653965636364643636383734346232.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d38643637663366306163663634346265.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d6175746f6e6f6d6f/75732d696e71756972792d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
