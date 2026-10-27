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
  "generated_at": "2026-10-27T23:35:17.847405+00:00",
  "head": "snapshot:f7b7c47e3c9540b16495767fcf1dec53e5b72cfe08c24b214630d53163b19633",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T23:35:00.380405+00:00",
      "head": "91b565828a229d33c10cf1655fe5ee799204b832b06768de25bfa3f673a8d026",
      "node": "100.wake",
      "snapshot_digest": "b5cfd24ce699c309dc12184e438c7bb8a783cce2e13024dddab07e444ca385e3",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-27T23:34:58.420023+00:00",
      "head": "0df7fc5476319d44c37b10dd85b919ba040aad73c30236d9bc85b57090ea62b4",
      "node": "101.wake",
      "snapshot_digest": "288d58f37ea0fa163d08538204d5c5adbed4aa82d7f706d316d67d970bd4c0d1",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-27T23:34:54.501701+00:00",
      "head": "ea44be2e083f351ea81fc46c7897bc2d79ce829c363194b4ab3c36fd393b6a0b",
      "node": "102.wake",
      "snapshot_digest": "2e72b56d48fe1cc4c65127eff1fbc19a0c2bd591212aa2ab5960de0d00970980",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-27T23:35:12.375425+00:00",
      "head": "e2f119d4d32517b1816bc38b2aa9599dc8f3da07b7b344006976a87fb89d8159",
      "node": "103.wake",
      "snapshot_digest": "1099ced83c0ffc8da6352add3e4cacbb9a9ec6444bb7ed3c2feced17aa3cce13",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-27T23:35:13.023749+00:00",
      "head": "b16a8341d9244b086f6130dca501d1dcacdc1121589ac1794eaef5881663645e",
      "node": "200.wake",
      "snapshot_digest": "c61ceffac0ac84e81efa4891f36ec365f08a7c55cb94c846f90187e355684457",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-27T23:35:17.847405+00:00",
      "head": "3e2b0c830f4eab5d211acba780121bc3bf00bb3ed44e8e7c840fb8adb414ae4e",
      "node": "201.wake",
      "snapshot_digest": "8bd38b0f1020ab7845bd6d013e936c5e0966b51a44430dbd817e3ab336d30816",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-27T23:35:01.870132+00:00",
      "head": "9743b5e51873a2f79a885bee51f514b86013b513f27d50166c29a1d9e90db422",
      "node": "202.wake",
      "snapshot_digest": "e3ffbfc510ae3261c5a7487d78909e5931ec00ec9480f1f8a2718a9712ceb727",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-27T23:34:56.473165+00:00",
      "head": "581bca283a406656fbf2aa232de3d80746e3486e34ec8c31406c61d7ca11548a",
      "node": "203.wake",
      "snapshot_digest": "2357040bdb6c401546641980affa070d1d1331888a3ef70c4abae1ea1d486d3c",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-27T23:34:49.198224+00:00",
      "head": "42ab178588eed9e03c9bf9753fe58fdabc0f4750e7f096fdcee4c921123c5d71",
      "node": "300.wake",
      "snapshot_digest": "3af4d7834b8c71436ac83fa82d9465fc49a58804e9bb6ee6252799e41db97235",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-27T23:35:01.659815+00:00",
      "head": "0077bd3999eb2095789ee61504b4bda22582fac3e20655d6036e01b758da8c59",
      "node": "301.wake",
      "snapshot_digest": "96922b73b1375e1b5a36f8966a29fa2655b8f4b71d9b4485830eb7de7bed2287",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-27T23:34:48.459519+00:00",
      "head": "96bc17dfb86aeb087272efdae0ab04a0653b2796e0a1dbdf8528715cbd1948b5",
      "node": "302.wake",
      "snapshot_digest": "78df3794cebd8596e814cdc309b5e90cec68e64891f8dab1bee5f6b5388b5063",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-27T23:35:00.655806+00:00",
      "head": "8dfac6db9db996d2245e996eabe0288e6383ff721554c934a105048cfa7f6123",
      "node": "303.wake",
      "snapshot_digest": "24ba687c26a9adfc192d97d2a7d5d4dbf9c375bbec1dfc4474c16fe93a1f04fb",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d39306236386437656337623234343639.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d39323262316333366263323334373762.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
