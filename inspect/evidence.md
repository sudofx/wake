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
  "generated_at": "2026-10-30T14:46:42.296366+00:00",
  "head": "snapshot:27edbf379f1e815206ee2c3a8d8a24ab7793fe20eb6beff164d734fbe6f916ec",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T14:42:57.034492+00:00",
      "head": "b8158f216179df665cdb130f55ff143c56901fa1625c67ef1d19f43c03df1e41",
      "node": "100.wake",
      "snapshot_digest": "50e191be8ae23e8f2599239272af41a29dfc58dbbd278609b3b7870d163f4b63",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T14:44:11.420984+00:00",
      "head": "89cf73447b618864e13db80d5f9829afa4d6f52bcb04f0d180310d1d8b39dbcd",
      "node": "101.wake",
      "snapshot_digest": "b1aa1fe5d77e50bd7cc617f165d46a392e81ee4b8a6e0b3ed88e4c03e5b1a3a6",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T14:44:13.451184+00:00",
      "head": "520e219cea1e6086617026c6d5af8c853518d0f0d01edbc35855ac1cadf4271c",
      "node": "102.wake",
      "snapshot_digest": "6463d19e4e71d7697f2968432db465c8653871edfe3882e2480351fd6c493687",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T14:44:14.070002+00:00",
      "head": "e1d77366b6375b11e1902d8271be6e2ccf0ea7b92e9728e3c99b6905b34474ed",
      "node": "103.wake",
      "snapshot_digest": "661a3878620e629a0971840e14ba702056fe932d701b429c779dc6f8c8470493",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T14:44:26.609654+00:00",
      "head": "0c528bf25a2f725db1e4a34c5d4cbae75a00139e6af7591bd6a5c5e17d242cdf",
      "node": "200.wake",
      "snapshot_digest": "4f4ab223140e31d716fa41ba168f1fd074eab1746d185aebf3ae3e957868351e",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T14:45:24.417999+00:00",
      "head": "0bf22f2500ca4117efad6046f1ad7c1e7fe50e7ad31a03edb0d20a3d10ef4b7d",
      "node": "201.wake",
      "snapshot_digest": "4ecd4f4b7e7fa7c49a2dcf70f82aa29b232604d5294c9ee68b20f8d26c09faca",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T14:44:04.764148+00:00",
      "head": "1b5b27ab4ea93f2479ed1bc0e6ef4f675c940f7e36dfcecee6fb4b655854fd8e",
      "node": "202.wake",
      "snapshot_digest": "415434583cf87c6b6ec3da8abfc0d07e18d95568f2ca9fb570522bb458de056f",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T14:44:08.925555+00:00",
      "head": "596f2c8dfc29e52b30b00f5bc47005fda1d8b92a2485d79dba108f1a044eeca4",
      "node": "203.wake",
      "snapshot_digest": "497df93e64ca695d8797abbcb666e4394bb938a869c17a4fd25a991f6e61a2f8",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T14:44:21.836371+00:00",
      "head": "5ec943f4e4874db22dd0f264fc19abde887d684351fcf29ccb9cf72f9ee5bec3",
      "node": "300.wake",
      "snapshot_digest": "39594c46e810f79910f488163304cb1d4ef3c7a38061f28c1a11fad05c97707a",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T14:46:42.296366+00:00",
      "head": "202de3daa04cfaa57258dd08bb68fca0d86469769c9a3c2fb7327b0bd2a5595b",
      "node": "301.wake",
      "snapshot_digest": "cf51a1b42ff4b1f995cfc452a7615dd3b1395474870138d895e649ad25f1b373",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T14:45:39.404039+00:00",
      "head": "ebc87b5b53027f23d98c9e0274ca21cb20603bced1ea0557df354655e0c957fb",
      "node": "302.wake",
      "snapshot_digest": "cbede05e581e7c80565ba12762a07b7eedd45c204b45958180a13067f1f86e5c",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T14:44:04.471362+00:00",
      "head": "1144a106521ddf2356c619c88998ccb8b3e0a39b7ad681c48f8576e72ab2fa63",
      "node": "303.wake",
      "snapshot_digest": "63dc68b48b4cc785cb93a9fddedb2819d20ba469869ee50a2c106bfde7eb3df5",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61336262666633336430313734323133.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d34633066613030633062356634623133.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
