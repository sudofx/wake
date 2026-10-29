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
  "generated_at": "2026-10-29T13:32:44.127943+00:00",
  "head": "snapshot:eefbb7edc2a69f54c4c75c27917876e15d3d2d6671295e050d893c559e28cc9e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T13:21:02.687365+00:00",
      "head": "4ecdf9c14b831849e5befd58c1a4ae618ea7e321a475c671230c1f8be252672e",
      "node": "100.wake",
      "snapshot_digest": "8decc81ff518e63d51c84b12804e8d5528bec3802776b1560dd098d094508ad9",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T13:15:13.674129+00:00",
      "head": "6acd8fcdbd6f8d1b9c1f4f6eae0d7a5888cad805c833518d83b9356130bc64df",
      "node": "101.wake",
      "snapshot_digest": "86bafe02d69a63b93be127fc303176c07c016bd124feee38be7461879e6b3084",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T13:30:56.926973+00:00",
      "head": "cc4f8c93091be123c3da19c1e82d03785969cfe8dc05e3f30bb21e86537853f2",
      "node": "102.wake",
      "snapshot_digest": "6f4a4f842b2cfb90da5b1d1a1a6fcfbb531c9227f2b4dedec04cd8a20f82c913",
      "version": 18
    },
    "103.wake": {
      "generated": "2026-10-29T13:17:08.077961+00:00",
      "head": "fc14405b471286f326bba15514f8099c7bfdb230b5f26a30537c4407d150e43f",
      "node": "103.wake",
      "snapshot_digest": "41e98afc4f16e397b3194dddb34ac759b8d61151877bda7363a4843ba6f7e9fb",
      "version": 29
    },
    "200.wake": {
      "generated": "2026-10-29T13:19:03.803485+00:00",
      "head": "62cc81cdb4f66475aeb11ce05f27844293f4c0e5fedd99e951f3d698c2f12927",
      "node": "200.wake",
      "snapshot_digest": "312ad26b3ce8f7260d1f1673c580775dbdc04dbc2a6d684d909194a60e018f3a",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T13:05:03.947846+00:00",
      "head": "86a1848ec1aec976a543f59ae06cf2f8b4db1b1261db2233dd3d6add6463805f",
      "node": "201.wake",
      "snapshot_digest": "a4d24866bcec05424faefdb86c9fa9a7f532a41c10bb38b0b375686e34db95f3",
      "version": 23
    },
    "202.wake": {
      "generated": "2026-10-29T13:32:44.127943+00:00",
      "head": "ce590a148fa006c083f9d090f4756e3c614ceddb37b45d5ee59144532484714b",
      "node": "202.wake",
      "snapshot_digest": "8e8c4433d80b28ac72e3fcc4461d819af2de6630665370eb112cc869dfdf7c8b",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T13:13:34.469997+00:00",
      "head": "7cd798db0f9840eab7e8bf68cfa119a55c8febeb329f75fffc097e23c039cfbf",
      "node": "203.wake",
      "snapshot_digest": "5fc4176f469b111aa33e2b638504660a6a38d20cddf60eed91279ca098109b76",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-29T13:27:59.606529+00:00",
      "head": "6883f13c714195427457f8d1cc592bba659e7c7c64698c83a728f3cc9a4b74bf",
      "node": "300.wake",
      "snapshot_digest": "a3d57cf65593485de23c57e2e95873ed2286927e5d6300a80d46a71421360e78",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T13:03:29.613159+00:00",
      "head": "7999e531c6297d79f033c8d0acd686bf3e0dfefba6c061a20bbe315750eebbfd",
      "node": "301.wake",
      "snapshot_digest": "3dfc6da999a0bce21ec1e3107f5d213d303d30d0805d6401359b1f30a7d1e410",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T13:22:30.549639+00:00",
      "head": "743da20f223ccdd691e16b1185437fcebb9f8f1fda2c8900257f86302ee471bb",
      "node": "302.wake",
      "snapshot_digest": "5f1996c0f3a4caac0414340331f7b1e085aa0df669f500db36de42e99b400ebe",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T13:07:55.000077+00:00",
      "head": "d30009bfec3ac4919556f44a0aba576951b493e3bc5df0cf10acecffa5c108e7",
      "node": "303.wake",
      "snapshot_digest": "f05f3140588ea6d4467e2cc9789685800c5fae59493fc474d70c45699e9d8181",
      "version": 24
    }
  },
  "version": 295,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d386637373431623366613330343762/36.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d613466313134356332653337343062/65.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d726573706f6e7369/62696c6974792d666f726d6174696f6e2d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
