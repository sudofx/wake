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
  "generated_at": "2026-10-31T17:06:18.051425+00:00",
  "head": "snapshot:a513557454fd147310b2660e5fd1c113ca0b850955b96bcd0fc80ab135205c5b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T17:01:55.657161+00:00",
      "head": "22f2c07240b0210fbc2dd04c996c907a6380bfdf3eb34e17a58e7a868187d18a",
      "node": "100.wake",
      "snapshot_digest": "7ca6672e6e50d9412f1c3c0c3768a66aeed487a6b67da98e21ea949a8dc27d3d",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T16:35:20.978986+00:00",
      "head": "525a4f7aaa69cb0967229d2b8e6e290215d13d46bd3d109ec4dbc26c3fff6679",
      "node": "101.wake",
      "snapshot_digest": "b3cff5499c2a308c6f696ec2f9398a613c3cf4b2d535b59e81cce4beb2732759",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T16:35:34.070443+00:00",
      "head": "7eba3501e8f575161b0fa846adee67194b069cab548f70dc759a3eddab2ea903",
      "node": "102.wake",
      "snapshot_digest": "2a2cc174cf108ea1fe3e36c2cdcec4dacbfeb76a77393f98458fa837a656b2c0",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T16:35:41.742055+00:00",
      "head": "be0d63ed4b601c54d1900914585c545f65591defe61c8e555fdc41a55bfa08cc",
      "node": "103.wake",
      "snapshot_digest": "d709d301b41d60a2be2d122fde2f991c64dadb6ba9588836cdc9bfd145d45829",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T16:35:47.193028+00:00",
      "head": "036defa6f878fe43fbbf448c8b761e3199fbe16f13081fd374da18ecd9c3001d",
      "node": "200.wake",
      "snapshot_digest": "529de438692ec5711be6250e5c9d9e624012772ee7c4ee8ef8b416c1e5ce3a3c",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T17:03:44.292209+00:00",
      "head": "cb51121a9925d0e90058bf32b897c9f0e12541cf47950d6b5dc5b60b40250be9",
      "node": "201.wake",
      "snapshot_digest": "24e2d9a07b4d835bd03a5719492685312df5daf7cf148c1dd516d1481254d3a5",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T16:35:22.793719+00:00",
      "head": "7439ccf2b0ac6efdd18c3a75cbe988e3b93133eaf881337ad8063e0d0bb2c206",
      "node": "202.wake",
      "snapshot_digest": "64505cbb82d1ed3b73d5738d0ff8dae29899681b6b428538924742ba3173424d",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T16:35:38.081697+00:00",
      "head": "0b2966d24db56207919b8b2795e4ddbebc6c42adae414aa2b0666d646badda1e",
      "node": "203.wake",
      "snapshot_digest": "dde32e137eb2a3d5047081347c7a082e1798e925ecf9a0f71a712daada144e08",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T16:35:43.792816+00:00",
      "head": "2f2c43c6cbabfd591f6007acccb4d6f53d9cc8afc09ce67b416c23369200d67a",
      "node": "300.wake",
      "snapshot_digest": "cea5a29a95c99c3074d6824d31a01c477ac399e3d27d9c528cdfadac0ed77f5a",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T17:06:18.051425+00:00",
      "head": "b4545c8c197e304889916c3c9debd445035b2a3497718b14d3815b4db6d8b3d1",
      "node": "301.wake",
      "snapshot_digest": "cdb5f8e1256a7aabf18e331665ed9e09c273001b8a2087fce38b92b3c2aaac79",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T16:59:26.263292+00:00",
      "head": "f911c297f648d8b84c617859c6637ee45966a58a4058f781f5ebe21c14c733fa",
      "node": "302.wake",
      "snapshot_digest": "3c1925322a37b5d9f3667a6cd6efe66ebf0c65888200e4051f2a10eca9c6eafd",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T16:35:26.230682+00:00",
      "head": "598cb605bc53c862c69518aeff776d77d89e5d228eec80e98dac040c0a5c35dd",
      "node": "303.wake",
      "snapshot_digest": "e65094740b09dbd71c2d9ded6f5660354b0f150909c1456ace52b5a6c3998125",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d38386532653738646366636134303161.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31626538643737333534383334623136.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
