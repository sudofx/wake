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
  "generated_at": "2026-10-23T17:53:57.229464+00:00",
  "head": "snapshot:31c9b9b643ff8d35b211ca101a6a9dfe5360e2891e153946d072788df1252ecb",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T17:48:36.323416+00:00",
      "head": "1b1d1cd5ba0893ed6904434640f10413d8a1f51a13edfe6def7c69e4d5483bcc",
      "node": "100.wake",
      "snapshot_digest": "d14872cb1234996235b5f6d1a5a31194868a5a3dcb1db1314d2f9d10ddd624e4",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T17:49:59.480889+00:00",
      "head": "f8889bdb4b2c72e4fecab3ed398446bebe28d71e53aecf9b37530b45b424a4a1",
      "node": "101.wake",
      "snapshot_digest": "e0dd2fd6fca81eeb452ec40a080dc7ac7550a67c3c8848d430087565d3e23d7f",
      "version": 28
    },
    "102.wake": {
      "generated": "2026-10-23T17:48:23.545321+00:00",
      "head": "1287347dd8e0c09abb31c272a101b58891e654a76763cc4312317c8e46dad066",
      "node": "102.wake",
      "snapshot_digest": "f5ba46c26bb98907202b4b7977de09580f73c06353e5337c62ded974f9b39f6d",
      "version": 34
    },
    "103.wake": {
      "generated": "2026-10-23T17:48:44.179122+00:00",
      "head": "c14fc979125c74a3f00ecb5d6d72e8b23e83d79995ec4b4a46c372de5f3467f4",
      "node": "103.wake",
      "snapshot_digest": "af8cfc2c21284f4f57b264abdc879b17215cd4c41b59d5c79a0537ee2014f083",
      "version": 25
    },
    "200.wake": {
      "generated": "2026-10-23T17:51:48.884560+00:00",
      "head": "a2a2c9474c76dc2cad4e385b0d1d701c146fe9f7e000efc37c369b2ba9e1a941",
      "node": "200.wake",
      "snapshot_digest": "00abe25aef494e07811c036fce2e75b9c21326b59449f593dedd5e9f6489b50c",
      "version": 21
    },
    "201.wake": {
      "generated": "2026-10-23T17:48:58.249559+00:00",
      "head": "20657fb94445f20a4ed20000b59b7e98796e3596bf09297b744867e0cc9306cd",
      "node": "201.wake",
      "snapshot_digest": "fcc1a1a4732e062fd652ffa97405aa2445129274494cee48f8feb2c0b873f6b8",
      "version": 23
    },
    "202.wake": {
      "generated": "2026-10-23T17:41:52.934892+00:00",
      "head": "3c661869f5e4832be279838c7ab1b80d86730414e0959a0c06ac46f7cd505f13",
      "node": "202.wake",
      "snapshot_digest": "a2149f9c25c3e5168ca3f1c59c23b463cfc4e4ae45de2ea651d224a40d70a3e6",
      "version": 37
    },
    "203.wake": {
      "generated": "2026-10-23T17:45:33.351355+00:00",
      "head": "b93ecd56e57720d065a21e93ff1fa5549e6443cfca4b4ac7bc2fef9ef597f183",
      "node": "203.wake",
      "snapshot_digest": "46d6ff5cdec224ad72e2acd540d50c35cc5e87173a1cff81b60602ae897dc85d",
      "version": 16
    },
    "300.wake": {
      "generated": "2026-10-23T17:51:17.632509+00:00",
      "head": "20abf4d74e0037bed25a6f85ff1b8af95abbc5e861d1a7a5b55f6db067123d45",
      "node": "300.wake",
      "snapshot_digest": "a6791e1f8cfceeac08e92050b2f3ac86a4de61942f6c2a4941a5ce598b5cf44a",
      "version": 22
    },
    "301.wake": {
      "generated": "2026-10-23T17:53:57.229464+00:00",
      "head": "a2673fb84f2629b0179ea44709c34f08883f287356c49f222d0a756ed2174dac",
      "node": "301.wake",
      "snapshot_digest": "32802baf072a8678efc15d18847c12c3c8bbf783e047528a5812e24b3ddedd52",
      "version": 34
    },
    "302.wake": {
      "generated": "2026-10-23T17:19:59.819939+00:00",
      "head": "2533b96f3c703259daf18f1d7f4da94935cca76ccb693a9cc07c5a238bbef5ff",
      "node": "302.wake",
      "snapshot_digest": "095f823a83daa55c8dbc200d7e4ba66c3705e62b228115b0e926db59705cce40",
      "version": 16
    },
    "303.wake": {
      "generated": "2026-10-23T17:47:19.625234+00:00",
      "head": "272e210004052cf627bded0f6c397c96868398baa09f5e85583fb669adb93acc",
      "node": "303.wake",
      "snapshot_digest": "e681bb494cded9e11e37f0d899ca9cd64219b1d5d10e6a5dc85ea7e4861e3f08",
      "version": 31
    }
  },
  "version": 303,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d34306630333535646365653834636633.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d383964633966613463363462343565/63.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
