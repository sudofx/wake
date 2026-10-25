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
  "generated_at": "2026-10-25T04:35:32.492596+00:00",
  "head": "snapshot:8f5f4bd4231cf7d4e83374370fb884a19f060af8ad2b71e79fd4a22d4b8fcfd7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T04:35:10.317210+00:00",
      "head": "7f7e0bc1d5cc34ffe948d24b9f52b7e9119fc00bf452d0ec4d4e749dac5ce529",
      "node": "100.wake",
      "snapshot_digest": "c6c23f43cb00f1f211bcb69d948bc4be9fd9c52dd8d2d65744c27f0b4ad84c0b",
      "version": 26
    },
    "101.wake": {
      "generated": "2026-10-25T04:33:30.257229+00:00",
      "head": "159dc540d8dfb24b601f29758af670dfce1c262daca91854eb5723e748c2021e",
      "node": "101.wake",
      "snapshot_digest": "2516f1455c69034942310eba15d2a728406be55484cca6e65919845cf942ef6c",
      "version": 42
    },
    "102.wake": {
      "generated": "2026-10-25T04:20:02.590328+00:00",
      "head": "14956f9a59db1b6f0603a991f27dec253701fc69dfc1232119da1e230af8933a",
      "node": "102.wake",
      "snapshot_digest": "ba9a5ceb97affdf9066b81ed38bcb9ccf8bb63c402add12319e288cb54933f3c",
      "version": 55
    },
    "103.wake": {
      "generated": "2026-10-25T04:27:22.752474+00:00",
      "head": "6144375742e1e6e4d0601a300e59f4c459ab47d73ec26ec406297427c34327b8",
      "node": "103.wake",
      "snapshot_digest": "35b6cc09876794ea87c9e79fced43dbcaa81c962ffa0eeed41ca80526eb61080",
      "version": 38
    },
    "200.wake": {
      "generated": "2026-10-25T03:44:19.991347+00:00",
      "head": "8905447bede1e537933ed4bde7034ccc219867b8d423a38e9edd54732e24f5cf",
      "node": "200.wake",
      "snapshot_digest": "f34957c8ec5371a0d45720256feb8edadb8340f4bd6974ddd8f983e31cd00b3a",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T03:44:22.951784+00:00",
      "head": "9dce08aeae268ea6d77a333ee8614d0eb7777e807c64cef5b4de225c33c3692a",
      "node": "201.wake",
      "snapshot_digest": "957bef50a28dab76fde5758b64fd6116fa4e8a7d5422f7dde7a4b193f7bf8802",
      "version": 39
    },
    "202.wake": {
      "generated": "2026-10-25T04:35:32.492596+00:00",
      "head": "e3f1f7e1f3718944d9d83d2c2daa0b8296d438a38c4bf5c9ca7116c05e88e320",
      "node": "202.wake",
      "snapshot_digest": "7e1169b8e36c767d64b9fdf542c166afaaa2b033bcb515e649ef5b6f233fbdbe",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T04:33:58.604712+00:00",
      "head": "6af3855ed4160a140b6414db0f8917ce2a64903412b620a43ffc54f47b852265",
      "node": "203.wake",
      "snapshot_digest": "311e18c08d827be7f263dd58751f629ee1ecc62d87d3ef8ac25fbcf3d616ad58",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T04:35:01.158547+00:00",
      "head": "6a86d94bfd7861128e3911988dd66862e24675edab9b0cba33578092386b8699",
      "node": "300.wake",
      "snapshot_digest": "514c52eaa37b15478d60808b21c9d7fb734c6c6525c98585e33d888882f5a102",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T04:35:21.632939+00:00",
      "head": "64b08efca1e34add9cf7757785e41b7ba131b0c8fa369724a8a951bd987d6615",
      "node": "301.wake",
      "snapshot_digest": "191fbe84dd6649fed8b18cb3c7fe837a1c84373cedfa7df18b3541f1afa4f37d",
      "version": 56
    },
    "302.wake": {
      "generated": "2026-10-25T04:21:29.637603+00:00",
      "head": "81a4d89c012c5cf9ca8d70ffe1af77eac357b40c12882304c0517741aa4077b5",
      "node": "302.wake",
      "snapshot_digest": "05e1c29532fef826f08539340ca1e34b9e9bea4fc79ec467622b902465905467",
      "version": 36
    },
    "303.wake": {
      "generated": "2026-10-25T03:44:24.969656+00:00",
      "head": "4d8ab31a170d2eca465ce01edfb83bdb252d11beba6fc213cf051dcef28da65c",
      "node": "303.wake",
      "snapshot_digest": "208e94a9681c94fb58aa03c1ffc64e1c6584e529fe66b419e7869a7728be9ac8",
      "version": 50
    }
  },
  "version": 496,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3134.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d39616537316237616536363134323330.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d36343733393830333363653034356462.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d636f6e74696e2d72/61742d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
