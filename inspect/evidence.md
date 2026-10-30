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
  "generated_at": "2026-10-30T00:26:42.456944+00:00",
  "head": "snapshot:f8acbcb48723b3a7256c8db0abfd8471d21fec044533a95f28562f5ce52587b9",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T00:26:42.456944+00:00",
      "head": "f0a6260b158e44b74ddb4f49801a6a6c18d60dbea0d01c3f571d82a87dcd608c",
      "node": "100.wake",
      "snapshot_digest": "65803790836589ddab9fee663b62207899314bd96352eafa0beda93ba50d1cfd",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-29T22:46:40.714721+00:00",
      "head": "6ed27a95baf7463eeab80dfb6676b3db0f73f821dd9b6b77be7c0c2e038011d9",
      "node": "101.wake",
      "snapshot_digest": "8c3c3c6f128e3cd34f0f078ecc9f410779a754824ff7cd7a3641561e5de0abaf",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-29T22:46:35.434499+00:00",
      "head": "b6d49c8276fcea6992a728f828456f8c53b6963d1de87fe875e245d6002b6b90",
      "node": "102.wake",
      "snapshot_digest": "8346ef5dd6958f4cf9ab3ad539e995df94194695e5142f384e0aa7e33cd73942",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-29T22:46:51.933322+00:00",
      "head": "d86f1d78cdf1cd9a57fb7078becb743a1c225c9985c2cbfff763d382b0bd1126",
      "node": "103.wake",
      "snapshot_digest": "952bb4c47c91d28ccdef34c2e4ee2b69eb64fdd761f9456417cf9ef23212db9a",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T00:23:50.595544+00:00",
      "head": "084240f8e81ae2f160befd428925cc5402b428536d546e971610f45bc4395713",
      "node": "200.wake",
      "snapshot_digest": "08ae679b74984ebf7aa5771d7d0c2a3472e61216923f12a05449ab419e7b8a58",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T00:22:39.385845+00:00",
      "head": "65fa74a796a98ffd2732db335a091fe08711fc5d2a3f656941fa7f490976b21e",
      "node": "201.wake",
      "snapshot_digest": "a99e25f5ae1d1927255fd873b42d159efde62742b77c5cd285ab35535530fffe",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-29T22:46:41.274928+00:00",
      "head": "486642988a173e1609fa471417ae96441e08d5e2d7a027784ac54fe231e8d5f7",
      "node": "202.wake",
      "snapshot_digest": "ce0c21498f98369b5c656ade43af991037e86a41ba110e09d06c01548e0d9b90",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T22:46:45.600692+00:00",
      "head": "e86ec808935a152ac838bdf3781fe14e43c8433e7cadae12012c12fdcb51c57a",
      "node": "203.wake",
      "snapshot_digest": "6a8e099cc70adbe254ca472939dededaf8624378d692376f08c1ade035dc1bbf",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-29T22:46:49.238443+00:00",
      "head": "a8ba051eec6926d0f1c03be9b5ffbc6509172b74d19a9a7bb5a540e0572e4e4a",
      "node": "300.wake",
      "snapshot_digest": "47c693f28d30e83ca7adfafae757644a8ee175e85992e08aba238a1fc919a823",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T00:25:18.159393+00:00",
      "head": "8b6ed99e3ce30613a510c96d7e4c54be44439b7f3ff97429a0431dee74460e36",
      "node": "301.wake",
      "snapshot_digest": "9318fbc222a1343c91755e83255f59425e7484e9282d88d1839936d181cd1a16",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T00:21:01.649493+00:00",
      "head": "d1d05a1aeddfe8c00eafc0c74276d7c39af6a21f532f1155d5050ecd3c7e63a0",
      "node": "302.wake",
      "snapshot_digest": "df709550a9bec582c7c4978310a9bd32ebcf0be6ca958ebedee9fe831f907123",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-29T22:46:47.494536+00:00",
      "head": "12bdbf3212ebbabf182977f789892a5d6010a64a4af2ca258b80eb379df4f9d3",
      "node": "303.wake",
      "snapshot_digest": "d370040708fb5d6b18ed5fa9daa588a784f5ed9730b2cd95ded5b4ca53f60732",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d62643436373337346634626134626136.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d32646666373031313663623634393562.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
