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
  "generated_at": "2026-10-24T14:25:31.311428+00:00",
  "head": "snapshot:973d8f026b82a412e04f5dbda449171ef55b0449f7447e3535ca2c5f64796b3e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T14:21:58.673043+00:00",
      "head": "4dc24a883243bf68ea75365092e2fafd1f20589f743e59754bbd79355aed8c9f",
      "node": "100.wake",
      "snapshot_digest": "3be6adf1fd7c5b8e1896404023915f68d7bbcb5655263a65352634a0ab47a70a",
      "version": 22
    },
    "101.wake": {
      "generated": "2026-10-24T14:22:12.224643+00:00",
      "head": "ccbeb2b01f14e8597666a23d2408e91a4a297677e1cddf0db322b5df2a768fce",
      "node": "101.wake",
      "snapshot_digest": "28c5c56e67d547442109537a3043c441eb733dc7935b561348defcf2d4997ed9",
      "version": 36
    },
    "102.wake": {
      "generated": "2026-10-24T14:15:34.693888+00:00",
      "head": "040a67ae3ce7838eb8c1c3b83e45424961954f6255254c3db1796896f69a0536",
      "node": "102.wake",
      "snapshot_digest": "33e32b955141a070d0cb869e49d40f52f9dbdffbdbb0fa377d480d7617d47712",
      "version": 43
    },
    "103.wake": {
      "generated": "2026-10-24T14:21:19.635388+00:00",
      "head": "8d0f5b4c48ebd38c7042f2323e7806b6d109aa02029416c1f5642ff7116b3d7e",
      "node": "103.wake",
      "snapshot_digest": "e74a93f9d4c9a9120cc5f7eac8838bffb986f3d3b8d3debbfdf32d8e482e0dfe",
      "version": 34
    },
    "200.wake": {
      "generated": "2026-10-24T14:18:51.608599+00:00",
      "head": "8fd5fe4dd92291eb7af0b4cd35ccd3e0673aa88b8c7c5a6f6c3a60dbc138264f",
      "node": "200.wake",
      "snapshot_digest": "aa178df08b8e1731c55a0955855657164cb2465a555dd2271e50aabc19eff94b",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-24T14:20:38.157938+00:00",
      "head": "60dec2fc1e279d03a56e2eb84af26e8d0c87278f15b0a38c0911005a077de52e",
      "node": "201.wake",
      "snapshot_digest": "eec64e5c6b76eb9d2ad83e3b30eb28a98da5ec471b7beb0db57933d27d15d842",
      "version": 32
    },
    "202.wake": {
      "generated": "2026-10-24T14:21:44.962805+00:00",
      "head": "0ab9703004adb335a8f29a6fedd797ff42c5c271f8a0396ba0815d2b8af7bc95",
      "node": "202.wake",
      "snapshot_digest": "df4407342bc445b854ee6375d9557003c06537c725c4b61d63c680d469c87098",
      "version": 43
    },
    "203.wake": {
      "generated": "2026-10-24T14:21:09.983232+00:00",
      "head": "bbb352c36bb2cf40c83dd59a01eee652003a63572e9f24852f1331dae8d29769",
      "node": "203.wake",
      "snapshot_digest": "b940f527f3cb55898dcc5d307a0206dd8fb9c0a0034d3282ee7d0ecdabc0b74b",
      "version": 25
    },
    "300.wake": {
      "generated": "2026-10-24T14:09:15.716449+00:00",
      "head": "71539ae8a4059158bae4a7d89812bdb4ac8a1b0e77d71e92822ee60c84190ea6",
      "node": "300.wake",
      "snapshot_digest": "6484091a861c92e1944b98199b87adbad6ddca43c5f792d1d1f2f61618fe3448",
      "version": 28
    },
    "301.wake": {
      "generated": "2026-10-24T14:18:59.304377+00:00",
      "head": "a1554e8dcd08b0b4e6e2f52a52ca28a530ff41423b37877bdbd2c54f11561fac",
      "node": "301.wake",
      "snapshot_digest": "d5e49a5ab0a8ab76869cbbc607271179f875e4e8fe530b072df7018f7b161d3d",
      "version": 45
    },
    "302.wake": {
      "generated": "2026-10-24T14:25:31.311428+00:00",
      "head": "7f1cb0dd75b141d5cb1b084cd6e0e04307a8bfea5a2dce54c6a3de2dabe87c09",
      "node": "302.wake",
      "snapshot_digest": "637531cc2deb7fcdeb97df78b02f9653e37735de0e12acae98a98393896ac0ce",
      "version": 24
    },
    "303.wake": {
      "generated": "2026-10-24T14:21:29.566950+00:00",
      "head": "5e538600d01259906c923ddc6ff30a25752a47286af77cd1b2bb9796c87e6933",
      "node": "303.wake",
      "snapshot_digest": "a58210146adc8b2bdb12be6b30b9821b41072d1b1e77fe85b0b97dd5cf11d371",
      "version": 42
    }
  },
  "version": 400,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32363334373461613237616334343661.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d64653139633666313431313334396465.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
