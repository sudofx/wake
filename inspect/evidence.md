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
  "generated_at": "2026-10-22T22:28:49.285120+00:00",
  "head": "snapshot:9c148d38afd7ce3afd7bf535d2fd61a8c2ebec498e01fb1e1ebcf33beba7e0d6",
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
      "generated": "2026-10-22T22:25:49.738331+00:00",
      "head": "437ce40386752a1a080d3feecb18215cf600d1a2f5245d0ac657d6e097e9c08e",
      "node": "200.wake",
      "snapshot_digest": "e31c713ebbe18d2ebbebea91756abe54806c795224954f84bd45263afaf84415",
      "version": 2
    },
    "201.wake": {
      "generated": "2026-10-22T22:23:19.579227+00:00",
      "head": "b33f0ab847f77967453512ca99fe9e640fca948c21009e944318c9ad66018fbc",
      "node": "201.wake",
      "snapshot_digest": "5f8cf95a2ce006e0720b5358bbea511d0c63240f4c41f0c60b16a04fcf8a055b",
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
      "generated": "2026-10-22T22:26:00.112085+00:00",
      "head": "641efb0cc8e9efac4771abf9515ec55a647aeada9012ce1a0b27b9b375b80f56",
      "node": "203.wake",
      "snapshot_digest": "05d7f0e44f31811534db664e02508bfcc6e61ae1adc08bd18fae9efd1d68891a",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-10-22T22:26:40.660741+00:00",
      "head": "a88630f5ed51e6a8bfc3a1d90fa878b975523ea3ada71af657eac46fbb08a187",
      "node": "300.wake",
      "snapshot_digest": "3efb3f17f49ae6131eccef0de55e065c3a5aa57aec9c28319215ef19e6ca6d15",
      "version": 1
    },
    "301.wake": {
      "generated": "2026-10-22T22:26:54.630938+00:00",
      "head": "5c79dbca596fb080f554f1c3655b017f71112e5caad8fce69ea65d380638180a",
      "node": "301.wake",
      "snapshot_digest": "8e22ee69a29bb7add133d9f159d795888f4106426a9296eee72798397ff47f72",
      "version": 2
    },
    "302.wake": {
      "generated": "2026-10-22T22:24:45.157571+00:00",
      "head": "7b52c705a6bc730b95b6dffa4c0facc85c284c45faabc7e4e1a7de197d116b16",
      "node": "302.wake",
      "snapshot_digest": "3058b4bc847789fb4917fb1285e8405032fc309c86f0bacc9d59774d2b981f62",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d643364306339393465613066343430/32.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35636237623964636463356334653634.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
