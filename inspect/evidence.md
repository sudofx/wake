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
  "generated_at": "2026-10-22T20:17:20.592839+00:00",
  "head": "snapshot:6ddd3df6e20357d7248a1388e2d8758e0ab2dc0b508d29181641ac99da70e7ee",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T20:17:19.035922+00:00",
      "head": "a936de2a12a3ea26d864ba11e0bd55dab4a988b16805426d655ad4b9d0108a6f",
      "node": "100.wake",
      "snapshot_digest": "93e8a3a9ab0b8997935b70efcfa3568839206ee44a3b79b0ec9b4a25be78506e",
      "version": 0
    },
    "101.wake": {
      "generated": "2026-10-22T20:17:19.185517+00:00",
      "head": "c1cc10d391f97311a3b698b93ef49a7966c35e24cfa4e42e5507aeb63bd323d2",
      "node": "101.wake",
      "snapshot_digest": "7be4e8ca9c5522a13c0cb0ac4c78aea1a9b2573e1cf86c9d5e6070c4a73a75df",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-10-22T20:17:19.321218+00:00",
      "head": "e494a4f8146cebbea07eff32c40721fa971433c81ca38e12aa0b7dd372f42803",
      "node": "102.wake",
      "snapshot_digest": "40af29b07e1f2ada7b6ec3093241d2c70b62ec0a404c243c8a1f6519f5ffc03b",
      "version": 0
    },
    "103.wake": {
      "generated": "2026-10-22T20:17:19.463559+00:00",
      "head": "82486e70de48ce7d6ebf29e6fed6d847c74f30049629ee9a2933250cc4aca561",
      "node": "103.wake",
      "snapshot_digest": "1a0b51ea18e5c01271cc618a4cb2d104007c2cd589ca38b5defe10c9e863a0a6",
      "version": 0
    },
    "200.wake": {
      "generated": "2026-10-22T20:17:19.604561+00:00",
      "head": "61e3c54315bf9b0fd327d4bc204a0a07fc668a53f94934ae40c15cfe330c7f93",
      "node": "200.wake",
      "snapshot_digest": "f0585432098b7a1e6c38d24b4552d9a62f9963742526325fc8f8eaacfbb3c20b",
      "version": 0
    },
    "201.wake": {
      "generated": "2026-10-22T20:17:19.746301+00:00",
      "head": "27224add2e799749ceea110bbc9d69d4ba19f284f35a2a080d5f3146eb1baefa",
      "node": "201.wake",
      "snapshot_digest": "0bed0b566188fa4836da41eeb1fde1beb5bec15ecac174b653d773e3ac80de86",
      "version": 0
    },
    "202.wake": {
      "generated": "2026-10-22T20:17:19.896010+00:00",
      "head": "573eaa3beeb36a16dbb3a8ae888617827583b85b041f8de0932b6aa628a68ecb",
      "node": "202.wake",
      "snapshot_digest": "303b27ec47143ba0f9251fcc2e6d66f00ac339eba8ed2a58042bf14aa024266e",
      "version": 0
    },
    "203.wake": {
      "generated": "2026-10-22T20:17:20.038654+00:00",
      "head": "29bab95d679edbbe9011bb1eee67ac867d4ab8885f1db6a7c61d67da04c25f4f",
      "node": "203.wake",
      "snapshot_digest": "aabeab3ab23365a8bfb49f08f44a3272d6b4ba817503c1a16acb7a21dd5c2867",
      "version": 0
    },
    "300.wake": {
      "generated": "2026-10-22T20:17:20.178540+00:00",
      "head": "e110c9f918ddb9468168c6b3bf30cd54b7b3a42eda6e3249d94177f33551bfd8",
      "node": "300.wake",
      "snapshot_digest": "2b88c274463f9c5c8b3d203264e45046a9fa6ac6b6c10834ca63e60f448b646c",
      "version": 0
    },
    "301.wake": {
      "generated": "2026-10-22T20:17:20.317767+00:00",
      "head": "c0348834c4643383a97bc76f8b207ecee7734795f536f7b86be4435ea21af7a3",
      "node": "301.wake",
      "snapshot_digest": "bfe2abe0e97df45192294daf287503944b6a63ef8ba909fb3eb1509104e43f3c",
      "version": 0
    },
    "302.wake": {
      "generated": "2026-10-22T20:17:20.454414+00:00",
      "head": "3c0bdf81fb99f70dc0d107a1d4be0fd46d08534f12a1fa72ffe3c5a59820ada6",
      "node": "302.wake",
      "snapshot_digest": "1ac5f7b139cdf13bc777f875f7a3e1bc85c58811cddebb5b268a488500c220da",
      "version": 0
    },
    "303.wake": {
      "generated": "2026-10-22T20:17:20.592839+00:00",
      "head": "1a091c670aa86a0a196d92771e592fa1adbff70e1110baeb4a8e23c9fffa720a",
      "node": "303.wake",
      "snapshot_digest": "43dfddd8c8702b33d09717a105a60ff2668c43d69d9c22e332687e9d6dd0e077",
      "version": 0
    }
  },
  "version": 0,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

No matching bounded example records were available.

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
