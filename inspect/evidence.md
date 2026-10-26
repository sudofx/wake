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
  "generated_at": "2026-10-26T18:11:35.772532+00:00",
  "head": "snapshot:9a9e144e269030c2713621d0ef3cb1b982144b584aff9387cce345e5a2917a10",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T17:29:32.749503+00:00",
      "head": "da1428b5fdb9aca1726ee2bce64b11c5c118bf446dac8fe4189c53e4bb6c81d4",
      "node": "100.wake",
      "snapshot_digest": "7b78b706f00df753194a7e7a7b0a231e885b6c277a642fc9e86fec7502abf71f",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T18:09:50.809446+00:00",
      "head": "88499b06498b89dd3135de4dd35b7fde004f26973c5a9145b7d23c93b6546575",
      "node": "101.wake",
      "snapshot_digest": "35a97c77182dfb1ddd5fc5d368b5c9efa7a4843067816a4a3fe05174c206aa0b",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T18:01:09.780115+00:00",
      "head": "b78e2ce36cd39c18df3439d1cb0755aa9597db7d9de14abc10e1338924993dc0",
      "node": "102.wake",
      "snapshot_digest": "258fe73d0255cfe278449191e7555f09ef91e639d7aa83d5a659d16e5038e8fc",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T18:11:16.941184+00:00",
      "head": "3f7475fc4b9d1e25ef8f4d5c441251429f66f65dd3513cac9e9f84e7a3594104",
      "node": "103.wake",
      "snapshot_digest": "caed39888087b3033ef054d721d597b791bd2cf19081f688b165c61b1ec64ceb",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T18:09:12.110836+00:00",
      "head": "d2a627ce9048782dee307a8e86e73d9baef3c87fdc7673438e216bb821be177a",
      "node": "200.wake",
      "snapshot_digest": "536c4477151dfdea7c407ac246675edac42b2c04f0caf5bd2448e2fb54c09961",
      "version": 44
    },
    "201.wake": {
      "generated": "2026-10-26T18:03:06.140492+00:00",
      "head": "bbcc8d512771ccbb3c8c4aa9552bc84ed47900ef2d9dad8ba830fd3ff865ae05",
      "node": "201.wake",
      "snapshot_digest": "492be7a69ace613983f30dc0bc3462b6fdb269b8fd69eec58871140013e4293a",
      "version": 45
    },
    "202.wake": {
      "generated": "2026-10-26T18:02:28.169140+00:00",
      "head": "3a3736510ccf33350e23b150722cf9cf4deedb2afeffd400a18d51930b41f6fd",
      "node": "202.wake",
      "snapshot_digest": "932a256641dabdc95e3ccd819d62ff69637f8515b8900bfd50c506d7c7ed0c61",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T18:03:27.710361+00:00",
      "head": "e225d2e391ba97223451d7411a3939dc04a20a4da4d9282cd7221d5155267e09",
      "node": "203.wake",
      "snapshot_digest": "5e6573b2b36ed0d49f10d6fd6458306aece3aafa7eafb8021ae53723be524045",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T18:06:26.094192+00:00",
      "head": "ab5e30b53264eb92a74979514c9c5af8c811ffbdc3d2898570f9606c04a65b7d",
      "node": "300.wake",
      "snapshot_digest": "8aba3d3365d8e07faa8e6d303c17d08da799ea8d7bb52d006f0487e68a477aa0",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T17:53:42.789553+00:00",
      "head": "b6b9ee6985ff9429ed4a8de220f35f92613dbabb270cde66f731196b5df488ba",
      "node": "301.wake",
      "snapshot_digest": "fb86fcd78aca163428fc725d656c7ff4bdb6b45acacc16bea330254b2d42f79e",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T18:07:00.749112+00:00",
      "head": "0fc1ef582a51a8d84909aca73ced4c0177316a8c0946738bf4de4af84948ddba",
      "node": "302.wake",
      "snapshot_digest": "2118a2ebd303d0d96e358fe5d39410666a59b2ee8638898215a1dacb797e91ae",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T18:11:35.772532+00:00",
      "head": "c6baa8b8425cac7f6f439bcd955a0e30612b4647ccb95010efcba2a53953b9c8",
      "node": "303.wake",
      "snapshot_digest": "f25f3e3fc4be4b14686dee2b4fb5e77fb9b8cdbb685d21589a6057570e421172",
      "version": 56
    }
  },
  "version": 577,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d39356561396465666565323734373636.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d31653034343031326536623234323264.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
