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
  "generated_at": "2026-10-23T16:45:33.895243+00:00",
  "head": "snapshot:86041389347a09359c1ab8ec85543df964bfaf64c946e70487c902013f3d0f7e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T16:45:01.125586+00:00",
      "head": "4e47be03ac8b51c5dfd10e5aa6345f9bd8bbf949d6d6e3398b7bb6ed6b5af41f",
      "node": "100.wake",
      "snapshot_digest": "84e450cedfbfe58b959e6ce0638558eaaae80e770333097e33cf54be2aa14508",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T16:43:38.390911+00:00",
      "head": "ba20a4176168c38099f1ffe61eaeae0036531e716a2217b977247c963dad2aba",
      "node": "101.wake",
      "snapshot_digest": "9675a7eb9e4d67a4b2b9fdda6d06763765bec56e5ff6ff847913e85be73ea7dd",
      "version": 26
    },
    "102.wake": {
      "generated": "2026-10-23T16:42:56.693919+00:00",
      "head": "7ac58cc11680be3239bf305d22ca5646f2a95b340ee3f1dd96daac1cfc53f013",
      "node": "102.wake",
      "snapshot_digest": "e4fb65ae7ea1dfa11e68c433e2c9b141c468e0f3ca94821f883e378a52137180",
      "version": 33
    },
    "103.wake": {
      "generated": "2026-10-23T16:45:28.193018+00:00",
      "head": "902338d6c01201dd3a510af41a679c4fca9f839def28b062b4a15fd4961aa4fc",
      "node": "103.wake",
      "snapshot_digest": "53370dc3e0fdd78f12ef9087325a74b1082ff22833cc5a701c29976a01fe5923",
      "version": 23
    },
    "200.wake": {
      "generated": "2026-10-23T16:45:14.176697+00:00",
      "head": "5a4b60d4843e3ad3e4fac7b1a0eb650d4c6022a038d22ec6d064e8a5df1de0ad",
      "node": "200.wake",
      "snapshot_digest": "ce04f1211934b4a0962e5a09a7dbf3b37798e2b62c87ae490fa47a7843f88c44",
      "version": 21
    },
    "201.wake": {
      "generated": "2026-10-23T16:44:55.018733+00:00",
      "head": "a137fe3af6e219c54b731dd386f9e2dda027d52afde65dda9898c7560379f33b",
      "node": "201.wake",
      "snapshot_digest": "430c68925979e16a3632f8404e1ba3e84bb5041b768422338680bf5840016c26",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-23T16:43:49.664096+00:00",
      "head": "339f9031c8ebfeaf3c00e8e0ff863b4dc2e47faf5e77293ad8df756ae7433429",
      "node": "202.wake",
      "snapshot_digest": "2e1794714fca863efa7457f58476ee9b787c7787a93128929c720eebf48475e9",
      "version": 36
    },
    "203.wake": {
      "generated": "2026-10-23T16:28:10.137935+00:00",
      "head": "7ed38e30c69f6795c8e9396cabbbc8373990cebf51f46db971c3fcadfca56e9f",
      "node": "203.wake",
      "snapshot_digest": "402b9df65c0659122748ec209ae960c36384b5e47229186cef2c191726c465bf",
      "version": 15
    },
    "300.wake": {
      "generated": "2026-10-23T16:45:33.895243+00:00",
      "head": "ccf1e3f535df0824b7a5b1a99bfaa5dcd4fffffeed7b421b2b680d126542dd6e",
      "node": "300.wake",
      "snapshot_digest": "bad4c1c687c5968409da1bc7c38b3802ec18ae84115a1ab568fdee9a831c916d",
      "version": 21
    },
    "301.wake": {
      "generated": "2026-10-23T16:43:32.060258+00:00",
      "head": "225d4a53a78e47e5c795b5affca034c6658b9a970c1d25e6ce00459bc18996d0",
      "node": "301.wake",
      "snapshot_digest": "d27822b6e8e92f182522c5d621028a676b25873321e519873836f918d216d504",
      "version": 33
    },
    "302.wake": {
      "generated": "2026-10-23T16:45:20.493432+00:00",
      "head": "03e9f0e071450399f4b4f6c5cffe6de173fe9d8ea5c12cbfbf32b764305c4743",
      "node": "302.wake",
      "snapshot_digest": "cd6a206a94fec6d7b50171f0469d9e8a226c48f8bc6a06b46aa774dddf633464",
      "version": 16
    },
    "303.wake": {
      "generated": "2026-10-23T16:03:26.598087+00:00",
      "head": "b847863af4cd745ab79699da78bf414cafa0afe6b3f59729aec9e582d19ff689",
      "node": "303.wake",
      "snapshot_digest": "db6c83a3d201eaf3975ecc956da19b1d6c96e9bc88cc805fd450c896cb0fe9b2",
      "version": 30
    }
  },
  "version": 292,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d36333430613330633732383834363063.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d366133646531326366356166343230/39.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
