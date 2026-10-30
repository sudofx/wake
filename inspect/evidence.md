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
  "generated_at": "2026-10-30T02:09:49.625637+00:00",
  "head": "snapshot:ffae32b19afb1205b4db92de8edc198a2173f08498fd1de43de6c2f905ee9a33",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-30T02:09:49.625637+00:00",
      "head": "155d5707cec78ed37c652f70f007c17980b1b70817f9bb803dccd0aa8bbba38d",
      "node": "100.wake",
      "snapshot_digest": "14d6ea9c1b99c91ecae3ef7a8ac8f2129d32c4861960c110580d60aad3ce558e",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-30T01:04:07.897585+00:00",
      "head": "7007767bd2998c7758f2092b1e4a945d2d711956686503d8b6d77b09430856f9",
      "node": "101.wake",
      "snapshot_digest": "70a6c301b9a464afaffcbabbfb14356855582e1a37d2541c6d3a051c606c0502",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-30T01:04:11.253291+00:00",
      "head": "dddd465ce8308c5225767359b04280b37818102b069781ee9df505bfb334e856",
      "node": "102.wake",
      "snapshot_digest": "b5be6744fd281c3071fab39cc245c387d7175dd8d992beade0dfc0ee63cd2e66",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-30T01:04:22.871039+00:00",
      "head": "e447a99840f801ddec924fbaf63c75c02a6886d0978d39cfb3305ff21b09efae",
      "node": "103.wake",
      "snapshot_digest": "006dc0275ac9fd32d0be46bbbd0714a0c42b3949b42e061d1888e4eeb72cc815",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-30T01:04:34.156827+00:00",
      "head": "d86ad7757969e1cd314e8c0fb09ed16c63016603f0a46b220485be36d2e031b7",
      "node": "200.wake",
      "snapshot_digest": "e1ff11078c363ec961b2db3235ac0718946dc6d24f2fa954284195c0de69d581",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-30T02:04:47.181114+00:00",
      "head": "0e96f80bafdebce8c311ad55ba11d9efbe15ba5b3cfc6e179cb65d2e4c1a1fd7",
      "node": "201.wake",
      "snapshot_digest": "87a6ae054ec4974276c7438d6d041ea5d1613635654b6d1345262b14a727b448",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-30T01:04:10.260181+00:00",
      "head": "5116983ee8a59382f1adcdbffce368e0d2a3aa0381c482259d66ed7e0589369f",
      "node": "202.wake",
      "snapshot_digest": "b3c54f4275fa70d058a6bdbb3936d95061fd9f56e97844db27c80aa1397ef800",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-30T01:04:10.627449+00:00",
      "head": "fcfaeae646eeb6b1d7474a001fda5becc3d8995191dbe8268ad59ac21ecfa9ee",
      "node": "203.wake",
      "snapshot_digest": "4308468fbb14c11469e7aa4a92d27cdda3d4d0472265504497704a84339b4648",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-30T01:04:21.554940+00:00",
      "head": "fb4c2fc2eb4a00efc2dc8b6ca3a369f3280cd27c9234d15a76ba7c70a4c064c5",
      "node": "300.wake",
      "snapshot_digest": "d27ce5cccf0a36ecd6328ab281e9ee0843d2af591c50add0d879fe9dbff70325",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-30T02:08:10.944048+00:00",
      "head": "b2df6379e1e5995c16b77298f452ad50d4790e92d03f16ba4a385e7b8d0e68c9",
      "node": "301.wake",
      "snapshot_digest": "20d568cb8e5e6cff966a2b3d1c28500dae659b126bb994f55ae36a3f240b3456",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-30T02:06:29.697736+00:00",
      "head": "c716a2a4e26efc867ec229cf5547f0d74f85b848b3e8982b541c0152ceb24520",
      "node": "302.wake",
      "snapshot_digest": "e9e867f68d43c0217aeafa190ef5be27a89e00b037a71874aafd354859e5f223",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-30T01:04:12.760814+00:00",
      "head": "42ddf98b3454b864a9ba0595b97f3bbe856b330a39c7d3e289d33c42d910871a",
      "node": "303.wake",
      "snapshot_digest": "47bf04159cec1ff8d154ed49b689f4e8cecc999b92d837f575b1c5f9b88038ec",
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
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d32356131613164303930646334646333.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d30353438663361383463373334373632.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
