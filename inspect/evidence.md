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
  "generated_at": "2026-10-30T04:30:07.464450+00:00",
  "head": "snapshot:e399f40e664bb2d84488072ae5071ac5a24204dda7f2129d6bbed73ee503c6c2",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T04:26:40.487296+00:00",
      "head": "6a954e7d7b05877bcc28043dc3f7cac9fc1e4f024adf72d37a8d06ac6099e2d7",
      "node": "100.wake",
      "snapshot_digest": "1534aab711067c64512f9560a7b2a2d3debf9b653a8c6f14c1a07c441d6b95ad",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T03:22:08.808224+00:00",
      "head": "b2a6484a95cb6a030370588f3847c5fa187ee8cd2af1e39c3113c17ae593496b",
      "node": "101.wake",
      "snapshot_digest": "6f74fce989760cba4061426e6c015abf7000df5c65f2f223d3d2e1c2e3a31dd1",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T03:22:12.463717+00:00",
      "head": "9b60a20838f149dc5f0b9ccb9033a1bd9881fccf18d97a64a0adec5546d3f97d",
      "node": "102.wake",
      "snapshot_digest": "653e49603ca48e387c5c3a3d4829d56ede4cbf42a3b692b2fe80bd879391c89b",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T03:22:24.404833+00:00",
      "head": "fdc89b8576fbf1099fdc5a16fafea745d023810b11dbc770ea6fc328ff33174d",
      "node": "103.wake",
      "snapshot_digest": "35344479ff706709f452b18a97eaa2fa1bb629605b748ce36d0ba0e4333ef66e",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T03:22:31.236940+00:00",
      "head": "fe1ac9265b6c4a70816dbcc72f3954f3873dd00166e02db6f8f2cb6c15d09620",
      "node": "200.wake",
      "snapshot_digest": "4b73c6afdd833c88f8507fb8f5390706ad175492cadbdf3b775f7904b46d9ca5",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T04:28:25.872144+00:00",
      "head": "c754e1274b982ccd29fab2e95c0f5ebdf17b4fcf17aec7e4a721af3ac59234d3",
      "node": "201.wake",
      "snapshot_digest": "a01d5895b2a0d778452de7639bc568b94f2474e706bb9c06536550624b260fe0",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T03:22:12.411222+00:00",
      "head": "7ea4d098e0ab59a261701ac83d8e2cc17434de1d0b524911a461a060aae69e01",
      "node": "202.wake",
      "snapshot_digest": "93e9cbe072b6008c514872bb6efe94055b3b5fa709cdf1cff73a1eb824603bb1",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T03:22:07.563293+00:00",
      "head": "eb40d87bd72c442a3a70e5bb7370ae86e54fa560d593ae4c49b321f724529d85",
      "node": "203.wake",
      "snapshot_digest": "b4cfdbbc1e26d5134ca1cdbfe2b6e1f620e8a13a7baae6f7b6be547feeb88146",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T03:22:26.650272+00:00",
      "head": "49eb2d9121a78a90d2fcf036ddea2a02b7c328a44f3ab832017b525454d356c9",
      "node": "300.wake",
      "snapshot_digest": "bdf962acf112f94a937b72e960a7fcb6790138c5919857314db144802b35e0bc",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T04:30:07.464450+00:00",
      "head": "31651dcddcf28ac7807dc031bce233ece308b03a0ef4e80160b8c59705ec74b8",
      "node": "301.wake",
      "snapshot_digest": "110b6f520016fedd23a12eb3c6e66653030057c3cfbc2cad4e5ae94983849808",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T04:28:27.433151+00:00",
      "head": "f134ea6996fff1c20a9cc053a9d4843a56bb22eee95fcf1b96a6f4918600c0a8",
      "node": "302.wake",
      "snapshot_digest": "ad946712b3a4a4ff4aae188909de57c7e3f9b1833cd1f2f83e83723afe07ab00",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T03:22:11.634166+00:00",
      "head": "3c118317a291c6ecd2eeddff77dc46f0b28c4e7f7bed5f30e34190b848e1add5",
      "node": "303.wake",
      "snapshot_digest": "e4fc483665f91a5f6edd4a88a0229c6e7e53989cc334cf5348019916622bae0b",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d35656563653732633939306534663631.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d64626261393463633331303434363133.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
