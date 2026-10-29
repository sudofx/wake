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
  "generated_at": "2026-10-29T02:45:32.045838+00:00",
  "head": "snapshot:98b2299b0d53f9a063040923c1cc23d465b85e207eb87077af9e2d5d7f95cc4e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T02:43:50.596678+00:00",
      "head": "0043bbbad95ed6f9bc8b7d04fe913658409eb6840edac2a06f97047165ad6734",
      "node": "100.wake",
      "snapshot_digest": "be2a8c3f39fe79ad776137289c5190a3688421efaaf6bcba7ee147297648f247",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T02:44:53.418222+00:00",
      "head": "e0bcf0f0668cd3192212cc9ec8369b0d15dd9377e5074d74d3947f35b5595ce5",
      "node": "101.wake",
      "snapshot_digest": "5f0f006ddea1195ad0f70d384681a7798611c5909fcfe75db0ec2c1616916135",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T02:45:05.809362+00:00",
      "head": "9d858a401fcf05556eb5600d1f51346efa8ebfb75710219bc1afdf48079a6fbb",
      "node": "102.wake",
      "snapshot_digest": "e7aceff7ec482e827779b20248a7d6e6bc63dc74dc8867a1711431e9ebea3ac3",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T02:44:58.581169+00:00",
      "head": "53d34c7c3caf947d00f518b42b2efa650d8e176ae4b00982f321166a6d9e489d",
      "node": "103.wake",
      "snapshot_digest": "545544a47d9cf8cf2c19b41ece0aa5305f3f7c058bbdb54fc19d1315311f37a2",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T02:44:18.984558+00:00",
      "head": "67950e7694126d8088b60cfc4e230db36a98311f2f5c8ac9cb2e1823b36b997f",
      "node": "200.wake",
      "snapshot_digest": "aa21735050608184524dcd27a840083dc34b3cfc5eb3559c86f8f188a1f91241",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T02:44:49.108658+00:00",
      "head": "7c674e1a0a11b513a63d2f7586c7f54e3fabb5861deb3146100895bd13d04ba3",
      "node": "201.wake",
      "snapshot_digest": "2791140893d8914db97f9f6a184a68b7999af07e51193a118cf941a1f7e5782e",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T02:44:52.553915+00:00",
      "head": "e1bebfddc361913ff3bef0396a9a0c27e13c81249456c7ae61fbca058a465f36",
      "node": "202.wake",
      "snapshot_digest": "71413469b4119564f822b5f1978048dcd2159c4e75e8368a340b2a6914370110",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T02:43:07.647584+00:00",
      "head": "80709331664bbd6c67003b63ca472c93e3a4502491ebed3af7bb647a8e76c45c",
      "node": "203.wake",
      "snapshot_digest": "7144d2277c5ebb57ee82de0ff3324a4fb2f498015f343b6025a7ff0f8c519060",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T02:45:23.454600+00:00",
      "head": "a832dbe6493d013c173ae740d3fdf34155d2e6a810eb4ed51b07a089691d5b70",
      "node": "300.wake",
      "snapshot_digest": "861d03a1ad44b2692a6437f69f453a3315367b44624aa2684f1f0769815af7ba",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T02:45:12.771901+00:00",
      "head": "3c64e89549e7fd8cf6270ecd06124d508740932a6d1deb9443e7a0292af71e8a",
      "node": "301.wake",
      "snapshot_digest": "b329af62048c6577a52b15c113da3732a1ba8136acfea9b6d4f1094f1df5d2f0",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T02:45:32.045838+00:00",
      "head": "84285ffd919c0de5d0bfabe55a9bb05bba0c22700457459daa9065e30f6dd749",
      "node": "302.wake",
      "snapshot_digest": "6720037aebe7c8a995454954954342f823bf607f070bf4488cc3a1a42a6c45bc",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T02:45:09.854752+00:00",
      "head": "efe7b2a4d8d7f49ab8e26fda457d2429dcaa33b92bfe657fffc31ba3baedb911",
      "node": "303.wake",
      "snapshot_digest": "b8f7211d55b925cdc073bba83ca88c978a6677448ca89d971fbffb48241b2fe0",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61306234383030656566633034623061.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d62323135666235303237623034643063.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
