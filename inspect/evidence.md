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
  "generated_at": "2026-10-30T23:35:01.285162+00:00",
  "head": "snapshot:a60ba6ec1b9edf3b4e3a26269a727c01daf4a1835b362423861883305b787fa3",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T23:31:28.289551+00:00",
      "head": "1ddac4562225b37cd2b89360bfcd52d6a947ce999bd770081f929f408d552ee1",
      "node": "100.wake",
      "snapshot_digest": "64573be4c930135e5f18908a1eb1aba1e8669d8b918e68f1e9827ebd4bfb8b02",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T21:48:03.677895+00:00",
      "head": "2e774ab9de676278dd2b40430fb53fa278091fe0e285e5d6db424d86fc4477fb",
      "node": "101.wake",
      "snapshot_digest": "3a395731829cd8ecf403cb52503f56a9529a5147ae3e35f3e93376b5f8c0f98f",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T21:48:04.506184+00:00",
      "head": "319d6415266cce12e95daa1a775302ad3091e0686989bbdb54a5439121ad2372",
      "node": "102.wake",
      "snapshot_digest": "611182a33e7328117d1f7beda032030c53fa42ce17e1dfc0772c9fd49c764829",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T21:48:12.707779+00:00",
      "head": "a846389ce089d41c44f44fc85fa5d3a4b2ee3a5fcb127f916196b5547ab648e9",
      "node": "103.wake",
      "snapshot_digest": "5dcb6c22424f2c32522c5a0cfaa243f263d90d09b6e72462a38306d581fea892",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T21:48:15.002298+00:00",
      "head": "20add9875d59c7b11e7049a98796c80c4f4f5ed30dcda28ccf72741a2ace0403",
      "node": "200.wake",
      "snapshot_digest": "030531bf01808714f194e5e4b6ea6c73af0bae46e115c977c5a21ad005a6d72c",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T23:33:15.797370+00:00",
      "head": "4ccb1bed10c0b36efc192d8813a7fd39c0a6f333d772d50fdb0c7b75c500f0bc",
      "node": "201.wake",
      "snapshot_digest": "b684caece5ae3b452c5a93b11d1ed09ad6357e03baaa5487d57b1a70f67c26ea",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T21:47:57.774248+00:00",
      "head": "df5c1f8a075a861ac7be5ea12bcffbc683a0428ccbebf8e6289bef79c2c6ffbf",
      "node": "202.wake",
      "snapshot_digest": "4f0c9d3f41fbc3519494ada166d07ba058957ecced98d99fbbaa77000ec88e9c",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T21:48:02.671980+00:00",
      "head": "6799c9b52fd9f104d7ce52a9384415d435b2e40b1c203907153f58af142176d3",
      "node": "203.wake",
      "snapshot_digest": "25f16336d5736cb867f49b7710d6e03eb2f0aa0e2a60ac6394a2d8e5ad8fd340",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T21:48:05.750989+00:00",
      "head": "d0bcc3a7595c20d383a0606a44d55a150a556aa58589dfb6bb8926625c436ad5",
      "node": "300.wake",
      "snapshot_digest": "16307f1b945c75d8805d48d775cd04977300362c2594891162557c9d2fb35c53",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T23:35:01.285162+00:00",
      "head": "54413173ae7c3d074f5717b2cb25eb25c06fefc8f41e395f04d8de8e5c6123bd",
      "node": "301.wake",
      "snapshot_digest": "657231cdfebe899f5c2994fef2caeffc83bcf0acf6fc8d2635655c49085a396a",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T23:29:09.718965+00:00",
      "head": "33df9c189b939061e40b33f5381a9646ecde1039840e26cb0e2202089c07eba7",
      "node": "302.wake",
      "snapshot_digest": "85add7d7094e5f2096af41598380540fa1d85d346bb06868f303ca22f1d8ae3f",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T21:47:59.639472+00:00",
      "head": "e438f4e8278fb8f9b31bf54b7d652d1248fac47d8a364f1b951cfbef94f59c94",
      "node": "303.wake",
      "snapshot_digest": "642108e99918455531bcf1a4277c4754eec1b407c9a6de05d8b6b2d5d074d377",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61383466666138666261376134373039.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d38643966313264333135376634313236.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
