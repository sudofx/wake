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
  "generated_at": "2026-10-28T03:49:24.687255+00:00",
  "head": "snapshot:ef3ac072c5e13c84059dfe7c3c69829a8a3c820a66a148ff161e7eb938cd9183",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T03:49:07.621026+00:00",
      "head": "58182e76b3b7189a532577820390fa0c51c3eca741ed6b6df7d9b1b3b5ca5c4f",
      "node": "100.wake",
      "snapshot_digest": "8862fd8cb8b6427aaaffcdc384d5bcea197ae834fca678eb67c1265f57f9f1f7",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T03:48:58.244943+00:00",
      "head": "519fbb0b04da3e52343bf3cb1a1c7cdcb2915ff684d2f93d1850fa645c7aaef2",
      "node": "101.wake",
      "snapshot_digest": "e3cc0af631a7aef7e6f8c1cacd8cc52bc73436466b8163374708497cab94c0da",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T03:49:03.368239+00:00",
      "head": "cbb4c68a8c5eff7794d1a12d7a2ddecfc6574175c9fe53d29e1da5fd8ac88a0e",
      "node": "102.wake",
      "snapshot_digest": "5919eccebebcbeb0e4c17578ea4ad5858cfd36d066c8cf883f1935d88d0e641d",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T03:49:16.355729+00:00",
      "head": "dad5e43865debea2bbb8055721077ebde98566cb6698b1a47fa3aa33446b2241",
      "node": "103.wake",
      "snapshot_digest": "1436ccf0ef626742ab591b11aaecba73d0417d425e1eb3502f4642e29dc104b4",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T03:49:16.532492+00:00",
      "head": "24377253200409c72b66151ef3efdbabc7fbb2e1e2b778d25311bb3d4dae30c3",
      "node": "200.wake",
      "snapshot_digest": "e91a2f224f5b0bec93f7e7a274b01db62a9809b8aa3aacbe814eb3655f12de08",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T03:49:24.687255+00:00",
      "head": "b1da7ec781d3564ab24539e2c58fc53a82970666944ed19657d5f8af028ccf07",
      "node": "201.wake",
      "snapshot_digest": "ffc62f863e82a50465e43337742428331cf74a344436717251f77a48f2e02f39",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T03:49:03.869002+00:00",
      "head": "905ba72908e6b4a31129b0024c6bc048cd2b8ff014267bcdb74c5e9746d3d9d6",
      "node": "202.wake",
      "snapshot_digest": "c4ae3c88e0b2aedb2a8f1d32dcbcfb66817ce2cbbc66a937e52f435587f880c8",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T03:48:56.642963+00:00",
      "head": "8c0f903ec79e29deeca9d667f0e499dd55ae33918d2b15de0dc86d0b704a639f",
      "node": "203.wake",
      "snapshot_digest": "3aaa54dfd7049d4abc52ea7c9bd643cc4d38ccbce3739c36555e1f99ea6587e6",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T03:49:04.602600+00:00",
      "head": "bcd2a2dda1d97255df02a5abeae99b4bf5cbc905ce7018f2318159a60f00dd7a",
      "node": "300.wake",
      "snapshot_digest": "28de0ded35d09ca3f40dff7dfe5ba211cb39b94f490a866425cec2f79703bf9d",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T03:49:05.904668+00:00",
      "head": "6120ba77889b5397677bc986fde065c6481a9a91484d7d24295ff1c7eea9b1aa",
      "node": "301.wake",
      "snapshot_digest": "530cc6f63b52329e48dc512e4c666ab1f2a653ab59dd472b52fc1fe120401967",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T03:49:00.716090+00:00",
      "head": "27e45ec837501702fb672803e5e4d4accd5068377b8a2223e667927018ca0b03",
      "node": "302.wake",
      "snapshot_digest": "09306962f98c255a4166475a935616938b94f707f7e363da49ad3d884b0a0bf5",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T03:49:07.717538+00:00",
      "head": "b9187112b31cbec3d8b05dbddbee483deaf4826cd1ee32c13b57c46303f67c00",
      "node": "303.wake",
      "snapshot_digest": "92072da2717e2774011345510cc180ea332c9c3df33258cf91f0ac9d54cb5b0d",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31636563373731323066336434333261.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d62363533646234303965363134643137.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
