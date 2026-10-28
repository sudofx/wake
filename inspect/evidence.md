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
  "generated_at": "2026-10-28T20:02:50.589925+00:00",
  "head": "snapshot:91b8fd8362c38db749576a6cc2a8bdbb6f6c5bb0a1a3d8b84e303d0b9ed48c09",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T20:01:27.009915+00:00",
      "head": "5230b0d3d90e0ce6120c7ecf874c6b548efd8788f4092736a79433be2a33e2a4",
      "node": "100.wake",
      "snapshot_digest": "a29a666027685c3c41e511ba71871febe6e939e4d5d8ac834361da055ecf2f92",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T20:00:56.914375+00:00",
      "head": "4aa3d5ccbeaea60a44bcb5944fce446290446a2f4071aa85e325d6888dd46a93",
      "node": "101.wake",
      "snapshot_digest": "9e607721d5231ec91f343044525134f9f19e08b61a2606f3b1cbb8b867f98b9d",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T20:01:38.410719+00:00",
      "head": "e0e92051e509c913df3b4edc93ac2b90f1e071ef983acf5ce1ec9b1f9e8afa79",
      "node": "102.wake",
      "snapshot_digest": "2969909e572234e7de8e11c9863af9462f9575ac6ac971ba7ee5fd6d000fb42e",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T20:01:25.243204+00:00",
      "head": "406ce3fe61906dfad4f6b1493d8005566abea59f2a1f6032b00214b5a1337aa8",
      "node": "103.wake",
      "snapshot_digest": "8392924f8ee6a199d1e5848c5df105d5797b592b96720bf6bcf800d527a1e4dc",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T20:01:48.088226+00:00",
      "head": "a2a586f7e6fdd958394166f701a5e36bb10e7972d83903045d01e56ce2cd859a",
      "node": "200.wake",
      "snapshot_digest": "8b0e4e4c9df40c85be26e3fe92f5bb10e92eb173156f4355549ced6d04b6fbe3",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T20:00:56.122673+00:00",
      "head": "ab82e8a0de3ff6bbbd0f7f6aac2eee548fd40b5ebd64486d9ff781e95634c986",
      "node": "201.wake",
      "snapshot_digest": "93d68c7e93e90c3aed5b36fc908d3ad6720d100d599a343d48b6c9079955f413",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T20:02:40.581687+00:00",
      "head": "155dce37e811052978a305ff4f2ac6756650a0058332b31a4f41c1c30de8525e",
      "node": "202.wake",
      "snapshot_digest": "64978c9b9361b45cafa94f2630f57d03496fd4ef4a96dc6cf32469000383eff3",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T20:01:35.787170+00:00",
      "head": "0677de94bac40051ead1fbb4d39b15915a233fe19e6798816c53560acf801c29",
      "node": "203.wake",
      "snapshot_digest": "7e39a572a9155effaea0c8c0dcc426113f99e83b802af1b395f3ac5cb1d21ea0",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T20:01:39.889429+00:00",
      "head": "c2349c48735a5377109876ed912a946320749fddb94230c18bedf3914d98a616",
      "node": "300.wake",
      "snapshot_digest": "92c0541afc8784aefb8c139af746c23b90fde647e389b257a1982e2e2c5b6338",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T20:02:50.589925+00:00",
      "head": "cd2c00783960a29bb36c7efa863b1bd5126f29dc65d4ced35a7acef1cb65a7f6",
      "node": "301.wake",
      "snapshot_digest": "5b97f733375cfb926ad2554320aee5affa9c587a96095a7aaccc7d5e0d65346d",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T20:01:14.294086+00:00",
      "head": "45a24df8c9a7c5b972354284011fd0936478942e881b2e3fdd5d20cd2a52ff7a",
      "node": "302.wake",
      "snapshot_digest": "730969ebc84e949eb13f1f747dfff93bc397f9805e5c1d29fac7b73d0ebba1dd",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T20:02:34.685925+00:00",
      "head": "2f5f538209cd3bda793d96f204840478063198b72e377d6bc670ed0fc519dcdc",
      "node": "303.wake",
      "snapshot_digest": "c7e1bcfce1277ffaaf2896853bbc6ace7923c5593c0557739608e59ecd74a618",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d39666436663235653137333534613562.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33376335303638646164353034653231.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
