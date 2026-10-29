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
  "generated_at": "2026-10-29T06:57:07.884858+00:00",
  "head": "snapshot:00a5b7ed0c70aa00034ed3a7dcce57777654e9d5b9c94faa83913a0609d18d7b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T06:54:38.229325+00:00",
      "head": "39dae14b3baa93c99bdbdff061f8615f1505c4ab56494b24d60a56644018f4f9",
      "node": "100.wake",
      "snapshot_digest": "feb03cb3e4a7839a47ed35eb78cb84e0f876b8755e0004cc580e0cfbe60f012b",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T06:57:07.884858+00:00",
      "head": "c9bf2901a05294b739a3579ebf20c3c1a213d6bd965147006e47b4d2e46fdd7c",
      "node": "101.wake",
      "snapshot_digest": "67ed36d8e0da66d610dee0b7a48fa2cfa59f1b8405aa8dde653d2d8e09405b3f",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T06:48:17.702092+00:00",
      "head": "ed3d43c13f8e903f2774a9fe90248f8490630dae1a05e5445fa8e416bd91ccc4",
      "node": "102.wake",
      "snapshot_digest": "34a8e34b8bb8d4066246b003f7e605cca3fd941ce6b8902ae5bb9d15183b4dc6",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T06:56:06.422077+00:00",
      "head": "0da4052aee794a6ad68526e6805e5d081fd3e8873a447aa0b6c72f34a8f85ac6",
      "node": "103.wake",
      "snapshot_digest": "fa35d243140ac2185e071d44ce8b0296ca8baa73e358153297bc5fbb78ec6c60",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T06:54:17.282128+00:00",
      "head": "1f441b955a851e9973db0925ddc81b3f5e99ec6a846788eac294cabb42ffeaa5",
      "node": "200.wake",
      "snapshot_digest": "927f3b919fda41cb0d8a37e0fa22c8aa0cd8dfd066a9762a7afca085a3add051",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T06:56:45.956699+00:00",
      "head": "800e199de0bd354603e01757ce4e122e178d31b38d3a18d167e71ed92a2f58d1",
      "node": "201.wake",
      "snapshot_digest": "c4efb887a98437c34b04867b8084507aa31b64b0d5beb4d89d0c4c13f0c1036d",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T06:49:49.021894+00:00",
      "head": "bbc5a404b32f214c35673a39a87e522c9d312abe60c10dfe9a99643c1c9b838e",
      "node": "202.wake",
      "snapshot_digest": "b3eb4dedebcd0baa97970060c42ef46a91d716b12431b00a3e143fc5d902cc5d",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T06:47:58.676397+00:00",
      "head": "d4f011db4e931edba58c3de175b2b7b27b1e2ddf754fb3c70fd0a27e6e0f34e3",
      "node": "203.wake",
      "snapshot_digest": "02ed37fa0fabcbdf53a5433cdf464b9b77b4ace574beeabfc23fd8587d83321f",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T06:48:46.005383+00:00",
      "head": "150bf9064ce8ee4110b55f064006cb483a6e23155c5c1c29b2980e2943ee0d6b",
      "node": "300.wake",
      "snapshot_digest": "d77be47729cf32488cc5c528708682c4b27690228f1a5e8af55afac852ed34b2",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T06:47:03.514540+00:00",
      "head": "c52b94a1c4c7abad0f7cb394c23ab606b7292e8649211b0e7423df62e7cab557",
      "node": "301.wake",
      "snapshot_digest": "9d7f07ff007081ceca23d29873438c7a209dddc7e86c85930f254c2feabeb6c0",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T06:56:53.160009+00:00",
      "head": "5fdd1f3f2928e6df477becbc51f1d9248693517c4e62bd2df128cd3d065be691",
      "node": "302.wake",
      "snapshot_digest": "f823c2b1067d12c8edd7078851a20e8284d839d3abd46d2f1f82e13a811db86f",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T06:48:44.774448+00:00",
      "head": "4921f1307113abbef883211e6e47260ad139b72cf56bc84ee32fa84c472839ee",
      "node": "303.wake",
      "snapshot_digest": "28ca4633ff5ec5729893f0564adc4028ab7ef1b2f20ddf41f5ff0128dfdabf91",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d66653832613036373036316634303732.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d30666337353838343065346434363163.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
