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
  "generated_at": "2026-10-30T07:47:58.627195+00:00",
  "head": "snapshot:f17ca3eed47422d5e460d164288f6143792639b09f10ffc4618d6c3f557d2233",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T07:45:35.198384+00:00",
      "head": "2861d80b61c166e8c5d92414b48440757ff46e3b6295abe3d6abc28dcea7f838",
      "node": "100.wake",
      "snapshot_digest": "991cce177a9f95af6ec627da597afad7a165ec75badfa84fa797b54fb01506ec",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T05:42:36.550441+00:00",
      "head": "6353ea752248cf9196dad019343bee2024f7214ef69d5fd01627b582af5a3198",
      "node": "101.wake",
      "snapshot_digest": "cb50e221a93b72971657e4a44729fbd161ffa7aa3919528b8e19f646de337704",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T05:42:27.387635+00:00",
      "head": "4aa2438ad000a3d8d22110ca81b485b74d3b75ab17407763f717621097d40fb1",
      "node": "102.wake",
      "snapshot_digest": "9e15b525a123f6e7434666e96f94f0c2585612b167f0d9e561b9be8f8670750d",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T05:42:38.789639+00:00",
      "head": "83c755adc0954e2b7fb6215b62bde9d7be925ae9e135216ea43335fa6b97257a",
      "node": "103.wake",
      "snapshot_digest": "ab50a00253789e8d71439bde0c9a281b884839810ff5e59dad85240a99549e48",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T05:42:51.727864+00:00",
      "head": "81f218ca8f175646fcd26602bb10125c49891a0cadc3dda07aebaf619e982273",
      "node": "200.wake",
      "snapshot_digest": "b9f8255e755827f60cc074b3c1458c8ae00442579e298848761af44473183373",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T07:47:58.627195+00:00",
      "head": "95e5b83eeeb2e7339a8b7f0b64b7df80d3c8abb6b8ba32f4918e1a97741ddc51",
      "node": "201.wake",
      "snapshot_digest": "21d26d326e64c555e3c5966670ce91154fd98c915ecddc0c6b99d104b1578268",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T05:42:34.246755+00:00",
      "head": "c7d9fbaf8d6b492f30ac101adb6eb5fe8b97695e771ba05fb3dbf90edf68e29e",
      "node": "202.wake",
      "snapshot_digest": "8788e2e99798915d0d8966140412e367e2bb62cfee70b778cae95ce4849b1c35",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T05:42:35.009233+00:00",
      "head": "5cbbc4bb41f9ab0c85eaa5aea0693720dfeb0f7bc3fab13ae3027180573d2def",
      "node": "203.wake",
      "snapshot_digest": "8af2d99ac4801f06dd54d4a97dcac1a3b861f5176c41d55d2869fa8faad47633",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T05:42:42.705345+00:00",
      "head": "c12dd770d15b6c307100c5346cf5195b5ff99da4b153904741cb63a4af191dde",
      "node": "300.wake",
      "snapshot_digest": "48dc979774456e91f34461542b18b58d5e488e6d0196435d90b07b4551426567",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T07:46:45.383819+00:00",
      "head": "f20edd406125d178e908e4c65d34c1dcd2cebbe2d4fdc7e8293513b1e3d4f235",
      "node": "301.wake",
      "snapshot_digest": "971f5b92e28a52c4ae9025b827e76546b98944954c34d65da6678fd2d25c76a8",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T07:45:37.611017+00:00",
      "head": "36f788b1c82fc23714b16150bfbe43e393e3eff65c006330cb9258aab180e40b",
      "node": "302.wake",
      "snapshot_digest": "3a61b1669a675a23f10f8094ab4416b065e0b6396e62a8c345eb861f222b0d46",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T05:42:27.416172+00:00",
      "head": "e7894ba90c41627a0d3d7b1e3ec530aaac5692a7e3f549ca4e261d5e357aa41c",
      "node": "303.wake",
      "snapshot_digest": "2a772de4e1b915789b647bd8cf9ad7b4e496113526fe069dc2416066f3fdb676",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62633466366266633439353034626232.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d65613766623762376537353434343930.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
