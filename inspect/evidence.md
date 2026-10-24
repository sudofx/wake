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
  "generated_at": "2026-10-24T12:44:44.427614+00:00",
  "head": "snapshot:5f53e1964f938a2e0671c89e95a1d039760f6982a23219242fd58a31ad25a1ef",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T12:29:33.145608+00:00",
      "head": "ce72956041679ae9a34a1066b16c12699197d598dd82b5df102711ead9511590",
      "node": "100.wake",
      "snapshot_digest": "189e76feec1b18ffde13924a0f05dc04d2eaa2608dee0280407463c7f3592e79",
      "version": 22
    },
    "101.wake": {
      "generated": "2026-10-24T12:39:30.863080+00:00",
      "head": "0a18f6582ab68e320a968c4a70b7bd0bb7062e7c43e4b144bfd574a4042a5b99",
      "node": "101.wake",
      "snapshot_digest": "a74b5dd4d3689038603c4ba7f0d73491afadb047e101d94a3f6d0b42c4be472b",
      "version": 36
    },
    "102.wake": {
      "generated": "2026-10-24T12:32:00.025697+00:00",
      "head": "653d82e58465f153701a7adc465e68d37644b5afb2b77acc05680107c82cfd4b",
      "node": "102.wake",
      "snapshot_digest": "f2a8b48a01867fa831d007a6d65793a630c5daef10c285ef4008d157c31c7cb9",
      "version": 43
    },
    "103.wake": {
      "generated": "2026-10-24T12:44:44.427614+00:00",
      "head": "f5e00c48d90f6dfa2cd8c2f1b929013165f4dbc927fa49300641592d3cf1525a",
      "node": "103.wake",
      "snapshot_digest": "e33e7e41e887be51b88e9415b224cbbb30498290f12da79c73a14602a37a8a13",
      "version": 34
    },
    "200.wake": {
      "generated": "2026-10-24T12:26:04.280970+00:00",
      "head": "02b39e6bd2bca3ae27b41cffe807077f1d4ecb36edabd9b6831fc75df0d7e48f",
      "node": "200.wake",
      "snapshot_digest": "c376ed33cfb24cc55ae8d6bd3f84aa486b4dbbb5791f19ac575fbbf661fc311d",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-24T12:34:40.814006+00:00",
      "head": "833de4e894b33a582c5cbf7919d6481938eb07be23d3c8e682f4d4ee35e80a07",
      "node": "201.wake",
      "snapshot_digest": "7b8a0b02013fac5800b172d12d16fa6bf863255843e21d976385c877666ac769",
      "version": 30
    },
    "202.wake": {
      "generated": "2026-10-24T12:37:20.149353+00:00",
      "head": "387db80634f5ac7fcbdc71c97532d11f97cfae3f0cdbc97d858d3a089248d29a",
      "node": "202.wake",
      "snapshot_digest": "62b8c0b46469583828bd256822c89aab699e458a8970dcf5c48c2809fb34c03a",
      "version": 42
    },
    "203.wake": {
      "generated": "2026-10-24T12:40:45.505470+00:00",
      "head": "fad978fd4c554425abd0d840000d62533e2995a6c7d6a8d2ccd592bf2f104f36",
      "node": "203.wake",
      "snapshot_digest": "501aeb6f9418c94ce67d2c3cca96d4c468dc63588d2ad7ded9cb8a3590ede39d",
      "version": 24
    },
    "300.wake": {
      "generated": "2026-10-24T12:27:45.225404+00:00",
      "head": "8449f3c033a99ac063e3f789e73712a01b3cd106b43f7c3a3482c22425f4db90",
      "node": "300.wake",
      "snapshot_digest": "d8f0b2aeb6fbc6a84b8f19ef4690427890ac972e2143ec4b91aa70f476a6516f",
      "version": 27
    },
    "301.wake": {
      "generated": "2026-10-24T12:43:15.901704+00:00",
      "head": "6150445f3d403cfbbee45c5c1d25f8dae3dad4960ec53b181570cc46519d10ef",
      "node": "301.wake",
      "snapshot_digest": "52094f4cc3a3333a2a8b440d84ebe46de78521b348c58c2ba40196020f2d0d1f",
      "version": 42
    },
    "302.wake": {
      "generated": "2026-10-24T12:40:54.925466+00:00",
      "head": "d1f0f57ffc7d3d59494c7b9dd39e248372649570eb110467395fbdfb9930491f",
      "node": "302.wake",
      "snapshot_digest": "ad49214f5f9c10285ead8084321d475b1cf32a05e4351103849664bb389746ee",
      "version": 24
    },
    "303.wake": {
      "generated": "2026-10-24T12:29:51.603797+00:00",
      "head": "e6e776e44df03148418c0fb9ff44955592b520675614035a43e65667d5ccd0c2",
      "node": "303.wake",
      "snapshot_digest": "4762d9ce5d0402c7ca95165e48c93933c152b87a31e187bf4c16b0ddc0528bd0",
      "version": 42
    }
  },
  "version": 392,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d646338373232346563623261343837/38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d31383439363863336533366234663265.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6f626a6563746976652d646973636f76657279/2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
