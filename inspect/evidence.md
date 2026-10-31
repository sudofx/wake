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
  "generated_at": "2026-10-31T11:33:29.495896+00:00",
  "head": "snapshot:f48213718e31c7127ccaa6ca550b0531c802d6ee522660f0c014b61a28da0301",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T11:33:29.495896+00:00",
      "head": "f5b2307e7e941342653b34c8742ff9418ddc8e8be1a3a339931db8fc49624f15",
      "node": "100.wake",
      "snapshot_digest": "f9cc53253d4eb063b13e31a0a89b21bf976c97c651c6e93cd651c009f87fb4b2",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T09:27:25.847819+00:00",
      "head": "5e1f321665cbd4d2b2c40fd23bb122c46255119265e5c5ce9c31c1fd7d427b2b",
      "node": "101.wake",
      "snapshot_digest": "99a61c5553793b48ffe6ffce14b42718b517881e34e1b4cacdec46bdceadea63",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T09:27:26.164498+00:00",
      "head": "3838c39ddd27e8f250582e3ce1badd5c3a983d0ce06329af819e86022492a221",
      "node": "102.wake",
      "snapshot_digest": "153a530db10f4534f13095380dee6a7397274c62960b8ce57279cea4e7ce6b8b",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T09:27:33.279119+00:00",
      "head": "1f86ed6a74a6e9aaaea26a3bb2b40c88a50d6b4270f1fe11a7afe347b4de6168",
      "node": "103.wake",
      "snapshot_digest": "9b48f3b417f4b2f8994adcd8380195fc8ea6cd4686a96ed10968c3524651f133",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T09:27:37.629333+00:00",
      "head": "320c2d01b744072fe618abda740f3d2f39fe7919e7b6f045881185785a2c71a3",
      "node": "200.wake",
      "snapshot_digest": "b5ad8f3e829c7d8ed126b7d13d231915ffad130a846a06582a600060a1b5f079",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T11:31:46.447344+00:00",
      "head": "d93ce910dfd8b137c322357eeb1caab550b89fafbc2dec31737b8f1214f7b062",
      "node": "201.wake",
      "snapshot_digest": "1db7b247eabedede0bbb9e2bd2ebc2731257d24b843a48e47206a80f7b988bf2",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T09:27:20.165358+00:00",
      "head": "543d2d1a031897dafd17accf9f479cdcf5d26aac6d20397b4df46d18c4c5899c",
      "node": "202.wake",
      "snapshot_digest": "3ff4134e4ae06b43e4e7a972f72726c50f5c9d5c0d0de8f7a7ab16a9469f27b3",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T09:27:20.892132+00:00",
      "head": "95d27d47cae778fd81af6f2ff0cd6e8e7a044e2005f56ccc04b1486ffa4e317f",
      "node": "203.wake",
      "snapshot_digest": "dba123e044bd4e056c4e858eb6cce8fa9d4ac70911ba7d60ada18d76793605df",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T09:27:32.401542+00:00",
      "head": "b534c8b2642542d9600dd569169f1525d811e589d9e9acf23f8f1c55beca61ed",
      "node": "300.wake",
      "snapshot_digest": "e99b109c9eab678425d0c47a75ccfbec237dbbf31142aa6bbe75e3524c3b12cb",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T11:28:26.929786+00:00",
      "head": "73b3fbc53bc02bdd48143fa7d6d3676e1d89d138ba6b1571b62a09f12100d9e3",
      "node": "301.wake",
      "snapshot_digest": "8c76b4df9d6c8b598bec342f69fc445bba3f1e7093294e3f4fd65aeb470d8c83",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T11:30:12.862032+00:00",
      "head": "6bbb0d98ba3f6b17cf1fe2e53c76a7a93a13d2294e6e8d9d884920c65ecf5ef8",
      "node": "302.wake",
      "snapshot_digest": "1b28b07e148174b8db87592a7099a51aa0204cbd64847937adaff748d2cf8ba7",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T09:27:21.970466+00:00",
      "head": "58e8ea6d70ab599f005d03f09c5ffb2469821d9e0811ea188f36d28fd5dc454b",
      "node": "303.wake",
      "snapshot_digest": "96c11a570f041247dda95ecaae42a849aebf677bcbced641f1f0a69e431f8938",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62383565373235303731303134613732.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31666264373562326562646334383333.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
