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
  "generated_at": "2026-10-25T16:27:14.851964+00:00",
  "head": "snapshot:a49edcc72c022a639608e0c2cd7fdb5487cc09956e7a35f6825b358217b9840a",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T16:18:41.907214+00:00",
      "head": "9cf0672f83fb0cf22581a13f6c6c6c44a8f724981cfad96fd4d74e2ad00b0a87",
      "node": "100.wake",
      "snapshot_digest": "ca5da4611e616a6120f2dcec5072cd4ddcf8c2ffa74f5be5eea4d61ff2a3d212",
      "version": 27
    },
    "101.wake": {
      "generated": "2026-10-25T16:20:56.957348+00:00",
      "head": "929dad0f096bd1dd53f0a1bf45c4ee65b6f1b883678823303714e6a6c1eee613",
      "node": "101.wake",
      "snapshot_digest": "e15c38f0932bf8b1b788c3fe0ded0c5140f8d9b7e952a2b8bcd6d494e13bf9d7",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T15:53:15.368140+00:00",
      "head": "4af706a85578fb1724fedc89a8ce09df402b1fe8b57cd5c408cd06b7258d52b0",
      "node": "102.wake",
      "snapshot_digest": "e59911c9ebe726246c9329e1a181af1731f41ebd284b20bf725290cc48e279db",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T16:16:08.208690+00:00",
      "head": "f1ea795180d7a024547bb230d495957bb9aaf463b81eb6c4faa160f0023a95a1",
      "node": "103.wake",
      "snapshot_digest": "a8e2db90efb9b2c1e303e237092190c64aa0bac0c9f9073245fa2458abba63a3",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T16:23:10.843783+00:00",
      "head": "6fa265d3548bd08067a879eef50323c023069df02cc859e6ee8b30784e4f77bd",
      "node": "200.wake",
      "snapshot_digest": "8ba8681f7973666cd30d5b00efa3ebf3a2b947f24f0a694b019d54e36266d207",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T16:09:05.766769+00:00",
      "head": "eae1dc141d7ddc0b23478db888ff65e8d1f33b8d681099f507cb442445f85800",
      "node": "201.wake",
      "snapshot_digest": "cf110ff1df4e9a8faba5279ba15a25accfe3284bf83a850b0026d8c006894af3",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T16:13:05.695469+00:00",
      "head": "6e01aabbe7904543a4184935600d470022ffaf2224bab31fec2d67d41e1aa68f",
      "node": "202.wake",
      "snapshot_digest": "556bb02cc3a6aa4418ed57f24e8bda1fa21b154f102773000e1dd1ada3de8b27",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T16:27:14.851964+00:00",
      "head": "e9fd68132f4125e5d28078f73aa23c56eb66b322cd344a0b90a2836cdb170151",
      "node": "203.wake",
      "snapshot_digest": "d980a36f5968155efaff87b65242a2eca5a7ca8b3136fec1af8b0c8e0c2199e6",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T16:17:49.887614+00:00",
      "head": "b652adda0a434e1ee6543859e68b2ef1813b47cd7ef7865d69f6a8f869e259b3",
      "node": "300.wake",
      "snapshot_digest": "e3d3e3ec652d9003c4682a79ed9630864463567937f8a0d492ee6c435b0230a3",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T16:23:59.487906+00:00",
      "head": "7435e54c4f7785100d617c40a35fa192dd297f8c4e71bbb529c7fed1f2bf48f4",
      "node": "301.wake",
      "snapshot_digest": "3826e45319fc2427c1d76ece6342ea2c08735696ad214f24902b538ea050d07c",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T16:25:52.206424+00:00",
      "head": "af62cc5bfb3c25ca1679e6a58fb94cf8a86828cb2ab539815023829d78bcb0ee",
      "node": "302.wake",
      "snapshot_digest": "fd70f4b92a3e569ce6c63758e6c3eaaa867b26383c60769104e3cd8663d5604b",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T16:09:19.954372+00:00",
      "head": "448aed95f0e3b3d7172ba0829e3fef0bcafc7ef4194da83789633c570513e9ff",
      "node": "303.wake",
      "snapshot_digest": "9f550a9bd66424b46028af035c919ae8d0c2cab23fe4b2163717af02fee5d344",
      "version": 51
    }
  },
  "version": 509,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d63376535626233336561346534633339.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d656163653435363936346362343563/62.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
