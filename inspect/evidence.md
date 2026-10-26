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
  "generated_at": "2026-10-26T00:33:33.210821+00:00",
  "head": "snapshot:edee3d4e66b712966f6bacda42c383630ccb084dc79a0807a916974ce74ebb45",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T00:08:17.789307+00:00",
      "head": "f54a5aa0ab5f7b96f266f9c3453e464c7794952f23e672a258c0ebc0c046cded",
      "node": "100.wake",
      "snapshot_digest": "750c3a2624ccfaa822006b57a4280735aef0e06bd257fe6f784b88a601acafd2",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T00:29:16.719703+00:00",
      "head": "3db59bc58f708e114291d9d12795520c104c54e203f3254936a48ddc0ee64bcd",
      "node": "101.wake",
      "snapshot_digest": "326f4aea2f1d60d7b8a19be701ff48a5a78b44201949abaa0bd5bc9d03b8165c",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-26T00:08:57.051324+00:00",
      "head": "680922806b1b2484cf3394b622607d9de40f9e9874d7907e791f788c326e07a0",
      "node": "102.wake",
      "snapshot_digest": "461649617de7fd7a22c994b56474dfd856d5d4719ac43b8e450c7dadaf30073b",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-26T00:07:58.228578+00:00",
      "head": "51a4f5c4d9270932a7bfb2f42ddcf4eb2b9997029e81aea694a204ce6b617a31",
      "node": "103.wake",
      "snapshot_digest": "e39906726202dd6ba088e7526cc497ad8c902e407da2edf928480f8b8dd55695",
      "version": 40
    },
    "200.wake": {
      "generated": "2026-10-26T00:04:09.544923+00:00",
      "head": "ea1290013c20c1ac2b42cec8514941995aa0ab115d4935128930700029c19344",
      "node": "200.wake",
      "snapshot_digest": "74476256375ede73b6c1edebfb5675a019957968807e5ab62e18fd7e25e00e12",
      "version": 35
    },
    "201.wake": {
      "generated": "2026-10-26T00:04:25.388818+00:00",
      "head": "d5e5827a29114ada88dccc889a22e834134d5c3bb0419188e494f4f913fc7f9b",
      "node": "201.wake",
      "snapshot_digest": "6e7c37b0046ce1d159e8ccfc509070def631e941604c5b524f5eb908020fdd07",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-26T00:29:48.696919+00:00",
      "head": "59fb10341690a829d5ba5149dee20dfc8c31172c4cc87c9d6c3567c89b2e94f6",
      "node": "202.wake",
      "snapshot_digest": "2e4d240880f4cef1fa0f244ae0e76968411ca9b6ed54a7e7920b4fdbd7077e5f",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-26T00:04:41.386181+00:00",
      "head": "57dd5eb91e1f3edf1b463ccc4108f4d43c8734e98feec2ed742ff5a16fc2725c",
      "node": "203.wake",
      "snapshot_digest": "64c76fa51e8f639f975f1fdcbac8643ce7d613c78c0dc0c5f627c34232093eed",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T00:33:33.210821+00:00",
      "head": "4a98682dca9cda8f7a03c0d857d4d91ef2d6bca57958508af3cdab79d25f76a7",
      "node": "300.wake",
      "snapshot_digest": "d8699faaaa32ceaad07361bc1ea26db4845ef4a55dcc77523e99439bb7f3446e",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-26T00:00:43.445734+00:00",
      "head": "c97266c41bad72ad71ae23cf2f03b132a98235382472e6df3e9d3931c03b7afd",
      "node": "301.wake",
      "snapshot_digest": "9fb5bdbf10d50181a2bd488894f3b0a74640e2821d95a6a07e703b0aefd9f5b3",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-26T00:20:20.940615+00:00",
      "head": "ee09fd1678d293531304fc51512526322e7aacbbc89f1e511800ac509294e0cc",
      "node": "302.wake",
      "snapshot_digest": "b3092e679e8fac8a1955081a14ebc9ee10abc762e008d69f0cc5e494777cbf99",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-26T00:04:58.745864+00:00",
      "head": "78a24627b495c09a1745a8fb00e164485fb355a9d2e397352a9050d40544f3a2",
      "node": "303.wake",
      "snapshot_digest": "5edce54cb935d5cce00c0a87a887b3dedd6c615a4b2c723161b25c307fc38a97",
      "version": 51
    }
  },
  "version": 514,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d623033626435376231623638346330/37.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d666166306431353137376163346165/32.json)
- [notebooks record](../reader-records/notebooks/3230332e77616b653a3a6e6f7465626f6f6b2d726573702d666f726d6174696f/6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
