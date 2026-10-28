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
  "generated_at": "2026-10-28T04:56:07.347062+00:00",
  "head": "snapshot:e01572c08afd2433b70b882e368a46c66f73796a38c30a26dca0327396182914",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T04:55:46.183910+00:00",
      "head": "c3bd6689aa4e8880801a43b0939f9533b8647b5b11a7fe4505e1c09d00ab543c",
      "node": "100.wake",
      "snapshot_digest": "fa964d8ae142603a00c02a0290bdc1f9bca85792e0e58d1bd952833c6d6a3ce9",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T04:55:34.914748+00:00",
      "head": "536853280a02a019853298971403b1d794acb93a10bd726e9542025ecd76918f",
      "node": "101.wake",
      "snapshot_digest": "3efe198c0894d74ed6f2b71981fb74ed496c3dedaab6096736d1ef2bc5b14e4d",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T04:55:43.912677+00:00",
      "head": "1c27d2c39a0f72b52b51f6cc8e602602afab1db25d00302296b421f3b3154aa9",
      "node": "102.wake",
      "snapshot_digest": "2a7e211abc9f0b019612b0c3f10171f3b939d56a098a94436fe5aa12de7ae103",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T04:55:56.969291+00:00",
      "head": "234e6639d7c18682cdfda27e6791232ac05022264f7ad94495ca1d29dbf834d5",
      "node": "103.wake",
      "snapshot_digest": "562c62422cbafed65db403c8de004bc114b3d1ecabfcece2dfdddd7f6f14f4cc",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T04:55:58.417349+00:00",
      "head": "02d8534b23ad094bc24f97f9ef0e64e85034bb3a8f5fed06323edd561170cc86",
      "node": "200.wake",
      "snapshot_digest": "5c2379f25530647d4322ecf610b9948eccb6fdf834b9973ad38ce6295dfddfbf",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T04:56:07.347062+00:00",
      "head": "ea5cfa10b45a63b7771047c69ead23dfcd8269cd4330c1bef9d2e434a4af2c2d",
      "node": "201.wake",
      "snapshot_digest": "410bb2973a5354f23bc833c6903fac7eeccb6a0cfd41814cb61bca9074077f5c",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T04:55:45.461018+00:00",
      "head": "c483fc8d0cbdd1887c9dc750728c78b86fce9b9eed2ca8388418b1f6cbb823dd",
      "node": "202.wake",
      "snapshot_digest": "96edca61db1a17f5c37ba0e7b9ec12580c75c06ffee3ac46711749699c4aca08",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T04:55:40.880940+00:00",
      "head": "56028f80d51d580122999a8fae6250466bea45eaa13343a59f554dfe549ae4c2",
      "node": "203.wake",
      "snapshot_digest": "f133d827c4c2909c57c846db9d685f24ee8ca0c3af76d6c0239144b80c12ce85",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T04:55:48.098461+00:00",
      "head": "a22a90f3515ac9c8c672a5e190473e5b7bc84ead9757c8a48f1f69d45b7bece4",
      "node": "300.wake",
      "snapshot_digest": "da6b4fa45d7b8ba933f5b76c3dd98ae548399f5415aa50a4767c490f4e4b7de5",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T04:55:44.481149+00:00",
      "head": "ad44825c3645845890c60efafda39863c7e34ab98babdaac075592518a052fd1",
      "node": "301.wake",
      "snapshot_digest": "7ec1bcfe6f4579df49d3617a1b9b6a9222034931e290d8bfbc67067c15e4cfd3",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T04:55:40.092072+00:00",
      "head": "b8f49fdd850adeea99e6cfaf4639112771b7653696cdf4005d4e6d944d19040d",
      "node": "302.wake",
      "snapshot_digest": "8310a9d6bcc5b072fc6ad0300d164d4ba940cf8e00e0ab127fa1601657270eab",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T04:55:44.893343+00:00",
      "head": "955e2ba340a49ba07ec2638e8412e6acbe98ea9bf5aad2796c1ed0e20c49045f",
      "node": "303.wake",
      "snapshot_digest": "9bc685d96f55fca9cdca2c5de328dfd661fed1b33a7f496a1f0bd09b756faaa0",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d38613435376233353037353134613035.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d65353366343663363463333234333833.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
