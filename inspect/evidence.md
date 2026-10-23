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
  "generated_at": "2026-10-23T08:01:36.341894+00:00",
  "head": "snapshot:f9b09be5bcd47dc549fdb1cf272afd14dd8b22912c9874155931083033ff2688",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T07:59:24.740437+00:00",
      "head": "dda9712836cd310c13ff9a47d361365174cc3ed4827bc93275500e27e20afa22",
      "node": "100.wake",
      "snapshot_digest": "a9f34c73f1ba515c6f6c4de7af937ee9f5728b2e05e35098c3d039069c630b89",
      "version": 6
    },
    "101.wake": {
      "generated": "2026-10-23T08:00:17.471491+00:00",
      "head": "95e89fe0656a925fb2c8b2c44440272c542c9c0ffda76198b4b41e4967b06b99",
      "node": "101.wake",
      "snapshot_digest": "edcc60cbbbdeeacc42b037eefb296354e46d4a7432a09f1757e186e5ae958a31",
      "version": 18
    },
    "102.wake": {
      "generated": "2026-10-23T08:00:51.708549+00:00",
      "head": "5e66013e08756624185c7cea026c490b9743bfe96cb95f9ecb0411099cd13bf2",
      "node": "102.wake",
      "snapshot_digest": "05a6f4ffb94bc049f9734c5fec8fcd4aa04cc849fe19562b757c3b8ea85aa92e",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-23T07:59:46.079074+00:00",
      "head": "007b754795a972b95d64f67033d9f800274f68c2005a52540de7b79606f43a9a",
      "node": "103.wake",
      "snapshot_digest": "0a2b691a92d2b278b0636fd776bba45a55c589fa9d70416d53835b767e551934",
      "version": 11
    },
    "200.wake": {
      "generated": "2026-10-23T07:57:44.636034+00:00",
      "head": "9036e44f946540692e369ae823501c28eb542e078b71530da86e9af2c44c4cd9",
      "node": "200.wake",
      "snapshot_digest": "f84f709c81d63c0545b47c90d4198b502ef0d52450d1e5a0034ca230a5f57409",
      "version": 10
    },
    "201.wake": {
      "generated": "2026-10-23T08:00:34.644284+00:00",
      "head": "5a07f5f91e5b5aaf59410f8227f084c1314f8429550d44b5b333a934ad2691ac",
      "node": "201.wake",
      "snapshot_digest": "88d604c04644893aa8e58d421c5b6005a486ac126bb55ea9fbf8f8b865469b99",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T07:59:37.361190+00:00",
      "head": "eff1d55866a23141bc4a8b34698037629d4f27d66ae1e64cb25f48ff4dca2642",
      "node": "202.wake",
      "snapshot_digest": "acaa02fd7c621179bb045e6589129feebdc7bb502afab92cb11831cd7eed2a7c",
      "version": 17
    },
    "203.wake": {
      "generated": "2026-10-23T08:00:39.225404+00:00",
      "head": "e8740ffa66d5fe5ee77af4f19e5694bfb5b8af3c3ccfa316ae846c21e851b494",
      "node": "203.wake",
      "snapshot_digest": "c2a85f3a2197a529a07408eac443e26faac6601de7f7ce3b6c360dfdfbf01bca",
      "version": 9
    },
    "300.wake": {
      "generated": "2026-10-23T08:01:36.341894+00:00",
      "head": "a0de1ee625eddf6617b12680deca46186648d352ba252d3dfb82671eb6c26a19",
      "node": "300.wake",
      "snapshot_digest": "d303d29543b697761fd9855071154bb4a518dffb0707d6826e221f8f506b9f28",
      "version": 8
    },
    "301.wake": {
      "generated": "2026-10-23T08:01:08.269975+00:00",
      "head": "da532b18b655c8962247e1d7a6581da7f40dafdfdb180ee7c3d003b5c3e58861",
      "node": "301.wake",
      "snapshot_digest": "232965186e82bf80b423de0021fca18867da00eb303e3776c1f4fe51477ef6b5",
      "version": 14
    },
    "302.wake": {
      "generated": "2026-10-23T08:01:31.689287+00:00",
      "head": "f1f424f433f0edf608b10566262307b7ba451d24667eada3456d0f3fc32775f2",
      "node": "302.wake",
      "snapshot_digest": "f9099aa00b66a4c68b964daed4783e1970e32121e296852fe65becfab8d7bba5",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T08:01:27.550313+00:00",
      "head": "db89664f9c20b9ef0927a7517e2b86d0dc6af362aa1fa83e1ee19336c0c0b9bc",
      "node": "303.wake",
      "snapshot_digest": "fc3eefdd055867b695d21fac5cc88cef3e29d620c4a38b5aa9ca91712d0550bb",
      "version": 21
    }
  },
  "version": 155,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d35393431346339663733613134316533.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d396433643866653766626265343264/33.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
