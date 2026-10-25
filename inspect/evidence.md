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
  "generated_at": "2026-10-25T00:11:21.237687+00:00",
  "head": "snapshot:fb7b381744d72f567fe6040431f3d2053d75e8c2dcc0ff28b42533a2bb5279a1",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T00:01:12.234664+00:00",
      "head": "114cd7ef713bd1c1dbccbb0362f5a4f097b82d714b189db40aa216a8d9d6d5a2",
      "node": "100.wake",
      "snapshot_digest": "9bf3e3bf74826f11fb85b5411b53bb11b5eb6efb27cca5e02b4437f7d009fe9d",
      "version": 25
    },
    "101.wake": {
      "generated": "2026-10-24T23:45:54.023732+00:00",
      "head": "c626c81b3f9ead01797c9e1f1e290cb86c7d38726d56fff7c495b170642e93ab",
      "node": "101.wake",
      "snapshot_digest": "f1e31c58500103c04d5b2764b56f32d580175cc003e5f8e4ccc6443e17dc1653",
      "version": 40
    },
    "102.wake": {
      "generated": "2026-10-25T00:08:14.342641+00:00",
      "head": "ca5b823fd6bc0455eb3bc48fb5775e870948e1b29c18957b715a7df850c6fdc5",
      "node": "102.wake",
      "snapshot_digest": "0ffed47677a680136d609d3d85d9878cce62ede9f93ca2c0987c71a118c1ffc7",
      "version": 53
    },
    "103.wake": {
      "generated": "2026-10-24T23:45:03.824605+00:00",
      "head": "fc122a3027395a05c876cd04ed22c7ab8480028632aa5e3d7e9d488d3fdf212c",
      "node": "103.wake",
      "snapshot_digest": "2fbfe664738f881ae43f64c27aae58e82605329708be77189a450d7de70c0f41",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-24T23:43:45.294342+00:00",
      "head": "f4d319c59d66b3abac5b985851835b2e322235e338fa051987b6f8f31e11b198",
      "node": "200.wake",
      "snapshot_digest": "d4175dfe72de87594e38df0caeb0788a783e8fc1f961b014fb7cb6d66e26aa35",
      "version": 33
    },
    "201.wake": {
      "generated": "2026-10-24T23:44:04.175595+00:00",
      "head": "3a01d4ad1f4ea4bb16c47d46ec4e38a53a56e2bd42b345b1683d99f9d744254f",
      "node": "201.wake",
      "snapshot_digest": "c3d7913406aef3478fa72660b2b603ec03b80701b900d2e81906cdb3988ea98b",
      "version": 37
    },
    "202.wake": {
      "generated": "2026-10-24T23:44:39.072552+00:00",
      "head": "9fdb900b4eef1cede64c12b9605b8cb4c7645af7e88679689f4782aade9d6799",
      "node": "202.wake",
      "snapshot_digest": "3e075a017c51d0b235344134075f527aa7fb2bad25da563cdf02d709378d08fc",
      "version": 51
    },
    "203.wake": {
      "generated": "2026-10-25T00:11:21.237687+00:00",
      "head": "7cab2bed8d344be5743e78ed8c5af8d1f7c54dc4f49c3dee106de40d23b1ce01",
      "node": "203.wake",
      "snapshot_digest": "506bb384ee21193ce27a741aff559351a704e6c641004ef89c69a2225f9ee051",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-24T23:44:15.722862+00:00",
      "head": "f832419b178eb0635ffcc15472ef1a15f47265ef2e31f365db8c5f817c702e1a",
      "node": "300.wake",
      "snapshot_digest": "2b12523583d81a3ef6dc22fd4acb64baf3b541a06d8c6116ea894e4d70a2c4af",
      "version": 34
    },
    "301.wake": {
      "generated": "2026-10-25T00:06:55.198216+00:00",
      "head": "68b8ad788b26850d495da541a966b8c99859ac10e5626817514f40e7a491c448",
      "node": "301.wake",
      "snapshot_digest": "c6b72b87f94ebe437667a0217c7fbd119cb79571993bad126605db5b243fc128",
      "version": 54
    },
    "302.wake": {
      "generated": "2026-10-25T00:09:32.681620+00:00",
      "head": "520368b1901b0bda851a25ac337150075d8ef3e2b3003428e7d1ec0624051c71",
      "node": "302.wake",
      "snapshot_digest": "7a3205f861e70c837912abc454bcdde374f5b813434ebf3c807f6ddc02ef2608",
      "version": 32
    },
    "303.wake": {
      "generated": "2026-10-24T23:46:06.530833+00:00",
      "head": "a1b822e2030e264c9b52190ab507e80cb9d74ad1211876c33c7084457c095735",
      "node": "303.wake",
      "snapshot_digest": "3df45e4b9d24547cc23b3fd5960f6744b359526c9e613cf69ae3a9b03048d473",
      "version": 49
    }
  },
  "version": 473,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d63393138323764313739353134633935.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d313031323861303438366563346434/31.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d726573706f6e736962696c6974792d666f726d/6174696f6e2d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
