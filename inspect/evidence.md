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
  "generated_at": "2026-10-25T22:09:38.673297+00:00",
  "head": "snapshot:e4655106f5eb505a9f9a62c2381c01498b962eb6673768d6c4b0a02da55c30da",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T21:57:57.934734+00:00",
      "head": "da59419f2b055f13d9c39ffa0fa8a1eda7cae118a9e00c7e5e9a0ee076e037b1",
      "node": "100.wake",
      "snapshot_digest": "75fc9e534ae63c6297c08d3f4df79981641e0b7b41a90f0a392af5a686ca7eaa",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T21:56:51.432440+00:00",
      "head": "4bfe30d647752ddac5f9bfa56f63f8201dc023ec0babf6e39871d89feb1d0ac9",
      "node": "101.wake",
      "snapshot_digest": "aa44244eb683bb39ebec4ab061c3566fa0b224b2e9d0ef0ff1e569abbbb86073",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T22:05:34.929133+00:00",
      "head": "a085ae11b32b564e86dc7d140c9af1ee5fae301773a000c4458e2db589aa64a7",
      "node": "102.wake",
      "snapshot_digest": "5bdeb55879155acc918103508af23650bac65e9683ca284c49fa40d08912241e",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T21:39:00.057870+00:00",
      "head": "418c62fafd6151c36f6d797212bd0af67edbaa055cbdcad5c2e7c0b8fa538e11",
      "node": "103.wake",
      "snapshot_digest": "318c34c8a14ae0316d696c174b379d26d5612c987e26893e34ff70bff8ce2f7f",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T21:38:58.941141+00:00",
      "head": "cb57ed2bd0760d916f991cc6af5ea651f42dd11327b52d1caceb91423e178a32",
      "node": "200.wake",
      "snapshot_digest": "16bc38711214521a4c1c6824d8f7e3a5dc054131c315a2f2b48375cb22895b8e",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T21:38:59.572889+00:00",
      "head": "96c238fa209dd176120f98bf16f590c2323f694a5a9284b2b5c0053aa50ce6a4",
      "node": "201.wake",
      "snapshot_digest": "126e9d2842fda6cea5faba7efe0adfd30144f35d7fe983dc49971313995c65a1",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T21:56:31.017087+00:00",
      "head": "473e2896ea964bc8c03796341e2b33386bda98ef7f8af7b4d755d73ab16f11e4",
      "node": "202.wake",
      "snapshot_digest": "c104732c087f71414bd199df8331d121a1484929e8bd1d0f63eea899b3f8fb25",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T21:57:07.780466+00:00",
      "head": "5f61cf24cd1e302bc5ce8dbbde69d416a4bc25b6f340ebe5d0bd44c5c44f700c",
      "node": "203.wake",
      "snapshot_digest": "af4b873e77a8f00acda3aa212c4cfd4a1f6d5291f4301bb8cb9394002c5ee38c",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T21:39:00.057937+00:00",
      "head": "ae11ae1bb978b879afab307c7c5a3c55364f35390cfc1687938af1d078e4e4f0",
      "node": "300.wake",
      "snapshot_digest": "0e1acd6d306aeddfabacc23a09af7bdec0a699146998c9121d3ebd4e1cd93fd9",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T22:07:18.176595+00:00",
      "head": "a6aafcd1666f4076713cb8233aab393bb62c40299bba3ea363721f153e06f711",
      "node": "301.wake",
      "snapshot_digest": "008944ee3868d5ad254ce3989daec4b1619d6f122c58ec66004cd33b40c41c96",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T22:09:38.673297+00:00",
      "head": "5ced1eeb4040372e724a305ab0f8c47dc26752f91475d4c525359fb4cbda5e23",
      "node": "302.wake",
      "snapshot_digest": "a1acb52c158e6a5a129a2c974d093842b878a0eaf1d4c14aea9df2034a78e338",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T21:39:02.508552+00:00",
      "head": "9fdcd5038d8d135c5e974e8bbf5562ec6a5ed9e051c4ad0c2d70f834f4cb6dcc",
      "node": "303.wake",
      "snapshot_digest": "77fbf19edb6f63f6d5647f1fee2433e79cdb8cd4fa526e1f9aa2e59d0254731e",
      "version": 51
    }
  },
  "version": 510,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d38663161353964303166636634323633.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d37366462653163393238353734393130.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
