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
  "generated_at": "2026-10-29T12:26:58.154431+00:00",
  "head": "snapshot:bcb3fe33264b30b0b72a5187c5199f9a0bde2e9736dd1fae7ee47fc0eb7fda9b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T11:57:49.515090+00:00",
      "head": "4babc40e44540e019211eebaedce4f97fc8534c2be5e3a1cbcdc32744d547ff4",
      "node": "100.wake",
      "snapshot_digest": "ef4a47a23a4fdbc61563007086977c493080b8645e5d3166e5b0f781b3b0e89e",
      "version": 21
    },
    "101.wake": {
      "generated": "2026-10-29T11:57:50.047577+00:00",
      "head": "c3da3ef61547654f256c1ddf5e0dea9672576f186f5bd141da9cfa0969ff39c6",
      "node": "101.wake",
      "snapshot_digest": "2cbc8db64906f7ceb15c19aefc80b5d2ed1ad425faaef13cbc80a62ec9201b18",
      "version": 23
    },
    "102.wake": {
      "generated": "2026-10-29T12:07:27.305786+00:00",
      "head": "b461e551248d58af1bf39eee85c5a07569315d8e425c9388afc0ed280a7ce903",
      "node": "102.wake",
      "snapshot_digest": "1eb07157acc9c38acd7c3282e559397b1f37813e03e69f8d1f602ff9bcb1fd99",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T11:57:49.116942+00:00",
      "head": "b75ef1f371311a8b00be2a28d9573fa502032776dcad719f1aa019833df10c05",
      "node": "103.wake",
      "snapshot_digest": "f4ae317196418b058ed32781c7ae65d9de0dbe12cf2844f83302c8f58bf51bfc",
      "version": 29
    },
    "200.wake": {
      "generated": "2026-10-29T11:57:50.155096+00:00",
      "head": "0d761900a444b63d87fb6c1b79ec9bf9d4eae72828b7bef5a1ba886d533392e2",
      "node": "200.wake",
      "snapshot_digest": "6eb2cfd943b88655f0e231343ead6ee8274e203c712c7235a308d05158771b9a",
      "version": 24
    },
    "201.wake": {
      "generated": "2026-10-29T11:57:58.699556+00:00",
      "head": "bef89954c4e40cf393b1415c7a9bda3e4a19a9eeb8c437f8e479e9b9989092d1",
      "node": "201.wake",
      "snapshot_digest": "2c9e6c632245ff2b6b773087b2a3dcb6120476130b09d4251a069f379b20a96f",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T12:09:03.626108+00:00",
      "head": "3ee36a2b92043f97851f3275bd4927582ca9580c304d596dad42fca4c9f4a7ab",
      "node": "202.wake",
      "snapshot_digest": "f642b11d7e586e1b1cf7f204dd39a615a4c2b540ecf72abb4f0882d32bc4d84e",
      "version": 31
    },
    "203.wake": {
      "generated": "2026-10-29T11:57:47.017636+00:00",
      "head": "9e22fed70b53941feff7a4d0bc37305737fe17256836a4f02bd7208821b8c665",
      "node": "203.wake",
      "snapshot_digest": "fe4039573391b41e7f75d7a9641ae9b0b3744a9350d78cf9837dfbbafb465000",
      "version": 29
    },
    "300.wake": {
      "generated": "2026-10-29T11:58:02.964929+00:00",
      "head": "dfb663c6fde1019dd45e00159f8789a556f62036e21fec1e77799c5128ce58d0",
      "node": "300.wake",
      "snapshot_digest": "e5df8dbad4850f6cbade3518b2c5613747f9fbe8db3698cdd8d60dff35bb6b21",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T12:21:12.134013+00:00",
      "head": "04e41a310cd98f7cfff9de0cf0c69f806d4ce8afd0efa5d58c707355de592859",
      "node": "301.wake",
      "snapshot_digest": "e1af5fd630fab41ce4f249f046c83415ceba27b03c075d863049349d8ce83e70",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T11:57:54.323862+00:00",
      "head": "54ede8eace915382971e023b752ec52074b3ba6501a63d19db7a37dd01e4c3c8",
      "node": "302.wake",
      "snapshot_digest": "d41c86cd560a2596f482297faeafc49168d526042dc873fb53b40fc098ac8689",
      "version": 28
    },
    "303.wake": {
      "generated": "2026-10-29T12:26:58.154431+00:00",
      "head": "9bf53e23d7bee3b09ab45989ee03fbe6b97c4140d9e0ac814ecd7fc2745b4c01",
      "node": "303.wake",
      "snapshot_digest": "815b0372adc609853c134f9fe9156feefab466c2c6a4f35a230cc061c0839f8b",
      "version": 24
    }
  },
  "version": 290,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d623364663835636463633839346330/39.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a736f757263652d633732356564356630636263346166/64.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
