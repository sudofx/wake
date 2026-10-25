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
  "generated_at": "2026-10-25T14:23:41.685216+00:00",
  "head": "snapshot:9d41c1e302f227c05a98e72d5e2db3f3e1ee28203a2fd38b22ba42041a5ffc62",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T14:13:12.013308+00:00",
      "head": "4b57a0bed3e3b870e6f7872a909de69837989380c86f81cff3f140a3cdd791ee",
      "node": "100.wake",
      "snapshot_digest": "2f370bd0b8395be503e415cb5a8a30d56ef67b0a7257efdddcea7e2b81dc848f",
      "version": 27
    },
    "101.wake": {
      "generated": "2026-10-25T14:06:08.783971+00:00",
      "head": "cdfedadcd63eb47d5357e17527451ffd6d75c4db254403d5e32298aa56649b22",
      "node": "101.wake",
      "snapshot_digest": "89cbf1fc8c82a2a2d381d4fef89bd93d1f76d1e4ae27a703f28db83fbe53dd6a",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T14:05:13.625146+00:00",
      "head": "1de5c423fb93381fb615ddf2b595b6c94e9454d2dfb72989a4c23edc4d85e092",
      "node": "102.wake",
      "snapshot_digest": "02c867018ef95363a70aabd4dce3b1eff19225f35671c419f7649e8eef57ef1f",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T14:23:17.235455+00:00",
      "head": "f5ef8c7eb7f82b2107f3002015ef659aedba9167ab20eb2c07a3a0a4ce9621e1",
      "node": "103.wake",
      "snapshot_digest": "98bf7c7efb5c87b785c03dab175a90adfcbe1373e9693a336bf8599e28b0b92c",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T14:20:45.083746+00:00",
      "head": "9322657934a6f711564c006d95011f92871a3688bbf439c1f757e55a2f72f382",
      "node": "200.wake",
      "snapshot_digest": "71e09dc8c9f82c808b3d2a0e0cf445e2f8076c67d7ec2995b3408dc1f64ef066",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T14:02:57.263285+00:00",
      "head": "c86e551a42600f1e4d309171ec1ff82249bb89323b53734e75bcffe85a3a4ace",
      "node": "201.wake",
      "snapshot_digest": "4bf5cf444358966baa2b3bc0915d6023bed45dcaef546c45c45fa28b234f1a38",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T14:20:34.867846+00:00",
      "head": "5cc5ed77a4c19f37993220920cadd3da9cab1cb9f85c12bc1ad39b16a55ee8cf",
      "node": "202.wake",
      "snapshot_digest": "cec7e9fb61b06a467ef9c49f6432cd3040dea0b8031fd866c83077e031549923",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T14:18:41.535102+00:00",
      "head": "6295a39e04338dbd534d4ba3731b69551ca896baaeb01f6f544a897d01251cbb",
      "node": "203.wake",
      "snapshot_digest": "5221157587fe8b32faae31068ef02093318ad44771a10bc0fe5fe5506485618c",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T14:23:41.685216+00:00",
      "head": "699b5e6cbfd9330e71620a3b646b992c8134fbb85784811c9f5d809e5b83f098",
      "node": "300.wake",
      "snapshot_digest": "ed62d254e94f95f99c789fe3ed4180774682351797c862ace807a84a9d8a9471",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T14:16:04.554151+00:00",
      "head": "b7e95ba5fc95f3e11a3ef1dfa82cf6bfa50a6f40a4b2fbc9eddafbc72d22de86",
      "node": "301.wake",
      "snapshot_digest": "6bc614e1aef6ee79b16fce172c0debebf711de84a7c433fdac16611717921675",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T14:14:19.695545+00:00",
      "head": "5317bb32e2810dccd6baa414aa83e5038b50d191aecb24a074570b653a57f0ba",
      "node": "302.wake",
      "snapshot_digest": "14f52af31f18a44ec0bdbd43db736813b658ca849a7f7c076a44f7480a855e23",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T14:00:38.869758+00:00",
      "head": "efaa578f006cb3e5bbf297a3a629e194b328878535b483fcd1d16cfb0b85bdc7",
      "node": "303.wake",
      "snapshot_digest": "71b855ba1f50471bdb160113df1144ba31f3dc232399ce95226ee79a63e23e2c",
      "version": 51
    }
  },
  "version": 508,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d38373866373363613861633434313330.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d38633836356636363031313934373762.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
