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
  "generated_at": "2026-10-25T15:46:33.130185+00:00",
  "head": "snapshot:5be4918865338a47d617cb6f7ab017f0c34a37d05b00cd025a886466e44e1d6e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T15:35:20.146500+00:00",
      "head": "4dfe6cee24f8230da979f9b339b1dffb395f1ef2b5d44cac90c2de9a7b31a5b9",
      "node": "100.wake",
      "snapshot_digest": "4f82baaa98ff5f97136715182a09f47cf9a613b0799d10d66c33408e7cde0e0e",
      "version": 27
    },
    "101.wake": {
      "generated": "2026-10-25T15:36:12.009630+00:00",
      "head": "f8b357e3ec1d26974fd41ca1432f33f2eef65acd83621283b47c0f2662c3f233",
      "node": "101.wake",
      "snapshot_digest": "214c69b3ca096f0d97fb4fdf8f2a92bc42c2bcd9e8a6acb8c3aa95b1c6fffd52",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T15:33:01.765622+00:00",
      "head": "99bb6b3446a49decea2467f8ee8a26be99b4ca01bd4d810ff876a5ff81edbb99",
      "node": "102.wake",
      "snapshot_digest": "49240c7799c38080f543729c804458f4faf6122aad57221a1da6dc06a710d532",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T15:18:08.557235+00:00",
      "head": "6bd5e1fcae65d778b16a90cadc970204e3cad3e74e6915f50f3966ac71e70052",
      "node": "103.wake",
      "snapshot_digest": "e9e19712eb372cef5fe4c5c48c82d5e02a53460d45bc4c0e4ddfd0e6191f7498",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T15:42:55.312977+00:00",
      "head": "529eaf6bda2b46b322dab96de7b44a1d24a5d912511b22abe53b1c6add8ba967",
      "node": "200.wake",
      "snapshot_digest": "9281460a510b8e516fa7a9d83d0923c3fa1e0bf12983c66bf965d2bc1ca847df",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T15:18:09.880782+00:00",
      "head": "94d07a2673ef0af6b4cae83e5036f1c8cfdd4b264432c46eb00866f19fc15f39",
      "node": "201.wake",
      "snapshot_digest": "591d994824882330e2fe7cb59ca2535933a7b53a7ddf70fe36abb3c438421c06",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T15:34:44.582605+00:00",
      "head": "a413c25ebfabbb665f73721022b6299cbb41c3feaec41e0a703f2788c05fa066",
      "node": "202.wake",
      "snapshot_digest": "bb8776794331f6476fd42dcf598da7d21af0d3b85334c694c60a27432a71dd0e",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T15:18:07.505340+00:00",
      "head": "58f214295b3a9607bbd67d7385d3b9c2925e2e616051d690c272b100daffe2c1",
      "node": "203.wake",
      "snapshot_digest": "377dafe7560ab9e647c5330580054b2295188286843c5a7f660bee05bcf799d4",
      "version": 30
    },
    "300.wake": {
      "generated": "2026-10-25T15:18:08.295898+00:00",
      "head": "9676b30729d72b311524b85eb8d0006abecc8fb28242d2874f14064208250770",
      "node": "300.wake",
      "snapshot_digest": "421a342fc858f6a96eb62c23344d986294560999f43646ba5303c3256746af66",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T15:45:03.875821+00:00",
      "head": "fb8fecd3dda3d6d0cbdf59c450729f13600660befd268298cb0f47b64ba5b24d",
      "node": "301.wake",
      "snapshot_digest": "f4c399145876bc4dd95d0d0981b92a1665add61b71eb234e981eb89334c85d85",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T15:46:33.130185+00:00",
      "head": "12979c17194aba7b1c85d13e6811d1e7ea034c4b77f98b3e607db8430de2b786",
      "node": "302.wake",
      "snapshot_digest": "afb489392d96edfa19f53f4ef9ca1775a8e2dc529d88454d1ed00c16ed40ca77",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T15:37:06.945038+00:00",
      "head": "19d2b4a94ca26271653d7a8deeca2b329985eb08a1130efea14677b25c6306f8",
      "node": "303.wake",
      "snapshot_digest": "567b6d8458ecb8314973881322850c14bc47dca58c29d14b3ba2e061c79996e5",
      "version": 51
    }
  },
  "version": 508,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3135.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3136.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d30346239396134383965623434343463.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a736f757263652d636136613535353665306235346532/37.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
