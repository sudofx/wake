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
  "generated_at": "2026-10-23T07:28:00.258609+00:00",
  "head": "snapshot:6e16936c4544264272b5ce249579292e3a04f87fe0b8097c8fd3d336c2a86ab5",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T07:21:49.357393+00:00",
      "head": "8c6e3f5adf2a224cc3ffe20fc672f3c7ce387a23dbad35611629d69a2e5a7edc",
      "node": "100.wake",
      "snapshot_digest": "f34e1007ed784358464835df320b9bbe6ac916e2b69ee09058fffd6076b083a3",
      "version": 6
    },
    "101.wake": {
      "generated": "2026-10-23T07:27:39.873776+00:00",
      "head": "af8acdd405e051da0697048f2aab3d32a082b6239caf6c439147fdaf0696d00b",
      "node": "101.wake",
      "snapshot_digest": "a42f18ead31827274e243396a437cafb65a9734991771bcabde437c909d7b477",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T07:23:40.685786+00:00",
      "head": "adb08295c6b6a0f72f54e2a41ad75208e2e23b6115d2bb10947385f6856296a0",
      "node": "102.wake",
      "snapshot_digest": "05c46d597f6c9a8e06c9d002e67b57d0890c040bf548270b068b444a7bf8ad18",
      "version": 16
    },
    "103.wake": {
      "generated": "2026-10-23T07:26:55.111231+00:00",
      "head": "892222e0a4412f4bb851fd4beec4898e5e6d4688aefa1f85412bfa6e601ea53c",
      "node": "103.wake",
      "snapshot_digest": "b8679f894fe696e789b28a4af2a63e3f06c481b98ed385383e2e70a4fc6b35fa",
      "version": 11
    },
    "200.wake": {
      "generated": "2026-10-23T07:28:00.258609+00:00",
      "head": "20d2b224546ae32309df7d9e83d53f2a927a5bdcf7ac3d7512e1cf537377d9a0",
      "node": "200.wake",
      "snapshot_digest": "884e72469d59d6abea91c9fb4431023d62832dc7a553d120f8792a9ebb0af0b2",
      "version": 10
    },
    "201.wake": {
      "generated": "2026-10-23T07:27:44.339775+00:00",
      "head": "5e4719d1f761db8eec6a28d087da8a8ce50eeb0d2e288a4f8db6c7fc75f8879b",
      "node": "201.wake",
      "snapshot_digest": "df7d71c024e0cd6b04615685583cb64738ebcc1b7993a72344c17defe8900d55",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T07:26:59.745932+00:00",
      "head": "fc1f1111b9026d3e42475c051d15986a9f9a3638105aebe936977cda90dd18f8",
      "node": "202.wake",
      "snapshot_digest": "dfae0e467bed839ec7e3fdc1680c23dbac055da3d4410887c843281e6b2c47b3",
      "version": 16
    },
    "203.wake": {
      "generated": "2026-10-23T07:27:09.992600+00:00",
      "head": "5a4e968d26a33156f28d4986b2a8fd70d0a4bc12345575055e14f20f2771e812",
      "node": "203.wake",
      "snapshot_digest": "060381b7a0a611ce3ff529394a452a20b3e04d7c1b8558c3eeccf784d28dec88",
      "version": 8
    },
    "300.wake": {
      "generated": "2026-10-23T07:25:28.054469+00:00",
      "head": "910a468e589e572622c9d71541bf23a9aea2385a07564aac03e2099f4280e1ac",
      "node": "300.wake",
      "snapshot_digest": "ff5efceaf57ffdee1c08da7fcf16a1178b75515e772aefeea9c55b7811d25f73",
      "version": 7
    },
    "301.wake": {
      "generated": "2026-10-23T07:27:48.964070+00:00",
      "head": "8748d99483f2902502b37ee59e8d19280824ea3d298236b11840e87f47746885",
      "node": "301.wake",
      "snapshot_digest": "cdf5924b4f69bc16b764766d33cd82804f52cfffda59ce03a2c11709d9ab08e7",
      "version": 12
    },
    "302.wake": {
      "generated": "2026-10-23T07:26:01.674750+00:00",
      "head": "69c1fd65ef0a0beb71ebdbb7bc0429530abe69a3c67897e7e2d087aade002272",
      "node": "302.wake",
      "snapshot_digest": "3c26db528f343067edf0acaadbe01fc68a9451a9da49a8f38d1ee721d3a9967a",
      "version": 9
    },
    "303.wake": {
      "generated": "2026-10-23T07:24:33.273944+00:00",
      "head": "18b7225971ec8dc8335ca52c6ccfd1fca7eb19490f534a0babdf6d3464c16062",
      "node": "303.wake",
      "snapshot_digest": "b37a22e34c257960306d0f33881ac942854168a2e78c237b84f66afbbbc20bcb",
      "version": 21
    }
  },
  "version": 146,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d613462353137373439393237343932/33.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d663832643934353539366137346665/32.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
