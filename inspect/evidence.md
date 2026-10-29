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
  "generated_at": "2026-10-29T14:03:27.511860+00:00",
  "head": "snapshot:5ba896cf10bed300ba9ea74d2ec8bcbd6ac9bada10a8d8d432d8fbe739208885",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T14:01:35.729272+00:00",
      "head": "a16bbead4ba5e22da747dead5ac207589dfc989c719d22895837afdf1d5ea86b",
      "node": "100.wake",
      "snapshot_digest": "482ab40d3bd79c142afd81dfc31b3f1eb9b6504c769176263f9fc5494e832de4",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T14:01:23.349833+00:00",
      "head": "054dd35e7e2e39af6f6a107b1cd5d2ece88484049ba15af74f96a87b8e4f59d2",
      "node": "101.wake",
      "snapshot_digest": "48ee279deef25cefb673553548b2527bb6fd2803fbce86e8593dc8895f34f06d",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T14:01:18.691141+00:00",
      "head": "7c5e2cf595ffb7c20de8b85abddb49ed3adc9e05fe2e663583f99008db9262cc",
      "node": "102.wake",
      "snapshot_digest": "284020649e213a6cfdd0b53e30750f22593dd100a86302ad8305eb1691e1fffd",
      "version": 18
    },
    "103.wake": {
      "generated": "2026-10-29T14:03:27.511860+00:00",
      "head": "2e28bc241f54a349bb923e67939e0add6d5f866433e22d4c5d657145c5e7e18b",
      "node": "103.wake",
      "snapshot_digest": "f3c1ba69797033c93e3d5e96b426dc90f15471283d5b7651f3c45179b8e5fb0c",
      "version": 30
    },
    "200.wake": {
      "generated": "2026-10-29T14:01:27.500891+00:00",
      "head": "a0101acaab0778873ad9e9be8e941644a62381a016d8320720a835801cceecae",
      "node": "200.wake",
      "snapshot_digest": "5bb81d10de39afcbaeee6f96be45df9479452c6c791c6767525b355d5a4dfba2",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T14:01:34.237950+00:00",
      "head": "5c89dda25524e1bfa64dd4bdf35930f13e45fe8f423b4bd35667e22057924f07",
      "node": "201.wake",
      "snapshot_digest": "41f5dd2bce89efb137b6ce72671b28bc93fd2fad6378b4a1c44054a9636ab24a",
      "version": 24
    },
    "202.wake": {
      "generated": "2026-10-29T14:01:30.290232+00:00",
      "head": "31644d297780fa618582adfa03283cd22eaf102f4472afc36c2cfc20d13748fa",
      "node": "202.wake",
      "snapshot_digest": "61aacc40fc952a65fc126c89a761ec6df47f711b6c025195ccf4ef5668ac2f61",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T14:01:20.859919+00:00",
      "head": "202ac86683142fd6c13def6783ff2d5efd21a0e405b48ac85d1e2c86471f9111",
      "node": "203.wake",
      "snapshot_digest": "48eebfd18ff8b4d2a6fd6a549f6e11ed2fb1f1e5309adc739429b11af72716d8",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-29T14:01:43.858528+00:00",
      "head": "50d337062294f4bd789cd63cf6c7149d9926424d7585ddf98b5b6ea05e62b187",
      "node": "300.wake",
      "snapshot_digest": "981fd51aa22903d5dd3779f46eec55714b9275a9825ff03ceef08b03b83924a5",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T14:01:34.740716+00:00",
      "head": "28cd33ad3387a6b7a2f42fedf46e4f4f352dabba00dd26a96f1ab7337eab99cd",
      "node": "301.wake",
      "snapshot_digest": "aabb61b3a703c91e80b95dc09fdb31c4cf6e1bb11fa5b47634b0f41ae3fe017c",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T14:01:39.696402+00:00",
      "head": "d6b0c7503eb8302640d797801d4183d61dd30ab76d8c6f855cdf8a98a07f6647",
      "node": "302.wake",
      "snapshot_digest": "d85b99f03bbddbfb321348531a6e7ad6f5947f8de6b4de75e02f832acee9f83a",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T14:01:27.244091+00:00",
      "head": "c5051be952f37fdb950ac858fe6a111d2c4b0a2fd64cf96eb6abe96669ce276a",
      "node": "303.wake",
      "snapshot_digest": "da6910539b05ba59e040c819b833805e211dcbdffdae5950e1c7cc2c37f7d2c4",
      "version": 24
    }
  },
  "version": 297,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d33616631643731356364386634396261.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d30653134623338356566356134663139.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d726573706f6e7369/62696c6974792d666f726d6174696f6e2d30312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
