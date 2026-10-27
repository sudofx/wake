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
  "generated_at": "2026-10-27T22:37:09.243586+00:00",
  "head": "snapshot:66ebf1e99dc7e429d199ca2d4d07df3177d48193c3a46b12a66ca13addba1f0c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T22:36:51.752473+00:00",
      "head": "c2fe46877209d7d849d2095f590cbf252be3eba05c4897f0946f1f64f7fec65a",
      "node": "100.wake",
      "snapshot_digest": "e9ae0eef3800d9724bbec8f4127d0b5b77ee5afb31eb435300c640176d6df9de",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T22:36:49.645596+00:00",
      "head": "aafea877f5d75101a1a5debecf1f378bfacd8d4ffc3c17c120f0c993062052a5",
      "node": "101.wake",
      "snapshot_digest": "663a6a3024dcc461b183a1da6b0af5b770aeb830e7f1843705eea34d3892b04a",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T22:36:48.101147+00:00",
      "head": "cdf09c4ab7ef04ea43de4e1ca0c6a471e05bef21d99c865eac3996a7e1afb729",
      "node": "102.wake",
      "snapshot_digest": "b461b80d1ab3046a9ae5133d50a9f9bb8092378df34936055a351808f3e83296",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T22:37:05.216144+00:00",
      "head": "636b2a57f58a069d098a05568ca09d33e3c52991fc973cab85e8d7680674a649",
      "node": "103.wake",
      "snapshot_digest": "dd4baabd660802d7581d77c80ea9e872997e1f2031c19cbdaa8e46160bec08b4",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T22:37:06.570034+00:00",
      "head": "52f66a46d07a47ade61abfedeba51b0c6d6624989277622b2d5c4c580bc099d1",
      "node": "200.wake",
      "snapshot_digest": "66d2fe3a34777dd49f593b088aebe992cd485c83a50e8d6f2f150da822a8f706",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T22:37:09.243586+00:00",
      "head": "8f9eaa91200375104a8d29db445747f7ed55f8f02d5e3d0a4c7b8dcd9c36b24e",
      "node": "201.wake",
      "snapshot_digest": "e57b0724362c9612edaebd390e031de7e345298ff6f27dadc7668a31e8e2cb08",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T22:36:47.445843+00:00",
      "head": "8102c66b1fe12135e125e4d621f25664a0fb8fecbb48183b6ddbc60bb8046084",
      "node": "202.wake",
      "snapshot_digest": "2c8797bdabc861e9771cedbb87e89a01f2ed2e6dd2f5138052763f6c8b8f1f44",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T22:36:42.303629+00:00",
      "head": "df3d00d9e53eaf7a1a4b2e0cf1ae3f8805772395bafaa25beef211da2c855c19",
      "node": "203.wake",
      "snapshot_digest": "347f4679f76fe30fa58904b117f87d323eb11afb6fc6c96db45bf8fe2b011896",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T22:36:46.496157+00:00",
      "head": "ab9b63bba94b6c810019c314b37fc4b9404005d970cc8c7da6cd57abb148bc0d",
      "node": "300.wake",
      "snapshot_digest": "40a0014c12611eaf41dab4e2e64a0d4b761175431945e2123bb8609ae1b07953",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T22:36:42.404744+00:00",
      "head": "d21ad41ef8b5a66a49731c186d80d53a359b5ce6aea1239ea80f9fea83538bd5",
      "node": "301.wake",
      "snapshot_digest": "7240e74a46132f9cd7e10dd2dffdb5e1d3baa380be1af38a3b23768f3c14608a",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T22:36:41.308434+00:00",
      "head": "05b9bfc3e016a2d3c265ba2dde209ed06cad93e564286fef5d1b219c4bb7c47f",
      "node": "302.wake",
      "snapshot_digest": "0b8e5c4567bfa5c98fa702dca77f9abdbb8e92426d525909f486e8745de59a36",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T22:36:52.503432+00:00",
      "head": "3d6d3490da4d2a38feafdfa62627a6a70ef565eff1e9846dcdf7b298b26ef4e2",
      "node": "303.wake",
      "snapshot_digest": "37775221f860473e891dd0194520e071a9213cfade4ee6b21f830321fce7c873",
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
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d35363139343331636137663034383235.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d64663938376134633832386234653630.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
