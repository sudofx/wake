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
  "generated_at": "2026-10-30T13:10:57.985222+00:00",
  "head": "snapshot:6cac146b558516d71dc946bf3962f0fa9a56d3c432b20b1a87dfe60cfae8aa76",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T13:09:16.563577+00:00",
      "head": "ca30d9f5adae080299455eccb7ce08dadfc6caaf9757da2f62416742ddb57e61",
      "node": "100.wake",
      "snapshot_digest": "9c27345eaf85dfa38818d893e79ef6f7ba87df9d141084214cab1d29f0c63201",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T12:40:58.194816+00:00",
      "head": "2641145cc80c5f5b3985b16afde8cc4ebe9406e6a066f2b1d7a21506ceb3ff44",
      "node": "101.wake",
      "snapshot_digest": "2ee48c4d6cd55243c5c60294e43323c3a16e060f345b407874a0fcc5be9b0ed7",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T12:40:59.561834+00:00",
      "head": "fbbba689c6045ced308d6e583103d3cab7f7827f112aa83869363bd89dabb439",
      "node": "102.wake",
      "snapshot_digest": "5fe40d3f78d8b8632ffabe543bbd5eca11b2fffe15aa0423b06576788d71f582",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T12:41:11.784178+00:00",
      "head": "fea308ca25b4643402d7f6b527aa15cbac57d46da8d8be09343dd3377158d747",
      "node": "103.wake",
      "snapshot_digest": "aaa11c466c4716831914ecf4b85bafe1a319f7890e83e9ffc6998e95bf0521f3",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T12:41:19.413737+00:00",
      "head": "9f41eaa1c452e7c58cde20cfb3899deac983a6263f0427fcf6907545e3473a9d",
      "node": "200.wake",
      "snapshot_digest": "b8c4a6df5e1bd07aa7fc22ebfff4ce48eebdcf6b9d506fd692066fbc8b5cf3e5",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T13:05:57.312727+00:00",
      "head": "972ca2ad06d0e67da8e916a2c3673a2c44645a74532c3be54466b026cc8f4e39",
      "node": "201.wake",
      "snapshot_digest": "4f4326ac7dbbd1b2150113815e7106c5528b6565f1ed166e7c57f530588b49ab",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T12:41:05.209549+00:00",
      "head": "c2784691f46647f11003df8fe6cdf591b13f66790f5c77b54bddd69c59108a5e",
      "node": "202.wake",
      "snapshot_digest": "c079f6534e3c6fdc6d29a5b35889dc74e8e3466ecbf60c490dbf808030567572",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T12:41:03.013177+00:00",
      "head": "c8a57633cbdb0906aecc76f68df1b950f6026dadb85ed597a0e928d87876d429",
      "node": "203.wake",
      "snapshot_digest": "cd4802da3a016010fde083301e56198ef6545cd83ef40f5317a1038d8eb14abc",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T12:41:15.610272+00:00",
      "head": "ab1ef559264265c00da7a2c2ebe8eb89da484e14cbbbc143788a781a9682c1c3",
      "node": "300.wake",
      "snapshot_digest": "0f3a8e53039f63e1dda848fde770d8d7eb409f49c4910e5b04c735cbfa7659f7",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T13:10:57.985222+00:00",
      "head": "fe98335c6203e7cfc82cfb9b189586811b57bb28ebddb1892aca9c3aa08c9409",
      "node": "301.wake",
      "snapshot_digest": "87a3e8f28ddcf1ed575889091fc80f45adb2eacae2ecef369fc49405b27b504c",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T13:07:40.889643+00:00",
      "head": "9cb513b5f75eac6c9baafb72c521692763a7c71261391aa8d270992c7e2f8b41",
      "node": "302.wake",
      "snapshot_digest": "22d274d944267eb343a6b7a2f17c557c0d62974a1a45efbd2faad8d46f44f4f1",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T12:40:59.234570+00:00",
      "head": "fb417b9351769b955645b46d6bf1b6208fe8d1c734f931973b300e6cc915d26c",
      "node": "303.wake",
      "snapshot_digest": "6ad9a405150d4d97e25eeff7f8c35d824ebb2b260c213c4c562422e2ced253e9",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d32386139333338633833613634356635.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d66656339386162613331336234636263.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
