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
  "generated_at": "2026-11-04T03:34:52.236726+00:00",
  "head": "snapshot:f1fec4923bb14adc3d0a5d91891ceb03cc218efb36490ddaaa24f39965618d5a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T03:05:11.029392+00:00",
      "head": "8254a70f683ce5bbf443efcc820c5d22d2c6f7154e7df592265846f9cfaf34ae",
      "node": "100.wake",
      "snapshot_digest": "6b3b789edf12c98ec8893e274454510982d505d70c8a36dd17880177dba1e4cd",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-11-04T03:28:03.145273+00:00",
      "head": "5faf6611ee970a1a4369fc1b8bc344ac74452288e720950eef3211ab130bfc26",
      "node": "101.wake",
      "snapshot_digest": "91879487c69230564071b382239a317280f2bee156dbd2389dde158ff5980cf6",
      "version": 2
    },
    "102.wake": {
      "generated": "2026-11-04T03:05:10.822271+00:00",
      "head": "f152c9c4d3f21a5ede3c4716d91d75af97dd555e5606577cc8716dbbf15ead49",
      "node": "102.wake",
      "snapshot_digest": "4cabf85019f2c20ff162659d7b3261d4f1ec60c37f5b217614d4db0f5cb58b52",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-11-04T03:34:52.236726+00:00",
      "head": "2b0d3b1cbbf40412a29a081ca63ac19e7570ee4063052e5ed8016f3f79c16a53",
      "node": "103.wake",
      "snapshot_digest": "a2e4c3e299a8abb6a07f6f86a4f30b4b4b7a4768ce667b3291bfd98f69209c9f",
      "version": 10
    },
    "200.wake": {
      "generated": "2026-11-04T03:05:11.358795+00:00",
      "head": "a163581d00468ee7ce589cbde15f7d7d35a946dd036942d9aa055e6498639450",
      "node": "200.wake",
      "snapshot_digest": "535dcb762ebc1efe7a74d33b8670137283500043baed2933e574639106308399",
      "version": 6
    },
    "201.wake": {
      "generated": "2026-11-04T03:33:10.134108+00:00",
      "head": "11a0fb30789663168b9279c909bf6a21e06e0daa27339d322f8ac53208a01aea",
      "node": "201.wake",
      "snapshot_digest": "210ec6f6c6f52ecd3c26f2ace0b2c63c227968dddb89747506be53dfc97529a4",
      "version": 4
    },
    "202.wake": {
      "generated": "2026-11-04T03:05:11.096223+00:00",
      "head": "130f2ab7c7ccd4ac9f5ef9cff722861cd75c57137b7209701b20fe220b984d6f",
      "node": "202.wake",
      "snapshot_digest": "1a688ca90b4e06a1c6ab55c2da4f05590de866d0252562bc3bf8f3dcaca0aa59",
      "version": 8
    },
    "203.wake": {
      "generated": "2026-11-04T03:10:36.942527+00:00",
      "head": "df348d187313096dc8305c93ea87eb4ce99e3e3039951c9f71c790bc25d48876",
      "node": "203.wake",
      "snapshot_digest": "ce20cb465b599c8e0231c1340bf0efcbd91b05e01dee323442961101ebfa645a",
      "version": 7
    },
    "300.wake": {
      "generated": "2026-11-04T03:15:54.961445+00:00",
      "head": "d19f8e8fd1dd618e143797bb238d9a40aa1a6cb909e2f35d3e1b72a0947a69ac",
      "node": "300.wake",
      "snapshot_digest": "c7ed39201ae580f7a468ec382b8a288119c2dd1d6a93f8065f482616df56ab5c",
      "version": 5
    },
    "301.wake": {
      "generated": "2026-11-04T03:29:42.407836+00:00",
      "head": "3f35ffe955de507116f53e0b4e6cf4c703440e4311958801f8e30140af8728e1",
      "node": "301.wake",
      "snapshot_digest": "661b7e326441851857e5e393ac5ce827d45e83c59378071c69c0ba32e0f0041a",
      "version": 4
    },
    "302.wake": {
      "generated": "2026-11-04T03:05:35.248861+00:00",
      "head": "72e9fbc4e5fce6e98cf6c7d0b4b0785bfb5d5740b53d778a4bf15986845c0671",
      "node": "302.wake",
      "snapshot_digest": "d8bb15544a083e93d6ad3acf6ebaa74be4ad68d7bed0e3391485f450f526e040",
      "version": 2
    },
    "303.wake": {
      "generated": "2026-11-04T03:05:11.088371+00:00",
      "head": "2e8f3f69ee9c43f610e399a6611498b48eee4e1c2aaabff476af6c3c7c1a5d78",
      "node": "303.wake",
      "snapshot_digest": "6f0f8e0e7de4c889b86fd8a9ad4d6b34fc527bd31b953e761a594c59e0abbc18",
      "version": 8
    }
  },
  "version": 68,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d343862616230323837336336346431/63.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d663337613736643065346432343231/63.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
