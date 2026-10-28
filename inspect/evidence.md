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
  "generated_at": "2026-10-28T15:28:16.933417+00:00",
  "head": "snapshot:f492a5e2261cae0b60f29a095a014de3f7a8060d5e62fc7d02fe0d2e5688732b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T15:21:42.537984+00:00",
      "head": "e2a04efde8b585ca23a85b7450873875b678f66c8aa40f5b4c8c490dc9c817a7",
      "node": "100.wake",
      "snapshot_digest": "fd197a09ce58389bf04a04a4f67c686d9867086b23384783d95c09212c0ae8a5",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T15:16:52.877712+00:00",
      "head": "e1ed2abd377be89c78f8d0f986ff6fb1cc5c195cf4be00103b1535263b34dddc",
      "node": "101.wake",
      "snapshot_digest": "f089d1374cb2da6a3e9c1a42091e686bf09c2e47ee8b87ce19080151770518a5",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-28T15:23:13.354630+00:00",
      "head": "f4fce79f650c2025d7027e95808d538510e7d4cc2cfe158489dfc8b8189b109f",
      "node": "102.wake",
      "snapshot_digest": "31567a7bff1a945ea1479575f91538161be65e505fec250ae5171959e4f10d80",
      "version": 16
    },
    "103.wake": {
      "generated": "2026-10-28T15:21:21.841675+00:00",
      "head": "50c348909a58d3bbf1e9ddb676d05314f651bfe729dfe2c5cf88d3dcd588dc18",
      "node": "103.wake",
      "snapshot_digest": "ae35081056e1086e0ea93ea12698b37ce01e0ddaae8b0d7506cf045d61a38662",
      "version": 27
    },
    "200.wake": {
      "generated": "2026-10-28T15:23:42.242043+00:00",
      "head": "667594c97711cf20be36de77381c9eff8c3d27ec3ebf38a1834403a4bc843dab",
      "node": "200.wake",
      "snapshot_digest": "75e77f49f65153cb026b20023ee2b6958b62b7141f1c658a417adf41a046be3b",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T15:21:51.789517+00:00",
      "head": "382873daa1b103f29d29eb729e694feaa7b06e1d29f9bab236f3234fc5b45c06",
      "node": "201.wake",
      "snapshot_digest": "7e39413136bf2695a87041cef491678e3f17828ba84522c9dbabf45994a2fa32",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-28T15:22:32.416250+00:00",
      "head": "a05b94f97f6283f1ad4ab515989fa6130aecdfcba0ba76afb8edef282b8d18db",
      "node": "202.wake",
      "snapshot_digest": "527f909a1e33fe8059a9666c4c317dcb0590f1c33539e3d6c228f13416bc9f0e",
      "version": 28
    },
    "203.wake": {
      "generated": "2026-10-28T15:17:23.748062+00:00",
      "head": "d14df2772f96114b4c426b1d4f7939251b80c02cec2895ed8b10fbb2e4054bde",
      "node": "203.wake",
      "snapshot_digest": "26b242948dcc2dab03dfd353468c29df07ea35ca889e1211e4ea1d1f2d2f1045",
      "version": 25
    },
    "300.wake": {
      "generated": "2026-10-28T15:14:54.013742+00:00",
      "head": "cb49dbc1b5f4de909500fb8fdbe4abb8e9b6d058f8bbace6d804d096fc45427e",
      "node": "300.wake",
      "snapshot_digest": "4424ffa351a8625e214dfaa5bb9cde4f3f70b6372031e6fae2d8f369912cde41",
      "version": 23
    },
    "301.wake": {
      "generated": "2026-10-28T15:27:14.131699+00:00",
      "head": "5710ae08141d1187f76bf04df7debae2bb0ed3e54b945c1eb0640f92fd8c4a90",
      "node": "301.wake",
      "snapshot_digest": "a598285bba168d4d1b2592bebd8606d0e63987266cab0de7e08e023cba7649e0",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-28T15:28:16.933417+00:00",
      "head": "c5aecfe85c738185a10ca965b3ad131b772aaf1547cf14390ef78d513c87f798",
      "node": "302.wake",
      "snapshot_digest": "902b392f873076db33d662608573a22eda7001a9ad7a890e37eece909ebda565",
      "version": 24
    },
    "303.wake": {
      "generated": "2026-10-28T15:16:18.117947+00:00",
      "head": "78f85d97889d6ed68a392ad6e90d463768de07e20e138bd7ab9a0fd4320a03c2",
      "node": "303.wake",
      "snapshot_digest": "008ae4d59583bbc594a126154d7ddc1a4223f20694d604ef8b8c5bcf55e680e5",
      "version": 23
    }
  },
  "version": 269,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d30616361646235383035336634633062.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d386533393834353736343930346133/31.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d6f62/6a656374697665732d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
