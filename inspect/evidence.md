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
  "generated_at": "2026-10-30T15:32:23.179255+00:00",
  "head": "snapshot:1e5e26b96ef801fe7d33a6a9e3453ea1ecf806a9e8d55347472999087797a286",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T15:30:34.393654+00:00",
      "head": "490303923a8b04bfcfb6bf5b4cc588dfe54367fe3c996bd2f3bed55846332acd",
      "node": "100.wake",
      "snapshot_digest": "e602d94187ace01b8e6832b561859daf81010076c0ad5eb05aea48400758770e",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T15:00:53.528380+00:00",
      "head": "89cf73447b618864e13db80d5f9829afa4d6f52bcb04f0d180310d1d8b39dbcd",
      "node": "101.wake",
      "snapshot_digest": "253f67ccfa209f64f9a4c4e9725f02a7d484ead2253fdcee2610a87983c28cda",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T15:00:51.272704+00:00",
      "head": "520e219cea1e6086617026c6d5af8c853518d0f0d01edbc35855ac1cadf4271c",
      "node": "102.wake",
      "snapshot_digest": "d0b9871ecfd160e9a25a9572ae03c570c150ac80f799144deaba36797c2075f9",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T15:01:02.266917+00:00",
      "head": "e1d77366b6375b11e1902d8271be6e2ccf0ea7b92e9728e3c99b6905b34474ed",
      "node": "103.wake",
      "snapshot_digest": "1b5ca431d3f9e134a6bc5a63f63f4a496e21b9dc53288b2315d14f71ff20ca70",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T15:01:03.358767+00:00",
      "head": "0c528bf25a2f725db1e4a34c5d4cbae75a00139e6af7591bd6a5c5e17d242cdf",
      "node": "200.wake",
      "snapshot_digest": "cc889d76911c855956cc1b65135d3e3c23af80c29c76d4cf3c7c1fbc2ffa82b3",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T15:27:12.286192+00:00",
      "head": "93e8268bcc8ab1f698f1c05c70cca0841ab72e5bd98e9f038cb31289470ca41f",
      "node": "201.wake",
      "snapshot_digest": "cd4c62a18d99fafb68fa726f8da5ec0602550fe9930cd5e993e7572b22b9bd10",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T15:00:55.758276+00:00",
      "head": "1b5b27ab4ea93f2479ed1bc0e6ef4f675c940f7e36dfcecee6fb4b655854fd8e",
      "node": "202.wake",
      "snapshot_digest": "79db5b502d709156db1b271cca773b2690a20b1c8385935c20eb3cc96e43e679",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T15:00:54.042360+00:00",
      "head": "596f2c8dfc29e52b30b00f5bc47005fda1d8b92a2485d79dba108f1a044eeca4",
      "node": "203.wake",
      "snapshot_digest": "9976ac451970eed713293a46addb77aabf69a65b1119162ed5dd34156863d7c0",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T15:01:06.058858+00:00",
      "head": "5ec943f4e4874db22dd0f264fc19abde887d684351fcf29ccb9cf72f9ee5bec3",
      "node": "300.wake",
      "snapshot_digest": "8c4402f033b32736e5445879887e7044a043db8f1dfb4872e901feaaad5bfdf5",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T15:29:03.724264+00:00",
      "head": "417955f1bb1acc7e55eb4c41a732e0c760074f9ffe16440f6b3c882482cc0ed0",
      "node": "301.wake",
      "snapshot_digest": "1e87192815a4587e5a020fb01495cfb88cc74ba6b3a3bfa7e7bab31ed6c33d3d",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T15:32:23.179255+00:00",
      "head": "e6148ee70edf64d473189caa0aaded3c0fc6e21262590647bd6409582048883b",
      "node": "302.wake",
      "snapshot_digest": "7529c096932e18a60d54a41f3ce50fc5ebf7a42810abe57b7aba8c237ab3c603",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T15:00:57.323285+00:00",
      "head": "1144a106521ddf2356c619c88998ccb8b3e0a39b7ad681c48f8576e72ab2fa63",
      "node": "303.wake",
      "snapshot_digest": "0f82f5cc43485274e3f7151b0faaac783c228591efd8322a38e1c0b11b54d9f2",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d64626564643535373336393334306431.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32633731623464613166333534643936.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
