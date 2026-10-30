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
  "generated_at": "2026-10-30T05:07:01.119710+00:00",
  "head": "snapshot:db026bdcae858b00c062b6ef1de46124e826daccfa6b26417ea44a90beb4a03f",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T05:05:23.135896+00:00",
      "head": "342c17fa6023e8930a0cc03e8b6d481d02f238f9fe0730c5fe87a2be60ccb1ff",
      "node": "100.wake",
      "snapshot_digest": "4d9fb605dc4f829ed6face512d2986649c5e088947fe5fc4cd746f0e81f3c248",
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
      "generated": "2026-10-30T05:07:01.119710+00:00",
      "head": "b286c5e92b18b27fd87aa651caf37f7f8aa30ea2df5439e4683ac72a9713d8d6",
      "node": "201.wake",
      "snapshot_digest": "82898ce3d38a3121264b291cfb1fd353c194fad3db1fe91c3473563cca738c42",
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
      "generated": "2026-10-30T05:01:48.199611+00:00",
      "head": "6d5e66ee8619c8ff73e55452f0880ec86372f9e824d61205035e3d75e474e968",
      "node": "301.wake",
      "snapshot_digest": "af85c88bdd7206acd70433cfe378a569255a1688bd61d5d7e02c11e24d8904fa",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T05:03:35.164638+00:00",
      "head": "d02e5af5ff0a4b74043cfcfa86bd9ffa892acb5bc6890751401ab142dfa58da4",
      "node": "302.wake",
      "snapshot_digest": "960b1c031f1409f04bdc6a36d1513b0292133f349fe45417de95570e596c45ad",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61376462313832373535313534313233.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d39623865313164303664333034353338.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
