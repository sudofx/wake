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
  "generated_at": "2026-10-26T05:51:05.023960+00:00",
  "head": "snapshot:6803bcb7d40561fdd4269bd6c17073ffa8550a5fa2f68acb4e89432645f237e7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T05:50:59.006426+00:00",
      "head": "fe1be332e317e5c45ea8aaa4d6e55b9159f4d137ac90cf8b5133765f57ce0d7d",
      "node": "100.wake",
      "snapshot_digest": "de1e8365cfcace9707b0381aae7c2e10dd65ce974a9b928b4c0b9ce945957fbd",
      "version": 29
    },
    "101.wake": {
      "generated": "2026-10-26T05:50:59.629193+00:00",
      "head": "9a57e2d521c2ab9e8b197cce3728e684da7b396beea0cedc3d5c9f24a7337d23",
      "node": "101.wake",
      "snapshot_digest": "07ba9c07f4dec90f3ccc0b8eb62186b509192640bd41e5507dc8d08d1f5d1365",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T05:50:54.833928+00:00",
      "head": "8662e4c3d25775ba24187b76e647d77b9082258b94ca3b197bb940d61612e8cb",
      "node": "102.wake",
      "snapshot_digest": "460490f2f5886e7e7d2caa0a3eef0f2b9f2b01fc92711366c59d40b0ef669701",
      "version": 61
    },
    "103.wake": {
      "generated": "2026-10-26T05:51:01.102488+00:00",
      "head": "833fbcd805806339f7f71f5071f3fcba40f8aa6d664b773a6600cc42071b8d8c",
      "node": "103.wake",
      "snapshot_digest": "13eb09ce6811c3dff4816f48e8a3f28d5b18cb2e32497199e56e75bc89930c8b",
      "version": 42
    },
    "200.wake": {
      "generated": "2026-10-26T05:51:01.430913+00:00",
      "head": "3782a0d65285250f628a9ccbc5327e10ce6fc1a4288b67a1e4f853f3f3f15253",
      "node": "200.wake",
      "snapshot_digest": "468a15388337dce56000130acc556bfeb6e19ac7998e1587216d0ddcea56693f",
      "version": 38
    },
    "201.wake": {
      "generated": "2026-10-26T05:51:02.094837+00:00",
      "head": "0a572bc123bf6bf037ae86a11e311ac9ac8ab9d35c3efd68a3f62f3a61598cd1",
      "node": "201.wake",
      "snapshot_digest": "8ccc78da764616676ecb53af311cf79442fc65305b833d24a7cb6957e1bc1d88",
      "version": 43
    },
    "202.wake": {
      "generated": "2026-10-26T05:50:57.895177+00:00",
      "head": "05e594209b46ced210156828cc4cafb6d3d9fe683a362c79d423c30225d2cb7c",
      "node": "202.wake",
      "snapshot_digest": "63b7cff2786327240e6eeedb16e7aa684593837f794441637fe33aac3d966a6b",
      "version": 56
    },
    "203.wake": {
      "generated": "2026-10-26T05:51:00.432615+00:00",
      "head": "9e17a91b1a743f8fe3bd9d77e6d66f18df307d864528d0bca9d01910befadd08",
      "node": "203.wake",
      "snapshot_digest": "8a8a0da2b05fd8b3f93f054022d8ef99ae60bc354fbd500d431663e34b44e1dd",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-26T05:51:00.501591+00:00",
      "head": "cc3d4e376511d140db155eef5750d55bf16c39a9c3f8b85eebcd1748c84f34ad",
      "node": "300.wake",
      "snapshot_digest": "5473b48c363986b91aa0019d0080b866c106b9969972155e13791e2f0c884ae9",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T05:51:05.023960+00:00",
      "head": "8ec6b7cc722a28a11cfa9226463bff310bec4aa250d3dfa979dabb04c24bb5b2",
      "node": "301.wake",
      "snapshot_digest": "e6b12a3d2c29e9b5969a5f42dd3122d7460a8e9ab547b86c0af096a716de63da",
      "version": 60
    },
    "302.wake": {
      "generated": "2026-10-26T05:51:00.001975+00:00",
      "head": "3878cf5870bb85fccbc42d110eae0965a5426756fc66ac66e6fd65e9c8b74dd4",
      "node": "302.wake",
      "snapshot_digest": "7371461025d08c46ba70287ffacfdd05f1e6a3d31a216894e371dc22824342ad",
      "version": 44
    },
    "303.wake": {
      "generated": "2026-10-26T05:51:02.390884+00:00",
      "head": "d9e488f108f0fc499f6077ee247fc1cdfc010ed818c61affb3c063ea4e96b68c",
      "node": "303.wake",
      "snapshot_digest": "520b1d849ce23b98eb841e5e85526dbf9e5d5b252d8d8c24d83cd9d4f202c864",
      "version": 53
    }
  },
  "version": 544,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d613636383232343130333963343235/31.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d38353364353964396564373234303461.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
