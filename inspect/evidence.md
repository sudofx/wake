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
  "generated_at": "2026-10-22T22:29:15.194083+00:00",
  "head": "snapshot:19cb3936bdfd9c827586612575a21177c9eba708203aeaee8513295ba840e179",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T22:28:44.564513+00:00",
      "head": "330575a834854c5e83b1fb52005b0ea21bc003a93bee7425ff9c0b45f890b1d0",
      "node": "100.wake",
      "snapshot_digest": "3428497213561f812c60b97b1226b9cae7187869a15d72e66f9655bd9c7ed45c",
      "version": 1
    },
    "101.wake": {
      "generated": "2026-10-22T22:28:49.285120+00:00",
      "head": "be0d79f0783d8e3b745b67f7b151959f74686c1d1b0cf35673754a436c88cae9",
      "node": "101.wake",
      "snapshot_digest": "29d89f1c57f6564afd9b88830e15035832178cead23f6b7494663e0984d1d56e",
      "version": 4
    },
    "102.wake": {
      "generated": "2026-10-22T22:28:17.561400+00:00",
      "head": "cdc9c53a89feb7eab925aa48ec59b4add8144a0269d654e120871b0660dcdf71",
      "node": "102.wake",
      "snapshot_digest": "e099e009fa5d6e87734aa276a3a526d0e1e619ca164fdde60381e3cf0105e4a5",
      "version": 2
    },
    "103.wake": {
      "generated": "2026-10-22T22:28:31.604480+00:00",
      "head": "4fa08459d9c412c3a705c61154868b41095b119bc54ca7319d5f8566b273698b",
      "node": "103.wake",
      "snapshot_digest": "6140b0b261ec40f9c1bf33b460fdfdffd197d8223a2c64de795420e33556dcbe",
      "version": 2
    },
    "200.wake": {
      "generated": "2026-10-22T22:28:56.200541+00:00",
      "head": "ef676269e8705eb13547d816d5bb4fe6f6c2a969a23c460dd98164c56db22290",
      "node": "200.wake",
      "snapshot_digest": "b64b303b0e7cba97fb4c18f03b2b6fef5a601c1c62d0dacecb91f694faba57fa",
      "version": 2
    },
    "201.wake": {
      "generated": "2026-10-22T22:28:53.919158+00:00",
      "head": "803b99bccb67a9f5d46c98c5b701ca66897f5da130985ea7f2f7a84540a1f7c5",
      "node": "201.wake",
      "snapshot_digest": "9cf4bafb82b76dd6705f6727cd83df7649bd2ffbf6504a77917e9c1b6715ffaa",
      "version": 5
    },
    "202.wake": {
      "generated": "2026-10-22T22:28:28.883753+00:00",
      "head": "65adc09a93992ba73dd857cd47a3a74d06293829d188f008bda1901e6cbec848",
      "node": "202.wake",
      "snapshot_digest": "311c697fcc2c3a80ea8f05aeb81bc8483dbc9b37d3a6c0fe9ab3e6d6173d31ac",
      "version": 6
    },
    "203.wake": {
      "generated": "2026-10-22T22:29:01.806946+00:00",
      "head": "249bf46974064341967b124501a83c73427755f6195885bb79e0404494043ae6",
      "node": "203.wake",
      "snapshot_digest": "8df0a058ef41f561844abecbd413855aeb893d4cb4dc19cd5e1e5c26528eae3c",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-10-22T22:28:51.518176+00:00",
      "head": "479cf45ad6b707cf710bf92600b57a862cb243836e90e89c156c4b779ce09387",
      "node": "300.wake",
      "snapshot_digest": "aed17a33420278b68a461644c2c84e004e46e97f4ecce36f7e3b6a392e5b5ffb",
      "version": 1
    },
    "301.wake": {
      "generated": "2026-10-22T22:28:59.674566+00:00",
      "head": "951a2ec0b412f82b2f2024cdec986305763d99807704f1be863a01f36ddafcc2",
      "node": "301.wake",
      "snapshot_digest": "c61d595579beba403b31986c15a5af658a6e91e1f973dbd42c3ba98dc7787274",
      "version": 2
    },
    "302.wake": {
      "generated": "2026-10-22T22:29:15.194083+00:00",
      "head": "ff162bcb7fb18e56c51457547d3476d7a52c5d16209749cbf5ca124a46e65b66",
      "node": "302.wake",
      "snapshot_digest": "7a2fb497ad8f00eb0bf4c991e5a465488f092edab09fc3ebcc1a188a7d3e241d",
      "version": 4
    },
    "303.wake": {
      "generated": "2026-10-22T22:28:22.540961+00:00",
      "head": "4cdafd44544bfb8e0f9735360e427fa5222e0ad15684ae61de0bcc80f28cb0bf",
      "node": "303.wake",
      "snapshot_digest": "5f5b899cb3de6a72bc54262efd03355e926083176a5c4a8588e5573b25501a16",
      "version": 4
    }
  },
  "version": 35,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d663438356138303266623437343963/65.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35636237623964636463356334653634.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
