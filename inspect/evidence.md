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
  "generated_at": "2026-10-31T14:42:49.902831+00:00",
  "head": "snapshot:709ffb46ca298a907ef70f254b88d879f69926c42562a9f08be6af49c206cfc4",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-31T14:35:40.212408+00:00",
      "head": "ae2b1eb216d5fa3ddbabf41b5ea03b80f26d326ee1010e7a41714a49d2120ec7",
      "node": "100.wake",
      "snapshot_digest": "c3e997a80223a520266217b16a913b8185783d8ea8e4a13e89e36c2662b1e5bb",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-31T14:13:02.348956+00:00",
      "head": "14b3cc74a859cc89878a8d9f8d2ff17aa95b950c1b6c26f3c91aa1ef5df02c4c",
      "node": "101.wake",
      "snapshot_digest": "4b1e643c6b5aa7e55fecc0119a5473bc0b779b376142718b27417dc17b8fd200",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-31T14:12:58.179695+00:00",
      "head": "eafb89f2de7368506a22f94dc96f6d6052d1a4a8d0e6e64e0a15faa922621c02",
      "node": "102.wake",
      "snapshot_digest": "f6eb1e7721ef2ef8e6f123ab4fad5d65f96e53eab94a54d9b8de358f4d71e23e",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-31T14:13:18.264030+00:00",
      "head": "6b0b9ea69ba240d919914304a22f9ed3f78088ea15ad83a7a4aab72a7ed45f8f",
      "node": "103.wake",
      "snapshot_digest": "04776aad782f8ebd719ca41eafcef03c77525a66d931ead156f2ca94c847ff59",
      "version": 37
    },
    "200.wake": {
      "generated": "2026-10-31T14:13:23.212448+00:00",
      "head": "b8d14e19edb9a247714a8e7367571cc5d268c48c5acc137a9984491e4633c056",
      "node": "200.wake",
      "snapshot_digest": "7a18490bfb4cd9c1fe0bdeb11b71ed71e5eab12d00b3d47b8cdb47b9f42d4f28",
      "version": 39
    },
    "201.wake": {
      "generated": "2026-10-31T14:39:15.065733+00:00",
      "head": "26e0eeea2e4dc7da5c21ef89f7c3fb6a8b815f21807cc8a57bfad360e6e515e6",
      "node": "201.wake",
      "snapshot_digest": "d5362e32fbcc2debff765e1d7e615c9d8a6b602ec26ce3a86189ff4eae5f1b03",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-31T14:12:57.060164+00:00",
      "head": "171269ddff1b438e553dfe76090be06ffc1db15e06ed419ce1035dbadf278c6f",
      "node": "202.wake",
      "snapshot_digest": "b4a7450772d7b97c49e622425fbf402581396b5a84e36852948a7a10a993106e",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-31T14:13:00.692308+00:00",
      "head": "daa2ca6bf2cebf453488a92dd79c707ad475e3d31e184c6d3a50a9edfb46a7e3",
      "node": "203.wake",
      "snapshot_digest": "5011e4277915a4c5c7e431f2fc79b62d4f5694279944e729521cf1ed413f1284",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-31T14:13:13.068832+00:00",
      "head": "01694650feee1554b890efffd6a4c8bc1b3f2898af1be698719d6402cb80f589",
      "node": "300.wake",
      "snapshot_digest": "1ab7fc6c7873363902d85adf886b2811e12d427b7d51654d71b1664580fa448b",
      "version": 25
    },
    "301.wake": {
      "generated": "2026-10-31T14:41:07.793818+00:00",
      "head": "d57631914bc8320f67c5e66ebb07ba77a2999b2d0137759a6d635ae77f1a9e8f",
      "node": "301.wake",
      "snapshot_digest": "3f168337a4e6e5d303deb6d4cc525976e0440e40b825dc20f8b63f5fc3200ca8",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-31T14:42:49.902831+00:00",
      "head": "b50f9516327e693a6df72a52667a2df0890631585b9fd2da128573842a84b047",
      "node": "302.wake",
      "snapshot_digest": "f6a494998461af3f8e5737a9202be99bf56280e83b43c4971010769e7a2e860a",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-31T14:13:01.557997+00:00",
      "head": "3bc13c7412854642cb4c0a172c3dcf025806b698eff6b6a0de00d970d1210946",
      "node": "303.wake",
      "snapshot_digest": "b45daf592c23847856d7de65e35b5d24b6a21fa1219cd7541cc686e9f5493996",
      "version": 24
    }
  },
  "version": 336,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d3132.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d35356261363230666562666434613531.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d31346537663862333237303234393264.json)
- [notebooks record](../reader-records/notebooks/3230302e77616b653a3a6e622d77616b652d6172636869746563747572652d30/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
