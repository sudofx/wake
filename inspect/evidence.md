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
  "generated_at": "2026-11-03T21:21:32.694170+00:00",
  "head": "snapshot:9fa90e71ea83e4674611193f61d2f3aae14439b04914fb4e0534886ace923315",
  "node_heads": {
    "100.wake": {
      "generated": "2026-11-03T21:02:25.509177+00:00",
      "head": "d92ecf41455bf75b9c9319cdc7cdb35c48790947fba881cd82bd279a23ae5284",
      "node": "100.wake",
      "snapshot_digest": "010f3e69ba03300f936884a9620baf3d88ef546f70325996dc61bdcf39844133",
      "version": 0
    },
    "101.wake": {
      "generated": "2026-11-03T20:57:06.896599+00:00",
      "head": "0e9e301f69d1874b6fbdb117aa0084c7eeec736c679f47c1931e70c4adae5c05",
      "node": "101.wake",
      "snapshot_digest": "262516b984a2a3b01eb0373f2c3d056b602dd917bc10dce1d8df7e080775904a",
      "version": 0
    },
    "102.wake": {
      "generated": "2026-11-03T20:57:06.846541+00:00",
      "head": "9c2c0239b0257ed2ac67b91e7e295c9a9b7a9120da590dadea9d62218de8b42c",
      "node": "102.wake",
      "snapshot_digest": "1a848632eba912acfa61445483885bca802db56ec1224947173b9799499d4a27",
      "version": 0
    },
    "103.wake": {
      "generated": "2026-11-03T20:57:06.828220+00:00",
      "head": "54634c97203beaead650eebc0efd44ad1a1956623e8be3c7909a9ee88da26240",
      "node": "103.wake",
      "snapshot_digest": "304d3428993e5e6c6d5aa13e2a74015c6e3b9d30d1ea96ab7933c3e96ef43f38",
      "version": 0
    },
    "200.wake": {
      "generated": "2026-11-03T20:57:06.809808+00:00",
      "head": "0267b9521de88008133ccdc30852aceebab41995d4a05c66771fc32ca7c78cd3",
      "node": "200.wake",
      "snapshot_digest": "2755d43e83299ba388c640542a4db9ccc18a3d42e4031f91bd68450a6510bd16",
      "version": 0
    },
    "201.wake": {
      "generated": "2026-11-03T20:57:06.885906+00:00",
      "head": "f1b09b05198f1347b144986673a19962c387681637ea2145692faa1f45b75f8c",
      "node": "201.wake",
      "snapshot_digest": "4347345f05f8510690f517d18a63fe5c195e53a0e5601fde1f8561f3e4a66815",
      "version": 0
    },
    "202.wake": {
      "generated": "2026-11-03T21:21:32.694170+00:00",
      "head": "355e6f519fa44c072b72c0b363eb6ab9cdec1d84e868612dffc4136739ee4dca",
      "node": "202.wake",
      "snapshot_digest": "78d2343a28b5843f6fd9e4f6a2decb8540265479c87fa310db60c7b36dbf5b7a",
      "version": 1
    },
    "203.wake": {
      "generated": "2026-11-03T20:57:06.800173+00:00",
      "head": "22714f0a92f271296351760e713694a9003f68772b9682be839e1b9680347435",
      "node": "203.wake",
      "snapshot_digest": "caf60ca9f33f029598ee47467c3e5631bc99c13b56fe62373f24f1f7e9afcc8c",
      "version": 0
    },
    "300.wake": {
      "generated": "2026-11-03T20:57:06.824485+00:00",
      "head": "3e244c1a14450479c7968a6a651468112ff10da31f9fe538a7f2fdea63158286",
      "node": "300.wake",
      "snapshot_digest": "9458cfe8e090dd47ccfd065f48f2df5ed168578fb0bcc7b827b5d73b86b62e1b",
      "version": 0
    },
    "301.wake": {
      "generated": "2026-11-03T20:57:06.929830+00:00",
      "head": "6aaf74b52e9a524ebb030e727ed6d26af9bf2605db822904decf1a418f032dfe",
      "node": "301.wake",
      "snapshot_digest": "a6f1f08adc437480fee3ee7d484023fe66045b023bfaca6bd89af939ade23db0",
      "version": 0
    },
    "302.wake": {
      "generated": "2026-11-03T20:57:06.691888+00:00",
      "head": "56b0ee6620d26e7628129b7e6e611e70a93d8c9bdd8666ab27af01e268f7c753",
      "node": "302.wake",
      "snapshot_digest": "581826e783b20899048280917accf4f0f141a1d1c06fba5c01ce5829170fa894",
      "version": 0
    },
    "303.wake": {
      "generated": "2026-11-03T20:57:06.712018+00:00",
      "head": "fc7b571fb29e39b387ea165f5ce8e6af28165eed8c8969700dfd5c78433adbb1",
      "node": "303.wake",
      "snapshot_digest": "00be6afedf843268ccd2cd72b3a393f6ecc831a5aa43d1f0935a38a9939b4dfe",
      "version": 0
    }
  },
  "version": 1,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d393532656664643937626638346133/64.json)
- [evidence record](../reader-records/evidence/3230322e77616b653a3a736f757263652d633665623636376130653433346335/65.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
