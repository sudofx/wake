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
  "generated_at": "2026-10-29T19:15:52.993859+00:00",
  "head": "snapshot:93d01917eabe9c39d28aa1c2978ed47bf4ee7c2db3423151e19b628b2f0cc418",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-29T19:12:09.400173+00:00",
      "head": "15aa7b751bed2eba456f6ea4f37d19d0e2e1f63dc460738c3933f0fd8055bbbc",
      "node": "100.wake",
      "snapshot_digest": "5da57a2d59a3e3e8e15be1780f98c3aa67d51ac9dddbd1dcde58a8fea8416e02",
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
      "generated": "2026-10-29T19:11:06.343067+00:00",
      "head": "8d19eef31d484854d581401ffb23b9fc1f9cb9144f564e17398d0fdf4e921d5b",
      "node": "103.wake",
      "snapshot_digest": "12acdcae3a593bd7fdf429df052b047b107d87c42bbc9c8aaaae57cdaff1fad7",
      "version": 34
    },
    "200.wake": {
      "generated": "2026-10-29T19:07:13.398727+00:00",
      "head": "55ef0efe543e44ae3143d58244f2de633541766371621f9d37912eb0f0220314",
      "node": "200.wake",
      "snapshot_digest": "43eb6c7da79f29884cf885de32faaaa6113762efcfbad37a166a176492612862",
      "version": 25
    },
    "201.wake": {
      "generated": "2026-10-29T19:07:20.749494+00:00",
      "head": "1c059505da87fc8fdbb2ade503fb9e74691bfe25baf7a992a56a20317388cdd4",
      "node": "201.wake",
      "snapshot_digest": "b32aad59b25a6423cedf05660917b8ebe91b082a91cb7d9edc787e15b440ed04",
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
      "generated": "2026-10-29T19:08:57.978462+00:00",
      "head": "eb222165fef53a604685d2f80f8470d10e5a2eb4228a968ce426e27b6d302e06",
      "node": "203.wake",
      "snapshot_digest": "8b154575b5237c088dde772bb8982ffd647d7a9124e890f974361dbc96e7c8bd",
      "version": 32
    },
    "300.wake": {
      "generated": "2026-10-29T19:07:20.226739+00:00",
      "head": "09e678f32c9542d95fcad7e0f255083300f4a629bd62d7fa0d1f8b5bba6f7b7d",
      "node": "300.wake",
      "snapshot_digest": "dc14b44f72442e51f213ca7bff984e5e6a2eeabe80f101a7c97e98629e565eca",
      "version": 24
    },
    "301.wake": {
      "generated": "2026-10-29T19:12:09.688881+00:00",
      "head": "3528a49729af210ebd0b766a3a8251e52b4c035f90a205c29d2bdbe5d405aeaf",
      "node": "301.wake",
      "snapshot_digest": "a4200b332c881ce439140343cdb4ea344eaeec03616f28eeb54dae6ebd5d3fbf",
      "version": 19
    },
    "302.wake": {
      "generated": "2026-10-29T19:07:22.343271+00:00",
      "head": "0a13d670b1afdd8277548eae586b7be0e102c186718e4dcfc1624cffca2ef55e",
      "node": "302.wake",
      "snapshot_digest": "6064251bc311f6253d9c81731faf12d7b29e6d1a255a14c19f0bebfd1bff2ac7",
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
  "version": 316,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d38.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d39.json)
- [evidence record](../reader-records/evidence/3130322e77616b653a3a722d39313638646663386565303734373663.json)
- [evidence record](../reader-records/evidence/3230332e77616b653a3a722d33306366356364613337636234613361.json)
- [notebooks record](../reader-records/notebooks/3130332e77616b653a3a6e6f7465626f6f6b2d646973636f766572792d30312d/7631.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
