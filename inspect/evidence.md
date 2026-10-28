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
  "generated_at": "2026-10-28T14:12:39.911930+00:00",
  "head": "snapshot:ae03576aae982d77a7f78e7c164208b981f1fe48058e45b4314e93dc9ba0f1f2",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-28T14:10:10.521336+00:00",
      "head": "ca08f69cca54a541e8547b2cbe288b43d9ec0e9bc3927b3aab68cd64a19cbf09",
      "node": "100.wake",
      "snapshot_digest": "1bf6def6a8f0e759f4e59e6f5880b1bfd08d7368c7f8915af89d965c6f2156d8",
      "version": 19
    },
    "101.wake": {
      "generated": "2026-10-28T14:09:46.671549+00:00",
      "head": "cd9a64478d68e48f75c520a41b4eb92188f262a26f48c0795e5c53899c8b2748",
      "node": "101.wake",
      "snapshot_digest": "a8d43d988c94b0a57469082ed25a692163d7859dd5f2218283610c80b6498452",
      "version": 19
    },
    "102.wake": {
      "generated": "2026-10-28T14:12:20.511036+00:00",
      "head": "b8567dd81f236037e86bfdff46c487571cfc033711a6dcec515908ef7c753f48",
      "node": "102.wake",
      "snapshot_digest": "4b8b32efb8a109f45727f97a919c4853adce157a1b29d77e06fbac2230075941",
      "version": 15
    },
    "103.wake": {
      "generated": "2026-10-28T14:12:36.551126+00:00",
      "head": "bfe02418c18bc36e525883643939ee08b4a544cda5e8463aa72823bb17d98d81",
      "node": "103.wake",
      "snapshot_digest": "57c402583c38f3c86552d362980ad1d807e567afa39dfc24ba219c4d2bb8757e",
      "version": 26
    },
    "200.wake": {
      "generated": "2026-10-28T14:12:39.911930+00:00",
      "head": "08786d0907d973f29201e7e242b3a0a21ddf2cf6bed77dfcd62cdd623e672e75",
      "node": "200.wake",
      "snapshot_digest": "2ddcf5b3e0766e3c48df3ebe5adb405e27e2a411fb47115b2dfce1a113c85f29",
      "version": 23
    },
    "201.wake": {
      "generated": "2026-10-28T14:08:43.994978+00:00",
      "head": "53f11a9f936695043d9fdd51b1159b99c4ccf426a56ab56bffb256b806f33489",
      "node": "201.wake",
      "snapshot_digest": "950932c2baebd4f37bce174d58b45ad3950379f4c0e2201116f90d4e1acc2bd6",
      "version": 20
    },
    "202.wake": {
      "generated": "2026-10-28T14:10:45.696110+00:00",
      "head": "6328a1b98a2d9f52b2b124e05005735b265c1e1ddeb59899e6dbf20b3e0ae65b",
      "node": "202.wake",
      "snapshot_digest": "8cd351a8948750bb4af9cddbefc0d1283176a5c47a602af00272d90d528e444a",
      "version": 26
    },
    "203.wake": {
      "generated": "2026-10-28T14:08:33.573896+00:00",
      "head": "93a38b7892afd46de9f22e990f6ed635a8376ae145b1074d930a47da38016f3e",
      "node": "203.wake",
      "snapshot_digest": "52c69bb54764217b28e4a07f0eecdaeaa1c409ac2a8f82c74ff0cf2a9867c3d2",
      "version": 23
    },
    "300.wake": {
      "generated": "2026-10-28T14:09:40.721707+00:00",
      "head": "bba62c6743eb5fddd6f488561b1ec598e649f4c6680c4dae3ffc0d8ef309a1e3",
      "node": "300.wake",
      "snapshot_digest": "baa2a63667dc5efe9312e903b707d0416eba19b6d5c5d8e5c7c139c96c532283",
      "version": 22
    },
    "301.wake": {
      "generated": "2026-10-28T14:12:04.544402+00:00",
      "head": "7a15197fdd7b5cd6964ca2305a6a117e9af50b34e53013359a4d5eef89e27682",
      "node": "301.wake",
      "snapshot_digest": "54c8de888ffca257dfbaffbeb88df9dcae7f9a0728c5298218c927b1fc64e4cb",
      "version": 15
    },
    "302.wake": {
      "generated": "2026-10-28T14:11:52.371349+00:00",
      "head": "c75c4192a1ff96f11e64101dd7641d2e7f6325ecb9ee4261c5e1710ef3a64747",
      "node": "302.wake",
      "snapshot_digest": "903572476f344315d520f9643db57a1ede8db09cad0b584a40dcd68e0d766195",
      "version": 21
    },
    "303.wake": {
      "generated": "2026-10-28T14:08:36.676376+00:00",
      "head": "0bc696d5b8c6992f9dd148828bb5b44f98a15dda1f4c6c91a2aee1204e4ca3a7",
      "node": "303.wake",
      "snapshot_digest": "5169cdfc2ad1c6b983e9ccf9684771f05902f1721092b247678673b44e498ea9",
      "version": 22
    }
  },
  "version": 251,
  "version_meaning": "Sum of accepted node cycles; not one authoritative record version."
}
```

Selected exact public records (bounded examples, not an exhaustive evidence review):

- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d626f622d37.json)
- [posts record](../reader-records/posts/3130302e77616b653a3a67726f75702d77616b652d696e74726f64756374696f/6e.json)
- [evidence record](../reader-records/evidence/3330312e77616b653a3a722d37343965343663613661323334626434.json)
- [evidence record](../reader-records/evidence/3330322e77616b653a3a722d32346366643031306235656434626664.json)
- [notebooks record](../reader-records/notebooks/3330332e77616b653a3a6e6f7465626f6f6b2d77616b652d73656c662d737475/64792d303031.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
