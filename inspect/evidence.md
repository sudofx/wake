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
  "generated_at": "2026-10-28T19:52:19.685484+00:00",
  "head": "snapshot:23ca7ec2f4e96729ba26c9f15c04bb7a9f153513582bc81d5d3faeb87a2c906f",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T19:50:36.021909+00:00",
      "head": "9d0cc7ed255eb6335f1a14ce06406aef30ec0ec3cc100c5ebc18daff2f18ce16",
      "node": "100.wake",
      "snapshot_digest": "91077403a6a98631bf8b08285a7c1ae89ce4b6c7a975b681c16935a3cce3adb8",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T19:44:03.631086+00:00",
      "head": "1409a205bcc9584a0a11ba81a7e7fe6c231aa8fd49b4cff2fac607cea469b4ff",
      "node": "101.wake",
      "snapshot_digest": "cf6502407884dc57314ba56f4c108fee3cf6177c55f126a2cdd63f238f2177a8",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T19:44:40.928715+00:00",
      "head": "2aca5c9535aa1e51baa54a6258e04d1074729bfdb54b3f91c68f20f2f6566027",
      "node": "102.wake",
      "snapshot_digest": "99107e7227489e853f007b163111e300094adb67d0c152ca3ccf6eb72b45032b",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-28T19:50:15.180695+00:00",
      "head": "a6b7d9b9402a235ba106119dd7e2345eba888399d4ad09138a8c09c69818c7fc",
      "node": "103.wake",
      "snapshot_digest": "25e835400c99574f0245b197e299d863f3d4d85112c88855a5f6183cfcfa591f",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-28T19:50:35.042516+00:00",
      "head": "19aebcc37b389b1e1f734aa0e6b8a2c727edb41485a49dd186fa9262e99172fb",
      "node": "200.wake",
      "snapshot_digest": "4cac37d61f4f90ecd9d556fd7e707996c47537c31de0ef28cd1fc15beb6bd4e9",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T19:51:06.886924+00:00",
      "head": "a85945a5187e8249d5092e690700724bdee0ce21c409e23febe10811deef50f4",
      "node": "201.wake",
      "snapshot_digest": "25f18a5c5a78b63282dd5aaa794c1e41b0553cb5129bb88bedabe0abd36a33c6",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T19:46:01.359335+00:00",
      "head": "f5ed965d6fb73962708ad3281a30fba670e3517e516e35494feeb8f95c164f78",
      "node": "202.wake",
      "snapshot_digest": "9275f57213a2837b052eedf87c86f173cf8ac9d739af03ffdcf8d8fffd94aedc",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-28T19:52:19.685484+00:00",
      "head": "c3c807baf6307706c2e9f7d37055d11704bd624fa4edcbaee780f57b464f0604",
      "node": "203.wake",
      "snapshot_digest": "ba3ca96f78d32211663d96f6727c7b7f525dadaebe170fe842bc9d4b414b5b79",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-28T19:44:38.111427+00:00",
      "head": "12549d2770e62f05440db2f46d6b3281ee4196e891845a5a50895f0f788d7ce0",
      "node": "300.wake",
      "snapshot_digest": "bdbeeae53b56894862b3f631256ffd69d5fc3bc28dd20087720e44a43b6186cd",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-28T19:45:11.040650+00:00",
      "head": "a07938796241a4606c36f6ee6095058f9c61f0410cb5ea975f0d181f1a04720f",
      "node": "301.wake",
      "snapshot_digest": "0a071b4417b6d5f3b8ff0368f25c3b8e4048247c4c9a8908965f00dd4ce69920",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T19:43:05.593525+00:00",
      "head": "0f7975991b9280d3c19403c71d7f468128657ca710baaa3d0c06efe82948a0e4",
      "node": "302.wake",
      "snapshot_digest": "266944951664da302b21ae902dfed0e8c9828dcb0b81f5457ebc5280f45b4afc",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-28T19:45:31.337126+00:00",
      "head": "1963a7c9ebccfad438381f1e6ed2e5942c940711a8372777182299e3e0974eca",
      "node": "303.wake",
      "snapshot_digest": "f0701f3690025b37cfdd7005bb4b4a176ef127803608c021cff3de30f566d395",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a722d62303937323464646430316634626265.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d39613838386531303934656434623632.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
