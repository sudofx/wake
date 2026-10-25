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
  "generated_at": "2026-10-25T18:07:00.948891+00:00",
  "head": "snapshot:b29c4f6ec82ca3364a7babf573e0dc99b0d68db9f3f1d4a2eade4f6149286dc2",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T18:07:00.948891+00:00",
      "head": "26d323ba719ebb28dca2772742e4b1321d5d3bd01b5b225846a88a3d08020bcc",
      "node": "100.wake",
      "snapshot_digest": "732815aa4f395621c833caaf17e440540417473574a0a7d48076537325b74856",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T17:51:02.075340+00:00",
      "head": "0bf5d65f3217bf7f70d6d49afd3c1cd2b5e30b8473abac8b86b9d73155765339",
      "node": "101.wake",
      "snapshot_digest": "ce76c73c50c41dbba9e02310796ede1cba15e5001114ba923807195d7f5822f2",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T17:57:13.511063+00:00",
      "head": "df424d6e141c672344a65ddd3181e5087c0b537f04d96c7395fdbf3a769fa2ec",
      "node": "102.wake",
      "snapshot_digest": "c6a5625eea133b499a619b6da793bbf293e92e070d08f7a7174392ed0befddf1",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T18:01:31.408983+00:00",
      "head": "115f5a064b7f867dfc3d9a527401e0ef7777af77e7e9101d96f80d1bac9ea9e2",
      "node": "103.wake",
      "snapshot_digest": "9940b4d4845c8f303f302099c171380b56ecf8670c5d07d1b90b7a6690e1ff8c",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T17:50:46.134815+00:00",
      "head": "9964355fbc6b544fbaeb65543d7dbe354ffa67313bc5ae586f6942668aeda1e7",
      "node": "200.wake",
      "snapshot_digest": "f6711af2ee7f52b9e3d32a5f22ae1e439479370fdaeed706df6edc1d8728dcfe",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T18:05:55.269800+00:00",
      "head": "f707fb264d26d77831096df0bd987ab83288e8cd83985d931ba4d79b35eea8af",
      "node": "201.wake",
      "snapshot_digest": "85f8f803ddc9f481e76a6cd7297141a570640af569be6b2d499a3eab2d481f04",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T18:04:42.713912+00:00",
      "head": "2224695dcc4bfb2c41ebc32b71ec0c7e5da5dcdf1207884aba88fd2e365f1441",
      "node": "202.wake",
      "snapshot_digest": "88ca58a09b6f65ccd9444de66134b9845088e60a50e7cd120242d2bfd25c8655",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T18:04:11.303944+00:00",
      "head": "3b33c08253941021c19eac13cbe9ec920e3e29810a2defb76cd22b1cad57e640",
      "node": "203.wake",
      "snapshot_digest": "8dc8ad0f4b56d552797b22adbc82e3c294563e99f46cf943271e9a91136923a6",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T18:02:04.262041+00:00",
      "head": "7fb640532edaa67f9a0d4998e6d9d0d57595374911433eb23f55eb47f4a593a7",
      "node": "300.wake",
      "snapshot_digest": "96cd3cd8bac6092af781dbf888eaa57e05949b315b0e67620b23346b540d4411",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T17:59:27.802639+00:00",
      "head": "4fedb24333ca2a3595591543f650b91715e5f4ade92f70ecdc01401260100a00",
      "node": "301.wake",
      "snapshot_digest": "04cfd017a4864833b227c094dec5a93cda4b24d52d7872df126b05073e68c1a5",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T17:58:47.134220+00:00",
      "head": "6bd4c1fd8b66c368b2b1734de552341f473e46ead9459e821792bfd6b2b135b7",
      "node": "302.wake",
      "snapshot_digest": "6f2e1f697b131b05ed5fb95f5a3ba17a1298258dd7d951867bd501e22ceb9716",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T18:06:49.887017+00:00",
      "head": "6eec1fe99358527c062fc0ffb54fac764d3f8868d6d57117e809102d03673c0e",
      "node": "303.wake",
      "snapshot_digest": "c2ed07001b274debdd6ac7b10c0c68613d573cd99273e1daf6304322f2667b21",
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
- [evidence record](../reader-records/evidence/3230322e77616b653a3a722d64346238623864646630643734613331.json)
- [evidence record](../reader-records/evidence/3330332e77616b653a3a722d31396230613564366361343534626563.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
