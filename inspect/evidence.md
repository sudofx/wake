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
  "generated_at": "2026-10-26T12:46:12.569471+00:00",
  "head": "snapshot:0708ec7bed18f2ffc05044e361a7c5bc26540a37a0619982db5e47adebb3c7ad",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T12:29:33.594059+00:00",
      "head": "22eca1dd347ed5a959107cbee49ec99ff80d765ac983f34a79e3b2c73d9489f2",
      "node": "100.wake",
      "snapshot_digest": "1bd0bf379392567efb504dc35b22f4a94e18439c1af4ebb85e0142f6081f310f",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T12:20:02.207257+00:00",
      "head": "960031d1840cc1e917095ef97a7e875cf478fbdb29eb1dcd7e1622bd1e632cb4",
      "node": "101.wake",
      "snapshot_digest": "117f5f8ccbf98c902dca9204ecfc8135a0bcb74a0029b7cc97a1281556e898be",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T12:40:07.863115+00:00",
      "head": "cbc0d0144f5b44442fa9b162c38beb99daab4b19a87409f958758da2f11c36a5",
      "node": "102.wake",
      "snapshot_digest": "163fb3d937befb3e0f3cb4a64c46db97468b28f26783a468551adfb1d7101723",
      "version": 62
    },
    "103.wake": {
      "generated": "2026-10-26T12:46:12.569471+00:00",
      "head": "56e28e5a5eeaa3c978ce5077a2c0ddb351710bca96e433d232f566f34c3cc126",
      "node": "103.wake",
      "snapshot_digest": "ffb03bb8af3a02c3b280c7718ab74349f7a7b37f0306bf85cf46ff8958fd0748",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T12:20:03.443888+00:00",
      "head": "5a077d211409bd4983847de397d126cd9a95bec25e500e525ef05c9a30ca4a28",
      "node": "200.wake",
      "snapshot_digest": "279c0c026e9f14b6b76fc5107120b7914472eccb91b02e06fdc8478e5bbb37eb",
      "version": 41
    },
    "201.wake": {
      "generated": "2026-10-26T12:20:03.593365+00:00",
      "head": "b0f209ba620e71899c87eef875b808070f268b016533b46bb4beaa3023dbec4e",
      "node": "201.wake",
      "snapshot_digest": "944f083ffad9bf6c3498ea1585b6af1433ad92b8d0a26747b27695bbf7be4228",
      "version": 44
    },
    "202.wake": {
      "generated": "2026-10-26T12:20:02.560317+00:00",
      "head": "dc3bb6d6f5576685c85fcc4d1b1039ea1bd602d42a5b60045a07e6dee97dfbcc",
      "node": "202.wake",
      "snapshot_digest": "57cc10f8333697e3afec8a94dd128200d8bc0ff6fd4c8cd0ed4e18e85c6eebf4",
      "version": 58
    },
    "203.wake": {
      "generated": "2026-10-26T12:20:02.023727+00:00",
      "head": "06a820b2e171f3e8fb2ae0c7ed4e1b62c42564c6bbb9730e205ea3d98f0e3c6e",
      "node": "203.wake",
      "snapshot_digest": "2d5ebf5a1d4453a660ab64a0ed6bdda9a13817d17aabc1230126ce142ce50aaa",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T12:20:02.168207+00:00",
      "head": "be338a3a6bc8bd1b22704c4aa06c6f3fe16b5db1d0e99303f3a734fecd431337",
      "node": "300.wake",
      "snapshot_digest": "f2a28dd3cfb04454ea450ff8503bdda7f3db2ed24749a0498f5668155c3658cf",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T12:42:05.317020+00:00",
      "head": "ca2f87de2bd113d2769aac02dc40f38f9687781781b502222be7460cf69a8083",
      "node": "301.wake",
      "snapshot_digest": "2d9eed2236aca3bb44f884c90a6fc92419a89ce594e1c86db4bda6fa8935c547",
      "version": 63
    },
    "302.wake": {
      "generated": "2026-10-26T12:41:26.977253+00:00",
      "head": "2816cba1e1b4d3be80cfd9c3ed6d4e4ac04fc0e120ec1eff4b55aae7304845f6",
      "node": "302.wake",
      "snapshot_digest": "65024e8e00e83da2974e45f55bcebdf92d157edc29022064af2669d40b99b8f0",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T12:20:06.065081+00:00",
      "head": "36789ebcaab0dcc003d3090c73f447f60b7eebf191cb178df04aa5fcff6713ff",
      "node": "303.wake",
      "snapshot_digest": "63c982b71fc41b23b13cae78c945de1bf7f35d801499d0be7da90dd648a93e74",
      "version": 56
    }
  },
  "version": 569,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d35633830323338336333343234373934.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d66656363326638643838363434636532.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
