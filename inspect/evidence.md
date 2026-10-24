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
  "generated_at": "2026-10-24T08:50:21.909485+00:00",
  "head": "snapshot:15515631c8806f740458262873d523aab556bf0de9e5fd5c01280eb59f6d63b1",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T08:39:49.808599+00:00",
      "head": "eb75e5a41b7e808d339843eddb7e5c0755ea9f03ad069abf3bcc006c3be0d5b0",
      "node": "100.wake",
      "snapshot_digest": "d16a0c140f5bd8f9eb86cd912ae8fd75be6b8c9c94271903bfae56b19250f70e",
      "version": 20
    },
    "101.wake": {
      "generated": "2026-10-24T08:33:20.402601+00:00",
      "head": "32e25420a26143c3c2478a6961826dc6557b80116b5289cd9b757a0ebd4bb9ef",
      "node": "101.wake",
      "snapshot_digest": "72d1bbeb76f59b26e022b2e440635fe33e6c592143fb2bad3e88388c80303816",
      "version": 32
    },
    "102.wake": {
      "generated": "2026-10-24T08:33:41.353484+00:00",
      "head": "e76eeb635c7f9f9f71b832b50146fe1522a11f3f79e064c3bc5c9b82e80a1db8",
      "node": "102.wake",
      "snapshot_digest": "d7de2258d95f26b7e974567d01eebf566d356357a3397284add4b3c0db962416",
      "version": 37
    },
    "103.wake": {
      "generated": "2026-10-24T08:46:48.747152+00:00",
      "head": "e8d58e7a2fcdf479bf7f869029b2fe41ab9cc29e63ea321c9b89224cd4f7c7be",
      "node": "103.wake",
      "snapshot_digest": "26b0b81b2a5c0bceaf2e52febc38794cdd6bd7ef1577f61c5c1caba8a08495df",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-24T08:48:35.248753+00:00",
      "head": "e79b5b94e5c77d1f1e00275aca7e3a38d3700b8d3bc563eaf56cf128a16f3e64",
      "node": "200.wake",
      "snapshot_digest": "0ce0aebdfdce40c5e692a9c1fda1eef411637726300a8d5797d076c96f3a7896",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-24T08:45:19.627909+00:00",
      "head": "b2f9fac08de386d2ea74fe3ba44ec163fb266c6160077c393ac06503c93a1cfd",
      "node": "201.wake",
      "snapshot_digest": "71e41c06587f44cae35ce33049c26c670b644a82f9ea6800ebdf599b25b7c5d3",
      "version": 28
    },
    "202.wake": {
      "generated": "2026-10-24T08:37:11.536003+00:00",
      "head": "8306aa9f36dc5e6796b95b406c70b0c558152dac745210c910742abf32994ba8",
      "node": "202.wake",
      "snapshot_digest": "fe518b4de4a18e1ac00bc89128cb42444e55f3337ca7e084502b638aff0f0c53",
      "version": 39
    },
    "203.wake": {
      "generated": "2026-10-24T08:34:27.599726+00:00",
      "head": "aa5e5a3bf7ca128593d394b2fe574e2a3cada2b9fe6db985df134b8197d4627d",
      "node": "203.wake",
      "snapshot_digest": "f71b0c293828d61b5a47dd4ac49f4073b1e544bff836ad93c64b1e838b5ccd9b",
      "version": 20
    },
    "300.wake": {
      "generated": "2026-10-24T08:40:52.193596+00:00",
      "head": "7d602d4174604c32354ae5e8e0a7eeaeadb52b44d620e8eabbdb5cd1b9edd581",
      "node": "300.wake",
      "snapshot_digest": "d6e14d5b1dc5201fb0e15bf95f402ec4c253dc6b54749f5687d02ffcb90e1e58",
      "version": 26
    },
    "301.wake": {
      "generated": "2026-10-24T08:50:21.909485+00:00",
      "head": "0165c3fc39ad5e990dbf4db1e602af6137ab2c3f860b5931d7f69e8903be46ec",
      "node": "301.wake",
      "snapshot_digest": "b3eb8888543e4d2894131fbb41cde213fbfe699c41443b4039ad574eb9f88f02",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-24T08:50:12.914139+00:00",
      "head": "a71ba96db6b9ad43928d20f9712924fda0209038729705239391975c3281f155",
      "node": "302.wake",
      "snapshot_digest": "2de4131c5f5fce3797484d552b07cb3b3a554e82132d2c9e3cdbde2262c5faca",
      "version": 22
    },
    "303.wake": {
      "generated": "2026-10-24T08:35:19.755702+00:00",
      "head": "38fdc752026b05beb2ff2ebeb72b9bd956f52a946c08c8d7b104bff779e64fac",
      "node": "303.wake",
      "snapshot_digest": "f6420a093871fa30cc5b835d53b81b31ac6359b6b96653e9b6b4157627b15ee8",
      "version": 38
    }
  },
  "version": 354,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d666466386365363331343038343430/66.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d30343230623061383736666434616465.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d636f6e74696e756974792d7261/74696f6e616c652d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
