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
  "generated_at": "2026-10-23T19:33:37.277050+00:00",
  "head": "snapshot:350d2fd1b9f5cae3980b2e17971f78be2ab1149ba73fe5ad6db8367f21bd4cd4",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T19:32:20.511699+00:00",
      "head": "ba902d3a84e64f88ab3b898514ae19fe073d5e35fa0a5f73ea9236373cb4e79a",
      "node": "100.wake",
      "snapshot_digest": "3a1266cfd2fbfad6d88eb2a0b3c0c1cd680f15d7cdcd14b9a3416de1c8c927ce",
      "version": 17
    },
    "101.wake": {
      "generated": "2026-10-23T19:04:04.729545+00:00",
      "head": "0183bb7ec62d1851c32138520ef8bb28ab6ce3495bd6bba8d53ceeadba2a049b",
      "node": "101.wake",
      "snapshot_digest": "eefa812f24a65c7fbdc0c77025a7a13d410a6606717b116ed6c9a5a24072e44e",
      "version": 30
    },
    "102.wake": {
      "generated": "2026-10-23T19:04:03.555718+00:00",
      "head": "42f886215a3dfddb21847199bee48a06aa353e4494561b9b1b7cd073d72f7c22",
      "node": "102.wake",
      "snapshot_digest": "434a04628c3180130df941fe7508bc8e039d696e7481b03a0ab568fe0609f550",
      "version": 34
    },
    "103.wake": {
      "generated": "2026-10-23T19:04:04.969035+00:00",
      "head": "200c075cd0c038ca184fa11cb457672087cbb4674171bc69a2ac0b549974b499",
      "node": "103.wake",
      "snapshot_digest": "933058820381bcca7f71ed07e3fc686d04a4def2ca250bf162699345516d1c8b",
      "version": 25
    },
    "200.wake": {
      "generated": "2026-10-23T19:33:37.277050+00:00",
      "head": "8810ce9b42375d45455755663403a7891dfb3e9d8ab7e604c8689f930a729b46",
      "node": "200.wake",
      "snapshot_digest": "37efaea282fe2a0d5282ccbd534c9ea5948ff5c0c017ca733060cbde08a620f0",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T19:04:04.598339+00:00",
      "head": "ceeb0a00fa2382d002571e938860fe3b2e8a40d1def727ad2946c3c1ef95827f",
      "node": "201.wake",
      "snapshot_digest": "72a2fb20f749f0fd5d664ff20da112143f254e0d2f2f5026b3da79fd50bb8b08",
      "version": 24
    },
    "202.wake": {
      "generated": "2026-10-23T19:04:04.831283+00:00",
      "head": "b2dacbf57eff18932b8a4c93be5162eb4720d02c091cd423e8a7b96f09e9d94e",
      "node": "202.wake",
      "snapshot_digest": "43e635b90fdb6a3a9fbd36cc0c2326ee1375b47487dad93bd8dd1c9794daf5c7",
      "version": 37
    },
    "203.wake": {
      "generated": "2026-10-23T19:33:27.509000+00:00",
      "head": "18066c5b5b33876531baebcb409e161d3932fde079f19d8e3e7d1ae4d2e4cf59",
      "node": "203.wake",
      "snapshot_digest": "cbf1b1078d8b05701d4cd97e9d02e974c3dab4cdc49167a938369865afaea7f7",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-23T19:04:05.018612+00:00",
      "head": "60ed37b7985582f43f9300838ceee7ee954166fbd1077b87723472d7ea3d5569",
      "node": "300.wake",
      "snapshot_digest": "dae2434672a0975e309642c44c5a40f46a2f7435f18405d94e05779ece6a07c2",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-23T19:33:00.728409+00:00",
      "head": "9ca11546c39390d68e96e0d4c8a62e5da9676a13bdabb4ef5fed9982cd13237b",
      "node": "301.wake",
      "snapshot_digest": "50ed375aaa5231b8b31bf200d42a18ae1923c40ce82f018e8a9a027e93e8b037",
      "version": 37
    },
    "302.wake": {
      "generated": "2026-10-23T19:32:53.315265+00:00",
      "head": "97b6e7f52dc8da44335d448e54dbbedfaf92c2f0a1163bfba350c2427cef5690",
      "node": "302.wake",
      "snapshot_digest": "066a17f5e095e5296b1037edd6b87875dab97165e88b0a574c68614f2bb24b69",
      "version": 17
    },
    "303.wake": {
      "generated": "2026-10-23T19:32:13.377356+00:00",
      "head": "a0173b0f62668ea17576836c5c8f1577c9811f95d5d17650a0d5bddd672cbe45",
      "node": "303.wake",
      "snapshot_digest": "d4a5864edb6fb37b959c6756a7781909e8be531b1e200861d93001ac32c7fbd6",
      "version": 34
    }
  },
  "version": 320,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d65373632316365363264316534643965.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d33623431393931623862646434663962.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
