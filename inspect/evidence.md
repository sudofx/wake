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
  "generated_at": "2026-10-29T10:34:43.102545+00:00",
  "head": "snapshot:96839815928455ad55c1ba4f6bf4bb7a72022acaa3b59436fdf8d24087b94a4d",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T10:20:59.677697+00:00",
      "head": "9bb8f0a4647593edef19fe8c5883564b00c4f53a1976c1a1ee269302e4cae2a3",
      "node": "100.wake",
      "snapshot_digest": "585ffe7ea6b4b7fa31df53887e309ec28ee37d595c5bcf12d2904c6d7ac85fc3",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T10:10:27.713025+00:00",
      "head": "88809f97550de875760939b4cbd5b04a7863a150fd0c6008b271bbc95040495c",
      "node": "101.wake",
      "snapshot_digest": "159c6a0fb7a52354dd2e8695329bff0308dd456b3373157a582cd96900910633",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T10:08:49.432717+00:00",
      "head": "8561037edac6bd6f11602d96cc454abda9b81956b6c7dc19ecbe481a5f42093a",
      "node": "102.wake",
      "snapshot_digest": "f1d25eff68b21d00b95deffc42490993ceae516df2175bc204cf326fdd4dcdfb",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T10:17:31.415886+00:00",
      "head": "b03ed3bc809d200c64c2ea798da95feaaa1ab06a2bae6e8ee77fc76cdda1de10",
      "node": "103.wake",
      "snapshot_digest": "76414367afcf6084dc105d10be0710f27686fd8fa1e3f92daa59fbd3ed5ec5fb",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T10:19:16.068741+00:00",
      "head": "d9c6826175d617420c95df8565d9613f141b38a49ab7a8ba78e60d7f0c866971",
      "node": "200.wake",
      "snapshot_digest": "27a46ae02eca8d3d2abcb955241a953fd6d521adbe424cff98c1928ebaa2dc5b",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-29T10:22:41.906357+00:00",
      "head": "c9778fbddd409bf9d6e9e9f0a0841c45093942c6a0e724650d271aeb6defd054",
      "node": "201.wake",
      "snapshot_digest": "9aafe9b031e3f6d6cb0bd1ee08c8fbd2ee17bf36c56025215f58538bf8aca2fb",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T10:34:43.102545+00:00",
      "head": "3939f81956eff21fafb525f76346263370553fbf0257af838f66964bfef96e54",
      "node": "202.wake",
      "snapshot_digest": "2c23384ce3371013b158082163d85a1b7c620d837345a861b0f6f8ab6256fffd",
      "version": 31
    },
    "203.wake": {
      "generated": "2026-10-29T10:15:41.606298+00:00",
      "head": "82f90813fe4396d7bc0e6fbc579afced1422d1c8f72fc2118611fbf537c1c8d8",
      "node": "203.wake",
      "snapshot_digest": "2b19ba71008847e14f84f8efbeb798bb157d0a98e0504607a0df63e52710874a",
      "version": 28
    },
    "300.wake": {
      "generated": "2026-10-29T10:06:40.036508+00:00",
      "head": "62dcf667ed5b50a6ea7a52d2a796d819f28d834a0774f772593fef8b4c66193c",
      "node": "300.wake",
      "snapshot_digest": "4d71535beda441b0fe9e72cf0f02ceb7d1340bbd437fc190d74ea78cf76b68ef",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T10:24:26.890323+00:00",
      "head": "326a2dfd7ff5246485243f199b42344ac58e8e402dd5e5c75a5342bd97917c52",
      "node": "301.wake",
      "snapshot_digest": "22a7303ea7c2c3ce7b77a55c73033d3e3e8819a9f88c0ec0d29dc7c6b4dab6f0",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T10:26:10.268313+00:00",
      "head": "2bb1f9714419d1cb5573bb049ff592dda8f9230e92f1d1ecb1b4a2e0a6387710",
      "node": "302.wake",
      "snapshot_digest": "49439720a2b95cbfb1db86a792cdaae28f3eec093aca723ca48b71d4bde5b46d",
      "version": 27
    },
    "303.wake": {
      "generated": "2026-10-29T10:12:28.336224+00:00",
      "head": "74ae2da5597a2b83e30c559f942e6613197b716540da55b6d082ec2c3baacf53",
      "node": "303.wake",
      "snapshot_digest": "2ae515dd43a139f0a652088ccc1e5e90ab38d9312144e543daf1a04e99b2cc4a",
      "version": 24
    }
  },
  "version": 287,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d643736323564326466383266343461/39.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d63346231356635666461663934373730.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
