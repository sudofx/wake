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
  "generated_at": "2026-10-25T03:44:24.969656+00:00",
  "head": "snapshot:0173bc960ba1177103dfa5f1373d9d21bbbc8fa8aadd862f68671dacd2146f04",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T03:44:20.876421+00:00",
      "head": "764f58976ef56289ae824981528cea2ba427bd1d2c15a7d8b140015ba6784b44",
      "node": "100.wake",
      "snapshot_digest": "fc000a3c11cffcff65fa24e4e7900d70fdcb9118435914d2033e2fea00a3464d",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T03:44:22.969411+00:00",
      "head": "7b4538e1c42a8b4cd761ae0b015c400fb12e7ac482b7a04512bd393c8076b8ca",
      "node": "101.wake",
      "snapshot_digest": "d2588e98608bac8f6c973ff99632acf2bdf0e1bd1d1bfe90869410338ab932bf",
      "version": 42
    },
    "102.wake": {
      "generated": "2026-10-25T03:44:17.130056+00:00",
      "head": "30641ee79699abac8c4a72925605d2c3a65fef08709875e79c71ae5293de411a",
      "node": "102.wake",
      "snapshot_digest": "31bfee354ca1e805e0b4ed2fca45f8469706919b17e93b959b3e814af57ad3ff",
      "version": 55
    },
    "103.wake": {
      "generated": "2026-10-25T03:44:23.619256+00:00",
      "head": "9bd7d4ef524ee1a03b871b252954e81ed7306e25925992a0c84e2eea747bb3c7",
      "node": "103.wake",
      "snapshot_digest": "93f75dc74aa92a816857a90433ac27221a9980d6060921d90b70e42e17c62b2f",
      "version": 38
    },
    "200.wake": {
      "generated": "2026-10-25T03:44:19.991347+00:00",
      "head": "8905447bede1e537933ed4bde7034ccc219867b8d423a38e9edd54732e24f5cf",
      "node": "200.wake",
      "snapshot_digest": "f34957c8ec5371a0d45720256feb8edadb8340f4bd6974ddd8f983e31cd00b3a",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T03:44:22.951784+00:00",
      "head": "9dce08aeae268ea6d77a333ee8614d0eb7777e807c64cef5b4de225c33c3692a",
      "node": "201.wake",
      "snapshot_digest": "957bef50a28dab76fde5758b64fd6116fa4e8a7d5422f7dde7a4b193f7bf8802",
      "version": 39
    },
    "202.wake": {
      "generated": "2026-10-25T03:44:23.409569+00:00",
      "head": "3f86935fa3d170aaa2504e3eacc472879668915a533e7c7f2c7825c7ee2d7236",
      "node": "202.wake",
      "snapshot_digest": "8f14b5a0759f3551d84c572e517bae6820e7757c12a69dbb24e3a2e405c564d9",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T03:44:22.148564+00:00",
      "head": "4547fae095f496c8fdb305e78ea8a83a97a3ef5131a2bf0231a6f30725a388e8",
      "node": "203.wake",
      "snapshot_digest": "d8f98f9ccade8081264a1ebd3fb0abad76b9261f4e1678b5c4f5ce717102a184",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T03:44:23.243297+00:00",
      "head": "37dcb529891fd9419b6668cf745aef04ba78d25c11505e63f3b004ed2940b78e",
      "node": "300.wake",
      "snapshot_digest": "43151f6f17c39f36da041021ea8f3e61eb2611f74f322a462a8adf368703c58e",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T03:44:16.823313+00:00",
      "head": "fc8659f276bf0a340ffd20b904e49f73b2e39bc41f6464b7cd1207d38e23e85d",
      "node": "301.wake",
      "snapshot_digest": "4474e5718457cd0092b340326e6bc556975831e4011040936756cca757090eb0",
      "version": 55
    },
    "302.wake": {
      "generated": "2026-10-25T03:44:22.764486+00:00",
      "head": "eb317cdd5785fe5dbf3ff16d7c9ac09e2581641769d29135e9a455c04d1090ee",
      "node": "302.wake",
      "snapshot_digest": "d82f3b6ca5f6578eece27ec508962e71e9bda171ea8f910deeb3e70dc7615213",
      "version": 35
    },
    "303.wake": {
      "generated": "2026-10-25T03:44:24.969656+00:00",
      "head": "4d8ab31a170d2eca465ce01edfb83bdb252d11beba6fc213cf051dcef28da65c",
      "node": "303.wake",
      "snapshot_digest": "208e94a9681c94fb58aa03c1ffc64e1c6584e529fe66b419e7869a7728be9ac8",
      "version": 50
    }
  },
  "version": 494,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d34653237373833623930356434373333.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d33373237356237353735386534333634.json)
- [notebooks record](../reader-records/notebooks/3230312e77616b653a3a6e622d6d656d2d6964656e746974792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
