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
  "generated_at": "2026-10-28T11:42:48.548380+00:00",
  "head": "snapshot:f2b38f7e0be1dc4397a9cfc50ae89cdd71be50dc2f65b3bdc1d17b2e7914fe92",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T11:32:54.197140+00:00",
      "head": "938dc9ab1ae5288a51ec04a9ba2ef417426a7e0b4f51ed69e082b79266b1f47c",
      "node": "100.wake",
      "snapshot_digest": "a68dbedd190490c917c07d7a12841509fc13dab767f87e9af33881834403a15b",
      "version": 15
    },
    "101.wake": {
      "generated": "2026-10-28T11:42:48.548380+00:00",
      "head": "86349130c293ffba7892151fdd5de9406a508b5a89b2e615597abcafee71394b",
      "node": "101.wake",
      "snapshot_digest": "d065728389715194f97f6cc535c8fa5a9a55c64a1ff9aa2e5cd10582035bcb05",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-28T11:34:27.219640+00:00",
      "head": "e999999c01858b5385bd3c01d6d7c3dc048b15cb39694c924e95cf9ab70a02bc",
      "node": "102.wake",
      "snapshot_digest": "bfffff9bc13e52547fef7f3c030637fd63fbd66e0d1475b06b8f9d12b82f9ea1",
      "version": 11
    },
    "103.wake": {
      "generated": "2026-10-28T11:40:30.539805+00:00",
      "head": "0802d712db50478d7a7895180438a58d938dd39cebea2b5a250a2439783f3702",
      "node": "103.wake",
      "snapshot_digest": "8ee73b591ce7e03cdaadbf410d65a6eebe3d115a4aa2bbef54e243d25762c730",
      "version": 24
    },
    "200.wake": {
      "generated": "2026-10-28T11:31:08.939805+00:00",
      "head": "3305470adde9ca94c4e276e736282587f29b6cbf51a5cacab947fba1e93b084c",
      "node": "200.wake",
      "snapshot_digest": "42ba5132a9ca08ca17c1d72eb1cced5132f74f0ee41e7d0b7ae93fbf2e43c77a",
      "version": 20
    },
    "201.wake": {
      "generated": "2026-10-28T11:42:21.188663+00:00",
      "head": "4b3fb0dfffb06c60ac5096b04d52bf8f03931a39e6df09b819f8ab2ea2525a2a",
      "node": "201.wake",
      "snapshot_digest": "49439c30f8a4eac028be6596dd90fe6ffdf1aecbf9226ac41781888907b6b7df",
      "version": 17
    },
    "202.wake": {
      "generated": "2026-10-28T11:36:39.036487+00:00",
      "head": "b0b43ca2ef2ab5488e5f0ebaebcdfe7b36aa4ffd31e1c5ba09869caa9b4f5d6d",
      "node": "202.wake",
      "snapshot_digest": "50d4777efe21c4862b8c949d0a228c12e94a537ca070ac7e79a42d0e176e622b",
      "version": 20
    },
    "203.wake": {
      "generated": "2026-10-28T11:35:47.962084+00:00",
      "head": "ab5dd2cc856afff4c7b45cb82b9c662d9f4a4ad4a09c7bb67eed054d3b5fb366",
      "node": "203.wake",
      "snapshot_digest": "765d36dac36d22f1e6d64f921ff58746120c2785ca59c3c3710b71578b0b5800",
      "version": 22
    },
    "300.wake": {
      "generated": "2026-10-28T11:36:16.540735+00:00",
      "head": "7c722463f467e3f78b287178c027d019aade6980b1eaa14fc875d7ce70348a98",
      "node": "300.wake",
      "snapshot_digest": "b3691ffe5b26cac3178f165bf659970d15fd66fd56f1852033f13b090852f624",
      "version": 19
    },
    "301.wake": {
      "generated": "2026-10-28T11:27:16.844035+00:00",
      "head": "e51d8857cf13b2e0d63108efb8287b3dfaee03e0bd9e201c01fc9831e1360e57",
      "node": "301.wake",
      "snapshot_digest": "79b0f5e5f0ed6d2abd1291f40660309a30fbbe8586e529b6e53c39b861bd9af2",
      "version": 14
    },
    "302.wake": {
      "generated": "2026-10-28T11:38:47.039806+00:00",
      "head": "cc46e814eff4e7af8c86bc0662f9f2806a08e37daab844cb0f703377e5ce34b0",
      "node": "302.wake",
      "snapshot_digest": "fe3acdac131f35afc0ce1fc4ded72b01c16ac3e3dc67781b9d12459d67c7c9d4",
      "version": 15
    },
    "303.wake": {
      "generated": "2026-10-28T11:34:38.564633+00:00",
      "head": "79ab723406445ded0eef366f4764eb2ad0b775ad0f2e45d45a45de2bb4d1ed6e",
      "node": "303.wake",
      "snapshot_digest": "1394d0631ca04832542930b9b1f42db55e299a5b6ed76f9014c1a0fe90bbc3dd",
      "version": 19
    }
  },
  "version": 214,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d32366437646237636661396434653739.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d65623564633561363462303434333335.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d6175746f6e6f6d6f/75732d696e71756972792d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
