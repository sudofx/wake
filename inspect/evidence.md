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
  "generated_at": "2026-10-24T22:23:43.991768+00:00",
  "head": "snapshot:e796bb61bb731643f492cebdbfc5f7c39910664d05b10fbe3514da84aec6b229",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-24T22:01:29.215166+00:00",
      "head": "5f431faccb7513204e76e9dc48fbfebb8e077c0e4649101cbaa205af1835a628",
      "node": "100.wake",
      "snapshot_digest": "69edf0280de49b82107f56ddc0678dab68ca667b26d542fb5deaff6cda32892d",
      "version": 25
    },
    "101.wake": {
      "generated": "2026-10-24T22:01:55.587351+00:00",
      "head": "6b8f4a71fcee31d3017cc4e191bc8cfebdeaa5ed6fbb794d7ea4fbf8e9267bab",
      "node": "101.wake",
      "snapshot_digest": "d351ff045f2f41f23dcda651a12b13205a1597b3d520062267bb2ef9663d53f3",
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
      "generated": "2026-10-24T21:56:30.050698+00:00",
      "head": "a00c5b5bfdbddd1c910147698a036f7ac4afce9e35c12b65c1c5ab0b34aabff3",
      "node": "103.wake",
      "snapshot_digest": "da06ad8d5b48d29bb28e1d19e40050d1d7aaa9644ae90bc57e8ed2c08f18c3e6",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T22:00:51.190093+00:00",
      "head": "a3f99bf8f7b5d3f56287054d5677245ea26a74824fb76bfd6f947e462f7658ba",
      "node": "200.wake",
      "snapshot_digest": "8c897e9049d2a2fd9f6bfc782382c9c842ff0475511396ed90b353b9653a4f5e",
      "version": 32
    },
    "201.wake": {
      "generated": "2026-10-24T22:03:26.804468+00:00",
      "head": "dfb3ca1bbdca988650a3b702f003b67aa7b6c1485c634bbd4037a4681a3b5b2b",
      "node": "201.wake",
      "snapshot_digest": "220736d52b37bed9eaf216c1470c0992d52d36555c0a2e6c82a2de44c5f87471",
      "version": 37
    },
    "202.wake": {
      "generated": "2026-10-24T21:55:18.068655+00:00",
      "head": "8282f183c25fc0eddafe4faa30bbb8bc42befe72eba0a9f106956590b486ae27",
      "node": "202.wake",
      "snapshot_digest": "a71e61e48664631c9be26f027c44a86878e6e70d548185c4a1e04c16ff249144",
      "version": 50
    },
    "203.wake": {
      "generated": "2026-10-24T21:59:37.932189+00:00",
      "head": "6d6a2643f320fcbde2b517e065a61a4b6c236e161f15c50d189ef81d03bf00a8",
      "node": "203.wake",
      "snapshot_digest": "ce269cf0d481f2a3e57161a3e7903bb775ef1ef0b4c3f20f0cf16873e5132ccd",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-24T21:58:15.425943+00:00",
      "head": "380a9b65df5306d5da10053463443ee5f740c5552cb2ecc89fad147439c4aada",
      "node": "300.wake",
      "snapshot_digest": "32f7587487dce14dc69d51ceafaacb0f631474c9e4c9f74430a1c0f11d74186f",
      "version": 33
    },
    "301.wake": {
      "generated": "2026-10-24T21:53:10.214134+00:00",
      "head": "ce8dca965728f73d0b78d4fbf699e57f4a7906e496fa13afc92210c8d70c4f1d",
      "node": "301.wake",
      "snapshot_digest": "0b02b17870e3365e45c5da3a370edb4196865a42521557cada4e6858eb96fe5a",
      "version": 51
    },
    "302.wake": {
      "generated": "2026-10-24T22:23:43.991768+00:00",
      "head": "68bbeee6bd4f1328b3389202b298fe339bf5c3576d39034a54264fc202d28223",
      "node": "302.wake",
      "snapshot_digest": "765cddea2ef3bda7745560195cc567bdef92a7e79083df40d1950e7a668a407e",
      "version": 31
    },
    "303.wake": {
      "generated": "2026-10-24T22:02:09.131044+00:00",
      "head": "84d0f333cf5fae7240c77f883311f137f2a51033084733f101918d38c014334f",
      "node": "303.wake",
      "snapshot_digest": "c69ea4920fa432a30fff8e41f66e67376696eb447c69d7593e244dd29a8705bc",
      "version": 48
    }
  },
  "version": 464,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3133.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d65663462356337383630373034373764.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d376166356639616264333935343134/62.json)
- [notebooks record](../reader-records/notebooks/3130312e77616b653a3a6e6f7465626f6f6b2d6d657461636f676e6974697665/2d626c696e642d73706f7473.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
