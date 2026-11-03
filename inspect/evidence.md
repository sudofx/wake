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
  "generated_at": "2026-11-03T21:54:19.312614+00:00",
  "head": "snapshot:c92f8397f9b2daac821359645e4b28f81d8f0af8db9665dc84c75eafdcfa3fd9",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-03T21:44:27.798651+00:00",
      "head": "fa4dd1c1c2b2c0e4bca1c60a02953a77d6f13fd00ad53212d7752257808a8b1f",
      "node": "100.wake",
      "snapshot_digest": "884a7ee271a6496d7b2a8ec5bb87efdef29016481143d913387a4e51d7face28",
      "version": 1
    },
    "101.wake": {
      "generated": "2026-11-03T21:47:25.299369+00:00",
      "head": "775f974fd1493e2fc67f7a96d4cb9f9a86317a7c9f229412129e36aa219e1b17",
      "node": "101.wake",
      "snapshot_digest": "d36c7fa6d5e2e55724cda3943d76ca8f2f557f3b629c186806b4eed8348f31b0",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-11-03T21:52:41.145990+00:00",
      "head": "c03bf9874564c98e579dcd11a34aa1af5d7c26ded66273f72b7d9241f4cbf7e0",
      "node": "102.wake",
      "snapshot_digest": "2842ca1b4ec25daab5303dc177045505442db4fbcc13709b8e173184c3f2b036",
      "version": 1
    },
    "103.wake": {
      "generated": "2026-11-03T21:50:54.410335+00:00",
      "head": "b60be619e1bd95a803c8970e201e09dc2cca0f8e5191e4fa34acfdf9d745c18f",
      "node": "103.wake",
      "snapshot_digest": "191dd9f49f1143a4ee81c2431b09a1b4a38ebe7be12320ff63f6d809e48c81e7",
      "version": 1
    },
    "200.wake": {
      "generated": "2026-11-03T21:28:27.486133+00:00",
      "head": "ec685712fd33c159f45dc0708da452ba3b5195904b337192505e2d482e0b29fd",
      "node": "200.wake",
      "snapshot_digest": "751c75b9a0c88c1544adf649cea037e808d644a2749bc6c82b3493c7b088f635",
      "version": 0
    },
    "201.wake": {
      "generated": "2026-11-03T21:54:19.312614+00:00",
      "head": "2ebe60b3acac382a16890298ff815513dfb03aaca91dc41239977f7f1c51c774",
      "node": "201.wake",
      "snapshot_digest": "00c27b653cfeeaed0ba80cca0db319c50e78187f67f0aec617fc06e4369d40fd",
      "version": 1
    },
    "202.wake": {
      "generated": "2026-11-03T21:21:32.694170+00:00",
      "head": "355e6f519fa44c072b72c0b363eb6ab9cdec1d84e868612dffc4136739ee4dca",
      "node": "202.wake",
      "snapshot_digest": "78d2343a28b5843f6fd9e4f6a2decb8540265479c87fa310db60c7b36dbf5b7a",
      "version": 1
    },
    "203.wake": {
      "generated": "2026-11-03T20:57:06.800173+00:00",
      "head": "22714f0a92f271296351760e713694a9003f68772b9682be839e1b9680347435",
      "node": "203.wake",
      "snapshot_digest": "caf60ca9f33f029598ee47467c3e5631bc99c13b56fe62373f24f1f7e9afcc8c",
      "version": 0
    },
    "300.wake": {
      "generated": "2026-11-03T21:35:19.546380+00:00",
      "head": "b123a7b78d80b33e0a3e6eda15ce1772aa8d10d0e2867d65e93dd2df8fad48d2",
      "node": "300.wake",
      "snapshot_digest": "b17056b55914824642d41ef8c30a406afc3fea7b4d85179c97d15093b78932e8",
      "version": 0
    },
    "301.wake": {
      "generated": "2026-11-03T21:37:05.045410+00:00",
      "head": "1d9882175a65446e416c592f32ab95305ea6ba2b95167f99bd144181beef9d71",
      "node": "301.wake",
      "snapshot_digest": "6a93badb712c83d956e1514f05aa4f358ce6c846f07632d9ccdfdd983cad1ab6",
      "version": 1
    },
    "302.wake": {
      "generated": "2026-11-03T20:57:06.691888+00:00",
      "head": "56b0ee6620d26e7628129b7e6e611e70a93d8c9bdd8666ab27af01e268f7c753",
      "node": "302.wake",
      "snapshot_digest": "581826e783b20899048280917accf4f0f141a1d1c06fba5c01ce5829170fa894",
      "version": 0
    },
    "303.wake": {
      "generated": "2026-11-03T21:38:51.549578+00:00",
      "head": "8b81bf07f971f709ee8fecf61006730ecbbee8e31c52e2be787bd7b71565a312",
      "node": "303.wake",
      "snapshot_digest": "badaacca16ee27b4fcc8b72ab8725e5ce0668645a2995dd62d63f5cb6f90fd52",
      "version": 1
    }
  },
  "version": 7,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d326364306465396233316561346361/31.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d633335393863316166336463343034/30.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e622d726561736f6e696e672d6c696d6974732d3030/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
