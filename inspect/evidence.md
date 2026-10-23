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
  "generated_at": "2026-10-23T18:12:34.111088+00:00",
  "head": "snapshot:d7765029750e6ac8032bd950c89bf25bd56bae9064be7db54cb23ce65b43c786",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-23T18:06:49.121278+00:00",
      "head": "47cfb446ff53503de5ff3e792151c18a63a045d2bbfa08a04913c4a850166e46",
      "node": "100.wake",
      "snapshot_digest": "ab842889b222570fda75349278617ac002ef8fa795465c277636a4c3a1305b8e",
      "version": 16
    },
    "101.wake": {
      "generated": "2026-10-23T18:08:40.974445+00:00",
      "head": "edd42868de66e17ba23e84b1355dc17b67ccc7339838c8b2a94767660503f683",
      "node": "101.wake",
      "snapshot_digest": "5c5c928b8dfbd44b4353fe31527bf5bd87259fc471679bf124f2a9b8c7227086",
      "version": 29
    },
    "102.wake": {
      "generated": "2026-10-23T18:06:21.642441+00:00",
      "head": "59874f33c9f33738063fff089d70475d84c982ffed6361f3b49de74950220e18",
      "node": "102.wake",
      "snapshot_digest": "2640ee958736912953b05d28fed9266f223419ce8dadb2fd5c86972768351ad0",
      "version": 34
    },
    "103.wake": {
      "generated": "2026-10-23T18:08:05.869582+00:00",
      "head": "10e44b72a5cd26923e6c0a5a14d8cee37cb7d3931deeb0efa20ccf93d48c216c",
      "node": "103.wake",
      "snapshot_digest": "07ea046faee22c6a8e323f015e88300f782f7c9854b12b1faa8f07d8bc15e368",
      "version": 25
    },
    "200.wake": {
      "generated": "2026-10-23T18:11:08.544064+00:00",
      "head": "6bdee4c20f4778c2b2e6502b931641c2b985edb44b3a07b67d2240219afb250b",
      "node": "200.wake",
      "snapshot_digest": "6d76bb00f216699a1356f9037946968dc5e76a45f4393bcb91862592f60f5d0a",
      "version": 21
    },
    "201.wake": {
      "generated": "2026-10-23T18:07:13.802124+00:00",
      "head": "b9bcda0cf9affbfc600979ffb2ea0399537ee1e78920d1daf1cbc007a055fa74",
      "node": "201.wake",
      "snapshot_digest": "efce2386a3d81d9a12b10d9148025b512a7d09934677ac1afc613774c5ce2861",
      "version": 23
    },
    "202.wake": {
      "generated": "2026-10-23T18:00:52.216042+00:00",
      "head": "b9ef0a1da6f69dd38aac5e071679c5d34153e4f78f2910d912b2a7500e490435",
      "node": "202.wake",
      "snapshot_digest": "0d43575175b2ec55d66c92913eaa241882adbbe3f4ac8946801f05f33363c7e0",
      "version": 37
    },
    "203.wake": {
      "generated": "2026-10-23T18:03:39.168269+00:00",
      "head": "d29f1b116ffb9f99bb84cf1d25c95f4e818597d42b3571408a700826dd78ceff",
      "node": "203.wake",
      "snapshot_digest": "307a67981599a002f4281209b689d6a0fb8958c4b36e8797544e6964361667b2",
      "version": 17
    },
    "300.wake": {
      "generated": "2026-10-23T18:09:42.948183+00:00",
      "head": "7cb4b3f62fdc1aaace89a0fd569a6855abc2338a6f0985c8caf5721b99a6e6be",
      "node": "300.wake",
      "snapshot_digest": "bc5090a3f859733a607f16b5ff71db2d579f69b837f5a395965f0f71feee5b4f",
      "version": 23
    },
    "301.wake": {
      "generated": "2026-10-23T18:12:34.111088+00:00",
      "head": "bbc7bfec7c043465c70632ee3fd4d925dede4622436ddf80c4a75efda4ebf0be",
      "node": "301.wake",
      "snapshot_digest": "f09642de8412e54dcb339ec58b7df3711d98ac4d1982c763dfbfc50ad39fb548",
      "version": 35
    },
    "302.wake": {
      "generated": "2026-10-23T17:19:59.819939+00:00",
      "head": "2533b96f3c703259daf18f1d7f4da94935cca76ccb693a9cc07c5a238bbef5ff",
      "node": "302.wake",
      "snapshot_digest": "095f823a83daa55c8dbc200d7e4ba66c3705e62b228115b0e926db59705cce40",
      "version": 16
    },
    "303.wake": {
      "generated": "2026-10-23T18:05:23.817616+00:00",
      "head": "a4ef6b3eac9fc14a6f6f41d92b2df8ae5b8d20058eb2a49518ba65743271847a",
      "node": "303.wake",
      "snapshot_digest": "09bfd427e316a40205a7fe2254e0c2a62efe4edcdf57bbb45554d16a4d4b8441",
      "version": 32
    }
  },
  "version": 308,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d343966613739383738623562343939/38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a736f757263652d653566306366666265373334346438/61.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d656d6572672d7072/65662d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
