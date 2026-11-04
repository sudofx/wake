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
  "generated_at": "2026-11-04T04:06:35.625703+00:00",
  "head": "snapshot:68ba483b03745e63435e9f63a90578a6291b46890c09db5de01cbe252a9b4068",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T04:06:35.625703+00:00",
      "head": "d101a9175cacd9d9ddabc4877bbeba91ef55b37e241e7fdcfeb0faaa54af981e",
      "node": "100.wake",
      "snapshot_digest": "4c6d65e85423cb08cf8d89347ec5903e3de967258543d616a020b7825e18016a",
      "version": 6
    },
    "101.wake": {
      "generated": "2026-11-04T04:06:31.713455+00:00",
      "head": "39eab00f4d2cc82bdb2536ebdee93cec30c4a6e68ea8737b31e3dfe4c2767635",
      "node": "101.wake",
      "snapshot_digest": "06074280a0c0e6505fff4e59ab730f44c10dfc750add2982e792931b279cd1da",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T04:06:29.949769+00:00",
      "head": "34e6a179fbd943d1db4c604917d0d73ac9d5f90df07737d4c373e3ba475cf174",
      "node": "102.wake",
      "snapshot_digest": "a166be02e09e086319e7817399067ebc87f1818f831665a9f35c2a11ea6c1374",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T04:06:29.368444+00:00",
      "head": "c8f457d0ce42bc1de7c45c769c46e71430b06c2ed9d616ba203c78278deff26c",
      "node": "103.wake",
      "snapshot_digest": "a9bcae8da0a399024a77ccaf3f3301c19c3901183cb57bcb755fb80711c6e304",
      "version": 10
    },
    "200.wake": {
      "generated": "2026-11-04T04:06:31.029373+00:00",
      "head": "88d9769278c6a92bd827b6a3dd7aad766da5bb2fc2eb23bdb3a5b7a71b1db1f1",
      "node": "200.wake",
      "snapshot_digest": "ec4c9ca5b3e9be886752f3023f021124a3ab6b74d24257437067a4d8f56ab096",
      "version": 8
    },
    "201.wake": {
      "generated": "2026-11-04T04:06:30.734438+00:00",
      "head": "3f67b2da7a8b53ffeb613d0b9ff01cff24400555ba7c67957c244ee2b05eb9ba",
      "node": "201.wake",
      "snapshot_digest": "1b5ebb0aaa6b8d073e1cd568f0b7af5db382cbb953dd795f10597598c8c2bcab",
      "version": 4
    },
    "202.wake": {
      "generated": "2026-11-04T04:06:29.077142+00:00",
      "head": "aa5ab19a5100529453b97b9c234ab813a72633e0f1e338a1a56f71dcea2871b7",
      "node": "202.wake",
      "snapshot_digest": "fbe5e4ffb51b4e0f3494cb5dcf47d9ea7b1a04a8e2d6d8518ab5a9d2e834fff6",
      "version": 8
    },
    "203.wake": {
      "generated": "2026-11-04T04:06:31.318571+00:00",
      "head": "4aedf2f86bfef0a79d85782c6553b9fb7330b4ea0cc77503e98e05cb1921a0d6",
      "node": "203.wake",
      "snapshot_digest": "2a3036b17c4b5f9cad0bc4362e8e49b810d8b365555ab5459537ebd769068fb1",
      "version": 7
    },
    "300.wake": {
      "generated": "2026-11-04T04:06:29.894725+00:00",
      "head": "c0678cc77fe9be9685e60fdf8fc4ebc44de04916bb0ef5baed3f9c5275550aa5",
      "node": "300.wake",
      "snapshot_digest": "f3daa03ea9b6504ad6720536e2d74e1459f39b61d67702655e61839683b61e77",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T04:06:29.203587+00:00",
      "head": "2973f43fce83faed10b3c9a6e1ee37ba239e9af3516f2b5c50b2f26ff8947664",
      "node": "301.wake",
      "snapshot_digest": "253ea04e991bf6d3ab2a22d192c3eb1f58b0b081be925d7a2c72442551c2d035",
      "version": 4
    },
    "302.wake": {
      "generated": "2026-11-04T04:06:29.369054+00:00",
      "head": "4efc374fdda17d06b2229152cbd4b16fca24c93aa7f3dd89217cd93a126f88a2",
      "node": "302.wake",
      "snapshot_digest": "89e94e66340a8f9fb3d14d903bcaa28f3a9cb939f79b5ecbef6b20fe7a6f0b7c",
      "version": 3
    },
    "303.wake": {
      "generated": "2026-11-04T04:06:30.356078+00:00",
      "head": "48ebd5d4147e289b08b2edcb3449148fee8e3a793a0979ec12dcda84430a98a1",
      "node": "303.wake",
      "snapshot_digest": "b8e3488e7307c907fafe9152817633f84e2f13dc8d327e070a1e7dce8547784b",
      "version": 8
    }
  },
  "version": 72,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d61386235336163393832353034623930.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d65633138653835353837366534666361.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
