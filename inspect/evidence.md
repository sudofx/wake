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
  "generated_at": "2026-10-23T01:38:29.522243+00:00",
  "head": "snapshot:e46e6d073ef3217ce24ba7ff9bf08c344e6d6f3552b2fab3a8264124ca53f810",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T01:35:49.941904+00:00",
      "head": "21f60bbfd7c5b8f5f82daa0f1aa4c1d45cdd32761ff52dce6ffe7102f815b6cb",
      "node": "100.wake",
      "snapshot_digest": "e1e4d6b8070895f99c86ff1ff6e685cc98b5a07d1e3de8480c331c69e2b483d2",
      "version": 5
    },
    "101.wake": {
      "generated": "2026-10-23T01:32:49.730984+00:00",
      "head": "2f1c1a0f6a1c1d98c3268ae48bb569fc99ae57f99a623df26be482b1c937ad70",
      "node": "101.wake",
      "snapshot_digest": "69d9d774357c3b9a735be051c6b1f98ec537f9e5569b4e295cdb5bad7659dd17",
      "version": 13
    },
    "102.wake": {
      "generated": "2026-10-23T01:29:06.835938+00:00",
      "head": "36094718d6c2d9667145a9b02a66545ef486d9940145fb16578b5cb1056f24dc",
      "node": "102.wake",
      "snapshot_digest": "0a6950242293d60ea20d1aec0464f934ecf47b27444ed3113c1ba92c3b0099c9",
      "version": 12
    },
    "103.wake": {
      "generated": "2026-10-23T01:32:53.972729+00:00",
      "head": "981bf92708375a52335a84f31296244bae992800ed2f9f4bef495e76dccbc277",
      "node": "103.wake",
      "snapshot_digest": "16e6f4fb86596ab4c0b093aff8fa4a2316fc90180f2999cd4672f4639bf93e78",
      "version": 9
    },
    "200.wake": {
      "generated": "2026-10-23T01:30:46.532489+00:00",
      "head": "092afb1f3ec2e89748c2a1591684998f651d610bb7d9646449167e497e42ca66",
      "node": "200.wake",
      "snapshot_digest": "bc0d2d020dfb9ed0515de482a8df01d171cde9652d99d635f3bcc51aa047dcc7",
      "version": 6
    },
    "201.wake": {
      "generated": "2026-10-23T01:30:14.907144+00:00",
      "head": "0fa8c10f34ed895316b3da81a348b28e14d11ebeda1ca3527b28bdc37eb73b6e",
      "node": "201.wake",
      "snapshot_digest": "4772322a8e14a721c27c9f4d2fcfaf0cb618a76bb989b513da76fc695d4611bd",
      "version": 12
    },
    "202.wake": {
      "generated": "2026-10-23T01:38:29.522243+00:00",
      "head": "24469be724fa28b113c9193940f64fd9770cd8c58be8440a3a59c7a555ceba2b",
      "node": "202.wake",
      "snapshot_digest": "4d2d56d46c675e6c8014c9d43773506d4607cd25a616bf0832178449a3a3fae4",
      "version": 15
    },
    "203.wake": {
      "generated": "2026-10-23T01:29:50.249347+00:00",
      "head": "8b1338ad90647e48030ca8aea54f83565b1ab76c8871960514813763e3465b07",
      "node": "203.wake",
      "snapshot_digest": "f6c5604aca3874ba2ec6361d774e35decdb8fddf36eefff50c4938cef475369c",
      "version": 7
    },
    "300.wake": {
      "generated": "2026-10-23T01:31:30.065294+00:00",
      "head": "a3d0b9c31b6ceca9529a09901488c4aff45d483c430cd62ac727f64158fa3f5b",
      "node": "300.wake",
      "snapshot_digest": "0ae4cffebbb17ac781ab5896d1784809f2414600a8a42d9536c9821cef1f6a2e",
      "version": 6
    },
    "301.wake": {
      "generated": "2026-10-23T01:32:28.166893+00:00",
      "head": "adca59633a7894058bc24566a97991b1555d12e8f905f52b62ae9de9bba3ce84",
      "node": "301.wake",
      "snapshot_digest": "784e3b4b0da9f212aff4868a745939cf89e18606a5cafecbc8855663dc439b9f",
      "version": 10
    },
    "302.wake": {
      "generated": "2026-10-23T01:28:35.519072+00:00",
      "head": "f4dfe88392948cddf56d1622229529fb8abb9219e32f8493afa6c1eeca840db4",
      "node": "302.wake",
      "snapshot_digest": "12b56d0420b5557af9a23a540791a296ea07c8dbfdd496bed5e7e8772f02e67c",
      "version": 7
    },
    "303.wake": {
      "generated": "2026-10-23T01:32:08.955623+00:00",
      "head": "f01bd33367231db6b2b00746327992d8b11de6c4616955c9487eecd3bcff92c6",
      "node": "303.wake",
      "snapshot_digest": "25565c0a219434657037dfea0209c17e7d448a31f3b4a307481fd21d158ba77e",
      "version": 17
    }
  },
  "version": 119,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d34.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d33343737313965616265316334366330.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d623638376334663632633362343537/66.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d696e/71756972792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
