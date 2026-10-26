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
  "generated_at": "2026-10-26T14:06:01.842218+00:00",
  "head": "snapshot:2b907eeba5634249b3b106e6952ff7ac3376bcd58be31761cd4e4e55b30b565f",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T13:45:29.415795+00:00",
      "head": "287f1d37bb3da3e36bf95c0a6cb9a665f3738ff198a9f56aaaf7e9efc10968a0",
      "node": "100.wake",
      "snapshot_digest": "19cc1c8ff4bb6aa175e5b6a8f15ebd3f0e4dcdb57b150d92dbff9cf3b3ef6c34",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T13:54:35.797173+00:00",
      "head": "eeee350fad5052ac32e30962479416491e3a7cbec66e27218894eb611e9bbeb4",
      "node": "101.wake",
      "snapshot_digest": "02f1f4672f4fde2dd4083518ebc2ab48b0f1b6173279d2564a6fa9cb63e316e7",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T14:06:01.842218+00:00",
      "head": "0acc88d87a3a9d775a64b9d407ecfb8ac537c209f0cae722d7271e9b58a132ae",
      "node": "102.wake",
      "snapshot_digest": "27a67a474453a1aff389bdc8c17c10aeb21265e2dffbdd8e93d0a4f621a24f8b",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T13:57:26.397158+00:00",
      "head": "09db7d2c2eded33e7a337843af1d81dfe8db98bd6de674a1289b348715ca75d1",
      "node": "103.wake",
      "snapshot_digest": "cbadefc000ba61f6a465366b613402b95d6dac1f42981aa8e8ae9bf21a053ba3",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T13:30:54.654958+00:00",
      "head": "494c1ecd9a8c600c44380b4bd9aaa443336707dd32312c1cc7f06a9edc7840e4",
      "node": "200.wake",
      "snapshot_digest": "92f9955993b41ee994869ca52087b33f30cb67d6be6a7e61a6070d1fadf3d656",
      "version": 42
    },
    "201.wake": {
      "generated": "2026-10-26T13:46:03.311096+00:00",
      "head": "f4e8efd013c3e78b87d290b4ab21c2b7ebaeffc081ddc62a90abbcee10c900f5",
      "node": "201.wake",
      "snapshot_digest": "80a894a9f818bcacb43e813c5b093026eecaa8d29a9b6443093d6766939973f6",
      "version": 44
    },
    "202.wake": {
      "generated": "2026-10-26T13:52:27.958054+00:00",
      "head": "8937f8367b300065a109fa8231a88a0ca75ec6910ed65259d5ce68b78f3d236d",
      "node": "202.wake",
      "snapshot_digest": "23d8cf234c47362b9c8c7609bca59d5c4976908d10ec93de85627a6668927077",
      "version": 58
    },
    "203.wake": {
      "generated": "2026-10-26T13:59:41.760749+00:00",
      "head": "f8cba280e9e25e3ce97764e2100a8617325bd74ec790875176083f9cb40a6906",
      "node": "203.wake",
      "snapshot_digest": "2731d30bb21591b159d4d7d1cb854f3129fcfa2d8bdcb27e541fb5a4b50d66b7",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T13:52:10.961489+00:00",
      "head": "64de6b323086ea7372a48e35ae60983be7aee8eb6052fa71d3fd35098dcf025c",
      "node": "300.wake",
      "snapshot_digest": "e2d81176a68ed5dc35d740021aa0a605d6df1ff95a1394e991faad4a63a240c8",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T14:00:49.249939+00:00",
      "head": "9a73912f700e9ba228a2f461f3a2f7d0ef5d12bcd0b2554b64647037aa4553b7",
      "node": "301.wake",
      "snapshot_digest": "8100f104b62139e017b590658e61c3193982b25f96bd9da21370758de2187d37",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T13:54:54.842065+00:00",
      "head": "871b1da4f33714edf6d6c5a55fa1df33bbc02318999a48f8df6c97a0d4d92615",
      "node": "302.wake",
      "snapshot_digest": "15860a182aa3a260b9f43db25251be65d08819a27c9932c86417e58aabf26d98",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T13:48:34.469851+00:00",
      "head": "7f16729202367e59c9170ac47b89a9075fb1e252dd8915ad1f3d212ba6960472",
      "node": "303.wake",
      "snapshot_digest": "ea879ef357f1aface775ac23a4ec4f2c76a618e64209b9edf74b43cf555ef746",
      "version": 56
    }
  },
  "version": 573,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d32396338346636336339643534396133.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d646538363763326465303139343165/63.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
