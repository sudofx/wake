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
  "generated_at": "2026-10-29T11:45:21.986022+00:00",
  "head": "snapshot:2a357bd35fa8bc5c3dce4bcc35959624853d4496d50ff5e5b32627246c6f5eeb",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T11:43:17.292961+00:00",
      "head": "4babc40e44540e019211eebaedce4f97fc8534c2be5e3a1cbcdc32744d547ff4",
      "node": "100.wake",
      "snapshot_digest": "89a7a3f3fe7fdd73bce9803c825b8cfeec2c51e0a064c70441623e1d13c1e5f0",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T11:43:11.725858+00:00",
      "head": "c3da3ef61547654f256c1ddf5e0dea9672576f186f5bd141da9cfa0969ff39c6",
      "node": "101.wake",
      "snapshot_digest": "6cbac57b5dd9b947f25aee3600c0b7e6a4017078087ef7fe020b639773b090da",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T11:43:25.278410+00:00",
      "head": "ec9ef553c775ace9763bc503f47ca8c6649b164ccfb2be28adf7268cb856a0a7",
      "node": "102.wake",
      "snapshot_digest": "f3335d9ce6d6f29680c67c2ddd7c21d594bfa5e8ff9c05157c91e95e64e1a4b3",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T11:45:21.986022+00:00",
      "head": "b75ef1f371311a8b00be2a28d9573fa502032776dcad719f1aa019833df10c05",
      "node": "103.wake",
      "snapshot_digest": "bdedfae5184dd27a4999d22c10df48ca04979d2f0271b00b7897931fd29de21e",
      "version": 29
    },
    "200.wake": {
      "generated": "2026-10-29T11:43:36.066640+00:00",
      "head": "0d761900a444b63d87fb6c1b79ec9bf9d4eae72828b7bef5a1ba886d533392e2",
      "node": "200.wake",
      "snapshot_digest": "c6b78fd2f87cc78e176a55a47f87f1c1c918201e133caa74610fe5449406ccff",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-29T11:43:26.735892+00:00",
      "head": "bef89954c4e40cf393b1415c7a9bda3e4a19a9eeb8c437f8e479e9b9989092d1",
      "node": "201.wake",
      "snapshot_digest": "18e894763b9d3063f8cefdc1b295eccad4ac3d30bf9065548a43d0852f2cc951",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T11:43:16.676453+00:00",
      "head": "4894e0dbd0f25e4c5c5a6965d5e4ed7a000256fc94efa7656c52a231d6c5ce8f",
      "node": "202.wake",
      "snapshot_digest": "9a1db123bcdd44b2f41e520f80b75176b263ebd6b861157d4e577417dd3a3e55",
      "version": 31
    },
    "203.wake": {
      "generated": "2026-10-29T11:43:15.691134+00:00",
      "head": "9e22fed70b53941feff7a4d0bc37305737fe17256836a4f02bd7208821b8c665",
      "node": "203.wake",
      "snapshot_digest": "0d088b8e9821fa4cb1178081d26691d963373a0a5454b0d7b717b851c24bc41b",
      "version": 29
    },
    "300.wake": {
      "generated": "2026-10-29T11:43:32.819863+00:00",
      "head": "dfb663c6fde1019dd45e00159f8789a556f62036e21fec1e77799c5128ce58d0",
      "node": "300.wake",
      "snapshot_digest": "be88ac058b9049a52543ac80bb8d7179bb334347465bd0b11e855d97fd61e6dd",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T11:43:43.832055+00:00",
      "head": "3a32986a2b3cc56957fae94227c4fb03de43b5ca2652da682e301c98276ccd39",
      "node": "301.wake",
      "snapshot_digest": "26917ca8339392e4be25634cc3b0eb01acbe610eb53f7ca94f72e85fa0ef27d7",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T11:43:40.913180+00:00",
      "head": "54ede8eace915382971e023b752ec52074b3ba6501a63d19db7a37dd01e4c3c8",
      "node": "302.wake",
      "snapshot_digest": "05adc1f28dab935461ffaec81a62b357eb90a45570bddbdad089b94ffa6c445e",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T11:43:07.289630+00:00",
      "head": "ff735c6b8a789e9d1dc0b0537b5a7a896752bce7f9a6c78dc93cf17878d67824",
      "node": "303.wake",
      "snapshot_digest": "8c43e9d81da66d00d71caae241e43da803fc1f6c7c19a0732736e2a89635c8c7",
      "version": 24
    }
  },
  "version": 290,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d366364373131333933313162343534/33.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d62306463656438646637613434633962.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
