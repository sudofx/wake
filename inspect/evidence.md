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
  "generated_at": "2026-10-31T05:56:17.849998+00:00",
  "head": "snapshot:afa42f862e74598c60334a3401dfee2355a6fdbfce8e11be6fdb36ba219d942b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T05:56:17.849998+00:00",
      "head": "8e161d61092f54f6a18f492f5164972f1050ebd4cecd35ca919b82d367c199a6",
      "node": "100.wake",
      "snapshot_digest": "a9d03d45c5be6db7a621cfead6348c70fc6d8cdd6095093cf48705b6f0d17474",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T04:48:25.031657+00:00",
      "head": "9f48003801e1545c1ba002b15a98afe8e5de1bd9245b653f0d1233b5922580bc",
      "node": "101.wake",
      "snapshot_digest": "20a1ce5cbf2a44b3abcbcaccc819d3508e440e8615b650df6e129af5df033acf",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T04:48:13.093369+00:00",
      "head": "669263c0685c3b6639f4ddd35b064b7499173c4c319dbc02aabbf55e14b5002a",
      "node": "102.wake",
      "snapshot_digest": "60b5d323a4589a6ded37c81f3129768609d8076d916cc61d5b33b2b5440b7336",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T04:48:29.433282+00:00",
      "head": "4a6da62f80492e5f2a8462480d785ea4e3518c299f2497e33c964cad4a66b249",
      "node": "103.wake",
      "snapshot_digest": "393c09edb64a59e659c3962813829be54f09301711817e032926d9ddb03d4cbc",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T04:48:28.514448+00:00",
      "head": "0c310137b8f4a7c87e4591a2505bef644b024aa81f8193965977cb84e911cabb",
      "node": "200.wake",
      "snapshot_digest": "25f9a9bad2f264b3597f3fc0851326f7943fa189614d507434a1544fdd74271c",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T05:52:58.121600+00:00",
      "head": "d3049924a58714a91dad340ce7fa7d038b5ef6f1e033e2ddaf16f4f3c22d85bc",
      "node": "201.wake",
      "snapshot_digest": "e64b3599d263312dcbc03da319e2abd3dec5558f20d6e7c09c84f2312a9d432f",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T04:48:11.431271+00:00",
      "head": "1d8796051195573096e2e1478aa4703d6cd6f4e9977ae109dbb064c76fc5745a",
      "node": "202.wake",
      "snapshot_digest": "40e6c27203bb8ea5bc7c1657d75034135efe07e91a7159e514017ea209ecb441",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T04:48:16.654044+00:00",
      "head": "ea15f7bc9bdd7a6a07ce20ca2898b06caebc74474325c07520837df675ed4399",
      "node": "203.wake",
      "snapshot_digest": "db90ba888d6735e5141c8a05a1ce5694703d4c518474f2e0d899f65bc296f215",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T04:48:38.814012+00:00",
      "head": "694ee1fba2d44aaee9fea7fea0407c0b4fddb1bc52379e9d4e53fcbce8543197",
      "node": "300.wake",
      "snapshot_digest": "e9086deb25c020d57c39537bac279c73a8c5b859ff6d2412c2df8eeeb731d01c",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T05:54:44.797864+00:00",
      "head": "e6416d4e62127a2ed0ee3d88068480f7c552877910ec4b3c6d92840afa5b0b7f",
      "node": "301.wake",
      "snapshot_digest": "865801dcc93d9e42c4509ee397434d2c3624c17e21ec7e19f4399e9e6cd5044c",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T05:50:57.787849+00:00",
      "head": "94b9f4dbd5916a59dc2cfe42e2e8aec17cdf831e578927ef011c081f399113c5",
      "node": "302.wake",
      "snapshot_digest": "e20021f2527194aaebba6391dad8dcbbc4a9dd73ff0f60787adef9ff1cf11b26",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T04:48:25.234587+00:00",
      "head": "64917ed2df8899d372be7b35b921867a7f125977d8c602a251938c7320abcc1f",
      "node": "303.wake",
      "snapshot_digest": "181ed8b30ac9f44b56da537de7a030b5a343357e76f3ec100c4f452880eafabf",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d36396464653334396637356434306436.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d37666563313165316565623634363262.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
