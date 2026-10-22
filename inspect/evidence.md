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
  "generated_at": "2026-10-22T21:57:59.007256+00:00",
  "head": "snapshot:2d46cea1b7f7f2ae49d2cf425215fb2541e814d791bf88c4b5e49aaffd07833f",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T21:57:54.176531+00:00",
      "head": "ea937026a5cd320e2dffdeaed66f2d474835a9a23cb1dc39a3d321116c728eef",
      "node": "100.wake",
      "snapshot_digest": "ab20d072aeef5fe105048a80d6eac5f4f54d79e7ca12bcf5dd22930cdb145a1a",
      "version": 1
    },
    "101.wake": {
      "generated": "2026-10-22T21:54:48.531042+00:00",
      "head": "fd4a9fd26c568ddb19b4f2449cea7ce18de0905be2a854178c2df7cac0824ca9",
      "node": "101.wake",
      "snapshot_digest": "e776b63b5877794a80b882b81a359cbf97bc317ba89296f4c59ee45e0839e4e5",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-10-22T21:54:51.305916+00:00",
      "head": "491102c628dcdeeeaa2bf63d28b81225e510777e04a70bff405ccaf87688ac08",
      "node": "102.wake",
      "snapshot_digest": "c433dff003cb638f40e93f7bedca383b1dcce8d2aff13bfdeaba15b84a505326",
      "version": 1
    },
    "103.wake": {
      "generated": "2026-10-22T21:57:43.601134+00:00",
      "head": "e0f12f0eca96212fb07d9979486042e15bc6cd7650b6c39daed2b7b95af70096",
      "node": "103.wake",
      "snapshot_digest": "f528ce9f674eebf4cff34a63799426432f06a542f5ced95017f89bec6cf29eab",
      "version": 1
    },
    "200.wake": {
      "generated": "2026-10-22T21:57:35.983536+00:00",
      "head": "f8b874f21a3c62dea0509a268c0d6dda04fcc975790bc72322803fdce8ea559d",
      "node": "200.wake",
      "snapshot_digest": "bcb26130eea8e894ee4db69e5e6a4f0544db5e0557ba3b6f2f27b574a3c57dd2",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-10-22T21:56:29.534932+00:00",
      "head": "5c922f73bc06831e5f630eab08441376fc9afb657ca959a08e866450ca6fdc54",
      "node": "201.wake",
      "snapshot_digest": "0761a70cab8a9c92273179f9a6a1ffc8d0d35ccbadc5ae6f537252e425677f8e",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-10-22T21:54:39.188667+00:00",
      "head": "67eb9640dc1507fe5d3e32e7c940ca1f4b70cf4773af644cbac6d7b0a70047da",
      "node": "202.wake",
      "snapshot_digest": "7782796b2b6d8b53c9636a772c17ebe1f042a07d97ad94ce17717caf56b17f9a",
      "version": 4
    },
    "203.wake": {
      "generated": "2026-10-22T21:57:28.820928+00:00",
      "head": "f7b3dd6d59844f4bb2cc4dd9dbefdad57d103e97c7ae12ef72e69fb93a26bd84",
      "node": "203.wake",
      "snapshot_digest": "5c9ca8b0f3c4e6cbea89d6727c001b78c155c0efcacab6f29c3a802d5da76402",
      "version": 2
    },
    "300.wake": {
      "generated": "2026-10-22T21:57:46.088856+00:00",
      "head": "cc1534170589212e56f2c48aa3d075a2f3a8109a5c1af0c720fa98786d7d4ea3",
      "node": "300.wake",
      "snapshot_digest": "699e250e58075682242a0ff8508af0eeafad0e2f2bdd9e896456b55f4e1670c7",
      "version": 1
    },
    "301.wake": {
      "generated": "2026-10-22T21:57:59.007256+00:00",
      "head": "d159ce52e110a38e75348f59754686b693d1950cc211fb1bde46188ee402dde5",
      "node": "301.wake",
      "snapshot_digest": "f15d252dded35f2d6be662d1e615f0c77064ed2ba0448ed904a2e49ccdeb375d",
      "version": 1
    },
    "302.wake": {
      "generated": "2026-10-22T21:56:56.547466+00:00",
      "head": "bfbc32b1b5e3253f2a330140257aa26edaf5290102250ae32df07c07b14d5338",
      "node": "302.wake",
      "snapshot_digest": "18784a38bdaaa6630b8a9a73d26f80de814fce2182a27bc92de7319888295cae",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-10-22T21:57:33.621182+00:00",
      "head": "9f0a21cf8ef9ab55f07ea490517ca8e7f9e4013523e9c6603f8bbeb5c34e79c2",
      "node": "303.wake",
      "snapshot_digest": "c53ab2eb56d83f941e7979e7bab2731e95157fa212334b55651fa4e636f5ccf9",
      "version": 1
    }
  },
  "version": 19,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d363738356232386232643933346166/30.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d373533316136366233386231346261/61.json)
- [notebooks record](../reader-records/notebooks/3230332e77616b653a3a6e6f7465626f6f6b2d656d657267656e742d70726566/732d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
