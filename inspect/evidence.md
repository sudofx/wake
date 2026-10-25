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
  "generated_at": "2026-10-25T22:13:28.630358+00:00",
  "head": "snapshot:cc187d260f417d2b3216166aa6390f88d075ecb82d50b8f8350c1b96ee6f7dcb",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T21:57:57.934734+00:00",
      "head": "da59419f2b055f13d9c39ffa0fa8a1eda7cae118a9e00c7e5e9a0ee076e037b1",
      "node": "100.wake",
      "snapshot_digest": "75fc9e534ae63c6297c08d3f4df79981641e0b7b41a90f0a392af5a686ca7eaa",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T22:13:28.630358+00:00",
      "head": "bcc4b78b7ac71abb1f56c4049a47211b48642f258cd097594706ea3d927e6c37",
      "node": "101.wake",
      "snapshot_digest": "e723994ea2df39c5d16b4ae7cde73e509c0a8958ffc079066db92de6b449f95c",
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
      "generated": "2026-10-25T22:12:29.239604+00:00",
      "head": "b93240fd046abd327aced762414303c502f5058473fce88f0537ad561ac6060a",
      "node": "200.wake",
      "snapshot_digest": "349022efaadce498177abc94dc70953f1ebcb67aa097a77bf7071c732a5aa208",
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
      "generated": "2026-10-25T22:12:17.045156+00:00",
      "head": "886bfaf26326d3250874a151601632a8f7b2569671c67dd758b68c366ccefbef",
      "node": "202.wake",
      "snapshot_digest": "94029748262d9f9287e703b42aee58f1435eb4c71ebf2665d8a896caf582d189",
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
      "generated": "2026-10-25T22:10:42.946245+00:00",
      "head": "0b51912a19cbaf9a942222b9dfe3410ef9e83c3972126b4db1d1b6e3f07db70d",
      "node": "300.wake",
      "snapshot_digest": "7deaeffd21bcaa63f521df4192cddb4b92258191e2ae7ef8e0b0bd9b6a462fdb",
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
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d37653835316266393836393234646336.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d31363266386166616362326534393936.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
