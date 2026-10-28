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
  "generated_at": "2026-10-28T16:27:19.505181+00:00",
  "head": "snapshot:5801e8c67e0765b33b101d094d7dd831c6487606a7d1fecab982efe07a6743f7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T16:22:03.723977+00:00",
      "head": "3cb2ebfaf1c346482f3eeb8076ce3720faf677a61a87e40a8a8755f94e901153",
      "node": "100.wake",
      "snapshot_digest": "c25a3c1186c4ed473e7e72f9364ad57f7c4c61a72b3037e198d0f16bd73a5c30",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T16:25:40.126866+00:00",
      "head": "fe54e1425c5e6abd54d702fcb8774085c9f0c692260ccbb4082738cc6d0b2a2d",
      "node": "101.wake",
      "snapshot_digest": "7eee08423c9e730a1f77de24b812a40b67768b1471f5a6b38b3b418a55ee619a",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T16:23:57.394502+00:00",
      "head": "01eb79fbbf04129f6cc4d7a9e7b69e31a3d592b931d8b3e0f2f7543963023fb8",
      "node": "102.wake",
      "snapshot_digest": "fe22ad2791ae379ab91a0eb73450bd05cc85d4d7989ff734372f12c7dd508240",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T16:21:42.210535+00:00",
      "head": "dc24bd63d2217939816e309b22fd642c039ae45ac94c799cce33c66f2d7c14c2",
      "node": "103.wake",
      "snapshot_digest": "9034c08505aa38003327c051c734f9555a43f58ad6fed9531cb6b42606b63849",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T16:26:26.351454+00:00",
      "head": "9ce90ae705fe77c2458cf0c64776f895e44bffc6fcfc3e0d5284be033bc14583",
      "node": "200.wake",
      "snapshot_digest": "7c17de5f978354d942286a7e5e68f30601760739ec460fe6b19be0f09a08ac70",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T16:24:43.971796+00:00",
      "head": "2dbe3354648d3c9ad23f77305def81572180f41884dbcff26339979f96d5e291",
      "node": "201.wake",
      "snapshot_digest": "f8ad5a608ad3bbfb522b32c11c7678c4f8f4f0dc8efe5b3fe036da0103998c12",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T16:24:01.818326+00:00",
      "head": "8658d19f8f72741fb18edb0bf4234f253fdcbb4119ef6b5b2ecf2a6aedf45a2e",
      "node": "202.wake",
      "snapshot_digest": "10796008caae7ac954be09b420eca4b74c94557fd8050c0bcb5bf9560bcf0166",
      "version": 29
    },
    "203.wake": {
      "generated": "2026-10-28T16:26:23.796390+00:00",
      "head": "a513571e0d59f56ed5d6ea50a8073bb7a3e884e19f653f4abf36a944e644c0e8",
      "node": "203.wake",
      "snapshot_digest": "adb8e39bacc13c5c1e822425fc1ae25bd97813643a3abdb03454539cb306b84d",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T16:24:45.834738+00:00",
      "head": "de21a91e99e6dc6bdd982c88d109dede646468c6cd3602ed42de7f06084fe2ad",
      "node": "300.wake",
      "snapshot_digest": "f1907f2979d8c10c6d7dbce59f789f63d931aded0498b180ab76b224826174fd",
      "version": 23
    },
    "301.wake": {
      "generated": "2026-10-28T16:27:19.505181+00:00",
      "head": "ecfc33d1be4b3b2143bc008e98b39da3fe423fc0461ede54184628a03432d172",
      "node": "301.wake",
      "snapshot_digest": "950a58df0a36bb4f8cb6dbc1a73a9490409dd8ec0ff79f9ad3d1fda35f47cf6d",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T16:24:08.119791+00:00",
      "head": "898a2f742ef75f326faaba695fb69e0bd0e63f87819b3b6deb683565cea182da",
      "node": "302.wake",
      "snapshot_digest": "2179db6163cd1207f936edd3c96a921b0403a9e6810ddf14d1f0c60c70bdbc2c",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T16:25:37.320379+00:00",
      "head": "13fbd35e23bf98386d4842294ab3572ff3ec72f7260bf3e92c0e678a4ed42dec",
      "node": "303.wake",
      "snapshot_digest": "5dff2e7ab9a15e67f5ce75ca19070fba967c2849a8955a295bf522b0ed7a9613",
      "version": 23
    }
  },
  "version": 276,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d36303566366334643231363534613766.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d313565643763643866643163343963/64.json)
- [notebooks record](../reader-records/notebooks/3230332e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
