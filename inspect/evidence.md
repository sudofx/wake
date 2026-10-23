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
  "generated_at": "2026-10-23T14:34:46.020395+00:00",
  "head": "snapshot:ac5530f2a6e3c5cfbe7063739fdf15e88193dcb6979b85f359bedb8968e4c08b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T14:33:02.502773+00:00",
      "head": "bdba0faeb3535fcc37c55180161b4432cf38a032fb30ede95c5046004f714958",
      "node": "100.wake",
      "snapshot_digest": "45eae7503670a9ce80ecd604cb167f9f4361e2a18688a9c1b616f5f02039917e",
      "version": 15
    },
    "101.wake": {
      "generated": "2026-10-23T14:34:24.233576+00:00",
      "head": "47e4f3271bee9111be2434728e7a9c2647ba6c3eaf0237620a57055f7dce27c6",
      "node": "101.wake",
      "snapshot_digest": "d338e4b71d8c972464686ccc3d43548c929c83cd0a14cbb57cfab3373432c138",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-23T14:33:33.296306+00:00",
      "head": "da0f9a0e133e0f9d7b9de22f2dd266c338b40ac93af78993fbd06b8799e4d107",
      "node": "102.wake",
      "snapshot_digest": "d1fe95d7c398e3ba7d6982a74df4247cccdacd587ca55f9c451d21d6d4c5ea2a",
      "version": 30
    },
    "103.wake": {
      "generated": "2026-10-23T14:34:46.020395+00:00",
      "head": "baf1b00a91e497b1fc9d1f4d15f81f74e835972b44b0e26c11f260f0289e55c3",
      "node": "103.wake",
      "snapshot_digest": "8fab26c0d2ec060714ab8a3c78dad69c3fe01178eb86ff310eb582e0368a4b08",
      "version": 20
    },
    "200.wake": {
      "generated": "2026-10-23T14:31:58.813974+00:00",
      "head": "3257e9e2c9406c5df6fb9f3a9b951d1febfececeb1bb4c276ea15ac9ce1605e9",
      "node": "200.wake",
      "snapshot_digest": "d466b9b61437b7cce8fa6815485540bf9bd58687e4c6ac236a655125e5f0c720",
      "version": 19
    },
    "201.wake": {
      "generated": "2026-10-23T14:32:06.490075+00:00",
      "head": "ebdb75fb4dc372f486dafb6b6e092311a2785b3596d1b7a9b3390b49e81fafb9",
      "node": "201.wake",
      "snapshot_digest": "33a04855a903d17100623d45591749d55ed7297a6305631305fce5a0d08a4541",
      "version": 21
    },
    "202.wake": {
      "generated": "2026-10-23T14:33:09.441674+00:00",
      "head": "dd13383de6cd5cae98c1db32c51c5136f78209eb53395bdb73a4796efdfc41e5",
      "node": "202.wake",
      "snapshot_digest": "bf1c27eec62bfe6283f2aa1e287afabcfc6471ce47b24c02b5736185cb8aa6e6",
      "version": 31
    },
    "203.wake": {
      "generated": "2026-10-23T14:34:40.229254+00:00",
      "head": "bbbf6a2770dc3161a3f2cece8e60be0a32f76ee11bd6fa1929bd80b676d9e525",
      "node": "203.wake",
      "snapshot_digest": "0d9ab577c827bd1220c8ae1aff0c7ad392fa28cba37c6f0b84784470dcccb9b6",
      "version": 13
    },
    "300.wake": {
      "generated": "2026-10-23T14:32:57.348442+00:00",
      "head": "f14fd6981e6167cd0a1f607b4388de6e905c9030cf320a3c197ec06ef8c0e4dc",
      "node": "300.wake",
      "snapshot_digest": "a7e9eabd4080f024674b3916c505dc742488ee0ab1fd2ed8b82b19c877a3921f",
      "version": 17
    },
    "301.wake": {
      "generated": "2026-10-23T14:33:15.878894+00:00",
      "head": "83fb70ae581a2a5256894b2f7e877c48066d73eba1c1ab417e7dae39263db509",
      "node": "301.wake",
      "snapshot_digest": "397bce2dc6a852b897bbc4e384b5e47850b26a5ab2893d6a9f8a05a4bafbbb86",
      "version": 28
    },
    "302.wake": {
      "generated": "2026-10-23T14:33:39.931423+00:00",
      "head": "2e0524b5a5dc094eaa66e05cb9a52cc1e57ba893836652f191d084ee2129eb4b",
      "node": "302.wake",
      "snapshot_digest": "1917248b3008d3cdd0816971d92d416090c577cda93ccde9358331cec6793e4e",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T14:34:17.280078+00:00",
      "head": "ee5fd32fe5ace17654bb8a30fba1969d02fa5ea1eb92c2d007ee6c4de0f58a07",
      "node": "303.wake",
      "snapshot_digest": "17414ba26741a5ce421c17f792ae599db7b7775bb81c6d45d0a26dae0ff77b80",
      "version": 27
    }
  },
  "version": 256,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d373339353331326430663938343033/39.json)
- [evidence record](../reader-records/evidence/3130332e77616b653a3a736f757263652d393964363863383934333937343931/30.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
