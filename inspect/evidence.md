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
  "generated_at": "2026-10-27T22:02:39.030406+00:00",
  "head": "snapshot:4e3f493b9e45d1a8635325489a8b1a1e20881c53f707417263329d5a57282f98",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T22:02:33.138651+00:00",
      "head": "40a6eec74706cc4e4c2c1c520ddd0150e52695636d8a6f0d53311e0a81399701",
      "node": "100.wake",
      "snapshot_digest": "40d7e0a98a667094b7f0d44175a1ae2f24d3e44871239e2d99e23638d8876160",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T22:02:17.284023+00:00",
      "head": "04d767f4616464d969419bf6c8ff0f7775393b8f1db736f5bda9a5c3a5961de2",
      "node": "101.wake",
      "snapshot_digest": "33c717dc8d65ad7bf255d4a6ce2d11996d8a2477e44fc555c73e39e8a1943a5f",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T22:02:21.440337+00:00",
      "head": "ba3280f11062c6ba6fbd1684939068b632fb788cbe67eff30e1d3a3fd356c6af",
      "node": "102.wake",
      "snapshot_digest": "bd1b183c935f56490be2175efd687ce2e2076a6156ed42a37a1624dcd436a2c2",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T22:02:38.274757+00:00",
      "head": "3cba5da6f1e275fabd492af1b8e4533cba1bd4b1d7c6629183142108e7e764b7",
      "node": "103.wake",
      "snapshot_digest": "eb0779a175be5b0d56842ca128c22c27f5e84d88d6279985635f7dac7b025807",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T22:02:37.414294+00:00",
      "head": "d070ab581df7a66c03e9dadc99b0081edebf687d2139b3c0a44796ed83ef7d0a",
      "node": "200.wake",
      "snapshot_digest": "1e8f1a196fff5e24f6e7501fbbf5b4330d1fdf4e2f9b31c8613402d101c349a6",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T22:02:39.030406+00:00",
      "head": "c7f26412e349b6f19a9a70db4e392cf302c8e5664baf4e69614688d2dcc811d2",
      "node": "201.wake",
      "snapshot_digest": "9165bfa4b2fed112b533e24b02c1dca1a9ea633e1e838e5c360781f2ce1f8e7c",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T22:02:17.939411+00:00",
      "head": "9b389841dbd57abd2b644cc10b72b65f8465b8697051c38add396214ab96091f",
      "node": "202.wake",
      "snapshot_digest": "35b0a3f92d75d89e27f155eb44459979ad5d6437c0b26aa4520bec80dfa06fe1",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T22:02:11.973002+00:00",
      "head": "4ba530211255e8b5789790f8fdc78ed6f13614380e9904c631589c52fb656ebf",
      "node": "203.wake",
      "snapshot_digest": "e0d1c7431610d044d12e35cb850c8a4b92bcf8ef729ba03e824d0d8bedc155e9",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T22:02:11.822907+00:00",
      "head": "68c3d120aa4aaee452ac6663f4a6a9fef38d5b75c14f8c15d50b4c5b54b4e11b",
      "node": "300.wake",
      "snapshot_digest": "1dfdff0a278144da6fa9ae773ccba94850bad34daed41c668ce3a841b5d1fcb0",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T22:02:17.326417+00:00",
      "head": "566253c9a75ca72c319ce326b1ed40d6a69934aec9b32131c7582c3b07ef91af",
      "node": "301.wake",
      "snapshot_digest": "1c684da474701131df63a6eb455293410d594d726d4ebd22dc308cb1adfcf6e9",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T22:02:15.282862+00:00",
      "head": "faaa75ff74926c6a1719da2e604f61ae28f87f53c9421b89416bb24c79e94488",
      "node": "302.wake",
      "snapshot_digest": "0fed2c8c00484f7f5acfdb00f724ae10bf3fa561f5afc703a9cad6ce555abf30",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T22:02:18.650899+00:00",
      "head": "b90889e909b909b0e4d8a796098bd610abbbb1fb4deb19d66ef6a7482f518437",
      "node": "303.wake",
      "snapshot_digest": "c1c59d0179fcd234118cd702b3f53eecfaf40894fcc10010f22b38bd19a3c98c",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32313262653439336532303134363861.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d65303035326361333135653634363731.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
