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
  "generated_at": "2026-10-25T19:44:27.771524+00:00",
  "head": "snapshot:5d2e34867e3d12ad46a266d0ce7211f861c09fd8dfd1b1280d11c75e846f04bd",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T19:18:07.844146+00:00",
      "head": "f30e504593b8eb70c85aff9e403ea6c1f2f490002fc1886dd444c96b8b976dec",
      "node": "100.wake",
      "snapshot_digest": "4983acaca95f41a28e39d8686c3910b7b115f2111251ca7ab9df0a5931b02732",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T19:36:51.708084+00:00",
      "head": "48dedc900c095cc955fa8de178baeb03a89233062e8157ec3360851561816edb",
      "node": "101.wake",
      "snapshot_digest": "04ae032fff224de49dbb57d82fd73ead932a0f340e39df3f2b6709d03b587d35",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T19:34:01.291787+00:00",
      "head": "1b8941f97058dd8178843835440a485295fe78fc8fff25f74eb6a2c21a929bc5",
      "node": "102.wake",
      "snapshot_digest": "1ff8ca8275841a978d2c9c52669f0c7e3f9802f47846bc7949dd09c72558b56c",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T19:37:13.782232+00:00",
      "head": "ba1ed693cd78e4b26744fdfc738c9eaccf49a86f561aad34073b48284b051bb5",
      "node": "103.wake",
      "snapshot_digest": "b9c97cd187651f546807dacc186ac5f7e408bec1891ef158a3d9a9ec9e78fa68",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T19:36:30.429058+00:00",
      "head": "29d964d84019f423a047fb03d1873840cd65e495784c5f19e00b0eba34f9bcff",
      "node": "200.wake",
      "snapshot_digest": "14250261e7caa655c33b13559ccb4ea1c58237d4265b5e9d5967150fa7125dd6",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T19:36:07.916940+00:00",
      "head": "6ced0992bc8012a1bd2b1839bced9322d406501eef854c6313133c95cfe10f4f",
      "node": "201.wake",
      "snapshot_digest": "ed34073817b715762643947b8c879354089bea9a00140cb358c71cc3ad8cd08a",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T19:18:09.202406+00:00",
      "head": "c2357c226eb4a7f676a40ffea5b4e0a3ca7d3f7efad69001006dcfe0b9c868b3",
      "node": "202.wake",
      "snapshot_digest": "193154830be5ac0ab7667d9c6105d344df6ed63f79cecac352cff9a4c7893818",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T19:18:07.957511+00:00",
      "head": "876b5881f5c65ffe092368e3846807339745afa396c802e37213a8420eda21b7",
      "node": "203.wake",
      "snapshot_digest": "20c2562f19d332e9c94a807c742d2edbb9fa8cf528de3593f35753712f3e04b8",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T19:35:49.303347+00:00",
      "head": "a2a8595fa252bee371e35fa221098a2a5e41d3f8a0eb2943c1574b7c0fe9c5b1",
      "node": "300.wake",
      "snapshot_digest": "4a8b61853ad36ce8b65c5b6e266373030e8f8ff551df4fbdb56d2eb2c0d10d02",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T19:44:27.771524+00:00",
      "head": "dba4f987b3940801e3489a0f9c33610c073027cbb29939f39d118d2ec7ad4973",
      "node": "301.wake",
      "snapshot_digest": "98c4af94eca8bf082abbe6e1b3374cbad8ca67e52a66aa31992abce41b0edd80",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T19:34:26.813305+00:00",
      "head": "f8e0273dfe0cba0f9438f6da83036c2e77842a9662aa3e4de4abe189df7c8e5b",
      "node": "302.wake",
      "snapshot_digest": "6d4b8c47b01e5413b227046762d74c13b69c957950e43cb7047dfd46a5a92b5a",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T19:38:04.219896+00:00",
      "head": "c476d562597337bf995069d15903f61799d372a592b84d4fe82f7d61681438e0",
      "node": "303.wake",
      "snapshot_digest": "29ae3b636b316b3fb8814a66e350cfd09085137a8aa38506aae150be9bef23db",
      "version": 51
    }
  },
  "version": 510,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d33666236383963376336326334316535.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66393765326466373037613334313163.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
