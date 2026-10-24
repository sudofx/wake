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
  "generated_at": "2026-10-23T23:56:45.591495+00:00",
  "head": "snapshot:b5acc0b3cf15d9dc9865623ecde269431b4602e0f252ad335cc368cdf8ea1ec3",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T23:50:12.046000+00:00",
      "head": "3fac314f3e1faf0515b8bcf785c3dcac036b667f0786807a12e75d3e5f7a085f",
      "node": "100.wake",
      "snapshot_digest": "f5f5868ed10797df43d607dde6c665b9f3cbf61fbe891e5fcd62451dbbe2b84c",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-23T23:29:11.616288+00:00",
      "head": "98b0ca731d7c8135e22a013c1c8c6f0c0b11fcb25a12d626723fdb26c76d808b",
      "node": "101.wake",
      "snapshot_digest": "e6c0f8fb6b61d3f1158738bf99f4e35f6833d811d5f263822e351089c9c24a04",
      "version": 31
    },
    "102.wake": {
      "generated": "2026-10-23T23:35:29.047918+00:00",
      "head": "496a0a78125685f0c1dd8467a0f27dd6eee7b426355ee19c13e8e4a77b92797b",
      "node": "102.wake",
      "snapshot_digest": "785a8ae12565faaf360800b647f1eaabbbb74cc0a7794d883bcd0f07a31f7ef2",
      "version": 35
    },
    "103.wake": {
      "generated": "2026-10-23T23:56:45.591495+00:00",
      "head": "602d559f808544fa21660a9d98805b594b5b97c2e4ed95f90703d71e86f82430",
      "node": "103.wake",
      "snapshot_digest": "4db38a2b984aa8a454526956f7e4b7c60eb79d28e7a815d98895af14e067455e",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-23T23:54:40.739039+00:00",
      "head": "41ae371a1b4aabe8a2df2c0681dac335d5c231b3741f7454b11ff6cb108ba807",
      "node": "200.wake",
      "snapshot_digest": "b76db635240a25ed5331645cee949262c7ce446aed24c2c3a2de7edc28cb915e",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-23T23:54:50.376571+00:00",
      "head": "a710e6dafda99a093412ee5acfc2d784895f592406d055517864c41879e3858f",
      "node": "201.wake",
      "snapshot_digest": "13f8e9f01f42fd7867a49dda5fe6faefb19ae24be2594657aa1e71a3e7636da5",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-23T23:55:02.013217+00:00",
      "head": "89253f66622cbfa5c100533b27c20c29e6f76704158c622361520b323e338adf",
      "node": "202.wake",
      "snapshot_digest": "84f5532933e77673440780dd529b517552420918655ddba85816e2687ec4bce6",
      "version": 38
    },
    "203.wake": {
      "generated": "2026-10-23T23:54:30.883194+00:00",
      "head": "d5314ee41ef2c392823a43961303d5d9a2228fa6e68dc5d18a8c98998a873f5f",
      "node": "203.wake",
      "snapshot_digest": "87f9f27e101b2ed0027a12dd93d87cea7379fdefd43af908176281223d338826",
      "version": 19
    },
    "300.wake": {
      "generated": "2026-10-23T23:36:40.509970+00:00",
      "head": "249b966dd7d155b01a2192f3eef4ba540786807484378e21b8b6538ff5789f2c",
      "node": "300.wake",
      "snapshot_digest": "4002da588cd9fb67c18b9d08f3e9510c2b04f82ba922bc06c92dd2990936a992",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-23T23:54:19.401556+00:00",
      "head": "8e1d5830a4f085923937733d854f1c3730d25a79a5c3cd0e1b7f6f95862a8d01",
      "node": "301.wake",
      "snapshot_digest": "ed8de29df0d51cd121f4cfc274b88579d4ad051e7093a7021d6a1052489922ec",
      "version": 39
    },
    "302.wake": {
      "generated": "2026-10-23T23:54:03.238177+00:00",
      "head": "e953d8693adf1a4dccf9d4561a32919936136c519e5b7d1a44ab3a22d0730ad0",
      "node": "302.wake",
      "snapshot_digest": "467101a28ec49efc6736a9508f15315dcc1de21aaf4f811946444b35f3c37ed1",
      "version": 19
    },
    "303.wake": {
      "generated": "2026-10-23T23:53:57.000971+00:00",
      "head": "b8952345dc34e1d70d1f71fce3f96c219895ffb53db80156370b7b32b6e85d52",
      "node": "303.wake",
      "snapshot_digest": "7804fd11b7eb8b63c196c0e1fcd34ac4079d2498a2e51b0fc85d0529f160b247",
      "version": 36
    }
  },
  "version": 337,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d61313766363066386633376234323835.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d30643162636539336530623234623536.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
