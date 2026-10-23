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
  "generated_at": "2026-10-23T12:22:10.788077+00:00",
  "head": "snapshot:c01653b30498de55b420e9879bfb917f8648ce9140e57e96aa2b80fbedbf9af0",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T12:21:50.505252+00:00",
      "head": "89a2a54d67cb08536c023de3a2d80e712e5842e39016e0f5e6880c352c05832f",
      "node": "100.wake",
      "snapshot_digest": "6bffe0c4a4253052e1de94f4abe46ff17047f91f7cd6333d5883b292f7017771",
      "version": 13
    },
    "101.wake": {
      "generated": "2026-10-23T12:22:10.788077+00:00",
      "head": "72d14aeb347796d62b3ace2bea2c47a1275cc07ee6343444288744f18fc5afac",
      "node": "101.wake",
      "snapshot_digest": "51876c942b7a51bf9e3884d5502ce3b99900bdeaee2fa248cdcdbf4f8b98761e",
      "version": 20
    },
    "102.wake": {
      "generated": "2026-10-23T12:22:04.301057+00:00",
      "head": "c01e87d7e3c986651c12ded96fb15d14459e6fcd90c5cf1f0efdba6f772d2166",
      "node": "102.wake",
      "snapshot_digest": "586d92ff4e1a8e58d0ac52be13296eb1d96c75abbad1c9783eba9f343797057c",
      "version": 27
    },
    "103.wake": {
      "generated": "2026-10-23T12:07:53.996376+00:00",
      "head": "28c23e4ce4331e0be4eed2500a2bb555061f4087c054ddb72975c3c2dd65c09b",
      "node": "103.wake",
      "snapshot_digest": "96c63cc824ba69bfd91691ffcf862ab305d60398c607e4550127cd9d970230fc",
      "version": 15
    },
    "200.wake": {
      "generated": "2026-10-23T12:05:06.817870+00:00",
      "head": "6d63dea7b1494b2135f550148a092d16b0c94b692e9d4a7c28e1bfe1f2efb8e5",
      "node": "200.wake",
      "snapshot_digest": "8fd2c1bf9cbc9f5d556964ec2d0e2faaa3c8afca270ec6db0d6e215edefa9661",
      "version": 16
    },
    "201.wake": {
      "generated": "2026-10-23T12:20:50.352532+00:00",
      "head": "cadd29a03f0947700ba574dbc6fb75531dd90109a2029135e1188a8f2d133d3f",
      "node": "201.wake",
      "snapshot_digest": "ffe96312957cc2062a359d3319ae71669af25c5d3c6d14a398c8e80674510215",
      "version": 18
    },
    "202.wake": {
      "generated": "2026-10-23T12:19:05.023405+00:00",
      "head": "d28ab7ae28f9b60c92d3cafa4b6d0b24a3eb33f66d8887374cb6cc69fcf2f043",
      "node": "202.wake",
      "snapshot_digest": "26c5e5871b1547d30aca5c4f3fd8a6d0037672fcc38113f98a7d197138ecf932",
      "version": 28
    },
    "203.wake": {
      "generated": "2026-10-23T12:05:50.095429+00:00",
      "head": "4e7006cc648e5b15583e721ee350990fb066cc82f1119d36e1383cb8599d5255",
      "node": "203.wake",
      "snapshot_digest": "dd7da0d771211b04a6c4b9d636c0523702c44c10afce5ce95c5747cca7811d54",
      "version": 11
    },
    "300.wake": {
      "generated": "2026-10-23T12:07:13.412406+00:00",
      "head": "1d24471912b86be86ebca5765aafbe349ec2ec2b283b5e81d82a506ccb7781ce",
      "node": "300.wake",
      "snapshot_digest": "e820f8c76ef472b65181e55e465044fb9aa4c4e303954df7e082a60a35f70ef2",
      "version": 14
    },
    "301.wake": {
      "generated": "2026-10-23T12:20:22.516019+00:00",
      "head": "e166aa8a1b2a0c60ac5e075a31feab98a86f765be4aa3a69500e8fa5673a342d",
      "node": "301.wake",
      "snapshot_digest": "3272a1d79605bdbe4ce16aae828143bffdfa1e3af55cf381c6c56b7cc6b2617b",
      "version": 23
    },
    "302.wake": {
      "generated": "2026-10-23T12:19:55.297583+00:00",
      "head": "e55d71598b9fe6990520c7a6a72c1ac83db4561c2b8bda2f4b0c479a200c3219",
      "node": "302.wake",
      "snapshot_digest": "1424e502c53c7d89697155c615f31a592222026c2b16a911bd745bd49130e686",
      "version": 12
    },
    "303.wake": {
      "generated": "2026-10-23T12:08:48.100713+00:00",
      "head": "7b656169e86f3dcf7643e993dc01da7c5e2942cbe777b754084ee70a73cf8607",
      "node": "303.wake",
      "snapshot_digest": "de2edf5e29177f9bb4f568fe1f97d6952e6535d71e5fbc81fff82d351b6e9520",
      "version": 23
    }
  },
  "version": 220,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d36.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d373639333739323133613238343133/30.json)
- [evidence record](../reader-records/evidence/3130312e77616b653a3a736f757263652d613163663630633138613632343364/64.json)
- [notebooks record](../reader-records/notebooks/3330312e77616b653a3a6e622d6175746f6e6f6d6f75732d696e71756972792d/303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
