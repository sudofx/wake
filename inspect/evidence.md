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
  "generated_at": "2026-10-26T23:57:00.137988+00:00",
  "head": "snapshot:ef5afceb231e4560125840bd07fa03ecbab2c6de76c15b90a0644e3bea4d28c2",
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
      "generated": "2026-10-26T23:42:32.671819+00:00",
      "head": "9f1ae8dff904b7ef960bd3fa3dda2b89a9036df166a56359535fbca2613bebab",
      "node": "102.wake",
      "snapshot_digest": "21c058652f631d302b5cf83eaf5011f716ad5872c3aaea1a8d7a6920bd14912d",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T23:57:00.137988+00:00",
      "head": "6a200be71c1fd4abfa3ab62194ff52231e2941b0882b33bca80b0ee2e6d81eb0",
      "node": "103.wake",
      "snapshot_digest": "152a8d7ea518ad4082b67d66e710da9a4687508d6aa47ced2f566953ad4aed56",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T23:45:20.408099+00:00",
      "head": "49f4fdbca4bc353b87f1acacb292db573a67538413fd3f440ed62c8eac36c47c",
      "node": "200.wake",
      "snapshot_digest": "7d82dd14cbc516fe92c53bade7e1cb274ffbc82d9b4f35a4a0b0a6fce2f150bb",
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
      "generated": "2026-10-26T23:46:22.828877+00:00",
      "head": "463e26754054e1027ea49b0bf81f808c91c7331af300271fdbd938d08dcd3bd4",
      "node": "202.wake",
      "snapshot_digest": "aa72ff2cf240c140df65a227e171d7e9d766676be2629458688668f3eb1ddca9",
      "version": 60
    },
    "203.wake": {
      "generated": "2026-10-26T23:36:28.141569+00:00",
      "head": "341ca7693a94e8385ef65efff53c90dd7fff5a56ef2e9911466543d6a836baa1",
      "node": "203.wake",
      "snapshot_digest": "37dc37c1fbbc83b8d7081a8215d9f467d172ac0d8639ea3c0c1569fea8f3845e",
      "version": 37
    },
    "300.wake": {
      "generated": "2026-10-26T23:47:30.218497+00:00",
      "head": "f213cbe7c97d9734ec33f2cc2d200b02ea51cedbdcb5c25ab0585a7510d0635b",
      "node": "300.wake",
      "snapshot_digest": "840b45872d3c7af7ad58bab2163fe793e3c3f70cb6467058ed04633753a1befa",
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
  "version": 587,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d35336162623137653234353534326363.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d663236306239373537666130346662/39.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
