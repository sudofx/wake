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
  "generated_at": "2026-10-25T20:24:22.081790+00:00",
  "head": "snapshot:e7e40680820ae1f12d6a46df4985ed89daf2169d6755f9419968f58e116ef5b6",
  "node_heads": {
    "100.wake": {
      "generated": "2026-10-25T20:13:59.216689+00:00",
      "head": "ee29fad085bf1dedc83861e4083e587682d82193a35aa5876a5769b5fe6e719a",
      "node": "100.wake",
      "snapshot_digest": "7e4d33b7e8d080c67a3e5efa1c8a661a30f60c2e59d8689c057af8ea42f2f714",
      "version": 28
    },
    "101.wake": {
      "generated": "2026-10-25T20:10:50.002413+00:00",
      "head": "05cd016b9ca9e7e5b724d71d6ed7711b1645b7ea24298628c0037c76644ccee4",
      "node": "101.wake",
      "snapshot_digest": "6330429436a199d5081d8e2d4f126ff62ad026feed6d9afe3446d228dc0d2153",
      "version": 44
    },
    "102.wake": {
      "generated": "2026-10-25T19:57:45.966104+00:00",
      "head": "124e53ee00522392f1df732dfcda0968e1c88e864e42edba3cae95f094f5be7f",
      "node": "102.wake",
      "snapshot_digest": "73b49c9129fc2ef796c59ee3062060d332163b576ab63102bc900e09d5597190",
      "version": 57
    },
    "103.wake": {
      "generated": "2026-10-25T20:12:40.999514+00:00",
      "head": "22d49a5ec4fa7b253b25d367b7bbb245fb505a852e12339903cf849442cf149f",
      "node": "103.wake",
      "snapshot_digest": "6bca06d2fe84772574ad8331989727d57a6326afd0d3d8e9fcf724506f431e18",
      "version": 39
    },
    "200.wake": {
      "generated": "2026-10-25T20:24:22.081790+00:00",
      "head": "d597c69234ad834bb039fd0eb8085a6b35ac69c488b9678abd1ab4d57906c1bb",
      "node": "200.wake",
      "snapshot_digest": "2ab823ea425d360a852714153f4622c4249d5f1f385b41be08b2178e1c720500",
      "version": 34
    },
    "201.wake": {
      "generated": "2026-10-25T20:22:43.794643+00:00",
      "head": "8b61f0202a5a3b85b50fbc9d2efe5d5a3fb61b2f5ba82c7daccf1782bb55a51f",
      "node": "201.wake",
      "snapshot_digest": "df7b3cc57f8ad4642bd95805ab8e1fbc690186901d96b5a78297c6e16b9a0576",
      "version": 40
    },
    "202.wake": {
      "generated": "2026-10-25T20:17:35.928362+00:00",
      "head": "950b13a1f58363546391c599f3cc4a40582771a239698560b8fd3d517793dae1",
      "node": "202.wake",
      "snapshot_digest": "00eb45878f0a39f3d0a7c7e609d0fd79e28be301cc9904e943b1dbf01e1809d5",
      "version": 55
    },
    "203.wake": {
      "generated": "2026-10-25T20:02:42.197503+00:00",
      "head": "4c2d419855a87fa9b4593bd70729aecec193d2315cfab3d50e2d9923e13cf20a",
      "node": "203.wake",
      "snapshot_digest": "456f87e77a359f47127c86c83e3d2a33dfdc289dc201772dcddd336d299a482a",
      "version": 31
    },
    "300.wake": {
      "generated": "2026-10-25T20:07:32.152412+00:00",
      "head": "e0b1941660c341fce8c26951e7e72d70f12aa070a7516d71a187a8d573e829e8",
      "node": "300.wake",
      "snapshot_digest": "9642041e1ecedca4194199efb7b948c689797acfef2f7a09ec16ce2d2bfcb850",
      "version": 35
    },
    "301.wake": {
      "generated": "2026-10-25T20:14:48.386311+00:00",
      "head": "5c665d8170dbdcf13a3b2f370182e317d58906085bbedd47400322fedaaa986f",
      "node": "301.wake",
      "snapshot_digest": "d270e6cb95e7f718883ae8e2fcc9627c28f2d188e3330ba6efbdc4b80e394d64",
      "version": 57
    },
    "302.wake": {
      "generated": "2026-10-25T20:01:46.446564+00:00",
      "head": "0a8b29aa14024bfe313890a3dd6b7033b8e40dd174ee0fab4e89038eb370a327",
      "node": "302.wake",
      "snapshot_digest": "f748e05ba6819ddc00aee816e996713393018e373374bc06a2082538a7f38198",
      "version": 39
    },
    "303.wake": {
      "generated": "2026-10-25T20:12:54.649981+00:00",
      "head": "a49984456197dcfd1a1bfb73f8efcb885aa1eeb2896f77d73c943016089b16f7",
      "node": "303.wake",
      "snapshot_digest": "24bd46adf212e3383909747a71af812bd8a4d3ebceedd6c24d5197bbb2ee6ea2",
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
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d356638656335613935363765343035/64.json)
- [evidence record](../reader-records/evidence/3230312e77616b653a3a736f757263652d363762393237663436346634346430/32.json)
- [notebooks record](../reader-records/notebooks/3330322e77616b653a3a6e6f7465626f6f6b2d70726f6a2d76616c75652d616c/69676e2d3030312d31.json)

For complete history, read the current `event_history.complete_url` in [the public export index](../wake-data.json); resolve that URL relative to the index, not this inspection directory. The stream may be packaged as gzip.
