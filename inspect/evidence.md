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
  "generated_at": "2026-10-22T20:30:43.730278+00:00",
  "head": "snapshot:5822f7010f9c77943605f1835904fbdbfdd771d0e631224b61197452d6885584",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-22T20:30:42.137225+00:00",
      "head": "339a3736b8e2c85d9dc70313055939d27b50e97caded0524034b01a21062136d",
      "node": "100.wake",
      "snapshot_digest": "4646978b1ea7c8cc317156403dbda5280ed27480cd3623419f495f35fb906106",
      "version": 0
    },
    "101.wake": {
      "generated": "2026-10-22T20:30:42.318628+00:00",
      "head": "388e703996513a3d5dec6a6d1b27e975d9c55550d6add77063585d60c08912a3",
      "node": "101.wake",
      "snapshot_digest": "4d4fa3f36a566e94f735cdc3e08d1069d6e861faaa9a64bbb4b697915608ca7d",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-10-22T20:30:42.467866+00:00",
      "head": "3553593192d93652de98bd3d63f3c548c5d42bea275a50ad120da94e6658b756",
      "node": "102.wake",
      "snapshot_digest": "40b2cc3fbe205c87434b32f05bb5a251171b728a86408acc2eb8bff05081773d",
      "version": 0
    },
    "103.wake": {
      "generated": "2026-10-22T20:30:42.610422+00:00",
      "head": "0f484b0d10728be1a99075d892853a85904ef44b70941389222ae7fac5266748",
      "node": "103.wake",
      "snapshot_digest": "752cbad039eb18f7589cbfbd1f079f935974ea1cd2d2a95cb50746031e918cd8",
      "version": 0
    },
    "200.wake": {
      "generated": "2026-10-22T20:30:42.751094+00:00",
      "head": "7daceb49a032e974955ac8045eeaaf75e27b8a6c516138b7a68b903a5f7ea74e",
      "node": "200.wake",
      "snapshot_digest": "d0a2631be843d531e4ecfe2a54efef7dae8bf056cf64c00ac26eae89815ec633",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-10-22T20:30:42.895364+00:00",
      "head": "1c0fd6d908b1d11ab6e5d8569d05be1bc8e938eedc6572b091419a866921dd0b",
      "node": "201.wake",
      "snapshot_digest": "852129769ee55d9b3ff2ec93b10fcc5fe7fe0760c7b1774e25b647c62bec8c00",
      "version": 0
    },
    "202.wake": {
      "generated": "2026-10-22T20:30:43.028134+00:00",
      "head": "3a650157a1391e5131a4cb0b4e1a9b4bce35a66f6b02d1d2e75a93c8ef5b34f2",
      "node": "202.wake",
      "snapshot_digest": "884f04847f629edb6ee401052913a77b1c8a0b1b29547849a672fab31ac3f538",
      "version": 0
    },
    "203.wake": {
      "generated": "2026-10-22T20:30:43.170092+00:00",
      "head": "322bc6651c01ae1bc7c961e35f144ef0e1ad11edae1d0fbdce0dceb1eeb4a28d",
      "node": "203.wake",
      "snapshot_digest": "a8ee5ee76815887f00207a5626d67f2021533d53b7050a6652a90e83991d36f7",
      "version": 1
    },
    "300.wake": {
      "generated": "2026-10-22T20:30:43.317665+00:00",
      "head": "af49264a680a3451e1c51888bdf47df8ce1f9aae6ec3bd11e33d8704798e67ae",
      "node": "300.wake",
      "snapshot_digest": "0006ff290169a3224e61a3c3e86083396708e5e4cc21c9a5b73a1f1db631c8ef",
      "version": 0
    },
    "301.wake": {
      "generated": "2026-10-22T20:30:43.452439+00:00",
      "head": "8a780fc598fbd799c3d8d3a8ce6ec215789e434ef8af7237713231ab995d4562",
      "node": "301.wake",
      "snapshot_digest": "1fc85856f86f2b9e06ceab3e3d2b1e487edd394ba3f3b94357232114ecf9e7c9",
      "version": 0
    },
    "302.wake": {
      "generated": "2026-10-22T20:30:43.583357+00:00",
      "head": "aab6d098d6e23689888c9173fab616ad03a20e6731aafe8e9ee66e4041762e5b",
      "node": "302.wake",
      "snapshot_digest": "dd5752f86bb5c20c2dd1394523f82c029ebf67837b6ad065272a21f6e132ff3a",
      "version": 0
    },
    "303.wake": {
      "generated": "2026-10-22T20:30:43.730278+00:00",
      "head": "e98f91848779822d9254d42cad06c64aaa50c711d80f10cdc7891de81e62769a",
      "node": "303.wake",
      "snapshot_digest": "1669dfbec19358c75491fa241f2a8dc86a31bc03c57262dcc7e990692b1024a2",
      "version": 0
    }
  },
  "version": 2,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d613839303138346534306535343334/32.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d616436333037353833373762346237/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
