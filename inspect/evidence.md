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
  "generated_at": "2026-11-04T02:33:09.360373+00:00",
  "head": "snapshot:f374ff6a331c5d780ccec8ed144c4c6d4b8dbc38e64d145ae81f1c1f0024ce67",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T01:56:48.555632+00:00",
      "head": "96e0a8d472c838e43663a1465bbf909e5f4c7e31baa51d15b9c5552f2efb5aea",
      "node": "100.wake",
      "snapshot_digest": "7e0465a0b185911492bbdf1ae9f97b2b738be581d80a301f52c2841e43c50f06",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-04T02:19:13.674767+00:00",
      "head": "cbd63b6cfbc1d3be74f2476f7d689438498ce08055ba310745eab85b8fbb8ed4",
      "node": "101.wake",
      "snapshot_digest": "46740ab8b3cb255ee04c0cb6584d8465c37f75b3bc11af74673f8cdf6d4a5a8e",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T02:21:08.946458+00:00",
      "head": "e2f2a16a72349b549987d9e70bbf7896fe322f52ced28a9dab360751449067d7",
      "node": "102.wake",
      "snapshot_digest": "d270e6db15e32e6d4dc8a5621017851e60e2f2328f383828b0633475aa1b4a18",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T02:33:09.360373+00:00",
      "head": "70c9c718956f5390855a23238e5e9650234b1482d3d6dcbaf8607168542f1ddf",
      "node": "103.wake",
      "snapshot_digest": "ac041e48b7d9117ddb8d3a978eb6e390f75cf32d6126544068947a92b96e2abe",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-11-04T02:16:00.551129+00:00",
      "head": "744fc85b248d71f58be7306c9752cce75d73620f879d416b7bc6d6d3bbce5e68",
      "node": "200.wake",
      "snapshot_digest": "556a184230ee3c374b31b7493aea2fbb8d52742bcb800331f3686ef8b399cafd",
      "version": 5
    },
    "201.wake": {
      "generated": "2026-11-04T01:25:35.909384+00:00",
      "head": "7c61b57cadcde568f8d575700069080dd02615e425c1af39604884f494465cd9",
      "node": "201.wake",
      "snapshot_digest": "ab626799a06954ec1bd6ea92c1b86164984d82331c89467bc9d1843651815223",
      "version": 3
    },
    "202.wake": {
      "generated": "2026-11-04T01:22:05.459594+00:00",
      "head": "ec6cf56b5f9335c6363ce1035c3dc2863b1b0449e33e410478414223d886b062",
      "node": "202.wake",
      "snapshot_digest": "c5088935d5b261002a7b1c278e256e8fa79bef965b9f383e46ddb9938a4b7d5e",
      "version": 7
    },
    "203.wake": {
      "generated": "2026-11-04T02:08:49.141787+00:00",
      "head": "ad75cd5b706db7de531cd5985d686a402da61262716fc926c4d45ebf0f9d1fde",
      "node": "203.wake",
      "snapshot_digest": "88918a605e2b93dceb954e286c934e57dd54eeee7201afa32228fbc4c5171f47",
      "version": 5
    },
    "300.wake": {
      "generated": "2026-11-04T02:22:42.594576+00:00",
      "head": "6b3e368157e02ba8eb02222c6b388f6cb66568617b7f86054d8cf61065a6e308",
      "node": "300.wake",
      "snapshot_digest": "9dc9726f1951dc3d797a44cfb138b2d563225601e764c3284a7a5b57652264eb",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T02:26:17.219511+00:00",
      "head": "f14096c544952fea527633785fdd6e8c7e71fdde7d7055c05ac1e4eeb79e87bc",
      "node": "301.wake",
      "snapshot_digest": "57dad7702f4c13be9ae37758cb6b3a401e8eaed6628dde0aa20ecd4c3615da7e",
      "version": 4
    },
    "302.wake": {
      "generated": "2026-11-04T02:31:29.557838+00:00",
      "head": "038e21e593d4a1d2d8e3282e4b8870e6bd86fad3957df7edf1e54b4d82b74d8a",
      "node": "302.wake",
      "snapshot_digest": "178b0cdcef7cacf68629184e65d6505291d766c857899cb979ac4024f47abf83",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T02:13:59.163709+00:00",
      "head": "c0e5904374dfa92af2ffa99fe74f97db411554d138d845324386fd4780779217",
      "node": "303.wake",
      "snapshot_digest": "066d7578038311ebbb73c3b28d4e47a7e194b0464bc7f5d60cf73a0319964b2d",
      "version": 8
    }
  },
  "version": 61,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d35623733646365393633616534313931.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33376633373033666339666434306433.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
