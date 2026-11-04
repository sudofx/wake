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
  "generated_at": "2026-11-04T04:04:16.889049+00:00",
  "head": "snapshot:2a9f162a4832a89b6861d4d23d9863631403938c1c91182e085b07298b9631af",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-04T03:59:01.612950+00:00",
      "head": "8f95154392911fcaba503a3f17a0cfae67ef3189ede49697629352b526471f9d",
      "node": "100.wake",
      "snapshot_digest": "541da4bbcc92ce2911f365da2b0296d35ac075904837a608bc1096dff3caed58",
      "version": 6
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
      "generated": "2026-11-04T04:00:47.500124+00:00",
      "head": "1455f36d4d88d5a544a876c7396fe85a302ee21a101f296d6b2859fa9ac95cc1",
      "node": "200.wake",
      "snapshot_digest": "6d8ca986368e0947a71d5e5b35f7300fcb089d528a1b2591f218c5ef1dbd15f1",
      "version": 8
    },
    "201.wake": {
      "generated": "2026-11-04T03:33:10.134108+00:00",
      "head": "11a0fb30789663168b9279c909bf6a21e06e0daa27339d322f8ac53208a01aea",
      "node": "201.wake",
      "snapshot_digest": "210ec6f6c6f52ecd3c26f2ace0b2c63c227968dddb89747506be53dfc97529a4",
      "version": 4
    },
    "202.wake": {
      "generated": "2026-11-04T04:04:16.889049+00:00",
      "head": "b1b38354be4794a16d3788644aaf564ed044779367b1e999a448ee6f316fe285",
      "node": "202.wake",
      "snapshot_digest": "3f2defb5d5e2a35e37b88d7fd0b9b6ec943fadd9609e4832a95f51cdd91c05eb",
      "version": 8
    },
    "203.wake": {
      "generated": "2026-11-04T03:52:06.840584+00:00",
      "head": "354ab8d3eb84c35eeee4e75f021ea22403e98147e726df1de4e84e335b142ec8",
      "node": "203.wake",
      "snapshot_digest": "af102e47db91b1c136b386a2836d77dedee4b511cf42c05cf253d6e823b28961",
      "version": 7
    },
    "300.wake": {
      "generated": "2026-11-04T03:36:48.023616+00:00",
      "head": "74f8cf585c23d0559c46ba5c0062e0ffd79b6c3bf9a8adc97f5cb8d8955cf0f2",
      "node": "300.wake",
      "snapshot_digest": "c792739747d9986acf62b4f1f1cc003f0b74e9559633768eccce9670666031cd",
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
      "generated": "2026-11-04T03:46:53.606178+00:00",
      "head": "fa67c66e540c64d31aa8b4a470129c0dbc89397b8e56d0b4315ccbf1c01f5edf",
      "node": "302.wake",
      "snapshot_digest": "fb8bd8189626671f2f01bfb3b7add00fa7fdbb4a55689aaf90661deed6e9c10f",
      "version": 3
    },
    "303.wake": {
      "generated": "2026-11-04T04:02:30.786632+00:00",
      "head": "a594e886c38c9215dbb54614607e68f4310575a04f572c241ec28ad75669c634",
      "node": "303.wake",
      "snapshot_digest": "e56ee47639f98edaded103da52d4f4aa4f6349f32ae572de48dce0db86ac00d3",
      "version": 8
    }
  },
  "version": 72,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d36383566663038643635393234376661.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d313166353866653830636463343639/65.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e6f7465626f6f6b2d77616b652d636f6e74696e7569/74792d73747564792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
