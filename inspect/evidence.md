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
  "generated_at": "2026-10-28T01:41:55.441736+00:00",
  "head": "snapshot:b75fa3b1fd1b60506c657fafae9649aacef78c0a2b7ee04fc0e03007b10b0f52",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T01:41:46.033679+00:00",
      "head": "ad05bf48698ab23d34fb8fd590b1e9b0a30f29740d7b6844c5590be8be95c5ed",
      "node": "100.wake",
      "snapshot_digest": "77d5dc070a78a2d5a6c2de304aff638ca964f409ca8690a9438fbe160ffb2ebb",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T01:41:41.659017+00:00",
      "head": "386c87f6bfafa66d7fdab65c19eda84d221ccfd33e9722e89ebf83c65978839e",
      "node": "101.wake",
      "snapshot_digest": "d229483026cdda0a68ca0ec12d24bcd8bf1b424a365571b317a3d1eb7bd18e31",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T01:41:44.914981+00:00",
      "head": "e2f4df312ed0cf056466adfd148b4aa07f7c4091aaff1a7e2475b618682aca6b",
      "node": "102.wake",
      "snapshot_digest": "14f71270f394541506baa25f4fddf10d6a567371757171afa607f363cf93b791",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T01:41:55.441736+00:00",
      "head": "dc0ea06d44c91d39d761e9c17d0724f038ec8aac0d2a949ef8aacaed5af0e800",
      "node": "103.wake",
      "snapshot_digest": "88ff61cda47375a7b81e0a5e9df74f3844f40a30565bd554f5e3879676fc2d14",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T01:41:53.798968+00:00",
      "head": "d35fdff646f510f7c0f3df1404dca4bfe26d8132726a9dd3757612cdf71368b8",
      "node": "200.wake",
      "snapshot_digest": "8e0c95840e530d43c139c9ef53c7556cfcd06af110dd7ba0156efc9e76874093",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T01:41:55.290731+00:00",
      "head": "1dd5aea899668bb9d7d6e9148cba39a06775089986c0688ca2c85689b31078da",
      "node": "201.wake",
      "snapshot_digest": "9a4c5ac590aad14ff1210302acff211d2af5d154ac21ada24353e142032e19b8",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T01:41:45.564574+00:00",
      "head": "0f46d85f1f86065fdbc5fe96e58601040be7a76ae332d56d4db0a863a088be47",
      "node": "202.wake",
      "snapshot_digest": "639b464b9e78e6180c8c2d828f43a03f3c8838eb25977ba3284505892a8faa3d",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T01:41:40.239626+00:00",
      "head": "7631ab5d795cb5563423158f13e5595dde656c44a9b1159ce9b8512bfcf8e1b2",
      "node": "203.wake",
      "snapshot_digest": "b5946954be5bc7ec720333cb49283f0d4c90f10fd75b97d37cf8442b6d50340d",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T01:41:45.868389+00:00",
      "head": "e2c52173ee8547371dc36c79f45ef63c1bbe42960311101f8dd82df92f64cbbf",
      "node": "300.wake",
      "snapshot_digest": "cc790cdceabb15db8a52c4322c6ecc7b6d20ff3dd5e20e543eec2c32ba50db96",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T01:41:42.956159+00:00",
      "head": "80cb15ee8b6738394da8c8090e7009d98cbf11537a4f02a5bb3d0f671a50760d",
      "node": "301.wake",
      "snapshot_digest": "1397ad9960840fdd7faf6c83030ff2b639fa0f0f83ddec13471ce1a6cb2ffe72",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T01:41:40.704355+00:00",
      "head": "e404d5634138518a57ed9c47d0f0d93423b4d0cd7b9bd25da827777e41a1e469",
      "node": "302.wake",
      "snapshot_digest": "33ee92e2dfc5f2843a147182bfe6b6805c229ae2074ff47cd22542e748ae92f5",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T01:41:48.521186+00:00",
      "head": "7d915aa6218f2dd915ed79d8ee7a5b2a0e75cda90b105f0bb694d65af7f26a7c",
      "node": "303.wake",
      "snapshot_digest": "42db45e71e8db7bd489cdf204638289862440c8d77ed4787aad3049d02ee5112",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d36303439393864653466343434666238.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66386330636261663938373934343331.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
