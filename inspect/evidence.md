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
  "generated_at": "2026-11-03T23:26:51.418135+00:00",
  "head": "snapshot:469978ec1b2d4527f172e2788df0d8877d10d463d11291a32faa6806cc8d1321",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-03T23:00:44.815167+00:00",
      "head": "d7e2d1efaa0cd29064f42165e876f22cc45ab9e3d3ff5ac6b36012ed2f43444a",
      "node": "100.wake",
      "snapshot_digest": "c772edf8963372810b37a0df7d5a95e807d9579113ca688fa4b1ed3c8002b468",
      "version": 4
    },
    "101.wake": {
      "generated": "2026-11-03T23:00:44.115972+00:00",
      "head": "340720f1af4bec202f25c96366a6c86140f97736f8e3ba331ed40829c55bcdb3",
      "node": "101.wake",
      "snapshot_digest": "b29f2a6a45bef831e6aec1326e3b35e36dfcad59dfc6899b6d525906acdd5354",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-11-03T23:09:36.849284+00:00",
      "head": "11be8481eb98b2154db0e0b7595cfa47ff90ae2cda8e32e4551c88b3ceb7e6f6",
      "node": "102.wake",
      "snapshot_digest": "99c48d80b915866d21deb28c27fe6863403f871b1be7295ec222bd3d5940860d",
      "version": 4
    },
    "103.wake": {
      "generated": "2026-11-03T23:11:15.914599+00:00",
      "head": "7592ba7d8bc75383720ec2df329b0d5f379ce36b316b2aa4b7b993f50f38ea7a",
      "node": "103.wake",
      "snapshot_digest": "bc3dd91798ad0089e19f75ff6312591648e71b321e8fef15f4447b208f84f96f",
      "version": 4
    },
    "200.wake": {
      "generated": "2026-11-03T23:20:02.536713+00:00",
      "head": "9d66701261f17c79bd670afc5ec19cfb49cff4a01555d0b2ac3753672c779d22",
      "node": "200.wake",
      "snapshot_digest": "f9c37d5d56360c19cc36d6be91b5d2508fe569b20d9d082785d78696a4d65c67",
      "version": 1
    },
    "201.wake": {
      "generated": "2026-11-03T23:00:44.534853+00:00",
      "head": "fb43e3510712572d18575540883fa108a9c939cd05a2fe944742745ec261d37f",
      "node": "201.wake",
      "snapshot_digest": "7c53fb49e990393c295064cb2d70cf9e1cc7835527f8d104b6bd38fb091e2dd6",
      "version": 2
    },
    "202.wake": {
      "generated": "2026-11-03T23:26:51.418135+00:00",
      "head": "716fa8ef1d0e915c1b36549f26d617bc2eccfceca6e86f9add840048288271d6",
      "node": "202.wake",
      "snapshot_digest": "a0c2bf9094657d1c28514728d79a17adce65c238aff14e5ba83f8e4dafa90057",
      "version": 4
    },
    "203.wake": {
      "generated": "2026-11-03T23:25:09.483756+00:00",
      "head": "703be4c51d6b31d94b44afd259d3a9adb68582753a68fbccd34ec49f6b9f3c87",
      "node": "203.wake",
      "snapshot_digest": "c8e2cfc288397a58f7da275194e302832bb3185b08d7c8749b91eab2ff7ed0dd",
      "version": 1
    },
    "300.wake": {
      "generated": "2026-11-03T23:00:44.284752+00:00",
      "head": "9efb9b3d009aa35fc9e1486afdf408a621163ac9b5a8827294f7a7bce276f945",
      "node": "300.wake",
      "snapshot_digest": "d28add45d48cc3dc7cfb7b75a9a92f798979aabc65d39c1891d0dee6554c691f",
      "version": 2
    },
    "301.wake": {
      "generated": "2026-11-03T23:00:44.189508+00:00",
      "head": "d79cc98a6585deefc99f5e984c08990c70109af900eb2a4349ee7e8615906e62",
      "node": "301.wake",
      "snapshot_digest": "272f781d27b1ad72a410f7d7b4d7063536ddcd7b8a1babfcfc7f2bbb94b57930",
      "version": 2
    },
    "302.wake": {
      "generated": "2026-11-03T23:00:44.497102+00:00",
      "head": "105460cf6ccd86f76799be087e8c376ddd97ff6f6328b18275ce9e65010e1d0a",
      "node": "302.wake",
      "snapshot_digest": "7f0db0bd39f804e05a4f28239b88ba15e6a9543dad705367ef88cb38ff689d73",
      "version": 1
    },
    "303.wake": {
      "generated": "2026-11-03T23:14:45.457578+00:00",
      "head": "21c3c2c82931272d2afe5708fd1a145444315977f44f938576bc7691556e2880",
      "node": "303.wake",
      "snapshot_digest": "cfec95dd31fe503a9bb3529aad9c10f6ecd25b0f27d7e0c57d28f8e45188a802",
      "version": 4
    }
  },
  "version": 29,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d66386266623733663863346634316637.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d66363434383531393638376434303035.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e6f7465626f6f6b2d6175746f6e6f6d6f75732d6469/73636f766572792d696e666572656e63652d626172726965722d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
