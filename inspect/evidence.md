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
  "generated_at": "2026-10-24T15:04:03.481963+00:00",
  "head": "snapshot:b592d08685f888522c61f53f15945d4498b2288f9df293ab93ff62f642682005",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T14:59:01.327565+00:00",
      "head": "8bcd38ea9882bdd8439b624be2a0b867335852c5ac6ad28d7d0f4bc063bf1d90",
      "node": "100.wake",
      "snapshot_digest": "29ca8b608016f9e92e32f871c2da7c0923bfbaed87ed8cc178e78c5826839be8",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-24T14:55:33.875011+00:00",
      "head": "1b574c00488f54b19dbe4e27798ad88ac77e91bba5e12e0bf62751bc5a0ce25e",
      "node": "101.wake",
      "snapshot_digest": "18ee36edae13620ff78636d24f7b2255bb34c0322a2aee78e04b375c699b9e57",
      "version": 36
    },
    "102.wake": {
      "generated": "2026-10-24T14:55:55.711891+00:00",
      "head": "370200cf86fcf59e5d7fbfb26a0902638d57b70ba4a8bc15b66e713cc92f4a86",
      "node": "102.wake",
      "snapshot_digest": "9048973bf4222aa6fdaf0f43662f5af685c219bc706215ac7521dcf11523c3e9",
      "version": 45
    },
    "103.wake": {
      "generated": "2026-10-24T14:54:14.390620+00:00",
      "head": "795b4cb5bf39228e1bb963db8ee393c15cf9190f3b95f8d978ae6a5701ce3ef0",
      "node": "103.wake",
      "snapshot_digest": "45da23e3cfeeb2e327b0ebadb97c832e128f3f2bb6b7c1d2558ad3dd04a4f996",
      "version": 34
    },
    "200.wake": {
      "generated": "2026-10-24T14:47:31.620668+00:00",
      "head": "a3147c68c0936a16eac32029ffe1e8aaadc7304a32c0472389a102b119c3743b",
      "node": "200.wake",
      "snapshot_digest": "95345254aecee5373e6ccd736669e2f5668d38dc1d31e18682e84c83ea1516ad",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-24T14:59:15.875700+00:00",
      "head": "53450efe3ffd66043f47901d7a26fa0a1bba04761316224de9f39400d7795e00",
      "node": "201.wake",
      "snapshot_digest": "6fc49380ed6bc236d231d3d8827bc8e137d04d6e501bbf16230fe53dfa4a5e4b",
      "version": 33
    },
    "202.wake": {
      "generated": "2026-10-24T15:03:44.146918+00:00",
      "head": "5e85cb44eff91b46fd0fe5ab2f8311f8a8fdf46fea75fa70a43392be8478ebf0",
      "node": "202.wake",
      "snapshot_digest": "7e26fda328fca1e7fb27bc7ae69b15c7a528f1ba73945d879eb337bde6928876",
      "version": 44
    },
    "203.wake": {
      "generated": "2026-10-24T15:01:29.183169+00:00",
      "head": "872f55c7f6d95bb8c36d3faa127a0095c45e65f9688b7929c61aac506de8dcb2",
      "node": "203.wake",
      "snapshot_digest": "30735f9fadb49fe258b5caa2aa8ba0817b668043aeda7c838c4eb32337ccfee0",
      "version": 25
    },
    "300.wake": {
      "generated": "2026-10-24T14:48:36.448246+00:00",
      "head": "745fb57c9ec68493a28501feb1a13e1e2ad52630c7f5a47fadec40dd75415176",
      "node": "300.wake",
      "snapshot_digest": "12ad1ba06bc59cf26a728c3e7817f7cb0a522e5af13d2a3e07720f4afae51625",
      "version": 28
    },
    "301.wake": {
      "generated": "2026-10-24T14:57:31.990121+00:00",
      "head": "bd8bddf81ebc8981ac6a8e33a879eea320ac547330f6c758c1f9b6d358117b03",
      "node": "301.wake",
      "snapshot_digest": "530448bd274142954a0067999ee05dac8776078f703a8ccbe54cd646b1050c95",
      "version": 46
    },
    "302.wake": {
      "generated": "2026-10-24T14:46:44.845359+00:00",
      "head": "25de704210a60da266c9cde400a250dec552083a24e5832e56bbf6b5a67b6a4e",
      "node": "302.wake",
      "snapshot_digest": "73b9b0a306931c3591af57a987ffa81c2289dd4244567f8bf60bfbd6f631369d",
      "version": 25
    },
    "303.wake": {
      "generated": "2026-10-24T15:04:03.481963+00:00",
      "head": "d4040dbff927ea66a7309c4260e4a6e1035cb2a9c02acd21a98be0935f55ef4e",
      "node": "303.wake",
      "snapshot_digest": "48c602f0ccabb0a5cb30e5ffe824858714bb2d3cf038ef1c6eed660c3b32e841",
      "version": 44
    }
  },
  "version": 409,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d313038623863386236356637346433/30.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d623563363232396463333362346366/61.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
