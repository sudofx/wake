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
  "generated_at": "2026-10-29T04:46:45.518984+00:00",
  "head": "snapshot:fb4e340927f6c8d946f3e81522d98bf2d7d2a628b13c103b735fbdb96c28e0da",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T04:43:23.635565+00:00",
      "head": "d2394e79b8e7148e06b9a0607111ff4f2467d0b59a74e0e54cc092c4eaafabad",
      "node": "100.wake",
      "snapshot_digest": "d7cfefc5494c2e5a6c0781f1117a3f841583ed2ffa8fba6e326a2705ac3c7a04",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T04:44:42.669155+00:00",
      "head": "a381713c69f7de51e9a274a55f963f40eb071e12d27cf0802507799bbcd8e7e0",
      "node": "101.wake",
      "snapshot_digest": "c0e1f6a49d940de01580767e0710b3813eccf23fb3072d777742d3998cc18240",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T04:46:00.918145+00:00",
      "head": "fbaa70dcb7fe217bc6179c0efbbcaf937907820ad97774f2cc323da270cb9710",
      "node": "102.wake",
      "snapshot_digest": "1a64c2c93ea8a949c322f0ae7219d176b5f20ffb4d4f4d84d1db57b374f50217",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T04:43:25.802591+00:00",
      "head": "104c176e34c527977699748ba8275dfb364949dbba0c9fa4b1d74e45d6b54a07",
      "node": "103.wake",
      "snapshot_digest": "5ebdf890842309f3917734c23f89d895be1126a616eb585db8c7f2469f12e194",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T04:43:16.418081+00:00",
      "head": "da06246e9d097ea032d8567e0fa8743315078caa6b06b3601619a874f6d8bae7",
      "node": "200.wake",
      "snapshot_digest": "1e49409f606b6dadf147e0f7aed3b33e0504e212ecc5c049b8cbd83ec4756d70",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T04:43:51.062489+00:00",
      "head": "9d733e6d4c7d82e7c4fda862beff5fe494a942679ba050741daec8db55ad710e",
      "node": "201.wake",
      "snapshot_digest": "d5643d49712542678fdf361b978891fb0c8c86a5712583627447fb6833a76657",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T04:46:25.102777+00:00",
      "head": "a85950023b0f5f4f78f88e866b8448a98156c466f9385a246b5b3a07f0450b61",
      "node": "202.wake",
      "snapshot_digest": "6737fec5765401588c1cc044259991a96808e45111551ec0b45403d229def826",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T04:43:49.063793+00:00",
      "head": "ac6e32c423f3643fbaea921023f48ee0f3aafd6726697d4565c6c7683a183d40",
      "node": "203.wake",
      "snapshot_digest": "9e74336a457a23688a68bfd1fc2e07be0d7677eed797417f16e3dd19916705c4",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T04:46:00.556145+00:00",
      "head": "1f6f7477af9ec45c3a37e32c498a66aa58f72f54796d70583511919c47b51765",
      "node": "300.wake",
      "snapshot_digest": "f9fb3dd5c47ff60ff82cca1a6fdd4647c314871a5a61d7de48c98530571066d2",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T04:45:55.934997+00:00",
      "head": "3744a480bb7dea43745f5f7e7be394c6501ab14304081f3ce03af410a09c6f6b",
      "node": "301.wake",
      "snapshot_digest": "77319f130afd6f0f36d00e790493713cff1e3d0b5e1d1a3335bdf78ac1a35413",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T04:45:05.492306+00:00",
      "head": "3e2c5df567c38e0145f92036acae6e0a8ca649c1942edfa6eadc3e2680be37b6",
      "node": "302.wake",
      "snapshot_digest": "d5a0af5f7f53be0ce82cd63ac3e22e6babb7a59448f98fac8a54846bc9f45f9e",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T04:46:45.518984+00:00",
      "head": "9ebe6446d8089e5df2284da203478f537c44978e2e3fd8e2f87accdab074510d",
      "node": "303.wake",
      "snapshot_digest": "dc42b71bcc960a332ad0dbee0e1019c8a482df8e50eb20f46e1cc4d87632f95f",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d39383762653034613535303634616233.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d31373264306531656533333934643561.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
