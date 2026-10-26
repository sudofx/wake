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
  "generated_at": "2026-10-26T03:29:13.024030+00:00",
  "head": "snapshot:2beda3d760212f2561c880496ae094d6b9b0a2e2e3d7378c5c608ab339cae523",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T03:29:10.640452+00:00",
      "head": "49409557e670d4ac2cb32843d6a9ee4eeb7c130919e6510fea3336f5d156c02c",
      "node": "100.wake",
      "snapshot_digest": "55987dc5f8ef41333fa79582168fab51fa164ce3ab64a2e84c54c985686ed0b8",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T03:29:11.263486+00:00",
      "head": "908e748b7b4a95216d416da005dca6c84dcfcc14ef504d06e876b3130c50c59a",
      "node": "101.wake",
      "snapshot_digest": "1d269b00e5b15ee6833c207a936d1a93f9ce69d9b1b7951c849b4b5981e540cf",
      "version": 46
    },
    "102.wake": {
      "generated": "2026-10-26T03:29:07.009502+00:00",
      "head": "7a0e9166406c5e8be66610a91e38aa348a90df5f7323b25a9ac82f8b4cbde17e",
      "node": "102.wake",
      "snapshot_digest": "bb69ea85f2139ef9bfb5288d2c4d622cae5e1b1818e2ecc40f9df8e37bfd1752",
      "version": 60
    },
    "103.wake": {
      "generated": "2026-10-26T03:29:10.686136+00:00",
      "head": "a8547f221262ab8bc811c37469c3c558f202c3a6f791c1953786723af9a0e2e4",
      "node": "103.wake",
      "snapshot_digest": "747aa7cbe287297df7da02089715d756630b1967a2b4b6628ccab8906b97e636",
      "version": 41
    },
    "200.wake": {
      "generated": "2026-10-26T03:29:10.935967+00:00",
      "head": "fc1ccff4c842b9c0f9b2c0058517abe48c9fe2780a189f94b9b640bbe737b797",
      "node": "200.wake",
      "snapshot_digest": "7373a847c1d9baebd911e1177a60c8caa925e89d2d28d643c7c7ab1082c95cfb",
      "version": 37
    },
    "201.wake": {
      "generated": "2026-10-26T03:29:13.024030+00:00",
      "head": "43b8cd6a2541c448bd4fd7525b6aa9a4af18cb86d7ecc09f0fcf16717f4517ce",
      "node": "201.wake",
      "snapshot_digest": "920e47de8fe6a0dbcc7f579238ca4b54c3d33f02100354e7561d0dda84da8648",
      "version": 42
    },
    "202.wake": {
      "generated": "2026-10-26T03:29:10.275879+00:00",
      "head": "a3d7631d74f465a4c00619589fed0b442a37ad77b2728e5e86b11a2c726cdb20",
      "node": "202.wake",
      "snapshot_digest": "56745a50c17b565357af25a68415da0645238b3cd13b8d75ba81efad5b1e942d",
      "version": 56
    },
    "203.wake": {
      "generated": "2026-10-26T03:29:09.829510+00:00",
      "head": "e2e899c81c1ec8728e64a55f4de83d5f9ce9b363108c7d18584bc53417fd2e60",
      "node": "203.wake",
      "snapshot_digest": "05300ffa6f47218bfaaa69a9e857af26e468e08ac8229922bd44769a56e0e8c5",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T03:29:10.682485+00:00",
      "head": "8af7245d748037a2fd646f5c0f78b9e1f120baa0a18c5c8d6fe29f831247238e",
      "node": "300.wake",
      "snapshot_digest": "aa86769599e3da4136b4388e5d6b226045508ea09f1a3b90c1a657b3356ac7ab",
      "version": 36
    },
    "301.wake": {
      "generated": "2026-10-26T03:29:06.147411+00:00",
      "head": "2ad36b37255f168ca243a5e79964b48e2292c2f9a9e2e545be27c8d97f212bb3",
      "node": "301.wake",
      "snapshot_digest": "18e7e7e6f6b968adeff9be88e0626d11be6c495fea8fd96125d1226d8773d501",
      "version": 59
    },
    "302.wake": {
      "generated": "2026-10-26T03:29:11.380364+00:00",
      "head": "02635ff19e5bef68b59aa9c6fe2eb547fdff93281eb2e0ba66a1ba7848ac53a6",
      "node": "302.wake",
      "snapshot_digest": "afd29acd7d197cfd7339ec82de8b39ef98a24425c4cb490ae8b3c3a80dd847da",
      "version": 42
    },
    "303.wake": {
      "generated": "2026-10-26T03:29:12.501722+00:00",
      "head": "3f6af80959e0db2364ba635adc45932a5db45c79386775c71badf7ef703a6442",
      "node": "303.wake",
      "snapshot_digest": "21d737d181ed6908fdf15388173fc0a8f214abe88d8f8f975027b79b5d652a47",
      "version": 52
    }
  },
  "version": 532,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a722d31333166356538306261656234343433.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d30333761643462323538643334356662.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d726573706f6e736962696c6974792d666f726d/6174696f6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
