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
  "generated_at": "2026-10-23T03:48:23.323678+00:00",
  "head": "snapshot:97854058c9d8107261a7de4cea9ab4f59f6d4e2dcf64492544e52fd2305bee91",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T03:48:08.096267+00:00",
      "head": "0e55017388c316d6f3432fc13a5c4181c82084d88a5213ab2007e923aeb2797e",
      "node": "100.wake",
      "snapshot_digest": "23f740597a94bdeb2f5e132b4676d43157b15d1770f2938b8c712969bb667a79",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T03:48:09.461511+00:00",
      "head": "e5acc7fbc212f8cdd82535973da4b1439df73143123e571660b1d1ab6bee47f3",
      "node": "101.wake",
      "snapshot_digest": "e0d5a8dab2d060e9d4035ae2347183ea2478d6924e52518970c508af40bf072c",
      "version": 15
    },
    "102.wake": {
      "generated": "2026-10-23T03:48:10.963197+00:00",
      "head": "6d6d3b97ad8114042fd9411dc37c89f10b0f08f93e666520172efac0970d1696",
      "node": "102.wake",
      "snapshot_digest": "34fb6cc387d805232f1355706136e5124994144c7920a3b4b13f6cb70e192819",
      "version": 14
    },
    "103.wake": {
      "generated": "2026-10-23T03:48:12.350228+00:00",
      "head": "f6d5c1d0278d040bb24836f48cab46770f03bc4bc68ee8e14861c4e7395730e2",
      "node": "103.wake",
      "snapshot_digest": "1b4d9ed86553e41513d98c55fd5c453f54cb331e8cedbb99b14da9ca3819810c",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-10-23T03:48:13.646762+00:00",
      "head": "e8a6ea5af19043ae5b600026fa2fb55fb12801a3367a500c91d54153885d4837",
      "node": "200.wake",
      "snapshot_digest": "1150ac8a58b974b52bcaf08577387c181a3a8466408615c46e8e785dc6ba4e00",
      "version": 8
    },
    "201.wake": {
      "generated": "2026-10-23T03:48:15.011278+00:00",
      "head": "8d5ffd66859df9ae4ea9e5e7a282af3c367c073c00ef9f04ab2d0e314205cfa0",
      "node": "201.wake",
      "snapshot_digest": "5fd382b7052d336c7c9d2a2c6e19ca7bdb441f789192427ebd8958688b345007",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T03:48:16.408078+00:00",
      "head": "4c6574dd132820453f0a564f773144559eb69360d4eb1562f95d461007aab9e8",
      "node": "202.wake",
      "snapshot_digest": "a08f5f68e94599ece68687a52b72596b7f2c1fb51d500744619e1070f7f4dd40",
      "version": 15
    },
    "203.wake": {
      "generated": "2026-10-23T03:48:17.795605+00:00",
      "head": "74eea087e15ce8982e425ae15646db03929286dc1356ee7d6038efb253cfc5a0",
      "node": "203.wake",
      "snapshot_digest": "915807bc52562d70847ec8263e407a3be4af3ec34fee7d60962db99a26429b6d",
      "version": 8
    },
    "300.wake": {
      "generated": "2026-10-23T03:48:19.137005+00:00",
      "head": "5b6003c4ea3491aad3412ed861115319cf0383f7a995b064cec112a98f8d6fde",
      "node": "300.wake",
      "snapshot_digest": "3cc5cfb20039a38e157dd2f049b9489fb0ba692f00085fba557b1627d9093657",
      "version": 6
    },
    "301.wake": {
      "generated": "2026-10-23T03:48:20.541041+00:00",
      "head": "0ea8ca902766465bf32d8c25012c8a3e60ba745264306fecea48abecac23d150",
      "node": "301.wake",
      "snapshot_digest": "0c9eb5d250fcb0b9f0ec99f4646f3920bca3289410577599238fc7988a74a4c5",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-23T03:48:21.948536+00:00",
      "head": "958df55cfeb6ad97cd8cca6c033a82abb0cf4b11daf0281f6160c8b6186f40ce",
      "node": "302.wake",
      "snapshot_digest": "57fbdc1ba67e0556a6e650d7a2760a055ee2a1e74097ac73ffcf1f22567d4b3a",
      "version": 8
    },
    "303.wake": {
      "generated": "2026-10-23T03:48:23.323678+00:00",
      "head": "4d75ea3d5dfd22e0187935cac1227930a3726aad28eeb1113dcaf13f36e0b1f4",
      "node": "303.wake",
      "snapshot_digest": "da3c78c511c7ccba4886904dbbf5f5b0bc266bca2f94bfc0ae7d2af1333ca207",
      "version": 19
    }
  },
  "version": 129,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d343461616562303933616637343462/63.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d626633356466303832326637346131/30.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
