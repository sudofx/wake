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
  "generated_at": "2026-10-26T06:48:30.454812+00:00",
  "head": "snapshot:430aa52d8534db18901ff40113783aa8e2bb842e92c6c11b72b9f98a0320939d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T06:42:04.766454+00:00",
      "head": "755b0c5bacb3b540ad155dc88d8d3763c560cd3d16554bc6a17937bb2e2ba0fe",
      "node": "100.wake",
      "snapshot_digest": "1b98046013adacadc5170f3ee07a437eb19419145a831dff8539c675c94fb55d",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T06:40:18.927787+00:00",
      "head": "3ca64359c4f10da46b8da32d00dbc2c928a65d27320e241bdc655b65eed7f92f",
      "node": "101.wake",
      "snapshot_digest": "6f78914f191bbcbeb0de214454d192d8ca31eea431e0d9f58d27285a6073cb76",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T06:48:30.454812+00:00",
      "head": "950ad7159d54616a91620702d98e13be294ba95d65a50a39ce04147594930de5",
      "node": "102.wake",
      "snapshot_digest": "d0023cc616360592e405eba8a445f6ef1c5b5feeb7abfc7383589982f27b414e",
      "version": 61
    },
    "103.wake": {
      "generated": "2026-10-26T06:37:24.759485+00:00",
      "head": "50070ab8a1c6b86fc3f68cf9d5e87ef692666adc4c572413f08a0022afcf33be",
      "node": "103.wake",
      "snapshot_digest": "7086fef67dda903a78b63bcbdfaa8963558ade35e4cf05dd662e646937f81bb9",
      "version": 43
    },
    "200.wake": {
      "generated": "2026-10-26T06:38:54.678909+00:00",
      "head": "3b8d58d8f0f04b10a84c8db96c0229edcc723b84fe45c82ae59999f091771c93",
      "node": "200.wake",
      "snapshot_digest": "b4a17d92c192a8b4ff477492fa3e00b1b61f7dc7fd14772f96537d8310ad24fb",
      "version": 38
    },
    "201.wake": {
      "generated": "2026-10-26T06:41:45.752741+00:00",
      "head": "10b67aa374a8857a5fa98de4fac9010e86a18a25bb88e7d5e2301f370201433c",
      "node": "201.wake",
      "snapshot_digest": "6b8bfd327895d0603e8f91c528f0a3ebd6b6d11833933a208bb2861670832d9d",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T06:31:41.081245+00:00",
      "head": "46a129b087c1ebdfb9a1bb0c1f8f696d59db5b601894c2e5cbd6e1409b5c05ad",
      "node": "202.wake",
      "snapshot_digest": "c9c4b9663ea4d51a6fc6ec4055a1cf8b307e34806803d6bf34ae9261cfbb3e42",
      "version": 57
    },
    "203.wake": {
      "generated": "2026-10-26T06:35:42.937934+00:00",
      "head": "150470f1e60a784f33ef15c3b20dd69399dc7f7c8ad55e9925c5ad6095483d56",
      "node": "203.wake",
      "snapshot_digest": "bb532b9468e3730f57dfa8676ec644e55e5b381b34b8281b20fd1db28d50e068",
      "version": 33
    },
    "300.wake": {
      "generated": "2026-10-26T06:39:34.482922+00:00",
      "head": "82732c3de43ca4a2d80ff7fb712f22204fdde4356ef51e3e2526a33f50603d4c",
      "node": "300.wake",
      "snapshot_digest": "0b0dfd8c9dc8651a5e34c1cbeeafab73c8835189c480396d8c9aece7de1e3ebf",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T06:43:11.867864+00:00",
      "head": "70ab8a2760b79de3400108961470f465ee4b8e9702dc46c719bb28d361f7c328",
      "node": "301.wake",
      "snapshot_digest": "1011d1ca996c35a99a938ab58ea634e48ffd438330bee5267c149167f956bf93",
      "version": 60
    },
    "302.wake": {
      "generated": "2026-10-26T06:34:18.062403+00:00",
      "head": "b55a8e4ec27bb79c879cf5f2d1a2b4771ab0b1238e575fbcde9bf9bc3a86858f",
      "node": "302.wake",
      "snapshot_digest": "ca88cd5ab7928aab0206401f484aadb5693924cda782e675d02a91e062310dc8",
      "version": 45
    },
    "303.wake": {
      "generated": "2026-10-26T06:39:13.248191+00:00",
      "head": "70ec25721170c51a8ea71f260799c3d15b2c7e322cd3d4b0a03f195aa13b59f7",
      "node": "303.wake",
      "snapshot_digest": "9705294d1d51870953788fb6cad2b5e75fabb130c8a51722bad26cabc6cc5ac6",
      "version": 53
    }
  },
  "version": 548,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d65356665376638373561353634383534.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d38653239376265303737643934393836.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
