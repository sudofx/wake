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
  "generated_at": "2026-10-26T23:40:06.143984+00:00",
  "head": "snapshot:c3566af4f1ec40c59e3c34c2719242f14a1069953815f64d8cc4b7e9b7855f31",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T23:33:55.675404+00:00",
      "head": "2c536cb314af4cf932e7b6ef11d57fdb8c041bb9b666b447e36511bfd159f1b7",
      "node": "100.wake",
      "snapshot_digest": "991de34fc84a2dc77c7a682e00cabc295775ec63fbdeeff54057bce4734aef19",
      "version": 32
    },
    "101.wake": {
      "generated": "2026-10-26T23:32:09.963990+00:00",
      "head": "a31a041db87015f3fe8dd000b6787e34e18f7cb41e3ba87d4d4edfa72c72a706",
      "node": "101.wake",
      "snapshot_digest": "8f3b17a7de16f42b04d9219123f3b6a34bf41cc0643a47d1624f260e1acddad9",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T22:49:34.923603+00:00",
      "head": "029473e8dc9c216ef3c358281438616e7d2a55e7b3d07e60c0f39c180e976876",
      "node": "102.wake",
      "snapshot_digest": "2459fd0b3b10fb118ee49cb3eaf34465dfad19da1419d30e1411509021aa6494",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T23:35:56.095487+00:00",
      "head": "99af9dfca027f181192e14dd107a61ae2f2e5cf19210823c8f20a93c9abd6404",
      "node": "103.wake",
      "snapshot_digest": "7a8ae37ba2adcc3485a8a4076101d7164d88707b1d39e6921ae711eb1dd82189",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T22:51:01.552706+00:00",
      "head": "355f25fcc0cf6ee377bc55ec15dcf18c2b67afdc84fcfda8c4b73a5bb753434a",
      "node": "200.wake",
      "snapshot_digest": "b0b0287464c64a63a4e69f6d4d161cc1a6b9c17ceb7082a0a32808a24566edc5",
      "version": 46
    },
    "201.wake": {
      "generated": "2026-10-26T23:37:52.937693+00:00",
      "head": "eff9162455686a477ba6347f32000a27700c9316e031a1b4f40210df2ce7acd7",
      "node": "201.wake",
      "snapshot_digest": "03c42066bf489413111f71104cf6f73040db33cee8cd161a52b1e5adfc823491",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-26T22:53:18.164749+00:00",
      "head": "abb9147e949f0636114fdbc0a9a843e0e95f3c5b2479de674abbb027ce0fb52d",
      "node": "202.wake",
      "snapshot_digest": "90d27803ede4f47d6c3fc08b7061c117ee6e22ee6f72de98e093305e0bd67181",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T23:36:28.141569+00:00",
      "head": "341ca7693a94e8385ef65efff53c90dd7fff5a56ef2e9911466543d6a836baa1",
      "node": "203.wake",
      "snapshot_digest": "37dc37c1fbbc83b8d7081a8215d9f467d172ac0d8639ea3c0c1569fea8f3845e",
      "version": 37
    },
    "300.wake": {
      "generated": "2026-10-26T22:54:17.008666+00:00",
      "head": "fe7ae2b5515b2255c6426cea1e5760b83d97e5cc4cf6753dddf080837ae0707a",
      "node": "300.wake",
      "snapshot_digest": "137e595b0f6ccff8cecd38c513a1a50f830bd24fde74553a7801e82214420b4e",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T23:40:06.143984+00:00",
      "head": "4a7a2d3ebbd90584e07c64397be3471fce5e306f14a8a32ff23268ec65867586",
      "node": "301.wake",
      "snapshot_digest": "4b6c9d2dc6615f64ba17eca40ed1b482739d264257d31c8b4888e330fdfec943",
      "version": 67
    },
    "302.wake": {
      "generated": "2026-10-26T23:32:26.557951+00:00",
      "head": "6aeda209649e8bb3fffe891c36e41b38f75bcdf7a6717a2fb82073f45d796e86",
      "node": "302.wake",
      "snapshot_digest": "6e9ef376d1e94137c95fcc2dea457d446622bf108b7a200dae89be0bcccbf2c2",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T23:39:02.970437+00:00",
      "head": "98878d98b27ab844201a25479dca34807f692c6c28caffd96e3366c8b23a9e4f",
      "node": "303.wake",
      "snapshot_digest": "3a54d794105daea0b033c2f8469c4931bca7334f47876ee6de3add1d43763596",
      "version": 57
    }
  },
  "version": 586,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d613064663039303536366666343837/33.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d646230323466376639636462343566/65.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
