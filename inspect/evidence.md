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
  "generated_at": "2026-10-23T13:57:04.298923+00:00",
  "head": "snapshot:2d4dd1765f13f51168964c0c45ea2281539c3f913002d83824325db909dd7b5b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T13:45:35.187975+00:00",
      "head": "20699702d424a77332345d050df541e82a2509cda071f230e8e5212062ff03bb",
      "node": "100.wake",
      "snapshot_digest": "6f42b0d993b85ce05c913298c8eb874494024d16d04f3eeefe40da14c1bf00fd",
      "version": 15
    },
    "101.wake": {
      "generated": "2026-10-23T13:52:17.574262+00:00",
      "head": "3bdd738a879cfab125076fac3e4cabc590913da836f1814bf22aea1a485d1c71",
      "node": "101.wake",
      "snapshot_digest": "f7b1490489f2678fceff77751dd0447b1a8fc322d73281ace888191d68a989b8",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-23T13:46:29.771791+00:00",
      "head": "2853232cd25310b5cfc8d060d200d6aec5961c18c97629e3f0fb8ce800936261",
      "node": "102.wake",
      "snapshot_digest": "619c4d9cc9ddd839065adbb397c0e3c88ee74e79307cfd5b6cbbe97722a1855d",
      "version": 30
    },
    "103.wake": {
      "generated": "2026-10-23T13:54:37.911908+00:00",
      "head": "d42707ec65af639465d9e1f55709fb4c92fd69f7dc869dc3100b2ba098a3ffe7",
      "node": "103.wake",
      "snapshot_digest": "9899961e9d1291e173927ff3b1b1fa1ba3fd69633d61565671b2af7ca315033a",
      "version": 19
    },
    "200.wake": {
      "generated": "2026-10-23T13:57:04.298923+00:00",
      "head": "793deb479f7f3bfe3145e1042ab9444b83df186e5ea9639cb14974835c12492e",
      "node": "200.wake",
      "snapshot_digest": "d96b7a50c8ba993375e2922dd14af607fce1b325ef2518d6c794d37966882d55",
      "version": 18
    },
    "201.wake": {
      "generated": "2026-10-23T13:55:13.744413+00:00",
      "head": "e660c5106ccedef9be3980c0dea62b0231eafef7c11ea16a03f8865eaef9b4ab",
      "node": "201.wake",
      "snapshot_digest": "b13385246e1d38ed433e9f17805fa24fce967a19c515c897b61be34aa97b30f6",
      "version": 20
    },
    "202.wake": {
      "generated": "2026-10-23T13:54:59.426436+00:00",
      "head": "c0e0c7ef1b04a639c4fd29e00a1a55cbd2fcfb09151bf5c00f5724a47f7a5bbe",
      "node": "202.wake",
      "snapshot_digest": "355c7ce4fab24711953f5515f8fc851be8132aff963f7fc664a348bc99898d22",
      "version": 31
    },
    "203.wake": {
      "generated": "2026-10-23T13:54:17.793014+00:00",
      "head": "3eff9528357545c11c05149b123afdae4487ea77d895d1a77aaf034f8029b9ff",
      "node": "203.wake",
      "snapshot_digest": "4ca1fe63213a7fe46dbe2767465568621e1df199e44c17b503b6526503782976",
      "version": 13
    },
    "300.wake": {
      "generated": "2026-10-23T13:48:55.217307+00:00",
      "head": "7293a3ce65e7b9da5c14965fef29c9c4dafe589b3c8c765a4827c01156a32979",
      "node": "300.wake",
      "snapshot_digest": "87e7c99ba98f0f0b392c19662f38c9989ec88f17dc57d4bdf3360bef55a174fd",
      "version": 17
    },
    "301.wake": {
      "generated": "2026-10-23T13:49:37.524198+00:00",
      "head": "97b8253ce77b4c7ad2a57c4b1cd6812e74e69b0c325dd2ef1138378df83ac2ea",
      "node": "301.wake",
      "snapshot_digest": "9defa58ed744e4de65729396aa2ae6771ff06e75f3448f63413774dacdf8576f",
      "version": 27
    },
    "302.wake": {
      "generated": "2026-10-23T13:50:10.336390+00:00",
      "head": "31fd855811f7e3d9caf03f390c7b7794d540ead92ee223d4d2fba2ff965f7c50",
      "node": "302.wake",
      "snapshot_digest": "12a37bc18f8bc55925c0a852f359dd0c4b7d1553e3e0e7ebb158bb10f25db237",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T13:51:35.999362+00:00",
      "head": "7b5fce10f90107c3086ca421d2767f9de8fd04174df98834bdd2474fb2c293a1",
      "node": "303.wake",
      "snapshot_digest": "795d427cd3036c648b85c2722a8938277f4f381163b46f52cde398acdef87434",
      "version": 26
    }
  },
  "version": 251,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d343635326638386232313536343935/34.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a736f757263652d383137656133353164393632343634/37.json)
- [notebooks record](../reader-records/notebooks/3230322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d657267656e74/2d70726566732d30312d7631.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
