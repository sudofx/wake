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
  "generated_at": "2026-10-28T16:15:30.966800+00:00",
  "head": "snapshot:c613a7704d33ebc334f95f60cdc588bf69a624cee2ef73b598d91cbd4b736c8d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T16:00:19.022696+00:00",
      "head": "54d6e7842b7055ad7e5b83c5ee71890dd7776ce6e05d3a01f5b9374eee8f4b12",
      "node": "100.wake",
      "snapshot_digest": "6fe395a092bc15f35307d8550e9e5a3e487ed103d980a08f94ad5bcd4abb648b",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T15:58:35.252840+00:00",
      "head": "7b429127317663bf713e81f00af2877296564850b7bfd6be6ac04d855eedb2cf",
      "node": "101.wake",
      "snapshot_digest": "d872098075b519af4879a9493e4200acefdab53ba744a5c7229e46ed76019a85",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T16:05:21.760305+00:00",
      "head": "aaf7bf03d21f10e523be350f48ca5cbc8e87b0cd93028aca0698ac8a1f6af3b9",
      "node": "102.wake",
      "snapshot_digest": "5b6379980ce455bb30fefced09439c6a0776634fbab082f4acc625516eb20b2f",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T16:01:03.642957+00:00",
      "head": "595514a0e727f13b6e8eb7ca295fa4131dd96ed026cf11ca1e76d383483d7252",
      "node": "103.wake",
      "snapshot_digest": "50ec01837f29734e7c0f28ed9c4790df2e1e2def599dea52dd47546e29bef863",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-28T16:09:01.519974+00:00",
      "head": "4ee1ed5e7f7f79baa5c7b10f8e9f37a80a51b7bd3cf27fd57a4d9521c35e4c96",
      "node": "200.wake",
      "snapshot_digest": "31cb5f42aab43db43fb4324c15e410b8727c83719330dd9dd8d2933811cd8f56",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T16:05:08.410607+00:00",
      "head": "486d8d9d45f7fd3748405509b54ce8651432d66df5c02cae2aa6def178e52d39",
      "node": "201.wake",
      "snapshot_digest": "117720a2f97d543d14897e2fdeb349afac04052aa2ad977e14a03708acdcabfa",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T16:05:35.400918+00:00",
      "head": "e72eb88425d166a32e14780e5b66dd220fb484d2c54b9e136511fb6f23aa1888",
      "node": "202.wake",
      "snapshot_digest": "78b9b0f4801b2606aafbde102b424c5136b1f52d4dc51ba96dfbf292c759a22b",
      "version": 29
    },
    "203.wake": {
      "generated": "2026-10-28T15:59:48.680089+00:00",
      "head": "f9933dbbd925a4b9acf69b0402f2890461f2d41f36f05e88e7445d0ffe762b08",
      "node": "203.wake",
      "snapshot_digest": "117c2389c3b71f34f2c5c778fea682e7845cc8f531fe407276642aefe275c890",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T16:15:30.966800+00:00",
      "head": "4e3ef55a08ee9efaccb3d8dc2bf4f6bc46f1b1a70fa64cc58167a5cd6133c691",
      "node": "300.wake",
      "snapshot_digest": "f8ea3b058594c5bf0b61d01060e5ad74c414f8b0bfbfc9bf460725a41d9024fd",
      "version": 23
    },
    "301.wake": {
      "generated": "2026-10-28T16:13:21.993192+00:00",
      "head": "13e528e5f0e2ab3fa2bcc0a51ce87f2eb1600a57d9dda19e35fd83b65e48ec0c",
      "node": "301.wake",
      "snapshot_digest": "2dda74484502e4a17f0c42738101625dd4232683f58339ba1c223783d7899f83",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T16:14:10.358149+00:00",
      "head": "cc21ba6783988e2f584451a4c820e341d948e133f35ce6705381a1764caaf1e7",
      "node": "302.wake",
      "snapshot_digest": "c2fc9a90201c810b495837094129f949278b2e0a34eb6597b2e5e505ab721146",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T15:58:04.743015+00:00",
      "head": "703192124bafd86228673b9232b4605ebbe2393a328f1adebe182080d10e08f9",
      "node": "303.wake",
      "snapshot_digest": "68314637989246cc661ca53dcb04f57290553045378d2112cba2fe8ae586035b",
      "version": 23
    }
  },
  "version": 275,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d33383564393662376539356234623432.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34653638316631383936663834333263.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d6f62/6a656374697665732d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
