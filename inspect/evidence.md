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
  "generated_at": "2026-10-28T11:02:36.969378+00:00",
  "head": "snapshot:df399535383af99357ee1923ffd9be7596daf934b0a2b4e97e407b0600327df7",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T10:50:11.722412+00:00",
      "head": "9568c17860638f4a01902c1e80b6f5b6d311132abf7e638f370bc0b12ad7535c",
      "node": "100.wake",
      "snapshot_digest": "0b3b586ac28f283a7db7880d1d9a5a547ad0e569645a0e1512ac850dfe7f9c45",
      "version": 13
    },
    "101.wake": {
      "generated": "2026-10-28T10:54:20.393874+00:00",
      "head": "f9ed4bb6f16868f7fe688de69c92bae47aa54ed3452f3ae38f7090aae74445c3",
      "node": "101.wake",
      "snapshot_digest": "8272721de2a5ce644e3daad4e97ddf848448f674e06644f41040b73e62b1feb6",
      "version": 17
    },
    "102.wake": {
      "generated": "2026-10-28T11:01:30.055588+00:00",
      "head": "187fee11a27a5f59a271497731493375670b8b5e2c98cc194cc9c1f203632072",
      "node": "102.wake",
      "snapshot_digest": "4924a2402c65b9b68741c04d7a21e8b83072949087e9f28ec4e0242fbd0f05bd",
      "version": 10
    },
    "103.wake": {
      "generated": "2026-10-28T10:49:19.161323+00:00",
      "head": "b32088324faf30b7566f47bbc14649089aeab2cd2b27485a4fc9dadd36b0822a",
      "node": "103.wake",
      "snapshot_digest": "9f86ab1add6136109ed90a0030db25fb6cca47be731576e4f6c0bdf41cf4b959",
      "version": 24
    },
    "200.wake": {
      "generated": "2026-10-28T10:57:59.705408+00:00",
      "head": "fee4015a5ffdb60d4bc0e2bf57ef4b78b76a2485ec5da9cc0d33c92f60cf45fe",
      "node": "200.wake",
      "snapshot_digest": "ff856abf51e6afb192fc96491202c652599159788d05bbd993a45ae5834e4024",
      "version": 18
    },
    "201.wake": {
      "generated": "2026-10-28T10:52:18.949865+00:00",
      "head": "dcd6eba3ca0419d688223b7c529110051c607772531ca57a83d8c73bc35bc5bd",
      "node": "201.wake",
      "snapshot_digest": "cc5924e9d46670da2431fd577b1eaebfa52f798f4ba8a82377b218cb71dab2f1",
      "version": 16
    },
    "202.wake": {
      "generated": "2026-10-28T11:02:29.771109+00:00",
      "head": "852221aadc736d40c2b8b5e8c1164a018aaf751a20f842f824942fc72c954dc9",
      "node": "202.wake",
      "snapshot_digest": "6250dc8972290fb9a1fd190bc73175ef1205cada641e506ab61be1c00d22f830",
      "version": 19
    },
    "203.wake": {
      "generated": "2026-10-28T11:01:46.859929+00:00",
      "head": "08ceb855c88a9c7f8ce16125d756082f4286b2efbd9fff15133680753485eb50",
      "node": "203.wake",
      "snapshot_digest": "7d12f507054119c6530f5e5b6a64e4ca6c43fde7cd23437986aa285b9df6b182",
      "version": 21
    },
    "300.wake": {
      "generated": "2026-10-28T11:02:36.969378+00:00",
      "head": "e98d49ef56bddb1cffe45bcb59bd9ea216b90adffa31bd4d1b6b8a3d05cdf29c",
      "node": "300.wake",
      "snapshot_digest": "b052b16001bc94e2f4f3ea3e1bf115710c52db1b6f151385989fc1b4a31983a3",
      "version": 19
    },
    "301.wake": {
      "generated": "2026-10-28T11:01:52.232395+00:00",
      "head": "8a4465e5c941a372ea22514048639f342045f4359e2ee83c682a54fa4b69e71c",
      "node": "301.wake",
      "snapshot_digest": "073fe081d91d141ec7b164682d5550a8ce2b3d584a344153d23ebaab4b318da3",
      "version": 13
    },
    "302.wake": {
      "generated": "2026-10-28T10:54:08.222438+00:00",
      "head": "34354bb33812e15375f1cbb0d244eb4b48db5886f01ddbd8d2f5a8ecd82cfa61",
      "node": "302.wake",
      "snapshot_digest": "91ff16676f1c07ee6f7b5e086aa10ebaebcfbf6562a7bd82fe31173d8645905e",
      "version": 13
    },
    "303.wake": {
      "generated": "2026-10-28T10:54:24.441450+00:00",
      "head": "8a9c986fe0ddca9e1b136c32f2b2b10f8db0aa64493ea66e9e6582a4569625c1",
      "node": "303.wake",
      "snapshot_digest": "b0d4cd620f359ccc85e5dc4e5d31c38caeee6a5eb75911586092e050534cbe10",
      "version": 18
    }
  },
  "version": 201,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d35.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330302e77616b653a3a736f757263652d626539316563663066303035346438/37.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d31393539376562333730363434643330.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d756e61737369676e65642d696e/71756972792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
