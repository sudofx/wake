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
  "generated_at": "2026-10-29T19:57:00.604100+00:00",
  "head": "snapshot:293f9982cc66eeca2a10bd78fe1bf2e1b5ed300865d50e710cc2a297d31c9a12",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T19:51:51.711719+00:00",
      "head": "ea13efa081b06a207065c67cdae730ab9716dc3cff418c768cc383ce8e9c93dc",
      "node": "100.wake",
      "snapshot_digest": "1957651caff53f077088871b2efea402354ebb339bbfa6e496e6c8eaf3c02eec",
      "version": 23
    },
    "101.wake": {
      "generated": "2026-10-29T19:14:32.501960+00:00",
      "head": "e1136b8f0e80b14730f69e352075d5a3175af2a2b422af7fbcb8e733721ad7be",
      "node": "101.wake",
      "snapshot_digest": "48c9f85092ec79f29713d4943d33e1a8ed0de50e7f51f66dd853eff03e8d0780",
      "version": 27
    },
    "102.wake": {
      "generated": "2026-10-29T19:15:52.993859+00:00",
      "head": "d0af59fc2c96d1fbbb0185032616166bfc6a59edf950526c3c6a8fe08291eb2e",
      "node": "102.wake",
      "snapshot_digest": "cbc86882eb9239f6c228f203634ba0be26ed2e42e765306dcfcf276491a9028f",
      "version": 21
    },
    "103.wake": {
      "generated": "2026-10-29T19:57:00.604100+00:00",
      "head": "d9094d64fb009337db443ba2200fc41b82c1ab9a896ee32cb311d9945130661e",
      "node": "103.wake",
      "snapshot_digest": "9d626512e67332bc0696df61e1b0b2e6a5275be171ec15a49fcb9ce024634f74",
      "version": 36
    },
    "200.wake": {
      "generated": "2026-10-29T19:53:35.532622+00:00",
      "head": "97df12cbaba63b037bc42a385a025d610c1027266da84482b8b0df872d15615e",
      "node": "200.wake",
      "snapshot_digest": "7ae1412e2ee3ebb0d4ecb0f7f18774318782fe45e069f2b0696011fcbaa1cc17",
      "version": 26
    },
    "201.wake": {
      "generated": "2026-10-29T19:50:20.741105+00:00",
      "head": "5ee33f5a1f54aab2ca47d061746a0aef8d6484e9d9d0a41b43de38df883df4e3",
      "node": "201.wake",
      "snapshot_digest": "78981772703fd09a02b2fa44ef8ef916cc87e45fbf86a12bf73813857f9045b9",
      "version": 26
    },
    "202.wake": {
      "generated": "2026-10-29T18:12:18.436124+00:00",
      "head": "82f28d0317597c3289352c49921c76918f1a548f829ecb5d69ba14b602ed6f2d",
      "node": "202.wake",
      "snapshot_digest": "4f750545b6192158c16295b76e254145299e55052cce61d6dd1b4a80bd25b7d7",
      "version": 32
    },
    "203.wake": {
      "generated": "2026-10-29T19:38:12.376728+00:00",
      "head": "75ecf106896a3b90fb644308ee8a90be4872b04058722cbaa38cd8e01daf23e0",
      "node": "203.wake",
      "snapshot_digest": "8017f88d9901a06f44651c295f50681c2325b996cd7a803fde43a7848e315af8",
      "version": 34
    },
    "300.wake": {
      "generated": "2026-10-29T19:45:09.167847+00:00",
      "head": "071ab1e50aeeae47162389067da712721c829266724b70441f6392dd2d01be0f",
      "node": "300.wake",
      "snapshot_digest": "a8dbd6f8d45f70c2a1a10e6485d6284608d39156e5ae80d5e2a46eb28e2834ae",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T19:55:00.462231+00:00",
      "head": "050479e87b53520bc51d9abb0eb132032ab46eede0f9cfab57de485dc7806fe9",
      "node": "301.wake",
      "snapshot_digest": "72437c4ed29dc5e8659fe441d33dd599a81602a79968b8854e36021b8b45c395",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-29T19:48:12.509871+00:00",
      "head": "f684e3973c884af47003e429c7bc131d150fba57d623bc306761c94e89f8104f",
      "node": "302.wake",
      "snapshot_digest": "828edf9692bc7ce35f5ee3696ed4eedb765107e02d7203da8ebe07ee28968a13",
      "version": 29
    },
    "303.wake": {
      "generated": "2026-10-29T18:12:25.014528+00:00",
      "head": "46c25e2e79c38bed20f1917b2c13e3c49e3e9d72bbad2c4255079ac023799e85",
      "node": "303.wake",
      "snapshot_digest": "1707d85faf96d2ce0c830347e26f1c0ac0c31419451eb55c472fb9ebfe78a705",
      "version": 24
    }
  },
  "version": 321,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3230302e77616b653a3a722d34613364663930366533343534626365.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d66396331653365636466313634616138.json)
- [notebooks record](../reader-records/notebooks/3230332e77616b653a3a6e622d6d656d6f72792d6964656e746974792d30322d/3031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
