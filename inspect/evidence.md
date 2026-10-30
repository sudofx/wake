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
  "generated_at": "2026-10-30T11:28:27.936041+00:00",
  "head": "snapshot:b4ef9ed927d634345f0650e8f06e15d63020add44db9937097ec72ad437840b5",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T11:25:09.292765+00:00",
      "head": "5e7fa2169c36133b6b9b0b3bc3463b7fa09c9395fc40cff7fe4ca7c063194290",
      "node": "100.wake",
      "snapshot_digest": "69825ffd7878000483a7db5afd405f15fb3a022d91f1782beba8c8e613bbf052",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T10:21:05.103025+00:00",
      "head": "4973f697ab32e9036f6f4911b6e7c5044b86bb57e12237fc528b31e5fbda8fa9",
      "node": "101.wake",
      "snapshot_digest": "411ea02837902734ab98af432e1e30f635aa22934056f54857cb4fd85e63e3a8",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T10:21:07.122439+00:00",
      "head": "042aa5877662c6d019b01485f0a0530fcee241a9fdd8a9208eac3ecd2fa7edb9",
      "node": "102.wake",
      "snapshot_digest": "bc15a7f0a2d6c1f66492abc8f698207c275028be63e605194655d6a74616488e",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T10:21:14.520975+00:00",
      "head": "f1f99872d88808a7f13196109b4ddf0e457b664454d095e91fdec7f62d5aa3e9",
      "node": "103.wake",
      "snapshot_digest": "0b1c3ded07364d8f8eabec12e099c215d02573337c8bff3770edb734fad988b9",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T10:21:15.080354+00:00",
      "head": "63397182e4e079d4aa87b46ba8c69fb3cd4f7f94705b696d36e7d566c5060514",
      "node": "200.wake",
      "snapshot_digest": "d133e8aee9cf7e8b085155bb8f954f0c7609a0a828a77d781699148bceb658f7",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T11:28:27.936041+00:00",
      "head": "3ee89e18a668cb703b2462b032ab895d0c2bfc82d2b488a89977ee53654ef506",
      "node": "201.wake",
      "snapshot_digest": "2b395e8f0cdf84b6de40c1fdcc364288b1ea4c760a893ed105da3b1e8e681653",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T10:20:57.619469+00:00",
      "head": "5b00096c71c4bdb02cc77be435affe0fc191f6cfcc9529394a04b27ab6bc6081",
      "node": "202.wake",
      "snapshot_digest": "0540f8d10116d4b67725c5e91c10e1cf4d42ad9a08760f1b51bb5bd3db49fe75",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T10:21:00.664042+00:00",
      "head": "aa69856bac117f2b7a4f3d8f1352590592b29294975b714b412503c0afec9613",
      "node": "203.wake",
      "snapshot_digest": "5a3c930a2eb8b627fabb0c3d334b85f1dedfc2f991aa54146c052bc66220bc8d",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T10:21:17.043921+00:00",
      "head": "1b4940ad8873f05a52985cc372c92540275b3102e9f71793285a438ee48729e8",
      "node": "300.wake",
      "snapshot_digest": "d1171134f61a88e03a044767e7f73d751731429c0b3a33b4ad6fe7cf6891957d",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T11:26:52.807061+00:00",
      "head": "5d5daf57a9dd3a7995b6dac43ddc5d4dfe58d9939094d274ae3b7bef552552e4",
      "node": "301.wake",
      "snapshot_digest": "2bba46b86bccdea8c8bb0f694c7c295ec4cd9cc77f1ea401803d8e649af31c1b",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T11:23:13.898088+00:00",
      "head": "f4129a0624747d62905dc33f348fd23a7d9479361041f94270fec07e2d40c46c",
      "node": "302.wake",
      "snapshot_digest": "0684e169b977330e35482ac4fefa4e24f5dd121423ad947037c57d3965b25a38",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T10:20:58.862515+00:00",
      "head": "a764873b5de6b6ef2917bd30e3491b1e9397b972d4575339c7b175bd787691cc",
      "node": "303.wake",
      "snapshot_digest": "aacecb8010577ad856a789bd4ec2df8b8e6a157a5939da03d5be49dbdc7ad7a1",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d30373334383436616134333534316438.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d36656333366463353763306634303561.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
