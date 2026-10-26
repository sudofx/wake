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
  "generated_at": "2026-10-26T19:12:14.091165+00:00",
  "head": "snapshot:a5ce4cb581c8cea5d6bbf1d6580f3ce31fb09fef3d301125069b475184ca106e",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-26T18:53:51.194916+00:00",
      "head": "87bb6ed3d22ac0d5d5ba7b6a700682c5b275bbecc9dde963064e8e9db6174e1d",
      "node": "100.wake",
      "snapshot_digest": "a500c57ff0dfb0dca4c53396ed42ddee3b02fedf224c8284b9c84388958e0ad2",
      "version": 31
    },
    "101.wake": {
      "generated": "2026-10-26T18:49:20.959378+00:00",
      "head": "de40943097641219c2130d6f654f4e43e6cedbc851c45f08a9153e8217ff1612",
      "node": "101.wake",
      "snapshot_digest": "4067d667240560b46c110d532e28224ef94f1ff3598085dfab273fa6eafe1bf5",
      "version": 48
    },
    "102.wake": {
      "generated": "2026-10-26T18:58:03.707280+00:00",
      "head": "beb8974c56c342d86a2520f62146c6a0d183a280c98156faddec7c7c527c5886",
      "node": "102.wake",
      "snapshot_digest": "9c6d8d1f2faadf9dbf3c583a65c3bf327ef458d5e5994f4f1e483b96c3ca613a",
      "version": 63
    },
    "103.wake": {
      "generated": "2026-10-26T18:50:47.198153+00:00",
      "head": "510fc80db2e9c1556386911d509b83189271657048d91db86d3a49238d5338a5",
      "node": "103.wake",
      "snapshot_digest": "e2541c2de03d12c587d15722fa669e400985c05ec30821adfece1035491eabab",
      "version": 45
    },
    "200.wake": {
      "generated": "2026-10-26T18:49:02.830154+00:00",
      "head": "6c01e17643d7e04a25d2a96c0371c93ea01f21faddd39a058b9eb6ca04eb6664",
      "node": "200.wake",
      "snapshot_digest": "d6466c251e6f8353d2b28db860834207831d50eac7adc70094374d634b00617f",
      "version": 44
    },
    "201.wake": {
      "generated": "2026-10-26T18:24:21.722759+00:00",
      "head": "dfb7bfc2e766785399a739c9304dcf9082cc9c93fa61a1935ca4feb6d75f3256",
      "node": "201.wake",
      "snapshot_digest": "f21be0a9e7162762067b83e02f4c2c5e53899c6883718de0ae8deac4db579662",
      "version": 45
    },
    "202.wake": {
      "generated": "2026-10-26T19:00:56.273080+00:00",
      "head": "efecd074ae6e94f280d73f2cda180614641b8658ccb907913ce9671d507fddcc",
      "node": "202.wake",
      "snapshot_digest": "063ef310bb716d0f4784d3c1929ff99b00af57ca6d8e5e9c4569f5079296308b",
      "version": 59
    },
    "203.wake": {
      "generated": "2026-10-26T19:01:48.002186+00:00",
      "head": "b6e51e20a6ae5ba87cade8a0250a34e2ee7c48b5226035835616814192294570",
      "node": "203.wake",
      "snapshot_digest": "222bf3e8c3c59b18eca7855c5a959f56e5f1675dbac67be056403089a4865bff",
      "version": 35
    },
    "300.wake": {
      "generated": "2026-10-26T19:02:07.348719+00:00",
      "head": "6496de833822b43860353e30fa1ff3116c049e25762e05b383161e06925ec48e",
      "node": "300.wake",
      "snapshot_digest": "4391109ffabdd643e42b84fc91f8f326eeafcadd8d39a73bd826d44776e8e7f6",
      "version": 38
    },
    "301.wake": {
      "generated": "2026-10-26T19:12:14.091165+00:00",
      "head": "ff52923c0088d526baab8e8b0d8dbc50eef78bc5c49425bca245d83a8697a504",
      "node": "301.wake",
      "snapshot_digest": "7d30de971c42bfac94fe48d378a8c463bfc33a1d3528ecb73ae723cb297fedd8",
      "version": 65
    },
    "302.wake": {
      "generated": "2026-10-26T19:05:09.724364+00:00",
      "head": "0c0d6804b79c82d621436ee43d6c46c1aa4fc6880b9fc93dba0e90ee27381e03",
      "node": "302.wake",
      "snapshot_digest": "0cfae8ba94fa8457e3e5a9c8537fa54f7a9ed9a826c9ecf5006983b4ff41b8e7",
      "version": 48
    },
    "303.wake": {
      "generated": "2026-10-26T18:53:35.296077+00:00",
      "head": "40ff45dd3079d84c19b3e71beae41b97c9cf5f447162474663547611584d8450",
      "node": "303.wake",
      "snapshot_digest": "a9502980396b272d3a6b143d94a36a217e03f08b3b2ff6fb0d159b9e55ae84d9",
      "version": 56
    }
  },
  "version": 577,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3137.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3138.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d61636266373439613061336634663165.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d64353137326537353763636534626130.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d6f626a6563746976652d646973/636f766572792d73796e.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
