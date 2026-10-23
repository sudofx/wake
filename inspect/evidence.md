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
  "generated_at": "2026-10-23T22:13:25.302506+00:00",
  "head": "snapshot:23b6977560b84b474a6c0df03df570042fc84df549cd60b88b3187da9ea3350f",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T22:04:02.239949+00:00",
      "head": "5e341cc2a3c97c4d714b7e0840ea0ec9fe90fb794f11d1c88f530b1b32639528",
      "node": "100.wake",
      "snapshot_digest": "2d2b112aca04458450d0d194a8e6b1433716f3df9f0572b65f9644299be8b8c7",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T22:04:03.942959+00:00",
      "head": "e0d68c2a0b67500ed993f27f31aee5e437b85cbb9766298fe812e0d7de413e87",
      "node": "101.wake",
      "snapshot_digest": "538e29a319936754041654f468dd828913f0a4725a0990afe81d51cb1b1a772e",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T22:11:52.017472+00:00",
      "head": "fc395c774fbbcc8a80a52695de84e2371de1acd27b242572b99932a3bb18fa6c",
      "node": "102.wake",
      "snapshot_digest": "39c4c013a213a81c4d28d183e30c023f308bf17015e217aeb82c71f714292686",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T22:04:04.032463+00:00",
      "head": "efbc6f56cb57797cee5b2a29eb26b100832fa32dc7805e174d380d38e365bdcc",
      "node": "103.wake",
      "snapshot_digest": "ad034cd70248843c85339cd17dd0eec98fbd32fba0a4fc6140ab61523c089583",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T22:04:04.012852+00:00",
      "head": "273b4ec678e5e27ab695d9093b94a2f7501f4159680ff1ce6851bd773263f386",
      "node": "200.wake",
      "snapshot_digest": "78b0e059fee7980a24c674ffc38c2f1d7847eced0d8a29c60ded2f60f2d59819",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T22:13:25.302506+00:00",
      "head": "79892960bfd51fe45b16c2cd2df867b787cf8a0916c4fbbb3eea800d6f00ae6c",
      "node": "201.wake",
      "snapshot_digest": "fbe9f5482be7ee718d71eb2c79912c547fb45c33b0f2a60aecc6d8d7a6bbccdc",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T22:04:03.749502+00:00",
      "head": "0dfb1768f04f3ad2dc194ba5630390a496b70690ac2af422e3ae4008214e899c",
      "node": "202.wake",
      "snapshot_digest": "351fe13cc761425de02b99cb3bd7f27c048ed5f70b37a0fcc3a9b702bfed0f6f",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T22:04:03.220760+00:00",
      "head": "0a8c8597bf334b2233315157a44293459ca2d3a10066db2c84825e54d9c084ec",
      "node": "203.wake",
      "snapshot_digest": "0dc210cea2cd093bddcd61498b7dc1ff04705c5dce4c5f42c2327fcab3a416d3",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T22:04:03.801428+00:00",
      "head": "7fc8a910d9f3e3a16e3fe5a274d0497438bc2443dfd0160f1b93c7882648a30d",
      "node": "300.wake",
      "snapshot_digest": "dfb87db1c79a7e95a7340cbbcbacf2d81276ac705838ed291591375fee3e77ae",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T22:04:02.604612+00:00",
      "head": "7fcf103e7c2523ec47e6ccd9ac48e23f4be5600da7be5a71945f5510e76fabad",
      "node": "301.wake",
      "snapshot_digest": "2f66468a91fdd9bfc406252290cdfaec2b48333e085c1e87ac2b619dfe529259",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T22:04:02.901080+00:00",
      "head": "bbd49da508d5727551b86a46bcd3417053e6a8e95d45e3859011092804e83796",
      "node": "302.wake",
      "snapshot_digest": "75e20245e0672038c1711addff6a483962ac6e984b284f688a8f6f7da306c999",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T22:04:02.627989+00:00",
      "head": "e9c42272bf1e49c9ecdcfe88c41d27cdfc3a29de11b9d3d928812bbcce5ebcc3",
      "node": "303.wake",
      "snapshot_digest": "4daccda348c48fbc2a66b7f78de2acb05229e9987fa7055cc4b006315885d337",
      "version": 36
    }
  },
  "version": 337,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d63303439623530653237303234646532.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d61643235613439353465633234373137.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
