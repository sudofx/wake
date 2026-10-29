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
  "generated_at": "2026-10-29T03:25:36.686113+00:00",
  "head": "snapshot:18bdee0bef5d8e9b09c90d08bf9752a4a99291d047a013b006a82184d81f7b08",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T03:24:58.771133+00:00",
      "head": "d5f4a2159e1a8a0c7d39a780e516163c77b40b6116695d917e174d7390058f7c",
      "node": "100.wake",
      "snapshot_digest": "f2e4f52123c2dee2000396766556d382b940d15963beba894cfe8efb448be6b7",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T03:21:12.723578+00:00",
      "head": "f4c2629b38d387d7f318c7b1cd8fbe310ad974fa7b27010d3d1e05f13297b3cf",
      "node": "101.wake",
      "snapshot_digest": "90b2bacb5f36889aa14464fd482ceade474c84328464cdf44308df242a27bffc",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T03:21:35.783455+00:00",
      "head": "7e291e69f1847705db9f6de861b80754ba553bca170e879c41591d8259cdf6a2",
      "node": "102.wake",
      "snapshot_digest": "a485124900886f0eb201da00d0e4d1630dd54c894c33c72fcfd7f834e6bdfc90",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T03:24:47.016305+00:00",
      "head": "ab820c06643818183f32f7c7e08b9566f0b61e548be47a4d509f2a94fa9d9fdc",
      "node": "103.wake",
      "snapshot_digest": "cdade151af4eb9cf1b2c505d3f65bb8a18cff9af0388220c752d8b8956cfbe64",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T03:24:35.852846+00:00",
      "head": "a236bff49fbefd41af38fc314b048dac6bc0d857d40c8a694415f593be08cd4c",
      "node": "200.wake",
      "snapshot_digest": "a3f64a44cf329d3945a3f1cd77a22879d6586023e36f948719430151ee8519f7",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T03:24:54.351572+00:00",
      "head": "1aadc0ef4dac8ed7cfb95488b562d46b6bb3cac11b88c0e4b33134a6114ba3e4",
      "node": "201.wake",
      "snapshot_digest": "a8ed60558bf92556cbb426131bdbf78336f9300f2a22ed72f8da36dbefd4d4d4",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T03:22:00.572471+00:00",
      "head": "797ed165d1fbf0c76fc2d549b43e5b6cfc3edd61925954990c15a108be904024",
      "node": "202.wake",
      "snapshot_digest": "de014cb867e930175ad60fcd1b2a29de9d7df97ddd23c0a7c2695e968cb872f0",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T03:20:58.079506+00:00",
      "head": "32c8516c013799200ea0af888bcdf003cce9263785d9bac5c220a1ef499bef6a",
      "node": "203.wake",
      "snapshot_digest": "c1e09a09da0d3fd47e552ebc57bd17293803f64a390d89c3bf327e6a3443981c",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T03:21:42.701186+00:00",
      "head": "28fbce3ce7d9a1a1c231d8ba277f43be7e0de904b4ac3abd590f180c590807a3",
      "node": "300.wake",
      "snapshot_digest": "1dbf5103053ccd49382e0f15dee7a87d110fca41db9bec1a3e9e08c162af4ff3",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T03:25:36.686113+00:00",
      "head": "2140d937851326207a4c0223d3a36b07e77cd7f9d14ceb11e011f5257de96fcb",
      "node": "301.wake",
      "snapshot_digest": "5948a21105a8d4a31eab8f18d0ce5701109bf784a7603f4a5c3bffc07729c8a3",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T03:10:46.878938+00:00",
      "head": "b06f78168fb941c317be5f8350d3d27baa0d73fe51df4c8350d7d7fcdcaeb2ee",
      "node": "302.wake",
      "snapshot_digest": "3976a953ccbe47c5dbb61fe274971d8e1644637c8fb1bb6e644d8c1c2397708a",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T03:21:35.493465+00:00",
      "head": "ae90d233fe73ca7d1c17bb250b09692fc9f592094c297960689ca9f8495cf52c",
      "node": "303.wake",
      "snapshot_digest": "b2152178c2573e456b7b1369ada53505e5f362dc3e5586923e0765539f340594",
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
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d63613331366331343234666634363431.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d65333131323730303735323034653863.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
