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
  "generated_at": "2026-10-27T00:22:39.014994+00:00",
  "head": "snapshot:82e23bbf053e047c0df0ab70f1a33cd149496af9b39ce3ed87ecfd14ddf9322b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T00:22:32.739344+00:00",
      "head": "cfe9c010efa4c6320ae9eb46acd79990d3ef84df4bf334b3fe3d912e7e95c790",
      "node": "100.wake",
      "snapshot_digest": "6fb9bc1e129b9efbc77f5c6fce7a9cab35b4eaca008292b9b408a3c0c3084d4d",
      "version": 32
    },
    "101.wake": {
      "generated": "2026-10-27T00:22:32.944291+00:00",
      "head": "8a43340536208cffc4458b0592a86bb6289c66b50625cda794fb95c6949b24eb",
      "node": "101.wake",
      "snapshot_digest": "28d12da8d55654ef81471d31abcd743698a3ad221caf65d8fa6e250c606e555c",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-27T00:22:39.014994+00:00",
      "head": "ab35a356067a2e88e783edaf58fc76cf7a24abf92d453353bdd4dcb3125a5575",
      "node": "102.wake",
      "snapshot_digest": "35b504d9b59bb29f58038198f583be7eacec8642311cf84e0ddddaf576c8eacc",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-27T00:22:33.515986+00:00",
      "head": "d7d129930386e36226aa927ee03ef03f2d38eae5f0fc7b96121ca5b84c5afe1a",
      "node": "103.wake",
      "snapshot_digest": "cda572544349791fad26836306406000def2ecdef10b947cb0783bb7bafb734b",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-27T00:22:32.862438+00:00",
      "head": "a9bdf1a255656f9c00b0ca11ee66f4d136a706416de2c5de23b201a765c13517",
      "node": "200.wake",
      "snapshot_digest": "4492cfa405bdde61ec5f1355a7663bc5d129ab1dc2eea2b62feeb58be92022e4",
      "version": 46
    },
    "201.wake": {
      "generated": "2026-10-27T00:22:32.002532+00:00",
      "head": "a1b3876cca803c17dfabe98ba8802aa327ad9ca4b9b435741096160133ad13d6",
      "node": "201.wake",
      "snapshot_digest": "519c129fb823dc8103dfd72f0d74c8edbb9a27cc7ea001ddb3b86aff610bf839",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-27T00:22:35.748984+00:00",
      "head": "bef358a7e7d3a157490bce16e0c08abd0d26e36023926070b6d048a4445762fd",
      "node": "202.wake",
      "snapshot_digest": "b64ff5bffbb58bb70df2c3b8b98b63a6fd08c0dcebe8a4cc7d9807f4e3dceece",
      "version": 60
    },
    "203.wake": {
      "generated": "2026-10-27T00:22:32.575260+00:00",
      "head": "3ac54c3991c717d77ff1513446d4cafbb505ebe2fc6d222b9825e3437bd5d50f",
      "node": "203.wake",
      "snapshot_digest": "1b9a7f64a0c01748f9de8ee01231e3bc1e4d61832b6496b922827a110a724fc3",
      "version": 37
    },
    "300.wake": {
      "generated": "2026-10-27T00:22:34.311785+00:00",
      "head": "20068b95b7ebca97edd26104ac46f61d62018dd4bb58c4c9e4a225475a2e5309",
      "node": "300.wake",
      "snapshot_digest": "bf4586d9f957599aa482e12b5c4f68f1c05243fa2e8305e05470f0ada01b57c6",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-27T00:22:37.702358+00:00",
      "head": "2f4c54539240772f7b691847d3ea130ba0eede71fed788a22d1a726ba24cd082",
      "node": "301.wake",
      "snapshot_digest": "2e2efac43dd50e4e33685fb75c43f927c98caef4a286c6a0f86663db9931f080",
      "version": 67
    },
    "302.wake": {
      "generated": "2026-10-27T00:22:34.237442+00:00",
      "head": "6aeda209649e8bb3fffe891c36e41b38f75bcdf7a6717a2fb82073f45d796e86",
      "node": "302.wake",
      "snapshot_digest": "4c82ffd179fbb9f7f104cf91d8e75b6d49871c8fc292c3e0dbede8e1e6a50629",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-27T00:22:34.859317+00:00",
      "head": "abc31a3ac53a885d1a9f416ac06dabcded2f0d3044147361f54e67ec7d4e4914",
      "node": "303.wake",
      "snapshot_digest": "7d9b587bef32cd7ecccea41aca6f56e23560b149101e82c64e7821273ddead0c",
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
- [evidence record](../reader-records/evidence/3230332e77616b653a3a736f757263652d336239346434393761316533343263/61.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a736f757263652d393530643433376535393661343837/36.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
