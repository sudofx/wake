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
  "generated_at": "2026-10-27T03:37:57.333414+00:00",
  "head": "snapshot:41c6dd67be3877370b8ffe6311d8fa4a167ebe3d4a1556259919a356a2a8d72c",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-27T03:37:50.991764+00:00",
      "head": "9dd2f4960560b7f8e1805e9a5423a1378c448b03bf853f5bd45a0735cd783217",
      "node": "100.wake",
      "snapshot_digest": "ce0f00795b74178d3c93c709e7751a8f14c0066b46345aa0a724214c62a339a2",
      "version": 33
    },
    "101.wake": {
      "generated": "2026-10-27T03:37:52.547332+00:00",
      "head": "74ea998f9580135390952db48376871078b4f246a0f7663468c6bbc7b46ded98",
      "node": "101.wake",
      "snapshot_digest": "b9e98855ee9716a67f6cf579b874d20d38e3d7d718f94fab9faa6eaa53cdb445",
      "version": 49
    },
    "102.wake": {
      "generated": "2026-10-27T03:37:57.333414+00:00",
      "head": "7b759a9b8f5deb5bda4f61bbdaecf2cf5ae16398599fb912583dacedf2adf988",
      "node": "102.wake",
      "snapshot_digest": "cec17803da50f93c4412902800bfc05b990b8761044f1af3e83555fd67ba0f51",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-27T03:37:53.520684+00:00",
      "head": "1670511b8f7372ae71577837f8b51af5af49076e4001feec0bbe8b7a2338ff1d",
      "node": "103.wake",
      "snapshot_digest": "0424b06affb0502114c84ca9ec60fed52f6df1fd69c8cd1f07e50fb3b55c0f13",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-27T03:37:52.075852+00:00",
      "head": "3e0d579277e5746277884d72118fadc996dbd645aa5cecf6e6c2843bfac6cadb",
      "node": "200.wake",
      "snapshot_digest": "135fd1594c2d96eb1e21a2f2d82a0af55160724bee69afec476355404e27432c",
      "version": 47
    },
    "201.wake": {
      "generated": "2026-10-27T03:37:52.917506+00:00",
      "head": "8f3b2c4cf702b1163d4b065c75040eaceabb107aeba8399270c84a78565b03fa",
      "node": "201.wake",
      "snapshot_digest": "c17020162cdacdcb6a843776b4fcda6e39a84a044016f5bcc5396b62c14f6af3",
      "version": 46
    },
    "202.wake": {
      "generated": "2026-10-27T03:37:53.745146+00:00",
      "head": "c6c0a5ec583b326d3c8f7c0e3498285b791cd540c82bea46c2b753dd5efde560",
      "node": "202.wake",
      "snapshot_digest": "259ea6ea2ce460141f82dff49b2eb7d5ef5c299d5d5d3dbbea31f8a814eae54c",
      "version": 62
    },
    "203.wake": {
      "generated": "2026-10-27T03:37:52.254655+00:00",
      "head": "20303380c3b23de25c640b27cd9b6fff46d767b614b0630579b5e956403c367f",
      "node": "203.wake",
      "snapshot_digest": "a141ea8a1a7b58cb0493ee245dbbd55a7e236aa6a0c809a53c6aa2b5ad683e89",
      "version": 39
    },
    "300.wake": {
      "generated": "2026-10-27T03:37:54.138004+00:00",
      "head": "7a37bb11a86cf431bb1df784f450a91fb179136077e97b10eed2b0649fb61fe3",
      "node": "300.wake",
      "snapshot_digest": "709d1e9c429973ae334fb116b756ae597a147cbd9c3a237ffdb21b93bb4f6d96",
      "version": 40
    },
    "301.wake": {
      "generated": "2026-10-27T03:37:55.189774+00:00",
      "head": "c143eeb574018f5fb2628bfa9ee60c39af7e4e6d902b7ca3d7e595bd5f8fc5fe",
      "node": "301.wake",
      "snapshot_digest": "13369fedc3aaec60ec14b043278cb930f594c5239c7b3a2aab0b7a0011057a7a",
      "version": 68
    },
    "302.wake": {
      "generated": "2026-10-27T03:37:53.491034+00:00",
      "head": "045f8d1fd80ca73e5373d7ee856c93fd14bec6f82feb723536ffa2a617f31dee",
      "node": "302.wake",
      "snapshot_digest": "2648fc90241f9f0b597cbfd0eb2c250270f0c5cba182836618d223497728a330",
      "version": 49
    },
    "303.wake": {
      "generated": "2026-10-27T03:37:56.715364+00:00",
      "head": "ad514fe212ac3da3e36e3c7a49319569278675fb959f128d73115525bf5569fb",
      "node": "303.wake",
      "snapshot_digest": "c993455700977681d2938fc80bdbdbebae380f2a37f97f5870930d4e7153fb76",
      "version": 59
    }
  },
  "version": 600,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d62366362626361623431653234656230.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66333163353836663431633234386330.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6761/702d69642d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
