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
  "generated_at": "2026-10-29T05:40:17.974480+00:00",
  "head": "snapshot:292591eeb5b23019630c45cf76d2b31b040d04cb20a6e38fd69b198c5423cd6c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T05:39:26.430975+00:00",
      "head": "e054167898129ffd62f75306ffbbec88a503afccc596f51884b337299aacc5c1",
      "node": "100.wake",
      "snapshot_digest": "01a30340e40dbbcf15c47c7f50dc76cd239c9f6a0f169b440cd902666501987e",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T05:37:35.917207+00:00",
      "head": "34cc88f53fe09386a6c93e64c2237809e4c67640595238708fd03fe1b9cb93b1",
      "node": "101.wake",
      "snapshot_digest": "69665ca7fad6c2eb02de51d20267e1d163433736575f97a075528bebc1e3ec73",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T05:37:51.592418+00:00",
      "head": "a93694c0004eb68186a602fb9c2a66799e3dbf1e4cabe5b3687583054e8f9aa6",
      "node": "102.wake",
      "snapshot_digest": "52a92365d30b21f489ba5493f20b10f31b475a5b1845ef9993a1bc07de67289f",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T05:40:17.974480+00:00",
      "head": "88245a1187816325d0797a282aeb99a7646118138331720137fef7a48d062a8c",
      "node": "103.wake",
      "snapshot_digest": "c514a6d25e4339db0edef64a339a28f187acf47d606ff5e7b1375a05c6e02caf",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T05:39:36.775097+00:00",
      "head": "552e7be889db320875355e71146e60b2b10f9b7106faf540b7b400bf656c10c7",
      "node": "200.wake",
      "snapshot_digest": "236b5c7eaa3579133dd1552ed9e2febbfb15c67dbf2d9b927043e2fadd690c09",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T05:30:26.347186+00:00",
      "head": "7e1a3c3680c423402c77d4c6ff2e3f32d98de5e9c97d3a73f398c2f179973e06",
      "node": "201.wake",
      "snapshot_digest": "a82120b6a8f251e6fb2d23c3dfc8c07da0b29a924020f5fbd97600437290d393",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T05:38:18.860452+00:00",
      "head": "5c137ac211819e6c0b22f5e62720098c1c9f54462096a28244fc8ca0331f2305",
      "node": "202.wake",
      "snapshot_digest": "2f12afde921496e346cba7b5aa6ba86ef5841f7629a77ad5a887b901c1f32b58",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T05:38:02.244465+00:00",
      "head": "32750937c9eb282702226ca4203e0b17752a50fe27da59299781af9837e8a304",
      "node": "203.wake",
      "snapshot_digest": "3b8f2fb388565f1cba5a6e1ba0d6e74ef3e2b8f488dffcfd222f9e97638ccc8b",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T05:37:54.675883+00:00",
      "head": "16a7b1e8d330805450b603537553272a4f8c65db9ef2424a7e498ed6fcdb1ce3",
      "node": "300.wake",
      "snapshot_digest": "e1c7cc4fb2374c0bf0ce3f652badf9d0f7326cb3b23f21f8c0137c1a693e50f7",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T05:30:15.324433+00:00",
      "head": "afc307f05be0063937a2fff32eeea314521fbf03c2f27b3e832538d4cae46e16",
      "node": "301.wake",
      "snapshot_digest": "2f0e2a89028cc0ed0d7ef2ff08f8038cea1fe8bc411aef9f90592759c392d53c",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T05:30:09.334221+00:00",
      "head": "dc4718c83ebb53d496dba111ca8f34fcba258afcece6af93ba918985f292d467",
      "node": "302.wake",
      "snapshot_digest": "ca5f156d96c6f21f7d998c705f0fb5337c6c55c1d462472f95ca41027952b263",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T05:37:55.562751+00:00",
      "head": "3202b167e5b3adb534891b2121e5c0b5b1698a8c3463a7a05fb254d4dd05369e",
      "node": "303.wake",
      "snapshot_digest": "fc74774f9e011d1f3ba41b7469d15c41a030ba116275774174f8fdbb149a6135",
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
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d33616462646433636233323234303038.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d36393232613133653966323734633731.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
