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
  "generated_at": "2026-10-24T22:56:34.816468+00:00",
  "head": "snapshot:cd7c9b852aecd7398caee63171afc722ff713d39187d72cea11b3a129bcd4ee1",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T22:43:09.494750+00:00",
      "head": "cb1da6fff58ae0d80ba422c4443566f21499e089f7fbd3d82ad501d07e5922c2",
      "node": "100.wake",
      "snapshot_digest": "bb14bfb8acab8e195db3e2b1f866159478fcc3ff0b5a3efeb70e8a41c401d673",
      "version": 25
    },
    "101.wake": {
      "generated": "2026-10-24T22:55:18.949751+00:00",
      "head": "f3eaa559a03132574051ef1b900e28e777daeadc11333205da357d2e177fde91",
      "node": "101.wake",
      "snapshot_digest": "0d432c9afe23111d70211464e5107dee2da1442c2d5bead69891ed333841bafe",
      "version": 40
    },
    "102.wake": {
      "generated": "2026-10-24T22:19:19.807026+00:00",
      "head": "6ac4e1b6cf03448412a367278cb3d6d3a24b84a451d492930f6794965e20a7a8",
      "node": "102.wake",
      "snapshot_digest": "a1bbf7aaf98f92cdea845e03e02f3b68614234e6fef5168340e7b7b649a71db4",
      "version": 53
    },
    "103.wake": {
      "generated": "2026-10-24T22:37:36.215509+00:00",
      "head": "b6bd07881022d641b59bd9f63d082ddfc4a907b66fb8ceb2654855cfb563e0dd",
      "node": "103.wake",
      "snapshot_digest": "c018c7585b7be4ff24e675f0758f446b04c0a7c4edffe374f0ae06809f3d21a1",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T22:42:31.673705+00:00",
      "head": "3a369baabeb8f69125d57073e97931bbd99d649dbd7696e15bb5118b57bc3f98",
      "node": "200.wake",
      "snapshot_digest": "474848fb921920bf635dc99b1a5e8c89b9c210ab9504375799e29d25179aaabd",
      "version": 33
    },
    "201.wake": {
      "generated": "2026-10-24T22:47:07.998284+00:00",
      "head": "cec32c5e10ade694418ee840b97a11376d55aa79bb551e840b67f5e471f4b025",
      "node": "201.wake",
      "snapshot_digest": "3d65a1b8848581000ffba5909e4cb29961ceea9135ddc2b2882fdd0149d818f1",
      "version": 37
    },
    "202.wake": {
      "generated": "2026-10-24T22:37:04.204163+00:00",
      "head": "4e102309a4ad6f615fd96e23d04e1d5d284a2d21a2645d1c7c34168213057552",
      "node": "202.wake",
      "snapshot_digest": "c7f902f1903d96a21655a59467eaaad0d4b76d20b9497c3c4e825b89cbbe0af7",
      "version": 51
    },
    "203.wake": {
      "generated": "2026-10-24T22:56:34.816468+00:00",
      "head": "8bf89a1780c1c1411053de5cc49bc5c418f2ca831d9751f3cd861c83fddbf528",
      "node": "203.wake",
      "snapshot_digest": "e701842501d6f6399a06f26d4823718e6ae98a84ee9c391f0d18bd9d5df446fc",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-24T22:39:37.098405+00:00",
      "head": "d081fc12b727578a3961bcdc7149ffeed4e18d9a29eb463454230c90f99f8d64",
      "node": "300.wake",
      "snapshot_digest": "09cc7d88609e541dc3e405cba26f7b2c013e58b9a8bb29fc46eb275bdc79bf15",
      "version": 33
    },
    "301.wake": {
      "generated": "2026-10-24T22:35:11.345346+00:00",
      "head": "9c82709493087dfdddf0e0c9fde139bbd0c3877c9291709f3a0af749d3cde6d9",
      "node": "301.wake",
      "snapshot_digest": "b0039c028a5f6117bab8c0536bcd754ad6dd327e206882d8c1ef0b94a54dde4c",
      "version": 52
    },
    "302.wake": {
      "generated": "2026-10-24T22:23:43.991768+00:00",
      "head": "68bbeee6bd4f1328b3389202b298fe339bf5c3576d39034a54264fc202d28223",
      "node": "302.wake",
      "snapshot_digest": "765cddea2ef3bda7745560195cc567bdef92a7e79083df40d1950e7a668a407e",
      "version": 31
    },
    "303.wake": {
      "generated": "2026-10-24T22:44:51.424019+00:00",
      "head": "df2c7d3f51b16dc267e43c3a7d48fc9ee86db5a9ef0cc274cdc4e406078a30bd",
      "node": "303.wake",
      "snapshot_digest": "90e9eb230e763ac6786a22ad6281828858ba61bbb78f4ef6f90b5ce271e48158",
      "version": 48
    }
  },
  "version": 467,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d61303531383639303836393434313432.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35366332313339373738326334313332.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d726573706f6e736962696c6974792d666f726d/6174696f6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
