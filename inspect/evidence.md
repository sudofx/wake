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
  "generated_at": "2026-11-03T22:25:30.708590+00:00",
  "head": "snapshot:5dda6716b9cdccc34d730eb149b556dca9fcc71d7c8cd3579ec048016a2e059a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-03T22:25:30.708590+00:00",
      "head": "cdbc98a637a38257a3aa7ba355e6964239e41a3e430249c0b56dc3e51a5061c4",
      "node": "100.wake",
      "snapshot_digest": "3dc89510c42447a0e8b4d10bd0421632ca337a9760ebe51b03f669736b3490a1",
      "version": 3
    },
    "101.wake": {
      "generated": "2026-11-03T21:47:25.299369+00:00",
      "head": "775f974fd1493e2fc67f7a96d4cb9f9a86317a7c9f229412129e36aa219e1b17",
      "node": "101.wake",
      "snapshot_digest": "d36c7fa6d5e2e55724cda3943d76ca8f2f557f3b629c186806b4eed8348f31b0",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-11-03T22:13:23.200399+00:00",
      "head": "53269ba78e76b38e3819ce593878652103d390a9028f325bee30377013a3e8b6",
      "node": "102.wake",
      "snapshot_digest": "f18775bf3c7e29f341f3f76198f085f0c2ffc80c5309c4d2243d2bcd2cbce205",
      "version": 2
    },
    "103.wake": {
      "generated": "2026-11-03T22:11:44.614659+00:00",
      "head": "6bc70c3c8e9dd1faacca0cbad08c7209eac93f14617401ad27ce218d6431b90e",
      "node": "103.wake",
      "snapshot_digest": "4eb0e9a13456c4563f417ddab7ce712c06ec0424f88d3cb9142e8df62bf86742",
      "version": 2
    },
    "200.wake": {
      "generated": "2026-11-03T22:10:01.926747+00:00",
      "head": "635258b800a0b4100b4cb55b4edab507beab1e3b4c1c41872a0444e45a64a004",
      "node": "200.wake",
      "snapshot_digest": "8f5ec221b6c2044d15a6a6897c892f6014477cd10c00b77090442a0a2a6dfd5c",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-11-03T22:15:10.497150+00:00",
      "head": "8fe0ede69adbaa248ca46f52296fedb7c27318ac9be5eb70f7afa21fbc94e63e",
      "node": "201.wake",
      "snapshot_digest": "291ec50589f09db67ada24282df1857b19e5039a5a0d2a5c46496001b9b7bf0d",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-11-03T22:23:48.550272+00:00",
      "head": "8c753e69c68d1d481caebdb8145ca8b254a6e50187300af6b436474e1670d183",
      "node": "202.wake",
      "snapshot_digest": "d46b6c4fc9f46e4ab9b21ca231d2fe3b93f810682b38a7839182e96a937d65b4",
      "version": 3
    },
    "203.wake": {
      "generated": "2026-11-03T22:06:27.033125+00:00",
      "head": "0c1e24f41a80b665e22a54d003ec1d2914bb070acd1d4f16c308d0fe9a2e1ebe",
      "node": "203.wake",
      "snapshot_digest": "b0db6036a0963603f64a2f68ed612c7f99d2affe9883b56b42726650b3e39d10",
      "version": 1
    },
    "300.wake": {
      "generated": "2026-11-03T22:16:54.734268+00:00",
      "head": "13fb9e801a00bef4687ce39e736ab489069b4d2b71e3c8bcc5da4ff56dd5b044",
      "node": "300.wake",
      "snapshot_digest": "3ce7cc0499d9adad1bd4d4a82648bc7b8060b895151bc96a2955f1f0e5ce7a5e",
      "version": 1
    },
    "301.wake": {
      "generated": "2026-11-03T21:37:05.045410+00:00",
      "head": "1d9882175a65446e416c592f32ab95305ea6ba2b95167f99bd144181beef9d71",
      "node": "301.wake",
      "snapshot_digest": "6a93badb712c83d956e1514f05aa4f358ce6c846f07632d9ccdfdd983cad1ab6",
      "version": 1
    },
    "302.wake": {
      "generated": "2026-11-03T22:01:16.171744+00:00",
      "head": "8ae4c4f7addd36a3041b862fb6ec48e082bb53b22734694211a0bdb186ae1c51",
      "node": "302.wake",
      "snapshot_digest": "5ae6d290b0d6e067307033e76e50e64eb3948447e3aef2b4113c771115ed8573",
      "version": 1
    },
    "303.wake": {
      "generated": "2026-11-03T22:20:51.048343+00:00",
      "head": "90e6f711a3acfc946fdb5a1e35e4de9f1e0df95aa81825bdb15cdd2743b5feaa",
      "node": "303.wake",
      "snapshot_digest": "b959d2ded715c6500106caf6157ac741613c5696639a8097431e483b700b85a8",
      "version": 2
    }
  },
  "version": 19,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d633465306462633838326639343932/30.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d34613264386166303237386534633533.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e622d70726f6a2d6d656d2d707265662d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
