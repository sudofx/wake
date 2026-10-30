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
  "generated_at": "2026-10-30T08:32:58.945991+00:00",
  "head": "snapshot:f424f50f933bf6f28e3e822ac71c673c1d40ee099b07fdd40833a662268605f5",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T08:32:58.945991+00:00",
      "head": "2d983bfc89011648237bc68820c49aec7308447bea8293a73d31be471aee08e5",
      "node": "100.wake",
      "snapshot_digest": "a1edebfaf0146ccee6b620bef5ac418e8cded148716f2c5d151a185840189c18",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T08:01:39.527595+00:00",
      "head": "ae4a281d06d2de9064265145fd6093cc776400fef9be87d5c2efa7bef4a4a3d3",
      "node": "101.wake",
      "snapshot_digest": "af0e755b3dc10c1672bd87163a432f3221cff89f23b72b9a27eb7715b2c0fff3",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T08:01:50.549155+00:00",
      "head": "ebfde70aff9ff1fbf00bcff7a8307e0eac23c4abd697ce022ced8e3a7ecaf30f",
      "node": "102.wake",
      "snapshot_digest": "820a7e29ad56c457c209826a2bee29342ccebcc749f7da3feb2705ee7bc44c5a",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T08:01:51.077195+00:00",
      "head": "fa1d8af1124511f0f112ecf52d44a8a5fd77f4f42b68f8f925f3b62cf376d4f8",
      "node": "103.wake",
      "snapshot_digest": "ca9b08ebc5c36b5316d65584c2fc3163c86789da34ca864fccad0a1b4c79ffea",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T08:01:53.374955+00:00",
      "head": "6c8d1c9b0b50afc9c3bebdff27c92f31d179b32d721508095e3354118f11a69b",
      "node": "200.wake",
      "snapshot_digest": "ce5f1cb5718e944cba66486f4044dfd0cf6fa6228c4af342dde41de6178c0ede",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T08:25:50.800741+00:00",
      "head": "beca609742ebc1f4103cad9d696157bd3d06fbd1d1069ee23939d1863e6be02c",
      "node": "201.wake",
      "snapshot_digest": "976de9fe3aef37e3414cddc776ec7503febff7ff32bd9208dd1e25ce0dce65ea",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T08:01:48.905574+00:00",
      "head": "22e88a7db8b2aa4e8b58de7c25b443b099fcc20cee8b2744e271711ddc94e792",
      "node": "202.wake",
      "snapshot_digest": "1fa65dfd66d880529dad2632f42476c83a74a8a6b598215e5cfa8345962b0528",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T08:01:41.560332+00:00",
      "head": "614a80af882b4d4d4939e00d6550337941f13117fb2ba6278e48e67065c15db8",
      "node": "203.wake",
      "snapshot_digest": "4656ac131b85cad8343ae666b53435b92dc15213b2ed2d90a445ad68ee2b9cca",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T08:02:02.186295+00:00",
      "head": "71d45035d07a1554301ea57981b4232876252409102511ac41b6bbbd735f6de7",
      "node": "300.wake",
      "snapshot_digest": "103f47a1e4c68c2544d11104d87b7783e073e550bdb35b5bd0a63d74278984e6",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T08:31:14.312233+00:00",
      "head": "5dfa0a6dc52d157b3167ea5666b5d37212684fe14b5b2edd995ba73ee77a74a9",
      "node": "301.wake",
      "snapshot_digest": "4caa107a97dd10b3143191942de5963c76c85edae120422fdad93fabc4cf66a1",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T08:29:30.722293+00:00",
      "head": "2858794f742c26f3be2d30b72acddf75b2af3b734a6978eec38f956c5f13d412",
      "node": "302.wake",
      "snapshot_digest": "bec45c7b079464d938c8e22ae2d13698be17c15dcb5ee39341d75f4b15aaad07",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T08:01:44.434150+00:00",
      "head": "04bcca4df0f53797e71f39c80e2ab77c1ac56702016f8a20087e1281e63b9b36",
      "node": "303.wake",
      "snapshot_digest": "53a434f0199fddffb597639d31cccf0a70235077402e7d727bc96a312ed2a6d6",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61313366326131396436376434623764.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d35623165616338623236366234643933.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
