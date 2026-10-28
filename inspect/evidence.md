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
  "generated_at": "2026-10-28T11:57:39.263795+00:00",
  "head": "snapshot:d9e75d913da45458dd1c94ac191310045ce77e50a2c012c8bcd0dccaee776353",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T11:57:22.044764+00:00",
      "head": "b47991a41c55f3e0c33876d40b5205ba8ccd99113e0edd56cc09cf02623ee5a3",
      "node": "100.wake",
      "snapshot_digest": "a80a732035de8501166ae5b50db51a951636c93639046d0d8e93a044831a5e8f",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-28T11:57:09.820521+00:00",
      "head": "8cc81d4e85ab7023150b89430eeee3f02c206121c29bddb32d7c72bc5897016f",
      "node": "101.wake",
      "snapshot_digest": "ba9a1d3dc4f5137c118cef04d97ac6cb9053a47620b9b60607aa86e6ce536762",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-28T11:57:32.681160+00:00",
      "head": "23de65a9d63299cf29a9dfb6e04fe8c0d8bcc5a830b2d67a59a569b32eb241c1",
      "node": "102.wake",
      "snapshot_digest": "192460d07cc15315b574502c61adaa2ad6f1b56b7ba04272dd2c735f8dead148",
      "version": 12
    },
    "103.wake": {
      "generated": "2026-10-28T11:55:50.670634+00:00",
      "head": "f2fa1b332692809cb3d54eaa7957826fc2a865706538f8717c052f2e44ac5141",
      "node": "103.wake",
      "snapshot_digest": "bd9a065e8e3aebae7f2c6f1e0c07804b8fadf94b9059a3dd5c6eea9abcb8332a",
      "version": 24
    },
    "200.wake": {
      "generated": "2026-10-28T11:57:28.504755+00:00",
      "head": "76fc167f66b52a4d22def28cc24fbaa27d8eb65008cb9903ae61c20c32b551f7",
      "node": "200.wake",
      "snapshot_digest": "7e5cb007a477b7d0ee141395dc3974b9bfe064c11fdb7f77355da279f0c12b1f",
      "version": 20
    },
    "201.wake": {
      "generated": "2026-10-28T11:56:59.979403+00:00",
      "head": "021d02a5e8b6b2d825f47dc92c855467622cc1f4188825900cf391ace7d09e13",
      "node": "201.wake",
      "snapshot_digest": "347d59edc7abcbfed86b6c365b4b06932125135ea383e7b1040183cba592d702",
      "version": 17
    },
    "202.wake": {
      "generated": "2026-10-28T11:54:48.259545+00:00",
      "head": "dd68f720d7d7b7c18bc30b50c339903ae104a33b2bc5ddea2f70f5b52899c817",
      "node": "202.wake",
      "snapshot_digest": "f9e503fac38c319a5a3e3d343ddfdd670d38b8da7f2220e3ed93542c993ca609",
      "version": 21
    },
    "203.wake": {
      "generated": "2026-10-28T11:52:56.354473+00:00",
      "head": "624ccd40781e3be4c48fcfc53eab06621d66c1ca1e886fb01aef146d2a2a1281",
      "node": "203.wake",
      "snapshot_digest": "81e4020648952a6da1d014218136b803ff3cca063c4ebeac035286f7443e025b",
      "version": 23
    },
    "300.wake": {
      "generated": "2026-10-28T11:54:23.900093+00:00",
      "head": "dd6db6b699af22f845b7ecdbf38446e37751c81085aab1d000064334a1637f82",
      "node": "300.wake",
      "snapshot_digest": "21ae494bcddf1779e4a08ea3f029d905763c9e2ea817e7294177b3d3430fa5c0",
      "version": 20
    },
    "301.wake": {
      "generated": "2026-10-28T11:55:34.251124+00:00",
      "head": "59e885d55e8249d69fca30b05dac42fefc6359a881ce88d4096b41ae2156f49f",
      "node": "301.wake",
      "snapshot_digest": "e727bcaab4ab6eba212c64b9ed961e9fe7f11304a8d9915eab5a95a6381ded7f",
      "version": 15
    },
    "302.wake": {
      "generated": "2026-10-28T11:55:32.883187+00:00",
      "head": "7f8b72b516865a30b3caf6b420b83a38017587d89b5e2046dd1be7b6079d5c9b",
      "node": "302.wake",
      "snapshot_digest": "e067e2809f77ff8f675161a8bc8388ed401be010d285a08f09d2521dd4aab035",
      "version": 15
    },
    "303.wake": {
      "generated": "2026-10-28T11:57:39.263795+00:00",
      "head": "ec9f61e28e4829300c5e204ee9d59000aa63bc865d18af320d1411b644426bc6",
      "node": "303.wake",
      "snapshot_digest": "f1004dcd90b3492070574a21706b8aeb52243664156901a70e0cad4aa3a1a8ff",
      "version": 19
    }
  },
  "version": 220,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d366162363034396239356361346266/63.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d30653761353065303032666534313966.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d6175746f6e6f6d6f/75732d696e71756972792d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
