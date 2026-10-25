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
  "generated_at": "2026-10-25T11:20:23.283287+00:00",
  "head": "snapshot:3c1fc1e56b9d04a2c469e97cf0bcb953ff13c58b85bfd2024181fca47b4ed5ec",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T11:14:57.351789+00:00",
      "head": "3caa66a3c5dc3412f23af0c5c1efdc06a16e6183f74985683321fce89a5c1405",
      "node": "100.wake",
      "snapshot_digest": "cd2ea8cab25e73530f4fd5d58d2134fb7d65181127e9624e3b08f9b4f327c8a3",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T11:18:19.024107+00:00",
      "head": "43f7d945f3ecb988dcfbea69c13c162458f09c2a0a519caaca1eef80b3165e62",
      "node": "101.wake",
      "snapshot_digest": "0d1fd3c107601d3f26a1626f242d829be4f8aea3da0fb215042867e5252e856c",
      "version": 43
    },
    "102.wake": {
      "generated": "2026-10-25T11:11:59.093382+00:00",
      "head": "45e735ce7881ec29f9b9a549519b7885eca7ca64561c4b2327d4c449f45e5c16",
      "node": "102.wake",
      "snapshot_digest": "e633c94d611f76517040e363b052c239ca3e5d06c2e1b07a0372165d9fb79342",
      "version": 56
    },
    "103.wake": {
      "generated": "2026-10-25T11:20:23.283287+00:00",
      "head": "cf5b47c94b2edcd5aecdbbe170beb0834c4597f86743bcba489aa6842778a1be",
      "node": "103.wake",
      "snapshot_digest": "07ad4a752e14a97da8b9ce765bedb8900127f9d827711c8fe9ce7a1f452c8677",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T11:18:32.067183+00:00",
      "head": "20b2a1a5ba1d2bbd25df4387e8c044bcb56c9d864322916b8b2abd70ec9c821b",
      "node": "200.wake",
      "snapshot_digest": "08ccfc56b2fb620e7e045a57ea4bb4ef9ac889b20a87729ab9b217827876e61c",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T11:18:46.101795+00:00",
      "head": "38a137aa44beac0d6a395b87fef3ff97b9956a4e1c74690e4740a1c3bdfa7769",
      "node": "201.wake",
      "snapshot_digest": "75b7309f70218a38bfa6b2ad2b6d7a22f283e1cf6c92b769494f53d645a280c5",
      "version": 39
    },
    "202.wake": {
      "generated": "2026-10-25T11:17:55.753057+00:00",
      "head": "6b99b5f80fb18c214c094c41346bfd03f29ced833754c75fd0322b7a482e6965",
      "node": "202.wake",
      "snapshot_digest": "10dbefcb92ed7ee8614e9663bb3cec20a4e2d57d20f94252d151c25e5416c89d",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T11:14:32.447081+00:00",
      "head": "81dede7e6bb33901da2b88b90cbed8b8cb05e54faf9684e1c3224c714901f688",
      "node": "203.wake",
      "snapshot_digest": "62526cb797305a97e151a488f3efacd2f6caf417abec07d0bc9537cba79a7111",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T11:16:01.635051+00:00",
      "head": "3b7d53f692e49707af0d203303e595d55d45f13448402fa1991daa8cc4d223f9",
      "node": "300.wake",
      "snapshot_digest": "c260512a34f64bb646f11313d0f063750f8976a2fe3dba9f556c488d27fdce14",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T11:12:44.818079+00:00",
      "head": "fdd427331724b3788d077aaef310336137eb8edfb335c107dc924f281cb7b43f",
      "node": "301.wake",
      "snapshot_digest": "a224d3e030a3a67628c170da0cc4fcbc4901c729c134a16b7780cdf8aa8f14d1",
      "version": 56
    },
    "302.wake": {
      "generated": "2026-10-25T11:17:31.398813+00:00",
      "head": "8922d07d9bfa3ed73e46c14f498b1d9ae31d0f1a678457b6688af39cdc3ca1ab",
      "node": "302.wake",
      "snapshot_digest": "a20f59359127d3cc9565e769b2c5fb715f46c681a05feed01ad0bd0825d50eb8",
      "version": 37
    },
    "303.wake": {
      "generated": "2026-10-25T11:19:59.648867+00:00",
      "head": "4cabd279a3d42d9c12e49ea29b73260331f2debb334f8f95f23680024146d405",
      "node": "303.wake",
      "snapshot_digest": "e4895eb32800b6ab7803e3ef75fbed60d1f30b66143c78ba7bd006481186e092",
      "version": 50
    }
  },
  "version": 500,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d31363331373661383333633934333536.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d30306131373666316238643834353363.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d637269/74697175652d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
