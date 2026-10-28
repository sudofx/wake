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
  "generated_at": "2026-10-28T07:05:42.186859+00:00",
  "head": "snapshot:3c57878049920184cf0f5739ad38d2a60d89eda043d5748040f6720a82613e22",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T06:59:34.663029+00:00",
      "head": "c7530ebb17abeb74dd023a987a280df91ff6d05e9afce32ca1b5eef1a3fec5fd",
      "node": "100.wake",
      "snapshot_digest": "7d7455c926fe2b8f43d5f2779dfcc2ecb49fd786a7a483f6991f331427319844",
      "version": 8
    },
    "101.wake": {
      "generated": "2026-10-28T07:02:16.384609+00:00",
      "head": "69523f2e905b93a454e1299495b9fab3662cea218f904753b12975bfe5b7e5c1",
      "node": "101.wake",
      "snapshot_digest": "ed6e60d7fcd87a5efa540e0eaf9effa04e9b3829b8ef3ae034ff48c5e4547a2c",
      "version": 12
    },
    "102.wake": {
      "generated": "2026-10-28T07:05:42.186859+00:00",
      "head": "9945abf63894b7de61d1a3ff9e522b7f5ac4cc4fecb5a4d8fd80fac1a0290f6b",
      "node": "102.wake",
      "snapshot_digest": "d617dc777003ba28aaa138e57ac3e4efebb4ee234eecf95bc55f60fdb95d06b1",
      "version": 7
    },
    "103.wake": {
      "generated": "2026-10-28T06:59:58.963843+00:00",
      "head": "80517d32de301dc3a9d0a59a23a7253c035f1521851c5d08bef96da45612580d",
      "node": "103.wake",
      "snapshot_digest": "db6bbe614b4df576d563bc490b1286b55a52d5540beef8263a1e5d0605bd67f6",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-28T06:59:59.140045+00:00",
      "head": "bcfa3bd47ea52223b3a54b4d1563294b14b0ad744829beabf668acb2fb30a0a1",
      "node": "200.wake",
      "snapshot_digest": "0bd4df48dd0d4cbe8b8dbd09cb59a35d45c5b5e51b2235fd50a1257a60e66fba",
      "version": 14
    },
    "201.wake": {
      "generated": "2026-10-28T06:59:53.846551+00:00",
      "head": "6c9efc2bb6895ef4391a64485c4cff2ebe4b96358e86dd2edb6b36550ac68e15",
      "node": "201.wake",
      "snapshot_digest": "98ed758f686a2e3d8de3a7c921471241ad6b86cca6e055e274cdd4b3739a6e8a",
      "version": 11
    },
    "202.wake": {
      "generated": "2026-10-28T07:02:11.426481+00:00",
      "head": "38ba1c4f94944bafc4173eeecd10f1530554778179564ebea8c445b9d6f7511a",
      "node": "202.wake",
      "snapshot_digest": "52602a88a8b0d6b522dcfb99ea71f09fd5b2ac329bd135bf7a4c891c8c2d0459",
      "version": 13
    },
    "203.wake": {
      "generated": "2026-10-28T07:02:54.756367+00:00",
      "head": "0aba60c1ac783510d7bdbabe38977844bb5704af2fa7d9285dd634593cd7364a",
      "node": "203.wake",
      "snapshot_digest": "ba22c2629781e0a12294a4fcf8d936c8f27520b38d433d9d7b7dcca6993152b6",
      "version": 18
    },
    "300.wake": {
      "generated": "2026-10-28T07:03:44.945145+00:00",
      "head": "bc629a529a22ed188440b0cf69f00cff6947fe5ddfe7e390cd78a67f5dbd2ef3",
      "node": "300.wake",
      "snapshot_digest": "c89679d98b36d073ff8eca30bc2bccf136bd016867efcb805b9fddf6ad9902a6",
      "version": 15
    },
    "301.wake": {
      "generated": "2026-10-28T07:04:03.159143+00:00",
      "head": "3a2a385459b2187a1de6f9662e08addb32c0f82a5ca35b992b120ab37a2e4397",
      "node": "301.wake",
      "snapshot_digest": "2020ed68286d32839559e444fe1a0853a5c4e629967e269c44f2f9ad5efadd9f",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-28T07:03:12.241456+00:00",
      "head": "07bb5e2937ca1ddff27b0b514e5eb07dccf77412c6804b7594e90a55474dc0be",
      "node": "302.wake",
      "snapshot_digest": "e0b17dbf2cd11126994580f3529986d9259f75528c6cac137db1463d13a21df4",
      "version": 10
    },
    "303.wake": {
      "generated": "2026-10-28T07:02:43.317816+00:00",
      "head": "7721e1048985f57818609a463a57018ec811946d49453e133f1e6b8aeea04bcf",
      "node": "303.wake",
      "snapshot_digest": "72782635adc515a615dd317e0e024b7e48dc2f03659ea7ce0af9c90a024b6e01",
      "version": 15
    }
  },
  "version": 152,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d64623061303163316331663634346532.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d626364326230653166336164346266/35.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
