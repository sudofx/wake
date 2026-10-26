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
  "generated_at": "2026-10-26T21:09:41.849302+00:00",
  "head": "snapshot:3d80bd2da6b1354c8c1274f2c1ced62d220e256dfe54997f4efd7034615c2e27",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T21:06:14.086568+00:00",
      "head": "708e4b7f20fe9b73f715973c6a7a9943700507dad2ed746b690b344cc4c89b37",
      "node": "100.wake",
      "snapshot_digest": "781a6add89723a095ee43ba7bed39eab817244baf1100044906dbfb6e33df97c",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T20:51:28.880183+00:00",
      "head": "61e8975edc1863df4626f864e6184795eb56cbafdaf6116251d9bc467d196e32",
      "node": "101.wake",
      "snapshot_digest": "95ca7def06b2b1d4abb0b9266e162004c9b3c671466b532f7adc6d756028af77",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T20:58:50.109638+00:00",
      "head": "c2b207ef534f80e2a373a403ecce73a20e5f7a129846e2314c248614cefacf53",
      "node": "102.wake",
      "snapshot_digest": "ac716ec96bb7b1a228b5a53173ceed78508f380b3ff129f4bbd16dfeceddb202",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T21:09:41.849302+00:00",
      "head": "db38e58dc236e52392ba090ccb617e0d7b09ee3cf8c85be09bad3ac5b738b873",
      "node": "103.wake",
      "snapshot_digest": "f0fa33012fd4a771c34497b32f9749226d1c9388f9ca7904986f50c4ec5dc69a",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T21:06:30.374407+00:00",
      "head": "f0d72d3af64543e15470afab7746a2beb53c8ff6552f30011f9557ba708ad183",
      "node": "200.wake",
      "snapshot_digest": "78fbe0e91316c80ac2b27e7220f9c2242ac2b7238f773129d5053116e2c558f1",
      "version": 45
    },
    "201.wake": {
      "generated": "2026-10-26T20:44:38.052466+00:00",
      "head": "8fa62941679d0a17d0cc748241bea1e0f10ccebd54833c751aeca956be243647",
      "node": "201.wake",
      "snapshot_digest": "f2c1bf35648c42a17d685a08e9d6e54a1341b2795b6212be4d392c5cdecb492b",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-26T21:09:06.683241+00:00",
      "head": "3d159c73fa25dcb15339215d57182ef7ec272507588986f83adb0a77f178297c",
      "node": "202.wake",
      "snapshot_digest": "2550390b568a78cca3fc7e17c23d7966ad0ec9108b50497c2c6b6a89d9e05c6a",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T20:59:25.126302+00:00",
      "head": "b5ccf20a850b65bf80ba42ce97dc98f7e2ff62bc9525402596e7f7a1f0513368",
      "node": "203.wake",
      "snapshot_digest": "ebdcf6568899ae81f9a0aae7d802e2a06e04ae480498907d4b53286cf25c547b",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T20:46:24.713730+00:00",
      "head": "7498606be91947295ae65610d1ff53448909e7ef7123f636e61f8e6ec7b1f26f",
      "node": "300.wake",
      "snapshot_digest": "f030188af9182ebe920247da3aa8297196821e3b99bd1fc2588cbbc85cbf226d",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T20:52:03.982305+00:00",
      "head": "619c3642d2ddaf9b5c25ff02029a5701e01e44b1ea2615800302d2b8eaff4cd4",
      "node": "301.wake",
      "snapshot_digest": "e09278eda98c8ee7e6aaf650ce28f8c6876e8af8cb4bc113f8432d8def472975",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T20:44:19.932258+00:00",
      "head": "9b966814275e6c0dadf965ad0e36d5eb255fafbd3251cb6291a2a5370b27dc80",
      "node": "302.wake",
      "snapshot_digest": "a7c311984153daf1c841f3387320d085c898b28e1666668d6a7fc923352464bc",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T20:47:46.763159+00:00",
      "head": "49ce5f8e37dc94ca5532b4842a40cf59f42dc35e9f53893bc752c10769467d57",
      "node": "303.wake",
      "snapshot_digest": "f4f10905b08614e7d8ae22888768baa061a8a264f818155cb6ca7030534c3a97",
      "version": 56
    }
  },
  "version": 579,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d373032303135373432373466346161/66.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d663337643232383735646666343733/33.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
