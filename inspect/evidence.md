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
  "generated_at": "2026-10-29T01:48:17.530107+00:00",
  "head": "snapshot:019500df9ddd2f6ea6bcb9d9e9bd35ed9c7fe065dd06754dbef2ad379528837e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T01:41:57.035812+00:00",
      "head": "f01c2ce7deeb2753adc8d616632a1b318c5a46c98e9f883fa4cb72ab4f9144b1",
      "node": "100.wake",
      "snapshot_digest": "401038daab175d12b9578b6eaca0e47d047344e6953fe4052f31b90d612168bf",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T01:46:53.799179+00:00",
      "head": "e4ee87f75351975ca2d7f7d7864b1981e6875bb63a37649f34c4e06b968acf9a",
      "node": "101.wake",
      "snapshot_digest": "f40395b290d1522b021653fc3f3060aed78a80e98b63a4a4a0ed9158e37816b0",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T01:48:17.530107+00:00",
      "head": "396a7f3131fed574ff5c15b164e9aa3a1557336f77848fd22e6c7caf6051c798",
      "node": "102.wake",
      "snapshot_digest": "6730103e2e97c83198d6ca220332b978a275ede76f0020322e310a0c039cfe6e",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T01:42:54.652638+00:00",
      "head": "048b36ed0062b17b1b62851c585f1c2f5b278560f1623eee949fed72f2a26d21",
      "node": "103.wake",
      "snapshot_digest": "d022936f0305811ccee1fc0d53e6c945277ffbe89a893996d93a14d3244f60e2",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T01:41:52.649151+00:00",
      "head": "f94cd78fe8990b5b9b528522b42757c5b80da1562c0ff41b8ae122f2effa6cb6",
      "node": "200.wake",
      "snapshot_digest": "5117c3fde5abf1992741fd323b5b013e5061b94e82e35e8e4d442304900ec8ed",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T01:42:26.237672+00:00",
      "head": "f96dc1e21c71351fd0c1cc5f3ce2c453b544e3803c84748e74dc619bf55110c4",
      "node": "201.wake",
      "snapshot_digest": "8d7bd9500c8a46be6a0515e91163d0f576851f7b21c189fb973decf1936d3d79",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T01:48:10.055581+00:00",
      "head": "ebb823b230dfd02034e06142d53edc20884fe0eaec108f4af89b4562786fb42f",
      "node": "202.wake",
      "snapshot_digest": "415ec6fdb24f71a9b21a4c9b2e1a6b7f09c011fe32156e33ebd18bed3c672412",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T01:46:28.528356+00:00",
      "head": "a9f80c8d55b8bd25db7359c85cce1a4a0a4f9ba549f2dd9516fae1fbcbb313eb",
      "node": "203.wake",
      "snapshot_digest": "649d7215959503ed424957cb51fb2f9906b1a7ee64d0885fc6316f7ab9a8f780",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T01:47:35.582747+00:00",
      "head": "06a71bc08b784c0cf84307b024844411119c9a306b4aa803c1f36471a249c1e4",
      "node": "300.wake",
      "snapshot_digest": "7532b839b63307339dd9d9731f66eeab72dba0619c67487e8304d87eed7b6c3d",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T01:44:54.919854+00:00",
      "head": "092b8fd4ff2d76e362c0e459180c3e3952d820995e49f38edc002c3d51f31578",
      "node": "301.wake",
      "snapshot_digest": "fee9fcf66d7ea7c058a0b3d4d2202e69f73bb3e48c3c986071bdc92cde01c046",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T01:42:38.688188+00:00",
      "head": "b436344f58360ae0d13491829e2b892caf055f469cf02bedae57659c230f3b1b",
      "node": "302.wake",
      "snapshot_digest": "0c8c48a215bc70c3e2f13ada4e9723e90e29745691efc86047d70e4367a67f3c",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T01:47:47.353425+00:00",
      "head": "61fceff00fac0ffdb9f2a7823122962af36515cf53d199a1c85ecbe51f3a70f8",
      "node": "303.wake",
      "snapshot_digest": "8e5fa11b8f1c87ae73d1157cfa936b976e888324c7d58c48a2cd4c349c54e1d1",
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
- [evidence record](../reader-records/evidence/3330302e77616b653a3a722d31393336306364336564326134393163.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d61643832393832616135623734653064.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
