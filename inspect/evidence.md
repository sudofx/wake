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
  "generated_at": "2026-10-27T13:26:55.782238+00:00",
  "head": "snapshot:30d24e0679f042f8d7750df37564d4bd700041d5410feb0356a24fb01323ace6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T13:26:10.931411+00:00",
      "head": "536fd313c37c1533d5cdf336b9f139021062c6f55a68c72bc62f00afccdd4c6c",
      "node": "100.wake",
      "snapshot_digest": "874436372574cad4a060d1989e587a0a659a4e0ca4d4dfbc94c222d7740030f3",
      "version": 3
    },
    "101.wake": {
      "generated": "2026-10-27T13:26:25.357378+00:00",
      "head": "457bcb958e83e6139dbb491a48e8f3ed136b8d93ce9d98b6947c5a6a773d40c4",
      "node": "101.wake",
      "snapshot_digest": "3045b746755801c42b3dc9dcaa78e8346547c068e4970290da044741337ae2b5",
      "version": 3
    },
    "102.wake": {
      "generated": "2026-10-27T13:26:07.402094+00:00",
      "head": "1278a33f67ef408b106db4af28e490fe1ed7e743a0040c9f754382b9ba9c5578",
      "node": "102.wake",
      "snapshot_digest": "15ad462d797218dc2ddff2d1053116ad3e02617238b38433d33ad37b03ddcb39",
      "version": 4
    },
    "103.wake": {
      "generated": "2026-10-27T13:25:58.560572+00:00",
      "head": "6677aec50857a0ce7a38cc55c184aebc6d9ea5f079d24502a21d7a047a5f7b95",
      "node": "103.wake",
      "snapshot_digest": "606d78f1bfabbd511f227810e249185d1598ef01402fe082a9ecc8da7d577f70",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-10-27T13:26:16.680177+00:00",
      "head": "db8facf288351a6df7a4f383a77464c86eddf21e5e8a6e98237520f78b9286bd",
      "node": "200.wake",
      "snapshot_digest": "baa0f14e2e87f254bd491eab45bf8167eb134ac5b9c66f1fdf5ebbffc045b868",
      "version": 4
    },
    "201.wake": {
      "generated": "2026-10-27T13:23:20.512018+00:00",
      "head": "9fb702a92f4b15a718f3f839e699a68da4d9646dbb3bc7d76f407f1b9c592f9f",
      "node": "201.wake",
      "snapshot_digest": "32958db36227d7e474ab2cecae76ac8bf410e516d4bc2c86b229f577e418517f",
      "version": 8
    },
    "202.wake": {
      "generated": "2026-10-27T13:26:24.656749+00:00",
      "head": "fd84123ff1ddac62e4c7064c2d625fa09ea3ddabee4e06c3afbcc6f7c0701213",
      "node": "202.wake",
      "snapshot_digest": "139c9f2e1b50d5938a2ddbcb5966361574161bfd54c4c775183d51ad2a372c69",
      "version": 6
    },
    "203.wake": {
      "generated": "2026-10-27T13:26:06.178699+00:00",
      "head": "1eeb03ecd0ba8031721ae2adadbbbd4990617d01951b681d204149637024a983",
      "node": "203.wake",
      "snapshot_digest": "21008ed5e7e5e5a4e553f8b36be664d1a1ec6ef6a311c1f96ed7fda763aef4f5",
      "version": 6
    },
    "300.wake": {
      "generated": "2026-10-27T13:26:16.306958+00:00",
      "head": "8e78186cd36747b9ca2950203f4ab54f726b267e63aff03c2110af48cc83f1e7",
      "node": "300.wake",
      "snapshot_digest": "ad784e0ed9fb15ece7efadd62c085353dc3d6ae7822ceb57a72887fe1a270341",
      "version": 6
    },
    "301.wake": {
      "generated": "2026-10-27T13:26:55.782238+00:00",
      "head": "229d2182eb2bc6329a91b85f678f53e8daf65cd38531da41c5e65a7ad9b1b8e7",
      "node": "301.wake",
      "snapshot_digest": "099ebb0e5062eed1bc83c1e5a65bb93c82b2b9121feb3f09a62ef23348f18e3f",
      "version": 4
    },
    "302.wake": {
      "generated": "2026-10-27T13:24:38.750183+00:00",
      "head": "3322adcab36b90ce0876bb9af13352ae94c200bc10a99e8e5e94631fc3367c0f",
      "node": "302.wake",
      "snapshot_digest": "18a26e2398dd5e78a0e5d06a458d73e61c646cfaf8ce209c3f91c42d34b9ac79",
      "version": 5
    },
    "303.wake": {
      "generated": "2026-10-27T13:25:58.131471+00:00",
      "head": "a0dac73bd64de2120db7726d812df531c33cc7a14a3b1d6f52c1388b0e85deb6",
      "node": "303.wake",
      "snapshot_digest": "1d976ff302548357ea7e3c6c333dca7433b17b7db2aa23127b8fe87685dfa006",
      "version": 6
    }
  },
  "version": 64,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d366530386561663963646266346363/33.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d383561633663396263626662343237/30.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d636f6d706c65786974792d7072/6f762d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
