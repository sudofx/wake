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
  "generated_at": "2026-10-25T17:05:40.673563+00:00",
  "head": "snapshot:634b1c9ba250d40b2e680704cb96780250c7a1c67a5a74fa85bad3a81be4d5dc",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T16:56:44.270872+00:00",
      "head": "76f9fd5dc884efec5344f4e135641c38dd8001d192eb828ba8f52c29743624e1",
      "node": "100.wake",
      "snapshot_digest": "358f68763964348207e3ba5c2e1e185d1dd8b2c07eda0cece414d14d5de15c8f",
      "version": 27
    },
    "101.wake": {
      "generated": "2026-10-25T16:59:05.076101+00:00",
      "head": "883678473d303c05b39c39057501c059eaedd76f631ff91fe522734dda7ead2d",
      "node": "101.wake",
      "snapshot_digest": "1768d2c9a3857f72a0bfa184d78d4a94c157c30a879de221b5e8b10cdf53a2ef",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T15:53:15.368140+00:00",
      "head": "4af706a85578fb1724fedc89a8ce09df402b1fe8b57cd5c408cd06b7258d52b0",
      "node": "102.wake",
      "snapshot_digest": "e59911c9ebe726246c9329e1a181af1731f41ebd284b20bf725290cc48e279db",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T16:55:15.415557+00:00",
      "head": "6b4a95f24b68d94212b84c6229ee15053910a3906760be6e6c94b3ca056355c5",
      "node": "103.wake",
      "snapshot_digest": "45328542e37c1efff37950c02625f7a91d34c12f79e653fa3e0920f58c935146",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T17:02:12.618401+00:00",
      "head": "13ae7accbe66ca72585e09c4961ae589e75c091723a44fe83e30fef2d6336ee9",
      "node": "200.wake",
      "snapshot_digest": "8fcb1bdd7b103830720b26c300a5312e5693c450b3378ce72311e3a3fe7984ef",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T16:59:46.216886+00:00",
      "head": "8623b402c31d227d37ecce472fff1a5e5eb87523f58ac0d3cf4c7baa96f05a5d",
      "node": "201.wake",
      "snapshot_digest": "8210467660d40fd78aba54f709a596b81ee93f7cc079dbafd9651646dac948be",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T17:05:40.673563+00:00",
      "head": "3f728c71ea2ac2a4ea296c741ed61e2e9e057a00ef24366c986c3cb8d3893b9d",
      "node": "202.wake",
      "snapshot_digest": "6e205f3e018b9b37b5f1ae2445f6e4b9a03844ef577087b2dc1b586a206d87ae",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T16:53:29.470102+00:00",
      "head": "2cd27a4f559863674204a495a87faad6df93e7afbbe17ad1c10db83fd6da096b",
      "node": "203.wake",
      "snapshot_digest": "1dc138e98c7de00554b07dbce756846e3046e54be2bd0489f8323164c5d04dcf",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T16:56:00.483744+00:00",
      "head": "222916c3d273c8db53b4e8c8adeba5e542341292b6fdba4d22d0582c09c486c4",
      "node": "300.wake",
      "snapshot_digest": "3c38c9f1d0abcffb8a4a89719364f87b7616bf5c0b8129e72c69e0898a5d6d42",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T17:04:00.934142+00:00",
      "head": "27042fc530d574cec4cdb8405fd943f00a99ebfd11865867624da51ff5cdb6a2",
      "node": "301.wake",
      "snapshot_digest": "4e5142cc0a7541b5c21396fefdcf6025c2911352c0877e19c921721ebead7909",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T17:05:09.545003+00:00",
      "head": "a6d17b5db534b4d95a22f61778e6b2c9b8879ca2a7c75db16409332f4d53e956",
      "node": "302.wake",
      "snapshot_digest": "82741f4a81f9ce7fa7363768b8feec30930d67e2ce78ffb0a974099de7884971",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T17:01:48.757906+00:00",
      "head": "7865111ce5aeaca926ad42eaa55dc8fd8db4a5547471abdd7269a84e1a54ed13",
      "node": "303.wake",
      "snapshot_digest": "7c618e8bfe1532e87b552972bae3b01873a4de1aea79e68ec0620afe0efb863c",
      "version": 51
    }
  },
  "version": 509,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61353831613239323131313134333762.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32646337346264656533613634626363.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
