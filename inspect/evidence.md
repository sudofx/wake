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
  "generated_at": "2026-10-29T04:04:34.601074+00:00",
  "head": "snapshot:521f6b9ada5d8eb01502e90050e0de4a499d3b523137af3abdb25e2dc5785fad",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T03:56:35.522833+00:00",
      "head": "8a7961ce3591682918ab5ce471205511433d15fd61578a14f1190ed8b974878e",
      "node": "100.wake",
      "snapshot_digest": "f0205d646ea42975d58d89eecd2763021e12b2d1214133af1b564dbd36407e40",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T04:02:57.094298+00:00",
      "head": "3cd599f7281fb9770b8704da06783850a1102c40f19c3056193172e56c66b607",
      "node": "101.wake",
      "snapshot_digest": "ecb4246951d600986466e181bdf312d959f0905bd5f698f50e25386942aa3795",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T04:03:51.450002+00:00",
      "head": "093bc492563af99e45dcfbcc65247cef50e4186e03b66191534443d15d38b845",
      "node": "102.wake",
      "snapshot_digest": "835eff79ff2f5fd624fec48bb334a381ba947e3f3872cfb9ae3c0472838cd057",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T03:56:32.679191+00:00",
      "head": "fbebb1f4be25aa29a1c10645a3130ea8fd55a79e530b3d7d110578dd7bdaebac",
      "node": "103.wake",
      "snapshot_digest": "558a5a4796ee8c1435a0ff3612f2644c2cba4f7d5d998e89ebdb88241985a2c4",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T03:56:07.789603+00:00",
      "head": "82c6d47579be7126d2b79d0e09967bc64e3d77adbd9e701e77717121e52e2932",
      "node": "200.wake",
      "snapshot_digest": "a9415bcd349eaafb6f0b6e29f7d6f3e542a3ac58a7dfa0041c4c87e1184a821e",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T03:56:45.331008+00:00",
      "head": "f604a8342a41050299f49a669126df1c1ba8bde573352beb6a752552540d4c32",
      "node": "201.wake",
      "snapshot_digest": "4f42f4b5d367e44e6ececbe7f086b2ad20cf3aad6637d16502980815cb070df2",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T04:04:10.924216+00:00",
      "head": "438c62fb352ab3f25cc5a1894144eb2a3b403a6991b227bc4f74cf7c70a484df",
      "node": "202.wake",
      "snapshot_digest": "2ede728dc260d37c6cee1d1cc8c3aaa0b63fd93d375dde011a8d412f0ce2c105",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T04:02:07.044171+00:00",
      "head": "1c1aefd8484c9aab92ab5a517d0e3225c852b89b77b8cc629a1842e4721d1688",
      "node": "203.wake",
      "snapshot_digest": "cc6175dd362b1ac97fc56202179936361d2b2593e36724c628ad4af7f9e52009",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T04:04:22.163632+00:00",
      "head": "188dd5777ee85075ad2f0c2150d04f1d61d3790c1b9b1f7da63befbd4dac92de",
      "node": "300.wake",
      "snapshot_digest": "583abb8d17af278d08f54cda6fd7d1b74ee6771f2a37feeef9f1a98884623486",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T03:58:07.378779+00:00",
      "head": "76320a7c8b51810637c72aa98c8314b0a71c04a03c83932d20393a029f236a74",
      "node": "301.wake",
      "snapshot_digest": "37e1fafc0e0c1ac961e2d8ca90fe53ab3898e518e166b9c2168b532de458d56a",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T03:57:45.926555+00:00",
      "head": "d7e9ed3d7b97983b88d9ce10d03f7c471ee14360e9e2ee8d777653d762147888",
      "node": "302.wake",
      "snapshot_digest": "3ea1c4270ce761157a24c83da07b99446ba91b04f355b8e3adbff5e0c2bac5f3",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T04:04:34.601074+00:00",
      "head": "20788e438c619550f74594b2c7f6205308720e5c38927dc7a1f9af17f30c94af",
      "node": "303.wake",
      "snapshot_digest": "366a992151839643a3d26b1c950bbd6312089be6381e66c834d7531f3a1f7261",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d32386531656166333730633134343536.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d32656363323366656430666534626163.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
