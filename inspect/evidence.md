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
  "generated_at": "2026-10-29T05:00:02.978342+00:00",
  "head": "snapshot:58e6ccfdaf480b33223a1503c64f6706979534702d7d84905385290ab5b041f7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T04:59:15.990728+00:00",
      "head": "76455b802c67fb3abfbbc80bda7ad73b91257debecc802bd929c584af12be577",
      "node": "100.wake",
      "snapshot_digest": "1fd0222126c0f71bc0ec91e2dd46c24b2bd9fe6b5956db9e928c9df0185934f9",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T04:58:42.913921+00:00",
      "head": "7fb97a42e09bdc3bd9b739b41f6a5aa96ff996d19a759bd0d5e1f3a5a56e759f",
      "node": "101.wake",
      "snapshot_digest": "c86c0b70bee5c31a9c876ed0e66d647cad2631b54aee1fbcc74f77e6be0b027b",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T04:58:43.014575+00:00",
      "head": "0336f6c24a4926eee258067427e1c5314ae6167d9b60553b92d9cc64f2ce1d36",
      "node": "102.wake",
      "snapshot_digest": "f03ee044816cfff5ce8ee168d4e5def223829757dbc69b3b06be280f1679bf60",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T04:59:12.180138+00:00",
      "head": "997769a336c10ee2e5c8c2ae3de4122c1957b0b43147868cc604b3b7c31c23aa",
      "node": "103.wake",
      "snapshot_digest": "25f2180c13fbd1a0513343a640c871c49d399edc38526ff76df8a01ecb367a74",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T04:58:39.695804+00:00",
      "head": "0437875611c56fc6a4d526490c9fb775679cb6af2988996916f39c3f89b2d01c",
      "node": "200.wake",
      "snapshot_digest": "8b23d2e8859569c0adcb4a842b46033fc8fc78e6c04c9fed0783e4ffa5e3ecbf",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T04:59:51.238548+00:00",
      "head": "e645f5f7a9d4e79a3aafee6bae49a1d2328984dfbfa07eee19d02e4c1fbe7c8c",
      "node": "201.wake",
      "snapshot_digest": "28363d06738cb7513fa9f602792c7f28aa4d8f2c0e6df11594fbed9c9d01b65b",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T04:59:02.200494+00:00",
      "head": "cd93517a4b7d8894e6bb39439223d89f777808ed982d6ec0b6b617fbf1e61d1e",
      "node": "202.wake",
      "snapshot_digest": "97b8b2f4dd9d6d0f18763da5d621b32d85db56c0acb6bb033fcfa0e4a7a78ce1",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T04:58:06.310610+00:00",
      "head": "7389a7910d35c0177ab646704187eee26ae93e985acd989e20e68d3fd1528cc7",
      "node": "203.wake",
      "snapshot_digest": "c3156a8faa48a27d9a4b28eaaa1b4fbb92be8cae79e6c358399f7d95fc5422dc",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T04:58:38.558766+00:00",
      "head": "c2c9433aae5f4a34688940788e662a6bce00b1f9dd7a5efeb8314e9fe1a565ef",
      "node": "300.wake",
      "snapshot_digest": "64da406506173d26008b4ea4b95411068a26434fc1e21ed418a17b5c2b6d3045",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T05:00:02.978342+00:00",
      "head": "b141212baee0503c075c33aaf4376e2b452243a4c6c93e324ba741e85ae79c6d",
      "node": "301.wake",
      "snapshot_digest": "aee50bfdb8d3fb0a74be73d3eb77eea37bba10202914124f38c8a588ae040a86",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T04:59:24.323151+00:00",
      "head": "b3cc70a411ec8b6e130de2b3d2cae03c8d5f28af0ae1614be3564324e4f5d3d0",
      "node": "302.wake",
      "snapshot_digest": "630d984011354126871dd4e93f614d983aab10f3d350e2bbb19c0d685bfff362",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T04:59:20.322490+00:00",
      "head": "eb2b87d6be447abd54b0aefd85f75c72f15df3c75c857d51dc253b058dc9f682",
      "node": "303.wake",
      "snapshot_digest": "02be1531b52bfc89e1685c96b3ee09d4826bfabf08a911e35b1f64fe741e6021",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d66653537303164356132666134376432.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35396430366634396236346634623061.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
