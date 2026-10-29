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
  "generated_at": "2026-10-29T11:15:46.823926+00:00",
  "head": "snapshot:b25e1ef08c252ca3691d5ffd14809a74c2b1db1316b6121d55b959198f650159",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T11:02:38.608932+00:00",
      "head": "dbff916e33c6954f2a34ba8cf28b9ff92a5473f5feecb04d02d5f0b3da1000da",
      "node": "100.wake",
      "snapshot_digest": "03f64ccb1c1858d0c188168e16ba6f8f1420d8b94a767e8570d96c8406c60b75",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T10:52:02.376116+00:00",
      "head": "037b82307ea1967e546df7d253a23dada8ea8c8e66b874df434f9333a3e48d0b",
      "node": "101.wake",
      "snapshot_digest": "20a0bb35a1558183ce1049062d1b6beeed6961b1eef6e3a0121217bae342b325",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T10:50:18.492674+00:00",
      "head": "65d11af6d4f6d3b31db9b8fc7154cac1e1bb2d7bcdec094fc5ae366f45f399ae",
      "node": "102.wake",
      "snapshot_digest": "0bb0f759e3c0f75e5e609f57edd29f99c9338b36971c5d8c93d71f6d4ab0c37d",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T10:59:05.669264+00:00",
      "head": "843382fa4d6f07b5f06c95527aa384be0369e1bda56cc841b1198a960e59b374",
      "node": "103.wake",
      "snapshot_digest": "66fd2c58f0aaa11374e82a777e4e2a443070459d5e8954209be091d244ba6ed8",
      "version": 29
    },
    "200.wake": {
      "generated": "2026-10-29T11:00:57.763616+00:00",
      "head": "5956f9e116fe917392208955d7fb87f17fccbdba448153d9aade515370437bc6",
      "node": "200.wake",
      "snapshot_digest": "25f8b5c9139537a2229a3d954c285b4a9a7930e622a7c4548da279388b47303f",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-29T11:04:16.247445+00:00",
      "head": "a60c6568da3d02576408960e260e5038b01161149faf154101fa28e02cc653fc",
      "node": "201.wake",
      "snapshot_digest": "677934f3d9e817cf8e6fdea4fff808578dffe3dd822b0b8501b7c18734ecec7c",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T11:15:46.823926+00:00",
      "head": "3e08aa0ea95839d11dab0a2f91ef2dfa6f7dfef1398a7c6b0600e52bf67cf080",
      "node": "202.wake",
      "snapshot_digest": "4483fe94ca7fdb0fe822ae3e861dae05c681f1d11d8c0d5e784f8b77556a6665",
      "version": 31
    },
    "203.wake": {
      "generated": "2026-10-29T10:57:27.808645+00:00",
      "head": "ee301c35066fcda880e8b6b0d25a4292d2e1e2ed026147cfbaf5be63b9a4ff91",
      "node": "203.wake",
      "snapshot_digest": "56aa84b47e9936555fe1ae506c3045450978fc1d277e25357b128bded86f3e3a",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-29T10:48:47.041707+00:00",
      "head": "b72b4a3f0ab969e8d7b9ae8b661ff40d7b64eb225d16e37ae2fe22543e97145a",
      "node": "300.wake",
      "snapshot_digest": "7e63d120d2dfc5f6650131de530bd277732b6723aa463e237f3056bf7b363137",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T11:05:58.921940+00:00",
      "head": "1f78cf2fd71d6cfd3e97f6c23ea02461c6cfcb33d0e462c98674f6d2997198f4",
      "node": "301.wake",
      "snapshot_digest": "20d3a0e9a4f5f8362a89c613a941f27ba3c2215a2deba7f0540ce65de2102033",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T11:07:39.380158+00:00",
      "head": "9add38c8297e94a7248807c0cee251af43f48124979276b83f129cbc6c8f1e82",
      "node": "302.wake",
      "snapshot_digest": "79a1b98524937bc06689634e2e6364ccb0f6ecd9e4151ae5ec62d0e680b75def",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T10:53:46.544772+00:00",
      "head": "2ec75e864aec01b43401dac4467029e8d0d1ceb9754502ca87ac3cba5db19bce",
      "node": "303.wake",
      "snapshot_digest": "805e6c8f77a019f98f704fa09cd63aa083570f88c5e54b8a5c8b554a5519b6fa",
      "version": 24
    }
  },
  "version": 289,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d623466313437356364363131343139/31.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d636663346438656137323031346436/61.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
