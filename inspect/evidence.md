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
  "generated_at": "2026-10-27T01:45:58.530249+00:00",
  "head": "snapshot:c5678a528286eb2ae0e408b7389554bf529624269a85c4d1e5aae74641825996",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T01:44:30.246939+00:00",
      "head": "000a4192c2c3ab85fe28a0693f7e3cba432b8149c44c735280a3a5d5727e4370",
      "node": "100.wake",
      "snapshot_digest": "546bb26612eac9c5e8c7e12cd167f1554dd83d804d413970da2417cb5be95d7b",
      "version": 32
    },
    "101.wake": {
      "generated": "2026-10-27T01:38:21.415059+00:00",
      "head": "0f7193638c66d36497697953430cf3a819d755b91f87f107522276a573051f62",
      "node": "101.wake",
      "snapshot_digest": "6f119e20107b6ce612adca896554e3bae59e505294bd1bcf3e9ff3d5e9556cb5",
      "version": 49
    },
    "102.wake": {
      "generated": "2026-10-27T01:45:34.873081+00:00",
      "head": "65ad9de5627c146a2362bfe3d49e97a82668062b3b7084ecd644dbd2fb793cb5",
      "node": "102.wake",
      "snapshot_digest": "2908f7ed8d964d991264d740a09efb3ce48309f34e9b69f7336a4834220398d0",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-27T01:43:20.505797+00:00",
      "head": "f262eac9f1eedb75e2a35720910dbce82b6730715a215ca388b1e8cad90712fe",
      "node": "103.wake",
      "snapshot_digest": "e0c40bf9a9be9d0d8a05400654d49a0d0f7c62509e0650cf343ef5e14d134de0",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-27T01:45:58.530249+00:00",
      "head": "e94689ac373ee9880ee00f8cd770c8cdc852036f2c231cb43f5b8127ed15f2e9",
      "node": "200.wake",
      "snapshot_digest": "fd143cc2b4df078efa8ffd6c72c514c9cf8bc98956e57d42cdc2fe6080bc1915",
      "version": 46
    },
    "201.wake": {
      "generated": "2026-10-27T01:39:24.512064+00:00",
      "head": "3537c20912aa8c860b0927418ed7f6df9d5309ee4b27a66adcd41a740c704a40",
      "node": "201.wake",
      "snapshot_digest": "7aab34b0ba959540ed119e7f72ab42ea8eff49af540b9e74c4d48ab7a80f48fa",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-27T01:36:02.198808+00:00",
      "head": "e4b713351649eb84bff37a4d3a83d337ce6e8c9577bc221892bba027f6272138",
      "node": "202.wake",
      "snapshot_digest": "993018567aacdfd7b991663c9fdc5a674118a2e5adc54501c937e480f2381d1a",
      "version": 61
    },
    "203.wake": {
      "generated": "2026-10-27T01:43:43.439494+00:00",
      "head": "d2b28bfbb7e36176948d3c57167e1f8e80f772865fb259ecfb75190dd40049d1",
      "node": "203.wake",
      "snapshot_digest": "6558657b0a8d4bfd90889654c2ce62373e2a3aac7bc37c6902c5cbd49be347f1",
      "version": 38
    },
    "300.wake": {
      "generated": "2026-10-27T01:32:21.836937+00:00",
      "head": "7ada414b625d25136fb6518d70ce124bba675ac3fa09815e398f6bd5d6d5c959",
      "node": "300.wake",
      "snapshot_digest": "53f65a15115048c203be8ff5b061c3d21f0c84b6705e2044e7d6f2eb785a927f",
      "version": 39
    },
    "301.wake": {
      "generated": "2026-10-27T01:45:10.060703+00:00",
      "head": "3bd678359f7ce0860166db89e8c151ce7bef681c108b09b5c6d74e7f4527bbce",
      "node": "301.wake",
      "snapshot_digest": "707af0d077e6bc75ba9aa088820f3d6fc86ccf74fd08f782dd278bd377a31722",
      "version": 68
    },
    "302.wake": {
      "generated": "2026-10-27T01:42:06.699020+00:00",
      "head": "ac44537baeaf35cb10ad1bf0aecf034fe3ab561aa5a6d16910f81541b7cb395a",
      "node": "302.wake",
      "snapshot_digest": "7b86bbc18996149140ab56ea59d8f68961f7b4e8404176542f8f96e34f31aeb9",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-27T01:41:28.687857+00:00",
      "head": "f1a90ed7d1b7e219ef71d6afac7e08b0024cfceeb0b051e846b40a9d1f504c5d",
      "node": "303.wake",
      "snapshot_digest": "af5ec4592d3dd9c4a1010fb5a0466098de1b3c0123cf5508c4be0c1ab050d41c",
      "version": 58
    }
  },
  "version": 593,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d37303664326533306263313534383330.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62383838303966353664326134373736.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
