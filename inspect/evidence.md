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
  "generated_at": "2026-11-04T00:30:57.353426+00:00",
  "head": "snapshot:a401daadd7a2d4bedb427539c70dce1c96e6ec4ddd7962b15f6dcc3a9b8faf5d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T00:18:47.789564+00:00",
      "head": "fb53256c202476894b804713abfa4ae70a9f8f115071e3fa9fba19339416a13f",
      "node": "100.wake",
      "snapshot_digest": "c1cc5a0bb322855955b6d3161b62fbafa00a0920ad3e7ac566edca09d5bda4e7",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-04T00:30:57.353426+00:00",
      "head": "1328ecdc1e6a44d119000b7c3ceb399b7979ea7424a0d9d9271782052617b990",
      "node": "101.wake",
      "snapshot_digest": "858a5edd3a23a51b72a16ac78c293f7ee5124980af877e9bf9df063081f677a6",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T00:11:54.183690+00:00",
      "head": "12f2938a0e8d6f84b0ee34beb7a0108d9fd9e405297cfe66cd31e97a0ec82f50",
      "node": "102.wake",
      "snapshot_digest": "32d835f36704676511a354b951ac0b455147b720da12574ea818f8abfbda8ca8",
      "version": 6
    },
    "103.wake": {
      "generated": "2026-11-04T00:13:33.577151+00:00",
      "head": "00ca40eb74ea88013649d11316bdf651e17259826117b094226c4eee59d52076",
      "node": "103.wake",
      "snapshot_digest": "41ff25ae3669e074c1ed4203e89309faa80eddcbd289359b4156366aa649d914",
      "version": 6
    },
    "200.wake": {
      "generated": "2026-11-04T00:22:18.898131+00:00",
      "head": "2368ee632b9e7f3fe9dc0d5c0fd904995c551826cff9b30d437f53c229de7a2e",
      "node": "200.wake",
      "snapshot_digest": "88c642f12266316f5df2c5594c5c8a55b7a6ae095d6c862d2c25ee6b4028f81a",
      "version": 2
    },
    "201.wake": {
      "generated": "2026-11-03T23:54:36.078107+00:00",
      "head": "d535753bd85bf422c3958b08278970b8c154bfafc2c28e0655a09cab45035159",
      "node": "201.wake",
      "snapshot_digest": "9a69886e6c4b231c02275956c4ce3423f3ed0ec3b49783c1174574f6c7a4678f",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-11-04T00:29:14.676312+00:00",
      "head": "02eef0c494c39470e376062d24913a9024056a9510ea8fd036a290ebb306c034",
      "node": "202.wake",
      "snapshot_digest": "c501c759f8a811f655260a72f3a79804e9dd627af524960be810df95bb7e01bc",
      "version": 6
    },
    "203.wake": {
      "generated": "2026-11-04T00:27:31.090970+00:00",
      "head": "ddcad48b7f14d8c7f510c9cc04803bba8f77d1aff7fff0b9320fc12a66f962b4",
      "node": "203.wake",
      "snapshot_digest": "506aa15873380bcba3ac79ea2ac3a4c0b263fe04c7555288d995d97d2a69b6b2",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-11-04T00:20:31.539357+00:00",
      "head": "4aa721ae9ebcdf2344fd5ad6ef426a09dbfba08ebef496e7a2715b22290f646c",
      "node": "300.wake",
      "snapshot_digest": "0348bdb56728d530ff974c0a64bafd7b7d89befc4f543d3e3f13bdd620992f57",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T00:03:10.724314+00:00",
      "head": "45c01f4c6d728c84b50c91d14fa5eb1d152b5c1aac39092af9242d28d77ddde2",
      "node": "301.wake",
      "snapshot_digest": "fbd1034b296847fb5094ee2fac51cb1570e2bfae351c9af3dcdb4b0f6b22089f",
      "version": 3
    },
    "302.wake": {
      "generated": "2026-11-04T00:25:45.762040+00:00",
      "head": "ce4db180cff3413be697b56ef54f18105f59fa3f4bf2095c3493f57e9080b332",
      "node": "302.wake",
      "snapshot_digest": "48cf23c2c34be434306ba8a4b94ba93e28f75d58382918995d72a78bfadb7a07",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T00:17:04.838024+00:00",
      "head": "e2a6fc853fc182735a568f65c0ffb45a62005eb3f57098a52ed2429849c6e384",
      "node": "303.wake",
      "snapshot_digest": "a414054202e1e690327b19913f5e40dbff7ffa26fb122989a0797d352bd6d0e0",
      "version": 5
    }
  },
  "version": 45,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33326235656263383832303434343533.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d39376138353364613634356534396164.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
