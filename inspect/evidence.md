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
  "generated_at": "2026-10-29T01:12:09.240145+00:00",
  "head": "snapshot:3055bace86a5cb0a40f4660f8734630788bf646edfda197ddf1e26c2c410d43b",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T01:10:33.746777+00:00",
      "head": "f0d765a6b437420e8d4bb1ef7c0f20358c3a9dd26e01f43c73dd088515783084",
      "node": "100.wake",
      "snapshot_digest": "607b1f8ed37aa3546895369652bf9c1e5b6090181b56c7e714b6e18ca9f66b8d",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-29T01:08:39.311225+00:00",
      "head": "c3a95d29b7045c4f57a2688cf58be37a23953b837bdcf55f41fc348cb4ed1bec",
      "node": "101.wake",
      "snapshot_digest": "b952b999aefead97ebdc95989a006cec64985b21bd24af8bca9b3e83b94cfece",
      "version": 21
    },
    "102.wake": {
      "generated": "2026-10-29T01:09:00.661346+00:00",
      "head": "ba8ce15cc954bae59782fa6c6e5c6e1103b6cbff13206a8a86070e31499b9b9a",
      "node": "102.wake",
      "snapshot_digest": "03cc21748008a65f98e9ab1b366601c7dabf30c0fd1fa8ada515496360ca63d8",
      "version": 17
    },
    "103.wake": {
      "generated": "2026-10-29T01:11:58.687554+00:00",
      "head": "d28671e5ef7a1ed85a41741b1ca9875ebb2b235ed019ea8da60a5ab5fcfbe301",
      "node": "103.wake",
      "snapshot_digest": "be26d04b9068c33b93975917a053e4a93caebc55a85eb09ff5cb697611c9ce0a",
      "version": 28
    },
    "200.wake": {
      "generated": "2026-10-29T01:11:12.774980+00:00",
      "head": "ebe4690aa069124d33ca129d6dc6f49b9b112995e5d1cb16a6fbed0380f26930",
      "node": "200.wake",
      "snapshot_digest": "2215f7fedd0cdfadcea6db0fc1509574182b3fa7d4da2b803e0ee7eb3c5a21af",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-29T01:10:48.103345+00:00",
      "head": "08b88f92e3722235e9e6e23625fbf366f0275a883a5519c3726765321fa16f93",
      "node": "201.wake",
      "snapshot_digest": "8f8c55e48c7b78ec86bd02d56738bb10a3324762875e061b43193acc9b60eff8",
      "version": 22
    },
    "202.wake": {
      "generated": "2026-10-29T01:09:25.795780+00:00",
      "head": "a97761948b273cda339a4564a66c1d2b96acd45364319bf1b0f334aad1e47fa2",
      "node": "202.wake",
      "snapshot_digest": "5a1dca469930321f4d355b300163900e4ca1d8dabeac952e1d38f11089c3c946",
      "version": 30
    },
    "203.wake": {
      "generated": "2026-10-29T01:09:07.541978+00:00",
      "head": "13066862ccb3698c9f19059f6e8be88d82a7c42d754cdb43277b6d2a7a5216e1",
      "node": "203.wake",
      "snapshot_digest": "4358b7cea22c7d6b80ad90a267422cb0950dee6aad5e3236b903c223e0b15958",
      "version": 27
    },
    "300.wake": {
      "generated": "2026-10-29T01:09:03.458598+00:00",
      "head": "4457ebe8ab20ba41f141eba5f073fec091b50fafbd9c38916c86953811e8249e",
      "node": "300.wake",
      "snapshot_digest": "0800527916a1d7ec0e134e1c4eedd317ee3615a6e67d6e4d0fbc792d93208ce6",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T01:12:09.240145+00:00",
      "head": "9fc7089ba3b8309555961de498a63cd200d0fb1351c3339a13c70e66b3390f70",
      "node": "301.wake",
      "snapshot_digest": "cf88156c31b46d2850758b8eac134947f1b3824ca9cee93236d16417281af34d",
      "version": 18
    },
    "302.wake": {
      "generated": "2026-10-29T01:11:22.459886+00:00",
      "head": "d483f3da7747158fcd6c3afcdfc16cb622d7d98b35ccfef47cd5ccaac2d399ee",
      "node": "302.wake",
      "snapshot_digest": "34465ecd3409d41d0a8a494f93e48db723c4ddab530b04bda45985de385892c1",
      "version": 26
    },
    "303.wake": {
      "generated": "2026-10-29T01:08:45.404352+00:00",
      "head": "4f0a2b9debbfc7d5babd707e509b8353ef19a8e6f44d152338ecad8e3de4e5ea",
      "node": "303.wake",
      "snapshot_digest": "4f5a265fbf3e4c418f558f4c983a5e118de9364f7de9031f83878666e8260ca9",
      "version": 23
    }
  },
  "version": 278,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d35623531343564363831633334333032.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d63663739643131386139623734333334.json)
- [notebooks record](../reader-records/notebooks/3330302e77616b653a3a6e622d756e61737369676e65642d696e71756972792d/31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
