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
  "generated_at": "2026-10-31T04:34:46.003554+00:00",
  "head": "snapshot:ebea495203db1737231c6db6b49a1ad5d9fee5502b223df41b6b46e2cbe52c1e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T04:31:26.981026+00:00",
      "head": "8367b2fd2354db46855a5707dcdc22beb3446e9db462d54bfd170c742f509679",
      "node": "100.wake",
      "snapshot_digest": "91a51fb8ef3455d4dd9091cc242da991dc02e2685a051cce430341e9b90d35b9",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T02:27:45.175475+00:00",
      "head": "3795be723fd288aabaedc78204fa8891448898834cbedb843160638bb4384639",
      "node": "101.wake",
      "snapshot_digest": "be3e971d608585890b6baa047b8e1378bb0021341a408d1ac6aa81a21f8504bf",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T02:27:46.470868+00:00",
      "head": "e46de38ef786d9e9c3f8de240fbdf88c851f98938da8e8b7b0244bd3e0e88772",
      "node": "102.wake",
      "snapshot_digest": "b9206708fef1b3f2282fdc08c8eae3de17d0219a689c4ef12ae013fa2a85bfa8",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T02:27:51.969405+00:00",
      "head": "d6e8aefb752e9b5a546cbbac4eb0dfccab7edd804f1923ba40c76d0294bbf324",
      "node": "103.wake",
      "snapshot_digest": "6ed931106335e11cd228622b67724133dcad627da2fba7b3387954092e6fc265",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T02:28:11.739324+00:00",
      "head": "ab2f1a914847ecd94bb3d92e6c97d8fc96157927961e9e17fac634c12cf551bc",
      "node": "200.wake",
      "snapshot_digest": "3492b4f004b8b283b8ad2d337a8ca4522f21e9264d91ca4216e8887c9a22bb8f",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T04:34:46.003554+00:00",
      "head": "1e14e12364466f1268080bc072deb8eaf0b3c7a637457a0d5d2bb79bd608d011",
      "node": "201.wake",
      "snapshot_digest": "e78c4efe858be99b7f48d240cec44d9daf822c606d16a4adb7c1b58d6463be9c",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T02:27:48.422546+00:00",
      "head": "d388faa83df24f8e618918eece463d7ee6ddd4ad68eb7aad07679c3aca0bb4ab",
      "node": "202.wake",
      "snapshot_digest": "1723f3b7ad94c371396cf077e48f18b4fa48ed005f75a81a8f9131e8489a2c4d",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T02:27:49.246019+00:00",
      "head": "004794cc5a3b81129151c9cd191d08621a4ac893716169b390e533e02af00c63",
      "node": "203.wake",
      "snapshot_digest": "7f0f4fa715e161a507d0c4a167382056ddfe625633671e85020b61458864941d",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T02:28:11.226509+00:00",
      "head": "0655ade436016ca4e273ffbede2a2095f2c1478073efe52fb2e4b0e90dc2b314",
      "node": "300.wake",
      "snapshot_digest": "e8d4142afeb794d854017963262c6831d15a227e6bba4f6c5e04da1cfc45db6f",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T04:33:46.191652+00:00",
      "head": "a052d06b109c42db2fad9dbce3efe7cc1fb5048c7f8bb17c3f036f3d13c6cdbc",
      "node": "301.wake",
      "snapshot_digest": "79d1a61b5b332bff843bcaaefff5eaf2031c968a55571f71c0e106b55903584d",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T04:32:17.884823+00:00",
      "head": "39cc865797d3d453d8c1bc5a2af57c9809cb4c21e3e6bfd194758c9dede151b8",
      "node": "302.wake",
      "snapshot_digest": "70d7c5f8ee4a712ce03771443aab7fc8f566116b7b21aa4eebe5e3cf4a3ab7de",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T02:27:46.037452+00:00",
      "head": "a05cc68df30a06616a2325cd20336af7103544dada473dffae98c83c77aa0cfe",
      "node": "303.wake",
      "snapshot_digest": "72cf152a7110bf3d75b0a1913757d8187a4cebcd2f9e88153412e3c616f752c4",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d37663165653164346432303234393133.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34386164373538333939323034646436.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
