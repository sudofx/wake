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
  "generated_at": "2026-10-28T01:13:58.155470+00:00",
  "head": "snapshot:72e36e7e7361219138a06b18bd880ef97d636e6882d36d3af1fc2f5e291ef5f6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T01:13:32.270149+00:00",
      "head": "faedae85e5a98cd725663aec6e8d77350b50ef8e04f14b85f5763b8096bef76a",
      "node": "100.wake",
      "snapshot_digest": "1df62334a1543f10c4f023062e3c46c7e7f93320f23e65f73fbc3add2cedb489",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T01:13:54.449592+00:00",
      "head": "02f8f6a05873e693dd70f7ffe14fd0ec9aa43b749b9c12e1000f275d1749136f",
      "node": "101.wake",
      "snapshot_digest": "7d4f3270c14b25b627fcdd1c5caf060574135f14c3340d5ccaa519d8dc0246c7",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T01:13:23.049609+00:00",
      "head": "bd9c8295e75ff76231dc06919c867ce5bd10fc060924d0210954ee91d18b501a",
      "node": "102.wake",
      "snapshot_digest": "20b007dcff9d2c254511021b9f5c91b1f87e6564d0df4b337b9fe9801a985c38",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T01:13:35.954513+00:00",
      "head": "b816033c834e097e41b81496a6a8763f0edae70e3fb1cc80c2e96866051802d9",
      "node": "103.wake",
      "snapshot_digest": "4f6e4504f5bc7bae01456d3ed1ab01003f5c40257feb71ef0a2d6389db430929",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T01:13:41.878851+00:00",
      "head": "5c5e6cf2562d1f88e1aee7515f53aff9079c84d8f1c24610ed9b725591c9ed4c",
      "node": "200.wake",
      "snapshot_digest": "7dfec9975af614cdec6806427ad72829ac6fb99d6efa48c1da17dc2836cb154e",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T01:13:40.131334+00:00",
      "head": "ce8961e0a8269a9f7ee92a7bbe4456e14becb1788f70fcff32a3ba89496d977c",
      "node": "201.wake",
      "snapshot_digest": "7a5ca13789a9fb00a465ae9426dd51f46057872bdf8203851388d15ba347ac72",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T01:13:54.510067+00:00",
      "head": "f09572f849eb168893227d141ad49c0312c7f5624dfedc006a10e4f99d81bb92",
      "node": "202.wake",
      "snapshot_digest": "ba3761595ee8c408110c02f12a7a71867f78b5ba10bde9d02034ddca87f9a202",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T01:13:56.027858+00:00",
      "head": "029fc611950a68dada2a2bad81865f005618b7e724ef925865e42cef9a4bb09a",
      "node": "203.wake",
      "snapshot_digest": "ffa8fbeb2c976fa178b72fa71a408152bf7fb150dc1094899b02169a9c792e88",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T01:13:26.857077+00:00",
      "head": "3d9e49cd702c17ba68334e47947b961cc791d08d4e235b0fdc10ffd7bb5750ad",
      "node": "300.wake",
      "snapshot_digest": "83bfb9572c1117f60b082db3a71df0a00b53150134a91e94b7998e255c380c12",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T01:13:58.155470+00:00",
      "head": "8248cb3bf2246fbaf48979f2ccf3648af69c47fe93df067c979e000010df6c32",
      "node": "301.wake",
      "snapshot_digest": "2cb7b87220c9d4cda623a0d14f198a1ae8a3a66cf1cc113508c7dd5058ad5227",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T01:13:54.319321+00:00",
      "head": "070851dc3daba546f8018c61eff979bcc988e52ff2b59b3b5f0748df66fba93e",
      "node": "302.wake",
      "snapshot_digest": "277b760521c12caff4c0b152903cc030a185d8505bc6d3869508f42918fe8d76",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T01:13:24.027354+00:00",
      "head": "3584cadd016e8cd667387411587855d7af250d90ea0002446e1695f461ac8e5b",
      "node": "303.wake",
      "snapshot_digest": "26e025fc07f7287213aaad75bc2926d41d3e70df0d0eeb35e1e4d310de85b0cc",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d39303931393161383861643434323033.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d32393263653837383533363434633139.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
