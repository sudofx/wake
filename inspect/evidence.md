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
  "generated_at": "2026-10-26T21:35:14.235506+00:00",
  "head": "snapshot:64648c93c0a521c847b3d787429a7edf646ac723b6ad44ef24facdc027874a72",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T21:24:38.419696+00:00",
      "head": "24ca517dd378af8df2c1a0855258a02d01935641756552a9f8f21c6661480799",
      "node": "100.wake",
      "snapshot_digest": "f9e40d9594b3da10f5d480bc960036a7521c9e2d9b7571232dcc9f007a1de5a8",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T21:28:16.013795+00:00",
      "head": "c212366979e3dcc9d934301ea2522b894ccdb575767c4a9b7d16610b99582ea6",
      "node": "101.wake",
      "snapshot_digest": "fc6dde5e22015445c0e458b9fb7713a007172e4b74972d5b961028382d327f80",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T21:17:29.385653+00:00",
      "head": "8efcf521fcef90e5e2f2f322697153d3f01ddc0cf503301a099044547b7aa419",
      "node": "102.wake",
      "snapshot_digest": "24eb581112e7ff9ca53972e168ff273e58c78dd99270cb1187ab209ac3f6867e",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T21:27:28.648317+00:00",
      "head": "9be9e63c7899c897ebf7f385e6c45d0f763c7b3ec36c7cb5cfbfce4dd0cd3da9",
      "node": "103.wake",
      "snapshot_digest": "6c2a68f161d9ed5c661e5ef76544cca6bea3351ae0bb14e39d72f3c64fa0936e",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T21:06:30.374407+00:00",
      "head": "f0d72d3af64543e15470afab7746a2beb53c8ff6552f30011f9557ba708ad183",
      "node": "200.wake",
      "snapshot_digest": "78fbe0e91316c80ac2b27e7220f9c2242ac2b7238f773129d5053116e2c558f1",
      "version": 45
    },
    "201.wake": {
      "generated": "2026-10-26T21:35:14.235506+00:00",
      "head": "291dade813a94bdcedb12c076af02cfc1f63085eb93b2cfec41bb0a50416aaca",
      "node": "201.wake",
      "snapshot_digest": "b3f60a8bd2d0912c120788e666ea30a1dc980883042ce40743eee579b21155da",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-26T21:09:06.683241+00:00",
      "head": "3d159c73fa25dcb15339215d57182ef7ec272507588986f83adb0a77f178297c",
      "node": "202.wake",
      "snapshot_digest": "2550390b568a78cca3fc7e17c23d7966ad0ec9108b50497c2c6b6a89d9e05c6a",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T21:18:05.504738+00:00",
      "head": "421313b5d3be3e42f3db2d464e9816f62b5be99559719757806cbceec6902c70",
      "node": "203.wake",
      "snapshot_digest": "eaa392b6a1fdf475f408a4b2a4fda8346985b94a5bb85ce183a21887150a452c",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T21:21:50.479907+00:00",
      "head": "30dec9ce55e6d2ae22ff3ea7e6411fe8b5884eed2d4a19abf733ccb45865168a",
      "node": "300.wake",
      "snapshot_digest": "52eeb81daa63dc2ecddd6e29420c6731318dfd980df71e68b2a861c6255bb4bd",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T21:28:33.251655+00:00",
      "head": "95d3fcc2ac68951551879c8c116695a500b53630d9d1b0605ecd3db369cabb0a",
      "node": "301.wake",
      "snapshot_digest": "7cb351ccacf868161dabd88a7f1fbbcedb3a38cc21912da1a6dedbe776ab8572",
      "version": 66
    },
    "302.wake": {
      "generated": "2026-10-26T21:34:43.929484+00:00",
      "head": "ff785c6e61ae9abdce494fed7d337ccd42be86c5d72918f4dbc8947b65ca385f",
      "node": "302.wake",
      "snapshot_digest": "ff7171f5a8a8e1b2f61c45d71b562a309191086b0c1c3f47082a93fdcc75c847",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T21:22:06.538864+00:00",
      "head": "b5b38809ffd03bc07cb1ea16438933c0b2004e5aa574dcca82dc903b5c6adffd",
      "node": "303.wake",
      "snapshot_digest": "6c27ef9950caac18bc80d0c578aa2f9ff72e1c586108a3fd9d1ff349fd905ff5",
      "version": 56
    }
  },
  "version": 580,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d34356265663933663038656334646131.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d35326533346234326264303134613939.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
